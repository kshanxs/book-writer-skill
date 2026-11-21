# Changelog

All notable changes to the `book-writer` skill will be documented in this file.

## v3.0.0 — 2026-11-21

A major release focused on writing that sounds human, stories that stay consistent, and tools any author can use.

### Added
- **Book Tools:** one dependency-free command (`book.py`) for checks and exports on Mac, Linux, and Windows.
- **Prose Audit:** finds AI-sounding patterns with line numbers and suggested fixes, without editing the book.
- **Voice Baseline:** learns from the author's own writing so their real style is not flagged.
- **Humanizing guide:** word, rhythm, and story-level checks, plus safeguards against over-correction.
- **Cold Reader:** a blind review that reports where a chapter hooks, bores, or confuses.
- **Continuity Ledger:** checks deaths, promises, secrets, fixed facts, and name spelling.
- **EPUB export:** includes cover support, with validation when EPUBCheck is installed.
- **Optional integrations:** a Vale style pack and Harper grammar checks.
- **Credits:** `THIRD_PARTY_NOTICES.md` lists the open-source projects that inspired this release.

### Changed
- AI-written narration no longer uses em dashes. Dialogue may use one when a speaker is cut off, and the author's own dashes are left alone.
- Drafting, review, continuity, and final checks now use Book Tools.

### Upgrading an existing book
- Copy the new `Production/` folder, `Core/continuity_ledger.md`, and `Style/audit_ignore.txt` into your memory bank, or ask your assistant to do it.
- Your chapters and existing memory files do not need to change.

## v2.5.0 — 2026-11-21

### Fixed
- **Manuscript order:** Prologue, Epilogue, numbered Interludes, and mixed file names now compile in reading order. Old copies are skipped with a warning, and duplicate chapter numbers stop the build.
- **Export safety:** Failed builds no longer delete the previous manuscript or Word file. Unreadable chapters now stop the build.
- **Word output:** Chapters start on new pages, and a `---` scene break can no longer turn the line above it into a heading.
- **Empty and nested content:** Empty chapters are skipped with a warning, an all-empty book keeps the previous manuscript, and nested code fences no longer confuse scene breaks.
- **Windows export:** Custom `reference.docx` files are kept, Microsoft Word is optional, and scripts run under the default execution policy.
- **Memory:** Added the missing file index to `activeContext.md` and replaced conflicting read rules with one loading table per task.
- **Onboarding, spinoffs, and publishing:** Fixed the fast-track step, duplicate genre question, spinoff links and inheritance rules, companion skill detection, and publishing guides that read missing files.
- **Cover guidance:** Corrected the KDP portrait size and Midjourney aspect ratio.

### Added
- Unique revision snapshots in `Revisions/` before chapters are overwritten, including neighboring chapters for parallel reviews.
- A research-flag gate for final builds, with `--draft` for review copies.
- Style precedence, so the author's choices override skill defaults.
- Non-fiction genres in The Story Forge and an AI disclosure check before publishing.
- Script tests (`tests/test_scripts.sh`) and a documentation check (`scripts/check_repo.py`).

### Changed
- Rewrote the README and removed leftover setup instructions for another tool.

### Upgrading an existing book
- Copy the new `Production/Scripts/` folder into your project's memory bank.
- Add the `Memory Status & File Index` section to `activeContext.md`, or ask your assistant to do it.
- If your custom `reference.docx` has "page break before" on Heading 1, turn it off to avoid blank pages.

## v2.4.0 — 2026-06-22
- **Calligraph Sensei Proofreader Synergy:** Integrated support for Calligraph Sensei's new conservative **Proofreading / Correction** mode to allow spelling/grammar checks of sequential drafts without mutating character voices or structural outline tags.

## v2.3.0 — 2026-06-21
- **Research Dojo Synergy & Gated Installation:** Enabled modular fact-checking capabilities by dynamically detecting the sibling `Research Dojo` skill.
  - Added dynamic skill detection in `SKILL.md` using `skills-lock.json` to enable a dedicated "Factual Audit Mode".
  - Implemented boundary conditions separating `book-writer` narrative style guidelines from `research-dojo` adversarial logic.
  - Added proactive genre checks that prompt the user to install `research-dojo` when starting a non-fiction book format.
  - Updated the repository `README.md` with instructions on how to run both skills together.

## v2.2.0 — 2026-06-21
- **Sequential Prose Drafting Enforced:** Prohibited parallel prose drafting to resolve the narrative dependency paradox. Sequential drafting is now the default, restricting concurrent agents strictly to outlining, scene cards, and reviews.
- **Smart-Reading Protocol:** Transitioned core workflow from bulk-loading all memory bank files to an on-demand protocol indexed via `activeContext.md` to prevent latency and prompt bloat.
- **Reference-Based Spinoff Model:** Replaced copy-paste character inheritance in spinoffs with relative markdown link referencing, solving the "split-brain" data synchronization issue.

## v2.1.1 — 2026-06-18
- **Popular Science & Tech History Support:** Added a new `popscience_history_rules.md` reference file to support popular science, technology history, and narrative non-fiction books.
- **Checklist Quality Gates:** Integrated new checkpoints into `revision_checklist.md` to verify tense split, visual analogies, chronological tech accuracy, and paper quote formatting.

## v2.1.0 — 2026-06-18
- **World & Tech Gita (Story Gitas) Template:** Added the new `world_gita_template.md` template file to support deep technology, magic systems, and lore documentation.
- **Advanced Prose Style Guidelines:** Codified guidelines for Readability First (High Readability Standard), Narrator Warmth, Tech/Magic Introduction Rule (One-Sentence Context Rule), and Character Name/Number conventions in `author_rules.md`.
- **Integrated Quality Gates:** Updated `revision_checklist.md` with checkpoints to verify readability, warmth, name usage, and tech/magic introductions during chapter reviews.
- **Protocol & Workflow Updates:** Integrated World Gita files (`world_gita.md`) into the core memory bank flowcharts, update protocols, and review checklists.

## v2.0.1 — 2026-03-19
- **Memory Bank File Management:** Added guidance on when to split `world_and_characters.md`. Growing is expected — only split at ~200–300KB, and split by concern (characters vs. deep lore), never by character.

## v2.0
- Initial public release with full memory bank system, parallel drafting, spinoff support, and publishing toolkit.
