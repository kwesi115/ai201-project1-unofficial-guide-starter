"""
Query interface for The Unofficial Guide (Milestone 5).

A minimal Gradio UI over generate.ask(): a question goes in, a grounded
answer and its source documents come out. Run with:

    python app/app.py
"""

import gradio as gr

from generate import ask


def handle_query(question: str):
    question = (question or "").strip()
    if not question:
        return "Please enter a question.", ""

    result = ask(question)
    sources = "\n".join(f"- {s}" for s in result["sources"]) if result["sources"] else "(none)"
    return result["answer"], sources


with gr.Blocks(title="The Unofficial Guide") as demo:
    gr.Markdown(
        "# The Unofficial Guide — AI in Higher Education\n"
        "Ask a question about student and faculty attitudes toward generative AI in higher "
        "education. Answers are grounded in a fixed set of surveys, studies, and reports — "
        "the system will say so if a question falls outside that collection."
    )
    inp = gr.Textbox(label="Your question", placeholder="e.g. Do students think using AI on assignments counts as cheating?")
    btn = gr.Button("Ask")
    answer = gr.Textbox(label="Answer", lines=8)
    sources = gr.Textbox(label="Retrieved from", lines=4)

    btn.click(handle_query, inputs=inp, outputs=[answer, sources])
    inp.submit(handle_query, inputs=inp, outputs=[answer, sources])


if __name__ == "__main__":
    demo.launch()
