# Parallel Workflows — Simultaneous Chapter Drafting & Review

Read this reference when drafting or reviewing multiple chapters. It enables launching background agents to work on chapters simultaneously, dramatically reducing total time.

---

## When to Use Parallel vs Sequential

| Scenario | Approach |
|----------|----------|
| 5+ chapters to draft or review | **Parallel** (recommended) |
| User explicitly wants speed | **Parallel** |
| Very complex continuity between chapters | **Sequential** |
| Debugging specific issues | **Sequential** |
| User prefers step-by-step control | **Sequential** |

**Always ask the user which approach they prefer before launching.**

---

## Parallel Chapter Drafting

### Workflow

1. **Draft Chapter 1 manually** — present to user for approval. This establishes voice and sets expectations.
2. **After Chapter 1 is approved**, offer parallel drafting for remaining chapters.
3. **Launch one background task per chapter** (Chapters 2–N).
4. Announce how many tasks were launched and estimated completion time.
5. Wait for all tasks to complete, then announce completion.

### Offering the Choice

> "I can now draft the remaining chapters (2–[N]) using two approaches:
>
> 1. **Parallel (Faster):** Launch [N-1] background agents, one per chapter, all drafting simultaneously
> 2. **Sequential:** Draft one chapter at a time in order
>
> Which approach would you prefer?"

### Background Task Template (Drafting)

Each background drafting task must include:

```
TASK: Draft Chapter [N] as complete prose.

REQUIRED CONTEXT FILES TO READ:
- Outlines/Chapter_Outlines/chapter-[N]-outline.md (chapter beat sheet)
- book-memory-bank/Style/ (narrative voice, tone, language rules)
- book-memory-bank/Core/Characters.md (character profiles)
- book-memory-bank/Core/Worldbuilding.md (setting, atmosphere)
- book-memory-bank/Core/Timeline.md (chronological accuracy)
- book-memory-bank/Core/Synopsis.md (story direction)
- Chapters/chapter-1.md (established voice from approved chapter)
- Chapters/chapter-[N-1].md (if N > 2, for continuity)

DRAFTING REQUIREMENTS:
- Transform outline beats into full prose
- Show moment-by-moment, never summarize
- Follow Style files exactly
- Preserve emotional restraint and subtlety
- Honor established character behavior
- Respect silence and stillness as narrative tools

OUTPUT: Save complete draft to Chapters/chapter-[N].md
Format: # Chapter [N]: [Title]
[Complete prose draft]

MUST DO: Read ALL context files before drafting. Cross-check continuity.
MUST NOT: Add plot events not in outline. Change established voice. Summarize instead of showing.
```

---

## Parallel Chapter Review

### Workflow

1. **Offer parallel or sequential review** after all chapters are drafted.
2. **Launch one background task per chapter** (all chapters).
3. Announce task count and estimated time.
4. Wait for completion, then announce readiness for continuity check.

### Background Task Template (Review)

Each background review task must include:

```
TASK: Review and gently refine Chapter [N] draft.

EXPECTED OUTCOME: Improved draft preserving author's style, intent, and emotional subtlety.

REQUIRED CONTEXT FILES TO READ:
- Chapters/chapter-[N].md (current draft)
- Outlines/Chapter_Outlines/chapter-[N]-outline.md (original plan)
- Chapters/chapter-[N-1].md (if N > 1, for continuity)
- Chapters/chapter-[N+1].md (if exists, for forward continuity)
- book-memory-bank/Style/ (voice and tone)
- book-memory-bank/Core/Characters.md (character consistency)
- book-memory-bank/Core/Timeline.md (chronological accuracy)
- book-memory-bank/Core/Worldbuilding.md (setting consistency)

REVIEW FOCUS AREAS:
- Language: Reduce redundancy, tighten phrasing, improve rhythm
- Emotion: Clarify undercurrents, strengthen subtext, avoid over-explanation
- Dialogue: Make speech natural, remove exposition, preserve character voice
- Pacing: Smooth transitions, balance stillness and movement

REVISION PRINCIPLES:
- Preserve author's voice above all else
- Revise gently; never overwrite intention
- Clarify emotion without explaining it
- Respect ambiguity and silence
- Improve rhythm, not drama

MUST DO: Cross-check with outline, prior/next chapters, and context files.
MUST NOT: Introduce new scenes or events. Break authorial voice. Over-explain. Add new characters. Resolve future conflicts.

OUTPUT: Save refined draft to Chapters/chapter-[N].md (overwrite existing).
```

---

## Sequential Fallback

### Sequential Drafting
For each Chapter N (2 to total):
1. Read context files (outline, style, characters, worldbuilding, timeline, synopsis, previous chapter)
2. Draft complete chapter following outline beats
3. Save to `Chapters/chapter-[N].md`
4. Announce completion, move to next

### Sequential Review
For each Chapter N:
1. Read current draft, outline, adjacent chapters, context files
2. Review: Language → Emotion → Dialogue → Pacing → Continuity
3. Save revised version
4. Announce completion, move to next

---

## Task Design Principles

Every background task must:
1. Be completely **self-contained** and independent
2. List **ALL required context files** explicitly (full paths)
3. Include clear **success criteria** and output format
4. Specify what **NOT** to do (constraints)
5. Save results to the **correct file location**

**Avoid:**
- Tasks that depend on other background tasks completing first
- Vague instructions without file paths
- Tasks that require user input mid-execution

---

## Status Communication

When launching parallel tasks:
> "Launched [N] parallel agents for [task description]. Estimated time: [X] minutes."

As tasks complete:
> "Task [N] of [Total] completed."

When all done:
> "All [N] chapters [drafted/reviewed]. Ready for [next step]?"
