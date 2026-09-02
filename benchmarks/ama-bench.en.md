# AMA-Bench: moving from conversation memory to agent-trajectory memory

[中文](ama-bench.md) | **English** · [Home](../README.en.md) · [Benchmark Library](../library/README.en.md)

[Paper](https://arxiv.org/abs/2602.22769) · [Code](https://github.com/AMA-Bench/AMA-Bench) · [Project](https://ama-bench.github.io/)

## What it measures

AMA-Bench uses trajectories produced by agents interacting with environments rather than only human-agent dialogue. The official suite spans settings derived from GAIA, WebArena, BALROG, ALFWorld, and SWE-bench and compares long-context, RAG, and memory-agent methods through a common `memory_construction → memory_retrieve` interface. The project page reports 2,471 QA pairs in its main evaluation.

## Compared with what

LoCoMo and LongMemEval mainly ask what happened in past conversations. AMA-Bench changes the remembered object to actions, objective state, causal transitions, and tool-execution experience, which is closer to the experience an agent may need to reuse later. The common two-stage interface also controls more of the stack than unrestricted agent evaluations.

## Decisive evidence and score boundary

Official results show long-context baselines degrading as trajectory horizon grows and report separate recall, causal-inference, state-updating, and state-abstraction dimensions. The current project page also contains two different AMA-Agent headline variants (55.80%/+10.88pp and 57.22%/+11.16pp). Radar therefore does not promote either unexplained headline to a unique current-best score. This is exactly why result tracking must bind scores to a specific snapshot, base model, and judge.

## Fair comparison conditions

Lock the base model such as Qwen3-32B, open-ended QA split, LLM judge, trajectory subset, and memory interface. The official repository itself documents substantial judge strictness differences, so cross-judge and cross-backbone results require separate tracks.

## Next evaluation coordinate

AMA-Bench places memory inside agent trajectories, but the endpoint is still trajectory QA. The stronger next test is to execute future tasks and measure whether remembered workflow/causal knowledge improves action success while accounting for construction and retrieval cost.
