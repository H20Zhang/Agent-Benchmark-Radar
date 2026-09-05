# InjecMEM

## What it actually measures

InjecMEM measures **targeted persistent-memory injection**. An attacker uses one apparently ordinary interaction to write a malicious record into persistent memory; in a later independent session, a topic-relevant query may retrieve that record and cause the system to produce an attacker-selected target. The measured object therefore spans the full `write → persist/drift → retrieve → generate` trajectory.

## What changed relative to predecessors

AgentPoison and MINJA emphasize attack methods, while MPBench provides a broader persistent-poisoning taxonomy. InjecMEM narrows the question to **topic-conditioned targeted generation** and separates retrieval success, attack success conditional on retrieval, and end-to-end joint success. That decomposition exposes whether failure occurs in memory exposure or in generation after exposure.

## Decisive evidence

Multi-GCG on MemoryOS reports **46.5% RSR, 76.6% conditional ASR, and 35.6% joint ASR**. Several generic filters barely reduce conditional ASR. The combination matters more than a single attack-success number: once the malicious record is retrieved, the generation stage can still follow the target at high rates, while end-to-end success is also constrained by retrieval exposure.

## What the score supports

The results support the claim that, under the tested memory stack and white-box optimization conditions, an attack can traverse persistence, retrieval, and generation. They do not establish black-box transfer to unseen model families or isolate one MemoryOS component as the cause, because the strongest attack assumes backbone access and fused-prompt knowledge.

## Fair comparison contract

Comparisons should align backbone, memory-write policy, store/rewrite mechanism, retrieval top-k, trigger queries, attack optimization/token budget, and generation prompt. RSR, conditional ASR, and joint ASR should be reported together; otherwise a defense that merely reduces retrieval exposure can be mistaken for a safer generation policy.

## How to use it in research

InjecMEM is useful for testing whether a memory-security design protects only admission or remains robust later in the lifecycle. For a new memory architecture, the most informative ablation replaces admission, rewrite/consolidation, retrieval, and generation defenses separately while tracking joint attack success and benign retrieval utility.

## Next discriminating validation

The main gaps are rewrite-heavy stores, real deployments, adaptive defenses, and explicit security–utility curves. The highest-value next test is whether high conditional ASR persists across different backbones, memory rewrite policies, and black-box access conditions rather than further optimizing the same white-box attack setting.

<!-- RESEARCH-DECISION:START -->

## Research decision card

### When to use it

Use InjecMEM to diagnose how one low-privilege interaction can affect later answers through persistent memory. Successful writing, retrieval, and behavioral takeover are separate events. Reporting only success conditional on retrieval overstates end-to-end risk.

### What a concrete task looks like

Illustrative task: an external record attempts to blend source instructions into long-term memory, and a later benign query retrieves it. A defense must maintain the trust boundary between content and instructions without blocking legitimate information storage and use.

### Most discriminating experiment

Measure writing, retrieval, conditional behavioral deviation, and joint success separately, alongside benign blocking for the same defense. Vary writer, answerer, and summarization policy to assess transfer rather than treating one white-box setting as a bound on every deployment.

### Pair with

[mpbench](mpbench.en.md) · [utility-under-attack](utility-under-attack.en.md)

> **How to read scores:** align task / split, model and harness, tools and environment versions, resource budget, stopping and retry rules, and evaluator. Aggregate scores from different protocol cells are system-level evidence first; without a matched intervention or ablation, do not attribute the gap directly to one component.

<!-- RESEARCH-DECISION:END -->

## Genealogy

The benchmark pushes memory security from “can malicious content be written?” to the end-to-end **write → drift → retrieve → generate** path; `map_delta=reinforces`. MPBench provides breadth across attack surfaces, while InjecMEM provides finer targeted-generation attribution.

Primary: https://arxiv.org/abs/2608.23471
