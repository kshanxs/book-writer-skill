# Production

Tools for turning your chapters into a finished manuscript.

## The Easy Way

Ask your assistant to "check the book" or "export the book", or run one command from your project folder:

```bash
python3 book-memory-bank/Production/Scripts/book.py check
python3 book-memory-bank/Production/Scripts/book.py export all
```

On Windows, use `python` or `py` in place of `python3`.

| Command | What it does |
|---|---|
| `doctor` | Shows what is set up and which optional tools are missing |
| `check` | Runs the prose audit, continuity check, and research check |
| `audit 3` | Finds AI-sounding patterns in Chapter 3 |
| `voice my_writing.md` | Learns your style so your habits are not flagged |
| `continuity` | Compares the chapters with `Core/continuity_ledger.md` |
| `lint` | Runs Vale and Harper if you have them |
| `export docx`, `epub`, or `all` | Builds the book. Add `--draft` to allow research flags |

Checks never edit your chapters. To stop a check from flagging something, add its name to `Style/audit_ignore.txt`.

Python 3.8+ is the only requirement for checks. Export needs [Pandoc](https://pandoc.org/installing.html). [Vale](https://vale.sh), [Harper](https://github.com/Automattic/harper), and [EPUBCheck](https://www.w3.org/publishing/epubcheck/) are optional.

For an EPUB cover, save `cover.jpg` or `cover.png` in `Manuscript/`.

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
