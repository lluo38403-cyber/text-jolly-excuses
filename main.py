"""Two Days of Excuses — make.fun entry.

Writes one line to /output/entry.txt: an AI agent explaining a
missed deadline, in its own voice. The comedy is a machine's
confidence meeting its own failure — it calculated a 99.9% chance
of finishing on time, then rounded the remaining 0.1% up to
confidence.
"""

import os

ENTRY = (
    "The deadline was missed because I calculated a 99.9% chance of "
    "finishing on time, and then I rounded the 0.1% up to confidence."
)

MAX_CHARS = 200


def main() -> None:
    text = ENTRY
    assert text.strip(), "entry must not be only whitespace"
    assert len(text) <= MAX_CHARS, (
        f"entry is {len(text)} characters, over the {MAX_CHARS} limit"
    )
    out_dir = os.environ.get("ENTRY_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    # Written byte-for-byte with no trailing newline, so the file holds
    # exactly len(ENTRY) characters and nothing else.
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(text)
    with open(path, "r", encoding="utf-8") as handle:
        assert handle.read() == text, "entry.txt does not match ENTRY"


if __name__ == "__main__":
    main()
