# Research Flag Tracker

**Purpose:** To systematically track all uncertain facts, unverified historical claims, or placeholder details that need external research before the manuscript is finalized. Prevents unresolved flags from shipping into the final draft silently.

Update this file whenever a `[NEED RESEARCH]` flag is placed in a chapter or outline.

---

## 🔍 Open Research Items

| ID | Chapter | Flag Description | Priority | Source to Check | Status |
|----|---------|-----------------|----------|-----------------|--------|
| R-001 | {{TOKEN:Ch X}} | {{TOKEN:e.g., Was the Bosphorus strait navigable in winter 1453?}} | {{TOKEN:High / Medium / Low}} | {{TOKEN:e.g., Ottoman naval records, historian Runciman}} | 🔴 Open |
| R-002 | {{TOKEN:Ch X}} | {{TOKEN:...}} | {{TOKEN:...}} | {{TOKEN:...}} | 🔴 Open |

---

## ✅ Resolved Research Items

| ID | Chapter | Question | Answer / Decision | Source |
|----|---------|----------|-------------------|--------|
| R-00X | {{TOKEN:Ch X}} | {{TOKEN:Original question}} | {{TOKEN:Confirmed fact or creative decision made}} | {{TOKEN:Source used}} |

---

## 🏷️ Flag Usage in Chapters

When writing or reviewing chapters, mark unverified facts inline with:

```
[NEED RESEARCH: Brief description of what needs verification]
```

Then immediately log it in the table above with a new ID. Do not leave flags in the manuscript without a corresponding tracker entry.

---

## 📝 Integration Notes for the AI
*Before compiling the final manuscript, scan all chapter files for `[NEED RESEARCH]` tags and cross-reference against this tracker. All items must be either Resolved (green) or flagged with an explicit creative decision before the manuscript is considered complete.*
