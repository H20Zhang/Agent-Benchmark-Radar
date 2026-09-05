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

<!-- RESEARCH-DECISION:START -->

## Research decision card

### When to use it

Use StatABench to connect statistical knowledge, tool use, and complete modeling reports. Closed questions and open reports provide different evidence. A polished report does not establish sound methodology, and choosing a tool name does not establish correct parameters or assumptions.

### What a concrete task looks like

Illustrative task: an agent chooses a statistical method, executes tools, and interprets results. Software can return significant-looking outputs despite violated distributional or independence assumptions, so methodological applicability matters beyond successful calls.

### Most discriminating experiment

Report knowledge, tool parameterization, and open reports separately with a fixed toolkit and evaluator. Add data violating statistical assumptions to test whether the agent adapts or withholds a conclusion. Independently review methodology in open reports.

### Pair with

[causalds](causalds.en.md) · [dare-bench](dare-bench.en.md)

> **How to read scores:** align task / split, model and harness, tools and environment versions, resource budget, stopping and retry rules, and evaluator. Aggregate scores from different protocol cells are system-level evidence first; without a matched intervention or ablation, do not attribute the gap directly to one component.

<!-- RESEARCH-DECISION:END -->
