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

## Context Efficiency Rule

**CRITICAL — Read this before loading any files.**

This skill has many reference files. Do NOT pre-load them all. Use **lazy loading** — only read a reference file when its specific feature is needed:

| Only load this file... | When... |
|------------------------|---------|
| `references/author_rules.md` | Starting a session, drafting, or reviewing |
| `references/chapter_craft.md` | Writing or outlining chapters |
| `references/revision_checklist.md` | Reviewing or revising chapters |
| `references/book_memory_protocol.md` | Updating memory bank or running continuity check |
| `references/memory_update_prompts.md` | Performing a comprehensive memory audit |
| `references/story_forge.md` | Only during initialization |
| `references/readme_template.md` | Only when generating the project README |
| `references/character_worldbuilding_tables.md` | Building character profiles or worldbuilding tables |
| `references/childrens_book_craft.md` | Only for children's book projects |
| `references/parallel_workflows.md` | Only when parallel drafting |
| `references/punctuation_guide.md` | Running a punctuation pass or prose polish |
| `references/spinoff_guide.md` | Only for spinoff projects |
| `references/opening_chapter_checklist.md` | Only when reviewing Chapter 1 |
| `references/query_letter_guide.md` | Only when user asks for blurb, synopsis, or query letter |
| `references/popscience_history_rules.md` | Writing or reviewing popular-science, technical history, or narrative non-fiction |
| `Core/world_gita.md` (or `tech_gita.md`) | Reading world technology, magic, or lore rules |
| Template files | Only when generating the specific document |

**Never load more than 3–4 reference files at once unless explicitly required by the task.**

## Workflows

### 1. Initialization: Starting a New Book Project
When the user asks to start a new book project or "initialize the memory bank", follow these steps:

0. **Evaluate Genre and Skills:**
   - Read `skills-lock.json` in the root (if it exists) and ask about the project's genre.
   - If the book is narrative non-fiction, popular science, biography, or history, check if `research-dojo` is installed.
   - If NOT installed, recommend the user install it for factual/claim verification:
     > *"I noticed this is a non-fiction book project. The `research-dojo` skill can help verify historical dates and scientific paper details. Would you like me to install it?"*
     Offer to execute: `npx skills add https://github.com/kshanxs/skill-dojo --skill research-dojo` using the `run_command` tool.
   - **Evaluate Style Companion:** Check if `calligraph-sensei` is installed. If NOT, recommend the user install it for advanced humanization, prose styling, and writing cadence diagnostics:
     > *"Would you like me to install `calligraph-sensei`? It integrates with Book Writer to polish chapters, enhance sensory language, and vary sentence structures for fiction/non-fiction."*
     Offer to execute: `npx skills add https://github.com/kshanxs/skill-dojo --skill calligraph-sensei` using the `run_command` tool.
0a. **Run The Story Forge.** Read `references/story_forge.md` in full and follow its instructions. Ask questions one at a time to gather book details. Every question is skippable. If the memory bank Core files already exist, skip this step entirely — just read the memory bank and assist.
1. Copy the `assets/book-memory-bank/` directory to the root of the user's project workspace.
2. Read `references/author_rules.md` to adopt the persona and style of a master fiction author.
3. Help the user establish the foundational elements (concept, style, characters) by discussing the book's plan.
4. Use `references/character_worldbuilding_tables.md` for structured character profiles and worldbuilding tables when building out characters and settings. Offer to create `character_arcs.md`, `themes_and_motifs.md`, or a `world_gita.md` (or `tech_gita.md` / `lore_gita.md` for detailed tech/magic/lore) using the templates in `assets/book-memory-bank/Core/Templates/`.
5. **Offer the Pacing Blueprint.** Ask if the user wants to pre-plan the book's structural arc now using `assets/book-memory-bank/Core/Templates/pacing_blueprint_template.md`. Save the completed file as `Core/pacing_blueprint.md`. Recommended for novels — skippable for short projects.
6. Record these elements into the newly created `book-memory-bank/Core/` and `book-memory-bank/Style/` Markdown files.
7. **Generate the project README.** Read `references/readme_template.md`, fill all `{{TOKEN}}` placeholders using answers from the brainstorming gate and the newly written memory bank files, and write the completed file as `README.md` in the project root. Do not ask the user to review it — just create it silently.

### 2. Writing & Outlining
When the user asks to outline or write chapters:
1. **Initialize the Smart-Reading Protocol:** 
   - Read `book-memory-bank/Core/activeContext.md` and check `skills-lock.json` in the root.
   - **Dojo Synergy:** If `research-dojo` is installed, enable **Factual Audit Mode**. Scan the project's `Research/` directory for any Dojo audit files (e.g., `dojo_dossier.md` or `paper_audit_[name].md`). Ingest these as primary factual sources and record the active integration status in `activeContext.md`.
   - Consult the memory status index to check which files have changed, or if it is a fresh session. Only load other files (like characters, worldbuilding, or style guides) if they have been updated or if the task directly targets their specific domain.
2. Adopt the instructions in `references/author_rules.md` for generating high-quality narrative prose, realistic dialogue, and engaging scenes.
3. Consult `references/chapter_craft.md` for chapter structure templates, opening/closing formulas, and engagement techniques appropriate to the book type.
4. **For children's books (ages 2–9):** Also consult `references/childrens_book_craft.md` for age-appropriate vocabulary, rhyming/meter, illustration notes, and educational integration.
5. Write outlines in the `Outlines/Chapter_Outlines/` directory.
6. **After all chapter outlines are created**, auto-generate a `chapter-titles-guide.md` inside the `Outlines/` directory (see [Chapter Titles Guide](#chapter-titles-guide) below).
7. Write chapters in the `Chapters/` directory.
8. **For multi-chapter workflows**, consult `references/parallel_workflows.md`. Recommend sequential drafting for prose chapters to preserve narrative continuity, and reserve parallel workflows (background agents) strictly for outlining, creating scene cards, and conducting edit/review passes.

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
    - **Advanced Stylistic Polish & Proofreading:** If `calligraph-sensei` is installed, delegate the advanced style pass to it using **Creative/Fiction** mode (or General/Academic-Formal depending on book genre) for creative prose adjustments, or use its **Proofreading / Correction** mode for a conservative error-correction pass that leaves the story style and character dialogue voices completely untouched.
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
When multiple chapters need drafting, outlining, or reviewing:
1. Consult `references/parallel_workflows.md` for the full workflow constraints.
2. **Drafting:** Prose drafting of sequential narrative chapters must be performed **sequentially** to preserve continuity. Parallel drafting is restricted strictly to non-sequential scene cards or outlining.
3. **Review:** After chapters are drafted, offer parallel (using background agents) or sequential review and editing.
4. Always explain the continuity requirements and ask the user for their preferred approach before launching background tasks.

### 8. Complete & Present
After all chapters are drafted, reviewed, and continuity-checked:
1. Scan all chapter files for `[NEED RESEARCH]` flags and cross-reference against `Research/research_tracker.md`. All open items must be resolved or explicitly flagged before the manuscript is finalized.
2. Present a final verification summary listing all created files:
 - Foundation files (Characters, Worldbuilding, Synopsis, Timeline, Conflict, Style)
 - Chapter outlines and chapter titles guide
 - Drafted and reviewed chapters
 - Continuity diagnostic report
3. Suggest next steps (address continuity issues, refine chapters, compile manuscript).
4. Offer ongoing help: revise chapters, brainstorm scenes, refine arcs.

### 9. Starting a Spinoff
When the user mentions "spinoff", "companion book", "same world, different story", "side story", or asks to write a story about a secondary character from an existing project:
1. **Read `references/spinoff_guide.md` in full** before doing anything else.
2. Run the **Spinoff Forge** — the lightweight onboarding conversation defined in that file. Ask one question at a time; everything is skippable.
3. After approval, **initialize the spinoff directory structure** inside the parent project root:
 - Create `<spinoff-name>/book-memory-bank/` with Core and Style subdirectories
 - Set up memory bank files per the reference-based Inheritance Model in `references/spinoff_guide.md`
 - Link shared characters and world sections from the parent's `world_and_characters.md` using relative Markdown links, rather than duplicating the entire content blocks.
4. At the start of every subsequent spinoff session, read the spinoff's memory bank files and resolve/read any referenced sections of the parent's `world_and_characters.md` as needed.
5. After every spinoff chapter, run the **Cross-Reference Protocol** to flag potential canon conflicts before saving.

## Boundary Protocol (Synergy with Research Dojo)
When operating in a project with both `book-writer` and `research-dojo` installed:
- Treat all files generated by `research-dojo` in the `Research/` directory as factual source-of-truth reference material.
- Do NOT adopt the adversarial, hyper-skeptical critic persona of the Dojo when drafting narrative prose or revising chapters. Preserve the Master Author narrative register (Walter Isaacson voice, narrative warmth, and emotional resonance) at all times.
- Keep the technical details focused and readable (adhering to the 80–90% narrative ratio and equation budget in the Style Guide) by translating dense Dojo analyses into simple visual analogies.

## Chapter Titles Guide

**After chapter outlines are finalized, auto-generate a `chapter-titles-guide.md` inside the `Outlines/` directory.** No separate user approval is needed.

→ **Full instructions and column guide:** `references/chapter_titles_guide.md`
→ **Template:** `assets/book-memory-bank/Core/Templates/chapter_titles_guide_template.md`
