# DeepResearch Bench：评估研究报告质量与引用支持

<!-- RELEASE-REFERENCE:START -->
> **发布时结果（历史参考，非最佳声明）** · 2025-06-13 · 论文 v1 快照<br>
> **Gemini-2.5-Pro Deep Research — RACE Overall: 48.88** (深度研究智能体 · RACE 总分)；**Perplexity Deep Research — Citation Accuracy: 90.24%** (深度研究智能体 · 引用准确率)<br>
> 保留原始轨道中的指定结果，不把不同指标、子集或系统拼成一个榜首。 [原始来源](https://arxiv.org/abs/2506.11763)<br>
> 来自此前保存的原论文结果记录，仅作历史参考；本次未重跑实验，也不声明当前最佳。
<!-- RELEASE-REFERENCE:END -->

**中文** | [English](deepresearch-bench.en.md) · [基准库](../library/README.md)

<!-- EVIDENCE:reading:START -->
## 阅读范围与版本

已阅读下述主论文全文的方法、实验设置、结果与局限；未独立复现实验。

正文第1–6节及附录A–H，包含局限、指标公式、采集日期、工具设置和全部已提供提示；原文提示存在省略号。

[arXiv v1；提交日期 2025-06-13，PDF 前页日期 2025-06-16](https://arxiv.org/pdf/2506.11763v1)
<!-- EVIDENCE:reading:END -->

<!-- EVIDENCE:placement:START -->
## 与相邻评测相比改变了什么

以下为基于所读协议的编辑比较，不表示论文宣称直接继承。

与BrowseComp的短答案定位不同，这里评估长报告的组织、内容与引用支持。两者是互补坐标：答中一个事实不能证明报告覆盖完整，报告相对评分也不能代替可验证问答正确率。
<!-- EVIDENCE:placement:END -->

<!-- EVIDENCE:method:START -->
## 任务与证据如何构造

任务分布从 96147 条匿名搜索聊天查询中，经 DeepSeek-V3-0324 筛出 44019 条研究请求，再分为 22 个领域；专家据此编写 100 道任务，中英文各 50 道。RACE 先清除引用格式，生成任务特定的四维权重及细化标准，再让 Gemini 2.5 Pro 同时评分目标报告与 Gemini Deep Research 参考报告；最终分数是目标加权分除以目标与参考加权分之和。FACT 则抽取并去重断言—URL 对，用 Jina Reader 取网页，再由 Gemini 2.5 Flash 判断是否支持。引用准确率先逐任务计算再平均，零引用任务记零；有效引用数是每任务受支持断言—URL 对数量，不是独立来源数量。
<!-- EVIDENCE:method:END -->

<!-- EVIDENCE:setup:START -->
## 复现时必须保留的条件

主评测为 100 题、中英文各 50 题。RACE 使用 Gemini 2.5 Pro Preview，FACT 用 Gemini 2.5 Flash；参考报告来自 2025 年 4 月的 Gemini Deep Research。OpenAI 输出采集于 4 月1日–5月8日，Gemini 于4月27–29日，Perplexity 于4月1–29日，Grok 于4月27–29日，均为2025年。普通带搜索 LLM 在可配置时使用高搜索上下文、16000思考 token、最多5轮搜索和36000输出 token/原生上限；这些约束不能推成封闭商业DRA等预算。人工验证为50道中文题×4系统×3人，低一致性过滤后仅37题进入任务级相关性。
<!-- EVIDENCE:setup:END -->

<!-- EVIDENCE:result-1:START -->
## 报告质量、引用精度与数量

100 题；RACE 为相对质量分 ×100；引用准确率为逐任务百分比的宏平均；有效引用数为受支持断言—URL 对／任务。

| 系统 | RACE 综合分 | 引用准确率 | 每任务有效引用数 |
|---|---|---|---|
| Gemini-2.5-Pro Deep Research | 48.88 | 81.44 | 111.21 |
| OpenAI Deep Research | 46.98 | 77.96 | 40.79 |
| Perplexity Deep Research | 42.25 | 90.24 | 31.26 |

事实来源：表 1; 节 3–4; 附录 E · [论文](https://arxiv.org/pdf/2506.11763v1)
<!-- EVIDENCE:result-1:END -->

<!-- EVIDENCE:result-2:START -->
## 评分方法与人工一致性

均以百分数表示；人工样本为 50 道中文题、4 个系统、每题 3 名专家。整体相关性跨 4 个系统均值计算，过滤后相关性只用 ICC≥0 的 37 题；配对分母存在下述报告疑点。

| 方法 | 配对偏好一致率 | 系统均值 Pearson | 过滤后任务平均 Pearson |
|---|---|---|---|
| 直接评分提示 | 58.89 | 98.89 | 40.3 |
| 完整 RACE | 71.33 | 99.54 | 60.24 |
| 去掉参考报告 | 66.56 | 97.46 | 57.51 |

事实来源：表 2; 节 4.3; 附录 F · [论文](https://arxiv.org/pdf/2506.11763v1)
<!-- EVIDENCE:result-2:END -->

<!-- EVIDENCE:interpretation:START -->
## 这些比较支持什么结论

RACE 的 48.88 不是 48.88% 的任务正确率；它是相对参考报告的质量分。Gemini 的有效引用较多，但引用准确率低于 Perplexity，说明信息数量与支持精度会分离。RACE 相比直接评分提高了人类偏好一致性，不过整体 Pearson 只跨四个系统均值计算，不能把 99.54 解读为逐报告准确率；任务级相关性还排除了 13 道低人工一致性题。
<!-- EVIDENCE:interpretation:END -->

<!-- EVIDENCE:limitations:START -->
## 局限、来源冲突与下一步

只有 100 题，人工验证仅限中文 50 题；参考与裁判均来自 Gemini 系列，需外部裁判和参考敏感性验证。FACT 只检查带引用的断言—URL 对，不能直接度量未引用断言的幻觉率或相对所有应有事实的召回率。各商业系统的采集日期和内部预算不同。下一步应固定证据、长度、日期与预算，替换参考报告和裁判，同时报告含低一致性任务的未过滤相关性及逐断言覆盖审查。

附录把50题×4系统×3人称作600份报告，实际为200份不同报告、600次评分。配对定义分母为300，但表2的58.89%不是1/300步长，聚合细节不足。维度权重重复次数T未给定；FACT的100对验证没有分类别分母或完整混淆矩阵。
<!-- EVIDENCE:limitations:END -->

相关基准：[claimprobe](claimprobe.md) · [litreview-arena](litreview-arena.md)
