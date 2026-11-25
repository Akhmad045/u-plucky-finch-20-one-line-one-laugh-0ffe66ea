"""One Line, One Laugh - entry program.

Writes a single funny line of text to /output/entry.txt.
The line: I asked my smart speaker to play something relaxing, and it read
out my credit card balance.
"""

import os

LINE = ("I asked my smart speaker to play something relaxing, and it read "
        "out my credit card balance.")


def main() -> None:
    line = LINE.strip()
    if not line or len(line) > 200:
        raise ValueError("entry must be 1-200 characters")
    if line != line.strip():
        raise ValueError("entry must not start or end with whitespace")
    if "\n" in line or "\r" in line:
        raise ValueError("entry must be a single line")
    if not line.endswith("."):
        raise ValueError("entry must end with a full stop")
    out_path = "/output/entry.txt"
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(line)
    # Self-verify: the file the grader reads must be byte-exact.
    with open(out_path, "rb") as f:
        written = f.read()
    if written != line.encode("utf-8"):
        raise ValueError("entry.txt does not match the line byte for byte")


if __name__ == "__main__":
    main()
