# Spinoff Guide — New Stories in Shared Worlds

Read this file in full when the user wants to create a spinoff, companion book, or any new story that shares characters, world, or lore with an existing project.

---

## Definitions

| Type | Definition |
|------|------------|
| **Spinoff** | A new, standalone book set in the same world or with some of the same characters as a parent project, but with a different central protagonist, plot, or time period |
| **Companion Book** | A spinoff told from a secondary character's POV, or exploring a side event from the parent's timeline |
| **Sequel** | A continuation of the same protagonist's story — use the standard multi-book workflow, not this guide |
| **Prequel** | A story set before the parent — same protagonist lineage; use this guide if the cast or premise differs substantially |
| **Same-World New Story** | Entirely new characters in the same world with no direct cast overlap |

If the user is unsure, ask: *"Is this continuing the same protagonist's main arc (sequel), or starting a new story in the same world (spinoff)?"*

---

## Trigger Phrases

Activate the Spinoff Forge when the user says any of:
- "spinoff" / "spin-off"
- "companion book"
- "same world, different story" / "same universe"
- "story about [secondary character]"
- "prequel" (if the cast or premise differs substantially from the parent)
- "side story"

---

## The Spinoff Forge

A lighter version of The Story Forge, focused on *what carries over* and *what is new*. Ask questions one at a time; everything is skippable.

### Step 1 — Identify the Parent Project

> "Which existing project is this spinning off from? Share the project name or folder path, and I'll read its memory bank to understand what we're inheriting."

Read the parent's `book-memory-bank/Core/` files silently before asking anything else.

---

### Step 2 — Inheritance Declaration

> "From the parent project, what are you bringing into this spinoff? Tell me what carries over — characters, world, factions, technology, lore — and what is completely new."

Use their answer to populate the **Inheritance Table** (see below). If they skip, infer reasonable defaults from the parent's memory bank and confirm with one follow-up.

---

### Step 3 — New Protagonist

> "Who is the central character of this spinoff? This can be a secondary character from the parent, or someone brand new."

---

### Step 4 — New Premise & Time Period

> "What's the core story? One or two sentences — or say 'skip' if you're still working it out. Also, does this take place during, before, or after the parent's timeline?"

---

### Step 5 — Style Divergence (Optional)

> "Should this spinoff have its own distinct voice and tone, or closely mirror the parent's style? (Say 'same' to copy the parent's style guide, 'different' to set a new one, or describe the difference.)"

---

### Step 6 — Summary & Approval

Present a concise brief:

```
Here's what we have for your spinoff:

Parent Project: [name]
Spinoff Title: [title or TBD]
Protagonist: [name or TBD]
Time Period: [before / during / after parent — or TBD]
Premise: [one line or TBD]
Inherited: [list of carried-over elements]
New: [list of new elements]
Style: [same as parent / distinct — description]

Ready to initialize? Say yes — or adjust anything.
```

On approval → run spinoff initialization (see below).

---

## Directory Structure

Spinoffs live as siblings to the parent project's content directories, under their own named folder:

```
<project-root>/
  Chapters/                      ← parent chapters
  Outlines/                      ← parent outlines
  book-memory-bank/              ← parent memory bank

  <spinoff-name>/
    Chapters/                    ← spinoff chapters
    Outlines/
      Chapter_Outlines/
      Master_Outline.md
    book-memory-bank/
      Core/
        projectbrief.md          ← FRESH
        story_structure.md       ← FRESH
        activeContext.md         ← FRESH
        progress.md              ← FRESH
        world_and_characters.md  ← FORKED (see inheritance model)
      Style/
        style_guide.md           ← FORKED or FRESH (author's choice)
    Research/
    Manuscript/
```

For same-world new stories (no shared characters at all), the parent memory bank still acts as the lore source — read it but don't copy it.

---

## Inheritance Model

| Memory Bank File | Treatment | Rule |
|---|---|---|
| `world_and_characters.md` | **Forked** | Copy shared characters and world sections from parent. Append new spinoff-only characters. Mark carried-over sections with `[FROM: ParentTitle]`. |
| `style_guide.md` | **Forked or Fresh** | Author's choice (Step 5 of Spinoff Forge). Copy parent style or start fresh. |
| `projectbrief.md` | **Fresh** | New title, premise, protagonist. Reference parent title under "Connected Projects". |
| `story_structure.md` | **Fresh** | New themes, arcs, emotional core. |
| `activeContext.md` | **Fresh** | Tracks spinoff-specific current status. |
| `progress.md` | **Fresh** | Tracks spinoff chapter completion. |
| `Outlines/` | **Fresh** | Spinoff-specific outlines only. |
| `Chapters/` | **Fresh** | Spinoff chapters only. |

### Marking Inherited Content

In the spinoff's `world_and_characters.md`, mark any section copied from the parent clearly:

```markdown
## [Character Name]
> *[FROM: Parent Title — inherited profile, last updated Chapter X of parent]*

[Copied profile content here]

### Developments in [Spinoff Title]
[Spinoff-specific updates below]
```

This makes it immediately obvious what is inherited and what evolved in the spinoff.

---

## Shared Canon Rules

These rules prevent parent and spinoff from contradicting each other:

1. **Parent canon is read-only in the spinoff by default.** The spinoff can expand on or reference parent events, but cannot retroactively change them.
2. **Fate of inherited characters** — if the spinoff reveals a significant fate or change for a character who still has an open arc in the parent, flag it:
   > *"⚠️ Canon Alert: [Character]'s fate in this spinoff may affect the parent's open arc. Confirm with author before writing."*
3. **Timeline consistency** — use the parent's timeline as the fixed reference. Note spinoff events relative to parent chapters.
4. **Worldbuilding changes** — if the spinoff introduces new world facts (new factions, locations, technology), note them as `[SPINOFF ADDITION]` and optionally backport them to the parent's memory bank.

---

## Cross-Reference Protocol

When updating the spinoff's memory bank after a chapter:

1. Check if any written event **contradicts** a fact in the parent's `world_and_characters.md` or timeline. If yes, flag it before saving.
2. Check if any written event **adds new canon** that the parent should know about. If yes, note it at the bottom of the spinoff's `activeContext.md`:

```markdown
## Proposed Parent Canon Additions
- [Spinoff Ch. X]: [Name] established that [world fact]. Consider adding to parent's world_and_characters.md.
```

3. Only backport to the parent's memory bank with explicit author approval.

---

## Spinoff Initialization Steps

On approval of the Spinoff Forge summary:

1. Create the spinoff directory structure inside the project root (see Directory Structure above).
2. Copy the memory bank asset template into `<spinoff-name>/book-memory-bank/`.
3. For `world_and_characters.md` — copy inherited sections from the parent, mark with `[FROM: ParentTitle]`, and add new spinoff characters.
4. For `style_guide.md` — copy from parent (if "same") or start fresh (if "different").
5. Fill `projectbrief.md` with the spinoff's premise, protagonist, and a "Connected Projects" entry pointing to the parent.
6. Generate a spinoff `README.md` or section in the project README noting the spinoff relationship.
7. Announce initialization complete and offer to begin outlining.

---

## Memory Bank Reading Protocol (Spinoff Sessions)

At the start of every spinoff session:

1. Read `<spinoff-name>/book-memory-bank/Core/` files fully.
2. Read the parent's `book-memory-bank/Core/world_and_characters.md` for shared character/world facts.
3. Do NOT re-read the entire parent's memory bank every session — only the world/character file unless a specific continuity question arises.
