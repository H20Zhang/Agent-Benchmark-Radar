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

## What remains uncovered

Runs capped at 12 hours on one H100 exclude multi-node or multi-week research. Scoring captures improvement on a known metric, not methodological novelty, theoretical insight, or compute efficiency.

## Genealogy consequence

`map_delta=early_signal`, bound to `data-agent-research-integrity`. It moves Data Agent evaluation toward autonomous ML research in real repositories and makes reward integrity first-class. One new record does not change the durable defining chain.
