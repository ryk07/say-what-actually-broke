"""Entry for make.fun: Say What Actually Broke.

Writes one original line of software error copy (at most 200 characters)
to /output/entry.txt. Pure standard library, no network, no reliance on
the working directory.
"""

import os
from pathlib import Path

LINE = (
    "Your file is safe, but the server ran out of disk \u2014 it spent "
    "the space on logs about being out of disk. Delete something and "
    "try again."
)


MAX_CHARS = 200


def main() -> None:
    line = LINE
    if not 1 <= len(line) <= MAX_CHARS:
        raise ValueError(f"entry line is {len(line)} characters, must be 1-{MAX_CHARS}")
    if len(line.encode("utf-8")) > MAX_CHARS:
        raise ValueError("entry line must fit the gate in bytes too")
    if not line.strip():
        raise ValueError("entry line must not be only whitespace")
    if line != line.strip():
        raise ValueError("entry line must not start or end with whitespace")
    if "\n" in line or "\r" in line:
        raise ValueError("entry must be a single line")
    target = Path(os.environ.get("ENTRY_OUTPUT", "/output/entry.txt"))
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(line, encoding="utf-8")


if __name__ == "__main__":
    main()
