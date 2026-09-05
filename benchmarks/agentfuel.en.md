# AgentFuel: stateful analysis must prove its value through reuse across queries

[中文](agentfuel.md) | **English** · [Home](../README.en.md) · [Benchmark Library](../library/README.en.md)

[Paper](https://arxiv.org/abs/2603.12483) · **Area: Data Agent / Stateful Analysis**

AgentFuel asks a narrow but important question: **when a data agent receives a sequence of related analytical queries, does carrying forward analytical state actually help?** Instead of treating memory as an implementation detail, it turns cross-query state reuse into an explicit experimental variable.

## What it actually measures

AgentFuel currently contains **72 queries across three time-series domains**, 24 per domain with 12 stateless and 12 stateful or incident-oriented queries, over about 13.5 MB of generated data.

It compares two modes:

- each query starts from scratch;
- the agent can retain notebook state, context, intermediate findings, or other analytical state for later queries.

The target is therefore not single-query competence, but whether **state reuse reduces repeated exploration and improves later incident analysis**.

## Compared with what

Most data-agent benchmarks treat each task as an independent episode. Even when a system internally uses memory, aggregate task scores rarely reveal whether that memory caused the improvement.

AgentFuel moves toward a cleaner comparison by evaluating matched stateless/stateful conditions and elevating persistence from an implementation choice to a measurable factor.

It is particularly useful for asking whether:

- intermediate findings from one query help the next;
- state avoids repeated data exploration;
- gains come from remembering results versus remembering process;
- incident analysis improves as useful history accumulates.

## How the evaluation works

An interpretable result must record query order, persistence policy, data generator, agent scaffold, model, token/tool budget, and evaluator.

**Query order is part of the protocol.** If later queries depend strongly on earlier ones, ordering changes the value of state. Conversely, if an agent can preserve the full history verbatim, the gain may collapse to simple context carry-over rather than a more structured memory mechanism.

Matched stateless/stateful pairs are therefore more informative than one aggregate headline score.

## What a score supports

If the stateful condition consistently beats the stateless condition, the supported claim is: under the current synthetic time-series distribution, query sequence, and harness, **retaining analytical state has practical value**.

That does not yet prove the system learned semantic memory or workflow experience. The gain may come from:

- cached computed values;
- preserved notebook cells;
- copied prior natural-language outputs;
- genuinely abstracted reusable semantics or analysis strategies.

These mechanisms have very different research significance, and the final score alone cannot separate them.

## Main confounders

The first is **cache versus memory**. Avoiding recomputation demonstrates reuse, but not necessarily a stronger long-term representation.

The second is **state freshness**. Production analysis includes data updates, hypothesis reversals, and closed incidents; stale state can become actively harmful.

The third is reproducibility: incomplete public generation or environment details can shift task difficulty across implementations.

## Fair comparison contract

At minimum, align:

- query sequence and matched pairs;
- what state may persist across queries;
- state capacity, compression, and deletion rules;
- data snapshot or generator;
- model, harness, and tools;
- retry, token, and execution budgets;
- evaluator and failure handling.

Methods with full-history access and methods restricted to structured state should not be merged into one track.

## What is still missing

AgentFuel does not yet fully separate:

- cache, structured semantic state, and learned workflow experience;
- robustness to stale state after data changes;
- long-horizon state growth, contamination, and contradiction;
- when the agent should forget or rebuild state;
- whether latency/token/storage savings justify state-maintenance cost.

## Most discriminating next test

A high-value extension is a **state intervention matrix**: run the same sequential queries with only raw cache, structured semantic state, workflow summaries, or full history, then inject data updates or hypothesis reversals.

If structured state remains better than raw history or cache under freshness stress, that provides much stronger evidence that the representation itself—not merely retaining more context—creates value.

<!-- RESEARCH-DECISION:START -->

## Research decision card

### When to use it

Use AgentFuel for domain-specific time-series query evaluation, particularly state and incident reasoning. Released queries and a customizable generation framework are different artifacts. Establish whether data, environments, or a generator are actually available before treating the design as turnkey software.

### What a concrete task looks like

Illustrative task: an agent determines when a state changed or how metrics behaved during an incident. A stateless aggregate cannot replace state-transition analysis, and timestamp semantics during loading can determine the answer.

### Most discriminating experiment

Pin the raw time series and temporal rules, separating stateless, stateful, and incident queries. Have connectors read equivalently validated data before comparing agents, excluding loading-semantics differences. Generated-task claims additionally need held-out domains.

### Pair with

[irts-toolbench](irts-toolbench.en.md) · [dabstep](dabstep.en.md)

> **How to read scores:** align task / split, model and harness, tools and environment versions, resource budget, stopping and retry rules, and evaluator. Aggregate scores from different protocol cells are system-level evidence first; without a matched intervention or ablation, do not attribute the gap directly to one component.

<!-- RESEARCH-DECISION:END -->

## Evolution position

`independent data query → cross-query state reuse → updateable and forgettable long-term analytical state`

AgentFuel occupies the middle step: it makes statefulness measurable, but does not yet fully evaluate dynamic, long-lived, self-correcting analytical memory.
