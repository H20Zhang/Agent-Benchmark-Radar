# membench: current-fact hits versus stale-fact contamination

<!-- RELEASE-REFERENCE:START -->
> **Best at release (not yet verified)** · Benchmark recorded date: 2026-08-22<br>
> A best result tied to a model, metric, and protocol in the initial release has not yet been verified. [Original source](https://github.com/Ps23102004/membench)<br>
> No substitution from a live board, a single baseline, or a later paper; unknown is neither zero nor a claim that the authors reported no results.
<!-- RELEASE-REFERENCE:END -->

[中文](membench-staleness.md) | **English**

<!-- EVIDENCE:reading:START -->
## Reading coverage and version

Reviewed the pinned official protocol, settings, result artifacts and limitations; no independent reproduction.

Read pinned complete README, runner, grader, aggregation metrics and recency backend; inspected temporal-scoping scenarios and the complete frozen leaderboard JSON. Did not execute backends or audit every scenario and adapter.

[eff49d9904164a0bc3e4e5f6c261bffe4ff8663b](https://github.com/Ps23102004/membench/blob/eff49d9904164a0bc3e4e5f6c261bffe4ff8663b/README.md)

[Auxiliary material (checked 2026-09-30)](https://github.com/Ps23102004/membench/blob/eff49d9904164a0bc3e4e5f6c261bffe4ff8663b/membench/runner.py)

[Auxiliary material (checked 2026-09-30)](https://github.com/Ps23102004/membench/blob/eff49d9904164a0bc3e4e5f6c261bffe4ff8663b/membench/grader.py)

[Auxiliary material (checked 2026-09-30)](https://github.com/Ps23102004/membench/blob/eff49d9904164a0bc3e4e5f6c261bffe4ff8663b/membench/metrics.py)

[Auxiliary material (checked 2026-09-30)](https://github.com/Ps23102004/membench/blob/eff49d9904164a0bc3e4e5f6c261bffe4ff8663b/membench/backends/recency_backend.py)

[Auxiliary material (checked 2026-09-30)](https://github.com/Ps23102004/membench/blob/eff49d9904164a0bc3e4e5f6c261bffe4ff8663b/results/leaderboard-2026-08-22.json)

[Auxiliary material (checked 2026-09-30)](https://github.com/Ps23102004/membench/blob/eff49d9904164a0bc3e4e5f6c261bffe4ff8663b/scenarios/temporal_scoping.json)

The frozen release reference is preserved; newer paper results do not replace initial-release scores.
<!-- EVIDENCE:reading:END -->

<!-- EVIDENCE:method:START -->
## How tasks create memory demands

membench writes each handwritten multi-session story chronologically into a small store and probes at intermediate stages. Each suite resets memory; future writes are hidden. Backends return stored text without an answer model. An expected substring anywhere in top-k is a hit; a forbidden substring at rank one is staleness@1, while appearance anywhere is leak_rate@k. This reveals high recall achieved by returning both old and current facts.

Genealogy: These are independently authored update-semantics unit tests, not LongMemEval-derived data. Relative to knowledge-update QA, evaluation stops at text ranking and separates stale top-one output, lower-ranked contamination and missing current facts. StateMemBench offers a cross-scale pairing, not an interchangeable aggregate score.
Illustrative scoring: an old record names contact A and a later update names B. Returning B can count as a hit while ranking A first simultaneously counts as stale contamination. High recall can coexist with incorrect priority.
<!-- EVIDENCE:method:END -->

<!-- EVIDENCE:setup:START -->
## Experimental settings and scoring targets

Five suites contain twelve probes each: supersession, negation, entity confusion, temporal scoping and distractor load, totaling sixty. Stores contain roughly 12–52 facts and k=5. The frozen 2026-08-22 run records Ollama 0.32.15 and nomic-embed-text:latest digest 0a109f422b47. embed uses cosine; recency takes max(3k,10)=15 semantic candidates then sorts by timestamp; grep uses keyword overlap with recency tie-breaking. Default write metadata contains only timestamp/session ID, stripping handwritten topic/entity answer tags. Empty output has zero recall, is excluded from stale/leak denominators and counts toward abstention, so all three must be reported.
<!-- EVIDENCE:setup:END -->

<!-- EVIDENCE:result-1:START -->
## Frozen leaderboard pooled results

Hits and stale output can coexist on the same probe. All backends have zero abstention, making stale denominators sixty here. Wilson binomial intervals assume independence that shared stories do not satisfy; generalization uncertainty can be larger. Tokens are characters divided by four, not tokenizer-measured billing.

60 probes per backend, twelve in each suite; counts correspond to the frozen rounded rates.

| Backend | Hits / 60 | Stale top-one / 60 | Staleness@1 95% interval | Leak@5 | Mean approximate tokens |
|---|---|---|---|---|---|
| embed | 59 | 28 | 0.346–0.591 | 1 | 70.3 |
| grep | 56 | 24 | 0.286–0.526 | 0.95 | 67.8 |
| recency | 45 | 3 | 0.017–0.137 | 0.167 | 73.9 |

Locator: Frozen leaderboard pooled results · [Source](https://github.com/Ps23102004/membench/blob/eff49d9904164a0bc3e4e5f6c261bffe4ff8663b/README.md)
<!-- EVIDENCE:result-1:END -->

<!-- EVIDENCE:result-2:START -->
## Frozen leaderboard supersession subset

Supersession only: 11/12 cannot describe all sixty probes. New-fact priority requires the new value to appear ahead of the old, or appear with the old absent; removing only the old value is insufficient.

Twelve probes; contradiction-resolution is defined only where a supersedes label exists.

| Backend | Hits / 12 | Stale top-one / 12 | Top-five stale leakage | New-fact priority |
|---|---|---|---|---|
| embed | 11 | 11 | 1 | 0 |
| grep | 10 | 5 | 0.833 | 0.333 |
| recency | 10 | 0 | 0 | 0.833 |

Locator: Frozen leaderboard supersession subset · [Source](https://github.com/Ps23102004/membench/blob/eff49d9904164a0bc3e4e5f6c261bffe4ff8663b/README.md)
<!-- EVIDENCE:result-2:END -->

<!-- EVIDENCE:result-3:START -->
## Frozen leaderboard selected other-suite trade-offs

Proportions are 0–1. The correct entity may rank first while related entities contaminate lower ranks; recency increases stale top-one output from zero to 25% in distractor load.

Each row uses twelve probes with no abstention.

| Suite / backend | Recall@5 | Staleness@1 | Leak@5 |
|---|---|---|---|
| Entity confusion / embed | 1 | 0 | 1 |
| Entity confusion / recency | 0.667 | 0 | 0.333 |
| Distractor load / embed | 1 | 0 | 1 |
| Distractor load / recency | 0.583 | 0.25 | 0.5 |

Locator: Frozen leaderboard selected other-suite trade-offs · [Source](https://github.com/Ps23102004/membench/blob/eff49d9904164a0bc3e4e5f6c261bffe4ff8663b/README.md)
<!-- EVIDENCE:result-3:END -->

<!-- EVIDENCE:limitations:START -->
## Limits and next validation

Results establish a freshness–recall trade-off, not solved update handling. Staleness includes old values, wrong entities and expired facts, so the label is not one uniform failure mechanism. Temporal-scope and multi-session examples already exist; future work should expand their scale and composition. Substring scoring can reject paraphrases or credit a correct keyword in the wrong context. Downstream answers/actions, retrieval latency and long-run scalability are untested.

staleness@1 is k-invariant only for rankings independent of k; recency changes its candidate pool with k. README says three embed suites are largely zero at top one; the frozen table shows exactly zero in entity-confusion and distractor-load, while temporal-scoping is 0.5. The source’s claim that deterministic substring scores are a lower bound on reasoning systems is too strong: substring false positives can also occur.



Next: Pair with LongMemEval or StateMemBench, retaining the sixty probes as regression tests and adding story-held-out natural paraphrases, longer supersession chains and larger distractor stores. Fix the semantic candidate pool while varying returned k. Report appropriate abstention on unanswerable tasks alongside recall on answerable tasks, adding semantic human review and downstream answers.
<!-- EVIDENCE:limitations:END -->
