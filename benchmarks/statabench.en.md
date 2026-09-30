# StatABench: statistical judgment, tools and reports

<!-- RELEASE-REFERENCE:START -->
> **Best at release (not yet verified)** · Benchmark recorded date: 2026-06-22<br>
> A best result tied to a model, metric, and protocol in the initial release has not yet been verified. [Original source](https://arxiv.org/abs/2606.22977)<br>
> No substitution from a live board, a single baseline, or a later paper; unknown is neither zero nor a claim that the authors reported no results.
<!-- RELEASE-REFERENCE:END -->

[中文](statabench.md) | **English** · [Home](../README.en.md) · [Benchmark Library](../library/README.en.md)

<!-- EVIDENCE:reading:START -->
## Reading coverage and versions

Full substantive paper and appendix reading completed for the stated primary version; experiments were not independently reproduced.

Read the complete 28-page PDF: main text, Appendices A–I, all prompts, toolkit functions and both embedded generated reports. The text extraction contains an extra page-break character; physical page count is 28.

[arXiv 2606.22977v1 · 2026-06-22](https://arxiv.org/pdf/2606.22977v1)
<!-- EVIDENCE:reading:END -->

<!-- EVIDENCE:method:START -->
## What the method measures

Stat-Closed contains 404 questions, including 198 practical tasks using a 35-function toolkit. Stat-Open contains 30 report-producing modeling tasks. Closed grading mixes exact checks and semantic judgments; open reports receive rubric scores rather than execution-success labels.

<!-- EDITORIAL-METHOD:START -->
Closed tasks separate conceptual judgment from practical statistical-tool use; open tasks require modeling, analysis and a report. An illustrative workflow checks assumptions for two sample groups, selects a statistical function and interprets effect and uncertainty, while an open report must justify the method. This exposes gaps between concepts and tool execution but also introduces report-judge preferences. The 198 practical tasks are a subset of the 404 closed tasks, not an additional corpus.

Editorial placement: relative to DS-1000’s functional code checks, StatABench covers conceptual choice, statistical tools and open reports. StatFormBench isolates pre-execution formulation. The added coordinate is statistical judgment rather than merely runnable analysis code.
<!-- EDITORIAL-METHOD:END -->
<!-- EVIDENCE:method:END -->

<!-- EVIDENCE:setup:START -->
## Experimental setup

Evaluation uses temperature 0; Qwen3-8B thinking is disabled. The limit is five tool calls per interaction turn, with no clear overall runtime cap. Open comparisons share DeepSeek-V3 and use Gemini 3 Pro as judge.
<!-- EVIDENCE:setup:END -->

<!-- EVIDENCE:results:START -->
## Selected quantitative evidence

V1 Tables 3–5, printed pp. 7–8. Closed values are question accuracy; open values are judge/human rubric points. Do not pool these metrics.

| System / comparison | Dataset / denominator | Metric / unit | Result | Conditions | Source |
| --- | --- | --- | --- | --- | --- |
| GPT-5.1 + LangChain MCP | Stat-Closed; 404 questions | Accuracy (%) | 68.6% | T=0; SAToolKit | Table 3, p. 7 |
| DeepSeek-V3 + LangChain MCP | Practical subset; 198 questions | Accuracy (%) | 53.54% | T=0; shared toolkit | Table 4, p. 7 |
| DeepSeek-V3 + CrewAI | Practical subset; 198 questions | Accuracy (%) | 85.35% | T=0; changed scaffold | Table 4, p. 7 |
| DeepSeek-V3 + MathModelAgent | Stat-Open; 30-task suite; human subset count unclear | Mean judge / human rubric score (0–100) | 61.86 / 61.17 | Gemini 3 Pro; seven criteria | Table 5, p. 8 |
| DeepSeek-V3 + LLM-MM-Agent | Stat-Open; 30-task suite; human subset count unclear | Mean judge / human rubric score (0–100) | 54.29 / 52.62 | Gemini 3 Pro; seven criteria | Table 5, p. 8 |

Fact source: [Table 3, p. 7; Table 4, p. 7; Table 5, p. 8](https://arxiv.org/pdf/2606.22977v1)
<!-- EVIDENCE:results:END -->

<!-- EVIDENCE:limitations:START -->
## Limits and interpretation

The practical/fundamental gap compares different tasks, not a tool-use ablation. Table 5 averages seven displayed criteria despite four high-level rubric dimensions. Human subset size and rater counts are unclear; MathModelAgent’s Practical Science agreement is only κ=0.092. Perturbation-based filtering does not prove decontamination.

<!-- EDITORIAL-NEXT:START -->
Next, express identical statistical problems as conceptual questions, tool tasks and reports under matched models/budgets. Independent statisticians should blind-review assumptions, effect interpretation and error control to separate knowledge, interface and report-scoring failures.
<!-- EDITORIAL-NEXT:END -->
<!-- EVIDENCE:limitations:END -->
