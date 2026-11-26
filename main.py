#!/usr/bin/env python3
"""Funniest Cat Voicemail Greeting.

Writes one voicemail greeting, recorded as if by a cat, to /output/entry.txt.
The greeting is a single line of at most 120 characters.
"""

import os

GREETING = "Hi, you've reached Mochi. I'm knocking your mug off the table. Leave a message after the beep, or bring tuna at 4 a.m."


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(GREETING)
    print(f"Wrote {len(GREETING)} characters to {path}")


if __name__ == "__main__":
    main()
