# SGR-Bench: retrieval state and structured answers on specialist portals

<!-- RELEASE-REFERENCE:START -->
> **Best at release (historical reference)** · 2026-05 · paper v1<br>
> **GPT-5.5 / CLI agent — Overall Item-F1: 66.18%**; **GPT-5.5 / CLI agent — Overall Row-F1: 43.37%**<br>
> Best configuration in Tables 2–3 on 100 tasks; item and full-row F1 remain separate metrics. [Original source](https://arxiv.org/html/2605.22219v1)<br>
> Historical difficulty reference, not current SOTA; tasks, versions, and experimental conditions are not interchangeable.
<!-- RELEASE-REFERENCE:END -->

[中文](sgr-bench.md) | **English** · [Home](../README.en.md)

<!-- EVIDENCE:reading:START -->
## Reading coverage and version

Read the stated version’s complete main text and available appendices and checked selected results; no independent experiment reproduction.

Read Sections 1–5 and Appendices A–K, including metric formulas, tool restrictions, six cases, all error analyses and output-cardinality analysis; visually checked Table 3. References are not treated as experimental content.

[arXiv 2605.22219v1 · 2026-05-21](https://arxiv.org/pdf/2605.22219v1)
<!-- EVIDENCE:reading:END -->

<!-- EVIDENCE:method:START -->
## Method and measurement target

The 100 tasks comprise fifty underlying problems with two paired formulations: one supplies explicit retrieval constraints and the other emphasizes the goal. Each pair shares its target site, reference and output schema. Six source families cover twelve public ecosystems, with ordered-table answers. Sites are selected from Wikipedia external links with Qwen-Plus prioritization; ChatGPT-5.2 Pro assists drafting before human solving, state-necessity and shortcut checks. Filtering retains tasks where a baseline makes partial progress, conditioning the distribution on that baseline. One concrete failure changes medical OR doctor to medical bills OR doctors, producing analyzable records for the wrong population.

Editorial placement: BrowseComp emphasizes discovering answer evidence; SGR-Bench additionally requires configuring specialist-site filters, hierarchies and scope to recover structured rows. It adds retrieval state and row-bound constraints. Compared with general web interaction tasks, the endpoint remains information extraction rather than arbitrary website changes.

[Source](https://arxiv.org/pdf/2605.22219v1)
<!-- EVIDENCE:method:END -->

<!-- EVIDENCE:setup:START -->
## Scoring and experimental conditions

Eight CLI systems are limited to Serper search, webpage fetching and PDF reading. Tasks use isolated sessions, medium effort, a 6,000-second cap and a 3,000-second no-progress stall threshold. Commercial products are separately tested through their web interfaces, not the same tool configuration. Reviewer-defined alias, date and unit canonicalization precedes deterministic scoring without filling omissions or correcting facts. Item-F1 is twice the number of correct fields divided by total reference and predicted fields; Row-F1 applies the same formula to fully correct rows. P.O.A. scores relative order among shared rows, assigning zero when fewer than two are shared. Overall scores average tasks rather than binary passes; repeats and variance are not fully reported.

[Source](https://arxiv.org/pdf/2605.22219v1)
<!-- EVIDENCE:setup:END -->

<!-- EVIDENCE:result-1:START -->
## Selected CLI results on the complete task set

Macro averages over 100 task formulations representing fifty paired problems; controlled external retrieval tools and 6,000-second caps, but different CLIs/models. These are system scores, not model-only rankings under an identical controller.

| System | Item-F1 (%) | Row-F1 (%) | P.O.A. (%) |
| --- | --- | --- | --- |
| GPT-5.5 / Codex CLI | 66.18 | 43.37 | 90.40 |
| GLM-5.1 / Claude Code | 65.64 | 33.32 | 87.25 |
| Claude Opus 4.7 / Claude Code | 61.38 | 38.51 | 81.31 |

Source location: Table 3, p. 18; Table 2, p. 8; Appendix C, pp. 16–17 · [Source](https://arxiv.org/pdf/2605.22219v1)
<!-- EVIDENCE:result-1:END -->

<!-- EVIDENCE:result-2:START -->
## Selected primary causes in audited failures

Denominator: 156 analyzable failed trajectories, not all tasks or systems; eight CLI models × twenty-two aligned slots produce 176 runs, with twenty classified as correct. Each failure has one primary label; three of six categories are selected here.

| Cause | Failures | Share of failures (%) |
| --- | --- | --- |
| Retrieval-scope drift | 58 | 37.2 |
| Criterion mismatch | 43 | 27.6 |
| Final answer composition | 16 | 10.3 |

Source location: Appendices G–H, Table 4, pp. 20–21 · [Source](https://arxiv.org/pdf/2605.22219v1)
<!-- EVIDENCE:result-2:END -->

<!-- EVIDENCE:limitations:START -->
## Interpretation, limitations and next experiment

The gap between field and complete-row scores motivates explicit constraint binding, but cannot alone establish state control as the unique causal bottleneck. The manual audit covers eight models on twenty-two sampled task slots: 176 trajectories, including 156 failures. Each failure receives its earliest unrecoverable cause; commercial systems and vulnerability-database tasks are absent. Stable public-source selection, assisted construction and modest scale limit generalization. The complete batch runner and trajectory corpus are not released, so single-case instructions do not constitute complete experimental reproducibility.

The CLI is not identical across models: GPT-5.5 uses Codex CLI and the others Claude Code, with controlled external retrieval tools, prompts and time caps. The original claim that explicit guidance significantly reduces difficulty is too strong: some models score higher on goal-oriented tasks and no significance test is reported. Figure 5 labels the scholarly sample as 62 versus 64 in Table 5; Figure 7’s cardinality sample counts and values differ from surrounding prose and are not used here.

Fix page snapshots and models, separately supply the correct site, retrieval state and complete evidence, and compare structured APIs with page access over the same data. Use paired inference over fifty task pairs and report field, row and order scores alongside time and tool calls.

[Source](https://arxiv.org/pdf/2605.22219v1)
<!-- EVIDENCE:limitations:END -->
