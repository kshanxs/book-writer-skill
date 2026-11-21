#!/usr/bin/env bash
#
# Build a Word document from the chapters.
#
# Usage: generate_docx.sh [--draft] [--no-open]
#   --draft    Allow open [NEED RESEARCH] flags and write BOOK_DRAFT.docx.
#   --no-open  Do not open the finished file (use this for automated runs).
#
# The previous document is only replaced after a successful conversion.

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="$(cd "$SCRIPT_DIR/../../.." && pwd)"
MANUSCRIPT_DIR="$PROJECT_ROOT/Manuscript"
COMBINED_FILE="$MANUSCRIPT_DIR/COMBINED.md"
REF_DOCX="$SCRIPT_DIR/reference.docx"
LUA_FILTER="$SCRIPT_DIR/page_breaks.lua"

DRAFT=0
OPEN=1
for arg in "$@"; do
    case "$arg" in
        --draft) DRAFT=1 ;;
        --no-open) OPEN=0 ;;
        -h|--help) sed -n '3,9p' "${BASH_SOURCE[0]}" | sed 's/^# \{0,1\}//'; exit 0 ;;
        *) echo "Unknown option: $arg (try --help)" >&2; exit 2 ;;
    esac
done

if ! command -v pandoc >/dev/null 2>&1; then
    echo "Error: Pandoc is not installed. Your existing files were not changed." >&2
    echo "Install it from https://pandoc.org/installing.html" >&2
    echo "  Mac: brew install pandoc" >&2
    echo "  Linux: sudo apt-get install pandoc" >&2
    exit 1
fi

if [ "$DRAFT" -eq 1 ]; then
    DOCX_FILE="$MANUSCRIPT_DIR/BOOK_DRAFT.docx"
    bash "$SCRIPT_DIR/combine_chapters.sh"
else
    DOCX_FILE="$MANUSCRIPT_DIR/BOOK.docx"
    status=0
    bash "$SCRIPT_DIR/combine_chapters.sh" --strict || status=$?
    if [ "$status" -ne 0 ]; then
        if [ "$status" -eq 3 ]; then
            echo "For a review copy that keeps the flags, run: generate_docx.sh --draft" >&2
        fi
        exit "$status"
    fi
fi

TEMP_DOCX="$(mktemp "$MANUSCRIPT_DIR/.book.XXXXXX")"
trap 'rm -f "$TEMP_DOCX"' EXIT

PANDOC_ARGS=(-s "$COMBINED_FILE" -o "$TEMP_DOCX" --from markdown --to docx --lua-filter="$LUA_FILTER")
if [ -f "$REF_DOCX" ]; then
    PANDOC_ARGS+=(--reference-doc="$REF_DOCX")
else
    echo "Note: no reference.docx found, so Pandoc's default styling will be used."
fi

pandoc "${PANDOC_ARGS[@]}"
mv -f "$TEMP_DOCX" "$DOCX_FILE"
echo "Word document ready: $DOCX_FILE"

if [ "$OPEN" -eq 1 ]; then
    if [[ "$OSTYPE" == darwin* ]]; then
        open "$DOCX_FILE" || echo "Please open $DOCX_FILE manually."
    elif command -v xdg-open >/dev/null 2>&1 && [ -n "${DISPLAY:-}${WAYLAND_DISPLAY:-}" ]; then
        xdg-open "$DOCX_FILE" >/dev/null 2>&1 || echo "Please open $DOCX_FILE manually."
    fi
fi
