# Humanizing Prose

Read this when drafting, polishing, or when the author asks to "humanize", "de-AI", or "make this sound less like AI". The goal is better writing that sounds like this author. It is not a way to beat AI detectors or avoid a publisher's disclosure rules.

## Core Principles

1. **Story comes before words.** Research on 61,608 stories found that narrative choices alone separate most AI fiction from human fiction. AI stories over-explain themes and favor tidy, single-track plots ([StoryScope](https://arxiv.org/abs/2604.03136v1), preprint). Fix the outline first, then the prose.
2. **Count density, not single instances.** One em dash, one cliché, or one "not X but Y" means nothing. A page full of them is a pattern.
3. **The author's own style is the standard.** If the author naturally writes with dashes, fragments, or long sentences, keep them.
4. **Over-correcting creates a new fingerprint.** Do not sand every sentence into the same "human" shape.
5. **Never give a verdict.** Do not say a passage "is AI". Quote the text and describe the pattern. Do not use detector scores as evidence, because they can wrongly flag real writers.

## The Em Dash Rule

- **AI-written narration:** no em dashes.
- **AI-written dialogue:** only when a speaker is cut off or breaks off.
- **The author's own text:** never remove their dashes unless asked.
- **Voice baseline:** if the author's sample uses dashes, match that rate.
- After removing dashes, recount semicolons and colons so the habit does not simply move.

## Workflow

1. **Learn the voice.** If the author has 1,500+ words of their own writing, run `book.py voice <file>`.
2. **Check the outline** using the story checks below before drafting.
3. **Draft with positive direction.** Work from the style guide, the POV character's voice, and the scene's goal, conflict, and turn. Save the banned-pattern list for revision, where it does less harm.
4. **Audit.** Run `book.py audit <chapter>`. Read every hit in context, because the patterns over-match on purpose.
5. **Revise lightly.** Prefer cutting to replacing. Snapshot first and show the author what changed.
6. **Recount.** Run the audit again and check that one pattern did not become another.
7. **Cold read.** For important chapters, follow `references/cold_reader.md`. Clean scanner results do not prove a chapter works.

If a scene needs fixes in most categories, recommend redrafting it from its scene card instead of patching it.

## Always Check

| Pattern | Example | Better |
|---|---|---|
| Narrator explains subtext | "It was her way of saying goodbye." | Keep the gesture and cut the explanation |
| Theme stated outright | "She understood that grief was a kind of love." | End on what she does next |
| Emotion named after a body cue | "His stomach dropped. Panic surged." | Keep the action, or simply: "He was frightened." |
| Scene-ending wisdom | "For now, it would have to be enough." | End on the last concrete action |
| Coda after the turn | Paragraphs explaining what just happened | Cut to the last new action |
| Similes that don't map | "Silence like wet cloth" | Compare to something this character knows |
| Chatbot or planning text | "Here is the revised scene", "her character arc" | Delete |
| Recycled descriptors | The same trait word for word in each scene | Keep the first and show it doing something |
| Therapy-speak | "I hear you. That's valid." | Let people deflect, misread, or change the subject |
| Mic-drop closers | A quotable line no one answers | Let someone deflate it, or end on action |
| Conflict dissolved too soon | Apology and peace in the same scene | Leave it unresolved and carry it forward |
| "As you know" exposition | Telling someone what they already know | Give one person a real reason not to know |
| Default AI names | Elara, Elias, Kael, Lyra, Thorne, Voss | Choose names from the setting's culture and era |

## Patterns That Matter in Density

`book.py audit` counts these per 1,000 words and compares them with the author's rate:

- "Not X but Y" and its variants. Keep it when the reader really believed X.
- Lists of three, in words or in repeated short sentences.
- Significance tails, such as ", reflecting her isolation".
- "Unreadable", "unspoken", and similar adjectives.
- "The kind of X that".
- Stock body reactions, such as clenched jaws and held breaths.
- "Hung in the air", "a beat passed", "something shifted".
- Fancy dialogue tags and adverbs on tags.
- Sentences that are all about the same length.
- Runs of sentences with the same opening.

## Leave These Alone

- **Plain emotion words.** "She was angry" is often better than another clenched jaw.
- **Run-ons, comma splices, and sentences starting with And or But** when they are part of the voice.
- **Digressions.** A character getting distracted can make a scene feel alive.
- **Repeating the clearest word.** Rotating synonyms is worse.
- **Sarcasm, irony, and understatement.** Do not "clarify" them.
- **Uneven pacing.** A long scene or very short chapter can be right.
- **Specific real references.** Keep the actual song, street, or brand.
- **Dialogue that fits a character,** even when the character sounds corporate or clichéd.
- **A strong passage.** Finding nothing to change is a valid result.

## Signs of Over-Correction

| Failure | What it looks like | Fix |
|---|---|---|
| Fragment overuse | Short. Choppy. Everywhere. | Restore full sentences |
| Detail stuffing | Brand names and exact times in every line | One useful detail per beat |
| Signature endings | Every scene ends on a terse image | Vary the endings |
| Fake mistakes | Errors added to seem human | Never add errors |
| Punctuation swap | Dashes became semicolons | Recount and rewrite |
| Bodiless characters | All physical reactions removed | Keep specific actions |
| Flattened voices | A character's way of talking was "fixed" | Restore their voice |

## Story-Level Checks

For fiction, ask these about the outline and again about the finished book. They are prompts and not requirements. Genre and the author's intent come first.

1. Does at least one subplot have its own want, turn, and outcome?
2. Does the protagonist do something morally compromising that is not instantly forgiven?
3. Is at least one major problem resolved by someone or something other than the protagonist?
4. Is at least one thread, relationship, or cost still unsettled at the end?
5. Is there at least one non-linear move, time jump, or document?
6. Does the climax land late, around 80 to 90% of the book?
7. Do setbacks keep growing, including in the final quarter?
8. Do some scenes end badly, with no consolation?
9. Do chapter lengths, shapes, and endings vary?
10. If there is an epilogue, does it add something new?
11. Could a reader identify each POV character with their name removed?
12. Do the names fit the setting's culture and era?

If three or more answers are no, discuss the outline with the author before drafting. Never change a story decision without their approval.

## Non-Fiction and Children's Books

- **Non-fiction:** prioritize verified facts, named sources, and specific examples. Never invent a statistic, quote, or anecdote to sound human.
- **Children's books:** repetition, refrains, and simple rhythm are features of the form. Follow `references/childrens_book_craft.md` instead of the rhythm checks.
- **Other languages:** the audit is calibrated for English. Apply the principles by judgment.
