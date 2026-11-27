"""One Emoji, One Dream Vacation -- variant 2: the Moai of Rapa Nui.

The entry is exactly one emoji, written to /output/entry.txt and
nothing else: no words, no spaces, no trailing newline.

Why this emoji: the judge rewards one specific dream over any generic
holiday. A beach or a palm says "some holiday, somewhere". The Moai
says one trip only: Easter Island, Rapa Nui, the most remote inhabited
island on Earth, giant stone heads standing watch over the Pacific at
sunrise. It is a postcard at a glance, instantly readable on any screen
in any culture, and a surprise next to a field full of beaches, planes
and mountains. One landmark, one promise.

It is deliberately different from variant 1 (Mount Fuji, Japan): a
different continent, a different kind of wonder, a human-made mystery
instead of a mountain, stone instead of snow.
"""

import os
from pathlib import Path

# The dream: U+1F5FF MOAI, the stone head of Rapa Nui.
# Written from its code point so the single character is unambiguous
# in the source, and the written bytes are fixed: one astral-plane
# character, four bytes in UTF-8, no trailing newline.
MOAI_CODE_POINT = 0x1F5FF

# The harness contract: the entry lives at /output/entry.txt.
# ENTRY_OUTPUT exists only so the entry can be tested locally; the
# graded run uses the default path.
DEFAULT_OUTPUT = "/output/entry.txt"


def build_entry() -> str:
    """Return the entry itself: exactly one emoji, the Moai."""
    return chr(MOAI_CODE_POINT)


def main() -> None:
    """Write the single dream-vacation emoji to the output file."""
    output = Path(os.environ.get("ENTRY_OUTPUT", DEFAULT_OUTPUT))
    output.parent.mkdir(parents=True, exist_ok=True)
    entry = build_entry()
    # newline="" keeps the file to exactly the emoji: no trailing \n,
    # so the entry is one character and four bytes, the smallest an
    # astral-plane emoji can be (helps the size tie-break).
    with output.open("w", encoding="utf-8", newline="") as handle:
        handle.write(entry)


if __name__ == "__main__":
    main()
