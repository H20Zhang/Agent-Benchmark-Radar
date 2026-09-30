# BRIGHT: when relevance itself requires reasoning

<!-- RELEASE-REFERENCE:START -->
> **Best at release (not yet verified)** · Benchmark recorded date: 2024-07<br>
> A best result tied to a model, metric, and protocol in the initial release has not yet been verified. [Original source](https://arxiv.org/abs/2407.12883)<br>
> No substitution from a live board, a single baseline, or a later paper; unknown is neither zero nor a claim that the authors reported no results.
<!-- RELEASE-REFERENCE:END -->

[中文](bright.md) | **English** · [Benchmark Library](../library/README.en.md)

<!-- EVIDENCE:reading:START -->
## Reading scope and version

Reviewed the stated primary paper in full for methods, experimental setup, results and limitations; no independent reproduction.

main sections 1–6; Appendices A–I, construction/annotation instructions, examples and prompts; Tables 1–49; Table 2 visually verified; PDF filled mirror truncation after Table 18

[arXiv v4 (2025-03-26) — v4,2025-03-26, ICLR 2025; NOT initial-release result](https://arxiv.org/pdf/2407.12883v4)
<!-- EVIDENCE:reading:END -->

<!-- EVIDENCE:placement:START -->
## What changes relative to nearby evaluations

The following is an editorial protocol comparison, not an assertion of direct inheritance unless stated.

Compared with BEIR’s heterogeneous zero-shot retrieval, BRIGHT makes relevance depend specifically on solving the query rather than topical or lexical similarity. It targets reasoning-dependent relevance; conversational agents and downstream QA still require separate controls.
<!-- EVIDENCE:placement:END -->

<!-- EVIDENCE:method:START -->
## Task and evidence construction

1384 queries span 12 tasks: seven StackExchange domains use cited and verified evidence; coding/math relevance follows algorithms, syntax or shared theorems. Topically similar negatives are unhelpful; some query-specific candidate exclusions reduce false negatives.
<!-- EVIDENCE:method:END -->

<!-- EVIDENCE:setup:START -->
## Conditions needed to interpret the results

This note uses v4: 1,384 queries across twelve tasks, with equally weighted dataset-macro nDCG@10×100. SFR is SFR-Embedding-Mistral with a 4,096-token limit; Qwen is gte-Qwen1.5-7B-instruct with 8,192 tokens. Reranking compares MS-MARCO MiniLM-L12 with gpt-4-0125-preview, retaining candidate counts. Downstream QA covers only seven StackExchange domains; Claude 3.5 Sonnet both generates and scores reference-content coverage, rather than binary answer accuracy.
<!-- EVIDENCE:setup:END -->

<!-- EVIDENCE:result-1:START -->
## Raw-query ranking

Macro nDCG@10 on a 0–100 scale across 12 datasets; v4 contains 1,384 queries and weights datasets equally.

| System | Score |
|---|---|
| BM25 | 14.5 |
| SFR | 18.3 |
| Qwen | 22.5 |

Source: Table 2 · [Paper](https://arxiv.org/pdf/2407.12883v4)
<!-- EVIDENCE:result-1:END -->

<!-- EVIDENCE:result-2:START -->
## Separate reranking experiment block

Macro nDCG@10 on a 0–100 scale across 12 datasets; this separate experiment block uses a BM25 baseline of 14.3, which must not be mixed with Table 2’s 14.5.

| BM25 reranker | Candidate_k | Score |
|---|---|---|
| None | — | 14.3 |
| MiniLM-L12 | 100 | 8.3 |
| GPT-4 | 10 | 17.4 |

Source: Table 3/Table 41 · [Paper](https://arxiv.org/pdf/2407.12883v4)
<!-- EVIDENCE:result-2:END -->

<!-- EVIDENCE:result-3:START -->
## Initial downstream evaluation

Mean reference-content coverage score on a 0–100 scale over seven StackExchange domains; Claude 3.5 Sonnet generates and judges, with domain query counts in the dataset table; this is not binary accuracy.

| Retrieval | Average |
|---|---|
| None | 77.7 |
| Qwen | 79.6 |
| Oracle | 81.8 |

Source: Table 4, Table 46 · [Paper](https://arxiv.org/pdf/2407.12883v4)
<!-- EVIDENCE:result-3:END -->

<!-- EVIDENCE:interpretation:START -->
## What the comparisons establish

The paper includes initial downstream QA; do not say evidence use is wholly untested. Same-model generation/grading and coverage rubrics do not prove independent factual accuracy or agent-policy causality.
<!-- EVIDENCE:interpretation:END -->

<!-- EVIDENCE:limitations:START -->
## Limits, source discrepancies and next test

Relevance remains subjective; GritLM continuation tests one leakage condition without query-document mappings. Next: fixed candidates, version and compute, with separate retrieval/answer evaluation.

v1:1398 queries/SFR 18.0; v4:1384/SFR 18.3. v4 Table 2 best row 22.5; caption/text say 24.3. Raw BM25 Table 2=14.5; rerank baseline Table 3/41=14.3. Keep blocks separate. Table 46 places predicted_answer in PROBLEM as well as STUDENT ANSWER; implementation verification required. Table 6 and Table 39 differ for some long-context averages (e.g. OpenAI 21.9 vs 21.3).
<!-- EVIDENCE:limitations:END -->

Related benchmarks: [beir](beir.en.md) · [bright-pro](bright-pro.en.md)
