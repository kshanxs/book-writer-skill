@echo off
setlocal

rem Build a Word document from the chapters.
rem Usage: generate_docx.bat [--draft] [--no-open]
rem   --draft    Allow open [NEED RESEARCH] flags and write BOOK_DRAFT.docx.
rem   --no-open  Do not open the file or pause (use this for automated runs).
rem The previous document is only replaced after a successful conversion.

set "SCRIPTS=%~dp0"
set "MANUSCRIPT=%~dp0..\..\..\Manuscript"
set "COMBINED=%MANUSCRIPT%\COMBINED.md"
set "REFERENCE=%SCRIPTS%reference.docx"
set "FILTER=%SCRIPTS%page_breaks.lua"
set "OUTPUT=%MANUSCRIPT%\BOOK.docx"
set "STRICT=-Strict"
set "OPEN=1"

:parse
if "%~1"=="" goto parsed
if /i "%~1"=="--draft" (
    set "OUTPUT=%MANUSCRIPT%\BOOK_DRAFT.docx"
    set "STRICT="
    shift
    goto parse
)
if /i "%~1"=="--no-open" (
    set "OPEN=0"
    shift
    goto parse
)
echo Unknown option: %~1
set "CODE=2"
goto fail

:parsed
where pandoc >nul 2>&1
if errorlevel 1 (
    echo Error: Pandoc is not installed. Your existing files were not changed.
    echo Install it from https://pandoc.org/installing.html
    set "CODE=1"
    goto fail
)

if not exist "%REFERENCE%" (
    powershell -NoProfile -ExecutionPolicy Bypass -File "%SCRIPTS%prepare_word_template.ps1"
    if errorlevel 1 echo Note: could not create a Word template, so Pandoc's default styling will be used.
)

powershell -NoProfile -ExecutionPolicy Bypass -File "%SCRIPTS%combine_chapters.ps1" %STRICT%
set "CODE=%ERRORLEVEL%"
if "%CODE%"=="3" echo For a review copy that keeps the flags, run: generate_docx.bat --draft
if not "%CODE%"=="0" goto fail

set "TEMP_DOCX=%MANUSCRIPT%\.book_%RANDOM%%RANDOM%.docx"
if exist "%REFERENCE%" (
    pandoc -s "%COMBINED%" -o "%TEMP_DOCX%" --from markdown --to docx --lua-filter="%FILTER%" --reference-doc="%REFERENCE%"
) else (
    pandoc -s "%COMBINED%" -o "%TEMP_DOCX%" --from markdown --to docx --lua-filter="%FILTER%"
)
if errorlevel 1 (
    if exist "%TEMP_DOCX%" del "%TEMP_DOCX%"
    echo Error: Pandoc could not build the document. Your previous document was kept.
    set "CODE=1"
    goto fail
)

move /y "%TEMP_DOCX%" "%OUTPUT%" >nul
if errorlevel 1 (
    if exist "%TEMP_DOCX%" del "%TEMP_DOCX%"
    echo Error: could not replace the Word file. Close it in Word and try again.
    set "CODE=1"
    goto fail
)

echo Word document ready: %OUTPUT%
if "%OPEN%"=="1" (
    start "" "%OUTPUT%"
    pause
)
exit /b 0

:fail
if "%OPEN%"=="1" pause
exit /b %CODE%
