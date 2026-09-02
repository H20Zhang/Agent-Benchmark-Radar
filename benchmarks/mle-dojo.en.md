# MLE-Dojo

## What it actually measures

MLE-Dojo measures an **interactive ML-engineering trajectory**, not only the final submission. In a Gym-style environment, the agent repeatedly reads the task, executes code, observes errors and HumanRank feedback, changes the experiment, and submits again. The protocol therefore exposes whether each step moves the data/model/experiment state in a useful direction.

## What changed relative to predecessors

MLE-bench mostly compresses autonomous ML engineering into a terminal competition submission. MLE-Dojo converts 200+ tasks into a repeatable training/evaluation environment with roughly **150 train and 50 evaluation tasks**. Its main measurement advance is trajectory-level observability: failure can be localized to coding, experiment choice, feedback use, or stopping rather than inferred only from the final score.

## Decisive evidence

Under a shared harness, models are compared across four task classes with HumanRank, stepwise progress, and error decomposition. The useful evidence is therefore not one leaderboard position but the ability to compare **whether an agent improves after receiving feedback** and where the improvement loop breaks.

## What the score supports

Results support the capability of a model + scaffold under **visible real-score feedback, a bounded step budget, and best-of-two evaluation**. They are not directly comparable to hidden-score MLE-bench results and do not isolate the base model, because scaffold design, feedback exposure, and search budget are load-bearing conditions.

## Fair comparison contract

Task version, visible feedback, step budget, best-of-n policy, hardware, executable tools, code scaffold, recovery rules, and HumanRank computation should be matched. Whether real score feedback is visible is a first-order protocol variable: an agent that repeatedly tunes against a score signal and a blind-submission agent are solving different evaluation problems.

## How to use it in research

For work on planning, debugging, or self-improvement in data/ML agents, MLE-Dojo is more diagnostic than a terminal Kaggle score. Mechanism ablations can remove score feedback, cap retries, fix the scaffold, or disable history/memory and then compare both stepwise progress and final HumanRank, separating orchestration gains from model capability.

## Next discriminating validation

The benchmark still does not cover problem formulation, data acquisition, metric design, repair of messy research repositories, or methodological novelty. A key external-validity question is feedback overfitting: does the agent merely hill-climb against repeated task-specific scores, or learn an ML-engineering policy that transfers to genuinely held-out task families?

## Genealogy

After MLE-bench, MLE-Dojo moves evaluation from terminal scoring to a trainable interactive trajectory; `map_delta=reinforces`. Together with DeltaML and AI4AI, it pushes Data Agent evaluation from “submit an artifact” toward the complete research/engineering loop.

Primary: https://arxiv.org/abs/2505.07782
