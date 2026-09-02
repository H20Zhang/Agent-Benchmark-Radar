# TML-Bench：自动 ML agent 的比较必须锁定 wall-clock budget

**中文** | [English](tml-bench.en.md) · [返回入口](../README.md) · [Benchmark Library](../library/README.md)

[论文](https://arxiv.org/abs/2603.05764)

## 它在测什么

TML-Bench 基于 4 个 Kaggle competitions，比较 10 个 open-source LLMs，并设定 240/600/1200 秒三种 wall-clock budgets、每种 5 次 successful runs。evaluation 检查 valid submission、private holdout score 与跨运行稳定性，强调 agent 在时间限制内迭代建模。

## 相比什么前进了

MLAgentBench 有实验循环，但 compute/time 仍容易被忽略。TML-Bench 把 wall-clock budget 明确变成 track，避免“多跑十倍实验”被当作纯 agent intelligence gain。

## 分数边界

holdout score 支持具体 competition、hardware/runtime 与 time budget 下的 autonomous modeling；不同 budget/hardware 不是 apples-to-apples，也不应只看最好一次 run。

## 公平比较条件

锁定 240/600/1200s budget、hardware、competition data、submission validator、model/scaffold 与 run count，并报告 stability。

## 下一步评测坐标

下一步要同时看 experiment efficiency、reproducible artifacts 与 invalid-result detection，而不仅是 leaderboard score。
