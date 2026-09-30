# BrowseComp-PlusCM：将检索问题投射到独立大语料

<!-- RELEASE-REFERENCE:START -->
> **发布时结果（历史参考，非最佳声明）** · 2026-08-18 · 论文 v1 快照<br>
> **Independent 553M-document corpus / GPT-5.6 Sol — Answer accuracy: 80.7%** (跨语料回答准确率)<br>
> 保留原始轨道中的指定结果，不把不同指标、子集或系统拼成一个榜首。 [原始来源](https://arxiv.org/abs/2608.20317)<br>
> 来自此前保存的原论文结果记录，仅作历史参考；本次未重跑实验，也不声明当前最佳。
<!-- RELEASE-REFERENCE:END -->

**中文** | [English](browsecomp-plus-cm.en.md) · [基准库](../library/README.md)

<!-- EVIDENCE:reading:START -->
## 阅读范围与版本

已阅读下述主论文全文的方法、实验设置、结果与局限；未独立复现实验。

20页正文第1–7节与附录A–B全部阅读，包括失败案例、语料重复分析及完整评测/裁判提示；未运行管线，未查看未公开逐跳标签。

[arXiv v1, 2026-08-20](https://arxiv.org/pdf/2608.20317v1)
<!-- EVIDENCE:reading:END -->

<!-- EVIDENCE:placement:START -->
## 与相邻评测相比改变了什么

以下为基于所读协议的编辑比较，不表示论文宣称直接继承。

它直接将BrowseComp-Plus问题迁移到独立ClimbMix语料，保留全部事实跳有支持的子集。谱系变化是从围绕问题选文档到先有语料再筛可落地问题；筛选偏差和相关集合分母也随之改变。
<!-- EVIDENCE:placement:END -->

<!-- EVIDENCE:method:START -->
## 任务与证据如何构造

保留BrowseComp-Plus问题，把证据投射到独立构造的ClimbMix：约5.53亿文档、标称4000亿token，作者用Llama-2分词实测4106亿token，Lucene索引559GB。GPT-5.5/Codex依据问题、答案和原支持材料拆解原子事实，再用BM25搜索与全文读取逐跳落地；原材料仅作提示。830题先保留326道可答题，再要求必要跳和确认性冗余跳全部有证据，剩65；独立PIIKA/GPT-5.5给定证据答对65题，作者检查日期等细节后剩57。Opus 5合并候选并剔除不支持的逐跳关联，再扩展完全重复和经确认的近重复文档，形成每题qrels并集。
<!-- EVIDENCE:method:END -->

<!-- EVIDENCE:setup:START -->
## 复现时必须保留的条件

同57题在原约10万文档和ClimbMix上配对，PIIKA通过Pyserini BM25与全文工具访问，比较GPT–5.6 Sol(max)、Gemma 4 31B IT、Qwen 3.5 9B。最终GPT裁判仅判答案语义等价，精确裁判版本、统一绝对token/调用上限和生成采样设置未完整给出。Recall按搜索结果曾展示的相关文档比例逐题平均，不等于实际读取、使用或逐跳覆盖。闭卷在执行层禁用工具。只统计完成运行，GPT在ClimbMix最初未完成3题同设置重跑后均错，最终46/57。构造近失题曾加深到k=500，但不能把这个数当作所有评测调用深度。
<!-- EVIDENCE:setup:END -->

<!-- EVIDENCE:result-1:START -->
## 同题跨语料结果

相同57题，GPT为max推理；准确率为最终答案正确比例，召回是各语料自身qrels的逐题宏平均，分母不同。调用为平均检索调用次数；只纳入完成运行，无置信区间。

| 模型／语料 | 准确率（%） | qrel召回（%） | 每题调用数 |
|---|---|---|---|
| GPT–5.6 Sol / BrowseComp-Plus | 86.0 | 84.3 | 60.2 |
| GPT–5.6 Sol / ClimbMix | 80.7 | 21.4 | 98.3 |
| Gemma 4 31B IT / BrowseComp-Plus | 26.3 | 24.9 | 24.5 |
| Gemma 4 31B IT / ClimbMix | 15.8 | 2.8 | 23.4 |

事实来源：表 1; 节 6 · [论文](https://arxiv.org/pdf/2608.20317v1)
<!-- EVIDENCE:result-1:END -->

<!-- EVIDENCE:result-2:START -->
## 闭卷成功与投射筛选效应

执行层禁用检索及所有工具，只有问题；同一答案等价裁判。两个列分母分别830和57，不是独立随机同分布集合。正确并不证明记忆过该题原文。

| 模型 | 全部830题准确率（%） | 投射57题准确率（%） |
|---|---|---|
| GPT–5.6 Sol (max) | 46.1 | 70.2 |
| Gemma 4 31B IT | 0.8 | 1.8 |
| Qwen 3.5 9B | 0.1 | 0.0 |

事实来源：表 2 · [论文](https://arxiv.org/pdf/2608.20317v1)
<!-- EVIDENCE:result-2:END -->

<!-- EVIDENCE:interpretation:START -->
## 这些比较支持什么结论

最强模型准确率86.0→80.7%，召回84.3→21.4%，调用60.2→98.3；但是新语料每题相关集合更大且冗余不均，召回分母已经改变，不能把62.9点落差解释为等量必要证据丢失。该模型在57题闭卷就答对70.2%，故最终正确不证明检索到证据，提示“禁用内部知识”也不能保证做到。投射集只占830题的57题，且闭卷显著更易；结论应限于这一筛选子集与BM25，不能纯归因于语料规模或证明所有真实检索都如此。
<!-- EVIDENCE:interpretation:END -->

<!-- EVIDENCE:limitations:START -->
## 局限、来源冲突与下一步

57题是强筛选集合，未报告置信区间；同模型家族参与构造和验证，人工作者审查没有标注一致性。找不到跳不证明整个5.53亿语料确实缺失；构造受词面搜索和代理预算限制。347个题目—跳对中40个仅有至多两篇支持，而约四分之一超过40篇，集合召回容易偏向冗余跳；逐跳结构又未公开。语料独立于问题不等于无预训练污染，也非未经筛选的自然网页分布。下一步比较稠密/混合检索，在受控语料规模及相同预算下报告必要跳覆盖、引用支持率和闭卷增益，并补充可独立审查的隐藏标签评分服务。

正文工具名get_document与附录read_document不同，可能是包装别名，但精确schema需代码核验。明确的独立验证为GPT-5.5给65题证据，主评测为GPT–5.6 Sol的57题，结论所谓同一强模型全对的oracle配置未完全对齐。对原BrowseComp-Plus“前五篇512-token前缀86.5%含答案”的统计，这篇进一步表述为13.5%题必需证据被截掉，因果强度超出原审查。闭卷正确也不能区分整题记忆、来源事实学习与利用已有知识推断。
<!-- EVIDENCE:limitations:END -->

相关基准：[browsecomp-plus](browsecomp-plus.md) · [livebrowsecomp](livebrowsecomp.md)
