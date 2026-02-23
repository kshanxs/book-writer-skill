#!/usr/bin/env bash

echo "==============================================="
echo "Manuscript to DOCX Converter for Book Projects"
echo "==============================================="
echo ""
echo "This bash script will:"
echo "1. Clean up old manuscript files"
echo "2. Run the bash script to combine all chapters"
echo "3. Convert the markdown file to DOCX using Pandoc"
echo "4. Open the final DOCX file"
echo ""
echo "Prerequisites:"
echo "- Pandoc must be installed (https://pandoc.org/installing.html)"
echo "  (e.g., brew install pandoc / apt-get install pandoc)"
echo ""
echo "Starting process..."
echo ""

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="$(cd "$SCRIPT_DIR/../../.." && pwd)"
MANUSCRIPT_DIR="$PROJECT_ROOT/Manuscript"
COMBINED_FILE="$MANUSCRIPT_DIR/COMBINED.md"
DOCX_FILE="$MANUSCRIPT_DIR/BOOK.docx"
REF_DOCX="$SCRIPT_DIR/reference.docx"

echo "Step 1: Cleaning up old files..."
if [ ! -d "$MANUSCRIPT_DIR" ]; then
    mkdir -p "$MANUSCRIPT_DIR"
fi
[ -f "$COMBINED_FILE" ] && rm "$COMBINED_FILE"
[ -f "$DOCX_FILE" ] && rm "$DOCX_FILE"
echo "Cleanup complete."
echo ""

# Skip Word template generation since it relies on COM objects specific to Windows Word.
# Provide a warning or default empty reference template if one isn't present
if [ ! -f "$REF_DOCX" ]; then
    echo "Note: No reference.docx found in Scripts directory. Default Pandoc styling will be used."
    # We could theoretically generate an empty docx here with pandoc, but we'll proceed
fi

echo "Step 2: Running bash script to combine chapters..."
if [ -x "$SCRIPT_DIR/combine_chapters.sh" ]; then
    "$SCRIPT_DIR/combine_chapters.sh"
else
    bash "$SCRIPT_DIR/combine_chapters.sh"
fi

if [ $? -ne 0 ]; then
    echo "Error running bash script. Please check the script and try again."
    exit 1
fi
echo "Bash script completed successfully."
echo ""

echo "Step 3: Checking if Pandoc is installed..."
if ! command -v pandoc &> /dev/null; then
    echo "Pandoc not found. Please install Pandoc from https://pandoc.org/installing.html"
    echo "Mac: brew install pandoc"
    echo "Linux: sudo apt-get install pandoc"
    echo "After installing, run this script again."
    exit 1
fi
echo "Pandoc found. Converting markdown to DOCX..."

if [ -f "$REF_DOCX" ]; then
    pandoc -s "$COMBINED_FILE" -o "$DOCX_FILE" --from markdown --to docx --reference-doc="$REF_DOCX"
else
    pandoc -s "$COMBINED_FILE" -o "$DOCX_FILE" --from markdown --to docx
fi

if [ $? -ne 0 ]; then
    echo "Error converting to DOCX. Please check if Manuscript/COMBINED.md exists."
    exit 1
fi
echo "Conversion to DOCX completed successfully."
echo ""

echo "Step 4: Opening DOCX file..."
if [[ "$OSTYPE" == "darwin"* ]]; then
    open "$DOCX_FILE"
elif [[ "$OSTYPE" == "linux-gnu"* ]]; then
    xdg-open "$DOCX_FILE"
else
    echo "Please open $DOCX_FILE manually."
fi
echo ""

echo "============================================="
echo "PROCESS COMPLETED SUCCESSFULLY"
echo "============================================="
echo ""
echo "Next steps:"
echo "1. Review the Word document for formatting issues"
echo "2. Ensure chapter breaks and section formatting looks correct"
echo "3. Run the spell-checker and review any flagged content"
echo "4. Save the properly formatted document"
echo "5. Export to other formats as needed"
echo ""
