# MLE-bench

## 它到底测什么

MLE-bench 测的是 **从竞赛描述和原始数据出发，独立完成端到端 machine-learning engineering 并交付可评分预测文件**的能力。agent 需要理解任务、检查数据、写代码、训练/验证模型、迭代实验并提交结果；最终用重建测试集和历史 private-leaderboard 门槛判断是否达到 bronze / silver / gold 等 human-relative contract。

## 相比前身多测了什么

MLAgentBench 只有约 13 个任务，而且不少场景带有 baseline 或更强的起始结构。MLE-bench 扩到 **75 个 from-scratch competition**，并用真实竞赛历史分布定义 medal threshold，因此把 Data Agent 的测量对象从“能否完成一个研究脚本”推进到更接近真实 ML competition 的完整工程过程。

## 决定性证据

同一个 GPT-4o 在 MLAB、OpenHands、AIDE scaffold 下的 **Any Medal 分别只有 0.8%、4.4%、8.7%**；同时 pass@6 明显高于 pass@1。这个结果最重要的含义不是某个 scaffold 排第一，而是最终能力对 scaffold 与 retry budget 高度敏感：同一 backbone 在不同 orchestration 下可以有数量级差异。

## 这个分数支持什么判断

MLE-bench 的 headline score 测的是 **model + scaffold + retry + compute/resource system**，不是纯基础模型能力。尤其当 best-of-n、运行时长、GPU、工具、prompt assistance 或代码模板变化时，medal rate 的变化不能直接归因于 reasoning 或 coding capability。

## 公平比较条件

公平比较至少要对齐 competition version、数据访问、scaffold、工具接口、最大运行时长、GPU/CPU 资源、retry/best-of-n、是否允许外部搜索、prompt assistance 和最终 submission selection。官方后续暂停 leaderboard 处理公平性与版本问题，本身就说明 protocol drift 是 load-bearing variable，而不是维护细节。

## 研究上怎么用

MLE-bench 更适合评估 **autonomous ML engineering system**，而不是做 foundation-model leaderboard。如果研究想证明 planning、memory、multi-agent 或 search 有价值，必须在相同 backbone、相同工具和相同 compute budget 下做 matched ablation，否则 package-level gain 无法归因。最好同时报告 pass@1、pass@k、资源消耗以及失败类型。

## 下一步最有价值的验证

它仍没有覆盖问题定义、数据/指标设计、杂乱研究仓库、方法新颖性与人类协作。另一个关键缺口是 cost-normalized performance：如果一个系统靠更多 retry 和更多 GPU 获得 medal，研究者需要知道每单位 token / wall-clock / compute 的成功率是否真正更高。

## 谱系位置

MLE-bench 补齐 Data Agent 的自主 ML engineering 分支：`MLAgentBench → MLE-bench → MLE-Dojo → DeltaML / AI4AI`；`map_delta=splits`。它建立了大规模 terminal outcome coordinate，后续工作再逐步把 trajectory、研究过程和验证环纳入评测。

Primary: https://arxiv.org/abs/2410.07095

<!-- RESEARCH-DECISION:START -->

## 研究决策卡

### 什么时候值得用

适合评价从数据到有效竞赛提交的端到端机器学习工程。奖牌阈值是历史人类参照，不是同期、等预算的人机对照；排行榜提交次数、计算资源和智能体框架都可能改变结论。

### 一个具体任务长什么样

示意任务：系统在本地重建的竞赛环境中探索数据、训练模型并提交预测，由隐藏测试标签评分。完成预测文件只是底线，模型质量、规则遵从和是否存在泄露仍需要一起审查。

### 最有判别力的实验

固定硬件、时间、重试次数与数据切分，分别报告有效提交率和达到质量阈值的比例。比较相同骨干下的框架，并将所有失败运行保留在统计中；历史人类成绩只作参照，不宣称等条件超越。

### 建议搭配

[mle-dojo](mle-dojo.md) · [deltaml-bench](deltaml-bench.md)

> **读分数的原则：** 先对齐 task / split、模型与 harness、工具与环境版本、资源预算、停止与重试规则以及 evaluator。协议不同的总分首先是系统级证据；没有 matched intervention / ablation 时，不把差异直接归因给单个组件。

<!-- RESEARCH-DECISION:END -->
