# RAGCap-Bench: intermediate capabilities inside agentic RAG

<!-- RELEASE-REFERENCE:START -->
> **Best at release (not yet verified)** · Benchmark recorded date: 2025-10<br>
> A best result tied to a model, metric, and protocol in the initial release has not yet been verified. [Original source](https://arxiv.org/abs/2510.13910)<br>
> No substitution from a live board, a single baseline, or a later paper; unknown is neither zero nor a claim that the authors reported no results.
<!-- RELEASE-REFERENCE:END -->

[中文](ragcap-bench.md) | **English** · [Benchmark Library](../library/README.en.md)

<!-- EVIDENCE:reading:START -->
## Reading scope and version

Reviewed the stated primary paper in full for methods, experimental setup, results and limitations; no independent reproduction.

Read Sections 1–6, taxonomy, construction, metrics and experiments; appendices inspected: A–H, source datasets, error examples, all supplied generation/evaluation prompts, MCQ examples and bare-prompt results. Not performed: No dataset/code audit, no rerun; exact downstream graph values not digitized

[arXiv v1, 2025-10-15](https://arxiv.org/pdf/2510.13910v1)
<!-- EVIDENCE:reading:END -->

<!-- EVIDENCE:placement:START -->
## What changes relative to nearby evaluations

The following is an editorial protocol comparison, not an assertion of direct inheritance unless stated.

Compared with end-to-end search such as BrowseComp, RAGCap-Bench tests abstention, evidence and planning judgments on context snapshots through multiple choice. It diagnoses component capabilities rather than replacing completion rates on dynamic trajectories.
<!-- EVIDENCE:placement:END -->

<!-- EVIDENCE:method:START -->
## Task and evidence construction

The benchmark constructs 255 Chinese/English multiple-choice questions from existing research queries and trajectories produced by WebThinker, HiRA, WebSailor and WebDancer. It probes planning, evidence selection, grounded reasoning and noise robustness. Planning separates convergent and divergent strategies; noise separates abstention and source reliability. GPT-4o, Qwen-Plus and DeepSeek-V3 format questions or generate error-guided distractors, followed by removal of unanimously answered easy cases and malformed items. Experts determine gold answers by majority vote. The main task selects an option set given an intermediate state rather than autonomously executing search for all 255 questions.
<!-- EVIDENCE:method:END -->

<!-- EVIDENCE:setup:START -->
## Conditions needed to interpret the results

Main Table 3 uses informative prompts with typical-error examples; Appendix Table 6 uses bare prompts. EM requires an exact option-set match. F1 is averaged per instance and then within groups; overall scores equally weight four capabilities rather than micro-averaging 255 questions. Divergent planning and noise abstention report only EM, so EM and F1 cover different subcomponents. Downstream validation has three Qwen3 sizes, 8B/32B/235B, in WebThinker and HiRA on InfoDeepSeek/BrowseComp-Zh with at most ten Google calls. A separate study samples 500 WebThinker trajectories: the three models score each step from one to ten, average across steps, and correlate with final binary correctness. There are no human process-quality gold scores.
<!-- EVIDENCE:setup:END -->

<!-- EVIDENCE:result-1:START -->
## Two noise capabilities are not interchangeable

Percentages within each noise subgroup; exact subgroup counts are not printed in the main table for the 255-question benchmark. Abstention is a binary choice and reliability may be multi-select, so difficulty is not matched.

| Model | Noise-abstain EM | Noise-reliability EM | Noise-reliability F1 |
|---|---|---|---|
| GPT-4o | 97.3 | 10.0 | 65.96 |
| DeepSeek-R1 | 70.27 | 35.0 | 80.92 |

Source: Table 3, informative prompts · [Paper](https://arxiv.org/pdf/2510.13910v1)
<!-- EVIDENCE:result-1:END -->

<!-- EVIDENCE:result-2:START -->
## Error-example prompts can help overall but hurt a component

Same model and 255 questions, in percent; overall scores equally weight four capabilities and component columns average only their respective task types.

| Qwen3-235B prompt | Overall EM | Evidence-selection EM | Grounded-reasoning EM |
|---|---|---|---|
| Bare | 46.56 | 42.03 | 52.83 |
| Informative | 51.57 | 39.13 | 56.6 |

Source: Table 3 and Appendix F Table 6 · [Paper](https://arxiv.org/pdf/2510.13910v1)
<!-- EVIDENCE:result-2:END -->

<!-- EVIDENCE:result-3:START -->
## Process-rating correlation is not human agreement

Five hundred WebThinker trajectories; per-step 1–10 ratings are averaged within each trajectory and point-biserially correlated with final binary success. Correlation r is unitless; the paper reports p<0.05 without human process gold labels.

| Evaluator | Evidence rating vs outcome r | Reasoning rating vs outcome r |
|---|---|---|
| Qwen3-8B | 0.21 | 0.291 |
| Qwen3-235B | 0.528 | 0.338 |

Source: Table 4; Section 4.5 · [Paper](https://arxiv.org/pdf/2510.13910v1)
<!-- EVIDENCE:result-3:END -->

<!-- EVIDENCE:interpretation:START -->
## What the comparisons establish

RAGCap exposes uneven capabilities: GPT-4o reaches 97.30% noise-abstention EM but only 10.00% exact source-reliability selection. Knowing when to abstain differs from identifying reliable sources. Prompt gains are not uniform either: Qwen3-235B overall EM rises from 46.56 to 51.57 while evidence-selection EM falls from 42.03 to 39.13. The 0.528 value from 500 trajectories is a correlation between process ratings and final correctness, not agreement with human process judgments or proof that MCQ scores replace end-to-end evaluation.
<!-- EVIDENCE:interpretation:END -->

<!-- EVIDENCE:limitations:START -->
## Limits, source discrepancies and next test

Multiple choice measures recognition among supplied options, not plan generation or tool execution. Option counts differ across categories, affecting exact-match difficulty. Model-consensus filtering induces model dependence, and source questions overlap in benchmark families with downstream validation, requiring sample-independence checks. Source reliability includes normative choices rather than direct truth verification. Next, use disjoint questions with fixed backbones and budgets, intervene on intermediate modules, and obtain human evidence/answer judgments to test causal diagnostic value.

The paper says evidence-extraction F1 generally exceeds 70%, but informative Qwen3-32B is 62.97; retain per-model rows rather than universal prose. The strong downstream-surrogate claim relies on three model sizes and two frameworks, with Figure 4 rather than a reported broad correlation coefficient/confidence interval. Table 4 coefficients quantify evaluator ratings versus final binary correctness on 500 trajectories, not the correlation of MCQ scores with human process labels. The source-reliability prompt categorically lists promotional company pages and user-upload sites as less credible; this operational definition can penalize informative primary sources and should be visible. No inter-annotator agreement number or explicit annotator count is given for expert majority-vote labels in the reviewed paper.
<!-- EVIDENCE:limitations:END -->

Related benchmarks: [agenticragtracer](agenticragtracer.en.md) · [browsecomp-plus](browsecomp-plus.en.md)
