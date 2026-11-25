#!/usr/bin/env python3
"""Make the AI Judge Laugh — one office-life joke, one line.

Writes a single original joke about office life to /output/entry.txt.
Deterministic: stdlib only, no network, no randomness, no input.
"""

import os

# v2 (revised): tightened the setup — "My review said" drops the filler
# word "performance" — and sharpened the turn: instead of merely standing
# in doorways, he now does ALL his work there, committing to the literal
# reading of "be more visible". Shorter, punchier, same joke, harder turn.
JOKE = (
    "My review said I need to be more visible at work, "
    "so now I do all my work standing silently in doorways."
)


def main() -> None:
    text = JOKE.strip()
    assert 1 <= len(text) <= 200, "entry must be 1-200 characters"
    assert text.strip(), "entry must not be only whitespace"
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    with open(os.path.join(output_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
