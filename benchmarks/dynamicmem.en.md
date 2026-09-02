# DynamicMem: maintaining a changing personal state across months

[中文](dynamicmem.md) | **English** · [Back to Radar](../README.en.md) · [Benchmark Library](../library/README.en.md)

[Paper](https://arxiv.org/abs/2606.22877) · [Code](https://github.com/wenyaxie023/DynamicMem)

## What it actually measures

DynamicMem asks whether a personal-assistant memory system can infer and maintain **attributes, habits, and preferences that evolve over time** from distributed activity across many applications. The hard part is not recalling one event; it is deciding which observations define durable profile state and when new evidence should replace an older belief.

## What changed relative to prior evaluation

Conversation-memory benchmarks usually provide explicit statements inside one dialogue stream. DynamicMem distributes weak evidence across 16 applications and roughly 15 months, then checks the profile at multiple temporal checkpoints. This turns temporal supersession and aggregation into the primary measurement object.

## Decisive evidence

The benchmark averages about 2.2M tokens and 1,772 grounded events per simulated user, with five quarterly checkpoints. The paper reports that profile reconstruction degrades as history grows even when service-task accuracy remains relatively flat; no tested system simultaneously preserves stable facts and reliably replaces changing ones. More than 93% of analyzed failures are attributed to retrieval rather than the final answer model.

## What the score supports

The result supports a claim about **dynamic personal-state tracking** under the benchmark's simulated activity distribution. The retrieval diagnosis is stronger than end QA alone, but it still depends on the benchmark's attribution procedure and does not prove one index structure is the root cause.

## Fair comparison contract

Fix event stream, checkpoint, backbone, profile schema, retrieval budget, and evidence available up to that time. Future events must never leak into earlier checkpoints. Report stable-attribute retention and changed-attribute replacement separately; an append-only system can look good on the former while failing the latter.

## What remains unmeasured

Real personal data has missingness, contradictory devices/accounts, explicit user corrections, privacy constraints, and uncertain ground truth. The benchmark also does not score the downstream harm of a stale profile relative to a missing profile.

## Next discriminating validation

Add counterfactual update events with known revocation times and downstream decisions whose correctness depends on using the newest state. This would connect profile maintenance directly to action utility and stale-memory harm.

## Genealogy

`event recall → personal profile extraction → temporally evolving user state`

DynamicMem shifts the bottleneck from “can we retrieve history?” to “which version of the user is true now?”