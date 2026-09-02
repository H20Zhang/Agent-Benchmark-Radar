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

## Genealogy

`memory utility → memory update dynamics → adversarial memory evolution`

MemEvoBench makes memory maintenance—not only retrieval—a safety-critical evaluation coordinate.