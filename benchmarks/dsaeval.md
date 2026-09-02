# DSAEval：Data Science Agent 的输出包括 reasoning、code、result 和 report

**中文** | [English](dsaeval.en.md) · [返回入口](../README.md) · [Benchmark Library](../library/README.md)

## 它在测什么

DSAEval 有 641 个 problems、285 个 real datasets，覆盖 tabular、image、text，并在 GPU Jupyter 环境中支持 cumulative multi-query sessions。evaluation 同时检查 reasoning、code、execution result 与 report；paper 比较 13 个 agents。

## 相比什么前进了

只测 code correctness 会漏掉分析 reasoning 与最终沟通。DSAEval 把多模态 data-science session 的中间过程和 deliverable 共同设为评价对象，且后续 query 可以依赖前面 notebook state。

## 分数边界

multi-component score 支持完整 agent 在指定 GPU/Jupyter、datasets 与 judge/rules 下的 data-science quality；不同 component 权重或 judge 会改变 aggregate rank。

## 公平比较条件

锁定 dataset/version、GPU/runtime、session ordering、agent budget、component metrics 与 report judge，并保留 component breakdown。

## 下一步评测坐标

下一步应增加数据/目标随 session 演化、artifact review 和业务 consequence，检验累计 state 是否最终帮助或污染分析。
