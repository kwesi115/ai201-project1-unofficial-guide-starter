"""
Retrieval for The Unofficial Guide.

Queries the ChromaDB collection built by embed.py: embeds the query
string with the same all-MiniLM-L6-v2 model, and returns the top-k
most similar chunks with their source metadata and distance scores.

Run this file directly to test retrieval against the evaluation
questions from planning.md, before wiring in generation (Milestone 5).
"""

from embed import COLLECTION_NAME, PERSIST_DIR, embed_texts, get_chroma_client

DEFAULT_TOP_K = 5

# From planning.md's Evaluation Plan.
EVAL_QUESTIONS = [
    "According to the HEPI Student Generative AI Survey 2026, do students believe generative AI improves their learning experience?",
    "What concerns do instructors have about trusting generative AI, according to the study on instructor perceptions and distrust of AI?",
    "How do students and faculty differ in their perceptions of generative AI in university courses?",
    "What do students think about using generative AI for academic work, including concerns about cheating and academic integrity?",
    "According to the Oregon State University survey, how do online students and faculty differ in their perceptions of generative AI?",
]


def get_collection(persist_dir: str = PERSIST_DIR, collection_name: str = COLLECTION_NAME):
    """
    Open the existing ChromaDB collection built by embed.py.

    Raises if the collection doesn't exist yet — run `python embed.py`
    first to build the index.
    """
    client = get_chroma_client(persist_dir)
    return client.get_collection(collection_name)


def retrieve(
    query: str,
    k: int = DEFAULT_TOP_K,
    persist_dir: str = PERSIST_DIR,
    collection_name: str = COLLECTION_NAME,
) -> list[dict]:
    """
    Return the top-k chunks most relevant to `query`.

    Each result dict has:
        {
            "text": "...",          # the chunk's text
            "source": "hepi.txt",   # which document it came from
            "chunk_id": 3,          # its position within that document
            "distance": 0.42,       # cosine distance (0 = identical, 2 = opposite)
        }

    Results are already ordered by relevance (closest/most similar first)
    since collection.query() returns matches sorted by ascending distance.
    """
    collection = get_collection(persist_dir, collection_name)

    # Embed the query with the SAME model used to embed the chunks —
    # queries and documents must live in the same vector space for
    # the distance comparison to mean anything.
    query_embedding = embed_texts([query])[0]

    # n_results=k asks Chroma's HNSW index for the k nearest neighbors
    # to query_embedding. Chroma returns parallel lists (ids, documents,
    # metadatas, distances), each wrapped one level deeper because
    # collection.query() supports batching multiple queries at once —
    # we only send one query, so everything we want is at index [0].
    results = collection.query(query_embeddings=[query_embedding], n_results=k)

    hits = []
    for text, metadata, distance in zip(
        results["documents"][0], results["metadatas"][0], results["distances"][0]
    ):
        hits.append(
            {
                "text": text,
                "source": metadata["source"],
                "chunk_id": metadata["chunk_id"],
                "distance": distance,
            }
        )
    return hits


def _print_hits(hits: list[dict]) -> None:
    for rank, hit in enumerate(hits, start=1):
        print(f"  [{rank}] source={hit['source']} chunk_id={hit['chunk_id']} distance={hit['distance']:.4f}")
        preview = hit["text"][:300].replace("\n", " ")
        print(f"      {preview}...")


if __name__ == "__main__":
    print(f"Querying collection '{COLLECTION_NAME}' at {PERSIST_DIR}\n")

    for question in EVAL_QUESTIONS:
        print(f"Query: {question}")
        hits = retrieve(question, k=DEFAULT_TOP_K)
        _print_hits(hits)
        print()
