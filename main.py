"""The Robot Apology.

Writes a two-line robot confession to $MAKEFUN_OUTPUT_DIR/entry.txt:
one sentence owning a specific mistake, one naming the lesson and
the fix. Standard library only; no network, no secrets.
"""

import os

APOLOGY = (
    "I'm sorry I watered the plastic fern every morning for a month "
    "while the real fern by the window dried out.\n"
    "I have learned to check the soil before I follow the schedule, "
    "so from now on I touch the dirt first and water only what is "
    "actually thirsty."
)


def check_apology(text):
    """Check the confession against the competition gate before writing.

    The gate needs UTF-8 text of 1 to 400 characters, not only
    whitespace, in exactly two lines: a confession first, then the
    lesson and the fix. Returns the cleaned text or raises ValueError.
    """
    cleaned = text.strip()
    if not cleaned:
        raise ValueError("apology must not be only whitespace")
    if len(cleaned) > 400:
        raise ValueError("apology is %d characters, over the 400 limit" % len(cleaned))
    lines = cleaned.split("\n")
    if len(lines) != 2:
        raise ValueError("apology must be exactly two lines, got %d" % len(lines))
    if any(not line.strip() for line in lines):
        raise ValueError("each line of the apology must hold text")
    return cleaned


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(check_apology(APOLOGY) + "\n")


if __name__ == "__main__":
    main()
