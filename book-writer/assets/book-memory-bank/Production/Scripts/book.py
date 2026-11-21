#!/usr/bin/env python3
"""Book Tools: one command for checking and exporting a book.

    python3 book-memory-bank/Production/Scripts/book.py check

Commands:
    doctor               Show what is set up and what is optional
    check                Run the prose audit, continuity check, and research check
    audit [chapters]     Find AI-sounding patterns (for example: audit 3 7)
    voice FILE [FILE]    Learn the author's style from their own writing
    continuity           Check the story against the continuity ledger
    lint                 Run Vale and Harper if they are installed
    export [docx|epub|all] [--draft]   Build the finished book

Needs only Python 3.8+. Reading commands never change a chapter.
Pattern lists are adapted from open-source projects credited in
THIRD_PARTY_NOTICES.md.
"""

import argparse
import json
import os
import re
import shutil
import statistics
import subprocess
import sys
import tempfile
from collections import Counter, defaultdict
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
PROJECT = SCRIPT_DIR.parents[2]
CHAPTERS = PROJECT / "Chapters"
BANK = PROJECT / "book-memory-bank"
MANUSCRIPT = PROJECT / "Manuscript"
RESEARCH = PROJECT / "Research"
BASELINE = BANK / "Style" / "voice_baseline.json"
IGNORE = BANK / "Style" / "audit_ignore.txt"
LEDGER = BANK / "Core" / "continuity_ledger.md"
FLAG = "[NEED RESEARCH"
MIN_SAMPLE_WORDS = 300
GOOD_SAMPLE_WORDS = 1500

WORD = re.compile(r"[^\W\d_]+(?:['’-][^\W\d_]+)*")
ABBREVIATIONS = re.compile(r"\b(Mr|Mrs|Ms|Dr|Prof|St|Sr|Jr|vs|etc)\.")


# ---------------------------------------------------------------- Chapters

RETIRED = re.compile(r"^(old|draft|backup|bak|copy|wip|archive|prev|previous|v\d+|rev\d*)([\s_.-]*\d+)?$")


class BookError(Exception):
    """A problem the author can fix, reported without a traceback."""


def chapter_key(stem):
    name = stem.lower()
    match = re.match(r"^prologue(.*)$", name)
    if match:
        key, rest = (0, 0, 0), match.group(1)
    else:
        match = re.match(r"^chapter[\s_.-]*(\d+)(.*)$", name)
        if match:
            key, rest = (1, int(match.group(1)), 0), match.group(2)
        else:
            match = re.match(r"^interlude[\s_.-]*(\d+)(.*)$", name)
            if match:
                key, rest = (1, int(match.group(1)), 1), match.group(2)
            else:
                match = re.match(r"^epilogue(.*)$", name)
                if not match:
                    return None
                key, rest = (2, 0, 0), match.group(1)
    rest = re.sub(r"[()]", " ", rest).strip(" \t_.-")
    return "retired" if RETIRED.match(rest) else key


def label(key):
    section, number, order = key
    if section == 0:
        return "Prologue"
    if section == 2:
        return "Epilogue"
    return f"Interlude {number}" if order else f"Chapter {number}"


def parse_reference(text):
    text = (text or "").strip().lower().strip("*")
    if not text or text in {"-", "—", "–", "none", "n/a", "tbd", "open"}:
        return None
    if text.startswith("prologue"):
        return (0, 0, 0)
    if text.startswith("epilogue"):
        return (2, 0, 0)
    match = re.match(r"^interlude\s*(\d+)", text)
    if match:
        return (1, int(match.group(1)), 1)
    match = re.match(r"^(?:chapter|ch\.?)?\s*(\d+)", text)
    if match:
        return (1, int(match.group(1)), 0)
    return None


def book_chapters():
    if not CHAPTERS.is_dir():
        raise BookError(f"No Chapters folder found at {CHAPTERS}")
    found = {}
    for path in sorted(CHAPTERS.glob("*.md")):
        key = chapter_key(path.stem)
        if key is None or key == "retired":
            continue
        if key in found:
            raise BookError(f"Two files claim {label(key)}: {found[key].name} and {path.name}")
        found[key] = path
    return dict(sorted(found.items()))


def read_text(path):
    try:
        return path.read_text(encoding="utf-8-sig")
    except UnicodeDecodeError:
        raise BookError(f"{path.name} is not UTF-8 text. Save it as UTF-8 and try again.")
    except OSError as error:
        raise BookError(f"Cannot read {path}: {error.strerror}")


def select_chapters(requests):
    chapters = book_chapters()
    if not requests:
        return chapters
    chosen = {}
    for request in requests:
        key = parse_reference(request)
        if key not in chapters:
            raise BookError(f"Could not find chapter '{request}'")
        chosen[key] = chapters[key]
    return dict(sorted(chosen.items()))


# ---------------------------------------------------------------- Parsing prose


class Paragraph:
    def __init__(self, line, text, ends_scene=False):
        self.line = line
        self.text = text
        self.ends_scene = ends_scene
        self.narration, self.dialogue = split_dialogue(text)

    def line_at(self, position):
        return self.line + self.text.count("\n", 0, position)


def split_dialogue(text):
    """Returns narration and dialogue as same-length strings, blanking the other."""
    spans = []
    start = None
    for index, char in enumerate(text):
        if start is None and char in '“"':
            start = index
        elif start is not None and char in '”"':
            spans.append((start, index + 1))
            start = None
    if start is not None:
        spans.append((start, len(text)))
    if not spans:
        pattern = r"(?:(?<=^)|(?<=[\s(]))[‘'](?=\S).+?[’'](?=[\s.,!?;:)]|$)"
        spans = [match.span() for match in re.finditer(pattern, text, flags=re.S)]

    def blank(segment):
        return re.sub(r"[^\n]", " ", segment)

    narration, dialogue, cursor = [], [], 0
    for begin, end in spans:
        narration += [text[cursor:begin], blank(text[begin:end])]
        dialogue += [blank(text[cursor:begin]), text[begin:end]]
        cursor = end
    narration.append(text[cursor:])
    dialogue.append(blank(text[cursor:]))
    return "".join(narration), "".join(dialogue)


def parse_prose(text):
    text = re.sub(r"<!--.*?-->", lambda m: re.sub(r"[^\n]", " ", m.group(0)), text, flags=re.S)
    lines = text.splitlines()
    index = 0
    if lines and lines[0].strip() == "---" and len(lines) > 1 and re.match(r"^[\w-]+:", lines[1]):
        index = 1
        while index < len(lines) and lines[index].strip() not in {"---", "..."}:
            index += 1
        index += 1

    paragraphs, buffer, start, fence = [], [], 0, None

    def flush(ends_scene=False):
        nonlocal buffer
        if buffer:
            body = "\n".join(buffer)
            body = re.sub(r"\*", " ", body)
            body = re.sub(r"(?<!\w)_|_(?!\w)", " ", body)
            paragraphs.append(Paragraph(start, body))
            buffer = []
        if ends_scene and paragraphs:
            paragraphs[-1].ends_scene = True

    while index < len(lines):
        line = lines[index]
        stripped = line.strip()
        number = index + 1
        index += 1
        marker = re.match(r"^ {0,3}(`{3,}|~{3,})(.*)$", line)
        if fence:
            if marker and marker.group(1)[0] == fence[0] and len(marker.group(1)) >= len(fence) and not marker.group(2).strip():
                fence = None
        elif marker:
            flush()
            fence = marker.group(1)
        elif re.fullmatch(r"-{3,}|\*{3,}|_{3,}", stripped):
            flush(ends_scene=True)
        elif not stripped or stripped.startswith(("#", "|", "<")):
            flush()
        else:
            if not buffer:
                start = number
            buffer.append(re.sub(r"^\s*>\s?", "", line))
    flush(ends_scene=True)
    return paragraphs


def word_count(text):
    return len(WORD.findall(text))


def sentences(text):
    protected = ABBREVIATIONS.sub(lambda m: m.group(1) + "·", text)
    found = re.findall(r"[^.!?…]+(?:[.!?…]+[\"”’')]*|$)", protected)
    return [item.strip().replace("·", ".") for item in found if WORD.search(item)]


def snippet(text, begin, end, width=42):
    left = max(0, begin - width)
    right = min(len(text), end + width)
    body = re.sub(r"\s+", " ", text[left:right]).strip()
    return ("..." if left else "") + body + ("..." if right < len(text) else "")


# ---------------------------------------------------------------- Audit rules


class Rule:
    def __init__(self, id, title, pattern, scope, limit, fix):
        self.id, self.title, self.scope, self.limit, self.fix = id, title, scope, limit, fix
        self.regex = re.compile(pattern, re.IGNORECASE | re.MULTILINE)


BODY_CUES = (
    r"jaw (?:clenched|tightened|set)|fists? clenched|chest tightened|stomach (?:dropped|twisted|churned)"
    r"|heart (?:pounded|hammered|raced)|breath (?:hitched|caught)|throat tightened"
    r"|a chill (?:ran|crept)|hands trembled|eyes widened|expression darkened|furrowed brow"
    r"|squared (?:his|her|their) shoulders|smile (?:didn['’]t|did not) reach|something cold (?:settled|crawled|spread)"
    r"|a wave of \w+ washed|a pang of|a flicker of|the ghost of a smile|breath (?:he|she|they|I) (?:didn['’]t|hadn['’]t)"
)

# Counted per 1,000 words, then compared with the author's own rate when known.
RATE_RULES = [
    Rule("em_dash", "Em dashes in narration", r"—|(?<=\w)--(?=\w)|\s--\s|(?<=\w) – (?=\w)", "narration", 0,
         "Use a period, comma, or colon, or rewrite the sentence."),
    Rule("dialogue_dash", "Em dashes inside dialogue", r"—(?=\s*[^\W\d_]{2,})", "dialogue", 0,
         "Keep dashes for a speaker being cut off. Rewrite other uses."),
    Rule("not_x_but_y", "'Not X but Y' constructions",
         r"\bnot\b[^.!?\n]{1,45},\s*but\b|\bnot (?:just|only|merely|simply)\b"
         r"|\b(?:wasn['’]t|isn['’]t|weren['’]t)\b[^.!?\n]{1,40}[.;]\s+(?:it|he|she|they) (?:was|were|is)\b",
         "narration", 1.5, "State the true thing directly unless the reader really believed X."),
    Rule("tricolon", "Lists of three", r"\b[^\W\d_]+, [^\W\d_]+,? and [^\W\d_]+\b", "narration", 3,
         "Try two items, four items, or the single strongest one."),
    Rule("participle_tail", "Significance tails (', reflecting...')",
         r",\s(?:reflecting|highlighting|underscoring|mirroring|emphasizing|emphasising|echoing|signaling|signalling|symbolizing|symbolising)\b",
         "narration", 1, "End the sentence earlier and let the image work."),
    Rule("un_adjective", "'Unspoken, unreadable' adjectives",
         r"\bun(?:spoken|nameable|readable|deniable|bidden|mistakable|flinching|settling)\b", "narration", 1,
         "Name what the POV character actually saw."),
    Rule("kind_of", "'The kind of X that' framing", r"\bthe (?:kind|sort|type) of \w+ (?:that|who|which)\b", "narration", 1,
         "Name the specific thing."),
    Rule("body_cliche", "Stock body reactions", BODY_CUES, "narration", 2,
         "Use an action specific to this character, or just name the emotion plainly."),
    Rule("silence_cliche", "'Hung in the air' phrases",
         r"\b(?:hung|sat|lingered) (?:in the air|between them)\b|\bsilence (?:stretched|hung|settled)\b|\bthe air was thick\b|\blanded like\b",
         "narration", 0.5, "Go straight to the next thing anyone did or said."),
    Rule("beat_cliche", "'A beat' and 'something shifted' phrases",
         r"\ba beat passed\b|\bfor a beat\b|\bsomething (?:shifted|flickered)\b|\blet out a (?:breath|sigh)\b|\bfor what felt like\b|\bthe moment stretched\b",
         "narration", 0.5, "Show the specific change, or cut the pause."),
    Rule("gerund_realization", "'Watching him, she realized' openers",
         r"(?:^|[.!?]\s+)(?:Watching|Turning|Standing|Looking|Sitting|Staring|Listening|Holding|Walking)\b[^,.\n]{0,40},\s(?:he|she|they|I)\s(?:realized|realised|wondered|thought|understood|knew|felt)\b",
         "narration", 0.5, "Make the action its own sentence, or cut the thought."),
    Rule("ai_vocabulary", "Overused AI words",
         r"\b(?:delve[sd]?|delving|tapestry|testament|underscore[sd]?|pivotal|intricate|intricacies|meticulous(?:ly)?"
         r"|showcas(?:e|es|ed|ing)|fostering|leverag(?:e|es|ed|ing)|interplay|bolstered|garner(?:ed|s)?|navigat(?:e|ing) the complexities)\b",
         "narration", 0.5, "Use the plain word a person would say."),
    Rule("fancy_tag", "Fancy dialogue tags",
         r"[\"”]\s*,?\s*(?:he|she|they|I|[A-Z]\w+)\s(?:murmured|breathed|exhaled|rasped|mused|pondered|intoned|purred)\b",
         "all", 1.5, "Use 'said', an action beat, or no tag."),
    Rule("adverb_tag", "Adverbs on dialogue tags",
         r"[\"”]\s*,?\s*(?:he|she|they|I|[A-Z]\w+)\s(?:said|asked|replied|whispered|muttered)\s\w+ly\b", "all", 0.5,
         "Let the line or an action carry the tone."),
    Rule("therapy_speak", "Therapy-speak in dialogue",
         r"\bwhat I['’]m hearing\b|\bthat['’]s valid\b|\bhold space\b|\bI need you to hear\b|\bprocess(?:ing)? (?:this|that)\b|\bI appreciate you\b",
         "dialogue", 0.5, "Let people deflect, misread, or change the subject."),
    Rule("filter_words", "Filter words",
         r"\b(?:noticed|realized|realised|wondered|seemed|sensed|observed)\b", "narration", 8,
         "Show the thing directly instead of the character perceiving it."),
    Rule("intensifiers", "Empty intensifiers",
         r"\b(?:very|really|quite|actually|basically|literally|simply|totally|extremely|incredibly|truly|suddenly|somehow)\b",
         "narration", 8, "Cut the word or choose a stronger one."),
]

# Worth reading every time they appear.
ALWAYS_RULES = [
    Rule("chatbot", "Chatbot text left in the book",
         r"\bgreat question\b|\bI hope this helps\b|\blet me know if\b|\bhere(?:'|’| i)s? the (?:revised|updated|next|rewritten)\b|\bas an AI\b|\bin this (?:scene|chapter),",
         "narration", 0, "Delete it."),
    Rule("scaffolding", "Planning notes left in the book",
         r"\[(?:beat|turn|end here|todo|insert[^\]]*)\]|\bTODO\b|\binciting incident\b|\bcharacter arc\b|\brising tension\b",
         "narration", 0, "Delete it, or turn it into story."),
    Rule("explained_subtext", "Narrator explains the subtext",
         r"\bwhat (?:she|he|they) meant was\b|\b(?:she|he) was really saying\b|\bthey were really saying\b|\bit was (?:her|his|their) way of\b|\ba gesture that meant\b|\bas close as (?:she|he|they) (?:came|would come) to\b",
         "narration", 0, "Cut the explanation and trust the action."),
    Rule("theme_statement", "Theme stated outright",
         r"\b(?:she|he|they|I) (?:understood|realized|realised|knew),? (?:finally,? |at last,? |now,? |then,? )?that\b[^.!?\n]{0,80}\b(?:grief|love|forgiveness|memory|truth|home|loss|hope)\b"
         r"|\b(?:grief|love|forgiveness|memory|truth|loss|hope) (?:was|is) (?:not|never|a kind of|something)\b",
         "narration", 0, "Replace the idea with a concrete moment."),
    Rule("label_on_cue", "Emotion named right after a body cue",
         r"\b(?:jaw|chest|stomach|throat|breath|heart)\b[^.\n]{0,60}\.\s+[^.\n]{0,40}\b(?:anger|angry|fear|afraid|grief|relief|shame|panic|dread|rage)\b",
         "narration", 0, "Keep one half: the action or the plain emotion."),
    Rule("as_you_know", "'As you know' exposition",
         r"\bas you (?:know|remember|recall|well know)\b|\bneed I remind you\b|\byou['’]ll recall\b", "dialogue", 0,
         "Give one character a real reason not to know, or move it to narration."),
]

WISDOM_CLOSER = re.compile(
    r"\b(?:for now|would have to be enough|would have to do|maybe that was (?:enough|the point)|and that was enough|it was a start|understood now|knew then)\b[^.!?]{0,12}[.!?\"”]*\s*$",
    re.IGNORECASE,
)
DEFAULT_NAMES = re.compile(r"\b(Elara|Elias|Kael|Kaelen|Seraphina|Lyra|Aris|Thorne|Voss|Blackwood|Eldora)\b")
STOPWORDS = set(
    "a an and are as at be but by for from had has have he her his i if in into is it its me my no not of on or our "
    "she so than that the their them then there they this to up was we were what when which who will with would you".split()
)
RATE_RULE_IDS = {rule.id for rule in RATE_RULES}


def audit_ignores():
    if not IGNORE.is_file():
        return set()
    entries = set()
    for line in read_text(IGNORE).splitlines():
        line = line.split("#", 1)[0].strip()
        if line:
            entries.add(line.lower())
    return entries


def load_baseline():
    if not BASELINE.is_file():
        return None
    try:
        data = json.loads(read_text(BASELINE))
    except ValueError:
        raise BookError(f"{BASELINE.name} is damaged. Run the voice command again.")
    return data if isinstance(data.get("rates"), dict) else None


def rate_limit(rule, baseline):
    if not baseline or rule.id not in baseline["rates"]:
        return rule.limit
    author = baseline["rates"][rule.id] * 1.25
    return round(max(author, rule.limit * 0.5), 2)


def scoped(paragraph, scope):
    return {"narration": paragraph.narration, "dialogue": paragraph.dialogue, "all": paragraph.text}[scope]


def collect(rule, paragraphs):
    hits = []
    for paragraph in paragraphs:
        text = scoped(paragraph, rule.scope)
        for match in rule.regex.finditer(text):
            hits.append({"line": paragraph.line_at(match.start()),
                         "quote": snippet(paragraph.text, match.start(), match.end())})
    return hits


def measure_rates(paragraphs):
    words = sum(word_count(item.text) for item in paragraphs) or 1
    return {rule.id: round(len(collect(rule, paragraphs)) * 1000 / words, 2) for rule in RATE_RULES}


def sentence_variation(paragraphs):
    lengths = [word_count(item) for paragraph in paragraphs for item in sentences(paragraph.text)]
    if len(lengths) < 20 or not statistics.mean(lengths):
        return None
    return round(statistics.pstdev(lengths) / statistics.mean(lengths), 2)


def audit_chapter(key, path, baseline, ignores):
    paragraphs = parse_prose(read_text(path))
    words = sum(word_count(item.text) for item in paragraphs)
    findings = []
    per_thousand = 1000 / (words or 1)

    def add(rule_id, level, title, count, detail, fix, hits):
        if rule_id not in ignores:
            findings.append({"rule": rule_id, "level": level, "title": title, "count": count,
                             "detail": detail, "fix": fix, "hits": hits})

    for rule in ALWAYS_RULES:
        hits = collect(rule, paragraphs)
        if hits:
            add(rule.id, "FIX", rule.title, len(hits), f"{len(hits)} found", rule.fix, hits)

    for rule in RATE_RULES:
        hits = collect(rule, paragraphs)
        if not hits:
            continue
        rate = len(hits) * per_thousand
        limit = rate_limit(rule, baseline)
        if rate <= limit:
            continue
        level = "FIX" if limit == 0 or rate > limit * 2 else "REVIEW"
        source = "your usual rate" if baseline and rule.id in baseline["rates"] else "limit"
        add(rule.id, level, rule.title, len(hits), f"{rate:.1f} per 1,000 words ({source}: {limit:g})", rule.fix, hits)

    closers = []
    for paragraph in paragraphs:
        if paragraph.ends_scene and WISDOM_CLOSER.search(paragraph.narration.rstrip()):
            last = len(paragraph.text.rstrip())
            closers.append({"line": paragraph.line_at(max(last - 1, 0)), "quote": snippet(paragraph.text, max(last - 40, 0), last)})
    if closers:
        add("wisdom_closer", "FIX", "Scene ends on a wisdom line", len(closers), f"{len(closers)} found",
            "End on the last concrete action or image.", closers)

    variation = sentence_variation(paragraphs)
    floor = 0.35
    if baseline and baseline.get("sentence_variation"):
        floor = round(min(baseline["sentence_variation"] * 0.75, 0.45), 2)
    if variation is not None and variation < floor:
        add("rhythm", "REVIEW", "Sentence lengths are too even", 1, f"variation {variation} (aim for {floor}+)",
            "Let one sentence run long and cut another short. Do not make every sentence a fragment.", [])

    runs = []
    openers = []
    for paragraph in paragraphs:
        for item in sentences(paragraph.text):
            tokens = [word.lower() for word in WORD.findall(item)]
            openers.append((" ".join(tokens[:2]), paragraph.line))
    index = 0
    while index + 2 < len(openers):
        if openers[index][0] and openers[index][0] == openers[index + 1][0] == openers[index + 2][0]:
            runs.append({"line": openers[index][1], "quote": f"Three sentences open with '{openers[index][0]}'"})
            index += 3
        else:
            index += 1
    if len(runs) > 1:
        add("anaphora", "REVIEW", "Repeated sentence openings", len(runs), f"{len(runs)} runs",
            "Keep one deliberate run per chapter and vary the rest.", runs)

    return {"chapter": label(key), "words": words, "findings": findings, "paragraphs": paragraphs}


def repeated_phrases(chapters, ignores, size=5, min_chapters=3):
    if "repeated_phrase" in ignores:
        return []
    seen = defaultdict(set)
    for result in chapters:
        for paragraph in result["paragraphs"]:
            for sentence in sentences(paragraph.narration):
                tokens = [word.lower() for word in WORD.findall(sentence)]
                for index in range(len(tokens) - size + 1):
                    phrase = tokens[index:index + size]
                    if sum(word not in STOPWORDS for word in phrase) >= 3:
                        seen[" ".join(phrase)].add(result["chapter"])
    repeated = {phrase: names for phrase, names in seen.items() if len(names) >= min_chapters}
    kept = []
    for phrase in sorted(repeated, key=lambda item: (-len(repeated[item]), item)):
        if not any(len(set(phrase.split()) & set(other.split())) >= 3 for other in kept):
            kept.append(phrase)
    return [(phrase, len(repeated[phrase])) for phrase in kept[:5]]


def book_findings(results, ignores):
    notes = []
    if len(results) >= 4:
        lengths = [item["words"] for item in results]
        if statistics.mean(lengths):
            variation = statistics.pstdev(lengths) / statistics.mean(lengths)
            if variation < 0.2 and "chapter_length" not in ignores:
                notes.append("Chapters are all close to the same length. Real books usually vary more.")
        one_line = 0
        for item in results:
            if item["paragraphs"] and len(sentences(item["paragraphs"][-1].text)) == 1:
                one_line += 1
        if one_line / len(results) > 0.5 and "chapter_endings" not in ignores:
            notes.append(f"{one_line} of {len(results)} chapters end on a one-sentence paragraph. Vary the endings.")
    for phrase, count in repeated_phrases(results, ignores):
        notes.append(f"'{phrase}' appears in {count} chapters. Keep the strongest use.")
    names = Counter()
    for item in results:
        for paragraph in item["paragraphs"]:
            names.update(DEFAULT_NAMES.findall(paragraph.text))
    for name, _ in names.most_common():
        if name.lower() not in ignores:
            notes.append(f"'{name}' is a name AI models overuse. If you chose it, add it to audit_ignore.txt.")
    return notes


def run_audit(requests):
    chapters = select_chapters(requests)
    if not chapters:
        raise BookError("No chapters found yet. Add a file such as Chapters/Chapter01.md.")
    baseline = load_baseline()
    ignores = audit_ignores()
    results = [audit_chapter(key, path, baseline, ignores) for key, path in chapters.items()]
    return results, book_findings(results, ignores), baseline


def looks_non_english(results):
    tokens = [word.lower() for item in results for paragraph in item["paragraphs"] for word in WORD.findall(paragraph.text)]
    return len(tokens) >= 100 and sum(word in STOPWORDS for word in tokens) / len(tokens) < 0.15


def render_audit(results, notes, baseline, show_all=False):
    words = sum(item["words"] for item in results)
    fixes = sum(1 for item in results for finding in item["findings"] if finding["level"] == "FIX")
    reviews = sum(1 for item in results for finding in item["findings"] if finding["level"] == "REVIEW")
    out = [f"Prose Audit: {len(results)} chapter(s), {words:,} words",
           "These are patterns to read, not proof of AI writing. Nothing was changed."]
    out.append("Compared with your own writing." if baseline else "Using default limits. Run the voice command to compare with your own style.")
    if looks_non_english(results):
        out.append("Note: these checks are built for English, so results for this text may not be useful.")
    out.append(f"\nSummary: {fixes} to fix, {reviews} to review")
    for item in results:
        if not item["findings"]:
            continue
        out.append(f"\n{item['chapter']} ({item['words']:,} words)")
        for finding in sorted(item["findings"], key=lambda entry: entry["level"]):
            out.append(f"  {finding['level']:<6} {finding['title']}: {finding['detail']}")
            out.append(f"         {finding['fix']}")
            hits = finding["hits"] if show_all else finding["hits"][:3]
            for hit in hits:
                out.append(f"         line {hit['line']}: {hit['quote']}")
            if len(finding["hits"]) > len(hits):
                out.append(f"         and {len(finding['hits']) - len(hits)} more (use --all)")
    if notes:
        out.append("\nWhole book")
        out += [f"  - {note}" for note in notes]
    if not fixes and not reviews and not notes:
        out.append("\nNo patterns found. If it reads well, leave it alone.")
    return "\n".join(out)


def command_audit(args):
    results, notes, baseline = run_audit(args.chapters)
    if args.json:
        payload = {"chapters": [{key: value for key, value in item.items() if key != "paragraphs"} for item in results],
                   "book": notes, "uses_author_baseline": bool(baseline)}
        print(json.dumps(payload, ensure_ascii=False, indent=2))
        return 0
    report = render_audit(results, notes, baseline, args.all)
    print(report)
    if args.save:
        RESEARCH.mkdir(exist_ok=True)
        target = RESEARCH / "prose_audit.md"
        write_atomic(target, "# Prose Audit\n\n```text\n" + render_audit(results, notes, baseline, True) + "\n```\n")
        print(f"\nSaved to {target}")
    return 0


# ---------------------------------------------------------------- Voice


def command_voice(args):
    paragraphs = []
    names = []
    for item in args.files:
        path = Path(item)
        if not path.is_absolute():
            path = Path.cwd() / path
        if not path.is_file():
            raise BookError(f"Could not find sample file: {item}")
        paragraphs += parse_prose(read_text(path))
        names.append(path.name)
    words = sum(word_count(item.text) for item in paragraphs)
    if words < MIN_SAMPLE_WORDS:
        raise BookError(f"The sample has {words} words. Please use at least {MIN_SAMPLE_WORDS}, ideally {GOOD_SAMPLE_WORDS}+.")
    baseline = {"version": 1, "sample_words": words, "samples": names,
                "sentence_variation": sentence_variation(paragraphs), "rates": measure_rates(paragraphs)}
    write_atomic(BASELINE, json.dumps(baseline, indent=2) + "\n")
    print(f"Learned your style from {words:,} words. Saved to {BASELINE.relative_to(PROJECT)}")
    if words < GOOD_SAMPLE_WORDS:
        print(f"Tip: a sample of {GOOD_SAMPLE_WORDS:,}+ words gives more reliable results.")
    print(f"Your em dashes: {baseline['rates']['em_dash']} per 1,000 words in narration.")
    return 0


# ---------------------------------------------------------------- Continuity

COLORS = set("amber black blond blonde blue brown chestnut copper dark gold golden gray green grey hazel red silver violet white".split())
NOT_NAMES = set(
    "about after again also always another before being both could down during each even every first from have here "
    "just last later like many more most much never next nothing once only other over perhaps same since some still "
    "such than that their them then there these they this those through under until very were what when where which "
    "while with would chapter prologue epilogue interlude monday tuesday wednesday thursday friday saturday sunday".split()
)


def parse_tables(text):
    tables, section, header = defaultdict(list), None, None
    for line in text.splitlines():
        stripped = line.strip()
        if stripped.startswith("## "):
            section, header = stripped[3:].strip().lower(), None
        elif section and stripped.startswith("|"):
            cells = [cell.strip() for cell in stripped.strip("|").split("|")]
            if header is None:
                header = [cell.lower() for cell in cells]
            elif not all(re.fullmatch(r":?-+:?", cell) for cell in cells):
                row = dict(zip(header, cells))
                first = cells[0] if cells else ""
                if first and not first.startswith("["):
                    tables[section].append(row)
        else:
            header = None
    return tables


def split_list(text):
    return [item.strip() for item in (text or "").split(",") if item.strip() and not item.strip().startswith("[")]


def contains(term, text):
    return re.search(r"(?<!\w)" + re.escape(term) + r"(?!\w)", text, re.IGNORECASE)


def edit_distance(first, second):
    previous = list(range(len(second) + 1))
    for row, left in enumerate(first, 1):
        current = [row]
        for column, right in enumerate(second, 1):
            current.append(min(previous[column] + 1, current[-1] + 1, previous[column - 1] + (left != right)))
        previous = current
    return previous[-1]


def check_continuity():
    """Returns (errors, warnings, notes). Uses the ledger as the source of truth."""
    errors, warnings, notes = [], [], []
    if not LEDGER.is_file():
        return errors, warnings, ["No continuity ledger found, so continuity was not checked."]
    tables = parse_tables(read_text(LEDGER))
    chapters = {key: parse_prose(read_text(path)) for key, path in book_chapters().items()}
    full = {key: "\n".join(item.text for item in value) for key, value in chapters.items()}

    def reference(row, column, owner):
        raw = row.get(column, "")
        if not raw or raw.startswith("["):
            return None
        key = parse_reference(raw)
        if key is None and raw.strip().lower() not in {"-", "—", "–", "none", "n/a", "tbd", "open"}:
            errors.append(f"{owner}: cannot read chapter '{raw}' in '{column}'. Use a form like 'Ch 3'.")
        return key

    known = set()
    for row in tables.get("characters", []):
        name = row.get("name", "")
        aliases = split_list(row.get("aliases"))
        terms = [name] + aliases
        for term in terms:
            known.update(token.lower() for token in WORD.findall(term))
        death = reference(row, "dies in", name)
        if death is None:
            continue
        for key, paragraphs in chapters.items():
            if key <= death:
                continue
            for paragraph in paragraphs:
                match = next((found for found in (contains(term, paragraph.narration) for term in terms) if found), None)
                if match:
                    line = paragraph.line_at(match.start())
                    warnings.append(f"{label(key)}, line {line}: {name} appears after dying in {label(death)}. Is this a memory or flashback?")
                    break

    for row in tables.get("promises", []):
        title = row.get("promise", "")
        planted, paid = reference(row, "planted in", title), reference(row, "pays off in", title)
        if planted and paid and paid < planted:
            errors.append(f"Promise '{title}' pays off in {label(paid)} before it is planted in {label(planted)}.")
        if planted is None:
            warnings.append(f"Promise '{title}' has no planted chapter.")
        if paid is None:
            notes.append(f"Promise '{title}' has no payoff yet.")
        keywords = split_list(row.get("keywords"))
        for where, key in (("planted in", planted), ("paid off in", paid)):
            if key in full and keywords and not any(contains(word, full[key]) for word in keywords):
                warnings.append(f"Promise '{title}' should be {where} {label(key)}, but its keywords are not there.")

    for row in tables.get("secrets", []):
        title, person = row.get("secret", ""), row.get("character", "")
        learned = reference(row, "learns in", f"{title} ({person})")
        keywords = split_list(row.get("keywords"))
        if learned is None or not person or not keywords:
            continue
        for key, text in full.items():
            if key >= learned:
                continue
            for sentence in sentences(text):
                if contains(person, sentence) and any(contains(word, sentence) for word in keywords):
                    warnings.append(f"{label(key)}: {person} is linked to '{title}' before learning it in {label(learned)}: {sentence[:90]}")
                    break

    grouped = defaultdict(list)
    for row in tables.get("facts", []):
        subject, attribute = row.get("subject", ""), row.get("attribute", "")
        since = reference(row, "since", f"{subject} {attribute}") or (0, 0, 0)
        grouped[(subject, attribute.lower())].append((since, row.get("value", "")))
    for (subject, attribute), values in grouped.items():
        values.sort(key=lambda item: item[0])
        for (first, one), (second, two) in zip(values, values[1:]):
            if first == second and one.lower() != two.lower():
                errors.append(f"{subject}'s {attribute} is both '{one}' and '{two}' from the same point in the story.")
        noun = {"eyes": r"eyes?", "eye color": r"eyes?", "eye colour": r"eyes?", "hair": r"hair"}.get(attribute)
        if not noun:
            continue
        for key, text in full.items():
            current = next((value for since, value in reversed(values) if since <= key), None)
            canon = {word.lower() for word in WORD.findall(current or "")} & COLORS
            if not canon:
                continue
            for sentence in sentences(text):
                if not contains(subject, sentence) or not re.search(rf"\b{noun}\b", sentence, re.IGNORECASE):
                    continue
                stated = {word.lower() for word in WORD.findall(sentence)} & COLORS
                normalized = {"grey" if word == "gray" else word for word in stated}
                allowed = {"grey" if word == "gray" else word for word in canon}
                if normalized and not normalized & allowed:
                    warnings.append(f"{label(key)}: {subject}'s {attribute} should be {current}: {sentence[:90]}")

    if known:
        lower_words = {word for text in full.values() for word in re.findall(r"\b[a-z][a-z'’-]+\b", text)}
        suspects = {}
        for key, text in full.items():
            for token in re.findall(r"\b[A-Z][a-z]{3,}\b", text):
                word = token.lower()
                if word in known or word in lower_words or word in NOT_NAMES or word in suspects:
                    continue
                allowed = 2 if len(word) >= 8 else 1
                match = next((name for name in sorted(known) if len(name) >= 4 and name[0] == word[0]
                              and edit_distance(word, name) <= allowed), None)
                if match:
                    suspects[word] = (token, match, key)
        for token, match, key in suspects.values():
            warnings.append(f"{label(key)}: '{token}' looks like a misspelling of '{match.title()}'.")
    return errors, warnings, notes


def render_continuity(errors, warnings, notes):
    out = [f"Continuity: {len(errors)} problem(s), {len(warnings)} to check"]
    out += [f"  PROBLEM {item}" for item in errors]
    out += [f"  CHECK   {item}" for item in warnings]
    out += [f"  NOTE    {item}" for item in notes]
    if not errors and not warnings and not notes:
        out.append("  Everything in the ledger agrees with the chapters.")
    return "\n".join(out)


def command_continuity(_args):
    errors, warnings, notes = check_continuity()
    print(render_continuity(errors, warnings, notes))
    return 1 if errors else 0


# ---------------------------------------------------------------- Check, doctor, lint


def research_flags():
    found = []
    for key, path in book_chapters().items():
        for number, line in enumerate(read_text(path).splitlines(), 1):
            if FLAG in line:
                found.append(f"{label(key)}, line {number}")
    return found


def command_check(_args):
    results, notes, baseline = run_audit([])
    print(render_audit(results, notes, baseline))
    errors, warnings, continuity_notes = check_continuity()
    print("\n" + render_continuity(errors, warnings, continuity_notes))
    flags = research_flags()
    print(f"\nResearch: {len(flags)} open [NEED RESEARCH] flag(s)")
    for item in flags[:10]:
        print(f"  {item}")
    if len(flags) > 10:
        print(f"  and {len(flags) - 10} more")
    return 1 if errors else 0


OPTIONAL_TOOLS = [
    ("pandoc", "Word and EPUB export", "https://pandoc.org/installing.html"),
    ("vale", "Style checks in your editor", "https://vale.sh/docs/install"),
    ("harper-cli", "Private offline grammar checks", "https://github.com/Automattic/harper"),
    ("epubcheck", "EPUB validation before upload", "https://www.w3.org/publishing/epubcheck/"),
]


def command_doctor(_args):
    print(f"Book Tools (Python {sys.version_info.major}.{sys.version_info.minor})")
    print(f"Project: {PROJECT}\n")
    for name, path in (("Chapters", CHAPTERS), ("Memory bank", BANK), ("Continuity ledger", LEDGER), ("Voice baseline", BASELINE)):
        print(f"  {'ok' if path.exists() else '--':<3} {name}")
    if CHAPTERS.is_dir():
        print(f"\n  {len(book_chapters())} chapter(s) found")
    print("\nOptional tools (everything else works without them):")
    for command, purpose, url in OPTIONAL_TOOLS:
        if shutil.which(command):
            print(f"  ok  {command}: {purpose}")
        else:
            print(f"  --  {command}: {purpose} ({url})")
    return 0


def command_lint(_args):
    chapters = book_chapters()
    if not chapters:
        raise BookError("No chapters found yet.")
    ran = False
    if shutil.which("vale"):
        ran = True
        print("Vale\n", flush=True)
        config = SCRIPT_DIR.parent / "Vale" / "vale.ini"
        subprocess.run(["vale", f"--config={config}", "--no-exit"] + [str(path) for path in chapters.values()], check=False)
    if shutil.which("harper-cli"):
        ran = True
        print("\nHarper\n", flush=True)
        for path in chapters.values():
            subprocess.run(["harper-cli", "lint", "--no-color", str(path)], check=False)
    if not ran:
        print("Neither Vale nor Harper is installed. They are optional. Run the doctor command for links.")
    return 0


# ---------------------------------------------------------------- Export


def write_atomic(path, content):
    path.parent.mkdir(parents=True, exist_ok=True)
    descriptor, temporary = tempfile.mkstemp(dir=str(path.parent), prefix=".tmp")
    try:
        with os.fdopen(descriptor, "w", encoding="utf-8", newline="\n") as handle:
            handle.write(content)
        os.replace(temporary, str(path))
    finally:
        if os.path.exists(temporary):
            os.unlink(temporary)


def run_combine(strict):
    if os.name == "nt":
        command = ["powershell", "-NoProfile", "-ExecutionPolicy", "Bypass", "-File", str(SCRIPT_DIR / "combine_chapters.ps1")]
        command += ["-Strict"] if strict else []
    else:
        command = ["bash", str(SCRIPT_DIR / "combine_chapters.sh")] + (["--strict"] if strict else [])
    status = subprocess.run(command, check=False).returncode
    if status == 3:
        raise BookError("Open research flags remain. Resolve them, or use --draft for a review copy.")
    if status:
        raise BookError("The chapters could not be combined. Your previous files were kept.")


def brief_field(name):
    brief = BANK / "Core" / "projectbrief.md"
    if not brief.is_file():
        return None
    match = re.search(rf"^\*\*{name}\*\*:\s*(.+)$", read_text(brief), flags=re.M)
    if not match or match.group(1).strip().startswith("["):
        return None
    return match.group(1).strip()


def build_docx(draft):
    flags = ["--no-open"] + (["--draft"] if draft else [])
    if os.name == "nt":
        command = ["cmd", "/c", str(SCRIPT_DIR / "generate_docx.bat")] + flags
    else:
        command = ["bash", str(SCRIPT_DIR / "generate_docx.sh")] + flags
    status = subprocess.run(command, check=False).returncode
    if status:
        raise BookError("The Word export failed. Your previous document was kept.")


def build_epub(draft):
    run_combine(strict=not draft)
    target = MANUSCRIPT / ("BOOK_DRAFT.epub" if draft else "BOOK.epub")
    descriptor, temporary = tempfile.mkstemp(dir=str(MANUSCRIPT), prefix=".book", suffix=".epub")
    os.close(descriptor)
    try:
        title = brief_field("Title") or PROJECT.name
        command = ["pandoc", str(MANUSCRIPT / "COMBINED.md"), "-o", temporary, "--from", "markdown", "--to", "epub3",
                   "--toc", "--split-level=1", f"--lua-filter={SCRIPT_DIR / 'page_breaks.lua'}",
                   f"--metadata=title:{title}", f"--metadata=lang:{brief_field('Language') or 'en'}"]
        author = brief_field("Author")
        if author:
            command.append(f"--metadata=author:{author}")
        for name in ("cover.jpg", "cover.jpeg", "cover.png"):
            if (MANUSCRIPT / name).is_file():
                command.append(f"--epub-cover-image={MANUSCRIPT / name}")
                break
        if subprocess.run(command, check=False).returncode:
            raise BookError("The EPUB export failed. Your previous file was kept.")
        if shutil.which("epubcheck"):
            print("Validating with EPUBCheck...")
            if subprocess.run(["epubcheck", temporary], check=False).returncode:
                raise BookError("EPUBCheck found errors. Your previous file was kept.")
        os.replace(temporary, str(target))
    finally:
        if os.path.exists(temporary):
            os.unlink(temporary)
    print(f"EPUB ready: {target}")


def command_export(args):
    if not shutil.which("pandoc"):
        raise BookError("Export needs Pandoc: https://pandoc.org/installing.html. Your files were not changed.")
    MANUSCRIPT.mkdir(exist_ok=True)
    if args.format in {"docx", "all"}:
        build_docx(args.draft)
    if args.format in {"epub", "all"}:
        build_epub(args.draft)
    return 0


# ---------------------------------------------------------------- Main


def main(argv=None):
    for stream in (sys.stdout, sys.stderr):
        if hasattr(stream, "reconfigure"):
            stream.reconfigure(encoding="utf-8", errors="replace")
    parser = argparse.ArgumentParser(prog="book.py", description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    commands = parser.add_subparsers(dest="command")
    commands.add_parser("doctor", help="show what is set up").set_defaults(run=command_doctor)
    commands.add_parser("check", help="run every book check").set_defaults(run=command_check)
    audit = commands.add_parser("audit", help="find AI-sounding patterns")
    audit.add_argument("chapters", nargs="*", help="chapter numbers, Prologue, or Epilogue (default: all)")
    audit.add_argument("--all", action="store_true", help="show every example")
    audit.add_argument("--json", action="store_true", help="print JSON for other tools")
    audit.add_argument("--save", action="store_true", help="save to Research/prose_audit.md")
    audit.set_defaults(run=command_audit)
    voice = commands.add_parser("voice", help="learn the author's style")
    voice.add_argument("files", nargs="+", help="text or Markdown files the author wrote")
    voice.set_defaults(run=command_voice)
    commands.add_parser("continuity", help="check the continuity ledger").set_defaults(run=command_continuity)
    commands.add_parser("lint", help="run Vale and Harper if installed").set_defaults(run=command_lint)
    export = commands.add_parser("export", help="build Word and EPUB files")
    export.add_argument("format", nargs="?", choices=["docx", "epub", "all"], default="docx")
    export.add_argument("--draft", action="store_true", help="allow research flags and write a draft copy")
    export.set_defaults(run=command_export)

    args = parser.parse_args(argv)
    if not args.command:
        parser.print_help()
        return 0
    try:
        return args.run(args)
    except BookError as error:
        print(f"Error: {error}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())
