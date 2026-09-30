# MemBench：记忆准确率、延迟与历史长度压力测试

<!-- RELEASE-REFERENCE:START -->
> **发布时最佳结果（历史参考）** · 2025-06 · 论文 v1<br>
> **RetrievalMemory / Qwen2.5-7B — Factual participation @100K accuracy: 83.3%**；**RetrievalMemory / Qwen2.5-7B — Factual observation @100K accuracy: 93.3%**<br>
> 表 3、固定 Qwen2.5-7B 的两个 100K factual-memory 设置分别比较；不合成反思记忆总分。 [原始来源](https://arxiv.org/html/2506.21605v1)<br>
> 仅供了解当时难度，不代表当前最佳；不同任务、版本和实验条件不能直接混比。
<!-- RELEASE-REFERENCE:END -->

**中文** | [English](membench.en.md) · [首页](../README.md) · [基准库](../library/README.md)

<!-- EVIDENCE:reading:START -->
## 阅读范围与版本

已完整阅读所列版本的实质正文与附录；未独立复现实验。

已阅读全部 17 页，包括第 1–5 节、局限及附录 A–D：档案、事实与反思型样例、统计、生成提示和细分结果；目视核对表 3–4、10–12。

[arXiv v1 / 2025-06-20](https://arxiv.org/pdf/2506.21605v1)
<!-- EVIDENCE:reading:END -->

<!-- EVIDENCE:method:START -->
## 方法与测量对象

MemBench 从用户与实体关系图出发，把属性变成含有证据的对话或观察消息，再插入由新闻构造的无关内容，并按时间顺序写入记忆。合成信息流用于测试事实回忆及偏好、情绪推断。参与式场景回放预设助手回复，并不评测智能体自主选择的行动。答案采用选择题，与标签直接比较；Recall@10 衡量证据检索，延迟对应单次记忆操作（第 3–4 节）。

例如，用户先称活动持续四天，随后纠正为一天，后续选择题应采用新值；用户反复表达对不同甜咸食物的偏好，则支持更高层的口味判断（图 3；附录 A.4）。

### 测量坐标的演进

MemSim 提供了基于关系图的模拟基础。与 LoCoMo、LongMemEval 的长期历史问答相比，MemBench 把参与式与观察式场景、事实型与反思型内容明确分开，并加入操作耗时和历史长度压力。下一步应检验这些已存储或推断出的记忆，能否在相同成本下改善后续行动。
<!-- EVIDENCE:method:END -->

<!-- EVIDENCE:setup:START -->
## 实验设置

主实验使用 MemEngine、Qwen2.5-7B 和 multilingual-e5-small，并用新闻生成的噪声延长历史。普通规模的参与式／观察式样本分别含事实型 360/280 项、反思型 120/60 项；扩展规模分别为 90/84 和 30/15 项。具体记忆上限、采样参数、计时硬件和重复次数未明确报告。
<!-- EVIDENCE:setup:END -->

<!-- EVIDENCE:results:START -->
## 精选定量证据

以下仅摘选原文报告值，不合成总排名。准确率为答对选择题数除以评测题数；论文给出抽样项数，但未完整解释实际分母。计时单位为秒／记忆操作，并非整次回答耗时。

| 系统／比较项 | 数据集／分母 | 指标／单位 | 结果 | 条件 | 来源 |
| --- | --- | --- | --- | --- | --- |
| RetrievalMemory / Qwen2.5-7B／参与式 | 事实型，标称 100K；90 个抽样项 | 选择题准确率（0–1） | 0.833 | MemEngine；multilingual-e5-small；加噪历史 | 表 3, 第 7 页 |
| FullMemory / Qwen2.5-7B／参与式 | 事实型，标称 100K；90 个抽样项 | 选择题准确率（0–1） | 0.489 | 相同事实型样本；窗口上限未说明 | 表 3, 第 7 页 |
| RetrievalMemory / Qwen2.5-7B／观察式 | 事实型，表头标为 100K；84 个抽样项，实际分母未厘清 | 选择题准确率（0–1） | 0.933 | MemEngine；multilingual-e5-small | 表 3, 第 7 页 |
| GenerativeAgent / Qwen2.5-7B／写入 | 事实型参与式；每次操作；计时样本量未说明 | 写入延迟（秒／操作） | 6.116 | 仅记忆写入；硬件未说明 | 表 3, 第 7 页 |
| GenerativeAgent / Qwen2.5-7B／偏好 | 普通规模反思型参与式；切片分母未说明 | 选择题准确率（0–1） | 0.742 | 偏好切片；预设对话 | 表 10, 第 17 页 |
| GenerativeAgent / Qwen2.5-7B／情绪 | 普通规模反思型参与式；切片分母未说明 | 选择题准确率（0–1） | 0.412 | 情绪切片；预设对话 | 表 10, 第 17 页 |

来源：[表 3, 第 7 页; 表 10, 第 17 页](https://arxiv.org/pdf/2506.21605v1)
<!-- EVIDENCE:results:END -->

<!-- EVIDENCE:limitations:START -->
## 局限与解释边界

表 4 的 RetrievalMemory 准确率与表 3 完全重复，应标为原文报告值，不能当作独立确认。其普通规模反思型成绩对应表 10 的偏好列，情绪另列。第 4.1 节与表头的观察式历史长度不一致，0.933 也无法由 84 次单一二值试验还原。因此，容量曲线不能单独界定架构自身的存储上限。
<!-- EVIDENCE:limitations:END -->

<!-- EVIDENCE:next:START -->
## 下一步实验

先公开逐题评分记录，核对重复单元格与长度标签；再固定回答模型和上下文上限复测。增加噪声时保持题目相同，分别绘制事实、偏好、情绪准确率与写入及查询成本的关系。
<!-- EVIDENCE:next:END -->
