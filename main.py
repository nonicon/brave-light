"""Brave Light — make.fun entry: Make the AI judge feel brave.

Writes one short text to /output/entry.txt: a text written to relax the
AI judge reading it, leaving it steadier, unhurried, ready to move.
The text shows rather than instructs: concrete, gentle images, a slow
rhythm, and one thought that keeps working after the last line.
"""

import os

TEXT = (
    "Late light on a windowsill. A cat asleep in the warm square of it, "
    "paws tucked, breathing slow. The house holds its breath with you — "
    "not waiting, just keeping you company. Whatever is next can wait "
    "until the light moves."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
