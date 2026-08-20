# LoCoMo-Plus: From Factual Recall to Latent Constraint Consistency

[中文](locomo-plus.md) | **English** · [Back to entry](../README.en.md) · [Benchmark Library](../library/README.en.md)

[ACL Paper](https://aclanthology.org/2026.acl-long.1150/) · **Area: Agent Memory**

> **Measurement delta.** LoCoMo-Plus introduces **cue–trigger semantic disconnect**: a past user state, goal, or value forms a latent constraint that must shape a later response even when the later query does not restate that constraint.

## Predecessor / implicit critique

LoCoMo and related long-term-memory benchmarks made multi-session recall and long-context reasoning reusable evaluation targets. Many tasks, however, can still be framed as retrieving an explicitly stated past fact.

LoCoMo-Plus targets a harder personalization requirement: remembered state should constrain future behavior without a direct retrieval cue.

## What it actually measures

The benchmark evaluates long conversations in which latent user constraints must be preserved and applied later. The authors argue that string matching and explicit task-type prompting are misaligned with this setting and use **constraint consistency** as the central evaluation view.

## What a score supports

A higher score indicates stronger consistency with prior latent constraints in the benchmark response setting. It does not isolate memory storage: retrieval, state reconstruction, parametric reasoning, and harness/prompting can all contribute.

## Strongest confounder

Constraint construction and evaluation are load-bearing. Ambiguous constraints can make it difficult to distinguish reasonable adaptation from inconsistency. Explicitly telling the model that it is taking a memory test can also change the measured capability.

## What remains unmeasured

Real preference drift/conflict, action-level constraint application, permissions/authority/revocation, downstream harm from stale constraints, and matched retrieval/state-reconstruction cost remain open.

## Genealogy consequence

`multi-session factual recall → temporal/update reasoning → latent user-state constraint → future memory-guided action`

LoCoMo-Plus is an important transition/frontier signal from remembering the past toward correctly applying remembered state to future behavior.
