# SCALE-QA

- **Measurement object:** Whether a memory system can reconstruct the causally relevant episode in a flat, mixed-topic long-running thread when a later task decision depends on dormant local constraints, rather than merely retrieving semantically similar chunks.
- **Closest predecessor:** LongMemEval already tests cross-session reasoning, updates, and abstention but preserves timestamped session structure; SCALE-QA removes explicit boundaries and makes identifying the operative episode part of the task.
- **Decisive evidence:** The benchmark contains 3,000 audited questions across 10 domains and 4,346 exact evidence snippets; one deterministic runtime scales from 16K through 128K with a 400-question 1M diagnostic. At 128K, GPT-4o-mini Full Context scores 29.8% despite 100% evidence containment, separating “evidence is visible” from “the right episode is operationally reconstructed.”
- **Score ceiling:** The evidence supports SCALE-QA as a discriminating episode-integrity diagnostic. TSIM's 5.6–17.6 point gains over the strongest corresponding baseline across backends are system-level evidence and do not isolate segmentation, indexing, or routing as the cause.
- **Strongest confounder:** Counterfactual synthetic construction plus deterministic four-way MCQ; answerer choice, retrieval-context budget, and runtime noise construction remain part of system-level comparisons.
- **Remaining gap:** Natural long-running logs, open-ended responses, tool follow-up, and later action. The paper's LongMemEval transfer diagnostic uses transductive configuration selection and therefore is not held-out generalization evidence.
- **Genealogy:** It extends LongMemEval-style cross-session memory into recovering which interleaved episode and constraints actually bind the current task; `map_delta=early_signal`, so one work does not rewrite the durable Benchmark Map.

Primary: https://arxiv.org/abs/2608.25655
Code/data: https://github.com/LordTARN1SHED/SCALE-QA

<!-- RESEARCH-DECISION:START -->

## Research decision card

### When to use it

Use SCALE-QA for episode reconstruction in interleaved history, not a reduction of long-context memory to evidence recall. All evidence may be visible while the wrong context or constraint is applied. Treat it as a diagnostic of task binding rather than a generic retrieval leaderboard.

### What a concrete task looks like

Illustrative task: several projects interleave in a long thread without explicit boundaries, with recurring entities. A current query is governed by a local constraint from an earlier project. After retrieving entity-related snippets, the system must determine their episode membership.

### Most discriminating experiment

Keep questions and supporting evidence fixed while supplying interleaved history, correct episode boundaries, or operative state. Vary distractor length to separate episode identification from state reasoning. A reported full-context-model score is a historical baseline for that configuration, not the current best for the benchmark.

### Pair with

[came-bench](came-bench.en.md) · [statemembench](statemembench.en.md)

> **How to read scores:** align task / split, model and harness, tools and environment versions, resource budget, stopping and retry rules, and evaluator. Aggregate scores from different protocol cells are system-level evidence first; without a matched intervention or ablation, do not attribute the gap directly to one component.

<!-- RESEARCH-DECISION:END -->
