# T²-RAGBench：检索文本表格后回答数值问题

<!-- RELEASE-REFERENCE:START -->
> **发布时最佳结果（待核验）** · 基准记录日期：2025-05-14<br>
> 尚未核验原始发布版本中可定位到模型、指标和协议的最佳成绩。 [原始来源](https://aclanthology.org/2026.eacl-long.8/)<br>
> 不以最新榜单、单条基线或后续论文成绩代替；未知不代表零分或原作者未报告。
<!-- RELEASE-REFERENCE:END -->

**中文** | [English](t2-ragbench.en.md) · [主入口](../README.md)

<!-- EVIDENCE:reading:START -->
## 阅读范围与版本

已完整阅读所述版本的正文与可用附录，并核对所用结果；未独立复现实验。

完整阅读 EACL 正式论文 27 页，包括正文、局限及附录 A–K：全部六个数据示例、预处理、改写／检索／生成／摘要提示与错误分析；核对表 3–4 和数值评分公式。

[EACL 2026 · 2026.eacl-long.8 · 165–191](https://aclanthology.org/2026.eacl-long.8.pdf)
<!-- EVIDENCE:reading:END -->

<!-- EVIDENCE:method:START -->
## 方法与测量对象

正式版有 23,088 个问题—答案—上下文三元组，来自 FinQA 8,281 题、ConvFinQA 首轮 3,458 题和 TAT-DQA 11,349 题。文本与表格合成一个 Markdown 上下文单元，去重后共 7,318 个，平均约 924 个 token；不应把每个单元当成完整长报告。Llama 3.3-70B 在保留原答案的条件下补充元数据改写问题。示意流程是把笼统的“2009 年自由现金流是多少”改为指定公司及计算口径，检索相关文字／表格，读取行列并计算数值。每题假定只有一个所需金标上下文，替代证据未穷尽。

编辑比较：FinQA、ConvFinQA 和 TAT-DQA 是直接数据来源，原任务给定回答所需上下文；T²-RAGBench 通过补充公司、年份和指标限定，让检索目标可被辨认，再加入检索阶段。新增坐标是找到文本表格证据与数值回答之间的差距；它不是原始 PDF 版面理解、跨报告综合或持续金融分析代理的完整评估。

[来源](https://aclanthology.org/2026.eacl-long.8.pdf)
<!-- EVIDENCE:method:END -->

<!-- EVIDENCE:setup:START -->
## 评分与实验条件

三个子集分别建库和评测，主检索使用 multilingual-e5-large-instruct、Chroma，取前三个单元交给量化 Llama 3.3-70B 或 QwQ-32B；硬件为两张 H100。Hybrid BM25 混合词法和稠密检索；Summarization 用摘要检索并生成，SumContext 用摘要检索但给生成器原文。MRR@3 只计首个金标位置的倒数，Recall@3 计是否命中。Number Match（NM）先取答案绝对值，再消除最接近的十进制尺度差；归一化后的预测／参考比值与1相差小于0.01才算匹配，或两者绝对值均小于0.01时直接算匹配；由定义可知，符号及十的整数幂尺度错误可能不被惩罚，因此不是严格财务数值正确率。生成输出为规定 JSON，非数值失败；完整解码／重试／费用预算未报告。

[来源](https://aclanthology.org/2026.eacl-long.8.pdf)
<!-- EVIDENCE:setup:END -->

<!-- EVIDENCE:result-1:START -->
## 固定 Llama 3.3-70B 的检索与数值结果

三个子集共 23,088 题的问题数加权均值，各自独立语料；E5 检索，前三上下文，量化 Llama 3.3-70B。NM 对符号和十进制尺度不敏感，MRR 与 Recall 定义不同；给定正确上下文的 NM 为 72.7%，不属于真实检索系统。

| 方法 | NM（%） | MRR@3（%） | Recall@3（%） |
| --- | --- | --- | --- |
| Base-RAG | 35.8 | 32.6 | 39.8 |
| Hybrid BM25 | 40.9 | 35.2 | 49.4 |
| Summarization | 22.2 | 36.9 | 46.4 |
| SumContext | 39.5 | 37.0 | 46.3 |

事实位置：表 3，论文集第 171 页（PDF 第 7 页）；第 3、5 节 · [来源](https://aclanthology.org/2026.eacl-long.8.pdf)
<!-- EVIDENCE:result-1:END -->

<!-- EVIDENCE:result-2:START -->
## 总体赢家不等于每个子集赢家

相同 Llama 3.3-70B 设置；三个分母分别 8,281、3,458、11,349 题，上下文数分别 2,789、1,806、2,723。此处只比较数值匹配，不将其解释为所有计算步骤正确。

| 方法 | FinQA NM（%） | ConvFinQA NM（%） | TAT-DQA NM（%） |
| --- | --- | --- | --- |
| Hybrid BM25 | 41.7 | 50.3 | 37.4 |
| SumContext | 47.2 | 55.5 | 29.1 |

事实位置：表 2–3，论文集第 168、171 页（PDF 第 4、7 页） · [来源](https://aclanthology.org/2026.eacl-long.8.pdf)
<!-- EVIDENCE:result-2:END -->

<!-- EVIDENCE:limitations:START -->
## 解读、局限与下一步

Hybrid BM25 的总体 NM 更高，但 SumContext 在 FinQA／ConvFinQA 单独更高，不能宣称每个子集都最优。更高 MRR 也不保证更好答案：摘要可改善定位，却删掉计算所需数值。相同主干曾用于改写和回答，且只抽样验证问题；低闭卷成绩不证明没有训练污染。人工错误分析针对 Llama 在给定金标上下文时的 1,583 个错误样本，不是检索失败分布。主表总体按问题数加权，不能当作三个子集等权平均。

摘要称 91.3% 的问题不依赖预给上下文，第 4.2 节／图 3 却为 93%；不合并成一个确定比例。SumContext 正文均分 37.4／36.7 与表 3 的 39.5／38.3 不同；本页采用表 3。表 4 的 E5 和 OpenAI 数字也与相邻文字不同，若引用应以明确单元格为准。MRR@3 低于 50% 不等于正确文档只在一半查询的前三出现，那是 Recall@3 的含义。正式论文仅含三个来源的 23,088 题，本次未核验更早 32,908 版本或移除过程。

固定该正式版题集和上下文单元，比较原文／摘要索引与原文／摘要阅读的二维组合；并列报告原 NM、保留符号及单位的严格数值检查和证据定位。检查多个有效上下文与改写改变指标的案例，再在独立公司／年份及真实 PDF 解析链上验证泛化。

[来源](https://aclanthology.org/2026.eacl-long.8.pdf)
<!-- EVIDENCE:limitations:END -->
