# EnterpriseRAG-Bench: enterprise RAG is about cross-source conflict, constraints, and knowing when information is absent

<!-- RELEASE-REFERENCE:START -->
> **Best at release (not yet verified)** · Benchmark recorded date: 2026-04-14<br>
> A best result tied to a model, metric, and protocol in the initial release has not yet been verified. [Original source](https://arxiv.org/abs/2605.05253)<br>
> No substitution from a live board, a single baseline, or a later paper; unknown is neither zero nor a claim that the authors reported no results.
<!-- RELEASE-REFERENCE:END -->

[中文](enterpriserag-bench.md) | **English** · [Benchmark Library](../library/README.en.md)

<!-- EVIDENCE:reading:START -->
## Reading scope and version

Reviewed the stated primary paper in full for methods, experimental setup, results and limitations; no independent reproduction.

Read Sections 1–8, all evaluation and limitation discussion; appendices inspected: A–D, artifact/harness description, generation and question-type procedures, exact corpus and gold statistics. Not performed: No benchmark run, implementation audit or public leaderboard lookup

[arXiv v1, 2026-05-05](https://arxiv.org/pdf/2605.05253v1)
<!-- EVIDENCE:reading:END -->

<!-- EVIDENCE:placement:START -->
## What changes relative to nearby evaluations

The following is an editorial protocol comparison, not an assertion of direct inheritance unless stated.

Compared with public-web or single-source QA, this combines enterprise source types, conflicting versions, constraints and no-answer requests in one synthetic company. It measures work-document organization without testing permission enforcement or task execution.
<!-- EVIDENCE:placement:END -->

<!-- EVIDENCE:method:START -->
## Task and evidence construction

The synthetic Redwood Inference company begins with organizational, initiative, employee, directory and document-format scaffolds. High-coherence project documents form a core, while topic-controlled generation supplies background volume. Completeness questions distribute facts across four to ten mutually visible documents. Noise includes five percent random misfiling, three percent model-selected plausible misfiling, conflicting near-duplicates and informal files. The final 511,962 documents span nine enterprise source types and support 500 questions in ten categories. Questions are back-generated from documents, discovered through corpus tools or tied to designed document clusters; BM25, vector and Bash-agent pools help check gold labels. This is a synthetic enterprise-style file corpus, not live application interaction.
<!-- EVIDENCE:method:END -->

<!-- EVIDENCE:setup:START -->
## Conditions needed to interpret the results

BM25 uses an OpenSearch standard analyzer over concatenated text; vector search uses 3,072-dimensional text-embedding-3-large with Qdrant cosine similarity. Both return a fixed top ten. The GPT-5.4-low Bash agent iterates through directory tools for up to ten minutes and returns a variable number of documents. Answer generation and evaluation use GPT-5.4 medium throughout. Correctness is binary semantic alignment; completeness independently checks each atomic fact, after removing citation formatting. Document recall and invalid extras cover only the 470 questions with gold IDs, excluding ten High Level and twenty Info Not Found questions. Leaderboard scores average per-question completeness gated by correctness, not the product of two overall means.
<!-- EVIDENCE:setup:END -->

<!-- EVIDENCE:result-1:START -->
## Separate correctness from completeness

Answer metrics cover 500 tasks; invalid extras apply only to 470 tasks with gold IDs and count documents rather than a proportion. BM25 returns ten, while Bash has up to ten minutes and variable output volume; GPT-5.4 medium generates/judges.

| System | Correctness percent | Completeness percent | Invalid extra documents |
|---|---|---|---|
| BM25 | 68.8 | 56.0 | 9.0 |
| Bash Agent | 60.6 | 61.1 | 2.0 |

Source: Table 6; Section 6.1 · [Paper](https://arxiv.org/pdf/2605.05253v1)
<!-- EVIDENCE:result-1:END -->

<!-- EVIDENCE:result-2:START -->
## Completeness tasks: more recall need not mean correctness

Twenty completeness questions with an average of 6.5 gold documents, range two to ten. Percentages measure gold-set recall and final-answer correctness, with unequal system budgets.

| System | Correctness percent | Document recall percent |
|---|---|---|
| BM25 | 40.0 | 46.5 |
| Bash Agent | 35.0 | 59.0 |

Source: Table 7, Completeness row · [Paper](https://arxiv.org/pdf/2605.05253v1)
<!-- EVIDENCE:result-2:END -->

<!-- EVIDENCE:interpretation:START -->
## What the comparisons establish

BM25 correctness, 68.8%, exceeds the Bash agent’s 60.6%, while Bash completeness, 61.1%, exceeds BM25’s 56.0% and includes fewer invalid extra documents. On the twenty completeness questions, Bash recall is higher, 59.0% versus 46.5%, but correctness is lower, 35.0% versus 40.0%. More required documents do not guarantee correct synthesis. Bash also has up to ten minutes of exploration rather than fixed top-ten retrieval, making this a system-level tradeoff rather than a matched-budget algorithm comparison.
<!-- EVIDENCE:interpretation:END -->

<!-- EVIDENCE:limitations:START -->
## Limits, source discrepancies and next test

A single technology company is simulated, and flattened JSON omits real thread trees, rich media and access-control constraints. Bulk background documents have weaker coherence than the high-fidelity core. Similar local embedding density to the authors’ Onyx sample does not establish broad realism. Pooling uses retrieval systems also evaluated as baselines, potentially influencing judgments. Perfect results on twenty missing-information questions do not establish robust abstention. The paper leaves true sequential clue discovery, multimodality, recency and people-centric questions to future work. Next, freeze gold versions, expand to independent enterprise corpora and blinded human review, and match latency/token budgets.

Constrained questions are described as requiring exactly one gold document in Sections 2/4.4/C.2, but Table 11 and Appendix D.3 report a mean of 1.4, range one to two. Treat the exact gold-file snapshot as authoritative when reproducing. Section 5 discusses correction-aware scoring, while the explicit leaderboard note freezes gold within a release; distinguish experimental comparative correction from published within-version leaderboard scoring. The headline approximately 500,000 and Table 1 approximate source counts differ from exact released total 511,962 in Table 9; use the exact total for reproducibility. High Level generation explicitly does not guarantee every question is fully answerable from the released document set, despite references being produced from company scaffolding.
<!-- EVIDENCE:limitations:END -->

Related benchmarks: [gatemem](gatemem.en.md) · [mudabench](mudabench.en.md)
