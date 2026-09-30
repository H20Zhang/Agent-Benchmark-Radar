# HotpotQA：联合评估多跳问答与支持事实

<!-- RELEASE-REFERENCE:START -->
> **发布时最佳结果（待核验）** · 基准记录日期：2018-10<br>
> 尚未核验原始发布版本中可定位到模型、指标和协议的最佳成绩。 [原始来源](https://aclanthology.org/D18-1259/)<br>
> 不以最新榜单、单条基线或后续论文成绩代替；未知不代表零分或原作者未报告。
<!-- RELEASE-REFERENCE:END -->

**中文** | [English](hotpotqa.en.md) · [基准库](../library/README.md)

<!-- EVIDENCE:reading:START -->
## 阅读范围与版本

已阅读下述主论文全文的方法、实验设置、结果与局限；未独立复现实验。

全文第1–7节及附录A–C；关键表4–7经PDF图像核对。

[EMNLP 2018 终稿](https://aclanthology.org/D18-1259.pdf)
<!-- EVIDENCE:reading:END -->

<!-- EVIDENCE:placement:START -->
## 与相邻评测相比改变了什么

以下为基于所读协议的编辑比较，不表示论文宣称直接继承。

相较较早的单段、单跳问答，HotpotQA把跨段组合与支持句标注同时纳入任务。谱系上的关键变化是从只看答案，转向答案和证据链联合正确；它仍不等同开放网页上的自主研究。
<!-- EVIDENCE:placement:END -->

<!-- EVIDENCE:method:START -->
## 任务与证据如何构造

从Wikipedia首段超链接采样桥接实体，另从同类实体列表采样比较题；众包写问题、答案和支持句。三折模型筛选区分中等与困难题，开发/测试只取困难题。基线联合预测答案和支持句。
<!-- EVIDENCE:method:END -->

<!-- EVIDENCE:setup:START -->
## 复现时必须保留的条件

语料是 2017-10-01 英文 Wikipedia 首段，训练 90564 题，开发 7405 题；两个测试设置各有独立的 7405 题。Distractor 给定两个标准段落和八个 tf-idf 干扰段落；Fullwiki 在约 500 万页中先用倒排索引取最多 5000 个候选，再以 bigram tf-idf 取前 10 段。基线是带字符表示、自注意力及双向注意力的 RNN 阅读器，联合训练支持句预测与 yes/no/span 答案头。联合指标先把答案和支持事实的 precision/recall 相乘，再算 F1 并逐题平均。
<!-- EVIDENCE:setup:END -->

<!-- EVIDENCE:result-1:START -->
## 同一开发集两种信息条件

相同的 7405 题开发集，均为百分数；答案、支持事实与联合指标逐题计算后平均。Distractor 提供 2 个标准段落及 8 个干扰段落，Fullwiki 先从全库检索。

| 设置 | 答案 EM | 答案 F1 | 支持事实 F1 | 联合 F1 |
|---|---|---|---|---|
| 干扰段落开发集 | 44.44 | 58.28 | 66.66 | 40.86 |
| 全维基开发集 | 24.68 | 34.36 | 40.98 | 17.73 |

事实来源：表 4, 节 5.2 · [论文](https://aclanthology.org/D18-1259.pdf)
<!-- EVIDENCE:result-1:END -->

<!-- EVIDENCE:result-2:START -->
## 支持监督与给定证据

7405 题 distractor 开发集的平均答案 F1，单位百分数；区分去掉支持监督与直接提供标准证据。

| 条件 | 答案 F1 |
|---|---|
| 基线 | 58.28 |
| 无支持事实监督 | 56.19 |
| 仅标准段落 | 63.58 |
| 仅标准支持句 | 66.98 |

事实来源：表 7 · [论文](https://aclanthology.org/D18-1259.pdf)
<!-- EVIDENCE:result-2:END -->

<!-- EVIDENCE:interpretation:START -->
## 这些比较支持什么结论

答对与支持链正确必须分开：开发集干扰条件答案F1为58.28，联合F1只有40.86。不要跨不同测试集把差值当逐题干预；开发集比较更直接。
<!-- EVIDENCE:interpretation:END -->

<!-- EVIDENCE:limitations:START -->
## 局限、来源冲突与下一步

模型筛选、首段语料和仅100例人工类型分析限制外推；其中6%单跳、2%不可回答。下一步固定读者和候选预算，比较自主多跳检索。

附录 C 把未找到段落的排名截为候选数加一，因而其平均排名是乐观截断值，并非全语料真实排名。
<!-- EVIDENCE:limitations:END -->

相关基准：[multihop-rag](multihop-rag.md) · [browsecomp-plus](browsecomp-plus.md)
