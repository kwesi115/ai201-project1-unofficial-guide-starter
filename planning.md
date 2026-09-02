# Project 1 Planning: The Unofficial Guide

> Write this document before you write any pipeline code.
> Your spec and architecture diagram are what you'll use to direct AI tools (Claude, Copilot, etc.) to generate your implementation — the more specific they are, the more useful the generated code will be.
> Update the Retrieval Approach and Chunking Strategy sections if you change your approach during implementation.
> Update this file before starting any stretch features.

---

## Domain

<!-- What domain did you choose? Why is this knowledge valuable and hard to find through official channels? -->
The domain I chose was AI sentiment in higher education. I believe this information is valuable because AI is a rapidly growing field that is disrupting many parts of society, including higher education. For example, students may abuse AI to cheat on assignments or in class, while teachers may use AI to create lesson plans, which could potentially affect the quality of education. Information about overall sentiment toward AI in higher education can be difficult to find because there are many different approaches and opinions surrounding its use. Therefore, consolidating these perspectives and ideas could be beneficial.
 

---

## Documents

<!-- List your specific sources: URLs, subreddit names, forum threads, or file descriptions.
     Aim for at least 10 sources that together cover different subtopics or perspectives within your domain. -->

| # | Source | Description | URL or location |
|---|--------|-------------|-----------------|
| 1 | UChicago | Kale, Ling & Imas, "Underreporting of AI Use: The Role of Social Desirability Bias" (CHI 2026). Survey of 338 students finds a large gap between self-reported personal AI use (~60%) and perceived peer use (~90%), attributed to social desirability bias. | https://cs.uchicago.edu/news/are-students-hiding-their-ai-use-the-social-stigma-behind-ai-use-in-the-classroom/ |
| 2 | HEPI 2026 | HEPI Report 199, "Student Generative AI Survey 2026" (with Kortext). Survey of 1,054 UK undergraduates (Savanta, Dec 2025) finds AI use is now "near universal" (95%) among students but adoption support from institutions is lagging. | https://www.hepi.ac.uk/reports/student-generative-ai-survey-2026/ |
| 3 | Inside Higher Ed | "Survey: College Students' Views on AI" (Inside Higher Ed Student Voice series, Aug 2025). Student survey finding mixed views on faculty AI use, widespread use of AI to support their own learning, and concern that reliance on AI could affect critical-thinking skills. | https://www.insidehighered.com/news/students/academics/2025/08/29/survey-college-students-views-ai |
| 4 | Instructor (Dis)Trust Study | "Understanding the Practices, Perceptions, and (Dis)Trust of Generative AI Among Instructors: A Mixed-Methods Study in U.S. Higher Education" (ScienceDirect). Survey of 178 instructors at one U.S. university (March 2024) finds trust and distrust of GenAI are related but distinct constructs. | https://www.sciencedirect.com/science/article/pii/S2666920X25000232 |
| 5 | Faculty vs. Student Perceptions | Kim et al., "Examining Faculty and Student Perceptions of Generative AI in University Courses" (*Innovative Higher Education*, Springer Nature). Survey of 982 students and 76 faculty (Fall 2023) comparing attitudes across ease of use, ethical concerns, and perceived learning impact. | https://link.springer.com/article/10.1007/s10755-024-09774-w |
| 6 | Oregon State | Dello Stritto, Underhill & Aguiar, "Online Students' Perceptions of Generative AI" (OSU Ecampus Research Unit, July 2024). Survey of 669 online students on their knowledge, use, and course-level experiences with generative AI. | https://ecampus.oregonstate.edu/research/wp-content/uploads/Online-Students-Perceptions-of-AI-Report.pdf |
| 7 | Provide or Punish? | HEPI Policy Note 51, Josh Freeman with Kortext (Feb 2024). Poll of 1,250 students via UCAS on attitudes to generative AI tools; finds AI use has normalized without an epidemic of AI-based cheating. | https://www.hepi.ac.uk/reports/provide-or-punish-students-views-on-generative-ai-in-higher-education/ |
| 8 | EDUCAUSE QuickPoll | "EDUCAUSE QuickPoll Results: Adopting and Adapting to Generative AI in Higher Ed Tech" (April 2023). Institutional staff poll tracking disposition toward generative AI (optimism rose from 54% to 67% between Feb and April 2023). | https://er.educause.edu/articles/2023/4/educause-quickpoll-results-adopting-and-adapting-to-generative-ai-in-higher-ed-tech |
| 9 | Oxford University Press | "Higher Education and AI: Survey Findings" (OUP, June 2024). Paired survey of 674 students and 841 lecturers on perceptions and use of AI across higher education. | https://pages.oup.com/he/us/ai-survey |
| 10 | Multi-Informant Study | "Generative AI Perceptions: A Survey to Measure the Perceptions of Faculty, Staff, and Students on Generative AI Tools in Academia" (arXiv). Survey of 243 faculty/staff and 813 students, capturing perception differences across all three stakeholder groups in one instrument. | https://arxiv.org/abs/2304.14415 |

---

## Chunking Strategy

<!-- How will you split documents into chunks?
     State your chunk size (in tokens or characters), overlap size, and explain why those
     numbers fit the structure of your documents.
     A review-heavy corpus warrants different chunking than a long FAQ. -->

**Chunk size:**
500 tokens

**Overlap:**
100 Tokens

**Reasoning:**
The documents in this knowledge base include research articles, surveys, reports, and news articles about attitudes toward AI in higher education. A chunk size of 500 tokens is large enough to preserve important context, such as survey findings, comparisons between students and faculty, and explanations of concerns about AI, while still being small enough to retrieve specific information relevant to a user's question. A 100-token overlap helps preserve context when important ideas or findings continue across chunk boundaries. This should reduce the risk of separating a claim from its supporting explanation and improve the quality of retrieval for questions about topics such as academic integrity, faculty trust, student attitudes, and AI's impact on learning.

---

## Retrieval Approach

<!-- Which embedding model are you using (e.g., all-MiniLM-L6-v2 via sentence-transformers)?
     How many chunks will you retrieve per query (top-k)?
     If you were deploying this for real users and cost wasn't a constraint, what tradeoffs
     would you weigh in choosing a different embedding model — context length, multilingual
     support, accuracy on domain-specific text, latency? -->

**Embedding model:**
all-MiniLM-L6-v2 via the sentence-transformers library.

**Top-k:**
5 chunks per query.

**Production tradeoff reflection:**
I chose all-MiniLM-L6-v2 because it is lightweight, fast, and effective for a relatively small collection of documents. Retrieving the top 5 chunks provides enough relevant context for the model to answer questions while limiting the amount of irrelevant information included in the prompt. For a production system where cost was not a constraint, I would consider using a more advanced embedding model with higher accuracy, particularly one that performs better on academic and domain-specific text. I would weigh factors such as retrieval accuracy, context length, multilingual support, and latency. A larger model could improve the system's ability to recognize subtle differences in sentiment and meaning across research articles, surveys, and faculty or student perspectives, but it could also increase response time and computational requirements.

---

## Evaluation Plan

<!-- List your 5 test questions with their expected correct answers.

     Questions should be specific enough that you can judge whether the system's response
     is right or wrong. "What are good dining halls?" is too vague.

     "What do students say about wait times at [dining hall name] during lunch?" is testable. -->

| # | Question                                                                                                                             | Expected answer                                                                                                                                                                                                    |
| - | ------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| 1 | According to the HEPI Student Generative AI Survey 2026, do students believe generative AI improves their learning experience?       | The system should accurately summarize whether the survey found students generally viewed AI as improving their learning experience and cite the relevant source.                                                  |
| 2 | What concerns do instructors have about trusting generative AI, according to the study on instructor perceptions and distrust of AI? | The system should identify concerns such as inaccurate or unreliable outputs, lack of trust, and uncertainty about the quality and appropriate use of AI in education.                                             |
| 3 | How do students and faculty differ in their perceptions of generative AI in university courses?                                      | The system should accurately compare student and faculty attitudes, including differences in AI use, ethical concerns, and perceptions of AI's effect on learning.                                                 |
| 4 | What do students think about using generative AI for academic work, including concerns about cheating and academic integrity?        | The system should explain that students have mixed views, recognizing AI's potential to support learning while also expressing concerns about cheating, unfair use, and unclear university policies.               |
| 5 | According to the Oregon State University survey, how do online students and faculty differ in their perceptions of generative AI?    | The system should accurately compare the perspectives of online students and faculty, including student skepticism about AI-generated information and faculty concerns or uncertainty about its educational value. |


---

## Anticipated Challenges

<!-- What could go wrong? Name at least two specific risks with reasoning.

     Consider: noisy or inconsistent documents, missing source attribution, off-topic
     retrieval, chunks that split key information across boundaries. -->

1. **Off-topic or inaccurate retrieval:** Because the documents cover different perspectives on AI in higher education, some chunks may contain similar keywords but discuss different topics. For example, a question about student attitudes toward AI could retrieve a chunk about faculty concerns simply because both mention generative AI. I will address this by testing retrieval results with the five evaluation questions and checking whether the retrieved chunks are actually relevant to the question.

2. **Loss of context and missing source attribution:** Important survey findings or conclusions may be split across chunk boundaries, causing the system to retrieve only part of the information needed for an accurate answer. Additionally, the system could generate an answer without clearly identifying which document the information came from. The 100-token overlap should help preserve context between chunks, and I will store source metadata with each chunk so the final response can include citations to the original document.

---

## Architecture

<!-- Draw a diagram of your pipeline showing the five stages:

     Document Ingestion → Chunking → Embedding + Vector Store → Retrieval → Generation

     Label each stage with the tool or library you're using.

     You can use ASCII art, a Mermaid diagram, or embed a sketch as an image.

     You'll use this diagram as context when prompting AI tools to implement each stage. -->

```text
┌──────────────────────────────┐
│     Document Ingestion       │
│                              │
│ Python + requests /          │
│ BeautifulSoup or PDF reader  │
│                              │
│ Collect and extract text     │
│ from AI in higher education  │
│ articles and reports         │
└──────────────┬───────────────┘
               │
               ▼
┌──────────────────────────────┐
│          Chunking            │
│                              │
│ Python                       │
│ 500-token chunks             │
│ 100-token overlap            │
└──────────────┬───────────────┘
               │
               ▼
┌──────────────────────────────┐
│ Embedding + Vector Store     │
│                              │
│ sentence-transformers        │
│ all-MiniLM-L6-v2             │
│                              │
│ ChromaDB                     │
└──────────────┬───────────────┘
               │
               ▼
┌──────────────────────────────┐
│         Retrieval            │
│                              │
│ ChromaDB similarity search   │
│ Retrieve top 5 chunks        │
│ most relevant to the query   │
└──────────────┬───────────────┘
               │
               ▼
┌──────────────────────────────┐
│         Generation           │
│                              │
│ LLM API                      │
│                              │
│ Generate a grounded answer   │
│ using retrieved chunks and   │
│ include source citations     │
└──────────────────────────────┘
```

---

## AI Tool Plan

<!-- For each part of the pipeline below, describe:

     - Which AI tool you plan to use (Claude, Copilot, ChatGPT, etc.)

     - What you'll give it as input (which sections of this planning.md, which requirements)

     - What you expect it to produce

     - How you'll verify the output matches your spec

     "I'll use AI to help me code" is not a plan.

     "I'll give Claude my Chunking Strategy section and ask it to implement chunk_text()

     with my specified chunk size and overlap" is a plan. -->

### 1. Document Ingestion

I will use Claude Code to help me generate the document ingestion functions. I will provide Claude Code with my project description and requirements for collecting text from the nine selected articles about AI sentiment in higher education. I will ask it to generate Python functions that load or extract the document text and preserve metadata such as the document title and source URL. I will verify the output by checking that all documents are successfully loaded, the extracted text is readable, and each document has the correct source information attached.

### 2. Chunking

I will use Claude Code to help me generate the chunking functions. I will provide Claude Code with the **Chunking Strategy** section of this planning document and specifically ask it to implement a function that splits documents into approximately 500-token chunks with a 100-token overlap. I will verify the code by inspecting several chunks manually and confirming that the overlap is present and that source metadata remains attached to each chunk.

### 3. Embedding and Vector Store

I will use Claude Code to help me generate the functions for converting chunks into embeddings using `all-MiniLM-L6-v2` from the `sentence-transformers` library and storing them in ChromaDB. I will provide the **Retrieval Approach** and **Architecture** sections as requirements. I expect it to produce functions that create embeddings, store each chunk and its metadata, and allow the vector database to be queried. I will verify the output by checking that the number of stored chunks matches the number generated during chunking and that queries return stored documents.

### 4. Retrieval

I will use Claude Code to help me generate the retrieval functions. I will provide the **Retrieval Approach** section and specify that the system must retrieve the top 5 most relevant chunks for each user query using similarity search. I expect Claude Code to generate a function that accepts a natural-language question, converts it into an embedding, and retrieves the five most relevant chunks from ChromaDB. I will verify the output using the questions in the **Evaluation Plan** and manually check whether the retrieved chunks contain information relevant to each question.

### 5. Generation

I will use Claude Code to help me generate the functions for the generation step. I will provide the **Architecture**, **Retrieval Approach**, and **Evaluation Plan** sections and ask it to implement a prompt that instructs an LLM to answer questions using only the retrieved context. I will also require the response to include citations or source information from the retrieved documents. I will verify the output by testing the five evaluation questions, comparing each answer with the expected answers, and checking that the system does not make unsupported claims or cite sources that were not retrieved.


**Milestone 3 — Ingestion and chunking:**

**Milestone 4 — Embedding and retrieval:**

**Milestone 5 — Generation and interface:**
