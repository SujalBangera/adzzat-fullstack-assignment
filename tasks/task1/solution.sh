#!/bin/bash
set -e

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"

cat > "$SCRIPT_DIR/tag_utils.py" <<'PY'
import unicodedata


def normalize_tag(text):
    text = text.lower()

    text = "".join(
        char for char in text
        if not unicodedata.category(char).startswith("P")
    )

    return "-".join(text.split())
PY

echo "Reference solution applied successfully."
