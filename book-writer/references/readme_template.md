# README Template — Book Writer Skill

This template is used by the AI to generate a `README.md` in the user's book project root immediately after initialization. 

**Instructions for the AI:**
1. Read all `{{TOKEN}}` placeholders below
2. Fill each one using answers from the brainstorming gate and the newly created memory bank files
3. Delete any section whose data is entirely TBD (except the Progress and Status sections — always include those)
4. If GitHub visibility is `none`, remove the badges block entirely
5. If GitHub visibility is `private`, keep badges but use `#` as the URL and add the note below the badges
6. Write the completed README to `README.md` in the project root
7. After writing, do NOT ask the user to review it unless they ask — it is a living document they can edit anytime

---

<!-- ============================================================ -->
<!-- BEGIN README TEMPLATE — everything below goes into README.md -->
<!-- ============================================================ -->

<div align="center">

# {{BOOK_EMOJI}} {{BOOK_TITLE}}

*{{BOOK_TAGLINE}}*

<!-- BADGES: fill REPO_URL if public; use # if private; remove block entirely if no GitHub -->
[![Status](https://img.shields.io/badge/status-in%20progress-orange?style=flat-square)]({{REPO_URL}})
[![Chapters](https://img.shields.io/badge/chapters-{{CHAPTER_COUNT}}%20drafted-blue?style=flat-square)]({{REPO_URL}}/{{CHAPTERS_DIR}})
[![Genre](https://img.shields.io/badge/genre-{{GENRE_BADGE}}-purple?style=flat-square)]({{REPO_URL}})

</div>

<!-- PRIVATE REPO NOTE: add this line below badges if visibility = private -->
<!-- > ⚠️ *This repository is private. Update badge URLs above if you publish publicly.* -->

---

## About the Book

**{{BOOK_TITLE}}** {{PREMISE_PARAGRAPH}}

<!-- If historical mode is active, add this block: -->
<!-- > *This is a work of narrative history. All dates, events, and biographical facts are grounded in historical record. Fictional elements, where present, are clearly marked.* -->

> *"{{OPENING_QUOTE}}"*

<!-- Remove the quote block if no quote was provided -->

---

## Scope{{SCOPE_SUBTITLE}}

{{SCOPE_DESCRIPTION}}

| Period | Arc | Chapters |
|---|---|---|
{{SCOPE_TABLE_ROWS}}

<!-- SCOPE_TABLE_ROWS format (one row per arc):
| {{TIME_PERIOD}} | **{{ARC_NAME}}** — {{ARC_DESCRIPTION}} | {{CHAPTER_RANGE}} |
Remove this table entirely if scope is TBD -->

---

## Repository Structure

```
{{PROJECT_ROOT_NAME}}/
├── Chapters/               # Finished literary chapters
├── Outlines/
│   └── Master_Outline.md   # Full story structure and chapter notes
├── book-memory-bank/       # AI writing memory bank (context continuity)
│   ├── Core/               # Project brief, story structure, characters, progress
│   └── Style/              # Style guide and voice conventions
└── .agents/                # Book-writer skill and AI agent configuration
```

---

## Central Figures

| Figure | Role |
|---|---|
{{FIGURES_TABLE_ROWS}}

<!-- FIGURES_TABLE_ROWS format:
| **{{CHARACTER_NAME}}** {{LIFE_DATES}} | {{CHARACTER_ROLE}} |
Include protagonist, antagonist, and any key supporting figures gathered in the gate -->
<!-- Remove this section if no characters were defined -->

---

## Key Events{{KEY_EVENTS_SUBTITLE}}

{{KEY_EVENTS_LIST}}

<!-- KEY_EVENTS_LIST format:
- **{{LOCATION}}, {{YEAR}}** — {{EVENT_DESCRIPTION}}
Remove this section if no key events were defined -->

---

## Writing Approach

{{WRITING_APPROACH_PARAGRAPH}}

<!-- If a style reference was given:
The prose aims for the register of **{{STYLE_REFERENCE}}** — {{STYLE_DESCRIPTION}}.
If historical mode: Historical claims are hedged where evidence is uncertain. [FICTION] elements are marked in the memory bank. -->

---

## Progress

| Component | Status |
|---|---|
{{PROGRESS_TABLE_ROWS}}

<!-- PROGRESS_TABLE_ROWS: generate one row per chapter/component.
Start with all chapters as 📝 Not started. AI updates this table on each chapter write.
Format:
| {{CHAPTER_NAME}} | {{STATUS_EMOJI}} {{STATUS_TEXT}} |
Status options: ✅ Complete / 📝 Draft / ❌ Not yet written -->

---

{{SOURCES_SECTION}}

<!-- SOURCES_SECTION: include only if user provided sources during gate.
Format:
## Sources

**Primary:**
- {{SOURCE_1}}

**Secondary:**
- {{SOURCE_2}}

Remove entire section if no sources were given -->

---

## Status

This book is actively being written. The repository serves as the living manuscript — chapters are added and revised as the project progresses.

*Started: {{START_DATE}}*

<!-- ============================================================ -->
<!-- END README TEMPLATE -->
<!-- ============================================================ -->

---

## Token Reference

| Token | Source |
|---|---|
| `{{BOOK_EMOJI}}` | AI picks based on genre (⚔️ historical/war, 🌌 sci-fi, 🔮 fantasy, 🕵️ thriller, ❤️ romance, 📖 literary) |
| `{{BOOK_TITLE}}` | Gate Step 2 or draft import |
| `{{BOOK_TAGLINE}}` | AI generates from premise; 8–12 words |
| `{{REPO_URL}}` | Gate Step 7; use `#` if private, omit block if no GitHub |
| `{{CHAPTER_COUNT}}` | Start at 0; update on each chapter write |
| `{{CHAPTERS_DIR}}` | `Chapters` (default) |
| `{{GENRE_BADGE}}` | URL-encoded genre string (e.g., `historical%20fiction`) |
| `{{PREMISE_PARAGRAPH}}` | Gate Step 4; expand to 2–3 sentences |
| `{{OPENING_QUOTE}}` | Optional; from user's draft or AI-suggested; remove block if none |
| `{{SCOPE_SUBTITLE}}` | Append `: {{YEAR_START}} – {{YEAR_END}}` if historical |
| `{{SCOPE_TABLE_ROWS}}` | From gate Step 5 + user's outline if available |
| `{{PROJECT_ROOT_NAME}}` | Name of the project directory |
| `{{FIGURES_TABLE_ROWS}}` | Gate Step 5 characters; include life dates if historical |
| `{{KEY_EVENTS_LIST}}` | Historical events or plot beats from gate/draft |
| `{{WRITING_APPROACH_PARAGRAPH}}` | Gate Step 6 style reference + historical mode note |
| `{{PROGRESS_TABLE_ROWS}}` | One row per chapter, all start as ❌ Not yet written |
| `{{SOURCES_SECTION}}` | Gate Step 1 draft sources or user-mentioned sources |
| `{{START_DATE}}` | Current month + year at time of initialization |
