# SAGE: scientific search should separate finding one target paper from collecting a complete evidence set

<!-- RELEASE-REFERENCE:START -->
> **Best at release (not yet verified)** · Benchmark recorded date: 2026-02-05<br>
> A best result tied to a model, metric, and protocol in the initial release has not yet been verified. [Original source](https://arxiv.org/abs/2602.05975)<br>
> No substitution from a live board, a single baseline, or a later paper; unknown is neither zero nor a claim that the authors reported no results.
<!-- RELEASE-REFERENCE:END -->

[中文](sage.md) | **English** · [Benchmark Library](../library/README.en.md)

<!-- EVIDENCE:reading:START -->
## Reading scope and version

Reviewed the stated primary paper in full for methods, experimental setup, results and limitations; no independent reproduction.

Read Sections 1–6 and limitations; appendices inspected: A.1–A.6, examples, query decomposition, length distributions, BrowseComp comparison, SearchR1 and all prompt templates; visual checks: Table 2 rendered page 6. Not performed: No experiments rerun or data/code verification

[arXiv v1, 2026-02-05](https://arxiv.org/pdf/2602.05975v1)
<!-- EVIDENCE:reading:END -->

<!-- EVIDENCE:placement:START -->
## What changes relative to nearby evaluations

The following is an editorial protocol comparison, not an assertion of direct inheritance unless stated.

Compared with BRIGHT’s fixed relevance retrieval, SAGE separates target-paper identification from open-set scholarly discovery and supplies an agent search interface. Set recall highlights omissions but needs precision and completeness checks before supporting exhaustive reviews.
<!-- EVIDENCE:placement:END -->

<!-- EVIDENCE:method:START -->
## Task and evidence construction

Each of four domains contributes 150 short-form and 150 open-ended queries, totaling 1,200. GPT-5-mini generates questions from paper metadata, figure/table details and relationships between papers sharing at least four references. Short-form queries identify a single seed paper; open-ended gold sets contain two seed papers and their shared references. Short-form scoring checks whether the target paper appears in response text or citations. Open-ended scoring assigns weight two to the seeds and one to shared references, dividing the returned relevant weight by total gold weight. The corpus expands these papers and their references with open-access papers from 2020 onward. Experiments separate native commercial web search from DR Tulu using MCP retrieval over a fixed paper corpus.
<!-- EVIDENCE:method:END -->

<!-- EVIDENCE:setup:START -->
## Conditions needed to interpret the results

Each question type has 600 queries, 150 per domain. Fixed-corpus runs use DR Tulu/vLLM with at most ten searches and return five or ten paper titles/abstracts per call; dense indexes encode the first 32,000 Markdown tokens. Web GPT-5 models use medium effort and Gemini dynamic thinking. Corpus augmentation adds bibliographic metadata and eight Qwen3-Next-80B-A3B-Instruct keywords. Table 1 domain counts sum to 186,669 for short-form corpora and 180,886 for open-ended corpora; overlap is unspecified, so 200,000 is not a verified exact union.
<!-- EVIDENCE:setup:END -->

<!-- EVIDENCE:result-1:START -->
## Question-type reversal with the same agent

600 queries per question type; DR Tulu, top ten results, at most ten search iterations. Scores are four-domain mean percentages and searches are per-query means.

| Retriever | Short EM | Open weighted recall | Short searches | Open searches |
|---|---|---|---|---|
| BM25 | 81.2 | 30.7 | 6.42 | 4.17 |
| gte-Qwen2-7B-instruct | 63.0 | 33.0 | 5.88 | 4.54 |
| ReasonIR | 49.3 | 26.2 | 7.51 | 4.44 |

Source: Table 2, corpus-search block · [Paper](https://arxiv.org/pdf/2602.05975v1)
<!-- EVIDENCE:result-1:END -->

<!-- EVIDENCE:result-2:START -->
## Conditional gains from corpus augmentation

600 queries per type with DR Tulu, top five results and at most ten searches fixed; both columns are percentages and differences are percentage points; augmentation preprocessing cost is not reported.

| BM25 corpus | Short EM | Open weighted recall |
|---|---|---|
| Before augmentation | 75.8 | 25.52 |
| After augmentation | 83.98 | 27.25 |

Source: Table 4; Section 5 · [Paper](https://arxiv.org/pdf/2602.05975v1)
<!-- EVIDENCE:result-2:END -->

<!-- EVIDENCE:interpretation:START -->
## What the comparisons establish

BM25’s advantage depends on question type. With DR Tulu and top ten results fixed, short-form EM is 81.2 for BM25, 63.0 for gte-Qwen and 49.3 for ReasonIR. On open-ended queries, however, gte-Qwen reaches 33.0 weighted recall versus BM25’s 30.7. Corpus augmentation raises top-five BM25 short-form EM from 75.80 to 83.98, an 8.18-percentage-point gain, while open-ended recall rises only from 25.52 to 27.25. These conditional results do not establish a universal sparse-over-dense ranking across deep-research agents.
<!-- EVIDENCE:interpretation:END -->

<!-- EVIDENCE:limitations:START -->
## Limits, source discrepancies and next test

Open-ended gold sets come from two seeds and their shared citations rather than exhaustive expert search: useful unlisted papers receive no credit, and recall does not penalize extra irrelevant papers. Short-form EM allows the target to appear in a long citation list and is not answer-quality scoring. Indexes see near-full papers while agents receive only titles and abstracts, introducing parsing and visibility factors. Keyword-query mismatch is a case-supported explanation, not established causality; the natural-language SearchR1 supplement still favors BM25 on short-form queries. Next, fix visible text and budgets, intervene on query wording, expand gold sets with human review, and report precision and paper-identity normalization.

The reviewed v1 describes GPT-5-mini query generation, without an expert-authorship or comprehensive human-validation protocol. The headline says 200,000 papers, while Table 1 gives smaller domain-specific counts and different short/open collections. Exact union size cannot be reconstructed from the paper. The abstract/conclusion generalize BM25 superiority by about 30%; Table 2 reverses the BM25 versus gte-Qwen ranking on open-ended questions. The keyword prompt uses content[:20000] without specifying whether this is characters or tokens; do not silently call it a 20,000-token context. Appendix A.4 causal explanations about BrowseComp-Plus document-prefix encoding are cross-paper hypotheses, not controlled ablations in SAGE.
<!-- EVIDENCE:limitations:END -->

Related benchmarks: [autoresearchbench](autoresearchbench.en.md) · [scholarquest](scholarquest.en.md)
