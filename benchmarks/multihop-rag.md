# MultiHop-RAG：检索并组合多篇新闻证据

<!-- RELEASE-REFERENCE:START -->
> **发布时最佳结果（待核验）** · 基准记录日期：2024-01<br>
> 尚未核验原始发布版本中可定位到模型、指标和协议的最佳成绩。 [原始来源](https://arxiv.org/abs/2401.15391)<br>
> 不以最新榜单、单条基线或后续论文成绩代替；未知不代表零分或原作者未报告。
<!-- RELEASE-REFERENCE:END -->

**中文** | [English](multihop-rag.en.md) · [基准库](../library/README.md)

<!-- EVIDENCE:reading:START -->
## 阅读范围与版本

已阅读下述主论文全文的方法、实验设置、结果与局限；未独立复现实验。

全文第1–6节、局限及附录A–B的生成提示与例子；表5–6和图3经图像核对。

[v1,2024-01-27](https://arxiv.org/pdf/2401.15391v1)
<!-- EVIDENCE:reading:END -->

<!-- EVIDENCE:placement:START -->
## 与相邻评测相比改变了什么

以下为基于所读协议的编辑比较，不表示论文宣称直接继承。

与HotpotQA的维基百科多跳问答相比，这里换成较新的新闻语料，并显式分开检索质量和给定证据后的生成表现。它延续证据组合问题，却增加时间与无答案条件；不能把不同语料、分母上的提升视为对前代的直接胜出。
<!-- EVIDENCE:placement:END -->

<!-- EVIDENCE:method:START -->
## 任务与证据如何构造

609篇2023年新闻被提取事实并由GPT-4改写为无歧义主张，以实体/主题桥接2–4条证据生成问题，再用UniEval与GPT-4检查。2556题含推断、比较、时间和301道无答案题。
<!-- EVIDENCE:method:END -->

<!-- EVIDENCE:setup:START -->
## 复现时必须保留的条件

609 篇新闻发表于 2023-09-26 至 2023-12-26。2556 题中有 301 道无答案题；检索评价使用 2255 道非空题。LlamaIndex 将材料切成 256-token 块，余弦检索先取 20 块，再用 bge-reranker-large 重排；生成器看到 voyage-02 检索并重排的前六块，最多 2048 token。GPT-4 版本引用为 gpt-4-1106-preview；Mixtral 为 8x7B-Instruct。Hits@k 表示标准证据找回比例，不是“至少找到一条”的概率。
<!-- EVIDENCE:setup:END -->

<!-- EVIDENCE:result-1:START -->
## 同一检索器重排前后

2255 道非空题；Hits@k 是已找回标准证据的比例，单位 0–1；重排从前 20 个候选中选择。

| 检索流程 | Hits@10 | Hits@4 |
|---|---|---|
| voyage-02 | 0.6506 | 0.4619 |
| voyage-02+bge-reranker-large | 0.7467 | 0.6625 |

事实来源：表 5 · [论文](https://arxiv.org/pdf/2401.15391v1)
<!-- EVIDENCE:result-1:END -->

<!-- EVIDENCE:result-2:START -->
## 回答结果：分母不同

答案准确率（0–1）；检索条件分母为全部 2556 题，标准证据条件为 2255 道非空题，因此两列不是严格配对的检索损失。

| 模型 | 检索证据（全部 2556 题） | 标准证据（2255 道非空题） |
|---|---|---|
| GPT-4 | 0.56 | 0.89 |
| Mixtral-8x7B-Instruct | 0.32 | 0.36 |

事实来源：表 6, 节 4.2 · [论文](https://arxiv.org/pdf/2401.15391v1)
<!-- EVIDENCE:result-2:END -->

<!-- EVIDENCE:interpretation:START -->
## 这些比较支持什么结论

检索与给定证据推理均有缺口，但0.56→0.89包含题目分布变化，不能全归因检索。Hits也不代表整条证据链找齐。
<!-- EVIDENCE:interpretation:END -->

<!-- EVIDENCE:limitations:START -->
## 局限、来源冲突与下一步

最多四条证据、短答案、生成器参与验题；新闻新鲜度只相对当时模型成立。下一步在同一非空题集与同一预算上重做检索/金标对照。

检索回答与标准证据回答的分母分别为2556与2255；这是明确的协议不对称，不能隐去。表6称ChatGPT但未给出明确日期版本。
<!-- EVIDENCE:limitations:END -->

相关基准：[hotpotqa](hotpotqa.md) · [agenticragtracer](agenticragtracer.md)
