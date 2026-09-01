"""
Embedding + Vector Store for The Unofficial Guide.

Takes the chunks produced by ingest.py + chunk.py, embeds them with
all-MiniLM-L6-v2 (sentence-transformers), and stores them in a
persistent ChromaDB collection along with source metadata.

This is a "build the index" script — run it once (or whenever your
documents/ folder or chunking strategy changes) to (re)populate the
vector store. Milestone 5's retrieval/generation code just queries
the collection this script builds; it doesn't re-embed anything.
"""

from pathlib import Path

import chromadb
from sentence_transformers import SentenceTransformer

EMBEDDING_MODEL_NAME = "all-MiniLM-L6-v2"
COLLECTION_NAME = "unofficial_guide_chunks"

_PROJECT_ROOT = Path(__file__).resolve().parent.parent
PERSIST_DIR = str(_PROJECT_ROOT / "chroma_db")

# Loaded lazily so importing this module doesn't immediately pull the
# model into memory (useful when retrieve.py just wants to query an
# already-built collection).
_model: SentenceTransformer | None = None


def get_embedding_model() -> SentenceTransformer:
    """Load (once) and return the shared all-MiniLM-L6-v2 model."""
    global _model
    if _model is None:
        _model = SentenceTransformer(EMBEDDING_MODEL_NAME)
    return _model


def embed_texts(texts: list[str]) -> list[list[float]]:
    """Embed a list of strings into a list of 384-dim vectors (as plain lists)."""
    model = get_embedding_model()
    embeddings = model.encode(texts, show_progress_bar=len(texts) > 20, convert_to_numpy=True)
    return embeddings.tolist()


def get_chroma_client(persist_dir: str = PERSIST_DIR) -> chromadb.ClientAPI:
    """Return a ChromaDB client backed by on-disk storage at `persist_dir`."""
    return chromadb.PersistentClient(path=persist_dir)


def build_vector_store(
    chunks: list[dict],
    persist_dir: str = PERSIST_DIR,
    collection_name: str = COLLECTION_NAME,
    reset: bool = True,
) -> chromadb.Collection:
    """
    Embed every chunk and store it in a ChromaDB collection.

    Each chunk (as produced by chunk.chunk_documents) becomes one
    entry in the collection:
        - id:        "{source}::chunk-{chunk_id}"   (stable, unique)
        - embedding: the all-MiniLM-L6-v2 vector for chunk["text"]
        - document:  chunk["text"]  (Chroma stores the raw text too,
                                      so retrieval can return it directly)
        - metadata:  {"source": ..., "chunk_id": ..., "token_count": ...}

    `reset=True` (default) drops any existing collection of the same
    name first, so re-running this script doesn't create duplicate or
    stale entries after you've changed your chunking strategy.
    """
    client = get_chroma_client(persist_dir)

    if reset:
        try:
            client.delete_collection(collection_name)
        except Exception:
            pass  # collection didn't exist yet — nothing to delete

    # "hnsw:space": "cosine" tells Chroma's HNSW index to rank results
    # by cosine distance instead of its default squared-L2 distance.
    # sentence-transformers models (including all-MiniLM-L6-v2) are
    # trained/evaluated using cosine similarity, so this keeps the
    # distance scores meaningful for this embedding model.
    collection = client.get_or_create_collection(
        name=collection_name,
        metadata={"hnsw:space": "cosine"},
    )

    ids = [f"{c['source']}::chunk-{c['chunk_id']}" for c in chunks]
    documents = [c["text"] for c in chunks]
    metadatas = [
        {"source": c["source"], "chunk_id": c["chunk_id"], "token_count": c["token_count"]}
        for c in chunks
    ]

    print(f"Embedding {len(documents)} chunks with {EMBEDDING_MODEL_NAME}...")
    embeddings = embed_texts(documents)

    # Add in batches so this doesn't choke if the corpus grows well
    # past what a single collection.add() call comfortably handles.
    BATCH_SIZE = 100
    for start in range(0, len(ids), BATCH_SIZE):
        end = start + BATCH_SIZE
        collection.add(
            ids=ids[start:end],
            embeddings=embeddings[start:end],
            documents=documents[start:end],
            metadatas=metadatas[start:end],
        )

    return collection


if __name__ == "__main__":
    from chunk import CHUNK_OVERLAP, CHUNK_SIZE, chunk_documents
    from ingest import load_documents

    docs = load_documents()
    print(f"Loaded {len(docs)} documents.")

    chunks = chunk_documents(docs, chunk_size=CHUNK_SIZE, overlap=CHUNK_OVERLAP)
    print(f"Created {len(chunks)} chunks.")

    collection = build_vector_store(chunks)
    print(f"\nVector store ready: '{COLLECTION_NAME}' at {PERSIST_DIR}")
    print(f"Collection now contains {collection.count()} embedded chunks.")
