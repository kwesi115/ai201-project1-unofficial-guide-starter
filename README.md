# The Unofficial Guide — Project 1

> **How to use this template:**
> Complete each section *after* you've built and tested the corresponding part of your system.
> Do not write placeholder text — if a section isn't done yet, leave it blank and come back.
> Every section below is required for submission. One-liners will not receive full credit.

---

## Domain

This system covers **sentiment toward AI in higher education** — how students, instructors, and institutional staff actually feel about and use generative AI tools like ChatGPT, drawn from recent surveys, policy notes, and peer-reviewed studies (2023–2026).

This knowledge is valuable because AI is actively reshaping teaching and learning: students may lean on it to complete assignments (raising academic-integrity questions), while instructors are simultaneously being pushed to use it for lesson planning, grading, and feedback. Whether that shift is net-positive is genuinely contested — nearly universal student adoption (95%, per HEPI 2026) sits next to instructor distrust and hesitancy, with faculty adoption lagging well behind students' (per the ScienceDirect and OUP instructor-focused surveys), and these numbers rarely show up together in any single official source. A university's own AI policy page tells you what's *allowed*, not what students or faculty actually *think* or *do*. Consolidated survey and study data — the kind scattered across HEPI, EDUCAUSE, Oxford University Press, ScienceDirect, Springer Nature, PubMed, and individual university research pages — is hard for a student or instructor to assemble themselves, because it requires cross-referencing multiple standalone reports that were never designed to be read together. This system pulls those perspectives (student, faculty, and institutional) into one place and answers questions grounded in what the underlying research actually found, rather than in general AI hype or a single institution's messaging.

---

## Document Sources

<!-- List every source you collected documents from.
     Be specific: include URLs, subreddit names, forum thread titles, or file names.
     Aim for variety — sources that together cover different subtopics or perspectives. -->

| # | Source | Type | URL or file path |
|---|--------|------|-----------------|
| 1 | Columbia University, Center for Teaching and Learning — "AI in Higher Education" | Institutional practitioner guide | [ai.ctl.columbia.edu/explore/understanding-ai](https://ai.ctl.columbia.edu/explore/understanding-ai/) (local copy: `documents/columbia.txt`) |
| 2 | EDUCAUSE QuickPoll Results — "Adopting and Adapting to Generative AI in Higher Ed Tech" | Staff/institutional poll report | [er.educause.edu/articles/2023/4/...](https://er.educause.edu/articles/2023/4/educause-quickpoll-results-adopting-and-adapting-to-generative-ai-in-higher-ed-tech) (local copy: `documents/educause.txt`) |
| 3 | HEPI Report 199 — "Student Generative AI Survey 2026" (with Kortext) | Student survey (n=1,054 UK undergraduates) | [hepi.ac.uk/reports/student-generative-ai-survey-2026](https://www.hepi.ac.uk/reports/student-generative-ai-survey-2026/) (local copy: `documents/hepi.txt`) |
| 4 | HEPI Policy Note 51 — "Provide or Punish? Students' Views on Generative AI in Higher Education" (Josh Freeman, with Kortext) | Student survey / policy note (n=1,250 students) | [hepi.ac.uk/reports/provide-or-punish-...](https://www.hepi.ac.uk/reports/provide-or-punish-students-views-on-generative-ai-in-higher-education/) (local copy: `documents/hepi-policy-note-51.txt`) |
| 5 | Klimova & Pikhart — "Exploring the Effects of AI on Student and Academic Well-Being in Higher Education: A Mini-Review" | Peer-reviewed literature review (NLM/PubMed Central) | [pmc.ncbi.nlm.nih.gov/articles/PMC11830699](https://pmc.ncbi.nlm.nih.gov/articles/PMC11830699/) (local copy: `documents/nlm.txt`) |
| 6 | Dello Stritto, Underhill & Aguiar — "Online Students' Perceptions of Generative AI" (Oregon State University Ecampus Research Unit, July 2024) | Student survey (n=669) | [ecampus.oregonstate.edu/research/.../Online-Students-Perceptions-of-AI-Report.pdf](https://ecampus.oregonstate.edu/research/wp-content/uploads/Online-Students-Perceptions-of-AI-Report.pdf) (local copy: `documents/oregon-ecampus-genai-survey.txt`) |
| 7 | Oxford University Press — "Higher Education and AI: Survey Findings" (June 2024) | Paired student/lecturer survey (674 students, 841 lecturers) | [pages.oup.com/he/us/ai-survey](https://pages.oup.com/he/us/ai-survey) (local copy: `documents/oup-higher-education-ai-survey.txt`) |
| 8 | "Understanding the Practices, Perceptions, and (Dis)Trust of Generative AI Among Instructors" | Peer-reviewed journal article, ScienceDirect (n=178 instructors) | [sciencedirect.com/science/article/pii/S2666920X25000232](https://www.sciencedirect.com/science/article/pii/S2666920X25000232) (local copy: `documents/sciencedirect.txt`) |
| 9 | Kim et al. — "Examining Faculty and Student Perceptions of Generative AI in University Courses" | Peer-reviewed journal article, Springer Nature / *Innovative Higher Education* (n=982 students, 76 faculty) | [link.springer.com/article/10.1007/s10755-024-09774-w](https://link.springer.com/article/10.1007/s10755-024-09774-w) (local copy: `documents/springnature.txt`) |
| 10 | Kale, Ling & Imas — "Underreporting of AI Use: The Role of Social Desirability Bias" (University of Chicago, CHI 2026) | Research news summary of a peer-reviewed study (n=338 students) | [cs.uchicago.edu/news/are-students-hiding-their-ai-use-...](https://cs.uchicago.edu/news/are-students-hiding-their-ai-use-the-social-stigma-behind-ai-use-in-the-classroom/) (local copy: `documents/uchicago.txt`) |

---

## Chunking Strategy

<!-- Describe your chunking approach with enough specificity that someone else could reproduce it.
     Include:
     - Chunk size (characters or tokens) and why that size fits your documents
     - Overlap size and why (or why not) you used overlap
     - Any preprocessing you did before chunking (e.g., stripping HTML, removing headers)
     - What your final chunk count was across all documents -->

**Chunk size:**

500 tokens, measured with `tiktoken`'s `cl100k_base` encoding (`app/chunk.py`). `chunk_text()` encodes the whole cleaned document to token ids once, then slides a fixed-size window across that token array and decodes each window back to text — so every chunk (except possibly the last one per document) is exactly 500 tokens, not an approximation based on word or character count.

**Overlap:**

100 tokens. The sliding window advances by `chunk_size - overlap` = 400 tokens each step, so consecutive chunks from the same document share their last/first 100 tokens.

**Preprocessing before chunking:**

`ingest.py`'s `clean_text()` runs on every document before chunking: it HTML-unescapes entities, normalizes line endings, collapses runs of 3+ blank lines to one, and collapses runs of horizontal whitespace — all generic cleanup for text pulled from PDFs/webpages, not tailored to any one source, so it's safe to rerun if new documents are added.

**Why these choices fit your documents:**

The 10 source documents are research articles, survey reports, and policy notes — dense, multi-paragraph prose where a single finding (e.g., a specific statistic and the methodology or caveat that qualifies it) often spans several sentences or a full paragraph. 500 tokens is large enough to keep a survey finding together with its immediate context (who was surveyed, what percentage, what it means) without pulling in unrelated sections of the same document. The 100-token overlap exists specifically to protect against key claims landing right on a chunk boundary — splitting a statistic from the sentence that explains it would silently degrade retrieval and generation quality, and this was worth the ~20% storage/embedding overhead it adds. Live retrieval testing (see Retrieval Test Results below) came back with all top-ranked distances well under the 0.6–0.7 "weak match" threshold, so no chunk-size or overlap tuning was needed after the fact.

**Final chunk count:**

152 chunks across 10 documents (verified by running `chunk_documents()` over all documents in `documents/` — output: `docs: 10`, `chunks: 152`). The ChromaDB collection built by `embed.py` also reports `collection.count() == 152`, confirming every chunk was embedded and stored.

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

All 5 questions were run live through `generate.ask()` against the real 152-chunk collection (not hand-simulated) on the date of this report.

| # | Question | Expected answer | System response (summarized) | Retrieval quality | Response accuracy |
|---|----------|-----------------|------------------------------|-------------------|-------------------|
| 1 | According to the HEPI Student Generative AI Survey 2026, do students believe generative AI improves their learning experience? | Should summarize whether the survey found students generally view AI as improving their learning experience, citing HEPI. | "AI improves the student experience for many – but not all," citing that 49% of students report AI improves their experience (`hepi.txt`). | Relevant | Accurate |
| 2 | What concerns do instructors have about trusting generative AI, according to the study on instructor perceptions and distrust of AI? | Should identify concerns such as inaccurate/unreliable outputs, lack of trust, and uncertainty about quality/appropriate use. | Explained that instructor distrust reflects "suspicion and the expectation of harm," distinct from an absence of trust, citing `sciencedirect.txt`. | Relevant | Partially accurate |
| 3 | How do students and faculty differ in their perceptions of generative AI in university courses? | Should compare student/faculty attitudes, including differences in use, ethical concerns, and perceived effect on learning. | Students report higher ease-of-use, enjoyment, and personal innovativeness; faculty report more habitual use; both groups expect more negative than positive effects on most competencies except academic performance, where students are more optimistic (`springnature.txt`). | Relevant | Accurate |
| 4 | What do students think about using generative AI for academic work, including concerns about cheating and academic integrity? | Should explain mixed views: AI supports learning, but students worry about cheating, unfair use, and unclear policies. | Students expect institutions can detect AI misuse and worry about false-positive accusations; over two-thirds say AI can promote dishonesty, yet about half still see its use as ethical; students want more institutional guidance (`hepi-policy-note-51.txt`, `springnature.txt`). | Relevant | Accurate |
| 5 | According to the Oregon State University survey, how do online students and faculty differ in their perceptions of generative AI? | Should compare online student and faculty perspectives, including student skepticism and faculty concerns/uncertainty. | "I don't have enough information on that." | Partially relevant | Inaccurate (see Failure Case Analysis) |

**Retrieval quality:** Relevant / Partially relevant / Off-target  
**Response accuracy:** Accurate / Partially accurate / Inaccurate

For Q2, "partially accurate" reflects that the answer is correctly grounded in the right study (`sciencedirect.txt`) but leans on the paper's abstract theoretical framing of trust/distrust rather than the concrete, practical concerns (e.g., output reliability, appropriate-use uncertainty) the expected answer named — those specific concerns exist elsewhere in the same document but weren't among the top-5 chunks retrieved for this phrasing of the question.

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

"According to the Oregon State University survey, how do online students and faculty differ in their perceptions of generative AI?" (evaluation question 5)

**What the system returned:**

"I don't have enough information on that." — the refusal string, with an empty effective context even though retrieval itself succeeded: the top hit was `oregon-ecampus-genai-survey.txt` chunk 0 at distance 0.2072, well under the 0.7 relevance threshold, and 2 of the top 5 hits came from that exact document.

**Root cause (tied to a specific pipeline stage):**

This is not a retrieval bug — `retrieve()` correctly found the right document on the first try. The failure traces back to the **document collection itself, and to a false assumption baked into the evaluation question in `planning.md`**. I checked the source text directly (`grep -i "faculty\|instructor" documents/oregon-ecampus-genai-survey.txt`): the OSU Ecampus report surveyed *only online students* — every mention of "instructor" in the document describes students' perceptions of their instructors' AI policies (e.g., "About three-quarters of undergraduate participants indicated they had at least one instructor who did not allow any use of generative AI"), never instructors' own attitudes toward AI. The evaluation question assumes the survey directly compares student and faculty perspectives, but no chunk in the corpus actually contains faculty's own perceptions from that survey — because that data doesn't exist in the source document. Faced with retrieved-but-irrelevant-to-the-question chunks, `generate_answer()`'s system prompt (rule 2) correctly told the model to refuse rather than fabricate a faculty perspective that isn't in the excerpts — the grounding mechanism worked exactly as designed, it's just that "working as designed" here means correctly refusing an unanswerable question.

**What I would change to fix it:**

Two options, not mutually exclusive: (1) Rewrite the evaluation question to match what the OSU document actually contains — e.g., "How do online students' AI use compare across undergraduate, post-baccalaureate, and graduate levels, per the OSU Ecampus survey?" — which the collection can answer. (2) If a true student-vs-faculty OSU-specific comparison is the goal, that would require adding a genuine faculty-side OSU survey document to the corpus; note the collection does already contain a real faculty-vs-student comparison (`springnature.txt`, the Kim et al. study), so a corrected evaluation question could also just target that document by name instead of misattributing the comparison to OSU.

---

## Spec Reflection

<!-- Reflect on how planning.md shaped your implementation.
     Answer both questions with at least 2–3 sentences each. -->

**One way the spec helped you during implementation:**

Writing the Chunking Strategy and Retrieval Approach sections in `planning.md` *before* touching any code gave me concrete, testable numbers to hand to Claude Code instead of vague instructions. Because I had already committed to "500-token chunks, 100-token overlap, top-5 retrieval" on paper, I could ask for `chunk_text(text, chunk_size=500, overlap=100)` as a precise function signature and immediately verify the output against that spec (checking that consecutive chunks actually shared ~100 tokens, that chunk counts matched expectations) rather than eyeballing whether the output "looked reasonable." The same was true for the `RELEVANCE_THRESHOLD = 0.7` cutoff in `generate.py` — because planning.md's evaluation plan forced me to think about what a "good" versus "bad" retrieval match looked like before generation existed, I had a concrete number to filter on instead of tuning it after the fact once bad answers started showing up.

**One way your implementation diverged from the spec, and why:**

The assignment's recommended Groq model, `meta-llama/llama-4-scout-17b-16e-instruct`, had been retired from Groq's model catalog by the time I built the generation stage (confirmed via `client.models.list()` — see the comment in `app/generate.py`). I substituted `openai/gpt-oss-120b`, a free-tier Groq model, because in testing it followed the "refuse if the excerpts don't have enough information" instruction (system prompt rule 2) far more reliably than the alternatives I tried, which matters more for a grounded system than raw fluency. Separately, my final 10 documents don't exactly match the 10 sources originally listed in `planning.md`'s Documents table (e.g., "Inside Higher Ed" and "Multi-Informant Study" from that early list aren't among the final files in `documents/`) — the corpus evolved during collection to the set documented in Document Sources above, still covering the same domain and source variety the plan called for.

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

- *What I gave the AI:* I gave Claude Code the Architecture and Retrieval Approach sections of `planning.md`, plus the assignment's recommendation to use `meta-llama/llama-4-scout-17b-16e-instruct` via Groq, and asked it to implement `generate.py`'s LLM call.
- *What it produced:* Claude Code discovered (by calling `client.models.list()`) that the recommended model had been retired from Groq's catalog and would fail at runtime, and proposed switching to `openai/gpt-oss-120b` as a free-tier replacement.
- *What I changed or overrode:* I accepted the model swap, but I didn't just take "it works" as sufficient — I directed additional testing specifically on whether the replacement model reliably obeyed the "say you don't know" refusal rule (system prompt rule 2), since a fluent-but-non-compliant model would silently break grounding. I also had it document the substitution and the reason inline as a code comment in `generate.py`, so the model choice wouldn't look arbitrary to someone reading the code later.

**Instance 2**

- *What I gave the AI:* After the first working version of `generate.py` was in place, I ran a batch of test questions (including borderline/out-of-scope ones) and gave Claude Code one specific failure I noticed: the model was citing the correct source document, but also inventing a fake citation-style reference that looked like `【sciencedirect.txt†L1-L5】` — a line-range format that was never given to it anywhere in the prompt. I asked Claude Code to fix the system prompt so this couldn't happen again.
- *What it produced:* Claude Code's first fix just added a general instruction like "cite sources accurately," which didn't reliably stop the fabricated line-range format in follow-up testing.
- *What I changed or overrode:* I rewrote system-prompt rule 3 myself to be much more restrictive and explicit: "name the source document it came from inline in plain prose... Do not invent line numbers, footnote markers, or bracketed reference codes — a filename mentioned in a sentence is the only citation format allowed." I also decided the citation list shouldn't depend on the model's compliance at all as a second line of defense — I directed that `ask()` build the returned `"sources"` list programmatically from retrieval metadata (`[h["source"] for h in relevant]`) instead of trying to parse whatever citation format the LLM produced, so the UI's source attribution stays correct even if a future model change reintroduces a citation-formatting quirk.
