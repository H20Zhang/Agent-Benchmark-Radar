# StatABench: statistical agents need both conceptual judgment and correct tool selection/execution

[中文](statabench.md) | **English** · [Home](../README.en.md) · [Benchmark Library](../library/README.en.md)

[Paper](https://arxiv.org/abs/2606.22977)

## What it measures

StatABench includes Stat-Closed with 404 questions across 18 statistical topics and four formats, 198 practical tool-use tasks over a 35-function statistics toolkit, and Stat-Open with 30 modeling competitions. It jointly measures conceptual judgment, procedure/tool selection, execution, and open modeling.

## Compared with what

General data-science benchmarks often bury statistics inside coding workflows. StatABench separates statistical reasoning from tool use, distinguishing not knowing the method from knowing it but executing the wrong function or parameters.

## Score boundary

Closed, practical, and open scores support statistical competence under their respective topic mixes, toolkits, and competitions. They are distinct evaluation settings and should not be collapsed into one ranking.

## Fair comparison conditions

Align Stat-Closed/Practical/Open track, toolkit version, data split, runtime, model access, and evaluator; open competitions also require matched compute budgets.

## Next evaluation coordinate

The next step strengthens assumption checking, uncertainty communication, and causal/statistical model criticism rather than only selecting the right function.
