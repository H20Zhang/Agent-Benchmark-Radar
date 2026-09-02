# MLE-bench

## What it actually measures

MLE-bench measures whether an agent can **start from a competition description and raw data, perform end-to-end machine-learning engineering, and deliver a scoreable prediction artifact**. The agent must understand the task, inspect data, write code, train and validate models, iterate, and submit. Reconstructed test sets and historical private-leaderboard thresholds define human-relative bronze/silver/gold style success contracts.

## What changed relative to predecessors

MLAgentBench contains roughly 13 tasks and often provides stronger starting structure or baselines. MLE-bench expands to **75 from-scratch competitions** and uses historical competition outcomes to define medal thresholds. The measurement object therefore moves closer to real autonomous ML engineering rather than completion of a small research script.

## Decisive evidence

For the same GPT-4o backbone, reported **Any Medal rates are 0.8% with MLAB, 4.4% with OpenHands, and 8.7% with AIDE**; pass@6 is also substantially higher than pass@1. The important interpretation is not simply that one scaffold wins, but that measured capability is highly sensitive to scaffold and retry budget even when the backbone is held fixed.

## What the score supports

The headline score measures a **model + scaffold + retry + compute/resource system**, not pure base-model ability. Changes in best-of-n, runtime, GPU resources, tools, prompt assistance, or code templates can materially change medal rate and therefore cannot be attributed directly to reasoning or coding capability.

## Fair comparison contract

Competition version, data access, scaffold, tool interface, maximum runtime, CPU/GPU resources, retry/best-of-n policy, web access, prompt assistance, and final-submission selection should be aligned. The later official leaderboard pause for fairness/version issues is itself evidence that protocol drift is load-bearing rather than a minor maintenance detail.

## How to use it in research

MLE-bench is best treated as an evaluation of an **autonomous ML-engineering system**, not a foundation-model leaderboard. Claims about planning, memory, multi-agent orchestration, or search require matched-backbone, matched-tool, matched-compute ablations. Reporting pass@1, pass@k, resource use, and failure types is more informative than one medal rate.

## Next discriminating validation

The benchmark still does not cover problem formulation, data/metric design, messy research-repository repair, methodological novelty, or human collaboration. Another important missing coordinate is cost-normalized performance: if a system wins through more retries and more GPU time, researchers need success per token, wall-clock, and compute unit to know whether the agent is genuinely more efficient.

## Genealogy

MLE-bench anchors the autonomous ML-engineering branch of Data Agent evaluation: `MLAgentBench → MLE-bench → MLE-Dojo → DeltaML / AI4AI`; `map_delta=splits`. It establishes a large-scale terminal-outcome coordinate that later work extends toward trajectories, research process, and verification loops.

Primary: https://arxiv.org/abs/2410.07095
