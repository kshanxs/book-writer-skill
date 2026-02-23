# 📖 Book Writer Skill — Usage Guide

> You don't need to memorize any commands. Just talk naturally. This guide shows you what's possible and exactly what the conversation looks like at every stage.

---

## Quick Start

```
"Let's start building a new book"
```

That's it. The AI takes it from there — one question at a time.

---

## The Story Forge — Onboarding Conversation

When you start a new book, the AI runs **The Story Forge**: a short setup conversation, one question at a time. Every question is optional. Say "skip" at any point.

### Full example — starting from scratch

**You:** `"Let's start building a new book."`

**AI:** *"Do you have any existing material — an outline, draft, or notes? If yes, share a file path or paste the content. If not, just say 'no'."*

**You:** *"No, I'm starting from scratch."*

**AI:** *"What's your name or pen name, and do you have a working title?"*

**You:** *"Shubhanshu. No title yet."*

**AI:**
```
What genre best fits your book?

 1. Literary Fiction       6. Thriller / Suspense
 2. Historical Fiction      7. Horror
 3. Narrative History       8. Romance
 4. Fantasy (4a–4d)         9. Adventure / Action
 5. Science Fiction        10. Mystery / Detective
                           11. Biographical / Memoir
                           12. Young Adult (YA)
                           13. Children's / Middle Grade
                           14. Short Story Collection
                           15. Other — describe it
```

**You:** *"2 — Historical Fiction."*

**AI:** *"Historical Accuracy Mode is now on. All dates, titles, and events default to the historical record. You can mark invented elements with `[FICTION]` anytime. What's the story about?"*

**You:** *"The rise of the Maratha Empire — seen through the eyes of Bajirao I."*

**AI:** *"Tell me about Bajirao at the start of the story."*

**You:** *"Young commander, tactical genius, appointed Peshwa at 19. Wants to make the Marathas the dominant power in India."*

**AI:** *"Any author's style you want to echo? And roughly how many chapters?"*

**You:** *"William Dalrymple. Around 12 chapters."*

**AI:**
```
Here's your project brief:

Title:    (working title TBD)
Author:   Shubhanshu
Genre:    Historical Fiction
Mode:     Historical Accuracy ON
Premise:  Rise of the Maratha Empire through Bajirao I
Lead:     Bajirao — appointed Peshwa at 19, tactical genius
Style:    William Dalrymple
Chapters: ~12
GitHub:   Not set

Ready to initialize? Say yes — or tell me anything to change.
```

**You:** *"Yes."*

> ✅ AI initializes the memory bank, fills all Core files, and generates a `README.md` in your project root.

---

### Starting with an existing draft

**You:** *"I have some notes already. Here's my outline file: `./my_outline.md`"*

**AI:** *[reads file]* *"Got it — I've extracted: Title, Genre, Protagonist, Setting, Scope. A few things I didn't find — what's your name, and any style you're going for?"*

**You:** *"Shubhanshu. Dalrymple's style."*

**AI:** *"Anything for GitHub — public, private, or skip?"*

**You:** *"Private."*

> ✅ Initializes. Draft import skips any questions already answered by the file.

---

### Skipping everything

```
"Just initialize now. I'll fill in details later."
"Skip all questions."
```

> ✅ AI initializes immediately with no questions. Fill in the memory bank any time by just telling the AI.

---

## Developing Characters Mid-Project

After initialization, develop any character through conversation:

**You:** *"Let's build out Nizam-ul-Mulk as a character."*

**AI:** *"What's his role — antagonist, rival, foil to Bajirao?"*

**You:** *"Antagonist. He's the one Bajirao keeps outmanoeuvring."*

**AI:** *"Historically, Nizam-ul-Mulk was a capable but cautious strategist — his defeats at Palkhed (1728) and Bhopal (1738) came from being drawn into terrain that neutralised his strengths. Do you want him as a purely strategic antagonist, or give him a personal through-line?"*

**You:** *"Personal pride. He genuinely believes he's the superior strategist."*

**AI:** *"Strong ironic position. Shall I add him to the memory bank with that psychological profile?"*

**You:** *"Yes."*

> ✅ `world_and_characters.md` updated — Nizam-ul-Mulk entry added with role, historical background, and psychological profile.

---

## Historical Accuracy Mode

Activates automatically when your genre is historical or you mention real figures.

- All dates, battles, titles, and facts default to what history records
- The AI flags uncertain or disputed facts and asks how you'd like to handle them

### Flagging a fiction element

```
"[FICTION] Bajirao to have a younger brother who fights at Palkhed."
```

> **AI:** *"Added and marked `[FICTION]`. He won't be treated as a historical figure. Do you have a name, or shall I suggest a period-appropriate one?"*

> **You:** *"Suggest one."*

> **AI:** *"How about Vikram Rao Bhat? Common Chitpavan surname, fits the period."*

---

## Historical Titles & Honorifics

The AI only uses a title from the point in the timeline when the figure actually earned it. Never retroactively.

| Figure | Before the title | After the title |
|---|---|---|
| Shivaji | *Shivaji* | *Chhatrapati Shivaji Maharaj* (June 1674 coronation) |
| Pratap Singh | *Pratap Singh / Kunwar Pratap* | *Maharana Pratap* (1572) |
| Bajirao | *Bajirao* | *Peshwa Bajirao* (1720 appointment) |

### Within a scene — who is speaking changes the address

The narrator uses the canonical title. But different characters address the same figure differently:

| Speaker | What they'd say | Why |
|---|---|---|
| Loyal courtier, formal setting | *Chhatrapati Shivaji Maharaj* | Deference and ceremony |
| Close companion / soldier | *Maharaj* / *Shivaji Raje* | Familiarity |
| Equal or rival ruler | *Bajirao* | Peer-level address |
| Villain / enemy | *Pratap* / *"that Rajput"* | Deliberate degradation — reveals the speaker |
| Narrator, intimate or death scene | First name alone | Signals humanity over politics |

The AI reads the scene's register and chooses automatically. But you can always override:

```
"In this scene, Aurangzeb refers to Shivaji contemptuously — just 'Shivaji', no title."
"Use 'Bajirao' alone in the death scene, not 'the Peshwa'."
```

### Example — same moment, two perspectives

**You:** *"Write a scene where Aurangzeb hears about Shivaji's coronation. He's furious."*

> AI writes Aurangzeb's courtiers using *"Chhatrapati Shivaji Maharaj"* in narration — but Aurangzeb himself says *"this Shivaji"*, stripped bare. The contrast characterises his refusal to acknowledge the title's legitimacy.

**You:** *"Now write the same moment from the Maratha camp."*

> Maratha soldiers shout *"Chhatrapati Maharaj ki jai!"* — full title, full reverence. Narrator uses the canonical form throughout.

---

## Developing a Chapter

**You:** *"Write the outline for Chapter 3."*

> AI reads all memory bank files silently. Returns a full outline.

**You:** *"Add a scene where Bajirao scouts alone at night — quieter, more internal."*

**AI:** *"Added — Chapter 3, Scene 4: Night reconnaissance. Internal monologue. Should it resolve in confidence or doubt?"*

**You:** *"Doubt. He's not sure the gamble will work."*

**AI:** *"Good — that makes the Palkhed victory more earned. Updating the outline now."*

---

## Updating the Memory Bank

**You:** *"We just finished Chapter 5. Update the memory bank."*

**AI:** *[reads Chapter 5 in full]*

> ✅ **Book Memory — Updates after Chapter 5:**
> - `world_and_characters.md` — Nizam-ul-Mulk: Chapter 5 developments added
> - `activeContext.md` — current position: end of Chapter 5; next chapter: Delhi march
> - `progress.md` — Chapter 5 marked complete
> - `story_structure.md` — "speed vs. mass" theme reinforced; noted for Chapter 6 callback

---

## Checking Consistency

**You:** *"Check for consistency issues."*

**AI:** *"Found one: in Chapter 2, scene 3, Bajirao is called 'Peshwa Bajirao' — but the scene is set in 1717, three years before his appointment. Correct it to 'Bajirao'?"*

**You:** *"Yes, fix it."*

> ✅ Chapter_02.md corrected. Memory bank note added.

---

## The Memory Bank

The AI maintains context files in `book-memory-bank/` — it reads them at the start of every session and updates them automatically after writing. You never manage them manually.

```
book-memory-bank/
├── Core/
│   ├── projectbrief.md         ← concept & goals
│   ├── story_structure.md      ← themes, arcs, narrative patterns
│   ├── world_and_characters.md ← all characters, locations, world rules
│   ├── activeContext.md        ← current session focus
│   └── progress.md             ← chapter completion tracking
└── Style/
    └── style_guide.md          ← prose voice, tone, stylistic rules
```

---

## Your Project README

A `README.md` is generated in your project root on initialization — title, badges, scope table, characters, progress tracker, and sources. The progress tracker updates automatically as chapters are written.

- **Public GitHub repo** → badges link to your repo
- **Private repo** → placeholder links; update when you publish

---

## Trigger Phrases — Quick Reference

| Say this | What happens |
|---|---|
| `"Let's start building a new book"` | Runs The Story Forge onboarding |
| `"Just initialize now"` | Skips all questions, starts immediately |
| `"Here's my outline: ./path"` | Draft import — AI extracts and skips answered questions |
| `"Let's build out [character]"` | Character brainstorming conversation |
| `"[FICTION] ..."` | Mark an invented element in historical mode |
| `"Write chapter [N]"` | Writes the chapter |
| `"Outline chapter [N]"` | Writes the chapter outline |
| `"Write the master outline"` | Creates `Outlines/Master_Outline.md` |
| `"Update memory bank"` | Full audit and update of all memory files |
| `"Check for consistency"` | Flags contradictions across memory bank |
| `"What chapter are we on?"` | AI reports current progress |
| `"In this scene, [speaker] calls him just '[name]'"` | Override address register for a scene |

---

## Tips

- **You don't repeat context** — AI reads the memory bank at the start of every session
- **Partial answers are fine** — say what you know; add more later
- **Change your mind freely** — just tell the AI the new version, it updates the memory bank
- **For historical books** — providing your primary sources upfront helps the AI flag uncertainties accurately
