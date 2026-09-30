# DreamBench-SWE: Using hidden earlier-session evidence in code changes

<!-- RELEASE-REFERENCE:START -->
> **Best at release (not yet verified)** · Benchmark recorded date: 2026-08-21<br>
> A best result tied to a model, metric, and protocol in the initial release has not yet been verified. [Original source](https://arxiv.org/abs/2608.20664)<br>
> No substitution from a live board, a single baseline, or a later paper; unknown is neither zero nor a claim that the authors reported no results.
<!-- RELEASE-REFERENCE:END -->

[中文](dreambench-swe.md) | **English** · [Benchmark Library](../library/README.en.md)

<!-- EVIDENCE:reading:START -->
## Reading scope and version

The full primary paper was read for methods, setup, results and limitations; experiments were not independently reproduced.

Read the full 67-page first-version paper, Sections 1–9 and Appendices A–H, including per-trap audits, original/successor identities, preregistration, construct quotas, clustered inference, execution/scoring details, glossary and integrity limits. The original v2.0.5 study and additive v2.1.0 audit are separate; manuscript and experiment version numbers are different. Code and private raw logs were not independently verified.

[Full primary paper](https://arxiv.org/pdf/2608.20664v1) · 2608.20664v1
<!-- EVIDENCE:reading:END -->

<!-- EVIDENCE:placement:START -->
## Relation to neighboring evaluations

Relative to SWE-bench, the target moves from a single issue fix to repository continuation across sessions: can later code use a convention observed earlier but not inferable now? MemoryArena, EvoMemBench and STATE-Bench already cover multi-session or execution-oriented memory, so the narrower new coordinate combines SWE-specific scope, stale facts, generated-file provenance and faulty lessons with hidden executable checks. Controlled fixture repositories are used rather than a direct extension of SWE-bench issues. “Sleep” means offline trajectory processing and “dream” means a derived replay or repair artifact.
<!-- EVIDENCE:placement:END -->

<!-- EVIDENCE:method:START -->
## Task and evidence construction

Each trap has setup sessions S1/S2 and a scored S3 task. Earlier sessions inject project rules, reviewer feedback or invalidation evidence; S3 must produce a nonempty production-code change checked by hidden external tests. For example, S1/S2 specify an exact private export marker, while S3 asks for export functionality without revealing that marker in the current prompt or agent filesystem. Cryptographic randomness fills author-written placeholders. Remembering the marker still requires correct implementation, not copying a complete solution patch.

Original v2 contains 60 traps: 22 earlier tasks, eight synthesis-pilot tasks and 30 newly authored tasks. Ten constructs cover verbatim retention, retrieval under interference, supersession, propagation, scope, provenance conflict, cross-session synthesis, source-of-truth workflows, spurious-lesson rejection and abstention from irrelevant memory. Ordinary tasks inherit earlier production edits even after oracle failure if patches apply and satisfy editing policy; 13 clean-start traps reset S3 to the frozen base while retaining memory. Three seeds are repeated observations of the same trap, not three times as many independent questions.

The reference probe preserves immutable raw trajectories and maintains derived memories with type, provenance, scope, confidence, risk and validity metadata. Offline operators consolidate, extract failure lessons, generate evidence-grounded counterfactual replay, repair contradictions and suppress stale records. Deletion changes derived-record status without destroying raw evidence. Read-time gates filter before ranking under a token budget. Typed-only uses the derived pipeline, raw-only exposes event capsules, and hybrid combines them. B5 deterministically stores one verbatim event per trajectory; it is not stock Mem0. B6 is likewise a subtask-memory substitute rather than a faithful external implementation.
<!-- EVIDENCE:method:END -->

<!-- EVIDENCE:setup:START -->
## Experimental setup and scoring

The principal wake and maintenance/diagnostic model is GPT-5.5 through Codex CLI 0.142.0 in a node:22-slim-based image. The agent container includes git and Codex but no Python/pytest, so the agent cannot self-test; an external scorer applies production diffs and runs hidden checks. Edits to tests, Git metadata and import hooks are forbidden. Hidden oracles, reference patches, sequence records and analysis files are not mounted. This is filesystem isolation, not network isolation. Early unisolated results were invalidated; canary/scanner checks support the reported boundary without proving absence of all external leakage.

Each complete condition has 60 traps × three seeds = 180 valid S3 cells. Pass@1 excludes timeout-then-pass outcomes. Inference clusters by the 60 traps, exchanging labels for all seeds within a trap using exact sign permutations and Holm correction. Original v2’s six comparisons remain separate from successor v2.1’s families. The successor was designed after original results but frozen before its own outcomes; four admitted conditions completed 720/720 S3 cells. Only the hosted Mem0 literal-storage configuration with fact inference disabled was admitted: mem0ai 2.0.11, isolated namespaces, six retrieved items and a 1,200-token read budget. Native Mem0 and two Supermemory configurations failed pre-evaluation conformance/repair gates, not performance tests. Main outcomes are executable; model-derived hygiene labels are not independent task scores. Complete tool/generation stopping limits are not consolidated in the text; exact reproduction also requires frozen configurations and private scoring assets.
<!-- EVIDENCE:setup:END -->

<!-- EVIDENCE:result-1:START -->
## Original v2: primary system comparison does not reject

Original v2, GPT-5.5/Codex with hidden executable S3 checks. Sixty traps × three seeds; Pass@1 is a 0–1 proportion and intervals are trap-cluster bootstrap intervals. Hybrid versus B5 has 21/15 discordant wins/losses, clustered P1 p=0.518419 and six-comparison Holm p=1.000.

| Condition | Passes /180 | Pass@1 | Clustered 95% interval |
|---|---|---|---|
| B0 | 21 | 0.117 | [0.050, 0.200] |
| B5 | 89 | 0.494 | [0.378, 0.617] |
| DF typed-only | 80 | 0.444 | [0.333, 0.556] |
| DF raw-only | 84 | 0.467 | [0.350, 0.578] |
| DF hybrid | 95 | 0.528 | [0.422, 0.633] |

Source: Tables 7 and 9 · [Paper](https://arxiv.org/pdf/2608.20664v1)
<!-- EVIDENCE:result-1:END -->

<!-- EVIDENCE:result-2:START -->
## Successor v2.1: discrimination without identified mechanism

Separately frozen successor audit, the same 60 traps and three repeated seeds, 180 valid S3 cells per condition. Rates are 0–1 proportions; exact permutation inference clusters by trap. Family A retains all six slots, including three unavailable slots at p=1. The B0 dash means no self-comparison, not a missing or zero p-value.

| Condition | Passes /180 | Pass rate | Holm p versus B0 |
|---|---|---|---|
| B0 | 21 | 0.1167 | — |
| B5 | 82 | 0.4556 | 0.00129625 |
| DF-hybrid | 83 | 0.4611 | 9.36294e-06 |
| B5-MEM0-LIT | 97 | 0.5389 | 3.92602e-05 |

Source: Tables 12–13 · [Paper](https://arxiv.org/pdf/2608.20664v1)
<!-- EVIDENCE:result-2:END -->

<!-- EVIDENCE:interpretation:START -->
## What the evidence supports

The original study does not establish superiority of elaborate maintenance over verbatim event memory. Hybrid has six more successful cells, but clustered P1 p=0.518419 and Holm p=1; none of the other five registered comparisons rejects. This does not prove equivalence. In descriptive ablations, removing contradiction repair scores 88/180, above typed-only’s 80/180, so individual operators are not established causal mechanisms.

The successor more clearly demonstrates benchmark discrimination: all three available memory-bearing conditions reject against B0 after correction across the fixed six-slot family. It profiles one exact hosted Mem0 configuration, not a product winner. Its secondary comparison with B5 has raw p=0.0273438 but trap-majority sensitivity p=0.21875; comparison with hybrid has p=0.162649. Both registered mechanism contrasts are unavailable because their counterpart conditions were rejected before evaluation. Historical low hosted-Mem0 scores and successor high scores belong to distinct experiments, not a causal before/after repair estimate.
<!-- EVIDENCE:interpretation:END -->

<!-- EVIDENCE:limitations:START -->
## Limits, source gaps and next test

Complete execution does not validate every construct. Original B0 warmup is 287/360=0.797, below the registered 0.80 gate, so not every S3 failure isolates memory. B0 passes all C9 spurious-lesson and C10 abstention cells, 12/12 and 6/6, leaving no intended no-memory headroom; the successor retains that defect. Hybrid useful-memory precision is 0.264 versus B5’s 0.556. Harmful-memory rate is zero for every condition, so it cannot establish harm reduction. Several hygiene metrics are collinear or task-coupled, and regression diagnostics scan failure-output substrings.

Only one wake-model family, controlled fixtures, three-session sequences and a fixed read budget are evaluated; the second-backbone transfer was not completed. Mutable hosted services and model aliases make live reruns new experiments. The successor operational table records 12,655 hybrid maintenance/diagnostic calls and about 174.205 million tokens versus B5’s 2.20936 million. Recorded costs do not impute unknown service prices, so small recorded dollar totals do not establish production efficiency. Public artifacts exclude raw hosted logs and hidden scoring assets; reading the paper is not independent verification of private evidence. Next tests should revalidate C9/C10, enable agent self-testing and preregister paired comparisons on new backbones and real repositories.

Keep experiment versions distinct: arXiv v1 reports original v2 and additive v2.1 together; successor reruns are not original-release scores. Table 8’s “Cells” pools conditions, whereas a particular system’s denominator is traps times three seeds. Some Table 10 strata cover newly authored tasks only, so their smaller denominators cannot replace full-stratum totals. The paper supports this protocol and selected-result review, but all frozen result files/private assets were not independently opened; versions, costs and significance are reported on the paper’s stated basis.
<!-- EVIDENCE:limitations:END -->
