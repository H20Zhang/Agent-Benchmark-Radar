# KILT：在统一维基快照上联合评估答案与来源

<!-- RELEASE-REFERENCE:START -->
> **发布时最佳结果（待核验）** · 基准记录日期：2020-09<br>
> 尚未核验原始发布版本中可定位到模型、指标和协议的最佳成绩。 [原始来源](https://arxiv.org/abs/2009.02252)<br>
> 不以最新榜单、单条基线或后续论文成绩代替；未知不代表零分或原作者未报告。
<!-- RELEASE-REFERENCE:END -->

**中文** | [English](kilt.en.md) · [基准库](../library/README.md)

<!-- EVIDENCE:reading:START -->
## 阅读范围与版本

已阅读下述主论文全文的方法、实验设置、结果与局限；未独立复现实验。

全文第1–9节及附录11的映射、标注、接口和实现；表1–17已阅读。

[v1,2020-09-04](https://arxiv.org/pdf/2009.02252v1)
<!-- EVIDENCE:reading:END -->

<!-- EVIDENCE:placement:START -->
## 与相邻评测相比改变了什么

以下为基于所读协议的编辑比较，不表示论文宣称直接继承。

KILT把此前各自使用不同知识源的知识密集型任务映射到同一维基快照。改变的测量坐标是统一来源与证据门控，因而跨任务比较更可解释；它没有统一训练预算或消除来源标注缺口。
<!-- EVIDENCE:placement:END -->

<!-- EVIDENCE:method:START -->
## 任务与证据如何构造

把11数据集、五类任务的来源映射到2019-08-01维基快照（590万页）。页面重定向后以最高BLEU定位原证据，开发/测试过滤低于0.5者。分别评输出、页面检索及只有完整证据集排到前列才计分的KILT指标。
<!-- EVIDENCE:method:END -->

<!-- EVIDENCE:setup:START -->
## 复现时必须保留的条件

DPR 索引包含 22220793 个不重叠的 100 词块。BART+DPR 使用固定 DPR 的前 3 块；RAG 使用前 5 块并更新查询编码器，因此二者还改变训练方式。KILT 指标仅在至少一个完整标准来源集合达到 R-precision=1 时保留答案分数。所选测试集 NQ 为 1444 题、HotpotQA 为 5569 题；按参考答案和来源判分，没有 LLM 裁判。
<!-- EVIDENCE:setup:END -->

<!-- EVIDENCE:result-1:START -->
## 答案与完整来源之间的缺口

测试集 NQ 1444 题、HotpotQA 5569 题；指标为百分数，KILT-EM 要求答案正确且至少一个完整来源集合的 R-precision=1。

| 数据集／系统 | 答案 EM | R-precision | KILT-EM |
|---|---|---|---|
| NQ / BART+DPR | 41.27 | 54.29 | 30.06 |
| NQ / RAG | 44.39 | 59.49 | 32.69 |
| HotpotQA / BART+DPR | 25.18 | 25.04 | 1.96 |
| HotpotQA / RAG | 26.97 | 30.59 | 3.21 |

事实来源：表 2–4, 附录表 13–14 · [论文](https://arxiv.org/pdf/2009.02252v1)
<!-- EVIDENCE:result-1:END -->

<!-- EVIDENCE:interpretation:START -->
## 这些比较支持什么结论

统一快照不等于统一能力：同一RAG在HotpotQA答案EM26.97，但完整来源门控后只剩3.21。RAG与固定DPR对照还同时改变训练和检索数量，不能单归因于检索器。
<!-- EVIDENCE:interpretation:END -->

<!-- EVIDENCE:limitations:START -->
## 局限、来源冲突与下一步

全部题目设计为库内可回答，不测弃答；来源可不完备，也可能由另一个系统补出。人工来源标注κ在NQ为0.3、ELI5为0.1。下一步固定证据数量并扩充等价来源标注。

正文一处写BART+DPR分类器，附录讨论BERT+DPR，属于命名不一致；不要据此推测未说明的模型变体。
<!-- EVIDENCE:limitations:END -->

相关基准：[beir](beir.md) · [crag](crag.md)
