# DynamicMem: at 2.2M-token user histories, updating becomes as important as recall

[中文](dynamicmem.md) | **English** · [Home](../README.en.md) · [Benchmark Library](../library/README.en.md)

[Paper](https://arxiv.org/abs/2606.22877) · [Code](https://github.com/wenyaxie023/DynamicMem)

## What it measures

DynamicMem generates 15 months of activity per user, averaging 2.2M tokens and 1,772 grounded events across 16 applications, with five quarterly checkpoints for State Completion and Personalized Service. The target is whether attributes, habits, and preferences remain current as life changes and are then used appropriately.

## Compared with what

Static memory QA asks whether a fact can be found. DynamicMem makes time and repeated updates load-bearing, requiring systems both to retain stable facts and replace facts that have changed.

## Decisive evidence and score boundary

The paper attributes more than 93% of failures to retrieval and reports that no evaluated system simultaneously preserves stable facts and replaces changing ones well. This supports retrieval/update coupling as a bottleneck under the synthetic trajectory and reference-profile contract, not as a deployment-level conclusion about real users.

## Fair comparison conditions

Align trajectory synthesis, app-event schema, reference profile, retrieval budget, and judge, and report quarterly checkpoints. One final-time score hides the staleness trajectory.

## Next evaluation coordinate

The next step adds real consent and permissions, unmodeled behavior, and external consequences when an incorrect profile drives tool actions.
