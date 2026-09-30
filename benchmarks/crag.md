# CRAG：检验时效性、长尾知识与拒答能力

<!-- RELEASE-REFERENCE:START -->
> **发布时最佳结果（历史参考）** · 2024-06 · 论文 v1<br>
> **Copilot Pro — Human-eval Score_h (equal-weighted): 50.6**；**GPT-4 Turbo + Task-3 RAG — Auto-eval accuracy: 43.6%**<br>
> 分别为表 6 商业系统人工评分最佳和表 5 Task-3 基线准确率最佳；两类评分及挑战赛分数不可互换。 [原始来源](https://arxiv.org/html/2406.04744v1)<br>
> 仅供了解当时难度，不代表当前最佳；不同任务、版本和实验条件不能直接混比。
<!-- RELEASE-REFERENCE:END -->

**中文** | [English](crag.en.md) · [基准库](../library/README.md)

<!-- EVIDENCE:reading:START -->
## 阅读范围与版本

已阅读下述主论文全文的方法、实验设置、结果与局限；未独立复现实验。

全文第1–6节及附录A.1–A.4的构造、提示、裁判验证和延迟设置；表5/图2经图像核对。

[v1,2024-06-07](https://arxiv.org/pdf/2406.04744v1)
<!-- EVIDENCE:reading:END -->

<!-- EVIDENCE:placement:START -->
## 与相邻评测相比改变了什么

以下为基于所读协议的编辑比较，不表示论文宣称直接继承。

相较HotpotQA/KILT常用的静态、库内可答任务，CRAG增加时间敏感性、长尾实体、错误前提及拒答，并让网页和知识图谱共同供证。谱系意义在于把答得更多与错误更多的风险取舍显式化，而非只扩大量。
<!-- EVIDENCE:placement:END -->

<!-- EVIDENCE:method:START -->
## 任务与证据如何构造

4409题来自知识图谱模板与人工网页问答，覆盖五领域、八类问题、不同新鲜度和实体热度。提供冻结网页与38个模拟API。任务1用五网页；任务2加知识图谱；任务3扩大至50网页。答对、幻觉与弃答分别计分。
<!-- EVIDENCE:method:END -->

<!-- EVIDENCE:setup:START -->
## 复现时必须保留的条件

主要结果使用 1335 道公开测试题。GPT-4 Turbo 的网页上下文最多 4000 token、KG 上下文最多 2000 token；实体抽取使用 Llama3-8B-Instruct。自动判分先做精确匹配，再平均 GPT-3.5-turbo 与 Llama3-70B-Instruct 的判断。Scorea 是准确率减幻觉率；人工 Scoreh 则给完全正确 1、可接受 0.5、缺失 0、错误 −1。商业系统采用人工评测，不应与冻结网页的自动基线混排。
<!-- EVIDENCE:setup:END -->

<!-- EVIDENCE:result-1:START -->
## 准确率提高不等于风险分提高

1335 道公开测试题，GPT-4 Turbo；前三项为回答比例百分数，Scorea 为准确率减幻觉率的百分点分数；网页上下文 4000 token，KG 2000 token。

| GPT-4 Turbo 条件 | 准确率 | 幻觉率 | 未作答率 | 自动风险分数 |
|---|---|---|---|---|
| 仅语言模型 | 33.5 | 13.5 | 53.0 | 20.0 |
| Task1 | 35.9 | 28.2 | 35.9 | 7.7 |
| Task2 | 41.3 | 25.1 | 33.6 | 16.2 |
| Task3 | 43.6 | 30.1 | 26.3 | 13.4 |

事实来源：表 5, 节 5.1 · [论文](https://arxiv.org/pdf/2406.04744v1)
<!-- EVIDENCE:result-1:END -->

<!-- EVIDENCE:interpretation:START -->
## 这些比较支持什么结论

应保留核心取舍：检索让GPT-4回答更多问题，也增加错误作答，任务3风险敏感分13.4仍低于闭卷20.0。商业系统不是相同协议的对照。
<!-- EVIDENCE:interpretation:END -->

<!-- EVIDENCE:limitations:START -->
## 局限、来源冲突与下一步

商业测试不使用原题目指定查询时间或冻结检索内容，不能和基线直接排序。模拟API不覆盖实时导航。下一步同时间、同来源比较，联合报告错误/弃答。

表5的任务3风险分为13.4，而展示值43.6−30.1等于13.5；这是原因未明的展示差异，原文未证明由舍入造成，保留论文报告值。第5.2节有自动/人工评测的前者后者措辞颠倒，实际设置应按第4节、第5.1节及附录A.4解释。
<!-- EVIDENCE:limitations:END -->

相关基准：[livebrowsecomp](livebrowsecomp.md) · [mtrag-un](mtrag-un.md)
