# Parallel Workflows — Outlining, Reviews, and Concurrency Limits

Read this reference when handling multiple chapters. It explains when to use parallel background agents, limits concurrent operations to prevent narrative divergence, and defines the rules for sequential vs. parallel workflows.

---

## When to Use Parallel vs Sequential

| Scenario | Approach |
|----------|----------|
| 5+ chapters to outline or create scene cards | **Parallel** (recommended) |
| 5+ chapters to review, revise, or edit | **Parallel** (recommended) |
| Prose drafting for sequential narrative chapters | **Sequential** (Mandatory for continuity) |
| Independent stories or anthology collections | **Parallel** |
| Debugging specific narrative or pacing issues | **Sequential** |

---

## The Dependency Paradox of Parallel Prose Drafting (CRITICAL)

Prose drafting of sequential novel chapters is **inherently stateful and sequential**.
*   **The Flaw:** If background agents attempt to draft Chapter 2 and Chapter 3 in parallel, the agent writing Chapter 3 is forced to write without knowing the exact final prose, emotional tone, and character choices made in Chapter 2.
*   **The Result:** Narrative drift, broken subplots, inconsistent characters, and redundant pacing.
*   **The Rule:** Sequential drafting is the mandatory default for prose narrative progression. Concurrency (parallel agents) must never be used to draft consecutive prose chapters.

---

## Parallel Chapter Outlining & Scene-Cards

Since outlining follows a top-down structure derived from `Master_Outline.md`, outlining multiple chapters can be safely performed in parallel.

### Workflow
1. Approve `Outlines/Master_Outline.md`.
2. Launch one background agent per chapter to write detailed scene cards and chapter-level outlines.
3. Save output to `Outlines/Chapter_Outlines/Chapter[NN]_Outline.md`.

---

## Parallel Chapter Review & Editing

Review and revision passes look for specific patterns (grammar, pacing, voice, sensory detail). They can run concurrently across already-drafted chapters when every agent reads the same frozen snapshot.

### Workflow
1. Verify all target chapters have completed drafts in `Chapters/`.
2. Copy each target and the files immediately before and after it in reading order (Prologue, chapters, Interludes, Epilogue) to a new `Revisions/<YYYY-MM-DD_HHMMSS>/` folder. If that folder exists, add `-2`, `-3`, and so on. This is both the backup and the stable copy for continuity.
3. Launch one background task per chapter. Each task edits only its own chapter.
4. Once all review tasks finish, run a **Sequential Continuity Check** across the whole set.

### Background Task Template (Review & Edit)

Each background review task must include:

```
TASK: Review and gently refine Chapter [N] draft.

EXPECTED OUTCOME: Improved draft preserving author's style, intent, and emotional subtlety.

REQUIRED CONTEXT FILES TO READ:
- Chapters/Chapter[NN].md (current draft)
- Outlines/Chapter_Outlines/Chapter[NN]_Outline.md (original plan)
- Revisions/<snapshot>/<previous file in reading order> (if any, for backward continuity)
- Revisions/<snapshot>/<next file in reading order> (if any, for forward continuity)
- book-memory-bank/Style/style_guide.md (voice and tone rules)
- book-memory-bank/Core/world_and_characters.md (character consistency)

REVIEW FOCUS AREAS:
- Language: Reduce redundancy, tighten phrasing, improve rhythm.
- Emotion: Clarify undercurrents, strengthen subtext, avoid over-explanation.
- Dialogue: Make speech natural, remove exposition, preserve character voice.
- Pacing: Smooth transitions, balance stillness and movement.

REVISION PRINCIPLES:
- Preserve author's voice above all else.
- Revise gently; never overwrite intention.
- Clarify emotion without explaining it.
- Respect ambiguity and silence.

MUST DO: Cross-check with outline, prior/next chapters, and context files.
MUST NOT: Introduce new scenes, events, or characters. Resolve future conflicts.
OUTPUT: Save refined draft to Chapters/Chapter[NN].md. Do not edit any other chapter.
```

---

## Sequential Drafting Workflow (Default for Prose)

For prose writing, chapters must be drafted one by one:
1. **Prepare Context:** Read the memory bank files, the approved Chapter N-1 prose, and the outline for Chapter N.
2. **Draft Prose:** Write Chapter N and save to `Chapters/Chapter[NN].md`.
3. **Execute Memory Update:** Run the Memory Updating Protocol to record character additions, plot turns, and timeline events in the memory bank files.
4. **Context Carryover:** Move to Chapter N+1 using the updated memory files and Chapter N's final prose.

---

## Status Communication

When launching parallel outlining or review tasks:
> "Launched [N] parallel agents for [task description]. Estimated time: [X] minutes."

As tasks complete:
> "Task [N] of [Total] completed."

When all tasks are done:
> "All [N] chapters processed. Ready for the final continuity check?"
