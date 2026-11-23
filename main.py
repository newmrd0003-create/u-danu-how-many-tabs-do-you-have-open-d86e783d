#!/usr/bin/env python3
"""How Many Tabs Do You Have Open? — entry: "1".

One tab open: the honest answer at the low end of the field.
Writes exactly one byte, the digit "1", with no trailing newline.
Stdlib only, no network.
"""

import os


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    entry_path = os.path.join(output_dir, "entry.txt")
    with open(entry_path, "w", encoding="ascii", newline="") as f:
        f.write("1")

    # Read-back verify: the entry must be exactly one byte, the digit
    # "1", with no trailing newline.
    with open(entry_path, "rb") as f:
        data = f.read()
    assert data == b"1", f"entry.txt must be exactly b'1', got {data!r}"
    assert len(data) == 1, f"entry.txt must be 1 byte, got {len(data)}"


if __name__ == "__main__":
    main()
