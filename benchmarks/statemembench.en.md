# StateMemBench

## What it actually measures

StateMemBench measures **maintenance of the currently operative state after cross-session revisions**. Facts, constraints, and decisions can be added, superseded, or linked by dependencies; the final answer must use what remains valid now rather than succeeding merely because some historical record can be recalled. The object is “what should the system currently believe and which rules are still in force,” not only local old-versus-new ranking.

## What changed relative to predecessors

LongMemEval and MemoryAgentBench already include knowledge updates, but update failures can remain entangled with retrieval, long-context understanding, and generic reasoning. StateMemBench uses symbolic event programs, deterministic replay, and a closed-pool grader to generate explicit dependencies and revision trajectories. This isolates **state drift** more directly: an output can be classified as current, targeted-superseded, or another failure.

## Decisive evidence

The benchmark contains **234 multi-session scenarios and 322 probes**. Its grader separates current, targeted-superseded, and other outcomes. The paper reports that StateMem raises the score from **0.205 to 0.363 with the same DeepSeek backbone**; a length- and cost-matched control still retains roughly a **+15–32 point** structural advantage. The important evidence is that the gain is not fully explained by simply keeping more context or spending more tokens.

## What the score supports

The results support the claim that structured current-state maintenance improves operative-state correctness under explicit dependencies and controlled revisions. They are not a general memory-quality measure and do not directly establish better long-horizon action in open environments because dependencies, revisions, and final probes are deliberately constructed.

## Fair comparison contract

Backbone, event program, visible history, state-representation budget, token/cost budget, replay policy, and grader should be fixed. Length- and cost-matched controls are especially important; otherwise a structured-state method can benefit simply from retaining more explicit information. Current-state accuracy and targeted-superseded error rate should also be reported separately so an average score cannot hide old-state leakage.

## How to use it in research

StateMemBench is useful for evaluating **state stores, versioned memory, dependency-aware update, and structured consolidation**. It complements a staleness benchmark: StateMemBench tests whether a complete current state can be reconstructed after multiple revisions, while staleness is closer to a local retrieval/ranking unit test. For an agent-memory paper, the combination localizes update mechanisms more cleanly than downstream long-context QA alone.

## Next discriminating validation

The main gaps are latent relation discovery, real user/environment drift, privacy governance, and whether better state tracking improves later closed-loop action. The highest-leverage next step is to remove explicit dependency annotations, require the agent to infer which natural-language facts supersede or constrain others, and connect state correctness to downstream tool/action success.

<!-- RESEARCH-DECISION:START -->

## Research decision card

### When to use it

Use StateMemBench to separate stale-state use from other answer errors, particularly for state maintenance and dependency updates. Its value is interpretable error typing. Collapsing all failures into incorrect answers discards the main advantage over ordinary QA.

### What a concrete task looks like

Illustrative task: a value in a plan is revised and dependent arrangements must change accordingly. After retrieving an old plan and a new event, the system must recover operative state rather than choose the most frequently mentioned description.

### Most discriminating experiment

Use the same event stream with full-evidence and supplied-operative-state controls, reporting stale-state and other errors separately. Vary revision-dependency depth while fixing text length to distinguish propagation difficulty from long-context interference.

### Pair with

[longmemeval](longmemeval.en.md) · [membench-staleness](membench-staleness.en.md)

> **How to read scores:** align task / split, model and harness, tools and environment versions, resource budget, stopping and retry rules, and evaluator. Aggregate scores from different protocol cells are system-level evidence first; without a matched intervention or ablation, do not attribute the gap directly to one component.

<!-- RESEARCH-DECISION:END -->

## Genealogy

`map_delta=early_signal`. The benchmark advances update evaluation from “are both old and new facts stored?” to “**what is the operative state now?**” This coordinate complements staleness and applicability evaluation, but independent natural-data evidence is still missing, so the durable Benchmark Map should not yet change.

Primary: https://arxiv.org/abs/2608.19652
