# MemoryAgentBench: separating memory tasks and budget conditions

<!-- RELEASE-REFERENCE:START -->
> **Best at release (historical reference)** · 2025-07 · paper v1<br>
> **NV-Embed-v2 RAG / GPT-4o-mini — RULER-QA: 83.0**; **Contriever RAG / GPT-4o-mini — FactCon-MH accuracy: 7.0%**<br>
> Best configurations for two selected subtasks in main Table 2; different capabilities are not reduced to a synthetic overall score. [Original source](https://arxiv.org/html/2507.05257v1)<br>
> Table 2 scope only, excluding later ablations. Its 7.0 multi-hop conflict entry differs from the prose claim of at most 6.
<!-- RELEASE-REFERENCE:END -->

[中文](memoryagentbench.md) | **English**

<!-- EVIDENCE:reading:START -->
## Reading coverage and version

Reviewed the stated paper version, method, experimental setup, key results and limitations; no independent reproduction.

Substantive main 1–5 and Appendices A–L read; PDF Figures 4–5 prompt text checked. No reruns; plotted curves use tabular counterparts.

[arXiv 2507.05257v4 (2026-06-28)](https://arxiv.org/html/2507.05257v4)

[Supplementary source 2507.05257v4, inspected 2026-09-30](https://arxiv.org/pdf/2507.05257v4)

The frozen release reference is preserved; newer paper results do not replace initial-release scores.
<!-- EVIDENCE:reading:END -->

<!-- EVIDENCE:method:START -->
## How tasks create memory demands

Convert source tasks into ordered chunks with memorization instructions, then evaluate retrieval, learning from examples, global understanding and conflict updates. FactConsolidation gives newer counterfactual facts larger serial numbers.

Editorial placement: Relative to conversational QA such as LongMemEval, MemoryAgentBench feeds incremental chunks and expands to retrieval, test-time learning, long-range understanding and selective forgetting. Different source tasks and metrics require subtask interpretation rather than a single memory-capacity claim. This is an evaluation-coordinate comparison, not a claim of direct dataset inheritance.
<!-- EVIDENCE:method:END -->

<!-- EVIDENCE:setup:START -->
## Experimental settings and scoring targets

2,071 questions across heterogeneous tasks. Default RAG/backbone GPT-4o-mini; most synthetic QA/SF chunks 512, other tasks 4096; Mem0/Cognee/Zep/MIRIX always 4096. Usually top 10 retrieval. LME(S*) is 300 questions on 5 reconstructed histories, not original LongMemEval-S.
<!-- EVIDENCE:setup:END -->

<!-- EVIDENCE:result-1:START -->
## A shared answerer has different strengths across tasks

QA/SF substring-match accuracy; MCC mean classification accuracy. Same default answerer, different memory/evidence budgets. No cross-task overall ranking.

QA 100; MCC5 datasets×100; FC-SH 100/FC-MH 100, each one 262K-token stream

| System | SH-Doc QA (%) | MCC (%) | FactCon-SH (%) | FactCon-MH (%) |
|---|---|---|---|---|
| GPT-4o-mini (128K) | 64.0 | 82.0 | 45.0 | 5.0 |
| BM25 / GPT-4o-mini | 66.0 | 75.4 | 48.0 | 3.0 |
| HippoRAG-v2 / GPT-4o-mini | 76.0 | 61.4 | 54.0 | 5.0 |

Locator: v4 Table 3, selected subtask scores · [Source](https://arxiv.org/html/2507.05257v4)
<!-- EVIDENCE:result-1:END -->

<!-- EVIDENCE:result-2:START -->
## Matching processed tokens does not match all costs

Banking77 accuracy; fluency-weighted summary F1 on paper scale. Matched processed-token budget; low retrieval top 1, high enlarged retrieval. Forward passes not matched; distinct subset from main 100 summaries.

Banking77 task 100 questions; summary random 30-book subset

| System | Banking77 4K (%) | Banking77 104K (%) | Summary 113K score |
|---|---|---|---|
| Long-Context / GPT-4.1-mini | 74.0 | 93.0 | 39.7 |
| BM25 / GPT-4.1-mini | 83.0 | 88.0 | 38.0 |
| MIRIX / GPT-4.1-mini | 52.0 | 67.0 | 38.8 |

Locator: v4 Table 18, Appendix J · [Source](https://arxiv.org/html/2507.05257v4)
<!-- EVIDENCE:result-2:END -->

<!-- EVIDENCE:result-3:START -->
## Update prompts do not automatically solve forgetting

 Prompt policy intervention; conservative rule changes acceptance policy and may mismatch latest-fact gold labels.

100 questions per SF task; main long-stream configuration

| System | FactCon-SH (%) | FactCon-MH (%) |
|---|---|---|
| GPT-4.1-mini / baseline | 36.0 | 5.0 |
| GPT-4.1-mini / always prefer later | 40.0 | 4.0 |
| GPT-4.1-mini / explicit-negation only | 28.0 | 4.0 |

Locator: v4 Table 19 · [Source](https://arxiv.org/html/2507.05257v4)
<!-- EVIDENCE:result-3:END -->

<!-- EVIDENCE:limitations:START -->
## Limits and next validation

Profiles differ across tasks and evidence budgets. Shared prompts do not establish architecture causality. Short-context solvability does not isolate failure mechanisms in long streams. Costs exclude indexing and assume historical caching prices.

Appendix H/Table 16 calls MCC Banking77 but reports 82.0 full-context, while Table 7 Banking77=93.0 and five-task mean=82.0; exclude unresolved zero-shot comparison. Table 16 calls all metrics accuracy; recommendation is Recall@5 per Appendix B.2.2. Summary prompt asks 1000–1200 words but maximum output budget Table 14 is 1200 tokens. Table 3 GPT-4o-mini duplicate overall 42.2/42.3; avoid overall. EventQA HippoRAG-v2 Table 3=67.6 but Table 9 top 10=67.4; use source-specific values.

Next: Match backbone, chunking, retrieval and lifecycle compute; compare incremental versus deferred indexing. Audit stored obsolete facts separately from latest-answer accuracy; pair with MemProbe for preserve/update discrimination.
The protocol ingests chunks before held-out QA; §3.2 permits structured RAG to build its structure after all chunks arrive. Selective forgetting scores latest-fact answers without verifying storage deletion.
<!-- EVIDENCE:limitations:END -->
