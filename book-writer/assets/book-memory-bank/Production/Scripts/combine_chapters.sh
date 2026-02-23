#!/usr/bin/env bash

# Bash Script to Combine Chapter Files into a Complete Manuscript
# This script assembles individual chapter Markdown files into a single complete manuscript.

# Configuration variables - modify these for your project
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="$(cd "$SCRIPT_DIR/../../.." && pwd)"
CHAPTERS_DIR="$PROJECT_ROOT/Chapters"
MANUSCRIPT_DIR="$PROJECT_ROOT/Manuscript"
OUTPUT_FILE="$MANUSCRIPT_DIR/COMBINED.md"
FRONT_MATTER_FILE="$PROJECT_ROOT/Front_Matter.md"
BACK_MATTER_FILE="$PROJECT_ROOT/Back_Matter.md"
CHAPTER_PREFIX="Chapter"

# Colors for log output
CYAN='\033[0;36m'
GREEN='\033[0;32m'
RED='\033[0;31m'
NC='\033[0m' # No Color

write_log() {
    local message=$1
    local color=$2
    echo -e "${color}${message}${NC}"
}

create_complete_manuscript() {
    write_log "Starting manuscript assembly process..." "$CYAN"

    # Check if chapters directory exists
    if [ ! -d "$CHAPTERS_DIR" ]; then
        write_log "Error: Chapters directory not found at $CHAPTERS_DIR" "$RED"
        exit 1
    fi

    # Create Manuscript directory if it doesn't exist
    if [ ! -d "$MANUSCRIPT_DIR" ]; then
        write_log "Creating Manuscript directory at $MANUSCRIPT_DIR" "$CYAN"
        mkdir -p "$MANUSCRIPT_DIR"
    fi

    # Get all chapter files and sort them numerically
    shopt -s nullglob
    CHAPTER_FILES=("$CHAPTERS_DIR"/$CHAPTER_PREFIX*.md)
    if [ ${#CHAPTER_FILES[@]} -eq 0 ]; then
        write_log "Error: No chapter files found in $CHAPTERS_DIR" "$RED"
        exit 1
    fi

    # Sort files numerically
    IFS=$'\n' sorted_files=($(sort -V <<<"${CHAPTER_FILES[*]}"))
    unset IFS

    write_log "Found ${#sorted_files[@]} chapter files to process" "$GREEN"

    # Clear or create the output file
    > "$OUTPUT_FILE"

    # Add front matter if it exists
    if [ -f "$FRONT_MATTER_FILE" ]; then
        write_log "Adding front matter from $FRONT_MATTER_FILE" "$GREEN"
        cat "$FRONT_MATTER_FILE" >> "$OUTPUT_FILE"
    fi

    # Add each chapter to the output file
    for file in "${sorted_files[@]}"; do
        write_log "Processing $(basename "$file")..." "$CYAN"
        printf "\n\n<div style='page-break-before: always;'></div>\n\n" >> "$OUTPUT_FILE"
        cat "$file" >> "$OUTPUT_FILE"
    done

    # Add back matter if it exists
    if [ -f "$BACK_MATTER_FILE" ]; then
        write_log "Adding back matter from $BACK_MATTER_FILE" "$GREEN"
        printf "\n\n<div style='page-break-before: always;'></div>\n\n" >> "$OUTPUT_FILE"
        cat "$BACK_MATTER_FILE" >> "$OUTPUT_FILE"
    fi

    write_log "Manuscript assembly complete! Output file: $OUTPUT_FILE" "$GREEN"
    write_log "Total chapters: ${#sorted_files[@]}" "$GREEN"
    
    # Simple word count estimate
    word_count=$(wc -w < "$OUTPUT_FILE" | tr -d ' ')
    write_log "Word count estimate: $word_count words" "$GREEN"
}

# Main execution
create_complete_manuscript || {
    write_log "Error occurred during manuscript assembly." "$RED"
    exit 1
}
