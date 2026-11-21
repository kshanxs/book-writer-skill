#!/usr/bin/env bash
#
# Tests the manuscript scripts against throwaway book projects.
# Needs bash and python3. Uses pandoc and pwsh when they are on PATH.

set -uo pipefail

REPO="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
BANK="$REPO/book-writer/assets/book-memory-bank"
WORK="$(mktemp -d)"
trap 'chmod -R u+rw "$WORK" 2>/dev/null; rm -rf "$WORK"' EXIT

PASSED=0
FAILED=0
pass() { PASSED=$((PASSED + 1)); echo "  ok    $1"; }
fail() { FAILED=$((FAILED + 1)); echo "  FAIL  $1"; }
check() { if [ "$2" = "$3" ]; then pass "$1"; else fail "$1 (expected '$3', got '$2')"; fi; }

new_book() {
    BOOK="$WORK/$1"
    mkdir -p "$BOOK/Chapters"
    cp -R "$BANK" "$BOOK/book-memory-bank"
    cd "$BOOK" || exit 1
}
write() { printf '%b' "$2" > "Chapters/$1.md"; }
bodies() { grep -o 'BODY-[A-Za-z0-9_-]*' Manuscript/COMBINED.md | sed 's/BODY-//' | tr '\n' ' ' | sed 's/ $//'; }

run_combine_suite() {
    local label="$1" strict="$2"; shift 2
    local combine=("$@")
    echo "combine ($label)"

    new_book "$label-order"
    for name in Epilogue Chapter10 Interlude02 Chapter02 Chapter01 Prologue; do write "$name" "BODY-$name\n"; done
    "${combine[@]}" >/dev/null 2>&1
    check "reading order" "$(bodies)" "Prologue Chapter01 Chapter02 Interlude02 Chapter10 Epilogue"

    new_book "$label-names"
    write "chapter-1" "BODY-one\n"; write "Chapter_2" "BODY-two\n"; write "Chapter 10 - The Road" "BODY-ten\n"; write "Chapter3" "BODY-three\n"
    "${combine[@]}" >/dev/null 2>&1
    check "mixed names sort by number" "$(bodies)" "one two three ten"

    new_book "$label-old"
    write Chapter01 "BODY-keep\n"; write Chapter01_old "BODY-old\n"; write "Chapter01 (copy)" "BODY-copy\n"; write "Chapter 2 - Old Friends" "BODY-title\n"
    local output; output="$("${combine[@]}" 2>&1)"
    check "old copies skipped, real titles kept" "$(bodies)" "keep title"
    case "$output" in *Chapter01_old*) pass "skipped file is reported" ;; *) fail "skipped file is reported" ;; esac

    new_book "$label-dup"
    write Chapter01 "BODY-a\n"; write Chapter1 "BODY-b\n"
    "${combine[@]}" >/dev/null 2>&1
    check "duplicate chapter number stops" "$?" "1"

    new_book "$label-gap"
    write Chapter01 "x\n"; write Chapter04 "x\n"
    output="$("${combine[@]}" 2>&1)"
    case "$output" in *"missing: 2-3"*) pass "gap is reported" ;; *) fail "gap is reported" ;; esac

    new_book "$label-keep"
    mkdir -p Manuscript Chapters; echo PREVIOUS > Manuscript/COMBINED.md
    "${combine[@]}" >/dev/null 2>&1
    check "no chapters is an error" "$?" "1"
    check "previous output kept on failure" "$(cat Manuscript/COMBINED.md)" "PREVIOUS"

    new_book "$label-flags"
    write Chapter01 "Text [NEED RESEARCH: a date]\n"
    "${combine[@]}" "$strict" >/dev/null 2>&1
    check "strict stops on research flags" "$?" "3"
    "${combine[@]}" >/dev/null 2>&1
    check "normal run allows flags" "$?" "0"

    new_book "$label-scene"
    write Chapter01 "# One\n\nFirst.\n---\nSecond.\n\n\`\`\`\n---\n\`\`\`\n"
    "${combine[@]}" >/dev/null 2>&1
    check "scene break gets blank lines" "$(grep -n -x -e '---' Manuscript/COMBINED.md | head -1 | cut -d: -f1)" "5"
    check "line before scene break is blank" "$(sed -n 4p Manuscript/COMBINED.md)" ""
    check "line after scene break is blank" "$(sed -n 6p Manuscript/COMBINED.md)" ""
    check "code block untouched" "$(grep -A1 -F '```' Manuscript/COMBINED.md | sed -n 2p)" "---"

    new_book "$label-fence"
    write Chapter01 "~~~~\n~~~\n---\n~~~~\n\nFirst.\n---\nSecond.\n"
    "${combine[@]}" >/dev/null 2>&1
    check "shorter marker stays inside code block" "$(sed -n 2,4p Manuscript/COMBINED.md | tr '\n' ' ')" "~~~ --- ~~~~ "
    check "scene break works after nested code block" "$(sed -n 6,10p Manuscript/COMBINED.md | tr '\n' '|')" "First.||---||Second.|"

    new_book "$label-empty"
    mkdir -p Manuscript; echo PREVIOUS > Manuscript/COMBINED.md
    write Chapter01 ""; write Chapter02 "  \n\n"
    "${combine[@]}" >/dev/null 2>&1
    check "all-empty book is an error" "$?" "1"
    check "all-empty book keeps previous output" "$(cat Manuscript/COMBINED.md)" "PREVIOUS"

    new_book "$label-one-empty"
    write Chapter01 "BODY-one\n"; write Chapter02 ""; write Chapter03 "BODY-three\n"
    output="$("${combine[@]}" 2>&1)"
    check "empty chapter does not stop the book" "$?" "0"
    check "empty chapter skipped" "$(bodies)" "one three"
    check "empty chapter adds no blank page" "$(grep -c 'page-break-before' Manuscript/COMBINED.md)" "1"
    case "$output" in *"Chapter02.md (the file is empty)"*) pass "empty chapter is reported" ;; *) fail "empty chapter is reported" ;; esac
    check "no temp files or folders left" "$(find Manuscript -name '.*' | wc -l | tr -d ' ')" "0"

    new_book "$label-unicode"
    write Chapter01 "Caf\xc3\xa9 \xe2\x80\x94 na\xc3\xafve\n"
    "${combine[@]}" >/dev/null 2>&1
    check "unicode preserved" "$(cat Manuscript/COMBINED.md)" "$(printf 'Caf\xc3\xa9 \xe2\x80\x94 na\xc3\xafve')"
    check "no byte order mark" "$(head -c 3 Manuscript/COMBINED.md | od -An -tx1 | tr -d ' ')" "436166"
}

run_combine_suite bash --strict bash book-memory-bank/Production/Scripts/combine_chapters.sh

if command -v pwsh >/dev/null 2>&1; then
    run_combine_suite powershell -Strict pwsh -NoProfile -File book-memory-bank/Production/Scripts/combine_chapters.ps1
else
    echo "combine (powershell): SKIPPED, pwsh not found"
fi

echo "docx"
GENERATE=book-memory-bank/Production/Scripts/generate_docx.sh
NO_PANDOC="$WORK/no-pandoc"
mkdir -p "$NO_PANDOC"
for tool in bash dirname; do ln -s "$(command -v "$tool")" "$NO_PANDOC/$tool"; done

new_book docx-missing
write Chapter01 "x\n"; mkdir -p Manuscript; echo PREVIOUS > Manuscript/BOOK.docx
PATH="$NO_PANDOC" bash "$GENERATE" --no-open >/dev/null 2>&1
check "missing Pandoc is an error" "$?" "1"
check "missing Pandoc keeps previous docx" "$(cat Manuscript/BOOK.docx)" "PREVIOUS"

if command -v pandoc >/dev/null 2>&1; then
    new_book docx-empty
    mkdir -p Manuscript; echo PREVIOUS > Manuscript/BOOK.docx
    bash "$GENERATE" --no-open >/dev/null 2>&1
    check "no chapters keeps previous docx" "$(cat Manuscript/BOOK.docx)" "PREVIOUS"

    new_book docx-flags
    write Chapter01 "Text [NEED RESEARCH: a date]\n"; mkdir -p Manuscript; echo PREVIOUS > Manuscript/BOOK.docx
    bash "$GENERATE" --no-open >/dev/null 2>&1
    check "final build stops on flags" "$?" "3"
    check "flags keep previous docx" "$(cat Manuscript/BOOK.docx)" "PREVIOUS"
    bash "$GENERATE" --draft --no-open >/dev/null 2>&1
    check "draft build allows flags" "$?" "0"
    if [ -f Manuscript/BOOK_DRAFT.docx ]; then pass "draft file written"; else fail "draft file written"; fi

    new_book docx-real
    write Prologue "# Prologue\n\nOpening.\n"
    write Chapter01 "# One\n\nFirst scene line.\n---\nSecond scene.\n"
    write Chapter02 "# Two\n\nBody.\n"
    bash "$GENERATE" --no-open >/dev/null 2>&1
    check "docx build succeeds" "$?" "0"
    result="$(python3 - <<'PY'
import re, zipfile
xml = zipfile.ZipFile('Manuscript/BOOK.docx').read('word/document.xml').decode()
breaks = len(re.findall(r'w:br w:type="page"', xml))
headings = len(re.findall(r'w:pStyle w:val="Heading2"', xml))
print(breaks, headings)
PY
)"
    check "two page breaks, no false headings" "$result" "2 0"
    leftovers="$(find Manuscript -name '.*' -type f | wc -l | tr -d ' ')"
    check "no temp files left" "$leftovers" "0"
else
    echo "docx conversion: SKIPPED, pandoc not found"
fi

echo
echo "$PASSED passed, $FAILED failed"
[ "$FAILED" -eq 0 ]
