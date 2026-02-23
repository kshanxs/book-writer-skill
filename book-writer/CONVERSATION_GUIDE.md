# 💬 Conversation Guide — How to Talk to the Book Writer AI

This document shows you the actual conversation flow at every stage of using the skill. Think of it as a script of what dialogue with the AI looks like — so you know exactly how to communicate and what to expect back.

---

## 1. Starting Fresh — You Have No Material

**You:**
> "Let's start building a new book."

**AI:**
> "Do you have any existing material — an outline, draft, or notes? If yes, share a file path or paste the content. If not, just say 'no'."

**You:**
> "No, I'm starting from scratch."

**AI:**
> "What's your name or pen name, and do you have a working title?"

**You:**
> "Shubhanshu. No title yet."

**AI:**
> "What genre best fits your book?
> ```
>  1. Literary Fiction       6. Thriller / Suspense
>  2. Historical Fiction      7. Horror
>  3. Narrative History       8. Romance
>  4. Fantasy (4a–4d)         9. Adventure / Action
>  5. Science Fiction        10. Mystery / Detective
>                            11. Biographical / Memoir
>                            12. Young Adult (YA)
>                            13. Children's / Middle Grade
>                            14. Short Story Collection
>                            15. Other — describe it
> ```"

**You:**
> "2 — Historical Fiction."

**AI:**
> "Historical Accuracy Mode is now on. All dates, titles, and events will default to the historical record. You can mark invented elements with [FICTION] anytime.
>
> What's the story about? One or two sentences, or say 'skip' if you're not there yet."

**You:**
> "It's about the rise of the Maratha Empire after Aurangzeb's death — seen through the eyes of Bajirao I."

**AI:**
> "Tell me about your main character. Who is Bajirao at the start of the story, and what drives him?"

**You:**
> "He's a young commander — ambitious, tactical genius, appointed Peshwa at 19. He wants to make the Marathas the dominant power in India."

**AI:**
> "Any author's style you want to echo? And roughly how many chapters are you imagining? (Both optional.)"

**You:**
> "William Dalrymple. Around 12 chapters."

**AI:**
> "Here's your project brief:
> ```
> Title:     (working title TBD)
> Author:    Shubhanshu
> Genre:     Historical Fiction
> Mode:      Historical Accuracy ON
> Premise:   Rise of the Maratha Empire through Bajirao I
> Lead:      Bajirao — appointed Peshwa at 19, tactical genius
> Style:     William Dalrymple
> Chapters:  ~12
> GitHub:    Not set
> ```
> Ready to initialize? Say yes or tell me what to change."

**You:**
> "Yes."

✅ *AI initializes memory bank, fills Core files, and writes README.md to your project root.*

---

## 2. Starting With an Existing Draft or Outline

**You:**
> "I have some notes already. Here's my outline file: ./my_outline.md"

**AI:**
> *[reads file]* "Got it — I've extracted the following:
> - Title: The Last Peshwa
> - Genre: Historical Fiction (Maratha era)
> - Protagonist: Bajirao I
> - Setting: Deccan and North India, 1720–1740
> - Scope: 12 chapters
>
> A few things I didn't find — what's your name or pen name, and any particular author style you're going for?"

**You:**
> "Shubhanshu. Dalrymple's style."

**AI:**
> "Perfect. Anything for GitHub — public, private, or skip?"

**You:**
> "Private."

**AI:**
> "Here's the brief: [summary]. Ready to initialize?"

**You:**
> "Yes."

✅ *Files created. Draft import skips any questions already answered by the outline.*

---

## 3. Skipping All Questions

**You:**
> "Just initialize now. I'll fill in everything later."

**AI:**
> ✅ *Initializes immediately with blank memory bank files. No questions asked.*

You can fill in the memory bank any time:

**You:**
> "The book is about Bajirao I. Update the memory bank with this premise: [paste text]"

**AI:**
> ✅ *Updates projectbrief.md and world_and_characters.md. Confirms which files changed.*

---

## 4. Brainstorming a Character Mid-Project

After initialization, you can develop any character through conversation:

**You:**
> "Let's build out Nizam-ul-Mulk as a character."

**AI:**
> "What's his role in the story — antagonist, rival, foil to Bajirao?"

**You:**
> "Antagonist. He's the one Bajirao keeps outmanoeuvring."

**AI:**
> "Historically, Nizam-ul-Mulk Asaf Jah I was a capable Mughal viceroy — highly intelligent but a cautious, defensive strategist. His defeats at Palkhed (1728) and Bhopal (1738) came from being drawn into terrain that neutralised his strengths.
>
> For your story: do you want him as a purely strategic antagonist, or do you want to give him a personal through-line — pride, ambition, or a specific grievance against Bajirao?"

**You:**
> "Personal pride. He genuinely believes he's the superior strategist and can't understand how Bajirao keeps winning."

**AI:**
> "That's a strong ironic position — a man who overestimates his own intelligence. Shall I add him to the memory bank with that psychological profile?"

**You:**
> "Yes."

**AI:**
> ✅ *Updated world_and_characters.md — Nizam-ul-Mulk entry added with role, historical background, and psychological profile.*

---

## 5. Historical Accuracy — Flagging a Fiction Element

**You:**
> "[FICTION] I want Bajirao to have a younger brother who fights alongside him at Palkhed."

**AI:**
> "Got it — I've added Bajirao's fictional younger brother to world_and_characters.md and marked him [FICTION]. He won't be treated as a historical figure. Do you have a name for him, or shall I suggest one that's period-appropriate?"

**You:**
> "Suggest one."

**AI:**
> "How about *Vikram Rao Bhat*? Common Chitpavan surname, fits the period. Or I can go with something else."

---

## 6. Title & Address in Dialogue

**You:**
> "Write a scene where Aurangzeb hears about Shivaji's coronation. He's furious."

**AI:**
> *[writes scene where Aurangzeb's courtiers use the full title "Chhatrapati Shivaji Maharaj" once in narration, but Aurangzeb himself says "this Shivaji" contemptuously — stripped bare. The contrast characterises Aurangzeb's refusal to acknowledge the legitimacy of the title.]*

**You:**
> "Perfect. Now write the same moment from the Maratha camp."

**AI:**
> *[writes scene where Maratha soldiers shout "Chhatrapati Maharaj ki jai!" — full title and reverence — narrator uses "Chhatrapati Shivaji Maharaj" throughout.]*

---

## 7. Developing a Chapter

**You:**
> "Write the outline for Chapter 3."

**AI:**
> *[reads all memory bank files silently]*
> "Here's Chapter 3 outline:
> **Title: The Road to Palkhed**
> ..."

**You:**
> "Good. Add a scene where Bajirao scouts alone at night — I want something quieter and more internal."

**AI:**
> "Added to outline — Chapter 3, Scene 4: Night reconnaissance. Bajirao alone on the ridge above the Niza's camp. Internal monologue. Should it resolve in confidence or in doubt?"

**You:**
> "Doubt. He's not sure the gamble will work."

**AI:**
> "Good — that makes the Palkhed victory more earned. Updating the outline now."

---

## 8. Updating the Memory Bank

**You:**
> "We just finished Chapter 5. Update the memory bank."

**AI:**
> *[reads Chapter 5 in full]*
> ✅ **Book Memory — Updates after Chapter 5:**
> - `world_and_characters.md` — Nizam-ul-Mulk: added Chapter 5 developments (personal humiliation after Palkhed; resolve hardens)
> - `activeContext.md` — current position: end of Chapter 5; next chapter covers Delhi march
> - `progress.md` — Chapter 5 marked complete
> - `story_structure.md` — theme of "speed vs. mass" reinforced; noted for Chapter 6 callback

---

## 9. Checking Consistency

**You:**
> "Check for consistency issues."

**AI:**
> "Found one potential issue:
> In Chapter 2 (scene 3), Bajirao is referred to as 'Peshwa Bajirao' — but the scene is set in 1717, three years before his appointment. Should I correct it to 'Bajirao' for that scene?"

**You:**
> "Yes, fix it."

**AI:**
> ✅ *Corrected. Chapter_02.md updated. Memory bank note added: Bajirao holds no formal title before 1720.*

---

## Quick Reference — What to Say

| Situation | What to say |
|---|---|
| Start a new book | `"Let's start building a new book"` |
| Skip all questions | `"Just initialize now"` |
| Import a draft | `"Here's my outline file: ./path"` or paste content |
| Add a character | `"Let's build out [name] as a character"` |
| Mark a fictional element | `"[FICTION] [your invented element]"` |
| Write a chapter | `"Write chapter [N]"` |
| Write an outline | `"Outline chapter [N]"` |
| Update memory bank | `"Update the memory bank"` |
| Check consistency | `"Check for consistency issues"` |
| Change address register | `"In this scene, [speaker] calls him just '[name]', no title"` |
| Ask about a historical fact | `"When exactly did Bajirao become Peshwa?"` |
