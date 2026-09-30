# InsightBench: insight discovery and coverage in multi-step business analysis

<!-- RELEASE-REFERENCE:START -->
> **Best at release (not yet verified)** · Benchmark recorded date: 2024-07<br>
> A best result tied to a model, metric, and protocol in the initial release has not yet been verified. [Original source](https://arxiv.org/abs/2407.06423)<br>
> No substitution from a live board, a single baseline, or a later paper; unknown is neither zero nor a claim that the authors reported no results.
<!-- RELEASE-REFERENCE:END -->

[中文](insightbench.md) | **English** · [Home](../README.en.md)

<!-- EVIDENCE:reading:START -->
## Reading coverage and version

Read the stated version’s complete main text and available appendices and checked the selected results; no independent experiment reproduction.

Read all 33 pages of v4 and Appendices A–D, including all ten prompt templates; checked Table 1.

[arXiv 2407.06423v4 · 2025-02-27](https://arxiv.org/pdf/2407.06423v4)
<!-- EVIDENCE:reading:END -->

<!-- EVIDENCE:method:START -->
## Method and measurement target

InsightBench’s 100 synthetic business datasets use ServiceNow-inspired schemas and contain 475 planted reference insights. AgentPoirot inspects schemas, develops three root questions with four follow-ups each, and summarizes up to fifteen insights. Python and custom cba tools support analysis and plotting. Controls include a modified iterative Pandas Agent and the same AgentPoirot framework with a generic goal.

[Source](https://arxiv.org/pdf/2407.06423v4)

<!-- EDITORIAL-METHOD:START -->
Editorial placement: fixed-question data QA specifies the target answer; InsightBench lets agents propose analyses around a business objective. It adds exploration and insight coverage. Soft matching to reference insights does not establish causal discovery, business value or exhaustive annotation. DDR-Bench offers another hidden-fact-coverage reference.
<!-- EDITORIAL-METHOD:END -->
<!-- EVIDENCE:method:END -->

<!-- EVIDENCE:setup:START -->
## Scoring and experimental conditions

Experiments use temperature 0 and report means and standard deviations across five seeds. LLaMA-3-70B selects the best matching prediction for each reference insight and separately grades summaries. This is reference-based soft similarity, not bidirectional precision/recall or business impact. Judge prompts use 1–10 while tables report normalized soft scores. Matched token or wall-clock caps are not given.

[Source](https://arxiv.org/pdf/2407.06423v4)
<!-- EVIDENCE:setup:END -->

<!-- EVIDENCE:result-1:START -->
## Selected GPT-4o controls, Table 1

100 datasets and 475 reference insights; GPT-4o; mean ± standard deviation across five seeds, not confidence intervals; AgentPoirot produces up to fifteen insights; LLaMA-3-70B judge; no matched token/time cap.

| Agent / condition | Insight LLaMA-3-Eval (mean±SD) | Summary LLaMA-3-Eval (mean±SD) |
| --- | --- | --- |
| Pandas Agent / GPT-4o | 0.54±0.01 | 0.40±0.04 |
| AgentPoirot / GPT-4o | 0.60±0.03 | 0.44±0.03 |
| AgentPoirot / GPT-4o / Generic goal | 0.40±0.03 | 0.33±0.12 |

Source location: §2.2,§3.1–3.2, Table 1 PDFp8; AppendixD Prompts1–10 · [Source](https://arxiv.org/pdf/2407.06423v4)
<!-- EVIDENCE:result-1:END -->

<!-- EVIDENCE:limitations:START -->
## Interpretation, source limitations and next experiment

Specific goals outperform generic ones, but one metric’s advantage does not extend to every metric: on GPT-4o insight ROUGE-1, Pandas Agent scores 0.35 and AgentPoirot 0.32. Synthetic trends and reference coverage limit generalization to open business discovery.

Hardware descriptions conflict: one section gives four A100s while reproducibility gives two 80 GB A100s; no uniform configuration is inferred.

Fix insight counts and compute, add no-planted-trend data and previously unknown trends, and blind-review evidence, correctness and value. Separate reference coverage from false-discovery rates.

[Source](https://arxiv.org/pdf/2407.06423v4)
<!-- EVIDENCE:limitations:END -->
