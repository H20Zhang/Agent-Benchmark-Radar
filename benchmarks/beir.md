# BEIR：跨域检索要同时看质量、成本与标注偏差

<!-- RELEASE-REFERENCE:START -->
> **发布时最佳结果（待核验）** · 基准记录日期：2021-04<br>
> 尚未核验原始发布版本中可定位到模型、指标和协议的最佳成绩。 [原始来源](https://arxiv.org/abs/2104.08663)<br>
> 不以最新榜单、单条基线或后续论文成绩代替；未知不代表零分或原作者未报告。
<!-- RELEASE-REFERENCE:END -->

**中文** | [English](beir.en.md) · [主入口](../README.md) · [基准资料库](../library/README.md)

<!-- EVIDENCE:reading:START -->
## 阅读范围与版本

已核对所述主论文版本的方法、设置、关键结果与局限；未独立复现实验。

v4主文第1—7节及附录中的数据集、模型、语料和实验设置；关键表3、9、10和图3—4经PDF检查。

[arXiv:2104.08663v4](https://arxiv.org/pdf/2104.08663v4)

下列表格重新组织了有来源的选定事实。页首历史参考与正文采用的版本、切分和模型可能不同，不能跨表混合成绩。
<!-- EVIDENCE:reading:END -->

<!-- EVIDENCE:method:START -->
## 测量对象、方法与比较

把语料、查询和相关性标签统一成检索输入，跨18个英语数据集测试训练分布外排序；MS MARCO只作为域内参照。主指标nDCG@10兼容二元和分级相关性。检索、后重排及域适配的资源设置需分别保留。

[原文](https://arxiv.org/pdf/2104.08663v4)
<!-- EVIDENCE:method:END -->

<!-- EVIDENCE:setup:START -->
## 实验设置与分母

主指标nDCG@10（0—1），采用pytrec_eval，无LLM评判器。MS MARCO作为域内参照，其余跨域检索按原数据集相关性标签评分。BM25使用Anserini的k=0.9、b=0.4；TAS-B为在MS MARCO训练的DistilBERT；BM25+CE用MiniLM-L6重排前100条。多数神经模型截取前512个wordpiece，ColBERT另有300长度设置。硬件、语料和截断必须随分数一起看。

[设置来源](https://arxiv.org/pdf/2104.08663v4)
<!-- EVIDENCE:setup:END -->

<!-- EVIDENCE:result-1:START -->
## 域内优势不保证跨域优势

原论文表2的选定数据集，nDCG@10范围0—1；只在同一行内比较，不把不同数据集绝对分数当统一难度。 三个切分的查询数依次为6,980、500、49；nDCG@10按查询求平均。

| 数据集／切分 | BM25 nDCG@10 | TAS-B nDCG@10 | BM25+CE nDCG@10 |
|---|---|---|---|
| MS MARCO 开发集 | 0.228 | 0.408 | 0.413 |
| BioASQ 测试集 | 0.465 | 0.383 | 0.523 |
| Touché-2020 测试集 | 0.367 | 0.162 | 0.271 |

TAS-B在域内MS MARCO优于BM25，但在这两个跨域例子反向。结论是迁移需要测试，不是“稠密检索永远更差”。

事实来源：表2, 第5节 · [原文](https://arxiv.org/pdf/2104.08663v4)
<!-- EVIDENCE:result-1:END -->

<!-- EVIDENCE:result-2:START -->
## 原论文实际测了延迟和索引体积

100万篇DBpedia文档，Xeon8168／8核CPU与V100 GPU；稠密检索使用精确搜索，横线为未报告。

| 系统 | CPU延迟（ms） | GPU延迟（ms） | 索引（GB） |
|---|---|---|---|
| BM25 | 20 | — | 0.4 |
| TAS-B | 125 | 14 | 3 |
| BM25+CE | 6100 | 450 | 0.4 |

因此不能把延迟／索引占用列成完全未测项。仍需在现代硬件、索引实现和实际工作负载下重新验证。

事实来源：表3, 第5节.1 · [原文](https://arxiv.org/pdf/2104.08663v4)
<!-- EVIDENCE:result-2:END -->

<!-- EVIDENCE:result-3:START -->
## 补标会改变关于检索器的判断

TREC-COVID，另加980条人工查询—文档标注；同一数据集下换标注集合，指标仍为nDCG@10。

| 系统 | 原标注nDCG@10 | 扩充标注nDCG@10 |
|---|---|---|
| BM25 | 0.656 | 0.668 |
| ANCE | 0.654 | 0.735 |

ANCE从略低于BM25变为更高，说明结果受原标注池偏向词法检索的影响。补标本身也不是所有未标相关文档的穷尽真值。

事实来源：表4, 第6节 · [原文](https://arxiv.org/pdf/2104.08663v4)
<!-- EVIDENCE:result-3:END -->

<!-- EVIDENCE:limitations:START -->
## 结论边界、缺口与下一步

这是检索排序证据，不能直接推导多轮搜索或RAG最终答案质量。正文称docT5query在11/18项胜过BM25，而图3显示12/18，本文不暗中调和。相比仅优化单一数据集，BEIR强调跨域、资源和标注条件；下一步固定语料、截断、硬件和判定集，做成本匹配对比并补标。

[原始证据](https://arxiv.org/pdf/2104.08663v4)
<!-- EVIDENCE:limitations:END -->

<!-- RESEARCH-DECISION:START -->

上述方法、对照与局限一起决定何时适合使用这个基准；表格不构成跨协议排行榜，结构校验也不证明事实正确或完成复现。

相关测量与对照：[BRIGHT](bright.md) · [RAGBench](ragbench.md) · [KILT](kilt.md)

<!-- RESEARCH-DECISION:END -->
