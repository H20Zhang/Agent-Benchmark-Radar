# LoCoMo-Conv：用户不直接索取旧事实时，记忆还能不能被正确调用

**中文** | [English](locomo-conv.en.md) · [返回入口](../README.md) · [Benchmark Library](../library/README.md)

[论文](https://arxiv.org/abs/2609.03467) · [代码](https://github.com/MiuLab/LoCoMo-Conv) · [数据](https://github.com/MiuLab/LoCoMo-Conv/tree/main/data)

## 它在测什么

LoCoMo-Conv 保留 LoCoMo 的历史、标准答案和证据 dia_ids，将查询改为 dialog、implicit、counterfactual、composed 四类，并分别测检索与自由文本回答。组合部分有 1,069 个由两个原始问题构成的多记忆簇。来源是改写后的既有历史，不是新采集的自然长期用户互动。[官方协议与数据](https://github.com/MiuLab/LoCoMo-Conv/blob/main/README.md)

## 相比什么前进了

相较 LoCoMo，固定历史后改变的是“当前请求怎样表达”。它能够检查显式问题是否提示了该找什么。与 LoCoMo-Plus 等约束一致性评测也应区分：这里特别保留原始证据标识，便于观察查询形式、检索证据和回答表现之间的差距。

## 实际怎样评测

公开运行入口包含 top-K、oracle、no-memory、query rewriting 和 CoT 对照。检索脚本将返回内容映射回 dia_ids：原始文本可用子串匹配，抽象记忆可通过 metadata 的 dia_ids 归属；组合题使用成员证据的并集。因而 Recall 不等于返回摘要语义完整，跨表示比较必须保留同等可靠的来源映射。[检索评分代码](https://github.com/MiuLab/LoCoMo-Conv/blob/main/retrieval/compute_retrieval_metrics.py)

## 决定性证据与分数边界

论文报告隐式与组合查询暴露了 QA 不易看到的检索差距，并区分强检索与好回答。还描述了 implicit 查询中的 silent grounding：历史可能改善回答的情境适配，却不显式复述标准事实。因此不能只用“是否说出 gold fact”代替对话质量，也不能把各 judge 的总分合为一个无条件排名。[论文](https://arxiv.org/abs/2609.03467)

## 主要混杂与尚未覆盖的能力

最强混杂是改写质量、类别过滤、来源标记完整性和回答评分标准。仅看 raw-turn 与抽象 memory 的 Recall 差，可能把映射或信息保留差异误认为召回算法差异。它仍不测外部应用行动、长期权限治理或持续学习成本。

<!-- RESEARCH-DECISION:START -->

## 研究决策卡

### 什么时候值得用

适合研究显式 QA 之外的日常对话记忆，以及检索成功为什么没有转化为回答质量。

### 一个具体任务长什么样

示意：用户只说“这次周末照旧安排吧”，并未直接问过去偏好；系统需要推断应找哪段历史，而不是匹配原 QA 中的名词。

### 最有判别力的实验

对同一历史和 source question 成对比较显式与隐式版本，固定 embedding、回答器、top-K 和 token 预算；再给定 oracle 证据。分别检查来源召回、记忆语义保留、事实使用和对话适配，避免把多个阶段折成一个总分。

### 建议搭配

[locomo](locomo.md) · [locomo-plus](locomo-plus.md) · [dolphinbench](dolphinbench.md)

<!-- RESEARCH-DECISION:END -->

---

证据核验：2026-09-23。本条依据论文元数据、官方协议及上述公开实现或数据说明；不把结构校验当作事实认证，也未独立复现实验。
