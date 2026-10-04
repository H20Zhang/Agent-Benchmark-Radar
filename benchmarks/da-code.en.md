# DA-Code: interactive data science, execution feedback and artifact scoring

<!-- RELEASE-REFERENCE:START -->
> **Best at release (historical reference)** · 2024-10-09 · paper v1<br>
> **DA-Agent / GPT-4 — Total score: 30.5**<br>
> Best total score in v1 Table 3; distinct from 76.8% executable code and 99.4% within-budget completion. [Original source](https://arxiv.org/html/2410.07331v1)<br>
> Historical difficulty reference, not current SOTA; tasks, versions, and experimental conditions are not interchangeable.
<!-- RELEASE-REFERENCE:END -->

[中文](da-code.md) | **English** · [Home](../README.en.md) · [Benchmark Library](../library/README.en.md)

<!-- EVIDENCE:reading:START -->
## Reading coverage and version

Reviewed the stated primary-paper version, method, setup, key results and limitations; no independent experiment reproduction.

Main Sections 1–7 and limitations, plus Appendices A–E, including an eleven-step debugging/artifact trajectory.

[arXiv:2410.07331v1](https://arxiv.org/html/2410.07331v1)

The tables reorganize selected sourced facts. The title-level historical reference may use a different version, split or model; do not pool scores across those settings.
<!-- EVIDENCE:reading:END -->

<!-- EVIDENCE:method:START -->
## Measurement, method and comparison

This is not one-shot code generation. DA-Agent observes files in Docker, acts through Bash/Python/SQL, reads results or errors, adjusts subsequent actions and produces checkable tables, charts or ML artifacts. Intermediate inspection and iterative repair are part of the evaluation. Executable code, producing a result within the step cap, and result quality are different measurements.

[Primary source](https://arxiv.org/html/2410.07331v1)
<!-- EVIDENCE:method:END -->

<!-- EVIDENCE:setup:START -->
## Experimental settings and denominators

The 500 tasks comprise 100 wrangling, 100 ML and 300 exploratory-analysis tasks. Greedy generation allows 20 steps, up to 15 history steps and 300 seconds per action. Tables/charts use task-specific matches; ML metrics are normalized and clipped to [0,1] before aggregation. Thus 30.5 is a mixed Total score displayed on 0–100, not a homogeneous binary pass rate across all 500 tasks. Exact model snapshots and package versions are not fully specified in the inspected setup.

[Setup source](https://arxiv.org/html/2410.07331v1)
Completion uses tasks as its denominator; executable-code rate uses generated code. Table checks target specified columns; chart checks extract values/parameters from plotting scripts rather than judge complete visual quality. Table 4 prints 99.5% completion on a 100-task subset without explicit rerun/aggregation details, so no successful-task count is inferred.

Additional scoring limits: Appendix C normalizes ML metrics using task-specific baseline and best-reference bounds; chart matching permits sorting/scaling transformations and does not establish complete visual quality. Appendix A excludes deep-learning tasks. Table 3 also contains completion rates such as 97.7% that cannot directly imply an integer count out of 500; repetition/aggregation remains unspecified. New tracks record Table 3 mixed Total only, excluding these ambiguous completion rates.

[Table 3 / Appendix C](https://arxiv.org/html/2410.07331v1) · [JSON](../data/results/da-code.json)
<!-- EVIDENCE:setup:END -->

<!-- EVIDENCE:result-1:START -->
## Models under the same framework

Full 500 tasks with DA-Agent; 20-step cap, 15-step history and 300 seconds/action. Completion and executable-code rates have different denominators.

| Model / framework | Mixed Total score (0–100) | Completion (%) | Executable code (%) |
|---|---|---|---|
| GPT-4 / DA-Agent | 30.5 | 99.4 | 76.8 |
| GPT-4o / DA-Agent | 29.1 | 97.4 | 77.7 |
| Qwen2.5-72B / DA-Agent | 22.6 | 93.8 | 72.2 |

GPT-4's 99.4% completion does not mean 99.4% correct tasks: producing a result and its 30.5 mixed quality score are different.

Fact source: §3.4;§5.1;Table 3,PDFp7 · [Source](https://arxiv.org/html/2410.07331v1)
<!-- EVIDENCE:result-1:END -->

<!-- EVIDENCE:result-2:START -->
## Reference plans on a separate subset

Random DA-Code-100 subset with GPT-4. A reference plan supplies additional task guidance; these scores are not pooled with full-500 results.

| Framework / condition | Mixed Total score (0–100) | Completion (%) |
|---|---|---|
| OpenDevin | 26.2 | 96.0 |
| DA-Agent (paper Table 4: DA-Code) | 31.5 | 99.5 |
| DA-Agent + Reference Plan | 39.7 | 97.7 |

Reference plans accompany a 31.5→39.7 score change, not an independent certification of general planning ability. Table 4 calls its own-framework row DA-Code while the text calls the agent DA-Agent; that correspondence is retained.

Fact source: §5.2–5.3;Table 4,PDFp7 · [Source](https://arxiv.org/html/2410.07331v1)
<!-- EVIDENCE:result-2:END -->

<!-- EVIDENCE:limitations:START -->
## Limitations, remaining gaps and next experiment

Interaction, feedback-driven repair and artifact validation were evaluated; they must not be listed as wholly absent. Long-lived project maintenance, enterprise governance and multi-application transfer remain unestablished. Difficulty counts 105/292/103 disagree with their printed percentages; no reconciliation is invented here. Compared with static code problems, it adds data-grounded planning/execution. Next, fix budgets and separately supply correct data summaries or reference plans, then retest independent tasks.

[Primary evidence](https://arxiv.org/html/2410.07331v1)
<!-- EVIDENCE:limitations:END -->

<!-- RESEARCH-DECISION:START -->

Use the method, comparisons and limitations together to decide whether this benchmark fits a claim. These tables are not a cross-protocol leaderboard; structural checks do not certify factual correctness or reproduction.

Related measurements and controls: [DS-1000](ds-1000.en.md) · [DataSciBench](datascibench.en.md) · [Data Agent Benchmark (DAB)](data-agent-benchmark.en.md)

<!-- RESEARCH-DECISION:END -->
