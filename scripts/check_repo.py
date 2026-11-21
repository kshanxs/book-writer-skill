#!/usr/bin/env python3
"""Checks the skill's docs for broken links, stale references, and version drift."""

import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
RETIRED = [
    "Cline", "clinerules", "write_to_file", "replace_in_file", "run_command",
    "custom_instructions.md", "Core/Synopsis.md", "Core/Characters.md",
    "Core/Timeline.md", "Core/Story_Structure.md", "chapter-[N]", "file:///",
    "equation budget", "--aspect 1.6:1",
]
# The spinoff link is an example that resolves inside a user's project.
EXAMPLE_LINKS = {"../../../book-memory-bank/Core/world_and_characters.md"}


def tracked_markdown():
    output = subprocess.check_output(["git", "ls-files", "--cached", "--others", "--exclude-standard", "*.md"], cwd=ROOT, text=True)
    return [ROOT / line for line in output.splitlines() if (ROOT / line).exists()]


def without_code(text):
    return re.sub(r"`[^`\n]*`", "", re.sub(r"```.*?```", "", text, flags=re.S))


def main():
    errors = []
    for path in tracked_markdown():
        name = path.relative_to(ROOT)
        text = path.read_text(encoding="utf8")
        if name != Path("CHANGELOG.md"):
            errors += [f"{name}: retired reference '{word}'" for word in RETIRED if word in text]
        for target in re.findall(r"\]\(([^)\s]+)", without_code(text)):
            target = target.split("#")[0]
            if not target or "{{" in target or target in EXAMPLE_LINKS or re.match(r"[a-z]+:", target):
                continue
            if not (path.parent / target).exists():
                errors.append(f"{name}: broken link '{target}'")

    skill = ROOT / "book-writer"
    for ref in set(re.findall(r"references/[\w-]+\.md", (skill / "SKILL.md").read_text(encoding="utf8"))):
        if not (skill / ref).exists():
            errors.append(f"SKILL.md: missing {ref}")

    active = skill / "assets/book-memory-bank/Core/activeContext.md"
    if "## Memory Status & File Index" not in active.read_text(encoding="utf8"):
        errors.append("activeContext.md: missing Memory Status & File Index")

    changelog = (ROOT / "CHANGELOG.md").read_text(encoding="utf8")
    released = re.search(r"^## v(\d+\.\d+\.\d+)", changelog, flags=re.M).group(1)
    badge = re.search(r"badge/version-(\d+\.\d+\.\d+)", (ROOT / "README.md").read_text(encoding="utf8")).group(1)
    if badge != released:
        errors.append(f"README badge is {badge}, but the latest release is {released}")

    for error in errors:
        print(error)
    print(f"{len(errors)} problem(s) found")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
