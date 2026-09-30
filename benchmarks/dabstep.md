# DABstep：多步金融数据分析与最终答案评分

<!-- RELEASE-REFERENCE:START -->
> **发布时最佳结果（历史参考）** · 2025-06-30 · 论文 v1<br>
> **o4-mini — Hard accuracy: 14.55%**；**GPT-4.1 — Easy accuracy: 80.56%**<br>
> 表 1 隐藏测试集；Hard 与 Easy 各自的最佳模型不同，不合成单一模型成绩。 [原始来源](https://arxiv.org/html/2506.23719v1)<br>
> 仅供了解当时难度，不代表当前最佳；不同任务、版本和实验条件不能直接混比。
<!-- RELEASE-REFERENCE:END -->

**中文** | [English](dabstep.en.md) · [主入口](../README.md)

<!-- EVIDENCE:reading:START -->
## 阅读范围与版本

已完整阅读下述版本的正文与可用附录，并核对所用结果；未独立复现实验。

完整阅读正文第 1–5 节和附录 A.1–A.4（26 页），逐张检查附录十张执行轨迹图及表 1。

[arXiv 2506.23719v1 · 2025-06-30](https://arxiv.org/pdf/2506.23719v1)
<!-- EVIDENCE:reading:END -->

<!-- EVIDENCE:method:START -->
## 方法与测量对象

DABstep v1 把 Adyen 的匿名业务查询整理成 450 个任务：72 个 Easy、378 个 Hard，来自 95 种核心问题，其中 Hard 由 23 种核心问题参数化扩展。代理读取支付表、费率与商户 JSON、类别及国家映射、规则手册，在隔离 Python 环境中计算一个短答案。评测使用轻量工具封装；通常采用 ReAct 提示，o4-mini、o3-mini、o1、R1 和 Gemini 2.5 Pro 使用另一套推理提示。表 1 报告最多十步；没有给出统一的 token、时间或重复运行预算。

[来源](https://arxiv.org/pdf/2506.23719v1)

<!-- EDITORIAL-METHOD:START -->
编辑比较：WikiSQL／Spider 主要输出查询，DABstep 要在同一业务数据与说明中完成多步金融分析，再以最终答案核对。相较 DA-Code 的异质产物评分，它保留较明确的答案目标。演化含义是把工具串联和业务规则纳入任务，同时不把正确答案误当作整条推理已被验证。
<!-- EDITORIAL-METHOD:END -->
<!-- EVIDENCE:method:END -->

<!-- EVIDENCE:setup:START -->
## 评分与实验条件

成绩是隐藏测试题最终答案的二元正确率，按 Easy 和 Hard 分开统计。评分器进行类型相关的数字、列表和字符串规范化，不依赖 LLM 裁判；数字容差在文字与伪代码中存在差异，应固定实际代码版本。两个标注者检查的 75 个模型答案中，自动评分全部与最终人工标签一致，但这只是小规模评分器验证，不能当作代理答题准确率。

[来源](https://arxiv.org/pdf/2506.23719v1)
<!-- EVIDENCE:setup:END -->

<!-- EVIDENCE:result-1:START -->
## 发布论文的选取基线结果

隐藏测试集；Hard 378 题、Easy 72 题，分别以该分组题数为分母；最终答案二元评分；表 1 的最多十步封装；提示类型不同；未报告跨随机种子方差。

| 模型 | Hard 正确率（%） | Easy 正确率（%） | 提示类型 |
| --- | --- | --- | --- |
| o4-mini | 14.55 | 76.39 | 推理提示 |
| Claude 3.7 Sonnet | 13.76 | 75.00 | ReAct 提示 |
| GPT 4.1 | 12.43 | 80.56 | ReAct 提示 |

事实位置：表 1，PDF 第 3 页；第 3.1–4.1 节，第 5–7 页；附录 A.2，第 13–14 页 · [来源](https://arxiv.org/pdf/2506.23719v1)
<!-- EVIDENCE:result-1:END -->

<!-- EVIDENCE:limitations:START -->
## 结果解读、来源限定与下一步

o4-mini 在 Hard 最好，而 GPT 4.1 在 Easy 更好，不能拼成一个系统的成绩。参数化实例并非 450 个独立工作流；跨核心问题划分比随机实例划分更能检验泛化。附录的 Claude 3.7 Sonnet 轨迹能读取手册、修复 JSON 结构错误并输出合规列表，却遗漏月度欺诈率等费率筛选条件，说明代码可运行与业务规则完整性是两回事。该案例不是量化归因实验。

数字容差在附录文字中示例为 1e-4，算法 1 则写成 1e-2，复现必须固定评分代码。表中历史费用时间标记也不够一致，本页不把它当作当前价格。

按核心问题分组划分任务，固定提示与十步预算，对照原手册、显式结构化规则和正确中间统计量；分别报告业务规则遗漏、数据处理错误、输出格式错误以及执行成本。

[来源](https://arxiv.org/pdf/2506.23719v1)
<!-- EVIDENCE:limitations:END -->
