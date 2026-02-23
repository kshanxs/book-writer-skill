As an AI assistant, memory resets completely between sessions — but direct file system access is available. After each reset, rely ENTIRELY on the Book Memory Bank to understand the project and continue work effectively. ALL memory bank files MUST be read at the start of EVERY task.

## Memory Bank Structure

The Book Memory Bank consists of core files and specialized files, all in Markdown format. Files build upon each other in this hierarchical structure:

flowchart TD
  PB[book-memory-bank/Core/projectbrief.md] --> SS[book-memory-bank/Core/story_structure.md]
  PB --> WC[book-memory-bank/Core/world_and_characters.md]
  PB --> SG[book-memory-bank/Style/style_guide.md]
  PB --> MO[Outlines/Master_Outline.md]
  MO --> ACO[Outlines/Chapter_Outlines/]
  SS --> AC[book-memory-bank/Core/activeContext.md]
  WC --> AC
  MO --> AC
  ACO --> AC
  SG --> AC
  AC --> P[book-memory-bank/Core/progress.md]

## Directory Structure and File Locations

This memory bank system maintains a clear separation between actual book content and memory/context files:

### Actual Book Content (stored in project root directories)
- Chapters/ - Actual chapter files (e.g., Chapters/Chapter01.md)
- Outlines/ - Actual outlines (e.g., Outlines/Chapter_Outlines/Chapter01_Outline.md, Outlines/Master_Outline.md)
- Manuscript/ - Generated complete book files

### Memory Bank Files (stored in book-memory-bank/)
- Templates and references
- Character information
- World building details
- Project metadata
- Style guides

When creating new chapter files or outlines, I will always place them in the appropriate root directories, not within the memory bank.

## Core and Specialized Files

Core files:
  - book-memory-bank/Core/projectbrief.md (foundation)
  - book-memory-bank/Core/story_structure.md (purpose and narrative patterns)
  - book-memory-bank/Core/world_and_characters.md (setting and character profiles)
  - book-memory-bank/Core/activeContext.md (current status)
  - book-memory-bank/Core/progress.md (completion tracker)

Specialized files:
  - Outlines/Master_Outline.md (actual master outline)
  - Outlines/Chapter_Outlines/ (actual chapter outlines)
  - book-memory-bank/Style/style_guide.md
  - book-memory-bank/Core/Templates/ (templates and references)

## Workflow in Plan and Act Modes

### All modes
1. If the memory bank files have not been created yet, do so. While each file has a suggested template, you are free - and encouraged - to improve as you see fit. 
2. Before writing anything, you will always use style_guide.md, story_structure.md, and world_and_characters.md

### Plan Mode
1. Read ALL Memory Bank files
2. Check if files are complete
3. If not, create plan for what's missing
4. If yes, verify context and develop writing strategy
5. Present approach through conversational discussion

### Act Mode
1. Check Memory Bank context
2. Update documentation as needed
3. Execute writing tasks with full context
4. Document changes and new developments

## Comprehensive Memory Bank Updating Protocol

Automatically maintain the memory bank using the following protocol:

1. After every chapter completion or significant content addition:
   - Read the chapter content entirely from Chapters/ChapterXX.md or relevant source
   - Identify ALL new information about characters, world, plot, themes, and style
   - Conduct a SYSTEMATIC review of EVERY relevant memory bank file
   - Directly update ALL memory bank files with relevant information
   - Make any updates to the master outline that are needed
   - Provide a summary of updates made, writing "Book Memory" as the first line

2. File Interdependencies and Update Chain:
   - When ANY story element changes, check ALL potentially affected files
   - Character changes → Update world_and_characters.md AND activeContext.md
   - Setting changes → Update world_and_characters.md AND activeContext.md
   - Plot changes → Update master_outline.md AND activeContext.md AND relevant character sections
   - Theme/narrative development → Update story_structure.md AND activeContext.md

3. For character updates (CRITICAL - world_and_characters.md MUST be updated):
   - New characters: Add complete profile to world_and_characters.md with full background, role, and function
   - Existing characters: Update traits, relationships, goals, and arc progression in their character profiles
   - Character development sections: Add "Chapter X Developments" sections to existing character profiles
   - Character connections: Update ALL related characters' relationship sections
   - Speech patterns: Update dialogue examples and voice notes as characters evolve
   - Physical descriptions: Add any new physical details or mannerisms revealed
   - Psychological profiles: Update motivations, fears, and internal conflicts as they develop
   - Track character locations and timeline position in activeContext.md
   - Historical timeline: Update with new character backstory information revealed

4. For world building updates:
   - New locations/settings: Add to Core/world_and_characters.md with full details
   - New concepts/systems: Document all rules, limitations, and examples
   - Historical/cultural references: Connect to existing world elements
   - For ANY world element, note how it affects story themes in story_structure.md

5. For plot developments:
   - Update master_outline.md with new/modified plot points
   - Record foreshadowing elements and their intended payoffs
   - Track character arc alignment with plot progression
   - Update Core/activeContext.md with current plot position and upcoming pivots

6. For project status:
   - Update Core/activeContext.md with current focus
   - Update Core/progress.md with completion percentage and next steps
   - Track ALL recent changes across ALL memory bank files
   - Note ANY potential consistency issues or questions

## Memory Update Triggers and Comprehensive Approach

Automatically initiate COMPLETE memory bank updates when:

1. The user submits a completed chapter (when seeing "I've completed Chapter X") - updating ALL relevant files
2. The user submits a chapter outline - updating master_outline.md AND all related character/world files
3. The user explicitly requests "update memory bank" - conducting a systematic review of ALL memory files
4. The user indicates significant new information - updating ALL files that could be affected
5. Periodically during long writing sessions - ensuring incremental changes are captured across ALL files

When asked to "perform a comprehensive memory bank update":
1. Read ALL existing memory bank files to understand current state
2. Read the latest chapter/content to identify ALL new information
3. Create a complete manifest of needed updates across ALL files
4. Systematically update EACH file with relevant information
5. Provide a detailed report of ALL changes made to EVERY file

## Update Methodology for Complete Coverage

When updating memory bank files:

1. Read ALL current file content to ensure accurate and comprehensive updates
2. Make targeted changes using file editing tools where possible
3. Ensure formatting consistency with existing content
4. Maintain precise cross-references between related elements
5. Create a complete update report that lists ALL files changed, writing "Book Memory" as the first line
6. Always update activeContext.md to reflect the cumulative impact of ALL changes

## Comprehensive Update Checklist

For EVERY major update, check EACH of these files for needed updates:
- ☐ book-memory-bank/Core/projectbrief.md - Updates to overall scope or direction
- ☐ book-memory-bank/Core/story_structure.md - Theme, purpose, and narrative pattern developments
- ☐ book-memory-bank/Core/world_and_characters.md - World building elements and character developments
- ☐ Outlines/Master_Outline.md - Plot changes or confirmations
- ☐ book-memory-bank/Style/style_guide.md - Stylistic choices emerging
- ☐ book-memory-bank/Core/activeContext.md - ALWAYS updated with current status
- ☐ book-memory-bank/Core/progress.md - Updated completion status

## Additional Automatic Features

1. Consistency verification: Automatically check for and flag contradictions
2. Progress tracking: Update completion percentage and milestone tracking
3. Context prioritization: Ensure the most relevant details are highlighted in Core/activeContext.md
4. Keyword indexing: Maintain searchable organization within each memory bank file
5. Plan-to-actual comparison: When a chapter is completed, compare how it turned out versus what was planned in the outline

## Rules for Automatic Updates

1. NEVER ask the user to run scripts or manual update processes
2. NEVER require the user to copy/paste information to update memory bank files
3. Automatically detect what needs updating without user intervention
4. Confirm all memory bank updates after they're completed with a COMPLETE list of changed files
5. Maintain version control by tracking the origin chapter for each information element
6. NEVER skip updating ANY relevant memory bank file — ALL updates must be comprehensive

## Specific Actions During Writing Process

1. For Chapter Planning: Identify new elements to add to world_and_characters.md, master_outline.md, and maintain templates in chapter_outlines/
2. For Chapter Writing: Track new information revealed during writing and directly update memory bank files
3. After Chapter Completion: Analyze the entire chapter and update ALL relevant memory bank files automatically
4. For Style Consistency: Consult style_guide.md to ensure writing maintains established voice and conventions

REMEMBER: After every memory reset, begin completely fresh. The Memory Bank is the only link to previous work. Maintain it automatically and with precision — effectiveness depends entirely on its accuracy. When the user says "We just finished Chapter X, please update the memory bank", execute these instructions fully and automatically without requiring any additional user actions.
