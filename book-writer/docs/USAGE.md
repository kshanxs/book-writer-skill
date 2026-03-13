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

**AI:** *"Historical genre features are now active. All dates, titles, and events default to the historical record. You can mark invented elements with `[FICTION]` anytime. What's the story about?"*

**You:** *"The rise of the Maratha Empire — seen through the eyes of Bajirao I."*

**AI:** *"Tell me about Bajirao at the start of the story."*

**You:** *"Young commander, tactical genius, appointed Peshwa at 19. Wants to make the Marathas the dominant power in India."*

**AI:** *"Any author's style you want to echo? And roughly how many chapters?"*

**You:** *"William Dalrymple. Around 12 chapters."*

**AI:** *"Any specific local language or dialect you want to weave into the dialogue when appropriate? (Like Hinglish, Marathi, French, etc.)"*

**You:** *"Marathi, occasionally."*

**AI:**
```
Here's your project brief:

Title:    (working title TBD)
Author:   Shubhanshu
Genre:    Historical Fiction

Premise:  Rise of the Maratha Empire through Bajirao I
Lead:     Bajirao — appointed Peshwa at 19, tactical genius
Language: Marathi (dialogue)
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

## Historical Genre Features

Applies automatically when your genre is historical or you mention real figures.

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

## Book Size Planning

When initializing a new book, you can specify the scope:

| Format | Words | Chapters | Best For |
|---|---|---|---|
| **MVB** | 15–20K | 5–7 | Lead magnet, quick authority builder |
| **Short Book** | 25–40K | 8–12 | Positioning, thought leadership |
| **Full Book** | 50–80K | 15–20 | Traditional publishing, comprehensive guide |
| **Literary Novel** | 60–100K | 15–30+ | Character-driven fiction |

**You:** *"Let's plan a short book — around 10 chapters."*

> AI adjusts word count targets, chapter structure, and pacing accordingly.

---

## Chapter Craft — Openings & Closings

The AI uses chapter opening and closing formulas adapted to your genre:

**Fiction openings:** In-medias-res (drop into mid-scene), observation (a telling detail), or a question that creates tension.

**Non-fiction openings:** Story open, question open, statistic open, or bold claim.

**Closings:** Unresolved hooks (fiction), emotional landings (fiction), action bridges (non-fiction), summary bridges (non-fiction).

**You:** *"Open Chapter 4 with a bold claim."*

> AI writes an opening that hooks immediately, calibrated to your style guide.

---

## Character & World Tables

Rich structured profiles can be built for characters and worlds:

**You:** *"Let's build out a full character profile for Mastani."*

> AI creates a 19-field character table:
> | Field | Details |
> |---|---|
> | NAME | Mastani |
> | ROLES | Love interest, political catalyst |
> | PERSONALITY | Fierce, graceful, unapologetic |
> | INTERNAL CONFLICT | Torn between two worlds — Hindu court and Muslim heritage |
> | CHARACTER ARC | From outsider to the figure who defines Bajirao's legacy |
> | ... | ... |

**You:** *"Build a worldbuilding table for the Maratha court."*

> AI creates a 10-category world table covering atmosphere, physical details, emotional geography, and the soul of the world.

---

## Chapter Review & Revision

**You:** *"Review and polish Chapter 6."*

> AI reads the draft, its outline, adjacent chapters, and all context files. Reviews in order: Language → Emotion → Dialogue → Pacing → Continuity. Uses the revision checklist. Revises gently — never overwrites your intent.

**For Chapter 1 specifically:**
> AI also runs the **Opening Chapter Checklist** — checking hook strength, protagonist establishment, reader promise, and whether the first page earns its place.

**You:** *"That chapter feels too fast. Can you slow down the middle section?"*

> AI adjusts pacing while preserving your voice and the scene's emotional core.

---

## Specialized Revision Passes

Instead of a full review, request a **targeted pass** on a single aspect:

| Say this | What it focuses on |
|---|---|
| `"Do a Dialogue Pass on chapter 3"` | Subtext, distinct voice, removing on-the-nose lines |
| `"Do a Sensory Pass on chapter 4"` | Smell, texture, sound — makes settings fully immersive |
| `"Do a Prose Polish on chapter 5"` | Rhythm, weak verbs, tightening — strictly enforces style rules |
| `"Do a Tension Pass on chapter 6"` | Sentence length and structural pacing — action vs. reaction beats |

---

## Scene Tension Map

During any chapter review, the AI evaluates the pacing wave:

**You:** *"Review Chapter 7 and do a tension map."*

> ```
> TENSION MAP — Chapter 7: The River Crossing
>
> | Scene | Brief Description         | Score | Note                    |
> |-------|--------------------------|-------|-------------------------|
> | 1     | Camp at dawn             |   3   | Grounding beat — good   |
> | 2     | Confrontation with scout |   7   | Escalates well          |
> | 3     | Crossing begins          |   8   | High — sustains tension |
> | 4     | Ambush                   |  10   | Peak — strong           |
> | 5     | Retreat to shore         |   4   | Needed reaction beat ✓  |
>
> Pacing verdict: Good wave shape. The peak at scene 4 is earned.
> Recommendations: Scene 3 could be lightened slightly to give the ambush more contrast.
> ```

---

## Book-Level Pacing Blueprint

Pre-plan the structural arc of the entire book before writing chapters:

**You:** *"Let's plan the pacing for the whole book."*

> AI fills `Core/pacing_blueprint.md` with a structural beats grid (inciting incident, midpoint, all-is-lost, climax) mapped to chapter and word count targets, plus a book-level tension curve table.

---

## Scene Cards

For precise scene-level planning before drafting:

**You:** *"Create a scene card for Chapter 3, Scene 2 — the confrontation with Nizam's envoy."*

> AI creates a structured card with: POV character, location, entering emotional state, Goal → Conflict → Outcome → Aftermath, story function, hook into next scene, and active motifs to weave in.

---

## Research Flag Tracker

Flag uncertain facts inline while writing:

```
[NEED RESEARCH: Was the Bosphorus strait navigable in winter 1453?]
```

**You:** *"Log that research flag in the tracker."*

> AI adds it to `Research/research_tracker.md` with an ID, chapter reference, and open status.

**You:** *"Show me all open research items."*

> AI reads and lists all unresolved flags.

---

## Beta Reader Feedback

**You:** *"Log this beta feedback from Riya: Chapter 2 felt slow, Chapter 5 great, wants more of Mastani."*

> AI adds entries to `beta_reader_log.md` by chapter with Type, Priority, and Status.

**You:** *"What are the high-priority beta notes I haven't addressed yet?"*

> AI returns all open, high-priority items.

---

## Publishing Toolkit

Once the manuscript is complete, generate all submission assets from your memory bank:

**You:** *"Write a back-cover blurb."*

> AI writes a 150–200 word blurb using Hook → Setup → Stakes → Question formula, in your voice.

**You:** *"Write a 1-page synopsis."*

> AI writes a 500–700 word synopsis in present tense, third person — full story including the ending, characters in ALL CAPS on first mention.

**You:** *"Write a query letter."*

> AI writes a 250–350 word query letter: hook, pitch, book details + comp titles, bio placeholder, closing.

**You:** *"Give me a logline."*

> AI writes a single 25–30 word sentence: `[Protagonist with flaw] must [pursue goal] before [deadline/stakes], or [consequence].`

---

## Continuity Diagnostics

**You:** *"Run a continuity check."*

> AI reads all chapters, memory bank, and outlines. Generates a diagnostic report:

```
Continuity Diagnostic Report — Generated: Feb 2026

✓ Timeline consistent across Chapters 1–8
✓ Character behavior aligned with profiles

⚠ Chapter 5, Scene 2: Bajirao is called "Peshwa Bajirao"
  but scene is set in 1717, before his 1720 appointment.
  → Question: Should this be corrected to "Bajirao"?

⚠ Chapter 7: Nizam-ul-Mulk references the Palkhed battle,
  which hasn't happened yet in the timeline.
  → Question: Is this foreshadowing, or a continuity slip?
```

> Report saved to `Research/continuity_diagnostic_report.md`. Issues are framed as questions — you decide what needs fixing.

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
| `"Let's plan the pacing for the whole book"` | Generates Book-Level Pacing Blueprint |
| `"Create a scene card for Chapter N, Scene X"` | Atomic scene planning card |
| `"Let's build out [character]"` | Character brainstorming with structured profile table |
| `"Build a worldbuilding table"` | Structured world profile creation |
| `"[FICTION] ..."` | Mark an invented element in historical genres |
| `"Write chapter [N]"` | Writes the chapter |
| `"Outline chapter [N]"` | Writes the chapter outline |
| `"Write the master outline"` | Creates `Outlines/Master_Outline.md` |
| `"Plan a [MVB/short/full] book"` | Sets book scope and adjusts targets |
| `"Review chapter [N]"` / `"Polish chapter [N]"` | Runs structured chapter review |
| `"Do a Dialogue Pass on chapter [N]"` | Subtext-focused revision pass |
| `"Do a Sensory Pass on chapter [N]"` | Immersive detail-focused revision pass |
| `"Do a Prose Polish on chapter [N]"` | Rhythm and tightening revision pass |
| `"Do a Tension Pass on chapter [N]"` | Structural pacing revision pass |
| `"Draft all remaining chapters in parallel"` | Launches background agents |
| `"Review all chapters in parallel"` | Parallel review via background agents |
| `"Compile the book"` | AI merges all chapters and saves to `Manuscript/` |
| `"Update memory bank"` | Full audit and update of all memory files |
| `"Check continuity"` / `"Run continuity check"` | Cross-chapter consistency diagnostic |
| `"Log beta feedback"` | Adds reader notes to Beta Reader Feedback Log |
| `"Show open research items"` | Lists all unresolved `[NEED RESEARCH]` flags |
| `"Write a back-cover blurb"` | Generates blurb from memory bank |
| `"Write a 1-page synopsis"` | Generates synopsis for agent submission |
| `"Write a query letter"` | Generates query letter from memory bank |
| `"Give me a logline"` | 25–30 word high-concept sentence |
| `"What chapter are we on?"` | AI reports current progress |
| `"In this scene, [speaker] calls him just '[name]'"` | Override address register for a scene |

---

## Tips

- **You don't repeat context** — AI reads the memory bank at the start of every session
- **Partial answers are fine** — say what you know; add more later
- **Change your mind freely** — just tell the AI the new version, it updates the memory bank
- **For historical books** — providing your primary sources upfront helps the AI flag uncertainties accurately
- **Chapter review is non-destructive** — the AI never adds new plot or removes your intentional choices

---

## Complete Features List

Everything this skill can do, at a glance:

| Category | Features |
|---|---|
| **Initialization** | One-time Story Forge onboarding, fast-track mode, draft import, genre auto-detection |
| **Genre Support** | Literary fiction, historical, fantasy, sci-fi, thriller, horror, romance, adventure, mystery, biographical, YA, children's, short stories |
| **Historical** | Title/honorific timeline rules, `[FICTION]` marking, contextual address by speaker relationship, fact-checking with dispute flags |
| **Dialogue** | Multi-language support — Hinglish, Hindi, Marathi, French, Spanish, Italian, German and more woven naturally |
| **Planning** | Book size options (MVB/Short/Full/Novel), Pacing Blueprint, narrative structure, emotional core discovery, synopsis templates, timeline mapping |
| **Scene Planning** | Scene Card template — Goal-Conflict-Outcome-Aftermath engine for atomic scene-level planning |
| **Characters** | 19-field structured profiles, Character Arc Matrix (chapter-by-chapter progression), historical title timelines, psychological profiles |
| **Worldbuilding** | 10-category world tables, sensory details, emotional geography, Thematic & Motif Tracker |
| **Conflict** | External/internal/thematic conflict mapping with stakes, opposition, and growth tracking |
| **Outlining** | Master outline, chapter beat sheets, chapter goals, emotional arcs, hooks, Chapter Titles Guide |
| **Writing** | Chapter opening/closing formulas, structure templates, read-aloud rhythm, engagement techniques |
| **Quality** | Anti-AI writing rules, Hype Test, revision checklists (story/prose/voice/character/continuity), Opening Chapter Checklist, Scene Tension Map |
| **Review** | Structured chapter review (Language → Emotion → Dialogue → Pacing → Continuity), 4 Specialized Revision Passes |
| **Continuity** | Cross-chapter diagnostic reports, timeline/character/worldbuilding checks, question-based flagging |
| **Research** | Research Flag Tracker — structured `[NEED RESEARCH]` log with open/resolved status |
| **Beta Readers** | Beta Reader Feedback Log — chapter-by-chapter notes with priority, type, and action tracking |
| **Publishing** | Query letter, back-cover blurb, 1-page synopsis, logline — all auto-generated from memory bank |
| **Memory** | Automatic Book Memory Bank — projectbrief, story structure, characters/world, active context, progress, style guide |
| **Updates** | Auto-triggered after chapters, outlines, or on-demand; comprehensive audit with file-by-file change reports |
| **Compilation** | Auto-combine chapters into manuscript, cross-platform scripts (bash/PowerShell) |
| **Documentation** | Auto-generated README with badges, progress tracking, scope table, character list, sources |

