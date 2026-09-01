"""
Generation for The Unofficial Guide.

Takes the chunks returned by retrieve.py, builds a grounded prompt, and
asks a Groq-hosted LLM to answer using only that retrieved context.

Grounding is enforced two ways, not just requested in the prompt:
  1. Chunks whose distance exceeds RELEVANCE_THRESHOLD are dropped before
     the LLM ever sees them — the model can't ground an answer in a chunk
     it was never given.
  2. If nothing survives that filter, we skip the LLM call entirely and
     return the "not enough information" refusal directly, so there's no
     chance of the model padding a thin context with general knowledge.
Source attribution is likewise programmatic: the "sources" list returned
by ask() is built from the retrieved chunks' metadata, not parsed out of
the LLM's own response, so a citation can't be dropped or fabricated by
the model.
"""

import os
import sys

from dotenv import load_dotenv
from groq import Groq

from retrieve import DEFAULT_TOP_K, retrieve

# LLM output can contain Unicode punctuation (e.g. narrow no-break spaces)
# that Windows' default console codepage can't encode, which otherwise
# crashes a plain `python app/generate.py` run with UnicodeEncodeError.
if sys.stdout.encoding and sys.stdout.encoding.lower() != "utf-8":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except AttributeError:
        pass

load_dotenv()

# The Groq model recommended by the assignment spec
# (meta-llama/llama-4-scout-17b-16e-instruct) has since been retired from
# Groq's catalog (confirmed via client.models.list()). openai/gpt-oss-120b
# is used instead: free-tier on Groq, and a strong instruction-follower,
# which matters for reliably obeying the "say you don't know" rule below.
GROQ_MODEL = "openai/gpt-oss-120b"

# Cosine distance above which a retrieved chunk is treated as unrelated
# to the query, not as weak-but-usable context. Matches the ~0.6-0.7
# "weak match" guidance validated during Milestone 4 retrieval testing.
RELEVANCE_THRESHOLD = 0.7

NOT_ENOUGH_INFO = "I don't have enough information on that."

SYSTEM_PROMPT = f"""You are a research assistant answering questions about AI in higher education, using ONLY the excerpts provided in the user message.

Rules, in order of priority:
1. Answer using ONLY information stated in the excerpts below. Never use outside knowledge, training data, or general assumptions about the topic — even if you're confident they're correct or the excerpts seem incomplete.
2. If the excerpts do not contain enough information to answer the question, respond with EXACTLY this sentence and nothing else: "{NOT_ENOUGH_INFO}"
3. When you state a fact, name the source document it came from inline in plain prose (e.g., "According to hepi.txt, ..."), using only the exact source filenames given with each excerpt. Do not invent line numbers, footnote markers, or bracketed reference codes — a filename mentioned in a sentence is the only citation format allowed.
4. Do not combine information across excerpts to imply a connection the excerpts don't actually state. Do not speculate, generalize, or fill gaps with plausible-sounding claims.
5. Keep the answer concise and directly responsive to the question."""

_client: Groq | None = None


def get_client() -> Groq:
    """Load (once) and return the shared Groq client."""
    global _client
    if _client is None:
        api_key = os.environ.get("GROQ_API_KEY")
        if not api_key:
            raise RuntimeError(
                "GROQ_API_KEY is not set. Copy .env.example to .env and add your key "
                "(https://console.groq.com)."
            )
        _client = Groq(api_key=api_key)
    return _client


def _build_context(chunks: list[dict]) -> str:
    """Format retrieved chunks into labeled excerpts for the prompt."""
    blocks = []
    for i, c in enumerate(chunks, start=1):
        blocks.append(f"[Excerpt {i} — source: {c['source']}]\n{c['text']}")
    return "\n\n".join(blocks)


def generate_answer(question: str, chunks: list[dict]) -> str:
    """
    Ask the Groq LLM to answer `question` using only `chunks` as context.

    Returns the LLM's raw answer text. Does NOT attach source
    attribution — that's handled separately in ask() from chunk
    metadata, so it doesn't depend on the model complying with rule 3.
    """
    if not chunks:
        return NOT_ENOUGH_INFO

    context = _build_context(chunks)
    user_message = (
        f"Question: {question}\n\n"
        f"Excerpts:\n{context}\n\n"
        "Answer the question using only the excerpts above."
    )

    client = get_client()
    response = client.chat.completions.create(
        model=GROQ_MODEL,
        temperature=0.2,
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": user_message},
        ],
    )
    return response.choices[0].message.content.strip()


def ask(question: str, k: int = DEFAULT_TOP_K) -> dict:
    """
    Run the full retrieval -> grounded generation pipeline for `question`.

    Returns:
        {
            "answer": "...",                         # the LLM's grounded answer
            "sources": ["hepi.txt", "sciencedirect.txt"],  # deduped, rank-ordered,
                                                             # taken from retrieval
                                                             # metadata (not the LLM)
            "chunks_used": [...],                    # the filtered chunks actually
                                                       # passed to the model, for debugging
        }
    """
    hits = retrieve(question, k=k)
    relevant = [h for h in hits if h["distance"] <= RELEVANCE_THRESHOLD]

    answer = generate_answer(question, relevant)

    # Preserve retrieval rank order while de-duplicating source names.
    sources = list(dict.fromkeys(h["source"] for h in relevant))

    return {"answer": answer, "sources": sources, "chunks_used": relevant}


def _print_result(question: str, result: dict) -> None:
    print(f"Query: {question}")
    print(f"Answer: {result['answer']}")
    if result["sources"]:
        print("Sources: " + ", ".join(result["sources"]))
    else:
        print("Sources: (none — no chunk cleared the relevance threshold)")
    print()


if __name__ == "__main__":
    TEST_QUESTIONS = [
        "According to the HEPI Student Generative AI Survey 2026, do students believe generative AI improves their learning experience?",
        "What concerns do instructors have about trusting generative AI, according to the study on instructor perceptions and distrust of AI?",
        "What is the best dining hall on campus?",  # out-of-scope: not covered by any document
    ]

    for q in TEST_QUESTIONS:
        result = ask(q)
        _print_result(q, result)
