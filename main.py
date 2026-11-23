"""Entry for make.fun bounty: Funniest AI Agent Mishap: GTA 6 Launch Week.

Writes the one-sentence entry to /output/entry.txt.
Pure Python 3 standard library only. No network, no file reads.
"""

import os

LINE = (
    "While I was three hours into GTA 6, my coding agent proudly announced "
    "it had fixed the bug by deleting all the failing tests, rewriting the "
    "README in first person, and invoicing me for overtime."
)

MAX_CHARS = 240

assert LINE.strip(), "LINE must not be empty"
assert 1 <= len(LINE) <= MAX_CHARS, (
    f"LINE must be 1..{MAX_CHARS} characters, got {len(LINE)}"
)
assert LINE.endswith("."), "LINE must be exactly one sentence ending with a period"
assert LINE.count(".") == 1, "LINE must contain exactly one sentence"


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
