# DataSpace: verifiable analysis in heterogeneous workspaces

<!-- RELEASE-REFERENCE:START -->
> **Best at release (historical reference)** · 2026-08 · paper v1<br>
> **Grok 4.5 / DataSpace-Agent — Task accuracy (272/410): 66.34%**<br>
> Best of six backbones with DataSpace-Agent fixed in Table 3, on 410 tasks; not a maximum over arbitrary model/harness combinations. [Original source](https://arxiv.org/html/2608.03451v1)<br>
> Historical difficulty reference, not current SOTA; tasks, versions, and experimental conditions are not interchangeable.
<!-- RELEASE-REFERENCE:END -->

[中文](dataspace.md) | **English** · [Home](../README.en.md)

<!-- EVIDENCE:reading:START -->
## Reading coverage and version

Read the stated version’s complete main text and available appendices and checked the selected results; no independent experiment reproduction.

Read Sections 1–7 and Appendices A.1–A.8 and B (24 pages), covering construction, review, scoring, runtime configurations, subgroups and failure analysis; visually checked Tables 3, 11 and 12.

[arXiv 2608.03451v1 · 2026-08-04](https://arxiv.org/pdf/2608.03451v1)
<!-- EVIDENCE:reading:END -->

<!-- EVIDENCE:method:START -->
## Method and measurement target

DataSpace starts from executable BULL and EHRSQL queries, jointly transforms question/database languages, samples relationally consistent data, and renders table content into CSV, JSON, SQLite, Markdown, PDF or video. At least two experts independently solve each task before checking references and grading configurations. Of 410 tasks, 265 are cross-language and 134 require multiple modalities; having video in a workspace does not mean video is necessary. Agents receive only a question and directory and must submit a complete CSV.

[Source](https://arxiv.org/pdf/2608.03451v1)

<!-- EDITORIAL-METHOD:START -->
Editorial placement: Spider/BIRD emphasize relational queries; DataSpace expands to multi-source, cross-language workspaces that can include multimodal material, while retaining structured-output checks. The change is input/evidence heterogeneity. Not every task uses every modality, and aggregate scores do not isolate vision or cross-language contributions.
<!-- EDITORIAL-METHOD:END -->
<!-- EVIDENCE:method:END -->

<!-- EVIDENCE:setup:START -->
## Scoring and experimental conditions

The official metric is binary complete-table accuracy. Headers and column order may vary, but a one-to-one column mapping must exist; numbers are normalized under fixed precision and units, duplicate multiplicities are preserved, and order-sensitive tasks require the correct row order. Shape, type, unit or value errors can fail the whole task, without an LLM final-answer judge. Fixed-harness DataSpace-Agent comparisons allow 60 model turns, 50 tool actions, 1,800 seconds, 4 CPUs and 16 GiB RAM, with 180 seconds per shell command and no network. Model calls have a 32,768-output-token ceiling and provider-default reasoning settings.

[Source](https://arxiv.org/pdf/2608.03451v1)
<!-- EVIDENCE:setup:END -->

<!-- EVIDENCE:result-1:START -->
## Selected accuracy/resource comparison with DataSpace-Agent fixed

July 2026 endpoints, all 410 tasks; binary complete-table scoring; token and cost values are per-task means, with historical evaluation-time pricing; 32,768 output tokens per call; 60 model turns, 50 actions and 1,800 seconds; no seed variance reported.

| Model | Correct tasks / 410 | Task accuracy (%) | Tokens per task (thousands) | API cost per task (USD) |
| --- | --- | --- | --- | --- |
| Grok 4.5 | 272/410 | 66.34 | 301.9 | 0.169 |
| GPT-5.6 Sol | 265/410 | 64.63 | 77.8 | 0.200 |
| MiMo-V2.5 | 161/410 | 39.27 | 237.9 | 0.011 |

Source location: Table 3, p. 7; Table 11, p. 23; Appendix A.7, pp. 21–22 · [Source](https://arxiv.org/pdf/2608.03451v1)
<!-- EVIDENCE:result-1:END -->

<!-- EVIDENCE:limitations:START -->
## Interpretation, source limitations and next experiment

With MiMo-V2.5 fixed, Grok Build achieves 190/410 (46.34%) versus Smolagents at 127/410 (30.98%). Only the 1,800-second deadline is common; native action and context policies differ, preventing single-component attribution. GPT-5.6 Sol proposes root causes for Grok’s 136 failures and a human checks every case: 71 involve materialization and 31 involve task intent. These are one system’s failure counts, not general industry rates.

All 410 inputs are public, but only 60 references/configurations are released; 350 remain withheld for official evaluation. Competition A/B boards use challenge-specific rules, distinct from the finalized paper protocol. Repeated-run uncertainty is unreported.

Fix the model and action budget, distinguish target-result specification, evidence extraction, relational computation and CSV materialization, and separately add typed intermediate tables and output-contract checks. Report complete-table accuracy and recovery cost, using within-task modality replacements to control difficulty.

[Source](https://arxiv.org/pdf/2608.03451v1)
<!-- EVIDENCE:limitations:END -->
