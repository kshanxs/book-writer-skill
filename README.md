<div align="center">

# 📖 book-writer

*A comprehensive AI skill that combines world-class fiction writing, structured story planning, and an automated Book Memory Bank — keeping your characters, plot, and world-building perfectly consistent across every session.*

[![Install](https://img.shields.io/badge/install-npx%20skills%20add-blue?style=flat-square)](https://github.com/kshanxs/book-writer-skill)
[![License](https://img.shields.io/badge/license-MIT-green?style=flat-square)](./LICENSE)
[![Docs](https://img.shields.io/badge/docs-USAGE.md-orange?style=flat-square)](./book-writer/docs/USAGE.md)

</div>

---

## ✨ Features

| | |
|---|---|
| ✍️ **Master Author Voice** | Literary prose, cinematic dialogue, and genre-aware style |
| 🧠 **Book Memory Bank** | Structured Markdown files that persist your entire story universe |
| 🔄 **Automatic Updates** | Memory stays current after every chapter — no scripts, no copy-paste |
| 📚 **The Story Forge** | Guided onboarding — one question at a time, everything skippable |
| 🎯 **Emotional Core Discovery** | North Star identification — the deeper truth your story explores |
| 📐 **Narrative Structure** | Three-Act, Hero's Journey, Literary Arc, Multi-Timeline, Episodic, or custom |
| 📏 **Book Size Planning** | MVB (15–20K), Short (25–40K), Full (50–80K), Literary Novel (60–100K) |
| 👤 **Character Profiles** | 19-field structured tables with psychological depth and relationship mapping |
| 🌍 **Worldbuilding Tables** | 10-category world profiles — atmosphere, sensory details, emotional geography |
| ⚔️ **Conflict Mapping** | External, internal, and thematic conflict structures with stakes tracking |
| 📝 **Chapter Craft** | 6 opening/closing formulas, engagement techniques, and drafting best practices |
| ✅ **Revision Checklists** | Comprehensive quality gates for story, prose, voice, characters, and continuity |
| 🛡️ **Anti-AI Writing** | Hype test, voice authenticity checks, and DO/DON'T quick-scan lists |
| 🔍 **Continuity Diagnostics** | Cross-chapter consistency checks with question-based diagnostic reports |
| 🏛️ **Historical Authenticity** | Verified dates, titles, events, and the title-timeline rule |
| 🗣️ **Multi-Language Dialogue** | Hinglish, Hindi, Marathi, French, Spanish, Italian, German, and more |
| 📜 **Auto GitHub README** | Generates a polished project README on initialization |
| 📄 **Draft Import** | Paste or link existing notes — AI skips questions already answered |
| 🎭 **15+ Genre Options** | Literary, Fantasy, Sci-Fi, Historical, Thriller, Horror, Romance, and more |
| 📦 **Compilation** | Auto-combine chapters into manuscript via scripts or AI |

---

## 🚀 Installation

```bash
npx skills add kshanxs/book-writer-skill
```

To get the latest version later on, just run:

```bash
npx skills update kshanxs/book-writer-skill
```

---

## 💬 How to Use

Just talk naturally. Start with:

```
"Let's start building a new book"
"Initialize the memory bank"
"I have some notes already — here's my outline: ./outline.md"
"Just initialize now, I'll fill in details later"
```

The AI guides you through setup one question at a time. Every question is skippable. After initialization, it never asks setup questions again — just say what you want to do.

**→ See [USAGE.md](./book-writer/docs/USAGE.md) for the full guide with example dialogues**

---

## 🏛️ Historical Genres

Applies automatically when you choose a historical genre or mention real figures. The AI:

- Keeps all dates, battles, titles, and biographical facts historically correct
- Only addresses figures by titles they've earned at the scene's point in time (*Shivaji* before 1674 → *Chhatrapati Shivaji Maharaj* after coronation)
- Lets different characters address the same figure differently — a villain strips the title; a loyal soldier uses *"Maharaj"*; the narrator holds the full form
- Accepts invented elements when you prefix them with `[FICTION]`

---

## 📁 Your Project After Initialization

```
YourBookProject/
│
├── README.md                    # Auto-generated project README (GitHub-ready)
│
├── Chapters/                    # Your actual chapter files
│   └── Chapter01.md
│
├── Outlines/                    # Planning documents
│   ├── Master_Outline.md
│   └── Chapter_Outlines/
│
├── Research/                    # Continuity reports and notes
│   └── continuity_diagnostic_report.md
│
├── Manuscript/                  # Compiled book output
│
└── book-memory-bank/            # Auto-maintained by the AI
    ├── Core/
    │   ├── projectbrief.md      # High-level concept & goals
    │   ├── story_structure.md   # Narrative patterns & themes
    │   ├── world_and_characters.md
    │   ├── activeContext.md     # Current session focus
    │   └── progress.md          # Completion tracking
    └── Style/
        └── style_guide.md
```

---

## 🔍 What's Inside the Skill

```
book-writer/
├── SKILL.md                              # Core skill instructions & features list
├── docs/
│   └── USAGE.md                          # 📖 Usage guide with full example dialogues
├── references/
│   ├── author_rules.md                   # Writing persona, quality standards & historical rules
│   ├── book_memory_protocol.md           # Memory bank update rules & continuity diagnostics
│   ├── memory_update_prompts.md          # Ready-to-use update prompts
│   ├── story_forge.md                    # The Story Forge — onboarding (15+ genres, North Star, structure)
│   ├── readme_template.md                # Template for auto-generating project README
│   ├── chapter_craft.md                  # Chapter formulas, book sizes, engagement techniques
│   ├── revision_checklist.md             # Quality gates, DO/DON'T lists, review principles
│   └── character_worldbuilding_tables.md # Character profiles, world tables, conflict mapping
└── assets/
    └── book-memory-bank/                 # Template directory copied to your project on init
```

---

## ⚡ Quick Reference

| Say this | What happens |
|---|---|
| `"Let's start building a new book"` | Runs the onboarding conversation |
| `"Just initialize now"` | Skips all questions, starts immediately |
| `"Plan a short book"` | Sets book scope (MVB / Short / Full / Novel) |
| `"Let's build out [character]"` | Creates structured character profile table |
| `"Build a worldbuilding table"` | Creates 10-category world profile |
| `"Write chapter 3"` | AI reads memory bank and writes the chapter |
| `"Outline chapter 3"` | Creates the chapter outline |
| `"Review chapter 3"` | Structured chapter review & polish |
| `"Update memory bank"` | Full audit and update after a writing session |
| `"Check continuity"` | Cross-chapter diagnostic report |
| `"Check for consistency"` | Flags contradictions across memory bank |
| `"Compile the book"` | Merges all chapters into `Manuscript/` |
| `"[FICTION] ..."` | Marks an invented element in historical genres |

---

## 📄 License

MIT © [Shubhanshu](https://github.com/kshanxs)
