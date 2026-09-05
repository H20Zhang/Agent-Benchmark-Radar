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

<!-- RESEARCH-DECISION:START -->

## 研究决策卡

### 什么时候值得用

适合检验固定时间内交付有效表格机器学习结果的可靠性。任务数量少时，稳定性与失败率尤其重要；只对成功运行取中位数可能隐藏难以完成的配置，必须同时报告全部尝试。

### 一个具体任务长什么样

示意任务：系统在有限时间内查看训练数据、选择特征和模型，输出满足提交格式的预测文件。高质量模型若未生成有效文件，就未完成交付；更长预算也不保证每次运行更稳定。

### 最有判别力的实验

保持硬件与指令相同，只改变时间预算，记录所有尝试的有效率、隐藏集质量和波动。把提示随预算变化的条件单独列出，防止把指令改变误当作时间扩展收益。

### 建议搭配

[dare-bench](dare-bench.md) · [mle-bench](mle-bench.md)

> **读分数的原则：** 先对齐 task / split、模型与 harness、工具与环境版本、资源预算、停止与重试规则以及 evaluator。协议不同的总分首先是系统级证据；没有 matched intervention / ablation 时，不把差异直接归因给单个组件。

<!-- RESEARCH-DECISION:END -->
