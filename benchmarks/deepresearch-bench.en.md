# DeepResearch Bench: evaluating research artifacts, evidence, and citations

<!-- RELEASE-REFERENCE:START -->
> **Release result (historical reference; not a best claim)** · 2025-06-13 · paper v1 snapshot<br>
> **Gemini-2.5-Pro Deep Research — RACE Overall: 48.88** (Deep Research Agent · RACE Overall); **Perplexity Deep Research — Citation Accuracy: 90.24%** (Deep Research Agent · Citation Accuracy)<br>
> Selected original-track results; metrics, subsets, and systems are not pooled into one winner. [Original source](https://arxiv.org/abs/2506.11763)<br>
> From a previously curated original-paper record, for historical reference; not rerun in this update and not current SOTA.
<!-- RELEASE-REFERENCE:END -->

[中文](deepresearch-bench.md) | **English** · [Benchmark Library](../library/README.en.md)

<!-- EVIDENCE:reading:START -->
## Reading scope and version

Reviewed the stated primary paper in full for methods, experimental setup, results and limitations; no independent reproduction.

Read Sections 1–6; appendices inspected: A–H, including limitations, metric formulas, collection dates, search configurations and all supplied prompt templates; visual checks: Table 2 checked on rendered page 8. Not performed: No experiments rerun or implementation audit; prompt templates contain author-provided ellipses

[arXiv v1 — arXiv v1, 2025-06-13; PDF front matter dated 2025-06-16](https://arxiv.org/pdf/2506.11763v1)
<!-- EVIDENCE:reading:END -->

<!-- EVIDENCE:placement:START -->
## What changes relative to nearby evaluations

The following is an editorial protocol comparison, not an assertion of direct inheritance unless stated.

Unlike BrowseComp’s short-answer fact finding, this evaluates long-report content, organization and citation support. The axes are complementary: finding a fact does not prove report coverage, and relative report quality does not replace verifiable QA correctness.
<!-- EVIDENCE:placement:END -->

<!-- EVIDENCE:method:START -->
## Task and evidence construction

DeepSeek-V3-0324 filtered 96,147 anonymized search-chat queries to 44,019 research requests and categorized them into 22 domains. Experts then authored 100 tasks, evenly split between Chinese and English. RACE removes citation formatting, generates task-specific dimension weights and detailed criteria, and asks Gemini 2.5 Pro to score the target and a Gemini Deep Research reference report together. Its final score divides the target weighted score by the sum of target and reference scores. FACT extracts and deduplicates statement–URL pairs, retrieves pages through Jina Reader and uses Gemini 2.5 Flash to judge support. Citation accuracy averages per-task proportions, assigning zero to tasks without citations. Effective citations count supported statement–URL pairs per task, rather than distinct sources.
<!-- EVIDENCE:method:END -->

<!-- EVIDENCE:setup:START -->
## Conditions needed to interpret the results

Main evaluation covers 100 tasks, fifty per language. RACE uses Gemini 2.5 Pro Preview, FACT Gemini 2.5 Flash, and references come from Gemini Deep Research in April 2025. Output collection spans April 1–May 8 for OpenAI, April 27–29 for Gemini, April 1–29 for Perplexity and April 27–29 for Grok, all in 2025. Search-enabled LLMs use high search context, 16,000 thinking tokens, up to five search turns and 36,000 output tokens or native maximum where configurable. These settings do not establish matched budgets for opaque commercial DRAs. Human validation covers fifty Chinese tasks, four systems and three raters; filtered task-level correlations retain only 37 tasks.
<!-- EVIDENCE:setup:END -->

<!-- EVIDENCE:result-1:START -->
## Report quality, citation precision and quantity

Across 100 tasks; RACE is relative quality ×100, citation accuracy is the macro-average of per-task percentages, and effective citations are supported statement–URL pairs per task.

| System | RACE overall | Citation accuracy | Effective citations/task |
|---|---|---|---|
| Gemini-2.5-Pro Deep Research | 48.88 | 81.44 | 111.21 |
| OpenAI Deep Research | 46.98 | 77.96 | 40.79 |
| Perplexity Deep Research | 42.25 | 90.24 | 31.26 |

Source: Table 1; Sections 3–4; Appendix E · [Paper](https://arxiv.org/pdf/2506.11763v1)
<!-- EVIDENCE:result-1:END -->

<!-- EVIDENCE:result-2:START -->
## Scoring method agreement with humans

All values are expressed as percentages; human evaluation covers 50 Chinese tasks, four systems and three experts per task. Overall correlation uses four system means, filtered correlation uses the 37 tasks with ICC≥0, and pairwise aggregation has the reporting ambiguity noted below.

| Method | Pairwise agreement | Overall Pearson | Filtered mean Pearson |
|---|---|---|---|
| Vanilla Prompt | 58.89 | 98.89 | 40.3 |
| RACE Full | 71.33 | 99.54 | 60.24 |
| No Reference | 66.56 | 97.46 | 57.51 |

Source: Table 2; Section 4.3; Appendix F · [Paper](https://arxiv.org/pdf/2506.11763v1)
<!-- EVIDENCE:result-2:END -->

<!-- EVIDENCE:interpretation:START -->
## What the comparisons establish

A RACE score of 48.88 is not 48.88% task accuracy: it is report quality relative to a reference. Gemini produces more effective citations but lower citation accuracy than Perplexity, separating supported information quantity from precision. RACE improves agreement with human preferences over direct scoring, but overall Pearson correlation is computed across only four system means. Its 99.54 value is not report-level accuracy, and task-level correlations exclude 13 low-consensus tasks.
<!-- EVIDENCE:interpretation:END -->

<!-- EVIDENCE:limitations:START -->
## Limits, source discrepancies and next test

The benchmark has only 100 tasks, and human validation covers 50 Chinese tasks. Both reference reports and the principal judge come from the Gemini family, motivating independent judges and reference sensitivity checks. FACT evaluates cited statement–URL pairs; it does not directly measure hallucinations in uncited claims or recall against all required facts. Commercial systems differ in collection dates and opaque internal budgets. A useful next experiment fixes evidence, length, dates and budget, swaps references and judges, and reports unfiltered correlations plus claim-level coverage audits.

Appendix A describes 600 reports, but 50 tasks × four agents yields 200 distinct reports and 600 ratings when three annotators are included. Appendix F defines pairwise agreement over 50 × 6 = 300 report pairs, yet Table 2 values such as 58.89% are not increments of 1/300; aggregation or repeat details are insufficient to reconcile this. The prompt appendix contains ellipses rather than complete executable templates; the number T of dimension-weight trials is not specified in the reviewed paper. FACT validation reports 96% support and 92% non-support agreement on 100 pairs, without class-specific denominators or full confusion matrix.
<!-- EVIDENCE:limitations:END -->

Related benchmarks: [claimprobe](claimprobe.en.md) · [litreview-arena](litreview-arena.en.md)
