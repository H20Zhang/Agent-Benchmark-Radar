# MemoryAgentBench: turning static long context into an incremental memory agent

[中文](memoryagentbench.md) | **English** · [Home](../README.en.md) · [Benchmark Library](../library/README.en.md)

[Paper](https://arxiv.org/abs/2507.05257) · [Code](https://github.com/HUST-AI-HYZ/MemoryAgentBench)

## What it measures

MemoryAgentBench feeds information incrementally through multi-turn interaction and decomposes memory into accurate retrieval, test-time learning, long-range understanding, and selective forgetting. The key change is that the system must form and maintain memory while information arrives, rather than receiving a fully prepared long prompt at evaluation time.

## Compared with what

LoCoMo and LongMemEval largely treat long history as the evidence source for QA. MemoryAgentBench makes the memory agent itself the evaluation object and puts forgetting and learning in the same framework. A system can therefore be strong at retrieval yet weak at updating or selective forgetting; one aggregate number should not hide those asymmetric failure modes.

## Decisive evidence and score boundary

The paper evaluates systems ranging from full-context and RAG baselines to external-memory and tool-augmented agents and finds that current methods do not master all four competencies simultaneously. The official dataset was subsequently revised, including removal of some inefficient/high-cost samples and field fixes, so dataset revision is part of the evaluation contract. A high score supports performance on a named competency under a named version and grader; it does not prove a memory architecture is universally better.

## Fair comparison conditions

Align dataset revision, answerer, embedding/retrieval model, memory harness, ingestion process, and grader. A stronger reader or a larger retrieval budget cannot be credited to the memory mechanism itself.

## Next evaluation coordinate

The four-way decomposition is useful, but the final outcome is still mostly question answering. The next coordinate is whether memory improves later planning and action while exposing the cost and failure propagation of writing, consolidation, and forgetting.
