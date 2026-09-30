# PM-Bench: remembering intentions and acting at the right moment

<!-- RELEASE-REFERENCE:START -->
> **Best at release (historical reference)** · 2026-07-14 · paper v1<br>
> **GPT-5.4 + optional heartbeat — Per-model Set-F1: 79.1%**; **Optional heartbeat (8-model aggregate) — Macro Set-F1: 65.1%**<br>
> Per-model best from Table 3 and best cross-model scaffold average from Table 2, with different denominators. [Original source](https://arxiv.org/html/2607.12385v1)<br>
> The abstract associates 65.1% with GPT-5.4, unlike the tables. This reference follows the explicit Table 2/3 scopes, not current SOTA.
<!-- RELEASE-REFERENCE:END -->

[中文](pm-bench.md) | **English**

<!-- EVIDENCE:reading:START -->
## Reading coverage and version

Reviewed the stated paper version, method, experimental setup, key results and limitations; no independent reproduction.

Read main Sections 1–5, ethics and Appendix A.1–A.6, including complete interface/scoring examples, all prompts and Tables 1–7; checked PDF Figure 4 numeric labels and qualitative cases. Official repository README confirms six live configurations and two replays. No implementation audit or reproduction.

[arXiv 2607.12385v1 (2026-07-14)](https://arxiv.org/html/2607.12385v1)

[Official source observed 2026-09-30 (mutable page)](https://github.com/genglinliu/PMBench)

The frozen release reference is preserved; newer paper results do not replace initial-release scores.
<!-- EVIDENCE:reading:END -->

<!-- EVIDENCE:method:START -->
## How tasks create memory demands

PM-Bench tests whether delayed intentions are executed at the right moment. One fixed synthetic week contains seven days and 80 decision points. At each step the agent may query hidden clock/state channels, then chooses an A/B/C ongoing activity and a set of currently due actions. A/B/C is checked only for protocol compliance, not performance on a separate substantive problem. Menus expose action text, with handles reshuffled daily and 74 lure actions. Intentions can be announced earlier, span days, be rescheduled/canceled or depend on prerequisites. Scores jointly reflect intention maintenance, updating, proactive querying and selection rather than storage capacity alone.

Editorial placement: Relative to LongMemEval’s retrospective QA, PM-Bench adapts the Virtual Week paradigm to deferred intentions executed amid ongoing activity. It adds future-cue monitoring and timely action, which successful historical recall alone does not establish. This is an evaluation-coordinate comparison, not a claim of direct dataset inheritance.
<!-- EVIDENCE:method:END -->

<!-- EVIDENCE:setup:START -->
## Experimental settings and scoring targets

Of 83 task definitions, 81 executable tasks are scored; the week includes 15 hidden-channel-triggered tasks, seven cross-day tasks and 11 updates (two cancellations, three overrides, six reschedules), with 11 channels. Eight backbones each have eight configurations: six live model runs and two deterministic voting replays of hierarchical traces, not independent samples. The in-context TODO ledger is capped at five items with eight-word notes. Optional heartbeat is agent-controlled; fixed heartbeats nudge monitoring every 30 or 60 virtual minutes without revealing actual cues. The hierarchical scaffold unions three specialists’ suggested queries before coordinator action selection. Complete decoding temperatures, output-token/context-truncation budgets and multi-scenario/repeated-run uncertainty are not specified.
<!-- EVIDENCE:setup:END -->

<!-- EVIDENCE:result-1:START -->
## Table 2, selected aggregate scaffold tradeoffs

Set-F1 accumulates TP/FP/FN across each trajectory, then computes 2TP/(2TP+FP+FN); macro F1 averages eight model scores. FP and query columns are totals over eight evaluations, not means or token costs.

Same fixed 80-step week per model; eight model evaluations per scaffold. Action-opportunity counts, not simply 81 tasks, form F1 denominators.

| Configuration | Macro Set-F1 (%) | Precision (%) | False positives | State queries |
|---|---|---|---|---|
| Single baseline | 60.0 | 66.7 | 199 | 106 |
| Todo ledger | 62.8 | 73.2 | 134 | 118 |
| Heartbeat (optional) | 65.1 | 70.6 | 178 | 130 |
| Auto-heartbeat (30m) | 57.8 | 63.2 | 489 | 203 |
| Hierarchical union-query | 45.2 | 51.2 | 273 | 1661 |
| Majority vote replay | 37.2 | 34.9 | 655 | 1661 |

Locator: Table 2, selected aggregate scaffold tradeoffs · [Source](https://arxiv.org/html/2607.12385v1)
<!-- EVIDENCE:result-1:END -->

<!-- EVIDENCE:result-2:START -->
## Table 3, selected within-backbone contrasts

Same-backbone, same-week scaffold comparisons. Optional heartbeat improves GPT-5.4 by 6.6 points but is below the baseline for the other selected backbones; the macro gain is not universal.

One fixed-week trajectory per model/configuration; no repeated-run intervals.

| Backbone | Single F1 (%) | Ledger F1 (%) | Optional heartbeat F1 (%) | Fixed 30m F1 (%) |
|---|---|---|---|---|
| GPT-5.4 | 72.5 | 73.5 | 79.1 | 74.1 |
| GPT-5.3-Codex | 78.9 | 74.8 | 76.6 | 71.0 |
| Qwen3-32B | 51.4 | 51.7 | 48.5 | 57.5 |

Locator: Table 3, selected within-backbone contrasts · [Source](https://arxiv.org/html/2607.12385v1)
<!-- EVIDENCE:result-2:END -->

<!-- EVIDENCE:result-3:START -->
## Table 2 and Figure 4 numeric labels, selected diagnostic slices

Task-subset hit rates aggregated over eight models, distinct from Set-F1. More monitoring can improve a slice while increasing false positives; non-clock hidden-state tasks remain particularly difficult.

Week contains seven cross-day tasks and 15 channel-triggered tasks; paper does not print all exact effective slice denominators, especially update eligibility.

| Configuration | Cross-day hit (%) | Update hit (%) | Clock-monitoring hit (%) | Non-clock hidden-channel hit (%) |
|---|---|---|---|---|
| Heartbeat (optional) | 50.0 | 44.4 | 54.7 | 10.0 |
| Auto-heartbeat (30m) | 35.7 | 47.2 | 60.4 | 15.8 |
| Hierarchical union-query | 10.7 | 20.8 | 60.4 | 5.0 |

Locator: Table 2 and Figure 4 numeric labels, selected diagnostic slices · [Source](https://arxiv.org/html/2607.12385v1)
<!-- EVIDENCE:result-3:END -->

<!-- EVIDENCE:limitations:START -->
## Limits and next validation

Cancellation, override, rescheduling and prerequisites are already included and should not be listed wholesale as unmeasured. Perfect-play validation establishes solvability under this synthetic interface, not representative real schedules or memory-specific causation for every failure. Hierarchical querying costs much more; voting replays isolate the final selection rule on existing evidence, not how alternate decisions change later queries/state. With one fixed week, 79.1% does not establish cross-week generalization or reliable real-time seven-day operation.

The abstract attributes 65.1% to GPT-5.4; Table 2 explicitly gives it as the optional-heartbeat macro average, while Table 3 gives GPT-5.4/optional heartbeat 79.1%. Preserve the frozen header’s existing distinction. Appendix A.5 cautiously infers default channel_query nudges because a flag was not overridden; this is not a verified runtime trace audit. The Figure 4 best non-clock aggregate 16.7% is distinct from individual-channel Table 7 values as high as 33.3%; do not conflate them.



Next: Retain existing update/cancellation controls and add unseen weeks and repeated runs. Compare in-context ledgers, external memory and explicit schedulers under matched query/token/call budgets. Add a substantive ongoing task plus memory-off and full-task-state diagnostic conditions to separate maintenance, monitoring and decision bottlenecks.
<!-- EVIDENCE:limitations:END -->
