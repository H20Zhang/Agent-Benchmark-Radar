# StructMemEval: evaluating how agents organize memory

[中文](structmemeval.md) | **English** · [Back to Radar](../README.en.md) · [Benchmark Library](../library/README.en.md)

[Paper](https://arxiv.org/abs/2602.11243)

## What it actually measures

StructMemEval asks whether an agent can choose and maintain a **task-appropriate memory structure**—for example a transaction ledger, to-do list, or tree—rather than only retrieving facts from an undifferentiated store. The central capability is representation organization.

## What changed relative to prior evaluation

Fact-retention, multi-hop recall, and temporal-update benchmarks can often be attacked with generic retrieval-augmented context. StructMemEval constructs tasks whose natural solution depends on a particular organization, making memory structure itself observable rather than treating storage layout as an implementation detail.

## Decisive evidence

The paper's initial experiments show simple retrieval-augmented LLMs struggle on the structured tasks. Memory agents can solve them reliably when explicitly prompted with the appropriate organization, but modern LLMs do not consistently recognize the needed structure without such hints. This separates **executing a known representation** from **discovering the right representation**.

## What the score supports

The benchmark can show whether a system benefits from structured state and whether it can instantiate a requested organization. It is weaker evidence for autonomous representation learning if the task or prompt reveals the intended structure.

## Fair comparison contract

Fix backbone, task instructions, whether structure hints are available, memory operations, and token/storage budget. Results with an oracle structure hint should be reported separately from autonomous structure selection; otherwise the main research question is hidden.

## What remains unmeasured

The task suite is intentionally narrow and uses human-interpretable structures. Real agents may need hybrid or learned representations whose utility is only visible through future queries/actions, and they may need to migrate structure as workloads change.

## Next discriminating validation

Hide structure identity, introduce tasks with multiple plausible organizations, and measure adaptation when query distributions shift. The key question is not whether an agent can use a ledger, but whether it knows when a ledger is the right representation.

<!-- RESEARCH-DECISION:START -->

## Research decision card

### When to use it

Use StructMemEval to test whether explicit memory organization affects task completion, particularly for tables, lists, and trees. Distinguish operating a prescribed structure from discovering a suitable structure autonomously. Scores with structure hints do not establish the latter.

### What a concrete task looks like

Illustrative task: a stream adds, retracts, and revises items, requiring a queryable operative state. An append-only transcript preserves all utterances but may not support later operations as directly as a ledger or tree.

### Most discriminating experiment

Separate no-hint, autonomous-structure-selection, and supplied-correct-structure conditions. Hold the input constant while changing later query types, then test whether the representation adapts. Include migration cost and repair of incorrect state when assessing adaptation.

### Pair with

[memoryagentbench](memoryagentbench.en.md) · [kbgym](kbgym.en.md)

> **How to read scores:** align task / split, model and harness, tools and environment versions, resource budget, stopping and retry rules, and evaluator. Aggregate scores from different protocol cells are system-level evidence first; without a matched intervention or ablation, do not attribute the gap directly to one component.

<!-- RESEARCH-DECISION:END -->

## Genealogy

`retrieve facts → maintain structured state → autonomously choose memory representation`

StructMemEval exposes representation selection as an independent memory capability.