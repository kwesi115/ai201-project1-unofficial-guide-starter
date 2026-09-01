"""
Milestone 3 entry point: Document Ingestion + Chunking.

Run with:  python app/main.py

This only exercises the first two pipeline stages (Document Ingestion
and Chunking). Embedding, vector storage, retrieval, and generation
are implemented in later milestones.
"""

from chunk import CHUNK_OVERLAP, CHUNK_SIZE, chunk_documents
from ingest import load_documents


def main():
    # 1 & 7. Load all .txt files from documents/, print how many loaded.
    docs = load_documents()
    print(f"Total documents loaded: {len(docs)}\n")

    # 4. Print one cleaned document so it can be inspected before chunking.
    if docs:
        sample_doc = docs[0]
        print(f"--- Cleaned document preview: {sample_doc['source']} ---")
        print(sample_doc["text"][:1000])
        print("--- end preview ---\n")

    # 5 & 6. Chunk every document into ~500-token chunks with 100-token
    # overlap, each chunk tagged with its source filename.
    chunks = chunk_documents(docs, chunk_size=CHUNK_SIZE, overlap=CHUNK_OVERLAP)

    # 8. Print the total number of chunks created.
    print(f"Total chunks created: {len(chunks)} (chunk_size={CHUNK_SIZE}, overlap={CHUNK_OVERLAP})\n")

    # 9. Print 5 representative chunks, spread across the collection,
    # clearly labeled with their source document.
    print("--- 5 representative chunks ---\n")
    step = max(1, len(chunks) // 5)
    sample_indices = [i * step for i in range(5) if i * step < len(chunks)]
    for idx in sample_indices:
        c = chunks[idx]
        print(f"[Chunk {idx}]  Source: {c['source']}  |  chunk_id: {c['chunk_id']}  |  tokens: {c['token_count']}")
        print(c["text"][:400].replace("\n", " "))
        print("...\n")


if __name__ == "__main__":
    main()
