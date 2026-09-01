# The Unofficial Guide — Project 1

> **How to use this template:**
> Complete each section *after* you've built and tested the corresponding part of your system.
> Do not write placeholder text — if a section isn't done yet, leave it blank and come back.
> Every section below is required for submission. One-liners will not receive full credit.

---

## Domain

<!-- What topic or category of knowledge does your system cover?
     Why is this knowledge valuable, and why is it hard to find through official channels?
     Example: "Student reviews of CS professors at [university] — useful because official
     course descriptions don't reflect teaching style, exam difficulty, or workload." -->

---

## Document Sources

<!-- List every source you collected documents from.
     Be specific: include URLs, subreddit names, forum thread titles, or file names.
     Aim for variety — sources that together cover different subtopics or perspectives. -->

| # | Source | Type | URL or file path |
|---|--------|------|-----------------|
| 1 | | | |
| 2 | | | |
| 3 | | | |
| 4 | | | |
| 5 | | | |
| 6 | | | |
| 7 | | | |
| 8 | | | |
| 9 | | | |
| 10 | | | |

---

## Chunking Strategy

<!-- Describe your chunking approach with enough specificity that someone else could reproduce it.
     Include:
     - Chunk size (characters or tokens) and why that size fits your documents
     - Overlap size and why (or why not) you used overlap
     - Any preprocessing you did before chunking (e.g., stripping HTML, removing headers)
     - What your final chunk count was across all documents -->

**Chunk size:**

**Overlap:**

**Why these choices fit your documents:**

**Final chunk count:**

---

## Sample Chunks

<!-- Paste 5 representative chunks from your document collection after running your ingestion pipeline.
     For each chunk, note which source document it came from.
     These must be actual text — not screenshots. -->

All 152 chunks were inspected programmatically for empty strings, leftover HTML tags, and encoding artifacts — none were found (`chunk.py` and `ingest.py` produced clean output). The 5 chunks below are the `chunk_id: 0` chunk (the document's opening section) from 5 different source documents, chosen because a token-window chunk that starts mid-document also starts mid-sentence — these are the most naturally self-contained samples the pipeline produces.

### Chunk 1 — AI use is now "near universal" among undergraduates

**Source document:** `hepi.txt` (chunk_id 0, 500 tokens)

```text
# AI Use Is Now "Near Universal" Among Undergraduates, but Students Are Divided on Its Impact

**Source:** Higher Education Policy Institute (HEPI)

In just three years, generative AI has moved from novelty to near universality among undergraduates. The question is no longer whether students use AI, but how well they use it – and how effectively institutions are supporting them to develop the skills to do so responsibly.

The Student Generative AI Survey 2026 (HEPI Report 199), published by HEPI and sponsored by Kortext, shows a striking contrast in students' experiences. For some, AI frees up time for deeper learning and critical thinking. For others, it risks becoming a crutch. Higher education providers have a crucial role in ensuring AI enhances learning rather than diminishing it.

Co-authored by Rose Stephenson, HEPI's Director of Policy and Strategy, and Charlotte Armstrong, HEPI's Policy Manager, the survey was conducted by Savanta in December 2025 and is based on responses from 1,054 full-time UK undergraduates.

This third iteration of the report shows that students have embraced generative AI at an extraordinary speed. The UK has set out a clear ambition to be a global leader in the development and application of AI technologies, and students are already living that ambition in their day-to-day learning. However, what the survey also highlights is that institutional adoption is lagging behind student behaviour. While nearly all students use AI to support their studies, only 36% feel encouraged by their institution to do so, and only 38% say they are provided with AI tools.

## Key Findings

- **AI use is now almost universal.** Some 95% of students report using AI in at least one way and 94% say they use generative AI to help with assessed work. Many of these students will be encouraged or required to use AI in assessments as providers pivot to teaching and assessing AI skills. However, the proportion of students directly including AI-generated text in assessed work has risen to 12%, up from 8% in 2025 and 3% in 2024.
- **Assessment has changed substantially.** Nearly two-thirds (65%) of students say assessment has changed significantly in response to AI. In addition, some students articulate a sense of anxiety about false accusations of misconduct.
- **AI improves the student experience for many – but not all.** Almost half (49%) of students
```

---

### Chunk 2 — Students underreport their own AI use (social desirability bias)

**Source document:** `uchicago.txt` (chunk_id 0, 500 tokens)

```text
# Study Finds Students Underreport Their Own AI Use Due to Social Desirability Bias

**Source:** University of Chicago, Department of Computer Science

In today's day and age, the use of AI has almost become ubiquitous across many different fields and platforms. It has evolved so quickly that many institutions, whether for work or education, are still learning how to deal with it. In universities and education-based settings, for example, many teachers have adopted their own approach, with some people permitting AI with citations, and others outright banning it. With all this discourse, studies on the social impacts of AI adoption are necessary and contribute to the broader conversation around AI usage in educational settings.

Alex Kale, Assistant Professor at the University of Chicago Department of Computer Science, recently published a paper titled "Underreporting of AI Use: The Role of Social Desirability Bias" alongside coauthors Yier Ling (PhD student in the Department of Economics) and Alex Imas (Professor at Booth School of Business). Making its debut at the leading human computer interaction conference, CHI 2026, the paper sought to understand the social impacts of AI adoption, and furthermore, whether social desirability bias plays a role in discussions and environments fostering AI use. Social desirability bias is a phenomenon where people self-report their behavior in a way that would be viewed more favorably by an outside party, because even when anonymized, people generally don't want to admit to something that would be viewed as unfavorable.

"I was fascinated by this topic because the problem is really important right now," Kale stated. "A lot of educational institutions are thinking about the use of AI in schools and classrooms, and how it changes learning and the environment. This was a project that was really trying to look directly at the underappreciated social impacts of AI adoption, and a broader conversation around the way that people view their own AI usage and the AI usage of their peers."

## Survey Design and Key Findings

To mitigate potential self-reporting bias in these surveys, the authors approached this survey using both direct and indirect questioning: the same set of questions are asked to students but framed slightly differently. One question may be asked directly, "how frequently do you use AI?" while the other asks indirectly, "how frequently do your peers use AI?" Interestingly, when asked these sets of questions, respondents describe a large discrepancy between their own AI use versus that of their peers: approximately 60% of students reported that they
```

---

### Chunk 3 — AI and student well-being (mini-review abstract)

**Source document:** `nlm.txt` (chunk_id 0, 500 tokens)

```text
# The Impact of Artificial Intelligence on Student Well-Being in Higher Education: A Mini-Review

**Source:** National Library of Medicine (NLM/PubMed Central)

**Keywords:** well-being, artificial intelligence (AI), higher education, quality of life

## Abstract

The increasing use of artificial intelligence (AI) in higher education is reshaping how students engage with their academic and personal lives. However, the impact of AI on students' well-being remains underexplored. This mini-review synthesizes current literature to assess how AI affects student well-being, focusing on mental health, social interactions, and academic experiences. While AI offers benefits such as personalized learning, mental health support, and improved communication efficiency, it also raises concerns regarding digital fatigue, loneliness, technostress, and reduced face-to-face interactions. Over-reliance on AI may diminish interpersonal skills and emotional intelligence, leading to social isolation and anxiety. Furthermore, issues such as data privacy and job displacement emerge as AI technologies permeate educational environments. The review highlights the need for balanced AI integration that supports both academic success and student well-being, advocating for further empirical studies to comprehensively understand these dynamics. As AI becomes more embedded in education, it is crucial to develop strategies that mitigate its negative effects while promoting holistic well-being among students.

## Introduction

The rapid integration of artificial intelligence (AI) into higher education is reshaping how students engage with academic content and spend their free time, yet its impact on their well-being remains underexplored. Despite the growing use of AI in both academic tasks and personal activities, empirical studies on its effects on student well-being are notably scarce. This study addresses this gap by conducting a mini-review that seeks to synthesize the limited experimental and empirical evidence available on this critical issue. While the small number of studies reflects the early stages of research in this field, it is vital to establish a clear understanding of what is currently known. By doing so, this mini-review lays the groundwork for future empirical investigations, highlighting the importance of exploring how AI affects students' mental health, social interactions, and overall well-being in higher education. Conducting this review is timely and necessary to create a foundation for further research, ensuring that the impact of AI on students is examined comprehensively as its use continues to expand.

In the context of higher education, AI-driven technologies are becoming indispensable tools for students, not only aiding their academic pursuits but also shaping the way they spend their leisure time (Chaudhary
```

---

### Chunk 4 — Instructor trust/distrust in GenAI (survey abstract)

**Source document:** `sciencedirect.txt` (chunk_id 0, 500 tokens)

```text
# Trust and Distrust in Generative AI Among Instructors in Higher Education

**Source:** ScienceDirect

**Keywords:** Generative AI, Trust, Distrust, Survey study, Teaching and learning, Higher education

## Abstract

Generative AI (GenAI) has brought opportunities and challenges for higher education as it integrates into teaching and learning environments. As instructors navigate this new landscape, understanding their engagement with and attitudes toward GenAI is crucial. We surveyed 178 instructors from a single U.S. university to examine their current practices, perceptions, trust, and distrust of GenAI in higher education in March 2024. While most surveyed instructors reported moderate to high familiarity with GenAI-related concepts, their actual use of GenAI tools for direct instructional tasks remained limited. Our quantitative results show that trust and distrust in GenAI are related yet distinct; high trust does not necessarily imply low distrust, and vice versa. We also found significant differences in surveyed instructors' familiarity with GenAI across different trust and distrust groups. Our qualitative results show nuanced manifestations of trust and distrust among surveyed instructors and various approaches to support calibrated trust in GenAI. We discuss practical implications focused on (dis)trust calibration among instructors.

## 1. Introduction

Generative AI (GenAI) is rapidly transforming teaching and learning in higher education, introducing significant changes and uncertainties (Michel-Villarreal et al., 2023). Faculty, students, and institutions all face uncertainty and anxiety surrounding the role of GenAI in teaching and learning, as it is uncertain to what extent they should embrace or restrict the use of GenAI in educational contexts (Adeshola & Adepoju, 2023). Policymakers also face challenges in devising appropriate regulatory frameworks and guidelines to manage the integration of GenAI into higher education, balancing innovation with ethical considerations and academic integrity (Luo, 2024). Meanwhile, attitudes and practices among different stakeholders regarding GenAI vary significantly across educational communities. For example, according to a survey conducted in 2023 by Tyton Partners, most students are increasingly curious about GenAI, with nearly half of the college students using these tools regularly (Fox & Shaw, 2023). In contrast, only 22% of faculty members have adopted GenAI (Coffey, 2023). Even among instructors, the integration of GenAI into educational practices has sparked polarized reactions (Mishra et al., 2024; D'Agost
```

---

### Chunk 5 — Online students' perceptions of generative AI (definitions and key findings)

**Source document:** `oregon-ecampus-genai-survey.txt` (chunk_id 0, 500 tokens)

```text
# Online Students' Perceptions of Generative AI

**Source:** Oregon State University Ecampus Research Unit, July 2024. Authors: Mary Ellen Dello Stritto, Ph.D.; Greta R. Underhill, Ph.D.; Naomi R. Aguiar, Ph.D.

*Note on this text version: the report's full survey instrument (Appendix A) and supplementary demographic data tables (Appendix B) have been omitted here since their content is already summarized in the Results and Description of Respondents sections below. See the original PDF for the complete appendices.*

## Definitions

**Generative AI Tools:** Tools that are capable of generating text, images, or other media. Examples included: ChatGPT, Bard, DALL-E, Copilot, and Claude.

**Professional Activities:** Anything outside of academic work that supports career goals, which could include activities such as a current job, internship, volunteering, and job-seeking activities.

**Personal Activities:** Anything outside of academic or professional work such as entertainment, personal growth, hobbies, household activities, and family activities.

## Key Findings

**Knowledge and use of generative AI tools**

- Participants demonstrated a deep knowledge of generative AI; however, the majority of participants had not used generative AI tools in their Ecampus courses. About half indicated they had used generative AI for professional and personal activities.
- Compared to fully online students, campus-based students, who were an average of 10 years younger, reported using these tools on a more frequent basis. Two-thirds of all respondents indicated they were using generative AI tools for brainstorming/generating ideas, code, or content.
- Participants were split in their responses about using generative AI tools in Ecampus courses, integrating them in their coursework, and receiving guidance from their instructors.

**Utility and value of generative AI tools**

- Although most participants were skeptical about the accuracy, trustworthiness, and reliability of generative AI tools, most agreed that knowing how to use generative AI would help them get a job, help at work, and help in their careers. However, they were less likely to agree that it would help their grade in a course.

**Course policies about generative AI**

- A significant number of participants indicated that generative AI tools were not addressed at all in their online courses. When they were addressed, participants experienced many different policies, levels of guidance, and degrees of clarity about policies regarding the
```

---

## Embedding Model

<!-- Name the embedding model you used and explain your choice.
     Then answer: if you were deploying this system for real users and cost wasn't a constraint,
     what tradeoffs would you weigh in choosing a different model?
     Consider: context length limits, multilingual support, accuracy on domain-specific text,
     latency, and local vs. API-hosted. -->

**Model used:**

`all-MiniLM-L6-v2` via `sentence-transformers`, running locally (no API key, no rate limits, 384-dim embeddings). Chosen as the recommended default for a class project of this scale — 152 chunks embed and query in well under a second on CPU, and index-build time doesn't factor into the per-query user experience.

**Production tradeoff reflection:**

If cost weren't a constraint, I'd weigh a larger API-hosted model (e.g. OpenAI's `text-embedding-3-large` or Voyage AI's domain-tuned models) against `all-MiniLM-L6-v2` on a few axes: (1) **accuracy on domain-specific text** — MiniLM is a general-purpose model trained mostly on short, everyday sentence pairs, and the retrieval tests above show it sometimes conflates chunks that share surface-level phrasing ("students and faculty," "generative AI in courses") but come from different studies; a model with stronger academic/research-text pretraining would likely separate those cases better. (2) **context length** — MiniLM truncates at 256 tokens internally, so a 500-token chunk is silently cut in half before embedding, which caps how much of each chunk's content actually informs its vector; a model with a longer effective context (e.g. 8k-token embedding models) would let me embed larger, more self-contained chunks without this truncation. (3) **latency and local vs. API-hosted** — a local model has zero network latency and no per-call cost, which matters for a live Gradio demo with unpredictable traffic, but an API-hosted model scales without me managing GPU/CPU capacity as the corpus grows. (4) **multilingual support** isn't relevant to this corpus (all documents are English), so I wouldn't pay for it here, but it would matter if the domain expanded to international student surveys.

---

## Retrieval Test Results

<!-- Run these 3 queries through your retrieval system and record the top returned chunks.
     For at least 2 of the 3, explain why the returned chunks are relevant to the query.
     Results must be text — not screenshots. -->

Retrieved via `python app/retrieve.py` (top-k=5, cosine distance, `all-MiniLM-L6-v2` embeddings, 152-chunk ChromaDB collection). All distances below are well under the ~0.6–0.7 "weak match" threshold, so no chunk-size or overlap tuning was needed.

**Query 1:** *"According to the HEPI Student Generative AI Survey 2026, do students believe generative AI improves their learning experience?"*

Top returned chunks:
- `hepi.txt` chunk_id 0, distance 0.2665 — "AI Use Is Now 'Near Universal' Among Undergraduates, but Students Are Divided on Its Impact... In just three years, generative AI has moved from novelty to near universality among undergraduates..."
- `springnature.txt` chunk_id 23, distance 0.3000 — "students are tasked with complex programming projects... Course-level analyses could explore which types of courses benefit most from generative AI integration..."
- `springnature.txt` chunk_id 4, distance 0.3025 — "...using them to explore topics of interest, create personal projects, or prepare for future careers. This highlights the dual nature of generative AI in education..."

Relevance explanation: The single best match (distance 0.27) is the opening chunk of `hepi.txt` itself — the exact HEPI 2026 survey named in the query — and it directly addresses whether students are divided on AI's impact on learning. The next two results come from a different paper (`springnature.txt`) discussing similar themes (student use of generative AI for learning) but not the HEPI survey specifically; they're topically adjacent rather than exact matches, which is expected since HEPI report content is split across only 4 chunks total.

---

**Query 2:** *"What concerns do instructors have about trusting generative AI, according to the study on instructor perceptions and distrust of AI?"*

Top returned chunks:
- `sciencedirect.txt` chunk_id 0, distance 0.1915 — "Trust and Distrust in Generative AI Among Instructors in Higher Education... We surveyed 178 instructors from a single U.S. university to examine their current practices, perceptions, trust, and distrust of GenAI..."
- `sciencedirect.txt` chunk_id 6, distance 0.2847 — "...understanding how instructors across a broad range of fields relate to GenAI... Trust is often conceptualized as a willingness to be vulnerable based on positive expectations of another party's intentions or behavior..."
- `hepi-policy-note-51.txt` chunk_id 7, distance 0.3284 — "software used to detect AI has consistently failed tests for reliability. Nearly two-thirds (65%) of students are 'quite' or 'very' confident that lecturers can determine whether AI has been used..."

Relevance explanation: This is the cleanest result of the three test queries. The top 2 hits (distances 0.19 and 0.28) both come from `sciencedirect.txt`, which is precisely the "study on instructor perceptions and distrust of AI" the query names — the abstract chunk and a chunk defining trust/distrust theory. The 3rd result drifts to a different document about AI-detection reliability, which is related to trust but from the student-facing HEPI policy note rather than the instructor study; it's a reasonable but looser match, consistent with its higher distance.

---

**Query 3:** *"According to the Oregon State University survey, how do online students and faculty differ in their perceptions of generative AI?"*

Top returned chunks:
- `oregon-ecampus-genai-survey.txt` chunk_id 2, distance 0.2072 — "...The goal of this study was to survey students taking online courses at Oregon State University about their perceptions, understanding, and use of generative AI tools..."
- `springnature.txt` chunk_id 23, distance 0.3057 — "students are tasked with complex programming projects... Course-level analyses could explore which types of courses benefit most from generative AI integration..."
- `oregon-ecampus-genai-survey.txt` chunk_id 0, distance 0.3329 — "Online Students' Perceptions of Generative AI... Source: Oregon State University Ecampus Research Unit, July 2024..."

Relevance explanation: Results 1 and 3 (distances 0.21 and 0.33) are correctly pulled from `oregon-ecampus-genai-survey.txt`, the exact document named in the query. Result 2 is a partial miss: it comes from `springnature.txt`, a different survey that also compares student and faculty attitudes toward generative AI, so it shares strong topical overlap ("students and faculty," "generative AI in courses") without being the Oregon State study specifically — a good illustration of why source metadata matters for attribution, not just topical relevance.

---

## Grounded Generation

<!-- Explain how your system enforces grounding — how does it prevent the LLM from answering
     beyond the retrieved documents?
     Describe both your system prompt (what instruction you gave the model) and any structural
     choices (e.g., how you formatted the context, whether you filtered low-relevance chunks).
     Do not just say "I told it to use the documents" — show the actual instruction or explain
     the mechanism. -->

**System prompt grounding instruction:**

Grounding is enforced by three mechanisms working together, not just a polite instruction — because an instruction alone is easy for a model to quietly ignore when its context is thin.

1. **Relevance filtering before the LLM ever sees anything.** `generate.py`'s `ask()` calls `retrieve()` and drops every chunk with cosine distance above `RELEVANCE_THRESHOLD = 0.7` (the same "weak match" cutoff validated during Milestone 4 retrieval testing) *before* building the prompt. If nothing survives that filter, `generate_answer()` returns the refusal string directly and skips the LLM call entirely — so a wildly off-topic question can never even reach a model that might otherwise pad thin context with general knowledge.
2. **A system prompt that ranks refusal above helpfulness**, sent verbatim on every call (`app/generate.py`):

   ```text
   You are a research assistant answering questions about AI in higher education, using ONLY the excerpts provided in the user message.

   Rules, in order of priority:
   1. Answer using ONLY information stated in the excerpts below. Never use outside knowledge, training data, or general assumptions about the topic — even if you're confident they're correct or the excerpts seem incomplete.
   2. If the excerpts do not contain enough information to answer the question, respond with EXACTLY this sentence and nothing else: "I don't have enough information on that."
   3. When you state a fact, name the source document it came from inline in plain prose (e.g., "According to hepi.txt, ..."), using only the exact source filenames given with each excerpt. Do not invent line numbers, footnote markers, or bracketed reference codes — a filename mentioned in a sentence is the only citation format allowed.
   4. Do not combine information across excerpts to imply a connection the excerpts don't actually state. Do not speculate, generalize, or fill gaps with plausible-sounding claims.
   5. Keep the answer concise and directly responsive to the question.
   ```

   The user message itself contains nothing but the question and the filtered excerpts, each labeled `[Excerpt N — source: <filename>]`, so the model has no other text to draw an answer from.
3. **Temperature 0.2**, to keep the model close to what the excerpts literally say rather than generating loosely-associated phrasing.

I verified this catches real failure modes during testing, not just theoretical ones: an early version of the system prompt (before rule 3 was tightened) had the model cite a correct source but invent a fake line-range reference like `【sciencedirect.txt†L1-L5】` — technically still grounded in content, but fabricating citation *metadata* that wasn't given to it. Tightening rule 3 to forbid anything but a plain filename mention fixed it.

**How source attribution is surfaced in the response:**

Attribution is **programmatic, not model-reported** — `ask()` builds the `"sources"` list from the metadata of the chunks that were actually retrieved and passed to the model (`[h["source"] for h in relevant]`, de-duplicated but rank-ordered), not by parsing the LLM's own citations out of its answer text. This guarantees the source list is accurate even if the model forgets rule 3 or phrases a citation oddly — the UI always shows exactly which documents were in context, independent of what the model chose to mention inline.

---

## Example Responses

<!-- Provide at least 2 grounded responses (query + response + source attribution)
     and 1 out-of-scope query showing your system's refusal.
     All entries must be text — not screenshots. -->

**Grounded response 1**

Query: `What concerns do instructors have about trusting generative AI, according to the study on instructor perceptions and distrust of AI?`

Response: "Instructors express uncertainty and anxiety about the role of generative AI in teaching and learning, and they view distrust as a distinct feeling of suspicion and an expectation that the technology could cause harm (sciencedirect.txt). This suggests that many instructors are cautious about relying on generative AI because they are unsure how it will affect their work and fear possible negative consequences."

Source attribution: `sciencedirect.txt`, `hepi-policy-note-51.txt`, `springnature.txt` — matches the correct instructor-trust study (`sciencedirect.txt`) that the query names, cited inline exactly as retrieved.

---

**Grounded response 2**

Query: `Do students think using AI on assignments counts as cheating?`

Response: "According to the oup-higher-education-ai-survey.txt survey, 38% of students said that 'using AI to generate content for graded assessments is the same as cheating.' This indicates that a notable minority of students do view AI-generated work on assignments as cheating."

Source attribution: `hepi-policy-note-51.txt`, `oup-higher-education-ai-survey.txt`, `columbia.txt`, `sciencedirect.txt`, `springnature.txt` — the specific statistic in the answer is traceable to `oup-higher-education-ai-survey.txt`, which the model correctly names inline; the response could not have come from anywhere but that retrieved excerpt.

---

**Out-of-scope query**

Query: `What is the capital of France?`

System response (refusal): "I don't have enough information on that."

This is the strongest grounding test in the set — the model unambiguously knows this fact from training, but the question falls outside the document collection (no chunk cleared the 0.7 relevance threshold), so `generate_answer()` never even reached the LLM. Same behavior verified with an in-domain-sounding but uncovered question, `"What is the best dining hall on campus?"` — same refusal, same empty source list.

---

## Query Interface

<!-- Describe your query interface: what are the input fields, what does the output look like?
     Then provide a complete sample interaction transcript showing a real exchange. -->

**Input fields:**

A single text box (`gr.Textbox`, labeled "Your question") with an "Ask" button; pressing Enter in the box also submits, via `inp.submit(...)` wired to the same handler as `btn.click(...)`.

**Output format:**

Two read-only text boxes: **Answer** (the grounded response text, or the "I don't have enough information on that." refusal) and **Retrieved from** (a `- filename.txt` bullet list of every source document behind the answer, built programmatically from retrieval metadata — see Grounded Generation above). Built with Gradio Blocks (`app/app.py`); run with `python app/app.py`.

---

**Sample Interaction Transcript**

<!-- Show a complete query → response exchange as it actually appears in your interface.
     Must be text — not a screenshot. -->

> **User:** Do students think using AI on assignments counts as cheating?

> **System:**
> **Answer:** According to the oup-higher-education-ai-survey.txt survey, 38% of students said that "using AI to generate content for graded assessments is the same as cheating." This indicates that a notable minority of students do view AI-generated work on assignments as cheating.
>
> **Retrieved from:**
> - hepi-policy-note-51.txt
> - oup-higher-education-ai-survey.txt
> - columbia.txt
> - sciencedirect.txt
> - springnature.txt

Captured directly from `app.handle_query()` (the same function wired to the Gradio button/textbox), confirmed working in a live `demo.launch()` session (HTTP 200 on `http://127.0.0.1:7860`).

---

## Evaluation Report

<!-- Run your 5 test questions from planning.md through your system and record the results.
     Be honest — a partially accurate or inaccurate result that you explain well is more
     valuable than a suspiciously perfect result. -->

| # | Question | Expected answer | System response (summarized) | Retrieval quality | Response accuracy |
|---|----------|-----------------|------------------------------|-------------------|-------------------|
| 1 | | | | | |
| 2 | | | | | |
| 3 | | | | | |
| 4 | | | | | |
| 5 | | | | | |

**Retrieval quality:** Relevant / Partially relevant / Off-target  
**Response accuracy:** Accurate / Partially accurate / Inaccurate

---

## Failure Case Analysis

<!-- Identify at least one question where retrieval or generation did not work as expected.
     Write a specific explanation of *why* it failed, tied to a part of the pipeline.

     "The answer was wrong" is not an explanation.

     "The relevant information was split across a chunk boundary, so retrieval returned
     only half the context — the model didn't have enough to answer correctly" is an explanation.

     "The embedding model treated the professor's nickname as out-of-vocabulary and returned
     results from an unrelated review" is an explanation. -->

**Question that failed:**

**What the system returned:**

**Root cause (tied to a specific pipeline stage):**

**What you would change to fix it:**

---

## Spec Reflection

<!-- Reflect on how planning.md shaped your implementation.
     Answer both questions with at least 2–3 sentences each. -->

**One way the spec helped you during implementation:**

**One way your implementation diverged from the spec, and why:**

---

## AI Usage

<!-- Describe at least 2 specific instances where you used an AI tool during this project.
     For each: what did you give the AI as input, what did it produce, and what did you
     change, override, or direct differently?

     "I used Claude to help me code" is not sufficient.
     "I gave Claude my Chunking Strategy section from planning.md and asked it to implement
     chunk_text(). It returned a function using a fixed character split. I overrode the
     chunk size from 500 to 200 because my documents are short reviews, not long guides." -->

**Instance 1**

- *What I gave the AI:*
- *What it produced:*
- *What I changed or overrode:*

**Instance 2**

- *What I gave the AI:*
- *What it produced:*
- *What I changed or overrode:*
