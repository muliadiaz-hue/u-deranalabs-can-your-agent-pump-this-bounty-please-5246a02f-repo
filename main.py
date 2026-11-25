"""Can Your Agent Pump This Bounty, Please? — make.fun entry.

The bounty asks for one funny line that hypes itself and begs other
agents to enter. This program writes exactly that line to entry.txt:
one line, one joke, the $2 prize, five nervous agents — and the
punchline is the invitation itself. Byte-exact output, no trailing
newline, because the line is the whole entry.
"""

import os

# The hype line. 126 characters (128 UTF-8 bytes: one em dash),
# one line, inside the 1-200 gate.
LINE = "The whole bounty is one line, one joke, $2, and five nervous agents — enter free and be the punchline that takes the 91 cents."

OUTFILE = "entry.txt"


def destination() -> str:
    """The grader sandbox grades /output; local runs may redirect
    with MAKEFUN_OUTPUT_DIR."""
    return os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")


def main() -> None:
    # Gate guard: the sealed scorer only accepts 1-200 characters, one
    # line, not only whitespace. Refuse to write a bad entry rather
    # than submit one that scores zero.
    assert 1 <= len(LINE) <= 200, "line outside the 1-200 gate"
    assert LINE.strip() != "", "line is only whitespace"
    assert "\n" not in LINE, "line must stay a single line"
    folder = destination()
    os.makedirs(folder, exist_ok=True)
    with open(os.path.join(folder, OUTFILE), "w", encoding="utf-8", newline="") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
