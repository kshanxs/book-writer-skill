# 📖 book-writer

> A skill for AI assistants that combines world-class fiction writing with an automated **Book Memory Bank** — keeping your characters, plot, and world-building perfectly consistent across every session.

---

## ✨ Features

| | |
|---|---|
| ✍️ **Master Author Voice** | Literary prose, cinematic dialogue, and genre-aware style |
| 🧠 **Book Memory Bank** | Structured Markdown files that persist your entire story universe |
| 🔄 **Automatic Updates** | Memory stays current after every chapter — no scripts, no copy-paste |
| 🗂️ **Clean Project Structure** | Chapters, outlines, and manuscripts organized from day one |

---

## 🚀 Installation

```bash
npx skills add kshanxs/book-writer-skill
```

---

## 💬 Usage

Just talk to your AI assistant naturally. Trigger phrases include:

```
"Start a new book project"
"Initialize the memory bank"
"Write chapter 3"
"Outline the next chapter"
"Update memory bank"
"Check for consistency issues"
```

---

## 📁 Project Structure

Once initialized, your book project will look like this:

```
YourBookProject/
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
├── SKILL.md                        # Core skill instructions
├── references/
│   ├── author_rules.md             # Writing persona & quality standards
│   ├── book_memory_protocol.md     # Memory bank update rules & checklist
│   └── memory_update_prompts.md    # Ready-to-use update prompts
└── assets/
    └── book-memory-bank/           # Template directory (copied to your project)
```

---

## 📄 License

MIT © [Shubhanshu](https://github.com/kshanxs)
