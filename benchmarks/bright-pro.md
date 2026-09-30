# Bright-Pro：从文档相关性走向推理要点覆盖

<!-- RELEASE-REFERENCE:START -->
> **历史论文结果（首版归属待核验）** · 2026-05-05 · 历史论文快照<br>
> **BGE-Reasoner-8B — α-nDCG@25: 68%** (静态检索 · Overall α-nDCG@25)<br>
> 保留原始轨道中的指定结果，不把不同指标、子集或系统拼成一个榜首。 [原始来源](https://arxiv.org/abs/2605.04018)<br>
> 来自此前保存的原论文结果记录，仅作历史参考；本次未重跑实验，也不声明当前最佳。
<!-- RELEASE-REFERENCE:END -->

**中文** | [English](bright-pro.en.md) · [基准库](../library/README.md)

<!-- EVIDENCE:reading:START -->
## 阅读范围与版本

已阅读下述主论文全文的方法、实验设置、结果与局限；未独立复现实验。

ACL版31页正文、局限及附录A–H，包含全部指标、解码设置、七领域例子、结果表及五种轨迹案例。

[ACL 2026 会议版，第 36776–36806 页；未宣称与 arXiv 首版相同](https://aclanthology.org/2026.acl-long.1705.pdf)
<!-- EVIDENCE:reading:END -->

<!-- EVIDENCE:placement:START -->
## 与相邻评测相比改变了什么

以下为基于所读协议的编辑比较，不表示论文宣称直接继承。

Bright-Pro沿BRIGHT的推理型相关性继续前进，把问题拆为加权要点并评覆盖和生成。它将“找到相关文档”扩展为“证据组合能否覆盖需要的方面”，因此静态排序与代理最终质量可能不同序。
<!-- EVIDENCE:placement:END -->

<!-- EVIDENCE:method:START -->
## 任务与证据如何构造

对 BRIGHT 的七个 StackExchange 领域重新审查证据，专家把每个查询拆成互补推理要点，给重要性打 1–5 分后归一化；删除弱相关证据、合并同源重复段落并补找新材料，再由同领域第二人复核。739 个查询的静态检索用 α=0.5 的 α-nDCG 惩罚同一要点的重复命中，并用加权要点召回率统计至少命中一次的要点权重。智能体实验固定 175 题，每轮返回 5 个段落，比较恰好 1–3 轮和自主停止两类协议。另构造 14 万条 RTriever-Synth 查询束，先生成参考解答、分解互补要点，再生成正例及刻意缺失关键要点的近主题负例；实际训练每步仍只采样一个正例和一个负例，以 LoRA 微调 Qwen3-Embedding-4B。
<!-- EVIDENCE:method:END -->

<!-- EVIDENCE:setup:START -->
## 复现时必须保留的条件

静态739题，智能体固定175题、每领域25题。每次搜索返回5段，每段按Qwen3-0.6B分词器截到2048 token，无全文读取工具。GPT-5-mini-08-07 用 medium，单轮输出最多30000、最终10000 token；Qwen3.5-122B-A10B-GPTQ-Int4 用vLLM 0.19.1，分别25600/12800 token。固定协议恰好1–3轮，自适应最多100轮。GPT-5既生成参考又判分：要点覆盖0/0.5/1按权重求均值w，再映射 round(4w+1)为完整性；整体质量1–5。AER逐题为质量×exp[-0.05(R−1)]。
<!-- EVIDENCE:setup:END -->

<!-- EVIDENCE:result-1:START -->
## 静态排名与固定三轮答案排名

静态为 739 题、α-nDCG×100；固定三轮为 175 题、GPT-5-mini，每轮 top-5；整体质量为 GPT-5 裁判的 1–5 分均值。两协议不能做纵向数值增益。

| 检索器 | 静态 α-nDCG@25 | 三轮 α-nDCG@15 | 三轮整体质量 |
|---|---|---|---|
| BGE-Reasoner-8B | 68.0 | 63.04 | 4.31 |
| DIVER-4B-1020 | 63.7 | 51.56 | 4.16 |
| DIVER-4B | 59.9 | 53.08 | 4.29 |
| RTriever-4B | 55.3 | 50.79 | 4.25 |

事实来源：表 2 and 表 3 · [论文](https://aclanthology.org/2026.acl-long.1705.pdf)
<!-- EVIDENCE:result-1:END -->

<!-- EVIDENCE:result-2:START -->
## 自适应质量与搜索轮数

固定 175 题、GPT-5-mini；轮数为每题平均，质量为 1–5 分，AER 为逐题质量按 exp[-0.05(R−1)] 折扣后平均，不能由表中均值直接重算。

| 检索器 | 平均搜索轮数 | 整体质量 | AER |
|---|---|---|---|
| BGE-Reasoner-8B | 5.1 | 4.43 | 3.65 |
| GTE-7B | 6.67 | 4.51 | 3.44 |
| BM25 | 5.73 | 4.42 | 3.53 |

事实来源：表 4; Equation 1 · [论文](https://aclanthology.org/2026.acl-long.1705.pdf)
<!-- EVIDENCE:result-2:END -->

<!-- EVIDENCE:interpretation:START -->
## 这些比较支持什么结论

静态领先不保证与智能体结合后仍保持同样排序：DIVER-4B-1020 的静态 α-nDCG@25 高于 DIVER-4B，但 GPT-5-mini 固定三轮的回答质量为 4.16，低于后者 4.29。自适应条件下，GTE-7B 的回答质量 4.51 高于 BGE 的 4.43，但平均轮数 6.67 对 5.10，使 AER 为 3.44 对 3.65。AER 是按轮数折扣的质量奖励，不是实测 token、美元或延迟；应同时展示质量与轮数。
<!-- EVIDENCE:interpretation:END -->

<!-- EVIDENCE:limitations:START -->
## 局限、来源冲突与下一步

静态全量集与 175 题智能体子集不同，α-nDCG@25 与跨轮累计 @5/@10/@15 也不能直接作提升差。人工 κ=0.742 仅验证 50 题的重要性评分；40 题参考答案检查由一名作者评分，不能替代最终裁判与独立人工的一致性测试。部分要点是专家对问题的扩展解释，可能偏向更广的答案。下一步补齐未微调 4B 基座和等训练预算消融，报告配对置信区间，交换裁判并测真实 token、延迟及重复制证据成本。

论文宣称相对4B基座大幅提升，但所读结果表只有Qwen3-8B，缺未微调4B对照。两智能体的每轮/最终输出上限不同。正文“领先4–14分”也不能概括表2的68.0对49.5。旧笔记的2763要点、5272标准段落不是论文直接给出的精确总数，仍需数据集核验。
<!-- EVIDENCE:limitations:END -->

相关基准：[bright](bright.md) · [claimprobe](claimprobe.md)
