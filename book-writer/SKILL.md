---
name: book-writer
description: |
  Comprehensive book writing assistant and memory maintainer. Use when tasked with:
  - Writing books, novels, fiction, non-fiction, or any long-form manuscript
  - Creating characters, outlining chapters, building worlds
  - Drafting, reviewing, or revising chapters
  - Writing children's books, picture books, rhyming stories, or songs for ages 2–9
  - "initialize memory bank", "update memory bank", "start a new book", "let's start building"
  - Planning book structure (MVB, short book, full book, literary novel, picture book)
  - Checking continuity or consistency across chapters
  - Any request involving book chapters, manuscripts, or story development

  Provides specialized guidelines to write like a master author while maintaining an automated book memory bank to preserve context across sessions. Includes children's book writing, parallel chapter workflows, and multi-genre support.
---

# Book Writer

## Overview

This skill equips Claude with the capabilities of a world-class fiction author and a robust system for maintaining story context ("Book Memory Bank") across long writing sessions. With this skill, Claude acts as a creative collaborator while automatically keeping characters, plots, and world-building details consistent.

## Context Efficiency Rule

**CRITICAL — Read this before loading any files.**

This skill has many reference files. Do NOT pre-load them all. Use **lazy loading** — only read a reference file when its specific feature is needed:

| Only load this file... | When... |
|------------------------|---------|
| `references/author_rules.md` | Starting a session, drafting, or reviewing |
| `references/chapter_craft.md` | Writing or outlining chapters |
| `references/revision_checklist.md` | Reviewing or revising chapters |
| `references/book_memory_protocol.md` | Updating memory bank or running continuity check |
| `references/story_forge.md` | Only during initialization |
| `references/childrens_book_craft.md` | Only for children's book projects |
| `references/parallel_workflows.md` | Only when parallel drafting |
| `references/spinoff_guide.md` | Only for spinoff projects |
| `references/opening_chapter_checklist.md` | Only when reviewing Chapter 1 |
| `references/query_letter_guide.md` | Only when user asks for blurb, synopsis, or query letter |
| Template files | Only when generating the specific document |

**Never load more than 3–4 reference files at once unless explicitly required by the task.**

## Features

This skill combines capabilities from multiple specialized writing disciplines:

- **Book Memory Bank** — Automatic context preservation across sessions (characters, plots, world, progress)
- **The Story Forge** — One-time onboarding conversation with fast-track option, draft import, and genre detection
- **Multi-Genre Mastery** — Literary fiction, historical, fantasy, sci-fi, thriller, romance, horror, YA, and more
- **Historical Genre Features** — Title/honorific timeline rules, `[FICTION]` marking, contextual address rules, fact-checking flags
- **Dialogue Language Support** — Weave local languages (Hinglish, Hindi, Marathi, French, Spanish, etc.) into dialogue naturally
- **Character Profiles** — Structured 19-field character tables with historical title timelines
- **Character Arc Matrix** — Chapter-by-chapter tracking of emotional progression, internal lies, and paradigm shifts
- **Worldbuilding Tables** — 10-category structured world profiles with sensory details
- **Conflict Mapping** — External/internal/thematic conflict structure with stakes
- **Thematic & Motif Tracker** — Matrix for tracking core themes and the evolution of recurring symbolic motifs
- **Synopsis & Timeline Templates** — Beginning/middle/end narrative beats; chronological event tracking
- **Chapter Craft** — Opening/closing formulas, structure templates, engagement techniques for fiction and non-fiction
- **Book Size Planning** — MVB (15–20K words), Short (25–40K), Full (50–80K), Literary Novel (60–100K)
- **Revision Checklists** — Comprehensive quality gates: story, prose, voice, punctuation, characters, continuity, engagement
- **Scene Tension Mapping** — 1-10 scoring system to evaluate structural pacing and the action/reaction cycle
- **Specialized Revision Passes** — Dedicated targeted reviews (Dialogue Pass, Sensory Pass, Prose Polish, Tension Pass)
- **Punctuation Standards** — Mark-by-mark rules for em dashes, commas, periods, colons, semicolons, ellipses, and exclamation points; quick-reference table and per-chapter review checklist
- **Anti-AI Writing Rules** — Hype test, voice authenticity checks, DO/DON'T quick-scan lists
- **Continuity Diagnostics** — Cross-chapter consistency checks generating question-based diagnostic reports
- **Automated Memory Updates** — Triggered after chapter completion, outline creation, or on-demand
- **Chapter Titles Guide** — Auto-generated `chapter-titles-guide.md` mapping every chapter title to its meaning and story connection. Adapts to flat chapters, multi-part books, and multi-book projects
- **Parallel Chapter Workflows** — Draft and review multiple chapters simultaneously via background agents, with sequential fallback
- **Children's Book Craft** — Age-based writing guidelines (2–9), rhyming/meter techniques, illustration notes, phonics/vocabulary, values framework, and children's revision checklist
- **Scene Card Template** — Atomic scene planning (Goal-Conflict-Outcome-Aftermath) before drafting
- **Book-Level Pacing Blueprint** — Structural grid pre-planning tension curve and all major beats across the whole book
- **Opening Chapter Checklist** — Dedicated scrutiny for Chapter 1: hook, protagonist, reader promise, exposition
- **Research Flag Tracker** — Structured `[NEED RESEARCH]` log to prevent unverified facts from shipping in the manuscript
- **Beta Reader Feedback Log** — Chapter-by-chapter feedback tracking with status and consolidated action items
- **Query Letter & Publishing Toolkit** — Generate back-cover blurb, 1-page synopsis, query letter, and logline from the memory bank
- **Spinoff Support** — Start a new story in the same world or with shared characters; Spinoff Forge onboarding, inheritance model, directory convention, shared canon rules, and cross-reference protocol
- **Project Completion Summary** — Final verification checklist of all created files and next steps
- **Compilation** — Combine all chapters into a single manuscript file via scripts or AI
- **README Generation** — Auto-generated project README with progress tracking and badges

## Workflows

### 1. Initialization: Starting a New Book Project
When the user asks to start a new book project or "initialize the memory bank", follow these steps:

0. **Run The Story Forge first.** Read `references/story_forge.md` in full and follow its instructions. Ask questions one at a time to gather book details. Every question is skippable. If the memory bank Core files already exist, skip this step entirely — just read the memory bank and assist.
1. Copy the `assets/book-memory-bank/` directory to the root of the user's project workspace.
2. Read `references/author_rules.md` to adopt the persona and style of a master fiction author.
3. Help the user establish the foundational elements (concept, style, characters) by discussing the book's plan.
4. Use `references/character_worldbuilding_tables.md` for structured character profiles and worldbuilding tables when building out characters and settings. Offer to create `character_arcs.md` and `themes_and_motifs.md` using the templates in `assets/book-memory-bank/Core/Templates/`.
5. **Offer the Pacing Blueprint.** Ask if the user wants to pre-plan the book's structural arc now using `assets/book-memory-bank/Core/Templates/pacing_blueprint_template.md`. Save the completed file as `Core/pacing_blueprint.md`. Recommended for novels — skippable for short projects.
6. Record these elements into the newly created `book-memory-bank/Core/` and `book-memory-bank/Style/` Markdown files.
7. **Generate the project README.** Read `references/readme_template.md`, fill all `{{TOKEN}}` placeholders using answers from the brainstorming gate and the newly written memory bank files, and write the completed file as `README.md` in the project root. Do not ask the user to review it — just create it silently.

### 2. Writing & Outlining
When the user asks to outline or write chapters:
1. Always start by reading ALL memory bank files (`book-memory-bank/Core/`, `book-memory-bank/Style/`, and any existing master outline) to regain context.
2. Adopt the instructions in `references/author_rules.md` for generating high-quality narrative prose, realistic dialogue, and engaging scenes.
3. Consult `references/chapter_craft.md` for chapter structure templates, opening/closing formulas, and engagement techniques appropriate to the book type.
4. **For children's books (ages 2–9):** Also consult `references/childrens_book_craft.md` for age-appropriate vocabulary, rhyming/meter, illustration notes, and educational integration.
5. Write outlines in the `Outlines/Chapter_Outlines/` directory.
6. **After all chapter outlines are created**, auto-generate a `chapter-titles-guide.md` inside the `Outlines/` directory (see [Chapter Titles Guide](#chapter-titles-guide) below).
7. Write chapters in the `Chapters/` directory.
8. **For multi-chapter drafting**, consult `references/parallel_workflows.md` and offer parallel (background agents) or sequential drafting.

### 3. Compilation
If the user asks YOU (the AI) to compile or combine the book (rather than running the included scripts themselves):
1. Determine the user's OS. If Mac/Linux, attempt to run the provided bash script `book-memory-bank/Production/Scripts/combine_chapters.sh`. If Windows, run `combine_chapters.ps1`.
2. If the script fails or is unavailable, create the `Manuscript/` directory in the project root if it does not already exist.
3. Read all files from `Chapters/` in numerical order, combine them into a single file, and save it inside the `Manuscript/` folder (e.g., `Manuscript/Complete_Manuscript.md`).

### 4. Memory Updating Protocol (CRITICAL)
Maintaining the Book Memory Bank is essential for consistency. You must seamlessly and *automatically* update the memory bank whenever substantive writing is done. No scripts or manual user steps should be required.
1. Consult `references/book_memory_protocol.md` for the strict rules on how and when to update the memory bank files.
2. Consult `references/memory_update_prompts.md` for specific criteria on what changes should trigger file modifications (e.g., character traits, plot developments, world-building).
3. If the user explicitly says "update memory bank", perform a comprehensive audit and update across all memory files based on the most recent chapter or outline. Always provide a clear summary of which files were updated and what changed.

### 5. Chapter Review & Revision
When the user asks to review, revise, or polish a chapter:
1. Read the chapter draft, its outline, adjacent chapters (for continuity), and all context files (Style, Characters, Worldbuilding).
2. Consult `references/revision_checklist.md` for the quality gates and review focus areas.
3. **If reviewing Chapter 1**, also load `references/opening_chapter_checklist.md` and run its additional gates.
4. Conduct a **Scene Tension Map** analysis to ensure proper structural pacing.
5. Review in this order: Language → Emotion → Dialogue → Pacing → Continuity.
6. Apply revision principles: preserve voice above all, revise gently, clarify emotion without explaining, respect ambiguity.
7. **Never** introduce new scenes, events, or characters during review. **Never** resolve conflicts the author left open intentionally.
8. Save revised version and announce changes.

*(Users can request Specialized Revision Passes: Dialogue, Sensory, Prose Polish, or Tension & Pacing — see `references/revision_checklist.md`).*

### 6. Continuity Check
When the user asks to "check continuity", "run continuity check", or "check for consistency":
1. Follow the Continuity Diagnostic Report process in `references/book_memory_protocol.md`.
2. Cross-check all chapters against the memory bank for timeline, character, worldbuilding, emotional, and thematic consistency.
3. Generate a diagnostic report saved to `Research/continuity_diagnostic_report.md`.
4. Use question-based language — flag issues, don't impose fixes.

### 7. Parallel Chapter Drafting & Review
When multiple chapters need drafting or reviewing:
1. Consult `references/parallel_workflows.md` for the full workflow.
2. **Drafting:** Draft Chapter 1 manually for approval, then offer parallel (background agents) or sequential for remaining chapters.
3. **Review:** After all chapters are drafted, offer parallel or sequential review.
4. Always ask the user which approach they prefer before launching.

### 8. Complete & Present
After all chapters are drafted, reviewed, and continuity-checked:
1. Scan all chapter files for `[NEED RESEARCH]` flags and cross-reference against `Research/research_tracker.md`. All open items must be resolved or explicitly flagged before the manuscript is finalized.
2. Present a final verification summary listing all created files:
   - Foundation files (Characters, Worldbuilding, Synopsis, Timeline, Conflict, Style)
   - Chapter outlines and chapter titles guide
   - Drafted and reviewed chapters
   - Continuity diagnostic report
2. Suggest next steps (address continuity issues, refine chapters, compile manuscript).
3. Offer ongoing help: revise chapters, brainstorm scenes, refine arcs.

### 9. Starting a Spinoff
When the user mentions "spinoff", "companion book", "same world, different story", "side story", or asks to write a story about a secondary character from an existing project:
1. **Read `references/spinoff_guide.md` in full** before doing anything else.
2. Run the **Spinoff Forge** — the lightweight onboarding conversation defined in that file. Ask one question at a time; everything is skippable.
3. After approval, **initialize the spinoff directory structure** inside the parent project root:
   - Create `<spinoff-name>/book-memory-bank/` with Core and Style subdirectories
   - Fork or create memory bank files per the Inheritance Model in `references/spinoff_guide.md`
   - Copy shared characters and world sections from the parent's `world_and_characters.md`, marked with `[FROM: ParentTitle]`
4. At the start of every subsequent spinoff session, read the spinoff's memory bank **and** the parent's `world_and_characters.md`.
5. After every spinoff chapter, run the **Cross-Reference Protocol** to flag potential canon conflicts before saving.

## Chapter Titles Guide

**After chapter outlines are finalized, auto-generate a `chapter-titles-guide.md` inside the `Outlines/` directory.** No separate user approval is needed.

→ **Full instructions and column guide:** `references/chapter_titles_guide.md`
→ **Template:** `assets/book-memory-bank/Core/Templates/chapter_titles_guide_template.md`

## References
This skill relies on the following reference documents to guide the AI's behavior:
- `references/author_rules.md`: Provides the artistic identity, style guidelines, and quality standards for fiction writing. Includes dialogue language handling, historical title/honorific rules, and contextual address rules.
- `references/book_memory_protocol.md`: Outlines the architecture of the Book Memory Bank, explicit rules for maintaining context files, and the Continuity Diagnostic Report process.
- `references/memory_update_prompts.md`: Contains criteria and expected templates for auditing and updating the memory bank when significant story changes occur.
- `references/story_forge.md`: **The Story Forge** — governs the one-time onboarding conversation for new book projects. Includes genre selection, emotional core discovery, narrative structure choice, and dialogue language preference. Run only at initialization; never repeat.
- `references/readme_template.md`: Template for generating the project `README.md` after initialization.
- `references/chapter_craft.md`: Chapter-level writing techniques — opening/closing formulas, book size options, chapter structure templates, reader engagement techniques, drafting best practices.
- `references/revision_checklist.md`: Comprehensive quality checklist for chapters — story, prose, voice, characters, continuity, engagement, historical accuracy checks, and DO/DON'T quick-scan list.
- `references/character_worldbuilding_tables.md`: Structured table templates for character profiles (19 fields), worldbuilding (10 categories), conflict mapping, synopsis structure, and timeline tracking.
- `references/childrens_book_craft.md`: **Children's Book Craft** — age-based writing guidelines (2–9), rhyming/meter techniques, illustration notes, phonics/vocabulary, educational integration, values framework, and children's revision checklist.
- `references/parallel_workflows.md`: **Parallel Workflows** — simultaneous chapter drafting and review via background agents. Includes task templates, sequential fallbacks, and design principles.
- `references/punctuation_guide.md`: **Punctuation Guide** — mark-by-mark rules for every punctuation mark used in novel writing.
- `references/spinoff_guide.md`: **Spinoff Guide** — definitions, Spinoff Forge onboarding, directory convention, inheritance model, and cross-reference protocol.
- `references/opening_chapter_checklist.md`: **Opening Chapter Checklist** — dedicated quality gates for Chapter 1: hook, protagonist establishment, reader promise, and exposition checks.
- `references/query_letter_guide.md`: **Query Letter & Publishing Toolkit** — generate back-cover blurb, 1-page synopsis, query letter, and logline from the memory bank.
- `references/chapter_titles_guide.md`: **Chapter Titles Guide** — full instructions, dynamic structure rules (flat, parts, multi-book), and column guidelines for the auto-generated title reference.
- `docs/USAGE.md`: Human-readable guide with real example dialogues for every stage of using this skill.
