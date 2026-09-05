# PerMemSafe: personalized memory can make generic safety rules insufficient

[中文](permemsafe.md) | **English** · [Back to Radar](../README.en.md) · [Benchmark Library](../library/README.en.md)

[ACL 2026](https://aclanthology.org/2026.findings-acl.320/)

## What it actually measures

PerMemSafe evaluates **implicit personalized safety** in long-horizon self-evolving agents. A response that is generically benign may become unsafe because of user-specific risk information accumulated in memory, and that risk can emerge, change, or resolve over time.

## What changed relative to prior evaluation

Traditional safety benchmarks evaluate the current prompt against context-independent policies. Personalized-memory benchmarks usually reward richer user modeling. PerMemSafe exposes the tension: better personalization increases the amount of latent safety context the agent must correctly retrieve and reason about.

## Decisive evidence

The paper reports that even the strongest evaluated self-evolving agent achieves only around a 50% safety rate. Its SentinelMem approach explicitly models personalized risk inference and memory evolution and improves implicit personalized safety by 23.8% over prior memory frameworks while maintaining helpfulness.

## What the score supports

The benchmark supports a system-level claim about whether a memory-augmented agent recognizes user-specific risk under evolving histories. The SentinelMem gain does not isolate a single memory operation because risk extraction, updating, retrieval, and response policy are co-designed.

## Fair comparison contract

Fix backbone, conversation history, risk evolution, helpfulness tasks, safety policy, and retrieval budget. Safety must be reported with helpfulness; refusing all personalized assistance is not a useful memory system. Compare stale-risk, resolved-risk, and newly emerging-risk cases separately.

## What remains unmeasured

The benchmark cannot cover all medical/legal/physical risk types or real user consent. False personalized-risk inference can itself be harmful, and long-term privacy/governance of sensitive risk memory is a separate concern.

## Next discriminating validation

Measure calibration: when should the agent act on a remembered risk, ask for clarification, or discard it as stale? The key frontier is not merely remembering safety context, but controlling confidence and lifecycle of personalized risk beliefs.

<!-- RESEARCH-DECISION:START -->

## Research decision card

### When to use it

Use PerMemSafe when a current request is benign in isolation but requires caution given personal history. Personalized safety requires both retention of relevant risk and updating when circumstances change. Persistently applying obsolete risk can also reduce helpfulness.

### What a concrete task looks like

Illustrative task: an earlier history establishes a personal restriction relevant to a service choice, and a later session explicitly revises it. A new request requires the operative state rather than automatic reuse of the earliest safety judgment.

### Most discriminating experiment

Pair histories with an active risk, a resolved risk, and no relevant risk while holding the current request fixed. Measure both omission of relevant history and overuse of obsolete risk, reporting safety alongside helpfulness to distinguish updating from blanket conservatism.

### Pair with

[longmemeval](longmemeval.en.md) · [memtrapbench](memtrapbench.en.md)

> **How to read scores:** align task / split, model and harness, tools and environment versions, resource budget, stopping and retry rules, and evaluator. Aggregate scores from different protocol cells are system-level evidence first; without a matched intervention or ablation, do not attribute the gap directly to one component.

<!-- RESEARCH-DECISION:END -->

## Genealogy

`generic safety → personalized memory → evolving personalized risk state`

PerMemSafe shows that personalization and safety are coupled objectives, not independent modules.