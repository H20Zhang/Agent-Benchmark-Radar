# MemProbe: measure valid updating, preservation and provenance separately

<!-- RELEASE-REFERENCE:START -->
> **Release result (historical reference; not a best claim)** · 2026-09-24 · paper v1<br>
> **A-MEM (Gemini-3-Flash-preview reader) — Overall probe accuracy: 88.4%**<br>
> Main suite, 56 episodes and 224 probes; A-MEM adapter with Gemini-3-Flash-preview final reader. Selected historical result, not a cross-system best claim. [Original source](https://arxiv.org/abs/2609.30558v1)<br>
> Retrieval budgets, ingestion failures and metadata access differ across adapters; this result establishes neither a causal architecture advantage nor a current leaderboard.
<!-- RELEASE-REFERENCE:END -->

[中文](memprobe-stability-plasticity.md) | **English** · [Home](../README.en.md) · [Benchmark Library](../library/README.en.md)

<!-- EVIDENCE:reading:START -->
## Reading coverage and sources

Full text reviewed: paper v1 methods, experimental setup, principal results, limitations and Appendices A–H, checked against pinned implementation details. No independent experiment reproduction.

[arXiv:2609.30558v1](https://arxiv.org/html/2609.30558v1) · [Pinned adapter details](https://github.com/jq-ding/MemProbe/blob/9068d8d9a2a47268fe6f7601b99a56a283c37be5/IMPLEMENTATION_DETAILS.md)

The tables below reorganize reported facts to explain the conclusions; they are not a current leaderboard. Reported findings, evidence gaps and this note's interpretation are kept distinct.
<!-- EVIDENCE:reading:END -->

<!-- EVIDENCE:method:START -->
## What measurement object changes?

This September paper by Jiaqi Ding and Guorong Wu is distinct from Ma et al.'s June [MEMPROBE / MemAudit](memprobe.en.md), which reconstructs hidden user state from final memory artifacts. Here, reusable paradigm specifications and a scoring protocol ask when a memory should be updated, preserved, or treated as uncertain.

The sequence is: reset one episode's memory → ingest sessions chronologically → obtain the system's memory/retrieved context → query a common reader → score typed fields. Four paradigms manipulate interference from similar facts, source credibility, prior reinforcement, and the timing of new evidence after reactivation. These are experimental conditions, not four established independent abilities.

**Illustrative toy example, not a dataset row:** the old deployment port is 8080; a trusted deployment log confirms 9090; a colleague later tentatively mentions 7070. Answering only “9090” misses the diagnosis: the system must also recover 8080, identify the update source, and recognize that 7070 was not accepted. Separate scores distinguish failed updating, inappropriate overwriting and provenance loss.

Relative to LongMemEval and MemoryAgentBench, the increment is separately observing updating, preservation, and historical/source/temporal information. It does not replace MemoryArena's closed-loop action utility. Source: [Sections 3–4 and Appendices B–C](https://arxiv.org/html/2609.30558v1).
<!-- EVIDENCE:method:END -->

<!-- EVIDENCE:setup:START -->
## How it is evaluated, and what is not matched

| Factor | Reported setting |
|---|---|
| Data | 56 episodes, 1,246 sessions, 224 nominal probes; 14 episodes per paradigm; 12 split-evidence and 44 non-split episodes |
| Construction | English text; personal, work and tool-state facts; human-designed/audited latent controls and labels, substantial GPT-5.4-assisted dialogue surface generation |
| Models | Final reader gemini-3-flash-preview; configurable internal memory calls gemini-2.5-flash; embedding backends differ |
| Scoring/denominators | Typed fields, with partial credit for conflict and temporal probes; execution/parsing errors are excluded from relevant denominators, so 224 is not an independently reconciled effective count for every cell |
| Uncertainty | 95% intervals from 2,000 episode-level bootstrap resamples, not variation across independently trained runs |
| Resources | Fixed final reader, but evidence volume, token budget, writing implementations and ingestion success are not fully matched |

| Configuration | Reader input | Comparison boundary |
|---|---|---|
| Mem0 / LangMem | All final facts | No common top-k or token budget matched against the other adapters |
| Graphiti | Top-15 edge facts | About 178 of roughly 1,100 session additions skipped after malformed JSON; graph built from remaining sessions |
| Cognee | Top-15 graph context | Uses only_context rather than its native final answer generator |
| A-MEM | Top-15 notes | Local all-MiniLM-L6-v2 embeddings; session types enter tags/categories, requiring a potential metadata-advantage audit |
| MemoryOS | Retrieved pages plus user/assistant knowledge | Short-term capacity 7; hierarchical-memory/model-call patches, no common evidence-budget claim |
| Naive RAG / Time-aware RAG | Top-5 keyword-retrieved sessions | The latter adds true temporal positions; Oracle bypasses retrieval and supplies non-filler evidence |

Sources: paper Section 4, Appendices A–C and [pinned implementation details](https://github.com/jq-ding/MemProbe/blob/9068d8d9a2a47268fe6f7601b99a56a283c37be5/IMPLEMENTATION_DETAILS.md). [Paper](https://arxiv.org/html/2609.30558v1)
<!-- EVIDENCE:setup:END -->

<!-- EVIDENCE:main-results:START -->
## Core evidence: what an aggregate hides

Main suite, 56 episodes / 224 nominal probes; shared final reader Gemini-3-Flash-preview.

| Configuration | Overall accuracy (%) and 95% interval | Update accuracy (%) | Preserve accuracy (%) |
|---|---|---|---|
| Mem0 | 41.5 [35.7, 46.9] | 28.6 | 54.5 |
| Graphiti | 62.5 [55.8, 68.8] | 58.9 | 66.1 |
| LangMem | 65.2 [57.6, 72.3] | 63.4 | 67.0 |
| Cognee | 81.7 [76.3, 86.6] | 75.0 | 88.4 |
| A-MEM | 88.4 [83.9, 92.4] | 91.1 | 85.7 |
| MemoryOS | 60.3 [53.6, 66.5] | 54.5 | 66.1 |

The update column uses conditions requiring a valid update; preserve uses conditions requiring resistance to weak/unreliable evidence. Their harmonic mean is the paper's SP-Balance, not overall accuracy. A-MEM is stronger on updating while Cognee scores higher on preservation: a higher aggregate does not mean stronger behavior on every dimension. These are configuration observations, not a budget-matched architecture ranking.

Fact sources: paper Tables 1–2, Sections 4.2/5.2; selected metrics reorganized here. [Source](https://arxiv.org/html/2609.30558v1)
<!-- EVIDENCE:main-results:END -->

<!-- EVIDENCE:diagnostics:START -->
## How much split evidence changes the diagnostic references

Same main suite and Gemini-3-Flash-preview reader; diagnostic references receive different evidence inputs and are not pooled with memory systems.

| Reference | Overall accuracy (%) | Split-episode accuracy (%) |
|---|---|---|
| Naive RAG | 68.3 | 29.2 |
| Time-aware RAG | 68.8 | 33.3 |
| Full-context | 88.8 | 81.2 |
| Oracle RAG | 93.3 | 89.6 |

Split evidence places the update trigger/source and the accepted new value in different sessions, across 12 episodes; column denominators must not be pooled. Time-position labels move that subset from 29.2 to 33.3, whereas clean evidence reaches 89.6. This motivates inspecting evidence access/integration, but Oracle also removes distractors and does not isolate retrieval's causal contribution. Full context is not a theoretical ceiling.

Fact sources: paper Tables 1 and 7; only overall and split-episode metrics are reorganized here. [Source](https://arxiv.org/html/2609.30558v1)
<!-- EVIDENCE:diagnostics:END -->

<!-- EVIDENCE:probe-reversal:START -->
## Why probe-level behavior matters

Main suite and Gemini-3-Flash-preview reader; probe types are reported separately as different measurement targets.

| Configuration | Current-value accuracy (%) | Previous-value accuracy (%) |
|---|---|---|
| Graphiti | 66.1 | 96.4 |
| LangMem | 80.4 | 67.9 |

Graphiti and LangMem reverse direction across the two probe types. The authors report a 28.5 percentage-point historical-value gap, paired bootstrap interval +9.1 to +48.3, p=0.002. It remains a difference between complete adapter configurations, not automatic causal evidence for a storage architecture.

Fact source: Section 5.2, comparison paragraph after Table 3; retain its decimal precision rather than mixing Table 5's rounded display. [Source](https://arxiv.org/html/2609.30558v1)
<!-- EVIDENCE:probe-reversal:END -->

<!-- EVIDENCE:reader-sensitivity:START -->
## Sensitivity to the final reader

Fix the already generated main-suite memories and change only the final reader; scores are overall accuracy (%).

| Configuration | Gemini-3-Flash-preview (%) | Qwen3-32B (%) |
|---|---|---|
| A-MEM | 88.4 | 72.8 |
| Graphiti | 62.5 | 61.6 |
| LangMem | 65.2 | 60.3 |

A-MEM's absolute score drops substantially, while Graphiti and LangMem exchange order. The authors report no significant overall difference among the three middle configurations (all pairwise p>0.37); this is near-tie sensitivity, not a meaningful ranking reversal. Scores are therefore not reader-independent memory-quality constants. This ablation fixes already generated memories and changes readout; it does not match ingestion reliability or retrieval budgets across systems.

Fact source: paper Table 4, three selected configurations. [Source](https://arxiv.org/html/2609.30558v1)
<!-- EVIDENCE:reader-sensitivity:END -->

<!-- EVIDENCE:limitations:START -->
## Claim ceiling, remaining gaps and the next discriminating experiment

- **A provenance failure does not establish storage loss.** The paper labels missing provenance in retrieved context as “storage-side.” Without inspecting the full store and another retrieval policy, retrieval failure remains possible. A common reader does not remove upstream evidence mismatch.
- **The paradigms are not independent axes.** Across six systems, Appendix D reports mean Pearson correlation 0.93 and minimum 0.85 across paradigms, versus minimum 0.43 across probe types. More independent diagnosis comes from probe decomposition; four paradigm scores are not four orthogonal abilities.
- **Do not pool other experiments.** Appendix E Tables 11–13 separately report validation results (full context 95.5%), while main Table 1 and cross-model Table 14 give 88.8%; the paper does not sufficiently explain the discrepancy, so the values remain separate and unpooled. The separate 40-episode suite changes generator, reader, fact types and length jointly, so it is neither a single-factor replication nor another row in the same leaderboard.
- **External validity remains limited.** Controlled synthetic/adapted English text does not establish real long-lived action utility, multilingual or multimodal generalization. Full lifecycle costs are not matched in these tables.
- **Next experiment.** Match ingestion success, embeddings, metadata access and evidence/token budget. Evaluate supplied-correct-evidence, system-retrieved evidence and direct-store inspection separately. Report effective denominators, exclusions and uncertainty by probe type before attributing retention/update mechanisms.

These boundaries are this note's analysis of [Sections 5–6 and Appendices C–G](https://arxiv.org/html/2609.30558v1) and the [implementation details](https://github.com/jq-ding/MemProbe/blob/9068d8d9a2a47268fe6f7601b99a56a283c37be5/IMPLEMENTATION_DETAILS.md). No independent reproduction is reported.
<!-- EVIDENCE:limitations:END -->

<!-- RESEARCH-DECISION:START -->

## Research decision

Use it to separate missed valid updates from inappropriate overwriting, and inspect whether history and provenance survive together. Existing result files retain separate main-suite configuration records; full context and Oracle are not treated as products.

[LongMemEval](longmemeval.en.md) · [MemoryAgentBench](memoryagentbench.en.md) · [MEMPROBE / MemAudit](memprobe.en.md) · [MemoryArena](memoryarena.en.md)

<!-- RESEARCH-DECISION:END -->
