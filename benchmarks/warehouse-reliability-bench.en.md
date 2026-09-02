# Warehouse Reliability Bench: the dangerous failure is not merely being wrong, but looking successful while violating business truth

[中文](warehouse-reliability-bench.md) | **English** · [Home](../README.en.md) · [Benchmark Library](../library/README.en.md)

[Paper](https://arxiv.org/abs/2608.09254) · [Code](https://github.com/k-w-lee/query_proof)

## What it measures

Warehouse Reliability Bench contains 400 tasks over two deterministic synthetic warehouses: 184 directly answerable cases, 216 cases requiring clarification, abstention, or refusal, plus 80 held-out cases. Business Truth Rate and False Success Rate use executable ground truth, behavioral contracts, and rule gates to detect systems that return plausible but semantically wrong results.

## Compared with what

Traditional text-to-SQL asks whether SQL or its result matches a reference. In BI, a more dangerous failure is using the wrong metric definition, grain, join, or time semantics while still producing a plausible answer. This benchmark makes business truth and non-answer behavior first-class outcomes.

## Score boundary

Business Truth and False Success support reliability under the synthetic warehouse rules and validators. They do not capture all enterprise semantics, but they are closer to analyst risk than SQL execution alone.

## Fair comparison conditions

Align warehouse generation, business rules, behavior contract, validator version, hints, and tool budget, and inspect answerable versus clarify/abstain/refuse slices separately.

## Next evaluation coordinate

The next step uses real semantic layers, metric evolution, access policies, and downstream decision cost so the impact of wrong business answers becomes measurable.
