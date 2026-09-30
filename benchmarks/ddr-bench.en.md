# DDR-Bench: entity-driven exploration and discovery coverage

<!-- RELEASE-REFERENCE:START -->
> **Best at release (not yet verified)** · Benchmark recorded date: 2025-11-30<br>
> A best result tied to a model, metric, and protocol in the initial release has not yet been verified. [Original source](https://arxiv.org/abs/2602.02039)<br>
> No substitution from a live board, a single baseline, or a later paper; unknown is neither zero nor a claim that the authors reported no results.
<!-- RELEASE-REFERENCE:END -->

[中文](ddr-bench.md) | **English** · [Home](../README.en.md) · [Benchmark Library](../library/README.en.md)

<!-- EVIDENCE:reading:START -->
## Reading coverage and versions

Full substantive paper and appendix reading completed for the stated primary version; experiments were not independently reproduced.

Read the complete 37-page v2 and Appendices A–I, including every checklist example, framework ablation, interaction/insight/time plot, checker prompt and provided trajectory excerpt. This is the May revision, not the February initial paper.

[arXiv 2602.02039v2 · 2026-05-15](https://arxiv.org/pdf/2602.02039v2)
<!-- EVIDENCE:reading:END -->

<!-- EVIDENCE:method:START -->
## What the method measures

DDR begins with an entity and database rather than checklist questions. GPT-5-mini checks whether collected insights support hidden facts. Per-turn insights come from separate same-model calls outside the agent trace; final reports summarize the full trajectory.

<!-- EDITORIAL-METHOD:START -->
Agents receive an entity and database, choose their own questions and accumulate discoveries. Hidden factual checklists are used afterward to score coverage. An illustrative workflow explores a company’s financial records, proposes a trend or anomaly, queries and revises it, then records evidence-backed insights without being told every target question. Separate calls to the same model extract per-round insights, while a final report summarizes the trajectory. Scores therefore combine exploration, insight extraction and judging.

Editorial placement: InsightBench also evaluates proactive insight discovery; DDR more explicitly pairs entity-started exploration with hidden-fact coverage and per-round analysis. It shifts from answering supplied questions to choosing investigations, while a finite checklist cannot exhaust valid discoveries.
<!-- EDITORIAL-METHOD:END -->
<!-- EVIDENCE:method:END -->

<!-- EVIDENCE:setup:START -->
## Experimental setup

There are 291 entities and 2,058 checklist items across MIMIC, GLOBEM and 10-K. ReAct uses SQL/Python interfaces and full history. Models normally self-terminate, but looping runs are forcibly stopped at 100 rounds and omitted from plots. Sampling and context caps are unspecified.
<!-- EVIDENCE:setup:END -->

<!-- EVIDENCE:results:START -->
## Selected quantitative evidence

V2; selected 10-K results use item-averaged checklist support over 849 items from 100 companies. Message-wise and final-report outputs are scored separately; the reactive control is given explicit questions.

| System / comparison | Dataset / denominator | Metric / unit | Result | Conditions | Source |
| --- | --- | --- | --- | --- | --- |
| Claude 4.5 Sonnet · ReAct | 10-K; 100 entities / 849 items | Message-wise / final-report support (%) | 77.27% / 61.25% | Entity-only start; GPT-5-mini checker | Table 2, p. 6 |
| DeepSeek-V3.2 · ReAct | 10-K; 100 entities / 849 items | Message-wise / final-report support (%) | 60.66% / 38.16% | Entity-only start; GPT-5-mini checker | Table 2, p. 6 |
| Qwen3-Next-80B-A3B · proactive | 10-K; 100 entities / 849 items | Message-wise / final-report support (%) | 45.58% / 31.10% | No explicit checklist questions | Table 5, p. 11 |
| Qwen3-Next-80B-A3B · reactive | 10-K; 100 entities / 849 items | Explicit-query support (%) | 70.55% | Each checklist item becomes a user query | Table 5, p. 11 |

Fact source: [Table 2, p. 6; Table 5, p. 11](https://arxiv.org/pdf/2602.02039v2)
<!-- EVIDENCE:results:END -->

<!-- EVIDENCE:limitations:START -->
## Limits and interpretation

Checklist coverage does not measure all unsupported claims or exhaust valid discoveries. Explicit-query controls change the task, while training-generation comparisons remain confounded. The hallucination audit measures correct-but-unfaithful facts, not every factual error. Its table contains rates above 5%, contrary to the prose; contamination is not ruled out.

<!-- EDITORIAL-NEXT:START -->
Next, compare free exploration, full checklists and partial checklists on identical entities/data/budgets. Vary insight extraction and judging separately, and have experts audit novel off-checklist findings and unsupported claims. Include forcibly stopped runs rather than analyzing only voluntarily terminated trajectories.
<!-- EDITORIAL-NEXT:END -->
<!-- EVIDENCE:limitations:END -->
