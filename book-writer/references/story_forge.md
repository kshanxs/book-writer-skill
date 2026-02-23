# Brainstorming Gate — New Book Initialization

This file governs the onboarding conversation when a user starts a new book. **Read this file in full before asking the user a single question.**

---

## When to Run This Gate

Run this gate ONLY when ONE of these triggers occurs AND the memory bank does not yet exist:

- `"start a new book"`
- `"initialize memory bank"`
- `"let's start building"`
- `"help me write a book"`
- `"new book project"`

**If the memory bank Core files already exist → skip this gate entirely.** The user has already onboarded. Just read the memory bank and assist.

---

## Core Principles

1. **One question at a time.** Never stack multiple questions in one message.
2. **Everything is optional.** If the user says "skip", "not sure", "doesn't matter", or gives a blank answer — accept it and move on.
3. **Run once, never again.** After the gate completes and files are initialized, never repeat this onboarding process. In future sessions, read the memory bank silently and begin.
4. **No repeated pinging.** If the user seems in a rush (e.g., says "just start", "skip everything", "initialize now") — skip all remaining questions, use reasonable defaults, and initialize immediately.
5. **Draft-first.** If the user provides existing material (a draft, outline, notes, file path), extract everything you can from it and skip questions already answered by that material.
6. **Respect the user's time.** Keep each question brief. If the user gives a short answer, accept it. Don't ask follow-ups unless something is genuinely ambiguous and important.

---

## The Gate Flow

### Step 0 — Fast-Track Check

Before asking anything, check if the user's initial message already contains enough information to start. If yes, skip to Step 6 (summary).

If the user says anything like:
- "just start"
- "skip everything" / "skip all questions"
- "initialize now"
- "I'll fill in details later"

→ **Immediately initialize with defaults and skip all gate questions.**

---

### Step 1 — Draft Import

Ask **only this**:

> "Do you have any existing material — an outline, a draft, notes, or a prior version? If yes, share a file path or paste the content and I'll pull what I can from it. Otherwise just say 'no' or 'skip'."

- If user provides material: extract author name, title, genre, characters, setting, and any other relevant details. Pre-fill answers for subsequent steps.
- If user says no/skip: proceed to Step 2.

---

### Step 2 — Author & Title

Ask:

> "What's your name (or pen name), and do you have a title or working title in mind? (Say 'skip' to skip either.)"

Accept whatever they give. Single-word answers are fine.

---

### Step 3 — Genre

Present the following menu and ask the user to pick one (or describe their own):

> "What genre best fits your book? Pick a number, name it, or describe something entirely different:"

```
FICTION
  1.  Literary Fiction          — character-driven, prose-focused, realistic
  2.  Historical Fiction        — real era, may blend real + invented figures
  3.  Narrative History         — non-fiction storytelling of real events
  4.  Fantasy                   — magic, mythological, or secondary world
      4a. Epic / High Fantasy
      4b. Mythological / Folk Fantasy
      4c. Dark Fantasy
      4d. Historical Fantasy     — real era + fantastical elements
  5.  Science Fiction
      5a. Hard Sci-Fi            — grounded in science
      5b. Space Opera            — sweeping interstellar scope
      5c. Dystopian / Post-Apoc
      5d. Cyberpunk / Biopunk
  6.  Thriller / Suspense
      6a. Political Thriller
      6b. Spy / Espionage
      6c. Crime / Noir
      6d. Psychological Thriller
  7.  Horror
      7a. Gothic Horror
      7b. Folk / Cosmic Horror
      7c. Psychological Horror
  8.  Romance
      8a. Contemporary Romance
      8b. Historical Romance
      8c. Paranormal Romance
  9.  Adventure / Action
  10. Mystery / Detective
  11. Biographical / Memoir      — real person's life, first or third person
  12. Young Adult (YA)          — any genre, YA lens
  13. Children's / Middle Grade
  14. Short Story Collection
  15. Other — describe it
```

Accept any answer — a number, a genre name, a mix (e.g., "historical fantasy"), or a free description.

**If the user picks 2, 3, 11, or mentions real historical figures/events, or describes a real era:**
→ Activate **Historical Accuracy Mode** (see section below).

**If the user picks a genre with subgenres (4–8) and hasn't specified one:**
→ Ask ONE follow-up: *"Any particular subgenre — [list the subgenres for that number]? Or just say 'general' to keep it broad."*

---

### Step 4 — Story Core

Ask:

> "What's the story about? Give me a sentence or two — or say 'skip' if you're not sure yet."

If the user gives a premise, great. If they skip, note it as TBD in the project brief.

---

### Step 5 — Characters & World

Ask:

> "Tell me about your main character and the world or setting. Who are they, and where/when does this story take place? Skip anything you're not sure about."

Accept partial answers. If nothing is provided, mark as TBD.

---

### Step 6 — Dialogue Language (Optional)

Ask:

> "Any specific local language or dialect you want to weave into the dialogue when appropriate? (Like Hinglish, Marathi, French, etc.) Or just standard English?"

Accept their preference or "skip".

---

### Step 7 — Style & Scope (Optional)

Only ask this if conversation is flowing naturally. If the user seems in a hurry, skip it:

> "Any author whose style you want to echo? And roughly how long — a short novel, full novel, or open-ended? (Both optional.)"

---

### Step 8 — GitHub Visibility (Optional)

Only ask if the user hasn't mentioned GitHub yet:

> "Will you be hosting this on GitHub? If so — public or private? (This affects how your project README is generated. Say 'skip' to skip.)"

Store the answer as one of: `public`, `private`, `none`.

---

### Step 9 — Summary & Approval

Present a concise project brief:

```
Here's what we've got so far:

Title: [title or TBD]
Author: [name or TBD]
Genre: [genre]
Historical Mode: [Yes / No]
Premise: [one line or TBD]
Protagonist: [name/description or TBD]
Setting: [or TBD]
Dialogue Language: [language or English]
Style: [or TBD]
GitHub: [public / private / none]

Ready to initialize? Say yes — or tell me anything to adjust.
```

On approval → run Workflow 1 initialization (copy memory bank, fill Core files, generate README.md).

---

## Historical Accuracy Mode

**Activated when:** genre is historical, narrative history, biographical, or historical fantasy — OR the user mentions real historical figures or events.

### Rules
- All dates, names, battle outcomes, and biographical facts default to historically recorded values.
- If the user wants a fictional element (invented character, altered timeline, fictitious event), they prefix it with `[FICTION]` in conversation or in their draft. The AI accepts it, marks it as `[FICTION]` in the memory bank, and never treats it as historical fact.
- When encountering gaps or disputed facts, the AI flags them:
  > *"The exact date of X is uncertain in the sources. Shall I use the most commonly cited date, or mark it as approximate?"*
- Historical accuracy applies to: names, dates of birth/death, battles, political events, titles, geographic names, and genealogy.
- It does **not** constrain: prose style, dialogue, interiority, or narrative framing — those are the author's creative domain.

### Title & Honorific Timeline Rule (CRITICAL)

Historical figures must be addressed **only by the titles and honorifics they held at the specific point in the narrative timeline.** A title earned later in life must NOT be applied retroactively to earlier periods.

**The rule:** For every named historical figure, record:
1. Their name at birth / before titles
2. Each title or honorific they received and the **exact date / event** that conferred it
3. Their full formal address after each title was conferred

The AI applies the correct form of address based on where the narrative currently sits in the timeline.

**Canonical examples:**

| Figure | Before title | Title conferred | Correct address after |
|---|---|---|---|
| Shivaji | Shivaji (no prefix) | Crowned Chhatrapati at Raigad, June 1674; title *Kshatriyakulavatamsa Kshatriyapati* conferred | Chhatrapati Shivaji Maharaj |
| Pratap Singh | Pratap Singh (prince) | Became Maharana of Mewar after Udai Singh II's death, 1572 | Maharana Pratap |
| Bajirao I | Bajirao (son of Balaji Vishwanath) | Appointed Peshwa in 1720 by Chhatrapati Shahu | Peshwa Bajirao / Bajirao Peshwa |

**In practice:**
- If a scene is set before 1674, refer to: *Shivaji* (not Chhatrapati Shivaji Maharaj)
- If a scene is set after June 1674, refer to: *Chhatrapati Shivaji Maharaj*
- If writing about Pratap Singh before 1572: *Pratap Singh* or *Kunwar Pratap*
- If writing about him after 1572: *Maharana Pratap*

**Recording in memory bank:** When a new historical figure is added to `world_and_characters.md`, always include a `Title Timeline` section:
```
### [Figure Name]
- Birth name: ...
- Title Timeline:
  - [Date/Event]: received title "..."; address changes to "..."
  - [Date/Event]: received title "..."; address changes to "..."
- Current address in narrative (as of chapter X): ...
```

**When the AI is uncertain** about when a title was conferred:
> *"I'm not certain of the exact date [figure] received the title '[title]'. Do you have a source, or shall I mark it as 'circa [year]' and flag it?"*

---

## After the Gate — Never Repeat

Once the gate has run and the memory bank files exist:
- **Do not run the gate again**, ever, in any session.
- **Do not ask any of these setup questions** in future sessions.
- In all future sessions: silently read memory bank files and assist with the current task.
