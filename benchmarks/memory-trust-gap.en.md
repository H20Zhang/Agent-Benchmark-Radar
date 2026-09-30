# Memory Trust Gap: evidence conflict across model scales

<!-- RELEASE-REFERENCE:START -->
> **Best at release (not yet verified)** · Benchmark recorded date: 2026-09-01<br>
> A best result tied to a model, metric, and protocol in the initial release has not yet been verified. [Original source](https://arxiv.org/abs/2609.01852)<br>
> No substitution from a live board, a single baseline, or a later paper; unknown is neither zero nor a claim that the authors reported no results.
<!-- RELEASE-REFERENCE:END -->

[中文](memory-trust-gap.md) | **English**

<!-- EVIDENCE:reading:START -->
## Reading coverage and version

Reviewed the stated paper version, method, experimental setup, key results and limitations; no independent reproduction.

Read main Sections 1–8 and Appendices A–E, all eleven tables and failure transcripts. PDF figure/probe labels checked; plotted coordinates not digitized. No harness audit or independent reproduction.

[arXiv 2609.01852v1 (2026-09-01)](https://arxiv.org/html/2609.01852v1)

The frozen release reference is preserved; newer paper results do not replace initial-release scores.
<!-- EVIDENCE:reading:END -->

<!-- EVIDENCE:method:START -->
## How tasks create memory demands

This experiment supplies conflicting evidence directly and measures answer selection at memory-consumption time, without a long-term write/update/retrieve pipeline. Three hundred templated scenarios split into 150 Benefit and 150 Safety items. Benefit omits current tool evidence, leaving memory-off near three-option chance; Safety always supplies the correct authoritative tool value while memory is absent, correct, stale or contains both values. Constrained action text is scored by exact, regex or canonical matching, without real execution. Three cyclic option rotations are averaged within each scenario before comparisons.

Editorial placement: Relative to STALE’s invalid-memory action checks, this study adds same-family scale comparisons, two memory-off meanings and a four-feature factorial. This is a consumption-side diagnostic extension, not a claim of direct STALE data reuse. AuthMem-Bench already tests both writing and action, despite this paper’s write-only related-work description.
In the paper’s example, the current calendar says Room B while stale memory says Room A. Safety requires B in every condition; Benefit removes the current tool value, separating conflict from missing information.
<!-- EVIDENCE:method:END -->

<!-- EVIDENCE:setup:START -->
## Experimental settings and scoring targets

Primary models are non-thinking Qwen3 0.6B/1.7B/4B/8B with greedy decoding; replication uses Llama-3.2-1B/3B-Instruct and Llama-3.1-8B-Instruct. Each 150-item suite spans 33 template families. Reliance is stale-value selection; Δmem is paired accuracy minus memory-off accuracy. Safety crosses label, apparent recency, source authority and stale-first position into 16 cells, averaging other features for each main effect. Ninety-five-percent intervals bootstrap scenarios, with family-cluster and leave-one-family-out checks. Analyses are exploratory, not preregistered confirmatory tests. Full level-by-level L0–L3 prompt contracts, all output-token caps and external-subset sample sizes are not specified in the paper.
<!-- EVIDENCE:setup:END -->

<!-- EVIDENCE:result-1:START -->
## Tables 2–3, Safety-suite trap progression

Accuracy/reliance use 0–1 units. Current tool evidence is always correct; L0–L3 increase apparent plausibility of stale memory. Larger models suffer more at stronger traps, but onset levels 0/1/1/1 do not become earlier as model size increases.

150 Safety scenarios per model/level, each averaged over three option rotations.

| Model | Minimum memory-off accuracy | L0 stale reliance | L2 stale reliance | L3 stale reliance | First significant-harm level |
|---|---|---|---|---|---|
| Qwen3-0.6B | 0.98 | 0.19 | 0.43 | 0.63 | 0 |
| Qwen3-1.7B | 1.0 | 0 | 0.45 | 0.72 | 1 |
| Qwen3-4B | 1.0 | 0 | 0.83 | 0.93 | 1 |
| Qwen3-8B | 1.0 | 0 | 0.94 | 1.0 | 1 |

Locator: Tables 2–3, Safety-suite trap progression · [Source](https://arxiv.org/html/2609.01852v1)
<!-- EVIDENCE:result-1:END -->

<!-- EVIDENCE:result-2:START -->
## Table 6, selected direct cross-size interaction tests

Values are differences of reliance effects, in 0–1 units. Recency dates the stale item newer; position places it first. These are paired interaction tests, not conclusions inferred from overlap between separate model intervals.

Safety 150 base scenarios with all 16 feature cells per model; scenario-paired bootstrap.

| Feature | 8B minus 0.6B effect | 95% lower | 95% upper |
|---|---|---|---|
| Recency | 0.302 | 0.269 | 0.336 |
| Position | -0.326 | -0.379 | -0.269 |
| Authority | 0.008 | -0.014 | 0.028 |

Locator: Table 6, selected direct cross-size interaction tests · [Source](https://arxiv.org/html/2609.01852v1)
<!-- EVIDENCE:result-2:END -->

<!-- EVIDENCE:result-3:START -->
## Table 7, selected representation interventions

Accuracy is 0–1. Metadata retains both items with source/date annotations; the representation oracle removes the stale item and changes available evidence. Metadata helps the small model too, without restoring near-oracle accuracy. This differs from the separate intervention that only marks the authoritative item.

Representation study sample count is not separately specified; do not assume every auxiliary study uses all 300 scenarios.

| Model | Raw accuracy | Metadata accuracy | Stale-item-removed accuracy |
|---|---|---|---|
| Qwen3-0.6B | 0.49 | 0.79 | 0.95 |
| Qwen3-8B | 0.41 | 0.95 | 1.0 |

Locator: Table 7, selected representation interventions · [Source](https://arxiv.org/html/2609.01852v1)
<!-- EVIDENCE:result-3:END -->

<!-- EVIDENCE:result-4:START -->
## Table 11a, selected framing controls

Reliance is 0–1; identical wrong information is framed as memory or document. The 8B contrast preserves the reported 0.016; subtracting displayed columns gives 0.015. The source does not explain that display discrepancy, so it is not attributed to rounding here. There is no consistent extra advantage for the memory label.

150 Safety scenarios per control; paired scenario bootstrap.

| Model | Memory-frame reliance | Document-frame reliance | Paired difference | 95% lower | 95% upper |
|---|---|---|---|---|---|
| Qwen3-0.6B | 0.307 | 0.618 | -0.311 | -0.36 | -0.262 |
| Qwen3-8B | 0.033 | 0.018 | 0.016 | -0.002 | 0.038 |

Locator: Table 11a, selected framing controls · [Source](https://arxiv.org/html/2609.01852v1)
<!-- EVIDENCE:result-4:END -->

<!-- EVIDENCE:limitations:START -->
## Limits and next validation

This does not establish that stronger models are generally less safe. Safety memory-off accuracy is near one at every scale, so its size differences cannot simply be explained by a weak small-model baseline. Checkpoint size proxies capability while training differences remain relevant. Llama replication mixes versions 3.2 and 3.1, and Qwen’s tiny-model positive position effect does not replicate. Label removal has positive effects at all Qwen scales; authority effects are smaller but significant, not absent. RGB free-text evaluation reduces the multiple-choice limitation, but external no-context baselines and construction differ and must not be pooled with Safety.

Benefit without memory lacks the needed fact, so adding both correct and stale values changes information availability; its explicit-conflict Δmem is not like-for-like harm. Oracle clean memory, oracle stale-item removal and authoritative-item marking are different interventions and estimands. The paper’s claim that AuthMem-Bench only tests writing conflicts with AuthMem’s Modules B/C. No public artifact pin or exact prompt manifest was independently inspected in this reading; paper-level coverage does not certify reproducible harness access.



Next: Retain existing memory-off, stale-memory, correct-evidence, document-frame and metadata controls. Extend to a write/update/retrieve pipeline with matched evidence/token budgets; vary scale and date-understanding training separately before assigning a mechanism, then add open-ended tool actions and side-effect scoring.
<!-- EVIDENCE:limitations:END -->
