# MTRAG-UN：检验多轮问答中的不可答与信息不足

<!-- RELEASE-REFERENCE:START -->
> **发布时最佳结果（待核验）** · 基准记录日期：2026-02-26<br>
> 尚未核验原始发布版本中可定位到模型、指标和协议的最佳成绩。 [原始来源](https://aclanthology.org/2026.findings-acl.503/)<br>
> 不以最新榜单、单条基线或后续论文成绩代替；未知不代表零分或原作者未报告。
<!-- RELEASE-REFERENCE:END -->

**中文** | [English](mtrag-un.en.md) · [基准库](../library/README.md)

<!-- EVIDENCE:reading:START -->
## 阅读范围与版本

已阅读下述主论文全文的方法、实验设置、结果与局限；未独立复现实验。

七页全文及附录A–B、所有图表；另定向查阅原MTRAG第6.3–8节以解释继承指标，未将其记作原MTRAG全文复读。

[ACL 2026 Findings，第 10363–10369 页](https://aclanthology.org/2026.findings-acl.503.pdf) · [TACL 2025，第 6.3–8 节定向核对指标](https://aclanthology.org/2025.tacl-1.36.pdf)
<!-- EVIDENCE:reading:END -->

<!-- EVIDENCE:placement:START -->
## 与相邻评测相比改变了什么

以下为基于所读协议的编辑比较，不表示论文宣称直接继承。

MTRAG-UN直接扩展原MTRAG多轮企业问答，集中加入不可回答和信息不足的请求。变化是把“缺事实应拒答”与“缺条件应追问”区分，不能只用一般答案相似度解释所有轮次。
<!-- EVIDENCE:placement:END -->

<!-- EVIDENCE:method:START -->
## 任务与证据如何构造

666 段对话各选一个评测轮次，保留该轮之前的历史，偏向不可答、信息不足、依赖上下文和用户澄清等困难情况；不是把每一轮都算成独立任务。六领域包括原有四个语料及银行、电信网页。信息不足题部分由人工问题拼接到既有对话，75% 同/近主题、25% 跨主题，再人工确认歧义仍成立。检索只在 468 道可答/部分可答题上比较最后一问与 GPT-OSS-20B 改写。生成比较最多 10 个标准段落与 Elser 改写检索的前 5 段，并要求少于 150 词；信息不足应明确向用户索取缺失条件。
<!-- EVIDENCE:method:END -->

<!-- EVIDENCE:setup:START -->
## 复现时必须保留的条件

检索只用468道可答/部分可答题，六领域宏平均；非独立/独立子集为214/254题。RBalg为BERT参考召回、相对证据的BERT知识精度及ROUGE-L的调和平均；RBllm对照参考答案和证据判断忠实、合适、完整；RLF为RAGAS无参考忠实度。三者按可答性与IDK条件化：不可答且拒答记1，可答却拒答记0。信息不足另用是否明确请求缺失信息的裁判；96.2%验证来自80条抽样回答。新版本以GPT-OSS-120B替换所述GPT-4o-mini裁判，其余沿用原协议。
<!-- EVIDENCE:setup:END -->

<!-- EVIDENCE:result-1:START -->
## 最后一问与对话改写

R@5 为 0–1；全体 468 题按六领域宏平均，非独立/独立子集分别 214/254 题；改写使用 GPT-OSS-20B。

| Elser 子集 | 最后一问 R@5 | 改写 R@5 |
|---|---|---|
| 全部可答／部分可答 | 0.4 | 0.49 |
| 依赖历史的问题 | 0.39 | 0.52 |
| 可独立理解的问题 | 0.4 | 0.46 |

事实来源：表 2–3 · [论文](https://aclanthology.org/2026.findings-acl.503.pdf)
<!-- EVIDENCE:result-1:END -->

<!-- EVIDENCE:result-2:START -->
## 生成分数与证据条件

三个指标均为 0–1、按可答性/IDK 条件化；信息不足用另一个裁判，各项精确分母未明确报告。参考最多 10 段，对照只取检索前 5 段。

| GPT-OSS-120B 证据条件 | RLF | RBllm | RBalg |
|---|---|---|---|
| 最多 10 个标准段落 | 0.65 | 0.76 | 0.46 |
| Elser 改写检索前 5 段 | 0.59 | 0.65 | 0.37 |

事实来源：表 4; metric definitions inherited from original MTRAG 节 6.3 · [论文](https://aclanthology.org/2026.findings-acl.503.pdf)
<!-- EVIDENCE:result-2:END -->

<!-- EVIDENCE:interpretation:START -->
## 这些比较支持什么结论

检索改写确实有配对收益：Elser 的 R@5 从 0.40 到 0.49；非独立问题从 0.39 到 0.52，大于独立问题的 0.40 到 0.46。生成的参考证据与实际检索存在差距，但两者同时改变段落数量，不能把差值全称为检索噪声因果效应。不可答与信息不足应分开：前者可以拒答，后者的裁判要求明确索取缺失信息；仅说“信息不够”不算成功澄清。
<!-- EVIDENCE:interpretation:END -->

<!-- EVIDENCE:limitations:START -->
## 局限、来源冲突与下一步

语料限定不可答依赖标注者没有找到相关段落，并不证明现实世界无答案。数据采集受 Elser 与 Mixtral 8×7B 初始回答影响；最强检索器可能受采集偏差。澄清裁判主要检查是否请求信息，未直接评估追问是否最有价值或后续问题是否真正解决。GPT-OSS-120B 同时参与评判与被评模型，也需独立裁判复核。下一步匹配参考/检索段落数量，人工审计信息不足追问质量并做后续用户回复后的闭环评估。

图3统一标RBalg，但信息不足题在正文定义使用独立澄清裁判，应另读红色柱。摘要超过2800轮与正文666对话平均8轮的单位/截断关系不清。生成各指标在排除信息不足题后的精确分母未明确。GPT-OSS-120B也不是每个指标最好：RAG的RBalg为0.37，部分模型为0.38。
<!-- EVIDENCE:limitations:END -->

相关基准：[rgb](rgb.md) · [longmemeval](longmemeval.md)
