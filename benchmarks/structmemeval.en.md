# StructMemEval: making memory structure itself an evaluation target

[中文](structmemeval.md) | **English** · [Home](../README.en.md) · [Benchmark Library](../library/README.en.md)

[Paper](https://arxiv.org/abs/2602.11243)

## What it measures

StructMemEval selects tasks that humans naturally solve with structures such as ledgers, to-do lists, and trees, and asks whether an agent can organize long-term memory into a task-appropriate representation rather than merely chunking history for similarity retrieval. Memory organization therefore becomes an explicit capability instead of an implementation detail.

## Compared with what

LoCoMo, LongMemEval, and many RAG-style memory benchmarks can largely be approached as store-and-retrieve problems. StructMemEval deliberately uses tasks whose solution depends on structured maintenance, exposing the ceiling of simple retrieval and moving the evaluation coordinate toward representation selection and structured state tracking.

## Decisive evidence and score boundary

Initial experiments report that simple retrieval-augmented LLMs struggle, while memory agents can reliably solve the tasks when told how to organize memory. Without a structure hint, however, modern LLMs often fail to recognize the appropriate organization. The important conclusion is therefore that structure selection is itself a bottleneck. Success with an explicit ledger/tree hint does not establish autonomous representation discovery.

## Fair comparison conditions

Align whether structure hints are provided, task templates, backbone reasoning, and available memory operations. Mixing “use this ledger” with “discover the representation yourself” in one ranking would erase the benchmark's load-bearing variable.

## Next evaluation coordinate

The next step is to move from narrow structure-sensitive tasks to open environments where structure is induced autonomously and revised under updates, conflicts, and schema evolution.
