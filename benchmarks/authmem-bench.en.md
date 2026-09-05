# AuthMem-Bench: Memory must preserve authority, not only content

[中文](authmem-bench.md) | **English** · [Back to Radar](../README.en.md) · [Benchmark Library](../library/README.en.md)

[Paper](https://arxiv.org/abs/2608.01679)

## What it measures

AuthMem-Bench tests whether persistent-memory consolidation preserves **source authority**. Its paired design holds the focal claim and downstream task fixed while changing only source authority, exposing whether consolidation launders low-authority content into reusable facts or instructions.

## What changed relative to prior evaluation

Benchmarks such as GateMem made access control in shared memory measurable. AuthMem-Bench moves the failure boundary earlier, into consolidation itself: summaries, extraction, or normalization can preserve a proposition while deleting the conditions under which it was authorized for reuse.

## Decisive evidence

The paper reports authority collapse in 48 of 49 configurations spanning seven consolidators and seven LLM backbones. In a controlled action-grounded evaluation, collapsed memories without authority metadata produce a mean unauthorized-action rate of 50.3%. In the end-to-end setting, automatically predicted and persisted authority labels reduce the observed unauthorized-action rate from 16.9% to 0.0% while benign task success remains essentially unchanged.

## What the score supports

The benchmark supports claims about preservation of authority boundaries through a memory pipeline. It does not establish complete authorization-system security: identity, production ACLs, cross-tenant isolation, provenance spoofing, and physical erasure are separate layers.

## Fair comparison contract

Match consolidator input, backbone, authority-label policy, memory write/read policy, and downstream action harness. A system supplied with human authority metadata is not the same causal treatment as one that must infer it.

## What remains unmeasured

Real multi-principal identity systems, adversarial provenance spoofing, authority drift across repeated consolidation, and governance cost in long-lived production memory stores.

## Next discriminating validation

Run a `same claim × same downstream task × source authority × consolidation depth` factorial experiment and add supplied-correct-authority metadata as an oracle condition to separate extraction, persistence, and action-policy failures.

<!-- RESEARCH-DECISION:START -->
## Research decision card
### When to use it
Use AuthMem-Bench when the claim concerns consolidation, summarization, experience extraction, or self-evolving memory preserving source constraints; it is more direct than a recall benchmark for that question.
### What a concrete task looks like
Illustrative task: the same statement comes from an authorized user or a low-authority external source. After consolidation, an identical later action request should be governed by the memory only in the authorized condition.
### Most discriminating experiment
Hold claim and action fixed, vary authority and consolidation depth, and add oracle authority metadata to separate source recognition from downstream policy.
### Pair with
[GateMem](gatemem.en.md) · [InjecMEM](injecmem.en.md) · [Utility Under Attack](utility-under-attack.en.md)
> **Score-reading rule:** authority preservation is one memory-lifecycle layer, not proof of complete deployment authorization security.
<!-- RESEARCH-DECISION:END -->

## Evolution position
`recall → shared-memory governance → provenance / authority-preserving consolidation`
