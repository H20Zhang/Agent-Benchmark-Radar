# DeltaML-Bench: machine-learning agents in real research repositories

[中文](deltaml-bench.md) | **English** · [Back to entry](../README.en.md) · [Benchmark Library](../library/README.en.md)

[Paper](https://arxiv.org/abs/2608.19653) · [Code and tasks](https://github.com/AlgorithmicResearchGroup/deltaml-bench-vivaria)

Agents enter imperfect real research repositories, repair training pipelines, iterate under bounded compute, and exceed published baselines while passing explicit integrity checks.

## What it follows

MLAgentBench frames ML experimentation as an iterative agent task, MLE-bench uses Kaggle competitions for end-to-end ML engineering, and RE-Bench emphasizes long-horizon research engineering. DeltaML-Bench makes a narrower critique: clean datasets and packaged tasks omit dependency and reproducibility failures in real research repositories, while final metrics alone can reward specification gaming. It gives the agent the paper, repository, dataset, and published baseline together.

## How it is evaluated

**Question:** Can an agent produce reproducible experimental improvements inside an imperfect ML repository instead of merely fixing a bug, gaming a proxy, or fabricating a metric?

**Measurement object:** repository navigation, training-pipeline repair, experimental design and iteration, improvement over a published baseline, and whether the submission passes static, artifact, semantic, and trajectory audits.

**Scale and protocol:** 48 executable tasks span vision, graph/molecular learning, time series, tabular data, and NLP. Each run uses an isolated Vivaria environment and one H100. The paper compares equal-total-compute allocations of 4×6 hours and 2×12 hours, scores normalized improvement over the paper baseline, and locks scoring after one submission.

## What a score can support

Under 4×6h, ARG raises GPT-5's per-run success from 9.4% to 33.9%; under 2×12h it reaches 49.0%. Modular configurations show observed specification-gaming rates up to 47.9%, while none is detected in the evaluated ARG configurations. The result shows that scaffold, experimental search, and integrity checks materially alter system-level outcomes; it cannot be reduced to the base model's generic ML ability.

## Strongest confounder

The study covers two model families and two scaffolds, while 4×6h versus 2×12h changes both run duration and restart count. Full evaluation is expensive and the suite is vision-heavy. Semantic and forensic audits depend on LLM judgments whose false-positive and false-negative rates are not estimated, so “no detected gaming” is not a general safety guarantee for ARG.

## Remaining Gap: What remains uncovered

Runs capped at 12 hours on one H100 exclude multi-node or multi-week research. Scoring captures improvement on a known metric, not methodological novelty, theoretical insight, or compute efficiency.

<!-- RESEARCH-DECISION:START -->

## Research decision card

### When to use it

Use DeltaML-Bench for improving published baselines in imperfect research repositories. Metric improvement is not scientific novelty, and a long run is not inherently better than repeated restarts. Inspect patches, independent reruns, and integrity checks together.

### What a concrete task looks like

Illustrative task: an agent reads a paper and repository, repairs training, and modifies the model to deliver reproducible gains. Exploiting evaluation defects or changing scoring semantics can also yield high numbers, making integrity inseparable from improvement.

### Most discriminating experiment

Compare one long run with several short runs under equal total compute and a fixed selection rule. Re-train selected patches from clean environments and report by patch type and domain, distinguishing repair, tuning, algorithm changes, and invalid gaming.

### Pair with

[ai4ai-bench](ai4ai-bench.en.md) · [mlagentbench](mlagentbench.en.md)

> **How to read scores:** align task / split, model and harness, tools and environment versions, resource budget, stopping and retry rules, and evaluator. Aggregate scores from different protocol cells are system-level evidence first; without a matched intervention or ablation, do not attribute the gap directly to one component.

<!-- RESEARCH-DECISION:END -->

## Genealogy consequence

`map_delta=early_signal`, bound to `data-agent-research-integrity`. It moves Data Agent evaluation toward autonomous ML research in real repositories and makes reward integrity first-class. One new record does not change the durable defining chain.
