# book-writer

A skill for AI coding assistants that turns them into a world-class fiction author with an automated **Book Memory Bank** — maintaining full story context (characters, plot, world-building) across sessions automatically.

## What It Does

- ✍️ **Writes like a master author** — literary prose, realistic dialogue, genre-appropriate style
- 📚 **Maintains a Book Memory Bank** — structured Markdown files that persist story context between sessions
- 🔄 **Auto-updates memory** — no scripts, no copy-paste; just write and the AI keeps everything consistent
- 🗂️ **Organises your project** — chapters, outlines, and manuscripts in a clean, consistent structure

## Installation

```bash
npx skills add kshanxs/book-writer-skill
```

## Usage

Trigger phrases that activate this skill:

- `"Start a new book project"` / `"initialize memory bank"`
- `"Write chapter 1"` / `"outline the next chapter"`
- `"Update memory bank"`
- `"Check for consistency issues"`

## What's Inside

```
book-writer/
├── SKILL.md                        # Core skill instructions
├── references/
│   ├── author_rules.md             # Writing persona & style guide
│   ├── book_memory_protocol.md     # Memory bank update rules
│   └── memory_update_prompts.md    # Prompts for memory updates
└── assets/
    └── book-memory-bank/           # Template directory (copied to your project)
        ├── Core/                   # projectbrief, story_structure, characters, etc.
        ├── Style/                  # style_guide.md
        └── Production/             # Scripts for manuscript generation
```

## Memory Bank Structure

The memory bank is automatically copied to your project on initialization and kept up to date after every chapter:

```
YourBookProject/
├── Chapters/          # Your actual chapter files
├── Outlines/          # Master outline + chapter outlines
├── Manuscript/        # Assembled output
└── book-memory-bank/  # Context files (auto-maintained by the AI)
    ├── Core/
    └── Style/
```

## License

MIT
