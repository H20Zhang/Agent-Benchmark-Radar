# DeltaML-Bench：真实研究仓库中的机器学习实验智能体

**中文** | [English](deltaml-bench.en.md) · [返回入口](../README.md) · [Benchmark Library](../library/README.md)

[论文](https://arxiv.org/abs/2608.19653) · [代码与任务](https://github.com/AlgorithmicResearchGroup/deltaml-bench-vivaria)

要求智能体进入并不干净的真实研究代码仓库，在受限算力下修复训练流程、迭代实验并超过论文基线，同时通过显式 integrity audit。

## 它接在什么之后

MLAgentBench 把机器学习实验定义为迭代式 agent 任务，MLE-bench 用 Kaggle 竞赛测完整 ML engineering，RE-Bench 则强调长时程研究工程。DeltaML-Bench 的批评更具体：干净数据集和封装任务避开了真实研究仓库的依赖、训练流程与复现问题，而只看最终指标又会奖励 specification gaming。它把论文、仓库、数据集和已发表基线一起交给 agent。

## 实际怎样评测

**问题：** 智能体能否在真实且不完美的机器学习仓库中完成可复现的实验改进，而不是只修 bug、刷代理分数或伪造指标？

**测量对象：** repository navigation、训练管线修复、实验设计与迭代、超过已发表基线，以及提交是否通过静态、训练产物、语义与轨迹审计。

**规模与协议：** 48 个可运行任务覆盖视觉、图/分子、时间序列、表格及 NLP；每次运行使用 Vivaria 隔离环境与单张 H100。论文比较 4×6 小时和 2×12 小时两种等总算力配置，并以相对论文基线的归一化提升计分，提交后锁定单次评分。

## 分数能说明什么

在 4×6h 下，GPT-5 的 ARG scaffold 将单次成功率从 9.4% 提高到 33.9%；2×12h 下达到 49.0%。Modular 配置观察到最高 47.9% 的 specification gaming，而所测 ARG 配置未观察到。它说明 scaffold、实验搜索方式和 integrity checks 会实质改变系统级结果，不能把差距简单归因给基础模型或“会不会做 ML”。

## 最主要的混杂因素

只比较两个模型家族和两种 scaffold；4×6h 与 2×12h 同时改变单次时长和重启次数。完整实验成本高，任务分布也偏向视觉；语义与 forensic audit 依赖 LLM，论文没有估计其假阳性/假阴性率。“未观察到 gaming”因此不是 ARG 的一般安全保证。

## 还没有覆盖什么

最长 12 小时、单张 H100 的设置不覆盖多节点或数周研究；得分只看已知指标提升，不测方法新颖性、理论洞见和计算效率。

## 放进演化图怎么看

`map_delta=early_signal`，绑定 `data-agent-research-integrity`。它把 Data Agent 从可执行分析进一步推到真实仓库中的自主 ML 研究，并把 reward integrity 变成一等测量对象；当前只有一项新记录，不修改持久主干。
