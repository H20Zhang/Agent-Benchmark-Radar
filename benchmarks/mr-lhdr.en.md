# Mr.LHDR

## Measurement object

Tests long-horizon multimodal research with final-answer accuracy and explicitly dependency-conditioned intermediate-conclusion coverage.

## What changed compared with predecessors

Compared with answer-only deep-research grading, makes prerequisite-consistent partial progress a scored object.

## Protocol and comparison controls

OA grades the final answer; SA additionally requires every checklist item. CS counts covered items; DACS grants an item credit only when its prerequisites also pass. The release separates run, judge and score.

## Decisive evidence and score ceiling

The paper reports a best 43.1% OA versus 34.3% SA. This demonstrates a final-answer/process-coverage gap under its evaluator, not that it has directly observed the system’s internal reasoning.

## Strongest confounders and limitations

The README identifies Qwen3-VL-235B for main results, while quick-start examples use another judge. Pin the judge and tool access before reproducing numbers. Heterogeneous systems and live evidence prevent simple component-level attribution.

## Coverage gap and next experiment

An annotated checklist evaluates expressed evidence and conclusions, not hidden reasoning; alternative valid solution paths may be under-credited.

Freeze evidence snapshots and one agent; compare short-answer and explicit-evidence outputs, then allow independently validated alternative dependency graphs. Bootstrap uncertainty before interpreting adjacent ranks.

## Genealogy and use

[SearchAuditBench](searchauditbench.en.md) · [ClaimProbe](claimprobe.en.md)

This entry is an `early_signal`: acceptance of a useful evaluation object does not promote one paper into a durable field-map claim.

## Primary sources and version

[Paper](https://arxiv.org/abs/2609.11318) · [Reviewed full text](https://arxiv.org/html/2609.11318v2)

[code](https://github.com/minghaoguo20/Mr-LHDR)

[data](https://huggingface.co/datasets/Henryeahhh/Mr-LHDR)

First public event: **2026-09-10**. Reviewed: **2026-09-17**. Source release and Radar acceptance are separate events.

[中文](mr-lhdr.md) · [Complete index](../library/README.en.md)
