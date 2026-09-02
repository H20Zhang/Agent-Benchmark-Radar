# MLAgentBench: from writing ML code to iterative experimentation

[中文](mlagentbench.md) | **English** · [Home](../README.en.md) · [Benchmark Library](../library/README.en.md)

[Paper](https://arxiv.org/abs/2310.03302) · [Code](https://github.com/snap-stanford/MLAgentBench)

## What it measures

MLAgentBench defines 13 machine-learning experimentation tasks where an agent reads existing assets, proposes changes, writes and executes code, inspects results, and iterates rather than generating one final program. Success is improvement under a fixed compute/time budget.

## Compared with what

DS-1000 measures local coding correctness. MLAgentBench turns data science into a sequential experiment loop, exposing the coupling among planning, execution, observation, and iteration.

## Score boundary

Final metric improvement supports experimentation under the named task repository, compute budget, baseline, and scaffold. It is not general data analysis, and hardware or time budget directly changes the accessible search space.

## Fair comparison conditions

Align task repository/version, baseline, compute/time budget, agent scaffold, model, and retry policy. The number of experiment rounds should accompany the outcome.

## Next evaluation coordinate

Successors should broaden task diversity and include experiment validity, artifact quality, and interpretable reporting rather than only the final metric.
