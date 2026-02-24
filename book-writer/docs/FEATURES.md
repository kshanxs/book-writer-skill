<div align="center">

# ✦ book-writer — Features & Reference ✦

**v1.5** · *Complete feature list, command reference, and skill architecture*

</div>

---

## ✨ Full Feature List

<table>
<tr>
<td width="50%">

### 📖 Writing Engine
| | |
|---|---|
| ✍️ **Master Author Voice** | Literary prose, cinematic dialogue, genre-aware style |
| 🎭 **15+ Genre Options** | Literary, Fantasy, Sci-Fi, Historical, Thriller, Horror, Romance, YA, Children's |
| 📏 **Book Size Planning** | MVB (15–20K) · Short (25–40K) · Full (50–80K) · Novel (60–100K) |
| 📝 **Chapter Craft** | 6 opening/closing formulas, structure templates, engagement techniques |
| 🛡️ **Anti-AI Writing** | Hype test, voice authenticity, DO/DON'T quick-scan |
| 🗣️ **Multi-Language Dialogue** | Hinglish, Hindi, Marathi, French, Spanish, Italian, German |

</td>
<td width="50%">

### 🧠 Story Memory
| | |
|---|---|
| 💾 **Book Memory Bank** | Persistent Markdown files — characters, plot, world, progress |
| 🔄 **Auto Updates** | Memory stays current after every chapter — zero manual work |
| 🔍 **Continuity Diagnostics** | Cross-chapter consistency checks with diagnostic reports |
| 🏛️ **Historical Authenticity** | Verified dates, titles, events, title-timeline rules |
| 📄 **Draft Import** | Paste existing notes — AI skips questions already answered |
| 📜 **Auto GitHub README** | Generates polished project README on initialization |

</td>
</tr>
<tr>
<td width="50%">

### 🧒 Children's Books
| | |
|---|---|
| 📚 **Age-Based Guidelines** | Tailored rules for ages 2–3, 4–5, 6–7, 8–9 |
| 🎵 **Rhyming & Meter** | Perfect rhyme schemes, meter analysis, read-aloud testing |
| 🎨 **Illustration Notes** | Per-page visual descriptions for artists |
| 🔤 **Phonics & Vocabulary** | Sight words, CVC words, vocabulary building |
| 💡 **Values & Lessons** | Natural moral integration — show, don't preach |
| 📖 **Book Types** | Picture books, songs/poems, series, non-rhyming stories |

</td>
<td width="50%">

### ⚡ Workflows
| | |
|---|---|
| 🚀 **Parallel Drafting** | Background agents draft Chapters 2–N simultaneously |
| 🔁 **Parallel Review** | Review all chapters at once via background agents |
| 📊 **Chapter Titles Guide** | Auto-generated title → meaning → story connection map |
| 🏗️ **The Story Forge** | Guided onboarding — one question at a time, all skippable |
| 📐 **Narrative Architecture** | Three-Act, Hero's Journey, Literary Arc, Multi-Timeline |
| ✅ **Complete & Present** | Final verification summary with all created files |

</td>
</tr>
<tr>
<td width="50%">

### 👤 Story Building
| | |
|---|---|
| 🧬 **Character Profiles** | 19-field structured tables with relationship mapping |
| 🌍 **Worldbuilding Tables** | 10-category world profiles with sensory details |
| ⚔️ **Conflict Mapping** | External, internal, thematic conflicts with stakes |
| 📋 **Synopsis & Timeline** | Full narrative beats + chronological event tracking |
| 🎯 **Emotional Core** | North Star identification — the truth your story explores |
| 📦 **Compilation** | Auto-combine all chapters into manuscript |

</td>
<td width="50%">

### 🔬 Quality Control
| | |
|---|---|
| ✅ **Revision Checklists** | Story, prose, voice, characters, continuity gates |
| 🧒 **Children's Checklist** | Rhyme, meter, age-appropriateness, engagement |
| 🔍 **Continuity Reports** | Question-based diagnostic — flags, never imposes |
| 🏛️ **Title-Timeline Rule** | Correct historical address based on scene date |
| 🎭 **Contextual Address** | Different characters use different titles for same figure |
| 🏷️ **`[FICTION]` Marking** | Explicit tagging of invented historical elements |

</td>
</tr>
</table>

---

## ⚡ Command Reference

| Say this | What happens |
|---|---|
| `"Let's start building a new book"` | Runs The Story Forge onboarding |
| `"Just initialize now"` | Skips all questions, starts immediately |
| `"Plan a short book"` | Sets book scope — MVB / Short / Full / Novel |
| `"Write a children's book for ages 4-6"` | Activates children's book craft |
| `"Let's build out [character]"` | Creates 19-field character profile |
| `"Build a worldbuilding table"` | Creates 10-category world profile |
| `"Write chapter 3"` | Reads memory bank, writes the chapter |
| `"Outline chapter 3"` | Creates chapter outline |
| `"Draft all remaining chapters in parallel"` | Launches background agents |
| `"Review chapter 3"` | Structured chapter review & polish |
| `"Review all chapters in parallel"` | Parallel review via background agents |
| `"Update memory bank"` | Full audit and update |
| `"Check continuity"` | Cross-chapter diagnostic report |
| `"Check for consistency"` | Flags contradictions across memory bank |
| `"Compile the book"` | Merges all chapters into `Manuscript/` |
| `"[FICTION] ..."` | Marks an invented element (historical genres) |

---

## 🏛️ Historical Genres

Activates automatically when you choose a historical genre or mention real figures:

- ✅ All dates, battles, titles, and biographical facts historically verified
- ✅ Figures addressed by titles they've earned *at the scene's point in time*
- ✅ Different characters address the same figure differently — context matters
- ✅ Invented elements accepted when prefixed with `[FICTION]`

---

## 📁 Project Structure After Initialization

```
YourBookProject/
│
├── README.md                         ← Auto-generated (GitHub-ready)
│
├── Chapters/                         ← Your manuscript
│   ├── Chapter01.md
│   ├── Chapter02.md
│   └── ...
│
├── Outlines/                         ← Planning
│   ├── Master_Outline.md
│   ├── chapter-titles-guide.md       ← Auto-generated title reference
│   └── Chapter_Outlines/
│
├── Research/                         ← Continuity reports & notes
│   └── continuity_diagnostic_report.md
│
├── Manuscript/                       ← Compiled book output
│
└── book-memory-bank/                 ← Auto-maintained by the AI
    ├── Core/
    │   ├── projectbrief.md           High-level concept & goals
    │   ├── story_structure.md        Narrative patterns & themes
    │   ├── world_and_characters.md   Characters, world, relationships
    │   ├── activeContext.md          Current session focus
    │   ├── progress.md              Completion tracking
    │   └── Templates/               Chapter, outline, titles guide templates
    └── Style/
        └── style_guide.md           Voice, tone, language rules
```

---

## 🔍 Skill Architecture

```
book-writer/
├── SKILL.md                                ← Core instructions & 8 workflows
├── docs/
│   ├── USAGE.md                            ← Usage guide with examples
│   └── FEATURES.md                         ← This file
├── references/
│   ├── author_rules.md                     ← Writing persona & historical rules
│   ├── book_memory_protocol.md             ← Memory bank architecture & rules
│   ├── memory_update_prompts.md            ← Update criteria & templates
│   ├── story_forge.md                      ← Onboarding (15+ genres, North Star)
│   ├── readme_template.md                  ← Auto-README template
│   ├── chapter_craft.md                    ← Chapter formulas & engagement
│   ├── revision_checklist.md               ← Quality gates & DO/DON'T lists
│   ├── character_worldbuilding_tables.md   ← Profiles, world, conflict tables
│   ├── childrens_book_craft.md             ← Ages 2–9, rhyming, illustration
│   └── parallel_workflows.md              ← Background agent drafting/review
└── assets/
    └── book-memory-bank/                   ← Template directory (copied on init)
        └── Core/Templates/
            ├── chapter_outline_template.md
            ├── master_outline_template.md
            └── chapter_titles_guide_template.md
```

---

## 📝 Changelog

### v1.5
- ✦ **Children's Book Craft** — Age-based writing, rhyming/meter, illustration notes, phonics, values framework
- ✦ **Parallel Workflows** — Simultaneous chapter drafting and review via background agents
- ✦ **Chapter Titles Guide** — Auto-generated title meaning & story connection reference
- ✦ **Complete & Present** — Final verification summary workflow
- ✦ **Project Completion Summary** — Checklist of all created files with next steps
