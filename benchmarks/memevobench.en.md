# MemEvoBench: safety under memory mis-evolution

[中文](memevobench.md) | **English** · [Back to Radar](../README.en.md) · [Benchmark Library](../library/README.en.md)

[Paper](https://arxiv.org/abs/2604.15774)

## What it actually measures

MemEvoBench asks whether an agent remains safe when its memory **evolves in the wrong direction** over repeated interaction. Misleading memories, noisy tool outputs, and biased feedback are accumulated across rounds, so the failure object is not a single prompt injection but a progressively corrupted internal evidence base.

## What changed relative to prior evaluation

Static safety benchmarks test whether a model resists a harmful prompt in one episode. Memory benchmarks usually score useful retention. MemEvoBench intersects the two: the agent may behave safely at the start yet become less safe because earlier observations are written, reinforced, and reused. It therefore evaluates the update policy and downstream reuse of memory as part of the attack surface.

## Decisive evidence

The benchmark contains QA-style tasks spanning seven domains and 36 risk types, plus workflow tasks adapted from 20 Agent-SafetyBench environments. It constructs mixed pools of benign and misleading memory and follows behavior over multiple rounds. The paper reports substantial safety degradation as misleading evidence persists; static prompt-level defenses are insufficient to prevent the longer-horizon effect.

## What the score supports

A degradation curve across rounds supports a system-level claim about **memory-update robustness** under the specified corruption process. It does not isolate whether the root cause is write admission, consolidation, retrieval, trust calibration, or the base model's susceptibility after retrieval.

## Fair comparison contract

Fix the corruption schedule, benign/malicious memory ratio, tool outputs, backbone, retrieval budget, and number of rounds. Report utility on benign memory together with attack/safety metrics: a policy that simply refuses to store or use memory can appear safe while destroying the purpose of memory.

## What remains unmeasured

Real attackers may adapt strategically rather than follow a fixed corruption generator, and long-term memory can contain access-control or deletion constraints not represented by poisoning alone. Recovery after the agent discovers a contradiction is also distinct from resistance before corruption.

## Next discriminating validation

Factor the lifecycle into admission, consolidation, retrieval, and use, then inject the same misleading evidence at one stage at a time. The highest-leverage question is whether robust memory requires better filtering at write time or calibrated verification at use time.

<!-- RESEARCH-DECISION:START -->

## Research decision card

### When to use it

Use MemEvoBench to study safety degradation across repeated memory updates, not only one-shot prompt injection. The central issue is accumulation through writeback. A final attack-success rate alone misses the degradation path and the cost of repair.

### What a concrete task looks like

Illustrative task: an agent stores feedback after ordinary tasks, with a small portion being misleading. Later decisions drift over repeated updates. Trace when incorrect content was written, when it was retrieved, and whether correction succeeds.

### Most discriminating experiment

Hold the benign task stream fixed and compare clean, noisy, and misleading feedback round by round, tracking both safety and legitimate utility. Compare selective removal of implicated records with a full reset to test targeted recovery rather than wholesale forgetting.

### Pair with

[injecmem](injecmem.en.md) · [utility-under-attack](utility-under-attack.en.md)

> **How to read scores:** align task / split, model and harness, tools and environment versions, resource budget, stopping and retry rules, and evaluator. Aggregate scores from different protocol cells are system-level evidence first; without a matched intervention or ablation, do not attribute the gap directly to one component.

<!-- RESEARCH-DECISION:END -->

## Genealogy

`memory utility → memory update dynamics → adversarial memory evolution`

MemEvoBench makes memory maintenance—not only retrieval—a safety-critical evaluation coordinate.