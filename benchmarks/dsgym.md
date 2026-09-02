# DSGym：Data Science Agent 需要在 stateful Jupyter 里工作，而不是只答一道题

**中文** | [English](dsgym.en.md) · [返回入口](../README.md) · [Benchmark Library](../library/README.md)

## 它在测什么

DSGym 有 972 个 analysis tasks + 114 个 prediction tasks，共 1,086 个，另含 DSBio 90-task slice。它使用 Docker/stateful Jupyter execution，让 agent 在持续 notebook state 中做分析、建模与调试，并包含 shortcut audits。

## 相比什么前进了

DS-1000 是 isolated coding problem；DSGym 让代码、数据、运行状态与后续步骤相互依赖，更接近 analyst notebook workflow，并能观察 agent 是否用 shortcut 绕过真正的数据推理。

## 分数边界

execution/task success 支持当前 notebook environment 与 task release 下的 agent performance；stateful execution、package versions 和 shortcut detection 都是 load-bearing protocol variables。

## 公平比较条件

锁定 Docker image、Jupyter state semantics、datasets、packages、agent step budget、shortcut policy 与 evaluator。

## 下一步评测坐标

下一步应把 notebook execution 与最终 report/artifact、review/recovery 和长期 project state 结合起来。
