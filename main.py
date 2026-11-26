#!/usr/bin/env python3
"""One-Line Office Joke Laugh-Off — entry writer.

Writes one original one-line office joke to /output/entry.txt
(the grader's artifact path), falling back to ./output/entry.txt
when /output is not present (local runs).

Deterministic: the same joke text is written on every run.
"""

import os

JOKE = (
    "Our company loves transparency: everyone's salary is a secret, "
    "the org chart is a rumor, and the layoffs are a surprise party."
)


def main() -> None:
    # Self-check gate: mirrors the sealed scorer's gate so a bad entry
    # fails loudly here instead of silently at grading time.
    # These asserts never change the output text.
    assert 1 <= len(JOKE) <= 200, f"entry must be 1-200 chars, got {len(JOKE)}"
    assert JOKE.strip(), "entry must not be only white space"
    assert "\n" not in JOKE and "\r" not in JOKE, "entry must be a single line"
    assert JOKE == JOKE.strip(), "entry must not start or end with white space"

    out_dir = "/output" if os.path.isdir("/output") else os.path.join(os.getcwd(), "output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(JOKE)
    # Verify what was actually written, byte for byte.
    with open(path, "r", encoding="utf-8", newline="") as f:
        written = f.read()
    assert written == JOKE, "written entry differs from JOKE"
    assert 1 <= len(written) <= 200, "written entry fails the 1-200 char gate"
    print(f"wrote {path} ({len(JOKE)} chars)")


if __name__ == "__main__":
    main()
