# Production

Tools for turning your chapters into a finished manuscript.

## Chapter File Names

The scripts read chapters in this order:

| File | Position |
|---|---|
| `Prologue.md` | First |
| `Chapter01.md`, `Chapter02.md`, ... | By number |
| `Interlude02.md` | Right after Chapter 2 |
| `Epilogue.md` | Last |

Titles are fine, as in `Chapter 3 - The Road.md`. Copies such as `Chapter01_old.md` are skipped with a warning. Two files with the same chapter number stop the build so nothing is included by mistake.

Optional `Front_Matter.md` and `Back_Matter.md` in the project root are added at the start and end.

## Combine Chapters

Creates `Manuscript/COMBINED.md`.

```bash
# Mac / Linux
book-memory-bank/Production/Scripts/combine_chapters.sh
```

```powershell
# Windows
powershell -NoProfile -ExecutionPolicy Bypass -File book-memory-bank\Production\Scripts\combine_chapters.ps1
```

## Create a Word Document

Requires [Pandoc](https://pandoc.org/installing.html). Creates `Manuscript/BOOK.docx`.

```bash
# Mac / Linux
book-memory-bank/Production/Scripts/generate_docx.sh
```

```bat
:: Windows
book-memory-bank\Production\Scripts\generate_docx.bat
```

| Option | Effect |
|---|---|
| `--draft` | Keeps open `[NEED RESEARCH]` flags and writes `BOOK_DRAFT.docx` |
| `--no-open` | Does not open the finished file |

A final build stops while research flags remain. Your previous document is only replaced after a successful build.

## Word Styling

Pandoc uses `Scripts/reference.docx` when it exists. On Windows with Microsoft Word installed, `prepare_word_template.ps1` creates one the first time you export and then leaves it alone, so your customizations are safe. Run it with `-Force` to rebuild it. Without a template, Pandoc's default styling is used.

## Book Covers

`AI_Generation/cover_prompts.md` has prompt templates and cover specifications for AI image tools.
