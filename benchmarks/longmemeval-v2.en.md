# LongMemEval-V2: moving memory from chat history to 115M-token agent trajectories

[中文](longmemeval-v2.md) | **English** · [Home](../README.en.md) · [Benchmark Library](../library/README.en.md)

[Project](https://longmemeval.github.io/)

## What it measures

LongMemEval-V2 uses 451 curated questions over as many as 500 trajectories totaling roughly 115M tokens, spanning web and enterprise agent experience with small and medium scales. It asks about cross-trajectory workflow knowledge and makes both accuracy and latency part of the evaluation contract.

## Compared with what

Original LongMemEval uses conversational history. V2 replaces that evidence with agent trajectories and compares no retrieval, slice RAG, RAG with notes, AgentRunbook, Codex, and other memory/context strategies. The official evaluation also uses an accuracy-latency frontier/LAFS so slower systems are not treated as pure progress.

## Current results

Radar separates small/medium accuracy and latency into four web tracks. The official snapshot reports small accuracy of 1.3% no retrieval, 42.8% slice RAG, 51.0% RAG+notes, 58.6% AgentRunbook-R, 69.9% Codex, and 74.9% AgentRunbook-C; medium accuracy is 1.3%, 38.1%, 45.9%, 57.0%, 68.7%, and 70.1%. Latency ranges from 0.1–0.3s for RAG to roughly 25–186s for agentic methods, so accuracy alone hides the central trade-off.

## Fair comparison conditions

Align small/medium scale, trajectory corpus, retrieval/context strategy, agent/model, and latency definition; both accuracy and latency need dated protocol versions.

## Next evaluation coordinate

The next step executes new tasks rather than only answering trajectory questions, measuring experience-reuse gains together with construction and retrieval cost.
