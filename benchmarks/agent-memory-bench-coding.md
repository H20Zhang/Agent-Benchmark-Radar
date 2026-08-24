# Agent Memory Bench：编码智能体中的因果记忆复用

**中文** | [English](agent-memory-bench-coding.en.md) · [返回入口](../README.md) · [Benchmark Library](../library/README.md)

[代码、任务、预注册与 pilot](https://github.com/GiulioDER/agent-memory-bench)

## 问题

在中性 feed 与可执行评分下，可插拔 memory layer 是否因果地帮助 coding agent 复用过去的仓库任务经验？

## 证据

公开 corpus 含 24 个真实仓库任务、24 条 precursor transcript 和 99 个 distractor。各 arm 共用 baseline 与逐字 session feed；integration hash 和 proof-of-treatment gate 在隐藏 executable oracle 计分前验证 memory 确实可用且被使用，同时显式记录 ingestion / session 成本与 negative transfer。当前预注册 pilot 最终只有 13 个 survivor，相对 CLAUDE.md baseline 的估计提升仅 +0.014，区间跨过零。

## Caveat

参测 Recall 产品由作者开发，环境限定 Claude，proof-of-treatment 还会产生 survivor set。Pilot 远低于目标统计功效，因此其零结果不能证明 memory 对 coding agent 无用。

## Map

`map_delta=reinforces`，绑定 `memory-action-utility`。它独立加强了 PAST-Bench 所代表的因果 treatment 协议，但不修改 defining chain。
