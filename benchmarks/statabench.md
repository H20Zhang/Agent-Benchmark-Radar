# StatABench：统计判断、工具执行与分析报告

<!-- RELEASE-REFERENCE:START -->
> **发布时最佳结果（待核验）** · 基准记录日期：2026-06-22<br>
> 尚未核验原始发布版本中可定位到模型、指标和协议的最佳成绩。 [原始来源](https://arxiv.org/abs/2606.22977)<br>
> 不以最新榜单、单条基线或后续论文成绩代替；未知不代表零分或原作者未报告。
<!-- RELEASE-REFERENCE:END -->

**中文** | [English](statabench.en.md) · [首页](../README.md) · [基准库](../library/README.md)

<!-- EVIDENCE:reading:START -->
## 阅读范围与版本

已完整阅读所列主版本的实质正文与附录；未独立复现实验。

完整阅读 28 页 PDF 的正文、附录 A–I、全部提示词、工具函数及两份嵌入的生成报告。文本提取中含多余分页字符，实际 PDF 为 28 页。

[arXiv 2606.22977v1 · 2026-06-22](https://arxiv.org/pdf/2606.22977v1)
<!-- EVIDENCE:reading:END -->

<!-- EVIDENCE:method:START -->
## 方法与测量对象

Stat-Closed 包含 404 题，其中 198 题使用 35 函数工具集完成实践任务；Stat-Open 包含 30 项输出报告的建模任务。封闭评测混用直接匹配与语义判断，开放报告获得量表分数，不是执行成功标签。

<!-- EDITORIAL-METHOD:START -->
闭合任务分成概念判断与需要调用统计工具的实践题，开放任务则要求选择模型、分析数据并产出报告。示意流程是面对两组样本，判断检验前提、选择统计函数、解释效应与不确定性；开放报告还需论证方法选择。这样既能暴露概念知识与工具落地的落差，也引入开放报告裁判的偏好。实践题是闭合题中的 198 道子集，不能再与 404 道总量相加。

编辑比较：相较 DS-1000 的功能代码检查，StatABench 同时评概念选择、统计工具使用和开放报告；StatFormBench 则把执行前的问题界定单独拿出来。演化坐标是统计判断，而非仅生成能运行的分析代码。
<!-- EDITORIAL-METHOD:END -->
<!-- EVIDENCE:method:END -->

<!-- EVIDENCE:setup:START -->
## 实验设置

评测温度为 0，关闭 Qwen3-8B 思考。限制是每个交互轮次最多五次工具调用，整体运行时限未明确。开放任务的两个框架共用 DeepSeek-V3，由 Gemini 3 Pro 评审。
<!-- EVIDENCE:setup:END -->

<!-- EVIDENCE:results:START -->
## 精选定量证据

v1 表 3–5，印刷页 7–8。封闭结果为题目准确率，开放结果为评审／人工量表分数，不应混合汇总。

| 系统／比较项 | 数据集／分母 | 指标／单位 | 结果 | 条件 | 来源 |
| --- | --- | --- | --- | --- | --- |
| GPT-5.1 + LangChain MCP | Stat-Closed；404 题 | 准确率（%） | 68.6% | T=0；SAToolKit | 表 3, 第 7 页 |
| DeepSeek-V3 + LangChain MCP | 实践子集；198 题 | 准确率（%） | 53.54% | T=0；统一工具集 | 表 4, 第 7 页 |
| DeepSeek-V3 + CrewAI | 实践子集；198 题 | 准确率（%） | 85.35% | T=0；更换框架 | 表 4, 第 7 页 |
| DeepSeek-V3 + MathModelAgent | Stat-Open；30 项任务；人工子集数量不明 | 评审／人工量表均分（0–100） | 61.86 / 61.17 | Gemini 3 Pro；七项指标 | 表 5, 第 8 页 |
| DeepSeek-V3 + LLM-MM-Agent | Stat-Open；30 项任务；人工子集数量不明 | 评审／人工量表均分（0–100） | 54.29 / 52.62 | Gemini 3 Pro；七项指标 | 表 5, 第 8 页 |

事实来源：[表 3, 第 7 页; 表 4, 第 7 页; 表 5, 第 8 页](https://arxiv.org/pdf/2606.22977v1)
<!-- EVIDENCE:results:END -->

<!-- EVIDENCE:limitations:START -->
## 局限与解释边界

实践题与基础题的差距来自不同任务，不是工具使用消融。表 5 对七项展示指标取平均，不能误作四个高层维度等权。人工子集规模与评审人数表述不清；MathModelAgent 的实践科学性一致度仅 κ=0.092。扰动筛选也不能证明没有污染。

<!-- EDITORIAL-NEXT:START -->
下一步让同一统计问题分别以概念问答、工具执行和报告三种形式出现，固定主干与预算，并让独立统计专家盲审假设、效应解释和错误控制，检验差距来自知识、接口还是报告评分。
<!-- EDITORIAL-NEXT:END -->
<!-- EVIDENCE:limitations:END -->
