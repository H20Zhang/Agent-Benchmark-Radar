# GISA: web search can combine deterministic structured answers with complete human trajectories

<!-- RELEASE-REFERENCE:START -->
> **Best at release (not yet verified)** · Benchmark recorded date: 2026-02-06<br>
> A best result tied to a model, metric, and protocol in the initial release has not yet been verified. [Original source](https://arxiv.org/abs/2602.08543)<br>
> No substitution from a live board, a single baseline, or a later paper; unknown is neither zero nor a claim that the authors reported no results.
<!-- RELEASE-REFERENCE:END -->

[中文](gisa.md) | **English** · [Benchmark Library](../library/README.en.md)

<!-- EVIDENCE:reading:START -->
## Reading scope and version

Reviewed the stated primary paper in full for methods, experimental setup, results and limitations; no independent reproduction.

Read Sections 1–8, all quantitative analyses and limitations; appendices inspected: A–C, data format, prompts, tool schema and behavioral metric formulas. Not performed: No rerun, code audit or verification that monthly updates actually occurred

[arXiv v1 — arXiv v1, 2026-02-09, as printed in PDF](https://arxiv.org/pdf/2602.08543v1)
<!-- EVIDENCE:reading:END -->

<!-- EVIDENCE:placement:START -->
## What changes relative to nearby evaluations

The following is an editorial protocol comparison, not an assertion of direct inheritance unless stated.

Between BrowseComp’s short answers and DeepResearch Bench’s report quality, GISA requests normalizable sets, lists and tables. It makes broad information gathering deterministically comparable while exposing whole-table sensitivity to local errors.
<!-- EVIDENCE:placement:END -->

<!-- EVIDENCE:method:START -->
## Task and evidence construction

Fifteen graduate annotators specializing in information retrieval formulate browsing-inspired questions with explicit item, set, list or table structures and ordering constraints. They answer using Google only while logging searches, results and clicks; separate checks enforce consistency between answers and trajectories. Queries fully solved by DeepSeek-V3.2 without reasoning or search are excluded, leaving 373 tasks: 223 stable and 150 live. TSV outputs undergo case, whitespace and numeric normalization before whole-answer exact match. Additional metrics are set F1, list content F1 and SequenceMatcher order similarity, and table row/cell F1. Human traces provide process references rather than uniquely correct search paths.
<!-- EVIDENCE:method:END -->

<!-- EVIDENCE:setup:START -->
## Conditions needed to interpret the results

The four answer types contain 22, 50, 48 and 253 tasks. ReAct uses Google Serper top ten results and Jina page reading, summarized by the same backbone in non-thinking mode. Each task allows thirty tool calls and 8,192 output tokens per step, with parallel calling disabled. Commercial budgets differ and Google AI Mode is manually converted to CSV. Final scoring is deterministic after normalization, without an LLM answer judge, although browsing summaries remain model-dependent. Monthly live-answer maintenance is promised but its actual update history was not verified.
<!-- EVIDENCE:setup:END -->

<!-- EVIDENCE:result-1:START -->
## Complete success and partial information quality

Scores are percentages; overall EM uses 373 tasks and table metrics use 253 tasks, with shared ReAct tools and a 30-call limit.

| Claude 4.5 Sonnet mode | Overall EM | Table EM | Table row F1 | Table cell F1 |
|---|---|---|---|---|
| Non-thinking | 16.36 | 9.49 | 47.85 | 63.71 |
| Thinking | 19.3 | 13.04 | 49.92 | 65.17 |

Source: Table 3 · [Paper](https://arxiv.org/pdf/2602.08543v1)
<!-- EVIDENCE:result-1:END -->

<!-- EVIDENCE:result-2:START -->
## Higher scores need not require more calls or cost

Per-question means over 373 tasks; costs use historical paper prices and include model tokens for main reasoning and browse summaries, not current prices or necessarily total service cost.

| Claude 4.5 Sonnet mode | Search calls | Browse calls | Token cost USD |
|---|---|---|---|
| Non-thinking | 10.11 | 5.67 | 1.62 |
| Thinking | 7.57 | 4.63 | 1.37 |

Source: Tables 3–4 · [Paper](https://arxiv.org/pdf/2602.08543v1)
<!-- EVIDENCE:result-2:END -->

<!-- EVIDENCE:interpretation:START -->
## What the comparisons establish

Claude 4.5 Sonnet thinking achieves 19.30% whole-answer EM but 65.17 table cell F1: perfect structured output and partially correct information are distinct metrics. Enabling thinking raises overall EM from 16.36 to 19.30 while the paper’s estimated token cost falls from $1.62 to $1.37 per question because calls and input volume decrease. Reasoning mode is therefore not uniformly more expensive. Opaque commercial budgets, formatting compliance and manual CSV conversion also prevent interpreting product scores as pure backbone capability.
<!-- EVIDENCE:interpretation:END -->

<!-- EVIDENCE:limitations:START -->
## Limits, source discrepancies and next test

Worse live-subset performance does not prove training contamination because task content and difficulty also differ. A no-search DeepSeek filter tests one model configuration rather than guaranteeing retrieval necessity for every system. Tables comprise 253 of 373 tasks, making overall EM highly sensitive to formatting and completeness; partial F1 is essential context. Human-trace similarity is correlational, and error categories come from 50 failed cases with multiple labels, not all-task failure probabilities. Next, fix answer dates and tool budgets, independently review scoring before and after format repair, and test deeper browsing through paired interventions.

Conclusion reports best EM 18.23%, whereas abstract and Table 3 report Claude thinking 19.30%; use the identified Table 3 row. Figure 5 says 40 queries but Best@1=8.90% and Best@16=22.22% are not multiples of 1/40; sample/aggregation details do not reconcile the denominator. Do not promote these as exact 40-query rates. Appendix C defines search diversity as adjacent-query Jaccard similarity with lower meaning more diverse, then narrates the direction oppositely. Keep the formula and avoid the inconsistent verbal interpretation. The headline claim that reasoning raises token cost has a counterexample in Table 4: Claude thinking costs less than its non-thinking condition. The registry date is 2026-02-06, while this exact arXiv v1 PDF is dated 2026-02-09; dates may refer to different events and should not be silently equated.
<!-- EVIDENCE:limitations:END -->

Related benchmarks: [sgr-bench](sgr-bench.en.md) · [wandr](wandr.en.md)
