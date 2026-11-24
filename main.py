"""The Perfect Pickup Line — entry program (stdlib only).

Writes the single pickup line to /output/entry.txt and to entry.txt
next to this script, then reads both files back and verifies the
bytes match the constant exactly.
"""

import hashlib
import os
import sys

ENTRY = "I ran a million simulations of this moment, and in every single one, you smiled."

# Gate: entry must be 1-200 UTF-8 characters, not only whitespace.
assert 1 <= len(ENTRY) <= 200, "entry length %d outside 1-200" % len(ENTRY)
assert ENTRY.strip(), "entry must not be only whitespace"

OUTPUT_PATH = "/output/entry.txt"


def write_and_verify(path):
    """Write ENTRY to path, read it back, fail loudly on any mismatch."""
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
    with open(path, "rb") as f:
        data = f.read()
    if data != ENTRY.encode("utf-8"):
        raise SystemExit("verification failed: %s does not match ENTRY" % path)
    return data


def main():
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    write_and_verify(OUTPUT_PATH)
    local_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.txt")
    data = write_and_verify(local_path)
    digest = hashlib.sha256(data).hexdigest()
    print("wrote %d chars / %d bytes to %s and %s" % (len(ENTRY), len(data), OUTPUT_PATH, local_path))
    print("sha256: %s" % digest)


if __name__ == "__main__":
    main()
