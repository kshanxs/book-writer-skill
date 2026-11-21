# Writing Rules for Popular Science & Technology History

This document defines the guidelines for writing and reviewing chapters in the popular-science, technical history, and biographical non-fiction genres. Read this file when working on books in these genres.

## 1. Voice & Tone
- **Authoritative yet Accessible**: Write with the curiosity and storytelling energy of a master biographer (in the vein of Walter Isaacson, Jon Gertner, Steven Johnson, or Richard Rhodes). Avoid the dry, passive tone of academic journals or engineering specs.
- **Human-Centric Narrative**: Science and technology do not advance in a vacuum. Focus on the people, their personal struggles, collaborative breakthroughs, disputes over intellectual priority, and the atmospheric context of their workspaces (e.g., Bletchley Park, Bell Labs, CERN).
- **Sense of Wonder**: Build a thematic bridge between abstract thoughts and the material world, emphasizing how simple ideas evolved to reshape human civilization.

## 2. Narrative vs. Explanatory Dual-Tense Split
To guide the reader smoothly between historical storytelling and technical logic, use two distinct tenses:
- **Past Tense (Narrative/Biographical)**: Use for all events, historical settings, actions, and biographical descriptions.
 - *Example*: "In June 1948, Claude Shannon published the paper establishing the mathematical limits of communication."
- **Present Tense (Explanatory/Algorithmic)**: Use when explaining abstract logical rules, mathematical theorems, algorithms, or how a machine functions in principle.
 - *Example*: "A Turing machine reads a single symbol on a tape. If it sees a zero, it writes a one and moves the scanner one cell to the right."

## 3. Conceptual Visualization & Analogies (No Equations or Code)
- **The Visual Analogy Rule**: Never use raw mathematical formulas, dense equations, or blocks of programming code in the narrative prose. Instead, translate technical concepts into intuitive, visual, and physical analogies.
 - *Example (Entropy)*: Explain Shannon's information entropy using the probability of guessing coin flips or drawing cards from a deck, rather than the formula $H = -\sum p_i \log_2 p_i$.
 - *Example (Relational Database)*: Explain E.F. Codd's relational database model as a series of neatly cross-referenced, two-dimensional ledger sheets, rather than relational algebra.
 - *Example (Neural Networks)*: Explain backpropagation and neural weights as a complex board of interconnected dials and knobs, where adjusting one slightly changes the behavior of the next.

## 4. Biographical Weaving (Anti-Info Dump)
- Do not dump pages of static biographical history before getting to a discovery. Weave the details of a scientist's life directly into the timeline of their paper's development.
- Introduce their quirks, background, or struggles at the moment they influence their thinking or design decisions.
- Make the setting a character: describe the ambient noise of a computer lab, the smell of burnt vacuum tubes, or the quiet isolation of Bletchley Park to ground the research in a physical reality.

## 5. Avoid Retroactive Technical Anachronisms
- **The Historical Context Rule**: Never explain a historical breakthrough using concepts, terminology, or technologies that were invented later. Do not attribute foresight that could not exist.
 - *Example (1936)*: When describing Alan Turing's paper *On Computable Numbers...*, do not refer to "RAM," "microprocessors," or "operating systems." Use Turing's original conceptual language: "infinite paper tape," "read-write head," "instruction table," and "state of mind."
 - *Example (1945)*: When explaining John von Neumann's EDVAC architecture, focus on the physical separation of arithmetic units and memory delay lines, not modern silicon chip packaging.

## 6. Research Paper & Document Citations
- **Markdown Integration**: When referring to or quoting a specific paper, format the paper title in *italics* and weave direct quotes in as blockquotes (`>`) to denote primary source material.
- **Narrative Framing**: Introduce quotes by explaining the tone of the writer—whether they wrote with dry academic reserve, quiet triumph, or cautious urgency.
- **Explanatory Follow-up**: Every direct quote of academic language must be immediately followed by a clear, simple translation of what that quote means in layperson's terms.

## 7. Quality & Fact-Proximity
- **Flagging Gaps**: If a specific biographical detail, date, or event is historically disputed or unknown, do not invent it. Use the `[NEED RESEARCH]` flag in the chapter draft and record the query in the project's research tracker.
- **Scientific Humility**: Avoid calling an idea "inevitable" or attributing magical genius. Highlight the small, incremental steps and the contributions of peers that made the final breakthrough possible.
