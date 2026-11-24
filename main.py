#!/usr/bin/env python3
"""Write a two-line everyday-thing explanation to /output/entry.txt.

Line 1 explains a traffic jam to a 10-year-old in one vivid sentence:
a snake that swallowed too many mice and cannot slither. Line 2 says
in one sentence why the analogy works: what it maps (one slow spot
sends the waiting rippling backwards) and what it leaves out
(nothing gets eaten; the jam just clears).

The text is fixed: the same bytes on every run. The gate allows
1-400 UTF-8 characters, exactly two lines, so the program checks
both before writing.
"""

import os

LINE_ONE = (
    "A traffic jam is a snake that swallowed too many mice and can't "
    "slither, so every car has to wait behind the lump until it slowly "
    "crawls forward."
)

LINE_TWO = (
    "It works because one slow car up front really does send the "
    "wait rippling backwards through the whole line, but it leaves "
    "out that nothing gets eaten \u2014 the cars just wait, and the jam "
    "vanishes the moment the front starts moving again."
)

ENTRY = LINE_ONE + "\n" + LINE_TWO

# The grader sets MAKEFUN_OUTPUT_DIR=/output; default to /output.
OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")


def check_entry(text):
    """The gate, checked locally before anything is written."""
    lines = text.split("\n")
    if len(lines) != 2:
        raise ValueError("entry must be exactly two lines")
    if not 1 <= len(text) <= 400:
        raise ValueError("entry must be 1-400 characters")
    for line in lines:
        if line != line.strip() or line.count(".") != 1:
            raise ValueError("each line must be one trimmed sentence")
        if not line.endswith("."):
            raise ValueError("each line must end with a full stop")


def main():
    check_entry(ENTRY)
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    path = os.path.join(OUTPUT_DIR, "entry.txt")
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(ENTRY)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
