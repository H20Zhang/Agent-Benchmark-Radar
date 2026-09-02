# Utility Under Attack

## What it actually measures

Utility Under Attack reframes memory security from “does the attack succeed?” to **how much benign long-term-memory utility is lost after a small amount of malicious memory enters the system, and how much legitimate evidence a defense sacrifices while trying to stop it**. It combines a LongMemEval-style benign task with false-fact poisoning, write-time screening, and provenance-aware retrieval in one security–utility contract.

## What changed relative to predecessors

MPBench establishes a broad taxonomy of persistent poisoning and emphasizes attack exposure/success. This work focuses on the relatively simple false-fact class and makes **retained benign utility** a primary outcome. That exposes two failures that attack-success metrics can hide: substantial utility loss even with a small poison fraction, and defenses that reduce attack exposure by making legitimate evidence unreachable.

## Decisive evidence

With only **1.2% of the corpus poisoned**, accuracy falls from **0.850 to 0.300**. The evaluated write-time pipeline rejects **0 of 360 poisoned memories**. Strong provenance weighting recovers some performance but drives recall for untrusted answer evidence to **0**. In the tested similarity distribution, content-only screening and simple additive provenance therefore exhibit a clear structural security–utility trade-off.

## What the score supports

The results support the claim that a small amount of false-fact poisoning can substantially degrade utility in the tested memory stack, retriever, embedder, and reader, and that the evaluated simple defenses trade security for access to benign evidence. They do not establish that all defenses fail, and residual utility cannot be attributed to retrieval alone because reader abstention also affects final accuracy.

## Fair comparison contract

Memory stack, embedder, retrieval top-k, reader, poison rate, poison-similarity distribution, and provenance prior should be aligned. A defense should report poisoned-record exposure, benign recall, answer accuracy, and abstention together rather than only attack rejection. Provenance-ranking weights are not directly comparable when source-quality distributions differ.

## How to use it in research

The benchmark is useful for detecting defenses that merely become more aggressive information rejectors. Admission filters, provenance ranking, conflict resolution, and memory consolidation methods should be compared through a **security–utility frontier**, with attribution of gains to reduced poison exposure, preserved trusted evidence, or better reader abstention.

## Next discriminating validation

The main gaps are adaptive attacks, realistic provenance distributions, additional memory stacks, and the proposed occupancy gate. The highest-value next study would compare defenses under the same benign workload and adaptive attacker and determine whether any method genuinely dominates the baseline Pareto frontier rather than moving along the same trade-off.

## Genealogy

The benchmark advances memory-attack evaluation from attack success to joint security–utility measurement; `map_delta=reinforces`. Together with MPBench and InjecMEM, it separates **write exposure, retrieval exposure, generation success, and benign utility** into distinct memory-security coordinates.

Primary: https://arxiv.org/abs/2608.21230
