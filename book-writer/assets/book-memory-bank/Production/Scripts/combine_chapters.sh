#!/usr/bin/env bash
#
# Combine chapter files into Manuscript/COMBINED.md.
#
# Reading order: Prologue, Chapter 1..N (InterludeN follows ChapterN), Epilogue.
# Names may use spaces, underscores, or hyphens: Chapter01.md, chapter-1.md,
# "Chapter 1 - The Road.md". Old copies such as Chapter01_old.md are skipped.
#
# Usage: combine_chapters.sh [--strict]
#   --strict  Stop if any chapter still contains a [NEED RESEARCH] flag.
#
# Exit codes: 0 success, 1 assembly error, 2 bad usage, 3 open research flags.
# The previous COMBINED.md is only replaced after a complete, successful build.

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="$(cd "$SCRIPT_DIR/../../.." && pwd)"
CHAPTERS_DIR="$PROJECT_ROOT/Chapters"
MANUSCRIPT_DIR="$PROJECT_ROOT/Manuscript"
OUTPUT_FILE="$MANUSCRIPT_DIR/COMBINED.md"
FRONT_MATTER_FILE="$PROJECT_ROOT/Front_Matter.md"
BACK_MATTER_FILE="$PROJECT_ROOT/Back_Matter.md"
PAGE_BREAK="<div style='page-break-before: always;'></div>"
FLAG='[NEED RESEARCH'

STRICT=0
for arg in "$@"; do
    case "$arg" in
        --strict) STRICT=1 ;;
        -h|--help) sed -n '3,13p' "${BASH_SOURCE[0]}" | sed 's/^# \{0,1\}//'; exit 0 ;;
        *) echo "Unknown option: $arg (try --help)" >&2; exit 2 ;;
    esac
done

info() { echo "$1"; }
warn() { echo "Warning: $1" >&2; }
die() { echo "Error: $1" >&2; exit 1; }

# Prints "section number order" for a recognized name, "retired" for an old
# copy, and nothing for a file that is not part of the book.
classify() {
    local stem rest section number order
    stem="$(printf '%s' "$1" | tr '[:upper:]' '[:lower:]')"
    if [[ "$stem" =~ ^prologue(.*)$ ]]; then
        section=0; number=0; order=0; rest="${BASH_REMATCH[1]}"
    elif [[ "$stem" =~ ^chapter[[:space:]_.-]*([0-9]+)(.*)$ ]]; then
        section=1; number=$((10#${BASH_REMATCH[1]})); order=0; rest="${BASH_REMATCH[2]}"
    elif [[ "$stem" =~ ^interlude[[:space:]_.-]*([0-9]+)(.*)$ ]]; then
        section=1; number=$((10#${BASH_REMATCH[1]})); order=1; rest="${BASH_REMATCH[2]}"
    elif [[ "$stem" =~ ^epilogue(.*)$ ]]; then
        section=2; number=0; order=0; rest="${BASH_REMATCH[1]}"
    else
        return 0
    fi

    rest="${rest//[()]/ }"
    while [[ "$rest" =~ ^[[:space:]_.-](.*)$ ]]; do rest="${BASH_REMATCH[1]}"; done
    while [[ "$rest" =~ ^(.*)[[:space:]_.-]$ ]]; do rest="${BASH_REMATCH[1]}"; done
    if [[ "$rest" =~ ^(old|draft|backup|bak|copy|wip|archive|prev|previous|v[0-9]+|rev[0-9]*)([[:space:]_.-]*[0-9]+)?$ ]]; then
        echo "retired"
    else
        echo "$section $number $order"
    fi
}

# Puts blank lines around "---" so Pandoc reads a scene break, not a heading.
normalize_scene_breaks() {
    awk '
    function emit(text) {
        if (need_blank && text != "") print ""
        need_blank = 0
        print text
        previous = text
    }
    function scene_break() {
        if (previous != "") print ""
        print "---"
        previous = "---"
        need_blank = 1
    }
    {
        line = $0
        sub(/\r$/, "", line)
        if (NR == 1 && line ~ /^ *--- *$/) { pending = 1; next }
        if (pending) {
            pending = 0
            if (line ~ /^[A-Za-z0-9_-]+:/) { print "---"; in_yaml = 1 } else scene_break()
        }
        if (in_yaml) {
            print line
            if (line ~ /^(---|\.\.\.) *$/) { in_yaml = 0; previous = line }
            next
        }
        if (line ~ /^ ? ? ?(```|~~~)/) { in_fence = !in_fence; emit(line); next }
        if (!in_fence && line ~ /^ *--- *$/) { scene_break(); next }
        emit(line)
    }
    END { if (pending) print "---" }
    ' "$1"
}

[ -d "$CHAPTERS_DIR" ] || die "Chapters directory not found at $CHAPTERS_DIR"
mkdir -p "$MANUSCRIPT_DIR"

INDEX="$(mktemp "$MANUSCRIPT_DIR/.chapters.XXXXXX")"
TEMP_OUTPUT="$(mktemp "$MANUSCRIPT_DIR/.combined.XXXXXX")"
trap 'rm -f "$INDEX" "$TEMP_OUTPUT"' EXIT

shopt -s nullglob
for file in "$CHAPTERS_DIR"/*.md; do
    name="$(basename "$file")"
    key="$(classify "${name%.md}")"
    case "$key" in
        "") warn "Skipping $name (not a Prologue, Chapter, Interlude, or Epilogue name)" ;;
        retired) warn "Skipping $name (looks like an old copy)" ;;
        *) printf '%s\t%s\n' "$key" "$file" >> "$INDEX" ;;
    esac
done

[ -s "$INDEX" ] || die "No chapter files found in $CHAPTERS_DIR"

SORTED="$(LC_ALL=C sort -t ' ' -k1,1n -k2,2n -k3,3n "$INDEX")"

DUPLICATES="$(printf '%s\n' "$SORTED" | cut -f1 | uniq -d)"
if [ -n "$DUPLICATES" ]; then
    while IFS= read -r key; do
        echo "Error: these files claim the same place in the book:" >&2
        printf '%s\n' "$SORTED" | awk -F '\t' -v k="$key" '$1 == k { print "  " $2 }' >&2
    done <<< "$DUPLICATES"
    exit 1
fi

FILES=()
while IFS=$'\t' read -r _ file; do FILES+=("$file"); done <<< "$SORTED"

GAPS="$(printf '%s\n' "$SORTED" | cut -f1 | awk '
    $1 == 1 && $3 == 0 { if (seen && $2 > last + 1) printf "%d-%d ", last + 1, $2 - 1; last = $2; seen = 1 }')"
[ -z "$GAPS" ] || warn "Chapter numbers are missing: $GAPS"

SOURCES=()
[ ! -f "$FRONT_MATTER_FILE" ] || SOURCES+=("$FRONT_MATTER_FILE")
SOURCES+=("${FILES[@]}")
[ ! -f "$BACK_MATTER_FILE" ] || SOURCES+=("$BACK_MATTER_FILE")

for file in "${SOURCES[@]}"; do
    [ -r "$file" ] || die "Cannot read $file"
done

FLAGGED=0
for file in "${SOURCES[@]}"; do
    count="$(grep -Fc "$FLAG" "$file" || true)"
    if [ "$count" -gt 0 ]; then
        warn "$(basename "$file") has $count open [NEED RESEARCH] flag(s)"
        FLAGGED=$((FLAGGED + count))
    fi
done
if [ "$STRICT" -eq 1 ] && [ "$FLAGGED" -gt 0 ]; then
    echo "Error: resolve $FLAGGED research flag(s) before the final build." >&2
    exit 3
fi

info "Assembling ${#FILES[@]} chapter file(s)..."
for file in "${SOURCES[@]}"; do
    if [ -s "$TEMP_OUTPUT" ]; then
        printf '\n\n%s\n\n' "$PAGE_BREAK" >> "$TEMP_OUTPUT"
    fi
    normalize_scene_breaks "$file" >> "$TEMP_OUTPUT"
done

mv -f "$TEMP_OUTPUT" "$OUTPUT_FILE"

WORDS="$(grep -Fv "$PAGE_BREAK" "$OUTPUT_FILE" | wc -w | tr -d ' ')"
info "Manuscript complete: $OUTPUT_FILE"
info "Chapter files: ${#FILES[@]}. Estimated words: $WORDS."
