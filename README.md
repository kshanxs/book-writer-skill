<div align="center">

# 📖 book-writer

*A skill for AI assistants that combines world-class fiction writing with an automated Book Memory Bank — keeping your characters, plot, and world-building perfectly consistent across every session.*

[![Install](https://img.shields.io/badge/install-npx%20skills%20add-blue?style=flat-square)](https://github.com/kshanxs/book-writer-skill)
[![License](https://img.shields.io/badge/license-MIT-green?style=flat-square)](./LICENSE)
[![Docs](https://img.shields.io/badge/docs-USAGE.md-orange?style=flat-square)](./book-writer/USAGE.md)

</div>

---

## ✨ Features

| | |
|---|---|
| ✍️ **Master Author Voice** | Literary prose, cinematic dialogue, and genre-aware style |
| 🧠 **Book Memory Bank** | Structured Markdown files that persist your entire story universe |
| 🔄 **Automatic Updates** | Memory stays current after every chapter — no scripts, no copy-paste |
| 🗂️ **Clean Project Structure** | Chapters, outlines, and manuscripts organized from day one |
| � **The Story Forge** | Guided onboarding — one question at a time, everything skippable |
| 📜 **Auto GitHub README** | Generates a polished project README on initialization, public or private |
| 🏛️ **Historical Accuracy Mode** | Verified dates, titles, and events for historical genres |
| 🔖 **Title-Timeline Rule** | Figures only addressed by titles they've actually earned at that point in the story |
| 📄 **Draft Import** | Paste or link existing notes — AI skips questions already answered |
| 🎭 **15 Genre Options** | Literary, Fantasy, Sci-Fi, Historical, Thriller, Horror, Romance, and more |

---

## 🚀 Installation

```bash
npx skills add kshanxs/book-writer-skill
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

**→ See [CONVERSATION_GUIDE.md](./book-writer/CONVERSATION_GUIDE.md) for full example dialogues**
**→ See [USAGE.md](./book-writer/USAGE.md) for the complete reference guide**

---

## 🏛️ Historical Mode

Activates automatically when you choose a historical genre or mention real figures. The AI:

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
├── Manuscript/                  # Final assembled output
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
├── SKILL.md                     # Core skill instructions
├── USAGE.md                     # 📖 Complete usage reference
├── CONVERSATION_GUIDE.md        # 💬 Example dialogues — how to talk to the AI
├── references/
│   ├── author_rules.md          # Writing persona, quality standards & historical rules
│   ├── book_memory_protocol.md  # Memory bank update rules & checklist
│   ├── memory_update_prompts.md # Ready-to-use update prompts
│   ├── story_forge.md           # The Story Forge — onboarding (15 genres, historical mode)
│   └── readme_template.md       # Template for auto-generating project README
└── assets/
    └── book-memory-bank/        # Template directory copied to your project on init
```

---

## ⚡ Quick Reference

| Say this | What happens |
|---|---|
| `"Let's start building a new book"` | Runs the onboarding conversation |
| `"Just initialize now"` | Skips all questions, starts immediately |
| `"Write chapter 3"` | AI reads memory bank and writes the chapter |
| `"Outline chapter 3"` | Creates the chapter outline |
| `"Update memory bank"` | Full audit and update after a writing session |
| `"Check for consistency"` | Flags contradictions across memory bank |
| `"[FICTION] ..."` | Marks an invented element in historical mode |

---

## 📄 License

MIT © [Shubhanshu](https://github.com/kshanxs)
