# Combine chapter files into Manuscript\COMBINED.md.
#
# Reading order: Prologue, Chapter 1..N (InterludeN follows ChapterN), Epilogue.
# Names may use spaces, underscores, or hyphens: Chapter01.md, chapter-1.md,
# "Chapter 1 - The Road.md". Old copies such as Chapter01_old.md are skipped.
#
# Usage: combine_chapters.ps1 [-Strict]
#   -Strict  Stop if any chapter still contains a [NEED RESEARCH] flag.
#
# Exit codes: 0 success, 1 assembly error, 3 open research flags.
# The previous COMBINED.md is only replaced after a complete, successful build.

param([switch]$Strict)

$ErrorActionPreference = 'Stop'

$projectRoot = (Get-Item $PSScriptRoot).Parent.Parent.Parent.FullName
$chaptersDir = Join-Path $projectRoot 'Chapters'
$manuscriptDir = Join-Path $projectRoot 'Manuscript'
$outputFile = Join-Path $manuscriptDir 'COMBINED.md'
$frontMatterFile = Join-Path $projectRoot 'Front_Matter.md'
$backMatterFile = Join-Path $projectRoot 'Back_Matter.md'
$pageBreak = "<div style='page-break-before: always;'></div>"
$flag = '[NEED RESEARCH'
$utf8 = New-Object System.Text.UTF8Encoding($false)

function Write-BookWarning([string]$Message) {
    [Console]::Error.WriteLine("Warning: $Message")
}

function Stop-Build([string]$Message, [int]$Code = 1) {
    [Console]::Error.WriteLine("Error: $Message")
    exit $Code
}

# Returns section/number/order for a recognized name, 'retired' for an old
# copy, and $null for a file that is not part of the book.
function Get-ChapterKey([string]$Stem) {
    $name = $Stem.ToLowerInvariant()
    if ($name -match '^prologue(.*)$') {
        $section = 0; $number = 0; $order = 0; $rest = $Matches[1]
    } elseif ($name -match '^chapter[\s_.-]*(\d+)(.*)$') {
        $section = 1; $number = [int]$Matches[1]; $order = 0; $rest = $Matches[2]
    } elseif ($name -match '^interlude[\s_.-]*(\d+)(.*)$') {
        $section = 1; $number = [int]$Matches[1]; $order = 1; $rest = $Matches[2]
    } elseif ($name -match '^epilogue(.*)$') {
        $section = 2; $number = 0; $order = 0; $rest = $Matches[1]
    } else {
        return $null
    }

    $rest = ($rest -replace '[()]', ' ') -replace '^[\s_.-]+', '' -replace '[\s_.-]+$', ''
    if ($rest -match '^(old|draft|backup|bak|copy|wip|archive|prev|previous|v\d+|rev\d*)([\s_.-]*\d+)?$') {
        return 'retired'
    }
    return [pscustomobject]@{ Section = $section; Number = $number; Order = $order }
}

# Puts blank lines around "---" so Pandoc reads a scene break, not a heading.
function Format-SceneBreaks([string]$Text) {
    $lines = @($Text -split "`r?`n")
    if ($lines.Count -gt 0 -and $lines[-1] -eq '') {
        if ($lines.Count -gt 1) { $lines = @($lines[0..($lines.Count - 2)]) } else { $lines = @() }
    }
    $out = New-Object System.Collections.Generic.List[string]
    $inFence = $false
    $inYaml = $false
    $needBlank = $false
    $previous = ''

    for ($i = 0; $i -lt $lines.Count; $i++) {
        $line = $lines[$i]
        if ($i -eq 0 -and $line -match '^ *--- *$' -and $lines.Count -gt 1 -and $lines[1] -match '^[A-Za-z0-9_-]+:') {
            $out.Add('---'); $inYaml = $true; continue
        }
        if ($inYaml) {
            $out.Add($line)
            if ($line -match '^(---|\.\.\.) *$') { $inYaml = $false; $previous = $line }
            continue
        }
        if ($line -match '^ {0,3}(```|~~~)') { $inFence = -not $inFence }
        elseif (-not $inFence -and $line -match '^ *--- *$') {
            if ($previous -ne '') { $out.Add('') }
            $out.Add('---')
            $previous = '---'
            $needBlank = $true
            continue
        }
        if ($needBlank -and $line -ne '') { $out.Add('') }
        $needBlank = $false
        $out.Add($line)
        $previous = $line
    }
    return ($out -join "`n") + "`n"
}

if (-not (Test-Path -LiteralPath $chaptersDir -PathType Container)) {
    Stop-Build "Chapters directory not found at $chaptersDir"
}
New-Item -ItemType Directory -Force -Path $manuscriptDir | Out-Null

$entries = @()
foreach ($file in Get-ChildItem -LiteralPath $chaptersDir -File | Where-Object { $_.Extension -eq '.md' }) {
    $key = Get-ChapterKey $file.BaseName
    if ($null -eq $key) {
        Write-BookWarning "Skipping $($file.Name) (not a Prologue, Chapter, Interlude, or Epilogue name)"
    } elseif ($key -is [string]) {
        Write-BookWarning "Skipping $($file.Name) (looks like an old copy)"
    } else {
        $entries += [pscustomobject]@{ Section = $key.Section; Number = $key.Number; Order = $key.Order; File = $file }
    }
}

if ($entries.Count -eq 0) { Stop-Build "No chapter files found in $chaptersDir" }

$entries = @($entries | Sort-Object Section, Number, Order)

$duplicates = @($entries | Group-Object Section, Number, Order | Where-Object { $_.Count -gt 1 })
if ($duplicates.Count -gt 0) {
    foreach ($group in $duplicates) {
        [Console]::Error.WriteLine('Error: these files claim the same place in the book:')
        foreach ($entry in $group.Group) { [Console]::Error.WriteLine("  $($entry.File.FullName)") }
    }
    exit 1
}

$numbers = @($entries | Where-Object { $_.Section -eq 1 -and $_.Order -eq 0 } | ForEach-Object { $_.Number })
$gaps = @()
for ($i = 1; $i -lt $numbers.Count; $i++) {
    if ($numbers[$i] -gt $numbers[$i - 1] + 1) { $gaps += "$($numbers[$i - 1] + 1)-$($numbers[$i] - 1)" }
}
if ($gaps.Count -gt 0) { Write-BookWarning "Chapter numbers are missing: $($gaps -join ' ')" }

$sources = @()
if (Test-Path -LiteralPath $frontMatterFile) { $sources += $frontMatterFile }
$sources += @($entries | ForEach-Object { $_.File.FullName })
if (Test-Path -LiteralPath $backMatterFile) { $sources += $backMatterFile }

$tempOutput = Join-Path $manuscriptDir ('.combined.' + [guid]::NewGuid().ToString('N'))
try {
    $texts = @{}
    $flagged = 0
    foreach ($source in $sources) {
        try {
            $texts[$source] = [IO.File]::ReadAllText($source, $utf8)
        } catch {
            Stop-Build "Cannot read $source"
        }
        $count = ([regex]::Matches($texts[$source], [regex]::Escape($flag))).Count
        if ($count -gt 0) {
            Write-BookWarning "$(Split-Path -Leaf $source) has $count open [NEED RESEARCH] flag(s)"
            $flagged += $count
        }
    }
    if ($Strict -and $flagged -gt 0) {
        Stop-Build "resolve $flagged research flag(s) before the final build." 3
    }

    Write-Host "Assembling $($entries.Count) chapter file(s)..."
    $builder = New-Object System.Text.StringBuilder
    foreach ($source in $sources) {
        if ($builder.Length -gt 0) { [void]$builder.Append("`n`n$pageBreak`n`n") }
        [void]$builder.Append((Format-SceneBreaks $texts[$source]))
    }

    [IO.File]::WriteAllText($tempOutput, $builder.ToString(), $utf8)
    Move-Item -LiteralPath $tempOutput -Destination $outputFile -Force

    $plain = $builder.ToString().Replace($pageBreak, ' ')
    $words = ([regex]::Matches($plain, '\S+')).Count
    Write-Host "Manuscript complete: $outputFile"
    Write-Host "Chapter files: $($entries.Count). Estimated words: $words."
} catch {
    [Console]::Error.WriteLine("Error: manuscript assembly failed: $_")
    exit 1
} finally {
    if (Test-Path -LiteralPath $tempOutput) { Remove-Item -LiteralPath $tempOutput -Force }
}
