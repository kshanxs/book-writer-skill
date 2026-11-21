# Book Memory Bank

This folder holds what your AI assistant needs to remember about your book between sessions. Your assistant reads and updates these files for you, so you do not need to manage them by hand.

## What's Inside

```text
book-memory-bank/
├── Core/
│   ├── projectbrief.md          Concept, scope, and goals
│   ├── story_structure.md       Themes, structure, and narrative patterns
│   ├── world_and_characters.md  World rules and character profiles
│   ├── continuity_ledger.md     Facts the tools can check
│   ├── activeContext.md         Current focus and memory file index
│   ├── progress.md              Completion tracking
│   └── Templates/               Starting points for optional documents
├── Style/
│   ├── style_guide.md           Voice, tone, and formatting rules
│   └── audit_ignore.txt         Things the prose audit should skip
└── Production/
    ├── AI_Generation/           Cover prompt templates
    ├── Scripts/                 Book Tools, plus Word and EPUB export
    └── Vale/                    Optional style rules for Vale
```

Your actual book lives outside this folder:

```text
YourBook/
├── Chapters/    Prologue.md, Chapter01.md, Interlude01.md, Epilogue.md
├── Outlines/    Master_Outline.md and Chapter_Outlines/
├── Research/    Research tracker and continuity reports
├── Revisions/   Snapshots made before chapters are revised
└── Manuscript/  Compiled book files
```

## How to Use It

Talk to your assistant naturally:

```text
Write the outline for Chapter 1
Write Chapter 1
Update memory bank
Check continuity
Humanize Chapter 3
Export the book
```

A good rhythm is outline, review, draft, review, then update memory. Read each chapter as it is written, because early corrections are much easier than late ones.

## Exporting Your Book

See [Production/README.md](Production/README.md) for the checks and for Word and EPUB export.
