<div align="center">

# book-writer — Features & Reference

**v3.0.0** · *Complete feature list, command reference, and skill architecture*

</div>

---

## Full Feature List

<table>
<tr>
<td width="50%">

### Writing Engine
| | |
|---|---|
| **Master Author Voice** | Literary prose, cinematic dialogue, genre-aware style |
| **15+ Genre Options** | Literary, Fantasy, Sci-Fi, Historical, Thriller, Horror, Romance, YA, Children's |
| **Book Size Planning** | MVB (15–20K) · Short (25–40K) · Full (50–80K) · Novel (60–100K) |
| **Chapter Craft** | 6 opening/closing formulas, structure templates, engagement techniques |
| **Humanized Writing** | Story-level de-AI checks, em dash rule, over-correction safeguards |
| **Multi-Language Dialogue** | Hinglish, Hindi, Marathi, French, Spanish, Italian, German |

</td>
<td width="50%">

### Story Memory
| | |
|---|---|
| **Book Memory Bank** | Persistent Markdown files — characters, plot, world, progress |
| **Auto Updates** | Memory stays current after every chapter — zero manual work |
| **Continuity Diagnostics** | Cross-chapter consistency checks with diagnostic reports |
| **Continuity Ledger** | Catches dead characters returning, early payoffs, leaked secrets, and misspelled names |
| **Historical Authenticity** | Verified dates, titles, events, title-timeline rules |
| **Draft Import** | Paste existing notes — AI skips questions already answered |
| **Auto GitHub README** | Generates polished project README on initialization |
| **Story Gitas** | Domain-specific ultimate truth docs (`lore_gita.md`, `tech_gita.md`) |

</td>
</tr>
<tr>
<td width="50%">

### Children's Books
| | |
|---|---|
| **Age-Based Guidelines** | Tailored rules for ages 2–3, 4–5, 6–7, 8–9 |
| **Rhyming & Meter** | Perfect rhyme schemes, meter analysis, read-aloud testing |
| **Illustration Notes** | Per-page visual descriptions for artists |
| **Phonics & Vocabulary** | Sight words, CVC words, vocabulary building |
| **Values & Lessons** | Natural moral integration — show, don't preach |
| **Book Types** | Picture books, songs/poems, series, non-rhyming stories |

</td>
<td width="50%">

### New Workflows
| | |
|---|---|
| **Pacing Blueprint** | Book-level structural grid with tension curve before drafting |
| **Scene Card** | Atomic Goal–Conflict–Outcome–Aftermath per scene |
| **Research Tracker** | Structured `[NEED RESEARCH]` log prevents unverified facts shipping |
| **Beta Reader Log** | Chapter-by-chapter feedback tracking with status and actions |
| **Publishing Toolkit** | Generate blurb, synopsis, query letter, logline from memory bank |

</td>
</tr>
<tr>
<td width="50%">

### Story Building
| | |
|---|---|
| **Character Arc Matrix** | Chapter-by-chapter progression of lies and emotion |
| **Worldbuilding Tables** | 10-category world profiles with sensory details |
| **Conflict Mapping** | External, internal, thematic conflicts with stakes |
| **Synopsis & Timeline** | Full narrative beats + chronological event tracking |
| **Thematic Tracker** | Matrix for tracking core themes and recurring motifs |
| **Emotional Core** | North Star identification — the truth your story explores |
| **Compilation** | Safe manuscript, Word, and EPUB export with ordering checks |

</td>
<td width="50%">

### Quality Control
| | |
|---|---|
| **Revision Checklists** | Story, prose, voice, characters, continuity gates |
| **Children's Checklist** | Rhyme, meter, age-appropriateness, engagement |
| **Scene Tension Mapping** | 1-10 scoring system evaluating structural pacing |
| **Specialized Passes** | Dedicated Dialogue, Sensory, Prose Polish, Tension passes |
| **Opening Chapter Checklist** | Extra scrutiny for Chapter 1: hook, promise, exposition |
| **Continuity Reports** | Question-based diagnostic — flags, never imposes |
| **Revision Snapshots** | Chapters are backed up to `Revisions/` before edits |
| **Prose Audit** | Finds AI-sounding patterns with line numbers, and never edits your book |
| **Voice Baseline** | Learns the author's style so their real habits are not flagged |
| **Cold Reader** | A fresh reader reports boredom, confusion, and what works |
| **Title-Timeline Rule** | Correct historical address based on scene date |
| **Contextual Address** | Different characters use different titles for same figure |
| **`[FICTION]` Marking** | Explicit tagging of invented historical elements |

</td>
</tr>
</table>

---

## Command Reference

| Say this | What happens |
|---|---|
| `"Let's start building a new book"` | Runs The Story Forge onboarding |
| `"Just initialize now"` | Skips all questions, starts immediately |
| `"Plan a short book"` | Sets book scope — MVB / Short / Full / Novel |
| `"Write a children's book for ages 4-6"` | Activates children's book craft |
| `"Let's build out [character]"` | Creates 19-field character profile |
| `"Build a worldbuilding table"` | Creates 10-category world profile |
| `"Write chapter 3"` | Reads memory bank, writes the chapter |
| `"Outline chapter 3"` | Creates chapter outline |
| `"Outline all chapters in parallel"` | Launches background agents for chapter outlines |
| `"Review chapter 3"` | Structured chapter review & polish |
| `"Do a Sensory Pass on chapter 3"` | Focused revision for immersive detail |
| `"Review all chapters in parallel"` | Launches background agents to edit/review drafted chapters |
| `"Write a query letter"` | Generates query letter from memory bank |
| `"Write a back-cover blurb"` | Generates blurb from memory bank |
| `"Write a 1-page synopsis"` | Full synopsis for agent submissions |
| `"Log beta feedback"` | Opens Beta Reader Feedback Log |
| `"Update memory bank"` | Full audit and update |
| `"Check continuity"` | Cross-chapter diagnostic report |
| `"Humanize chapter 3"` | Audits and gently revises AI-sounding prose |
| `"Learn my voice from ./sample.md"` | Builds the author's style baseline |
| `"Do a cold read of chapter 1"` | Blind reader feedback |
| `"Check the book"` | Runs every automated book check |
| `"Export the book"` | Builds Word and EPUB files |
| `"Check for consistency"` | Flags contradictions across memory bank |
| `"Compile the book"` | Combines chapters in reading order into `Manuscript/` |
| `"[FICTION] ..."` | Marks an invented element (historical genres) |

---

## Historical Genres

Activates automatically when you choose a historical genre or mention real figures:

- All dates, battles, titles, and biographical facts historically verified
- Figures addressed by titles they've earned *at the scene's point in time*
- Different characters address the same figure differently — context matters
- Invented elements accepted when prefixed with `[FICTION]`

---

## Project Structure After Initialization

```
YourBookProject/
│
├── README.md ← Auto-generated (GitHub-ready)
│
├── Chapters/ ← Your manuscript
│ ├── Chapter01.md
│ ├── Chapter02.md
│ └── ...
│
├── Outlines/ ← Planning
│ ├── Master_Outline.md
│ ├── chapter-titles-guide.md ← Auto-generated title reference
│ └── Chapter_Outlines/
│
├── Research/ ← Continuity reports & notes
│ └── continuity_diagnostic_report.md
│
├── Revisions/ ← Snapshots made before chapters are revised
│
├── Manuscript/ ← Compiled book output
│
└── book-memory-bank/ ← Auto-maintained by the AI
 ├── Core/
 │ ├── projectbrief.md High-level concept & goals
 │ ├── story_structure.md Narrative patterns & themes
 │ ├── world_and_characters.md Characters, world, relationships
 │ ├── continuity_ledger.md Facts the tools can check
 │ ├── activeContext.md Current session focus
 │ ├── progress.md Completion tracking
 │ └── Templates/ Planning and tracking templates
 ├── Style/
 │ ├── style_guide.md Voice, tone, language rules
 │ └── audit_ignore.txt Patterns the audit should skip
 └── Production/
 ├── Scripts/ Book Tools, Word and EPUB export
 ├── Vale/ Optional style rules
 └── AI_Generation/ Cover prompts
```

---

## Skill Architecture

```
book-writer-skill/ ← Repo root
├── docs/
│ ├── USAGE.md ← Usage guide with examples
│ └── FEATURES.md ← This file
├── tests/ ← Script and Book Tools tests
├── scripts/ ← Repository checks
├── book-writer/ ← Skill folder
│ ├── SKILL.md ← Core instructions & 10 workflows
│ ├── THIRD_PARTY_NOTICES.md ← Open-source credits
│ ├── references/
│ │ ├── author_rules.md Writing persona & historical rules
│ │ ├── book_memory_protocol.md Memory bank architecture & rules
│ │ ├── memory_update_prompts.md Update criteria & templates
│ │ ├── story_forge.md Onboarding (fiction + non-fiction, North Star)
│ │ ├── readme_template.md Auto-README template
│ │ ├── chapter_craft.md Chapter formulas & engagement
│ │ ├── revision_checklist.md Quality gates & DO/DON'T lists
│ │ ├── character_worldbuilding_tables.md Profiles, world, conflict tables
│ │ ├── childrens_book_craft.md Ages 2–9, rhyming, illustration
│ │ ├── parallel_workflows.md Parallel outlining and review limits
│ │ ├── punctuation_guide.md Mark-by-mark punctuation rules
│ │ ├── spinoff_guide.md Spinoff Forge & canon consistency
│ │ ├── opening_chapter_checklist.md Chapter 1 dedicated quality gates
│ │ ├── query_letter_guide.md Publishing toolkit
│ │ ├── popscience_history_rules.md Popular science and tech history
│ │ ├── humanizing_prose.md Voice, em dash, and de-AI rules
│ │ ├── cold_reader.md Blind reader review
│ │ └── chapter_titles_guide.md Title → meaning → story connection
│ └── assets/
│ └── book-memory-bank/ ← Template directory (copied on init)
│ ├── Production/Scripts/book.py ← Checks and export
│ └── Core/Templates/
│ ├── chapter_outline_template.md
│ ├── master_outline_template.md
│ ├── chapter_titles_guide_template.md
│ ├── character_arcs_template.md
│ ├── themes_and_motifs_template.md
│ ├── world_gita_template.md
│ ├── scene_card_template.md
│ ├── pacing_blueprint_template.md
│ ├── research_tracker_template.md
│ └── beta_reader_log_template.md
```

---

## Changelog

See [CHANGELOG.md](../CHANGELOG.md) for every release.
