# T²-RAGBench: numerical QA after text-and-table retrieval

<!-- RELEASE-REFERENCE:START -->
> **Best at release (not yet verified)** · Benchmark recorded date: 2025-05-14<br>
> A best result tied to a model, metric, and protocol in the initial release has not yet been verified. [Original source](https://aclanthology.org/2026.eacl-long.8/)<br>
> No substitution from a live board, a single baseline, or a later paper; unknown is neither zero nor a claim that the authors reported no results.
<!-- RELEASE-REFERENCE:END -->

[中文](t2-ragbench.md) | **English** · [Home](../README.en.md)

<!-- EVIDENCE:reading:START -->
## Reading coverage and version

Read the stated version’s complete main text and available appendices and checked selected results; no independent experiment reproduction.

Read all twenty-seven pages of the EACL proceedings paper, including the main text, limitations and Appendices A–K: all six examples, preprocessing, reformulation/retrieval/generation/summary prompts and error analysis; visually checked Tables 3–4 and the numerical-scoring formula.

[EACL 2026 · 2026.eacl-long.8 · 165–191](https://aclanthology.org/2026.eacl-long.8.pdf)
<!-- EVIDENCE:reading:END -->

<!-- EVIDENCE:method:START -->
## Method and measurement target

The proceedings version contains 23,088 question-answer-context triples: 8,281 FinQA, 3,458 first-turn ConvFinQA and 11,349 TAT-DQA questions. Text and tables form Markdown context units, deduplicated to 7,318 units averaging approximately 924 tokens—not necessarily complete long reports. Llama 3.3-70B adds metadata while preserving reference answers. An illustrative workflow replaces a vague free-cash-flow question with a named company, year and calculation definition, retrieves the relevant text/table, reads its rows/columns and computes a number. Each question assumes one required gold context without exhaustive alternative-evidence annotation.

Editorial placement: FinQA, ConvFinQA and TAT-DQA are the direct sources, originally supplying answer-bearing context. T²-RAGBench adds company/year/metric qualifiers to make the retrieval target identifiable, then introduces retrieval. The new coordinate is the gap between locating text-table evidence and answering numerically, not full raw-PDF understanding, cross-report synthesis or persistent financial analysis.

[Source](https://aclanthology.org/2026.eacl-long.8.pdf)
<!-- EVIDENCE:method:END -->

<!-- EVIDENCE:setup:START -->
## Scoring and experimental conditions

The three subsets are indexed/evaluated separately. Main retrieval uses multilingual-e5-large-instruct and Chroma, passing the top three units to quantized Llama 3.3-70B or QwQ-32B on two H100s. Hybrid BM25 combines lexical/dense retrieval; Summarization retrieves and answers from summaries, whereas SumContext retrieves summaries but supplies originals to the reader. MRR@3 rewards the first gold context’s reciprocal rank; Recall@3 measures any hit. Number Match first takes absolute values and removes the nearest power-of-ten scale difference. The normalized prediction/reference ratio must lie within 0.01 of one; alternatively, both absolute values below 0.01 count as a match. By definition it can overlook sign and power-of-ten magnitude errors, so it is not strict financial numerical correctness. Outputs use a fixed JSON format and nonnumeric answers fail; complete decoding/retry/cost budgets are unreported.

[Source](https://aclanthology.org/2026.eacl-long.8.pdf)
<!-- EVIDENCE:setup:END -->

<!-- EVIDENCE:result-1:START -->
## Retrieval and numerical results with Llama 3.3-70B fixed

Question-weighted averages over 23,088 questions across separately indexed subsets; E5 retrieval, top-three contexts and quantized Llama 3.3-70B. NM is sign-/decimal-scale-insensitive; MRR and Recall differ. Supplied-gold-context NM is 72.7%, not an actual retrieval system.

| Method | NM (%) | MRR@3 (%) | Recall@3 (%) |
| --- | --- | --- | --- |
| Base-RAG | 35.8 | 32.6 | 39.8 |
| Hybrid BM25 | 40.9 | 35.2 | 49.4 |
| Summarization | 22.2 | 36.9 | 46.4 |
| SumContext | 39.5 | 37.0 | 46.3 |

Source location: Table 3, proceedings p. 171 (PDF p. 7); Sections 3 and 5 · [Source](https://aclanthology.org/2026.eacl-long.8.pdf)
<!-- EVIDENCE:result-1:END -->

<!-- EVIDENCE:result-2:START -->
## Overall leadership does not imply every-subset leadership

Same Llama 3.3-70B setup; denominators 8,281, 3,458 and 11,349 questions, with 2,789, 1,806 and 2,723 context units respectively. These are numeric-match scores, not verification of every calculation step.

| Method | FinQA NM (%) | ConvFinQA NM (%) | TAT-DQA NM (%) |
| --- | --- | --- | --- |
| Hybrid BM25 | 41.7 | 50.3 | 37.4 |
| SumContext | 47.2 | 55.5 | 29.1 |

Source location: Tables 2–3, proceedings pp. 168,171 (PDF pp. 4,7) · [Source](https://aclanthology.org/2026.eacl-long.8.pdf)
<!-- EVIDENCE:result-2:END -->

<!-- EVIDENCE:limitations:START -->
## Interpretation, limitations and next experiment

Hybrid BM25 has stronger overall NM, but SumContext leads separately on FinQA/ConvFinQA; there is no universal subset win. Higher MRR need not improve answers when summaries remove required values. A model family participates in both rewriting and answering, with only sampled question validation. Low closed-book scores do not establish absence of contamination. The 1,583-error manual analysis concerns Llama with supplied gold context, not retrieval failures. Overall table values are question-weighted, not equal averages of the three subsets.

The abstract gives 91.3% context independence while Section 4.2/Figure 3 give 93%; they are not reconciled. SumContext prose gives 37.4/36.7 versus Table 3’s 39.5/38.3; this note uses the table. Table 4’s E5/OpenAI values also differ from adjacent prose. MRR@3 below 50% does not mean the correct document appears in the top three for only half the queries—that is Recall@3. The proceedings contain 23,088 questions from three sources; this pass does not verify the earlier 32,908-item version or removal history.

Freeze this proceedings set and its context units; cross original/summary indexing with original/summary reading. Report original NM alongside sign-/unit-sensitive numerical checks and evidence localization. Audit alternative contexts and metric-changing rewrites, then test independent companies/years and real PDF parsing pipelines.

[Source](https://aclanthology.org/2026.eacl-long.8.pdf)
<!-- EVIDENCE:limitations:END -->
