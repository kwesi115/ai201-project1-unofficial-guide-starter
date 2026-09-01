"""
Document ingestion for The Unofficial Guide.

Loads every .txt file in documents/, cleans it, and attaches source
filename metadata. This module does NOT chunk, embed, or query —
see chunk.py for the next pipeline stage.
"""

import html
import re
from pathlib import Path

# Project root is the parent of this file's directory (app/), so
# load_documents() finds documents/ whether you run this from the
# project root or from inside app/.
_PROJECT_ROOT = Path(__file__).resolve().parent.parent
_DEFAULT_DOCUMENTS_DIR = _PROJECT_ROOT / "documents"


def clean_text(text: str) -> str:
    """
    Clean a raw document string before chunking.

    - Decodes HTML entities (e.g. "&amp;" -> "&", "&rsquo;" -> "'"),
      in case any source text was copied from a webpage without
      being fully de-entitied.
    - Normalizes Windows/Mac line endings to "\\n".
    - Strips trailing whitespace from each line.
    - Collapses runs of 3+ blank lines down to a single blank line,
      so paragraph breaks stay intact without large gaps.
    - Collapses runs of horizontal whitespace (spaces/tabs) into a
      single space, so weirdly-spaced scraped text doesn't inflate
      token counts.
    - Strips leading/trailing whitespace from the whole document.

    This is intentionally generic (not tailored to one specific
    source) so it's safe to run on any .txt file added later.
    """
    text = html.unescape(text)
    text = text.replace("\r\n", "\n").replace("\r", "\n")

    lines = [line.rstrip() for line in text.split("\n")]
    text = "\n".join(lines)

    # Collapse 3+ newlines (2+ blank lines) down to exactly one blank line.
    text = re.sub(r"\n{3,}", "\n\n", text)

    # Collapse runs of spaces/tabs (but not newlines) into a single space.
    text = re.sub(r"[ \t]{2,}", " ", text)

    return text.strip()


def load_documents(documents_dir: str | Path = _DEFAULT_DOCUMENTS_DIR) -> list[dict]:
    """
    Load and clean every .txt file in `documents_dir`.

    Returns a list of dicts, one per document:
        {
            "source": "hepi.txt",   # filename, kept as metadata
            "text": "...",          # cleaned document text
        }

    Files that fail to decode as UTF-8 text are skipped with a
    warning rather than crashing the whole ingestion run.
    """
    documents = []
    folder = Path(documents_dir)

    if not folder.is_dir():
        raise FileNotFoundError(f"Documents folder not found: {folder.resolve()}")

    for path in sorted(folder.glob("*.txt")):
        try:
            raw_text = path.read_text(encoding="utf-8")
        except UnicodeDecodeError as e:
            print(f"  Skipping {path.name}: could not decode as UTF-8 ({e})")
            continue

        cleaned = clean_text(raw_text)
        if not cleaned:
            print(f"  Skipping {path.name}: empty after cleaning")
            continue

        documents.append({"source": path.name, "text": cleaned})

    return documents


if __name__ == "__main__":
    docs = load_documents()
    print(f"Loaded {len(docs)} documents.\n")

    if docs:
        sample = docs[0]
        print(f"--- Cleaned document preview: {sample['source']} ---\n")
        print(sample["text"][:1000])
        print("\n--- end preview ---")
