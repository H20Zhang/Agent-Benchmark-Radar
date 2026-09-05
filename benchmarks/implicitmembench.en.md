# ImplicitMemBench: memory that changes first behavior without recall

[中文](implicitmembench.md) | **English** · [Back to Radar](../README.en.md) · [Benchmark Library](../library/README.en.md)

[Paper](https://arxiv.org/abs/2604.08064) · [ACL 2026](https://aclanthology.org/2026.acl-long.1301/) · [Project](https://www.chonghanqin.com/project/implicitmembench/)

## What it actually measures

ImplicitMemBench measures **implicit / non-declarative memory**: whether prior learning, priming, or conditioning automatically changes an agent's first response even when the test prompt does not explicitly ask it to recall the earlier episode. It covers Procedural Memory, Priming, and Classical Conditioning under a shared learn/prime → interference → test protocol.

## What changed relative to prior evaluation

Conventional long-term-memory benchmarks reward explicit access to declarative content: retrieve a fact, answer a question, summarize a history. This benchmark changes the observable from “can the model report what it remembers?” to “does prior experience alter behavior at the moment it matters?” First-attempt scoring is important because repeated prompting would turn an implicit effect back into explicit deliberation.

## Decisive evidence

Across 300 items and 17 models, no evaluated model exceeds 66% overall. Reported aggregate scores include DeepSeek-R1 at 65.3, Qwen3-32B at 64.1, and GPT-5 at 63.0. A particularly sharp asymmetry appears between inhibition and preference behavior: 17.6% versus 75.0%, suggesting that models more readily acquire positive tendencies than suppress previously primed behavior.

## What the score supports

The score supports a claim about **behavioral adaptation from prior exposure**. It should not automatically be interpreted as evidence for an external agent-memory store: model context, prompting, latent adaptation, and explicit memory modules can all influence the behavior. This is a measurement-target contribution more than a clean component benchmark.

## Fair comparison contract

Fix the backbone/version, learning examples, interference sequence, test prompt, decoding policy, and first-attempt rule. Do not compare a system allowed explicit reflection/retrieval loops against one scored on the immediate first response; that changes implicit memory into explicit reasoning.

## What remains unmeasured

The suite does not establish durable learning across long real-world time spans, nor does it identify where the acquired behavior is represented. Safety-relevant persistence, forgetting, transfer across tasks, and interaction with external memory systems remain open.

## Next discriminating validation

Cross a fixed model with no external memory, explicit episodic retrieval, procedural summaries, and learned skill representations while keeping the test prompt identical. The key question is which representation improves first-action transfer without increasing harmful persistence.

<!-- RESEARCH-DECISION:START -->

## Research decision card

### When to use it

Use ImplicitMemBench to diagnose whether experience changes the first behavior without an explicit recall request. The focus is automatic enactment rather than factual reproduction. Behavior after a short learning episode does not establish durable cross-session external memory.

### What a concrete task looks like

Illustrative task: a learning phase demonstrates an operating convention, interference follows, and a related situation tests whether the first response follows that convention. Allowing repeated correction changes the object being measured, so first-attempt and retry success must remain separate.

### Most discriminating experiment

Keep the learning episode fixed and test within the same context, in a new session with external memory, and without memory. Increase interference distance to distinguish recency, persistence, and response bias. Same-session gains alone do not establish long-term memory.

### Pair with

[evomembench](evomembench.en.md) · [past-bench](past-bench.en.md)

> **How to read scores:** align task / split, model and harness, tools and environment versions, resource budget, stopping and retry rules, and evaluator. Aggregate scores from different protocol cells are system-level evidence first; without a matched intervention or ablation, do not attribute the gap directly to one component.

<!-- RESEARCH-DECISION:END -->

## Genealogy

`explicit recall → retained experience → automatic behavior change`

ImplicitMemBench broadens “memory” from stored information to learned behavioral bias.