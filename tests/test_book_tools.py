#!/usr/bin/env python3
"""Tests Book Tools against throwaway book projects. Uses only the standard library."""

import json
import os
import shutil
import subprocess
import sys
import tempfile
import unittest
import zipfile
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
BANK = REPO / "book-writer" / "assets" / "book-memory-bank"

CLEAN = (
    "Tomas carried the crate up from the harbor before the rain came in. His brother had left the van "
    "running, which cost money they did not have, so he reached through the window and turned it off. "
    "Nobody thanked him. The fish market was already closing, and the woman at the ice machine wanted "
    "cash. He paid her with the coins from the ashtray and asked about the Friday delivery. She laughed "
    "at him. It rained for an hour after that. "
)
SLOP = (
    "She stood at the window — watching the rain — and something shifted. The silence stretched between "
    "them. Her jaw tightened. Panic rose in her, cold and absolute. It was her way of saying goodbye. "
    "She understood, finally, that grief was something you carried. The room was a testament to the "
    "intricate tapestry of memory. Here is the revised scene. "
)


class Book:
    def __init__(self):
        self.root = Path(tempfile.mkdtemp())
        (self.root / "Chapters").mkdir()
        shutil.copytree(BANK, self.root / "book-memory-bank")
        self.script = self.root / "book-memory-bank" / "Production" / "Scripts" / "book.py"

    def chapter(self, name, text):
        (self.root / "Chapters" / f"{name}.md").write_text(text, encoding="utf-8")

    def ledger(self, text):
        (self.root / "book-memory-bank" / "Core" / "continuity_ledger.md").write_text(text, encoding="utf-8")

    def run(self, *args):
        return subprocess.run([sys.executable, str(self.script), *args], cwd=str(self.root), text=True,
                              encoding="utf-8", capture_output=True, check=False)

    def rules(self, *chapters):
        data = json.loads(self.run("audit", "--json", *chapters).stdout)
        return {finding["rule"] for chapter in data["chapters"] for finding in chapter["findings"]}

    def close(self):
        shutil.rmtree(self.root, ignore_errors=True)


class Base(unittest.TestCase):
    def setUp(self):
        self.book = Book()
        self.addCleanup(self.book.close)


class AuditTests(Base):
    def test_clean_prose_has_no_fix_items(self):
        self.book.chapter("Chapter01", "# One\n\n" + CLEAN * 4)
        data = json.loads(self.book.run("audit", "--json").stdout)
        levels = [finding["level"] for finding in data["chapters"][0]["findings"]]
        self.assertNotIn("FIX", levels)

    def test_finds_ai_patterns(self):
        self.book.chapter("Chapter01", "# One\n\n" + SLOP)
        found = self.book.rules()
        for rule in ("em_dash", "beat_cliche", "silence_cliche", "explained_subtext", "theme_statement",
                     "label_on_cue", "ai_vocabulary", "chatbot"):
            self.assertIn(rule, found)

    def test_audit_never_changes_chapter(self):
        self.book.chapter("Chapter01", SLOP)
        path = self.book.root / "Chapters" / "Chapter01.md"
        before = path.read_bytes()
        self.book.run("check")
        self.book.run("audit", "--save")
        self.assertEqual(before, path.read_bytes())

    def test_interrupted_dialogue_dash_is_allowed(self):
        self.book.chapter("Chapter01", CLEAN * 2 + '\n\n"I never said I was going to—"\n\n"Stop," he said.\n')
        found = self.book.rules()
        self.assertNotIn("dialogue_dash", found)
        self.assertNotIn("em_dash", found)

    def test_dialogue_voice_not_flagged_as_narration(self):
        self.book.chapter("Chapter01", CLEAN * 2 + '\n\n"This intricate tapestry is pivotal," the consultant said.\n')
        self.assertNotIn("ai_vocabulary", self.book.rules())

    def test_scene_break_and_code_are_not_em_dashes(self):
        self.book.chapter("Chapter01", CLEAN + "\n\n---\n\n" + CLEAN + "\n\n```\nthis — is code\n```\n")
        self.assertNotIn("em_dash", self.book.rules())

    def test_nested_code_fence_is_not_prose(self):
        self.book.chapter("Chapter01", CLEAN + "\n\n~~~~\n~~~\nthis — is code\n~~~~\n\n" + CLEAN)
        self.assertNotIn("em_dash", self.book.rules())
        self.book.chapter("Chapter01", CLEAN + "\n\n~~~~\ncode\n~~~~\n\nThe door — open — waited.\n")
        self.assertIn("em_dash", self.book.rules())

    def test_wisdom_closer_only_at_scene_end(self):
        self.book.chapter("Chapter01", CLEAN + "It would have to be enough.\n\n---\n\n" + CLEAN)
        self.assertIn("wisdom_closer", self.book.rules())

    def test_author_baseline_protects_their_dashes(self):
        sample = self.book.root / "sample.md"
        sample.write_text(("He ran — fast — to the door and knocked. " + CLEAN) * 12, encoding="utf-8")
        self.book.chapter("Chapter01", ("He ran — fast — to the door and knocked. " + CLEAN) * 4)
        self.assertIn("em_dash", self.book.rules())
        self.assertEqual(self.book.run("voice", "sample.md").returncode, 0)
        self.assertNotIn("em_dash", self.book.rules())

    def test_short_voice_sample_rejected(self):
        (self.book.root / "tiny.md").write_text("Too short.", encoding="utf-8")
        result = self.book.run("voice", "tiny.md")
        self.assertEqual(result.returncode, 1)
        self.assertNotIn("Traceback", result.stderr)

    def test_ignore_file(self):
        self.book.chapter("Chapter01", SLOP)
        ignore = self.book.root / "book-memory-bank" / "Style" / "audit_ignore.txt"
        ignore.write_text("em_dash\n", encoding="utf-8")
        self.assertNotIn("em_dash", self.book.rules())

    def test_select_single_chapter(self):
        self.book.chapter("Chapter01", CLEAN)
        self.book.chapter("Chapter02", SLOP)
        self.assertFalse(self.book.rules("1"))
        self.assertTrue(self.book.rules("2"))

    def test_unknown_chapter_is_friendly(self):
        self.book.chapter("Chapter01", CLEAN)
        result = self.book.run("audit", "9")
        self.assertEqual(result.returncode, 1)
        self.assertIn("Could not find", result.stderr)
        self.assertNotIn("Traceback", result.stderr)

    def test_no_chapters_is_friendly(self):
        result = self.book.run("audit")
        self.assertEqual(result.returncode, 1)
        self.assertNotIn("Traceback", result.stderr)

    def test_repeated_phrase_across_chapters(self):
        openings = ("The ferry docked late.", "Snow closed the pass.", "Her cousin sold the boat.")
        for number, opening in enumerate(openings, 1):
            self.book.chapter(f"Chapter0{number}", f"{opening} Then the scar through his eyebrow caught the lamp.")
        self.assertIn("eyebrow", self.book.run("audit").stdout)


LEDGER = """# Ledger

## Characters

| Name | Aliases | Dies In | Notes |
|---|---|---|---|
| [Full name] | [x] | [Ch N] | |
| Anneli Koski | Anneli | Ch 2 | |
| Jussi | | | |

## Promises

| Promise | Keywords | Planted In | Pays Off In | Notes |
|---|---|---|---|---|
| The brass key | brass key | Ch 3 | Ch 2 | |
| The letter | letter | Ch 1 | | |

## Secrets

| Secret | Keywords | Character | Learns In |
|---|---|---|---|
| The forged will | forged | Jussi | Ch 3 |

## Facts

| Subject | Attribute | Value | Since |
|---|---|---|---|
| Jussi | eyes | green | |
| Jussi | age | 40 | Ch 1 |
| Jussi | age | 41 | Ch 1 |
"""


class ContinuityTests(Base):
    def test_finds_contradictions(self):
        self.book.ledger(LEDGER)
        self.book.chapter("Chapter01", "Jussi knew the will was forged. His letter sat on the table. Jusi waved.")
        self.book.chapter("Chapter02", "Jussi rubbed his blue eyes.")
        self.book.chapter("Chapter03", "Anneli walked into the room holding the brass key.")
        result = self.book.run("continuity")
        self.assertEqual(result.returncode, 1)
        for text in ("appears after dying", "before it is planted", "before learning", "should be green",
                     "misspelling", "from the same point", "no payoff yet"):
            self.assertIn(text, result.stdout)

    def test_template_ledger_is_quiet(self):
        self.book.chapter("Chapter01", CLEAN)
        result = self.book.run("continuity")
        self.assertEqual(result.returncode, 0)
        self.assertIn("agrees", result.stdout)

    def test_fact_can_change_over_time(self):
        self.book.ledger("## Facts\n\n| Subject | Attribute | Value | Since |\n|---|---|---|---|\n"
                         "| Jussi | hair | black | |\n| Jussi | hair | white | Ch 2 |\n")
        self.book.chapter("Chapter01", "Jussi pushed back his black hair.")
        self.book.chapter("Chapter02", "Jussi pushed back his white hair.")
        result = self.book.run("continuity")
        self.assertEqual(result.returncode, 0)
        self.assertNotIn("should be", result.stdout)


@unittest.skipUnless(shutil.which("pandoc"), "pandoc not found")
class ExportTests(Base):
    def test_epub_and_docx(self):
        self.book.chapter("Prologue", "# Prologue\n\n" + CLEAN)
        self.book.chapter("Chapter01", "# One\n\n" + CLEAN)
        brief = self.book.root / "book-memory-bank" / "Core" / "projectbrief.md"
        brief.write_text(brief.read_text(encoding="utf-8").replace("[Your Book Title]", "The Harbor")
                         .replace("[Author Name]", "A. Writer"), encoding="utf-8")
        result = self.book.run("export", "all")
        self.assertEqual(result.returncode, 0, result.stderr)
        manuscript = self.book.root / "Manuscript"
        self.assertTrue((manuscript / "BOOK.docx").is_file())
        with zipfile.ZipFile(manuscript / "BOOK.epub") as archive:
            opf = next(name for name in archive.namelist() if name.endswith(".opf"))
            metadata = archive.read(opf).decode("utf-8")
        self.assertIn("The Harbor", metadata)
        self.assertIn("A. Writer", metadata)
        self.assertEqual([p.name for p in manuscript.iterdir() if p.name.startswith(".")], [])

    def test_flags_block_final_but_not_draft(self):
        self.book.chapter("Chapter01", CLEAN + "[NEED RESEARCH: date]")
        manuscript = self.book.root / "Manuscript"
        manuscript.mkdir()
        (manuscript / "BOOK.epub").write_text("PREVIOUS", encoding="utf-8")
        self.assertEqual(self.book.run("export", "epub").returncode, 1)
        self.assertEqual((manuscript / "BOOK.epub").read_text(encoding="utf-8"), "PREVIOUS")
        self.assertEqual(self.book.run("export", "epub", "--draft").returncode, 0)
        self.assertTrue((manuscript / "BOOK_DRAFT.epub").is_file())


class MiscTests(Base):
    def test_doctor_runs_without_optional_tools(self):
        env = dict(os.environ, PATH="")
        result = subprocess.run([sys.executable, str(self.book.script), "doctor"], text=True, encoding="utf-8",
                                capture_output=True, env=env, check=False)
        self.assertEqual(result.returncode, 0)
        self.assertIn("Optional tools", result.stdout)

    def test_export_without_pandoc_is_friendly(self):
        self.book.chapter("Chapter01", CLEAN)
        env = dict(os.environ, PATH="")
        result = subprocess.run([sys.executable, str(self.book.script), "export"], text=True, encoding="utf-8",
                                capture_output=True, env=env, check=False)
        self.assertEqual(result.returncode, 1)
        self.assertIn("Pandoc", result.stderr)


if __name__ == "__main__":
    unittest.main()
