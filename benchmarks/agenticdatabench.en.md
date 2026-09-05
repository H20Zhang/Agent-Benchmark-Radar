# AgenticDataBench: fine-grained skills behind realistic data-science tasks

[中文](agenticdatabench.md) | **English** · [Back to Radar](../README.en.md) · [Benchmark Library](../library/README.en.md)

[Paper](https://arxiv.org/abs/2607.01647) · [Project](https://agenticdatabench.github.io/) · [Code](https://github.com/AgenticDataBench/AgenticDataBench) · **Area: Data Agent**

AgenticDataBench is valuable not merely because it adds more end-to-end data-science tasks, but because it attaches **fine-grained skill labels** to them. The goal is to move from “did the task succeed?” toward “which recurring capability is actually failing?”

## What it actually measures

The benchmark contains **344 tasks across 15 domains and 97 real-world datasets**, totaling about **27.3 GB / 123.1M rows**, with **433 ground-truth skill labels**.

Each realistic data-science task is therefore evaluated at two levels:

- end-to-end: did the task succeed?
- diagnostic: do failures cluster around particular required competencies?

This is much more useful for capability coverage analysis than a single aggregate accuracy alone.

## What changed relative to prior evaluation

A central weakness of many data-science benchmarks is that the **task distribution itself is opaque**.

A five-point score gain may come mostly from task-mix effects. A benchmark may look difficult because a small number of unusual task patterns dominate failures. Without skill annotations it is hard to ask:

- how much data understanding, cleaning, statistics, modeling, debugging, and other work is represented;
- whether an agent has a broad capability gap or one high-frequency bottleneck;
- whether a new method improves core competence or one benchmark-specific task pattern.

AgenticDataBench turns these questions into measurable objects through an explicit taxonomy.

## How the evaluation works

The benchmark provides both a DevSet and a TestSet. The TestSet executes agent code in a sandbox and captures execution traces, so evaluation can verify actual execution rather than trusting a model's final claim of completion.

Interpreting results requires recording:

- task and dataset version;
- sandbox and package environment;
- tool availability;
- model and agent harness;
- execution and retry budget;
- skill distribution;
- aggregate metrics and per-skill breakdowns.

Reporting only the total score discards the benchmark's most distinctive diagnostic value.

## Decisive evidence and score boundary

Human performance is reported around **84–90%**. The key implication is not a literal universal human ceiling, but that the benchmark preserves substantial headroom while remaining within a realistic range of solvable work.

Per-skill results can support a diagnosis such as “this class of task repeatedly fails under the current system.” They do not prove that the model lacks an independent internal skill module.

A single task often requires several capabilities, and a skill label describes task requirements rather than causally decomposing the system's internal mechanism.

## Main confounders

The first is the **skill ontology itself**. The taxonomy is a benchmark-design choice; different ontologies can partition the same failure differently.

The second is **multi-skill interaction**. A failure originating in data understanding may surface as code-execution failure, so labels alone do not identify root cause.

The third is **agent-harness sensitivity**. The same model can expose very different skill profiles under different scaffolds, tool contracts, or retry policies.

The fourth is **hidden-set consumption**. Repeated tuning against the TestSet can turn skill diagnostics into benchmark-specific optimization.

## Fair comparison contract

At minimum, align:

- task and dataset version;
- sandbox, dependencies, and resource limits;
- tool set and data-access interface;
- model, agent harness, and system prompt;
- execution, retry, and token budgets;
- evaluator;
- Dev/Test usage boundary.

Alongside aggregate scores, report sample counts and uncertainty for each skill slice; tiny slices should not support strong conclusions.

## What remains unmeasured

AgenticDataBench improves coverage transparency but does not fully measure:

- whether skill labels have causal diagnostic value;
- business semantics and ambiguous-requirement clarification;
- longitudinal data and schema changes;
- collaboration and review workflows;
- governance, permissions, and irreversible data operations;
- whether different skill failures have comparable severity.

Production systems ultimately care not only about average weakness, but **which failures silently corrupt downstream decisions**.

## Next discriminating validation

A high-value next step is a **skill intervention test**: construct matched task pairs that differ systematically in one required competency, then add a targeted intervention for that skill.

If the intervention primarily improves the predicted slice while leaving unrelated slices mostly unchanged, the taxonomy becomes a more credible diagnostic coordinate rather than merely a post-hoc labeling scheme.

A further extension is a `skill × harness × backbone` matrix to test whether observed skill weaknesses remain stable across system choices.

## Genealogy

`end-to-end data tasks → skill-labeled coverage → causal capability diagnosis → capability-targeted improvement`

AgenticDataBench completes the second step. The next challenge is not adding more labels, but proving that those labels genuinely guide system improvement.
