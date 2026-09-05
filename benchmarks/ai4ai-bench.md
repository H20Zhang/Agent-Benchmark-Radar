# AI4AI-Bench：用 source-patch 边界隔离学习算法设计

**中文** | [English](ai4ai-bench.en.md) · [返回入口](../README.md) · [Benchmark Library](../library/README.md)

[论文](https://arxiv.org/abs/2608.20318) · [代码与任务](https://github.com/Einsia/AI4AI-Bench) · [已发布轨迹](https://lab.einsia.ai/ai4ai/trajectories/)

智能体先用低成本 proxy 探索四小时，只提交源码 patch，再进入探索阶段不可访问 evaluator 的全新正式训练环境。

## 它接在什么之后

MLAgentBench 测迭代式机器学习实验，MLE-bench 与 MLE-Dojo 扩展了端到端 ML engineering。AI4AI-Bench 的批评更窄：不受限的最终分数无法说明智能体改进了学习算法，还是只调了运行参数和基础设施。它冻结十个真实训练仓库，并把 source patch 设为探索与正式评测之间的唯一边界。

## 实际怎样评测

**问题：** 智能体能否诊断并改进学习算法，而不只是优化现有实现的运行方式？

**测量对象：** repository diagnosis、实验迭代、源码层算法修改、clean-start 正式训练表现，以及提交 patch 属于 run-side 还是 learning-side。

**规模与协议：** 十个仓库覆盖十类学习算法。每个智能体先在单张 B300 上使用低成本 proxy 探索四小时，只有源码 patch 会进入最长十二小时的全新正式环境。原仓库算法使用相同硬件、预算、evaluator 和 assets 重跑；异构任务指标被归一化为 0=无信息、0.1=原始基线、1=给定最优值。全部 290 条评测轨迹已公开。

## 分数能说明什么

290 个 system-configuration-task 单元的平均归一化分数为 0.166，最佳系统平均 0.250，124 个单元低于仓库自带基线。263 个有改动的提交中，learning-side patch 平均 0.226，run-side-only patch 平均 0.126。这是系统级和选择后分组差异：能说明该协议暴露了运行配置之外的大量改进空间，不能说明 learning-side 修改因果地带来 0.100 提升。

## 最主要的混杂因素

learning-side 提交并非随机分配；更强系统更可能深入到该层，论文也明确拒绝因果解释。另一个 LLM 负责 patch 分类，但没有报告分类可靠性。系统比较同时捆绑 model、harness 与 reasoning effort；proxy 和 final 阶段按访问权限和时间隔离，却不总是样本不重叠。

## 还没有覆盖什么

十个 B300 任务成本很高，没有 human baseline，统一分数也编码了不同任务的效用假设。仓库支持自托管正式评测，但目前没有运行 blind evaluation service，第三方无法复现官方隐藏边界的执行约束。

## 放进演化图怎么看

`map_delta=early_signal`，绑定 `data-agent-research-integrity`。它比宽泛 ML-agent 套件更紧地隔离学习算法设计，但单条记录不足以修改持久主干。

<!-- RESEARCH-DECISION:START -->

## 研究决策卡

### 什么时候值得用

适合研究学习算法修改，而不是不受限制地优化最终分数。源代码补丁和干净启动的正式训练有助于隔离持久修改，但代理反馈集与正式评测之间的独立性仍需审查；少量昂贵任务也限制统计把握。

### 一个具体任务长什么样

示意任务：智能体在代理环境中诊断训练行为并修改代码，之后只能移交源补丁，由正式环境重新训练。临时文件或已训练状态不能替代代码改进，否则会改变待评价对象。

### 最有判别力的实验

匹配代理探索和正式训练预算，固定基线重跑与补丁边界，并在多随机种子下验证。将代码修改类别作为描述而非自动因果解释；要证明算法机制，仍需专门消融和独立任务迁移。

### 建议搭配

[deltaml-bench](deltaml-bench.md) · [mle-bench](mle-bench.md)

> **读分数的原则：** 先对齐 task / split、模型与 harness、工具与环境版本、资源预算、停止与重试规则以及 evaluator。协议不同的总分首先是系统级证据；没有 matched intervention / ablation 时，不把差异直接归因给单个组件。

<!-- RESEARCH-DECISION:END -->
