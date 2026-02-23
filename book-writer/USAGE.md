# 📖 Book Writer Skill — Usage Guide

> This guide explains how to work with the book-writer AI skill. You don't need to memorize any commands — just talk naturally. This document is here so you know what's possible.

---

## Quick Start

```
"Let's start building a new book"
```

That's it. The AI will take it from there.

---

## The Onboarding Conversation

When you start a new book, the AI runs a short setup conversation — **one question at a time**. Every question is optional. You can skip any of them.

Here's what a typical session looks like:

---

**AI:** Do you have any existing material — an outline, a draft, notes, or a prior version? If yes, share a file path or paste the content and I'll pull what I can from it. Otherwise just say 'no' or 'skip'.

**You:** I have a rough outline — *[pastes or provides file path]*

> ✅ The AI reads your draft and extracts everything it can. It skips questions already answered by your material.

---

**AI:** What's your name (or pen name), and do you have a title or working title in mind?

**You:** Shubhanshu. Working title is "The Last Peshwa"

---

**AI:** What genre best fits your book? Pick a number, name it, or describe something entirely different:
```
 1. Literary Fiction        7. Horror
 2. Historical Fiction      8. Romance
 3. Narrative History       9. Adventure / Action
 4. Fantasy (4a–4d)        10. Mystery / Detective
 5. Science Fiction         11. Biographical / Memoir
 6. Thriller / Suspense     12. Young Adult (YA)
                            13. Children's / Middle Grade
                            14. Short Story Collection
                            15. Other — describe it
```

**You:** Historical fiction — set during the Maratha Empire

> ✅ **Historical Accuracy Mode activates.** The AI will now keep all dates, figures, and events historically correct by default.

---

**AI:** What's the story about?

**You:** skip

> ✅ No pressure. It gets marked as TBD and you can define it later.

---

**AI:** Tell me about your main character and the setting.

**You:** Bajirao I — 18th century Maratha commander. Setting is the Deccan plateau and North India, 1720–1740.

---

**AI:** Any author whose style you want to echo? And roughly how long?

**You:** William Dalrymple's style. Full novel, 12 chapters.

---

**AI:**
```
Here's what we've got so far:

Title: The Last Peshwa
Author: Shubhanshu
Genre: Historical Fiction
Historical Mode: Yes
Protagonist: Bajirao I
Setting: Deccan plateau & North India, 1720–1740
Style: William Dalrymple
Chapters: ~12

Ready to initialize? Say yes — or tell me anything to adjust.
```

**You:** Yes

> ✅ AI initializes the memory bank, fills all core files, and generates a `README.md` in your project root.

---

## Skipping Everything

If you're in a hurry:

```
"Just start. I'll fill details in later."
"Skip all questions, initialize now."
```

The AI initializes immediately with defaults. You can update any details later by just telling the AI.

---

## Draft Import

If you already have notes, an outline, or a partial manuscript:

```
"I have some notes — here's the file: ./my_notes.md"
"I've been working on this — let me paste my outline: [paste]"
```

The AI reads it and skips any questions already answered. You won't be asked twice.

---

## Historical Accuracy Mode

Activates automatically when your genre is historical or you mention real historical figures.

**What it means:**
- All dates, battles, titles, and biographical facts default to what history records
- The AI flags uncertain or disputed facts and asks how you'd like to handle them

**If you want to invent something:**

```
"[FICTION] Bajirao meets a mysterious Persian spy in Delhi"
```

Prefix invented elements with `[FICTION]` — anywhere in conversation or in your draft. The AI accepts it and marks it in the memory bank, but never treats it as historical fact.

**Example:**

> **You:** I want Bajirao to survive Raverkhedi in my version
> 
> **AI:** Got it — I'll mark Bajirao's survival as `[FICTION]` in the memory bank. Historically he died there in April 1740 at 39, so I'll keep that recorded as the historical fact, but your narrative version will diverge from that point.

---

## Historical Titles & Honorifics

When writing about real historical figures, the AI only uses a title from the point in the timeline when the figure actually earned it. Titles are never applied retroactively.

| Figure | Before the title | After the title |
|---|---|---|
| Shivaji | *Shivaji* | *Chhatrapati Shivaji Maharaj* (June 1674 coronation) |
| Pratap Singh | *Pratap Singh / Kunwar Pratap* | *Maharana Pratap* (1572) |
| Bajirao | *Bajirao* | *Peshwa Bajirao* (1720 appointment) |

If the AI isn't sure when a title was conferred, it will say so and ask rather than guess.

### Within a scene, how a character is addressed depends on who is speaking

The narrator's default is the full canonical title. But different characters in the story address the same figure differently — and the AI handles this automatically:

| Speaker | Address they'd use | Why |
|---|---|---|
| Loyal courtier, formal setting | *Chhatrapati Shivaji Maharaj* | Deference and ceremony |
| Close companion, soldier, camp | *Maharaj* / *Shivaji Raje* | Familiarity and solidarity |
| Equal ruler or peer | *Bajirao* (no honorific) | Peer-level respect |
| Villain, enemy, contemptuous figure | *Pratap* / *"that Rajput"* | Deliberate degradation — characterises the speaker |
| Narrator, intimate or emotional moment | First name alone | Signals vulnerability or closeness |

**You don't need to instruct the AI** — it reads the scene's dramatic register and chooses accordingly. But you can always override:

```
"In this scene, Aurangzeb refers to Shivaji contemptuously — just 'Shivaji', no title."
"The narrator should use 'Bajirao' alone in the death scene, not 'the Peshwa'."
```

A villain calling Maharana Pratap just *"Pratap"* is not a mistake. It's characterisation — and the AI knows the difference.

---

## After Initialization — Just Write

Once the memory bank is set up, the AI never asks setup questions again. Just tell it what to do:

| What you say | What happens |
|---|---|
| `"Write chapter 1"` | AI reads all memory bank files and writes the chapter |
| `"Outline chapter 3"` | AI creates `Outlines/Chapter_Outlines/Chapter03_Outline.md` |
| `"Update memory bank"` | AI audits all files after a writing session |
| `"Check for consistency"` | AI checks characters and plot for contradictions |
| `"We finished chapter 5"` | AI updates memory bank automatically |

---

## The Memory Bank

The AI maintains a set of context files in `book-memory-bank/` so it never forgets your characters, world, or plot — even across sessions.

You never need to manage these files manually. The AI reads them at the start of every session and updates them after every chapter.

```
book-memory-bank/
├── Core/
│   ├── projectbrief.md       ← high-level concept & goals
│   ├── story_structure.md    ← themes, arcs, narrative patterns
│   ├── world_and_characters.md ← all characters, locations, world rules
│   ├── activeContext.md      ← what we're working on right now
│   └── progress.md           ← chapter completion tracking
└── Style/
    └── style_guide.md        ← prose voice, tone, stylistic rules
```

---

## Your Project README

A `README.md` is automatically created in your project root when you initialize. It includes:

- Book title, tagline, and genre badges
- About the book
- Scope table (time periods and story arcs)
- Central figures table
- Progress tracker
- Sources (if you provided them)

The AI **updates the progress tracker** automatically after each chapter is written. If you're on GitHub:
- **Public repo** — badges link to your repo
- **Private repo** — badges use placeholder links; update when you publish

---

## Trigger Phrases Cheat Sheet

| Phrase | Effect |
|---|---|
| `"Start a new book"` / `"Initialize memory bank"` | Runs onboarding gate |
| `"Just start"` / `"Skip all questions"` | Instant initialization, no questions |
| `"Write chapter [N]"` | Writes the chapter |
| `"Outline chapter [N]"` | Writes the chapter outline |
| `"Update memory bank"` | Full audit and update of all memory files |
| `"Check for consistency"` | Flags contradictions across memory bank |
| `"[FICTION] ..."` | Marks a statement as intentionally fictional (historical mode) |
| `"What chapter are we on?"` | AI reports current progress |
| `"Write the master outline"` | Creates `Outlines/Master_Outline.md` |

---

## Tips

- **You don't need to repeat context** — the AI reads the memory bank at the start of every session
- **Partial answers are fine** — say part of what you know; you can always add more later
- **Change your mind freely** — just tell the AI the new version and it updates the memory bank
- **For historical books** — providing your primary/secondary sources upfront helps the AI flag uncertainties accurately
