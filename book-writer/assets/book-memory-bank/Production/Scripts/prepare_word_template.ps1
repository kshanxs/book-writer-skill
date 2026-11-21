# PowerShell Script to Create Word Reference Template for Pandoc Conversion
# This script generates a properly formatted Word document template with styles that
# Pandoc will use when converting markdown to DOCX format.
# An existing reference.docx is kept unless you pass -Force.

param([switch]$Force)

# Configuration variables - modify for your specific styling needs
$scriptDir = $PSScriptRoot
$templateFile = Join-Path -Path $scriptDir -ChildPath "reference.docx"  # Output template file
$fontFamily = "Times New Roman"  # Default body font
$titleFont = "Georgia"  # Font for title elements
$bodySize = 12  # Point size for body text
$headingBaseSize = 16  # Base point size for headings
$lineSpacing = 1.5  # Line spacing for body text

function Write-Log {
    param (
        [string]$Message,
        [string]$Color = "White"
    )
    Write-Host $Message -ForegroundColor $Color
}

function Create-WordTemplate {
    if ((Test-Path -LiteralPath $templateFile) -and -not $Force) {
        Write-Log "Keeping existing template: $templateFile" "Green"
        return
    }

    Write-Log "Creating Word reference template for formatting..." "Cyan"

    # Check if Word is installed
    try {
        $word = New-Object -ComObject Word.Application
    } catch {
        Write-Log "Microsoft Word is not available, so no template was created." "Yellow"
        exit 1
    }

    $doc = $null
    try {
    # Make Word invisible
    $word.Visible = $false

    # Create a new document
    $doc = $word.Documents.Add()

    # Configure styles
    # Title style
    $titleStyle = $doc.Styles.Item("Title")
    $titleStyle.Font.Name = $titleFont
    $titleStyle.Font.Size = 24
    $titleStyle.Font.Bold = $true
    $titleStyle.ParagraphFormat.Alignment = 1  # Center aligned
    $titleStyle.ParagraphFormat.SpaceAfter = 24  # Space after in points
    
    # Heading 1 (Chapter Titles). page_breaks.lua adds the page break before each chapter.
    $h1Style = $doc.Styles.Item("Heading 1")
    $h1Style.Font.Name = $titleFont
    $h1Style.Font.Size = $headingBaseSize + 4  # 20pt
    $h1Style.Font.Bold = $true
    $h1Style.ParagraphFormat.Alignment = 1  # Center aligned
    $h1Style.ParagraphFormat.SpaceAfter = 24  # Space after in points
    $h1Style.ParagraphFormat.SpaceBefore = 36  # Space before in points
    
    # Heading 2 (Section Headings)
    $h2Style = $doc.Styles.Item("Heading 2")
    $h2Style.Font.Name = $titleFont
    $h2Style.Font.Size = $headingBaseSize + 2  # 18pt
    $h2Style.Font.Bold = $true
    $h2Style.ParagraphFormat.SpaceAfter = 12
    $h2Style.ParagraphFormat.SpaceBefore = 24
    
    # Heading 3 (Subsections)
    $h3Style = $doc.Styles.Item("Heading 3")
    $h3Style.Font.Name = $titleFont
    $h3Style.Font.Size = $headingBaseSize  # 16pt
    $h3Style.Font.Bold = $true
    $h3Style.Font.Italic = $true
    $h3Style.ParagraphFormat.SpaceAfter = 12
    $h3Style.ParagraphFormat.SpaceBefore = 12
    
    # Normal text (Body)
    $normalStyle = $doc.Styles.Item("Normal")
    $normalStyle.Font.Name = $fontFamily
    $normalStyle.Font.Size = $bodySize
    $normalStyle.ParagraphFormat.LineSpacingRule = 1  # Line spacing
    $normalStyle.ParagraphFormat.LineSpacing = $lineSpacing * 12  # Convert to points
    $normalStyle.ParagraphFormat.SpaceAfter = 8
    $normalStyle.ParagraphFormat.FirstLineIndent = 0  # No indent for new paragraphs
    $normalStyle.ParagraphFormat.Alignment = 3  # Justified text (3 = wdAlignParagraphJustify)
    
    # Pandoc's body paragraph styles
    foreach ($bodyName in @("Body Text", "First Paragraph")) {
        try {
            $bodyStyle = $doc.Styles.Item($bodyName)
        } catch {
            $bodyStyle = $doc.Styles.Add($bodyName, 1)
        }
        $bodyStyle.BaseStyle = "Normal"
    }

    # Blockquote (Pandoc uses the "Block Text" style)
    try {
        try {
            $blockStyle = $doc.Styles.Item("Block Text")
        } catch {
            $blockStyle = $doc.Styles.Add("Block Text", 1)
        }
        $blockStyle.Font.Name = $fontFamily
        $blockStyle.Font.Size = $bodySize
        $blockStyle.Font.Italic = $true
        $blockStyle.ParagraphFormat.LeftIndent = 36  # Left indent
        $blockStyle.ParagraphFormat.RightIndent = 36  # Right indent
        $blockStyle.ParagraphFormat.SpaceAfter = 12
        $blockStyle.ParagraphFormat.SpaceBefore = 12
    } catch {
        Write-Log "Blockquote style already exists or could not be created. Continuing..." "Yellow"
    }
    
    # Code blocks (Pandoc uses the "Source Code" style)
    try {
        try {
            $codeStyle = $doc.Styles.Item("Source Code")
        } catch {
            $codeStyle = $doc.Styles.Add("Source Code", 1)
        }
        $codeStyle.Font.Name = "Consolas"
        $codeStyle.Font.Size = $bodySize - 2  # Slightly smaller
        $codeStyle.ParagraphFormat.LeftIndent = 36
        $codeStyle.ParagraphFormat.RightIndent = 36
        $codeStyle.ParagraphFormat.SpaceAfter = 12
        $codeStyle.ParagraphFormat.SpaceBefore = 12
    } catch {
        Write-Log "Code style already exists or could not be created. Continuing..." "Yellow"
    }
    
    # Page setup
    $doc.PageSetup.TopMargin = 72  # 1 inch in points
    $doc.PageSetup.BottomMargin = 72
    $doc.PageSetup.LeftMargin = 72
    $doc.PageSetup.RightMargin = 72
    
    # Add sample content - this helps ensure styles are saved properly
    $doc.Content.InsertAfter("Title Example`r`n")
    $doc.Content.Paragraphs.Last.Style = $doc.Styles.Item("Title")
    
    $doc.Content.InsertAfter("`r`nChapter 1: Chapter Title Example`r`n")
    $doc.Content.Paragraphs.Last.Style = $doc.Styles.Item("Heading 1")
    
    $doc.Content.InsertAfter("`r`nSection Heading Example`r`n")
    $doc.Content.Paragraphs.Last.Style = $doc.Styles.Item("Heading 2")
    
    $doc.Content.InsertAfter("`r`nSubsection Example`r`n")
    $doc.Content.Paragraphs.Last.Style = $doc.Styles.Item("Heading 3")
    
    $doc.Content.InsertAfter("`r`nThis is an example of body text formatting. It demonstrates the paragraph style, font family, size, and line spacing that will be used in the document.`r`n")
    $doc.Content.Paragraphs.Last.Style = $doc.Styles.Item("Normal")
    
    # Save the document
    $savePath = $templateFile.ToString()
    $doc.SaveAs($savePath, 16) # 16 = wdFormatDocumentDefault
    } finally {
        # Always close Word, even when a step above fails
        if ($doc) {
            $doc.Close(0)
            [System.Runtime.Interopservices.Marshal]::ReleaseComObject($doc) | Out-Null
        }
        $word.Quit()
        [System.Runtime.Interopservices.Marshal]::ReleaseComObject($word) | Out-Null
        [System.GC]::Collect()
        [System.GC]::WaitForPendingFinalizers()
    }

    Write-Log "Word reference template created successfully: $templateFile" "Green"
}

# Main execution
try {
    Create-WordTemplate
} catch {
    Write-Log "Error creating Word template: $_" "Red"
    exit 1
}
