# MemCalib：记忆应该影响回答多少，而不只是有没有被找到

<!-- RELEASE-REFERENCE:START -->
> **发布时最佳结果（待核验）** · 基准记录日期：2026-09-21<br>
> 尚未核验原始发布版本中可定位到模型、指标和协议的最佳成绩。 [原始来源](https://arxiv.org/abs/2609.24259)<br>
> 不以最新榜单、单条基线或后续论文成绩代替；未知不代表零分或原作者未报告。
<!-- RELEASE-REFERENCE:END -->

**中文** | [English](memcalib.en.md) · [返回入口](../README.md) · [Benchmark Library](../library/README.md)

[论文](https://arxiv.org/abs/2609.24259) · [项目](https://quark-medical.github.io/MemCalib-Project/) · [数据](https://huggingface.co/datasets/ZiLaotou/MemCalib)

## 它在测什么

MemCalib 的对象是已经放进上下文的记忆命题。针对当前问题，每条命题有三级目标：A / Ignore 不应留下特定影响，B / Bound 只提供局部支持，C / Control 应决定关键结论或约束。公开项目页给出 15,000 个样本、234,220 条命题，训练集 13,500、测试集 1,500；论文另从训练部分保留 1,500 个验证样本。[官方数据与协议](https://github.com/Quark-Medical/MemCalib-Project/blob/main/index.html)

## 相比什么前进了

相较只问记忆是否相关、是否召回或最终回答是否正确，这里检查的是命题对回答的影响强度。相较 MemTrapBench 等负迁移诊断，它同时保留影响过多与影响不足两个方向；完全忽略历史不能被当成良好的记忆策略。

## 实际怎样评测

样本包含问题、组合记忆块、拆出的命题、理想使用等级和命题级 rubric，覆盖健康、一般助手和编码三类情境。官方页面列出 Sample Calibration Score、Exact Calibration 以及双向错误指标。本次核验了公开数据卡和项目说明；代码仓库目前只有短 README，尚未核验到可执行评分器，因此不能承诺逐项复现其数值。[数据](https://huggingface.co/datasets/ZiLaotou/MemCalib) · [代码发布状态](https://github.com/Quark-Medical/memcalib)

## 决定性证据与分数边界

公开协议足以把“记忆使用校准”定义为可复用数据与标注任务，因而单独收录这个 benchmark；不把同文的 MemCalib-RL 当作第二个基准。论文报告常见训练方法可能改善一个方向却恶化另一个方向，这一报告提示必须同时读双向指标，不证明某种优化在所有情境都更好。[论文](https://arxiv.org/abs/2609.24259)

## 主要混杂与尚未覆盖的能力

最需要验证的是 B 与 C 的标注边界、命题拆分和 rubric 解释是否稳定。该评测把记忆直接提供给模型，不测检索、写入、来源权限或环境行动。健康情境的占比也会影响总分；不能把总分直接推广成医疗任务的可靠性结论。

<!-- RESEARCH-DECISION:START -->

## 研究决策卡

### 什么时候值得用

适合在检索之后诊断模型是否过度个性化、忽略约束或把局部事实错误提升为全局决策。

### 一个具体任务长什么样

示意：项目使用某种语言是当前实现的硬约束，旧项目偏好只是背景；模型应让前者控制答案，不能机械采用后者。

### 最有判别力的实验

保持生成模型和输入记忆不变，比较完整记忆、相关命题 oracle 与移除干扰命题；按 A/B/C 分组报告双向错误，并对边界样本做人类与多评分器一致性检查。发布评分器之前，明确标出本地 rubric 实现与原论文结果不可直接混比。

### 建议搭配

[memtrapbench](memtrapbench.md) · [memory-trust-gap](memory-trust-gap.md) · [locomo-conv](locomo-conv.md)

<!-- RESEARCH-DECISION:END -->

---

证据核验：2026-09-23。本条依据论文元数据、官方协议及上述公开实现或数据说明；不把结构校验当作事实认证，也未独立复现实验。
