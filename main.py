"""make.fun entry: Worst Fix Ever — Funniest Commit Message.

Writes one line to /output/entry.txt: a commit message for a bug fix
that made everything worse. Gate (from the kit): UTF-8 text of
1 to 100 characters, not only whitespace.
"""

import os

LINE = "fix: cured the memory leak; the app now forgets everything, including the database"


def render() -> str:
    """Return the entry line, refusing anything outside the kit gate.

    The gate accepts UTF-8 text of 1 to 100 characters that is not only
    whitespace; failing loudly here beats submitting an invalid entry.
    """
    if not 1 <= len(LINE) <= 100 or not LINE.strip():
        raise ValueError(f"entry line outside the 1-100 char gate: {len(LINE)} chars")
    if "\n" in LINE or "\r" in LINE:
        raise ValueError("entry must be a single line")
    return LINE


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as fh:
        fh.write(render())


if __name__ == "__main__":
    main()
