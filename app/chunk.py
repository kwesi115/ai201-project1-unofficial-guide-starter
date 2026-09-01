"""
Chunking for The Unofficial Guide.

Splits cleaned documents into ~500-token chunks with 100-token
overlap, per planning.md's Chunking Strategy. Does NOT embed,
store, or retrieve chunks — see ingest.py for the previous stage.
"""

import tiktoken

CHUNK_SIZE = 500
CHUNK_OVERLAP = 100

# cl100k_base is a general-purpose tokenizer (used by GPT-3.5/4).
# We use it purely to get a consistent, reproducible token count for
# sizing chunks — it doesn't need to match whatever tokenizer the
# embedding model uses later, since "~500 tokens" is an approximation
# by design (per planning.md).
_ENCODING = tiktoken.get_encoding("cl100k_base")


def count_tokens(text: str) -> int:
    """Return the token count of `text` using the cl100k_base tokenizer."""
    return len(_ENCODING.encode(text))


def chunk_text(text: str, chunk_size: int = CHUNK_SIZE, overlap: int = CHUNK_OVERLAP) -> list[str]:
    """
    Split `text` into a list of overlapping chunks of ~chunk_size tokens.

    Works by encoding the whole document to token ids once, then
    sliding a window of `chunk_size` tokens across it, moving forward
    by (chunk_size - overlap) tokens each step, and decoding each
    window back to text. This guarantees every chunk (except possibly
    the last) is exactly `chunk_size` tokens, and consecutive chunks
    share `overlap` tokens of context.

    Returns an empty list for empty input.
    """
    if overlap >= chunk_size:
        raise ValueError("overlap must be smaller than chunk_size")

    token_ids = _ENCODING.encode(text)
    if not token_ids:
        return []

    stride = chunk_size - overlap
    chunks = []

    start = 0
    while start < len(token_ids):
        window = token_ids[start : start + chunk_size]
        chunks.append(_ENCODING.decode(window))

        if start + chunk_size >= len(token_ids):
            break
        start += stride

    return chunks


def chunk_documents(
    documents: list[dict], chunk_size: int = CHUNK_SIZE, overlap: int = CHUNK_OVERLAP
) -> list[dict]:
    """
    Chunk every document in `documents` (as produced by ingest.load_documents).

    Returns a flat list of chunk dicts, each carrying its source
    document's filename as metadata:
        {
            "source": "hepi.txt",   # which document this chunk came from
            "chunk_id": 3,          # this chunk's index within that document
            "text": "...",          # the chunk's text
            "token_count": 500,     # actual token count of this chunk
        }
    """
    all_chunks = []

    for doc in documents:
        pieces = chunk_text(doc["text"], chunk_size=chunk_size, overlap=overlap)
        for i, piece in enumerate(pieces):
            all_chunks.append(
                {
                    "source": doc["source"],
                    "chunk_id": i,
                    "text": piece,
                    "token_count": count_tokens(piece),
                }
            )

    return all_chunks


if __name__ == "__main__":
    from ingest import load_documents

    docs = load_documents()
    chunks = chunk_documents(docs)

    print(f"Loaded {len(docs)} documents.")
    print(f"Created {len(chunks)} chunks (chunk_size={CHUNK_SIZE}, overlap={CHUNK_OVERLAP}).\n")

    print("--- 5 representative chunks ---\n")
    if chunks:
        step = max(1, len(chunks) // 5)
        sample_indices = [i * step for i in range(5) if i * step < len(chunks)]
        for idx in sample_indices:
            c = chunks[idx]
            print(f"[chunk {idx}] source={c['source']} | chunk_id={c['chunk_id']} | tokens={c['token_count']}")
            print(c["text"][:400].replace("\n", " "))
            print("...\n")
