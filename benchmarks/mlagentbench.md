# MLAgentBench：把机器学习实验迭代本身变成 agent task

**中文** | [English](mlagentbench.en.md) · [返回 Radar](../README.md) · [Benchmark Library](../library/README.md)

[论文](https://arxiv.org/abs/2310.03302) · [代码](https://github.com/snap-stanford/MLAgentBench)

## 它到底测什么

MLAgentBench 评估 agent 能否 **迭代完成 machine-learning experimentation**：读写文件、改代码、执行实验、观察结果、提出新假设，再继续下一轮。13 个任务从 CIFAR-10 到较新的 BabyLM 等挑战。

## 相比此前评测多测了什么

code-generation benchmark 通常只要求一次生成答案；ML experiment 是闭环：选择 intervention、付出 execution cost、解释 noisy feedback、更新 plan。MLAgentBench 因此把 experiment iteration 与 long-term planning 变成 measurement object。

## 决定性证据

被测 agent 中 Claude 3 Opus 平均 success rate 最高，为 37.5%。不同任务跨度极大：成熟旧 dataset 可到 100%，部分较新的 Kaggle challenge 可到 0%；作者也把 long-term planning 与 hallucination 列为主要 failure mode。

## 这个分数能证明什么

benchmark 支持固定 repository/task 下 end-to-end experimentation 能力，但不能把结果单独归因给 model research skill：scaffold、compute budget、starting code quality 与 benchmark familiarity 都会影响。新旧任务差异也提示 contamination/prior knowledge 风险。

## 公平比较契约

应固定 repository snapshot、starting baseline、hardware、wall-clock/experiment budget、agent tool、model 与 success threshold，同时报告实验次数与 compute，不应只看最终是否越过 target。

## 还没有测什么

13 个任务 coverage 有限，而且“benchmark 分数提高”不等于科学研究有效：hypothesis novelty、robustness、reproducibility、negative result interpretation 与 anti-gaming 都需要更强评测。

## 下一步最有判别力的验证

使用隐藏的 post-cutoff repository，在相同 compute 下只改变 planning/recovery mechanism，更好地区分 research-agent competence、pretraining familiarity 与 brute-force experimentation。

<!-- RESEARCH-DECISION:START -->

## 研究决策卡

### 什么时候值得用

适合研究执行反馈驱动的机器学习实验迭代，比一次性代码生成更接近研究工作。但少量任务上的成功并不证明科研创新；需要区分修好环境、调好已知流程和提出有效新方法。

### 一个具体任务长什么样

示意任务：系统修改训练代码、执行实验、查看结果再调整方案。失败日志和验证指标是反馈来源，但反复在同一反馈集上选择方案也可能过拟合，最终评测必须保留独立性。

### 最有判别力的实验

固定计算资源与实验次数，比较一次生成、无记忆迭代和有经验记忆迭代，分别报告有效运行率与模型质量。最终从干净环境复跑选定方案，避免把偶然运行状态或验证集过拟合当作改进。

### 建议搭配

[mle-bench](mle-bench.md) · [deltaml-bench](deltaml-bench.md)

> **读分数的原则：** 先对齐 task / split、模型与 harness、工具与环境版本、资源预算、停止与重试规则以及 evaluator。协议不同的总分首先是系统级证据；没有 matched intervention / ablation 时，不把差异直接归因给单个组件。

<!-- RESEARCH-DECISION:END -->

## 演化位置

`one-shot ML code → iterative experiment loop → autonomous research engineering`

MLAgentBench 把“做实验”而不是“写代码”确立为一项独立 agent 能力。