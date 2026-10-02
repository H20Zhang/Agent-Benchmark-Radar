# ClaimProbe: read faithfulness gains with quality and writing cost

<!-- RELEASE-REFERENCE:START -->
> **Best at release (not yet verified)** · Benchmark recorded date: 2026-08-12<br>
> A best result tied to a model, metric, and protocol in the initial release has not yet been verified. [Original source](https://arxiv.org/abs/2608.28643)<br>
> No substitution from a live board, a single baseline, or a later paper; unknown is neither zero nor a claim that the authors reported no results.
<!-- RELEASE-REFERENCE:END -->

[中文](claimprobe.md) | **English** · [Home](../README.en.md) · [Benchmark Library](../library/README.en.md)

<!-- EVIDENCE:reading:START -->
## Reading coverage and version

Reviewed the stated primary-paper version, method, setup, key results and limitations; no independent experiment reproduction.

v1 main Sections 1–8, limitations and Appendices A–F, including PDF judge/extractor prompts; no system rerun or line-by-line audit of the full released extractor.

[arXiv:2608.28643v1](https://arxiv.org/html/2608.28643v1)

The tables reorganize selected sourced facts. The title-level historical reference may use a different version, split or model; do not pool scores across those settings.
<!-- EVIDENCE:reading:END -->

<!-- EVIDENCE:method:START -->
## Measurement, method and comparison

Hold evidence fixed; replace writing with query-first outline, extracted/deduplicated facts, topic assignment and section drafting. Audit claims and highly relevant source facts bidirectionally through top 20 candidates; default metrics accept partial support.

[Primary source](https://arxiv.org/html/2608.28643v1)
<!-- EVIDENCE:method:END -->

<!-- EVIDENCE:setup:START -->
## Experimental settings and denominators

Hosts are EDR, AI-Q and ODR; writers use GPT-5.5 and keep retrieved evidence fixed within a host comparison. Main ClaimProbe auditing uses GPT-5.4-mini on 100 tasks, text-embedding-3-small and top-20 candidates in each direction, with micro-averaged pooled numerators/denominators. Hall uses all report claims, Mis cited claims and Rec highly relevant source facts. RACE uses GPT-5.5, but Table 1 says n=100 while methods say 50 English tasks; the discrepancy is unresolved.

[Setup source](https://arxiv.org/html/2608.28643v1)
EDR is Enterprise Deep Research, AI-Q is NVIDIA AI-Q, and ODR is OpenDeepResearch. Hall measures report claims unsupported by retrieved sources; Mis measures cited claims whose cited source does not support them although another retrieved source does; Rec measures coverage of highly relevant source facts. Default metrics accept partial support; strict variants require full support.

<!-- EVIDENCE:setup:END -->

<!-- EVIDENCE:result-1:START -->
## Claim-level gains with fixed evidence

EDR host, GPT-5.5 writing, GPT-5.4-mini judging, 100-task micro-average; default metrics accept partial support, with strict variants separate.

| Writer | Hall (%, lower better) | Mis (%, lower better) | Rec (%, higher better) | Strict Hall (%, lower better) | Strict Rec (%, higher better) |
|---|---|---|---|---|---|
| Default | 15.89 | 18.94 | 36.83 | 54.05 | 13.67 |
| ClaimWriter | 5.02 | 5.43 | 45.85 | 28.55 | 24.48 |

This supports writer-side faithfulness gains with fixed sources, not improved retrieval coverage or a deployment-wide hallucination rate.

Fact source: Table 2, sections4–5.2 · [Source](https://arxiv.org/html/2608.28643v1)
<!-- EVIDENCE:result-1:END -->

<!-- EVIDENCE:result-2:START -->
## Holistic scores decline slightly in all three hosts

RACE with GPT-5.5 judging; the source's 50/100 task-count conflict is unresolved. Each row compares the original writer and ClaimWriter within one host.

| Host | Original Overall (0–1) | ClaimWriter Overall (0–1) | Original Readability (0–1) | ClaimWriter Readability (0–1) |
|---|---|---|---|---|
| EDR | 0.544 | 0.536 | 0.510 | 0.470 |
| AI-Q | 0.553 | 0.535 | 0.528 | 0.473 |
| ODR | 0.540 | 0.530 | 0.523 | 0.485 |

The interpretation is higher faithfulness alongside slightly lower overall scores and readability, not improved RACE scores.

Fact source: Table 1, section5.1 · [Source](https://arxiv.org/html/2608.28643v1)
<!-- EVIDENCE:result-2:END -->

<!-- EVIDENCE:result-3:START -->
## Initial writing is not budget-matched

EDR with GPT-5.5, per-report writing-stage averages; excludes search, tools, query generation and planning.

| Writer | Input tokens / report | Output tokens / report |
|---|---|---|
| Default | 1019276 | 92252 |
| ClaimWriter | 9697825 | 700626 |

Fact structure may reduce later update cost, but first-run writing is substantially more expensive. The update experiment has only five tasks, so universal amortization is not established.

Fact source: Table 7,AppendixE · [Source](https://arxiv.org/html/2608.28643v1)
<!-- EVIDENCE:result-3:END -->

<!-- EVIDENCE:limitations:START -->
## Limitations, remaining gaps and next experiment

Extraction, relevance labels and top-20 shortlists still affect judgments. Hall κ=0.484 uses unanimous human labels; agreement against majority labels is only 0.299. The appendix claims every post-update metric stays within ±1 percentage point, but Table 6 includes strict Hall 43.7→45.3; the discrepancy remains. Compared with holistic scoring, local audits expose different failures without automatically removing judge bias. Next, match writing budgets, audit shortlist misses/human labels and expand update tasks.

[Primary evidence](https://arxiv.org/html/2608.28643v1)
<!-- EVIDENCE:limitations:END -->

<!-- RESEARCH-DECISION:START -->

Use the method, comparisons and limitations together to decide whether this benchmark fits a claim. These tables are not a cross-protocol leaderboard; structural checks do not certify factual correctness or reproduction.

Related measurements and controls: [DeepResearch Bench](deepresearch-bench.en.md) · [LiveDRBench](livedrbench.en.md) · [Mr.LHDR](mr-lhdr.en.md)

<!-- RESEARCH-DECISION:END -->
