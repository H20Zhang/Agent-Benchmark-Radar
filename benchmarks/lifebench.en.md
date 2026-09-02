# LifeBench: long-horizon memory beyond explicit facts

[中文](lifebench.md) | **English** · [Back to Radar](../README.en.md) · [Benchmark Library](../library/README.en.md)

[Paper](https://arxiv.org/abs/2603.03781) · [Code and data synthesis](https://github.com/1754955896/LifeBench)

## What it actually measures

LifeBench evaluates whether an agent can integrate **declarative and non-declarative memory** across long, heterogeneous life-event streams. In addition to explicit episodic and semantic facts, tasks require inferring habits and procedures from repeated behavior distributed across time and sources.

## What changed relative to prior evaluation

Conversation-memory benchmarks mainly encode what the user explicitly said. LifeBench asks what can be inferred from what the user repeatedly does. Its event simulation is densely connected over long horizons and draws on real-world priors, so a useful memory representation must aggregate repeated evidence rather than treat every event as an independent retrievable chunk.

## Decisive evidence

The paper reports that top evaluated memory systems reach only 55.2% accuracy. This matters because the added difficulty is not only context length: the benchmark mixes semantic, episodic, habitual, and procedural memory across multi-source traces, requiring evidence integration and behavioral abstraction.

## What the score supports

A LifeBench score supports whole-system ability to reconstruct and reason over long-horizon life patterns. It cannot cleanly attribute gains to retrieval versus aggregation versus inference, and the synthetic event generator embeds behavioral priors that may differ from real users.

## Fair comparison contract

Fix the event stream, backbone, accessible sources, temporal cutoff, retrieval budget, and answer evaluator. Report results by memory type; an approach strong on explicit episodic facts can otherwise hide failure on habits/procedures. Prevent future-event leakage when evaluating earlier time points.

## What remains unmeasured

Real personal data is sparse, contradictory, private, and often lacks objective labels for habits or intent. The benchmark also does not establish whether inferred habits should be persisted or acted on without user confirmation.

## Next discriminating validation

Pair inferred habits/procedures with future decisions and explicit user corrections. The crucial question is whether a memory system can both infer latent patterns and revise them when the user changes behavior.

## Genealogy

`explicit conversational facts → multi-source life traces → inferred habitual/procedural memory`

LifeBench expands the memory object from what users say to recurring structure in what they do.