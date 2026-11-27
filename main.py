"""One Emoji, One Dream Vacation — variant 2: the Moai of Rapa Nui.

Writes exactly one emoji to /output/entry.txt: the Moai statue.

Why this emoji: the judge rewards one specific dream over any generic
holiday. A beach or a palm says "some holiday, somewhere". The Moai says
one trip only: Easter Island, Rapa Nui, the most remote inhabited island
on Earth, giant stone heads standing watch over the Pacific at sunrise.
It is a postcard at a glance, instantly readable on any screen in any
culture, and it is a surprise next to a field full of beaches, planes
and mountains. One landmark, one promise.

It is deliberately different from variant 1 (Mount Fuji, Japan): a
different continent, a different kind of wonder, a human-made mystery
instead of a mountain, stone instead of snow.

The file holds the single emoji and nothing else: no words, no spaces,
no trailing newline, so the entry is byte-for-byte one emoji.
"""

import os
from pathlib import Path

# U+1F5FF MOYAI: one code point, four bytes in UTF-8.
EMOJI = "\U0001F5FF"

# The harness contract: the entry lives at /output/entry.txt.
# ENTRY_OUTPUT exists only so the entry can be tested locally; the
# graded run uses the default path.
OUTPUT_PATH = Path(os.environ.get("ENTRY_OUTPUT", "/output/entry.txt"))


def main() -> None:
    """Write the single dream-vacation emoji to the output file."""
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    # newline="" keeps the file to exactly the emoji: no trailing \n,
    # so the entry is one character and four bytes, the smallest an
    # astral-plane emoji can be (helps the size tie-break).
    with OUTPUT_PATH.open("w", encoding="utf-8", newline="") as handle:
        handle.write(EMOJI)


if __name__ == "__main__":
    main()
