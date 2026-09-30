# AgentFuel: evaluating single-turn temporal-state and incident queries

<!-- RELEASE-REFERENCE:START -->
> **Best at release (not yet verified)** · Benchmark recorded date: 2026-03-12<br>
> A best result tied to a model, metric, and protocol in the initial release has not yet been verified. [Original source](https://arxiv.org/abs/2603.12483)<br>
> No substitution from a live board, a single baseline, or a later paper; unknown is neither zero nor a claim that the authors reported no results.
<!-- RELEASE-REFERENCE:END -->

[中文](agentfuel.md) | **English** · [Home](../README.en.md) · [Benchmark Library](../library/README.en.md)

<!-- EVIDENCE:reading:START -->
## Reading coverage and version

Reviewed the stated primary-paper version, method, setup, key results and limitations; no independent experiment reproduction.

Main Sections 1–7 and Appendices A–D (32 pages), including query construction, main experiments, per-query outcomes and failure code.

[arXiv:2603.12483v1](https://arxiv.org/pdf/2603.12483v1)

The tables reorganize selected sourced facts. The title-level historical reference may use a different version, split or model; do not pool scores across those settings.
<!-- EVIDENCE:reading:END -->

<!-- EVIDENCE:method:START -->
## Measurement, method and comparison

Starting from a domain schema or samples, generate synthetic time series with specified patterns/incidents, construct corresponding reference questions and answers, then check a data agent end to end. Stateful refers to event order or state-machine semantics within one analysis, such as counting views while a cart is full. It is not memory retained from an earlier user question. Section 3.1 excludes multi-turn dialogue and historical context; Section 5.1 uses one-shot request/response.

[Primary source](https://arxiv.org/pdf/2603.12483v1)
<!-- EVIDENCE:method:END -->

<!-- EVIDENCE:setup:START -->
## Experimental settings and denominators

There are 24 questions per domain: e-commerce, IoT and telecom. Six configurations use Databricks Genie defaults, Snowflake Cortex Analyst defaults, Nao/GPT-4.1, and PandasAI with o4-mini-2025-04-16, Claude Sonnet 4.6 or Claude Opus 4.6. Each question/configuration is run independently three times. Main responses are manually checked against reference answers; incorrect answers and runtime errors fail. Models, tools and budgets are not matched. The separate GEPA pilot changes to GPT-4o-mini judging and restricted output, so it is not pooled with the main experiment.

[Setup source](https://arxiv.org/pdf/2603.12483v1)
The design has 36 stateless, 24 non-incident stateful and 12 incident questions. Multiplying six configurations by three runs gives design volumes of 648/432/216 responses. The paper does not separately disclose the exact weighting formula for the 73/34/10 aggregates; these derived volumes are not asserted effective statistical denominators.

<!-- EVIDENCE:setup:END -->

<!-- EVIDENCE:result-1:START -->
## Differences across query categories

Pooled query-category results across three domains and six configurations; three runs per question/configuration, with different category denominators rather than one model's scores.

| Query category | Accuracy (%) |
|---|---|
| Stateless | 73 |
| Stateful (no incident) | 34 |
| Incident-specific | 10 |

The 73→34→10 pattern points to temporal semantics and incident-window interpretation, not a memory-module effect. Categories are not difficulty-matched randomized interventions.

Fact source: §5.1–5.2,pp7–8;Figures6–8,p9 · [Source](https://arxiv.org/pdf/2603.12483v1)
<!-- EVIDENCE:result-1:END -->

<!-- EVIDENCE:limitations:START -->
## Limitations, remaining gaps and next experiment

The generator is not fully public; released datasets do not reproduce generation. Commercial systems have unmatched internal models/tools. Single-turn analysis is evaluated; cross-question memory, clarification dialogue and long-lived project maintenance are not. File size is artifact-version metadata, not inferred from this paper. Compared with ordinary table QA, the contribution is customizable event/temporal conditions. Next, fix model/tools and separately supply the correct incident window or state machine to distinguish discovery from calculation failures.

[Primary evidence](https://arxiv.org/pdf/2603.12483v1)
<!-- EVIDENCE:limitations:END -->

<!-- RESEARCH-DECISION:START -->

Use the method, comparisons and limitations together to decide whether this benchmark fits a claim. These tables are not a cross-protocol leaderboard; structural checks do not certify factual correctness or reproduction.

Related measurements and controls: [DA-Code](da-code.en.md) · [DataSciBench](datascibench.en.md) · [Data Agent Benchmark (DAB)](data-agent-benchmark.en.md)

<!-- RESEARCH-DECISION:END -->
