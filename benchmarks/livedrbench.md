# LiveDRBench：把证据发现与主张提取同报告写作分开

<!-- RELEASE-REFERENCE:START -->
> **发布时最佳结果（历史参考）** · 2025-08-06 · 论文 v1<br>
> **OpenAI deep research — Overall F1: 0.55**<br>
> 初始实验中最佳的深度研究系统；在 100 个任务的结构化主张发现上计分，不是报告文风评分。 [原始来源](https://arxiv.org/abs/2508.04183v1)<br>
> 仅供了解当时难度，不代表当前最佳；不同任务、版本和实验条件不能直接混比。
<!-- RELEASE-REFERENCE:END -->

**中文** | [English](livedrbench.en.md) · [基准库](../library/README.md)

<!-- EVIDENCE:reading:START -->
## 阅读范围与版本

已阅读下述主论文全文的方法、实验设置、结果与局限；未独立复现实验。

27页正文第1–6节和附录A–D均已阅读，包括全部任务例子、主张匹配与轨迹提示、作者人工重评；未运行代码或核验商业系统内部配置。

[arXiv v1, 2025-08-06](https://arxiv.org/pdf/2508.04183v1)
<!-- EVIDENCE:reading:END -->

<!-- EVIDENCE:placement:START -->
## 与相邻评测相比改变了什么

以下为基于所读协议的编辑比较，不表示论文宣称直接继承。

相较DeepResearch Bench的长报告质量评价，LiveDRBench把输出约束为结构化主张和子主张。它把研究中的证据发现与字段提取拆出来，代价是不直接测自由报告的组织和叙述质量。
<!-- EVIDENCE:placement:END -->

<!-- EVIDENCE:method:START -->
## 任务与证据如何构造

100道任务覆盖八类：材料17、地学19、新数据集识别6、识别与提取11、同类数据集检索3、先前研究17、实体枚举20、航班调查7。作者从论文、审稿意见和调查报告反向构造需要检索与推理的请求，要求嵌套JSON中的顶层主张和支持子主张。标准指标把顶层匹配与递归子主张精度/召回结合，再逐题计算F1；找到论文却抽错关键材料不能拿到同等分数。严格变体取最差子主张，但主表报告标准变体。作者人工检查所有系统的输出，把有效遗漏项补入金标，然后统一重评；这改善覆盖，仍不是全网穷尽证明。
<!-- EVIDENCE:method:END -->

<!-- EVIDENCE:setup:START -->
## 复现时必须保留的条件

三种Deep Research通过聊天界面手动运行，澄清问题统一回复让其继续；普通搜索模型经API运行。o4-mini为low、Sonar推理为medium、Gemini 2.5 Pro思考预算128 token，作者称约30秒；OpenAI/Perplexity搜索上下文medium，其他默认。它们与商业DR不是等算力比较。GPT-4o判主张匹配，NovelDS/Flights先按主键对齐字典，再给每字段0–3分；数值允许1%误差。个别Gemini长文被人工转换为JSON。表中逐题F1再平均，不能由总平均精度/召回重新计算。附录D用作者判断重复评分，没有报告独立盲审或一致性系数。
<!-- EVIDENCE:setup:END -->

<!-- EVIDENCE:result-1:START -->
## 整体成绩与两种平均

100题、8类别；所有分数0–1，越高越好。GPT-4o主张判分；题数加权等价逐题平均，类别宏平均给每类相同权重。商业DR预算不透明且未对齐。

| 系统 | 题数加权精度 | 题数加权召回 | 题数加权F1 | 类别宏平均F1 |
|---|---|---|---|---|
| OpenAI Deep Research | 0.629 | 0.519 | 0.55 | 0.555 |
| Perplexity Deep Research | 0.462 | 0.286 | 0.331 | 0.355 |
| Gemini Deep Research 2.5 Pro | 0.309 | 0.215 | 0.236 | 0.263 |

事实来源：表 2; 节 5.2 · [论文](https://arxiv.org/pdf/2508.04183v1)
<!-- EVIDENCE:result-1:END -->

<!-- EVIDENCE:result-2:START -->
## 类别结构与人工重判

材料17题、地学19题；后两列是100题的八类等权宏平均，单位0–1。材料要求嵌套提取而地学不含同样子主张结构，跨类别差异不是纯检索能力差异。作者重判未给独立标注一致性。

| 系统 | 材料F1：GPT-4o | 地学F1：GPT-4o | 宏平均F1：GPT-4o | 宏平均F1：作者 |
|---|---|---|---|---|
| OpenAI Deep Research | 0.314 | 0.721 | 0.555 | 0.556 |
| Perplexity Deep Research | 0.15 | 0.186 | 0.355 | 0.361 |
| Gemini Deep Research 2.5 Pro | 0.022 | 0.316 | 0.263 | 0.261 |

事实来源：表 2; 附录 D 表 11 · [论文](https://arxiv.org/pdf/2508.04183v1)
<!-- EVIDENCE:result-2:END -->

<!-- EVIDENCE:interpretation:START -->
## 这些比较支持什么结论

主表按题数加权的F1分别为0.550、0.331、0.236；八类别等权则为0.555、0.355、0.263，两种平均不能混写。OpenAI材料题论文名F1为0.735、材料名0.504，联合仅0.314，说明单独找到一个字段不代表正确完成研究证据链。人工重判类别宏平均保持系统排序，但不能据此宣称裁判对所有未来系统无偏。轨迹“每来源/回溯F1”只是行为代理，不是美元、延迟或token效率。
<!-- EVIDENCE:interpretation:END -->

<!-- EVIDENCE:limitations:START -->
## 局限、来源冲突与下一步

八类样本很少且不均衡，Peer Retrieval仅3题；不同答案嵌套结构也改变评分难度。作者参与构造及重判，金标扩充依赖所测系统发现的答案。商业界面没有精确可复现的内部模型、工具及算力预算，结果不能当作当前产品排名。公开摘要轨迹并非完整内部推理，分支/回溯与表现的关系不证明因果；“Live”描述可刷新构造方式，本次未核验持续更新。下一步固定版本和预算，预注册独立人工裁判、发布逐题输出与新增金标，并对字段匹配严格度和缺失来源做敏感性分析。

第4.2.1节称SciFacts为31题，但表1的17+19为36，全表合计才是100。材料分析段给Perplexity联合F1为0.158、Gemini为0.023，表2却为0.150/0.022，本文明确按表归属。附录裁判提示把CNN与ResNet视为等价，宽松匹配可能抹去重要细节。表11是作者重判条件，不能无说明替换表2的GPT-4o结果。
<!-- EVIDENCE:limitations:END -->

相关基准：[deepresearch-bench](deepresearch-bench.md) · [claimprobe](claimprobe.md) · [mr-lhdr](mr-lhdr.md)
