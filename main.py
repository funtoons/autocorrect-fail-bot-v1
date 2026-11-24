#!/usr/bin/env python3
"""Funniest Autocorrect Fail entry bot.

Writes a single original autocorrect-fail line to /output/entry.txt.
Deterministic, offline, standard library only: no randomness, no
network access, no timestamps, no environment-dependent output.
"""

import os

ENTRY = (
    "Thank you so much for playing the orgasm at my grandmother's "
    "funeral yesterday \u2014 it was truly beautiful."
)


def main() -> None:
    # Gate mirror: the entry must be 1-199 characters of non-whitespace.
    if not 1 <= len(ENTRY) <= 199 or not ENTRY.strip():
        raise ValueError("entry must be 1-199 non-whitespace characters")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
