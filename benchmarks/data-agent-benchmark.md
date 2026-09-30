# Data Agent Benchmark（DAB）：异构数据库上的企业数据问答

<!-- RELEASE-REFERENCE:START -->
> **发布时最佳结果（历史参考）** · 2026-03-21 · 论文 v1<br>
> **Gemini-3-Pro / paper ReAct agent — Pass@1: 38%**<br>
> 表 3 五个通用模型基线最佳，每题 50 次、跨 12 数据集平均；不含 PromptQL 个案或后续验证器重算榜单。 [原始来源](https://arxiv.org/html/2603.20576v1)<br>
> 仅为原论文口径的历史参考。后续验证器、hints 和专用提示变化后的成绩不直接对比。
<!-- RELEASE-REFERENCE:END -->

**中文** | [English](data-agent-benchmark.en.md) · [主入口](../README.md)

<!-- EVIDENCE:reading:START -->
## 阅读范围与版本

已完整阅读下述版本的正文与可用附录，并核对所用结果；未独立复现实验。

完整阅读 22 页正文和附录 A–C，包括全部 54 个问题、系统与裁判提示和失败案例；另完整读取官方当前 README，核对重新评分事件。未下载外链的全部原始轨迹。

[arXiv 2603.20576v1 · 2026-03-21](https://arxiv.org/pdf/2603.20576v1)
[官方仓库文档 · 2026-09-30](https://github.com/ucbepic/DataAgentBench/blob/main/README.md)
<!-- EVIDENCE:reading:END -->

<!-- EVIDENCE:method:START -->
## 方法与测量对象

DAB 根据六个行业的企业访谈挑出跨数据库整合、错配连接键、文本字段提取与领域规则四类困难，用公开数据及受控扰动构造 54 个查询、12 个数据集、9 个领域、4 种数据库。每题跨至少两库；公开扰动用来模拟业务数据，原始企业数据没有公开。为保证确定真值，作者主动排除了开放式分析问题和动态外部 API。

[来源](https://arxiv.org/pdf/2603.20576v1)

<!-- EDITORIAL-METHOD:START -->
编辑比较：Spider／BIRD 主要围绕给定关系数据库，DAB 将企业访谈中的跨数据库整合、连接键错配、文本提取和领域规则纳入同一道查询。它新增异构数据访问与整合坐标；开放式分析被排除，因此不替代 InsightBench 的主动发现或 DSAgentBench 的桌面操作。
<!-- EDITORIAL-METHOD:END -->
<!-- EVIDENCE:method:END -->

<!-- EVIDENCE:setup:START -->
## 评分与实验条件

主要实验为五种模型各做每题 50 次，共 13,500 次；ReAct 框架给出数据库列举、只读查询、Python 执行和提交答案工具。每次最多 100 轮、1 小时，单工具 600 秒；提供数据集说明和 hints，温度与推理强度用提供方默认值；超过 10,000 字符的工具结果保存到文件并在上下文留预览。pass@1 先按题计算，再按数据集平均，最后对 12 个数据集等权平均，不是 54 题直接微平均或 best-of-50。原版答案检查偏召回，容许夹带错误值。

[来源](https://arxiv.org/pdf/2603.20576v1)
<!-- EVIDENCE:setup:END -->

<!-- EVIDENCE:result-1:START -->
## 原始论文 ReAct 主实验（选取）

v1 原始验证器；54 题×50 次／模型，按 12 数据集等权宏平均；有 hints；ReAct；100 轮／1 小时／单工具 600 秒；费用是 2,700 次总和，不是单题价格。

| 模型 | pass@1（0–1） | 全部 2,700 次运行费用（美元） |
| --- | --- | --- |
| Gemini-3-Pro | 0.38 | 1355 |
| GPT-5-mini | 0.30 | 67 |
| GPT-5.2 | 0.25 | 283 |

事实位置：表 3–4，PDF 第 9 页；第 3.1 节，第 6–7 页 · [来源](https://arxiv.org/pdf/2603.20576v1)
<!-- EVIDENCE:result-1:END -->

<!-- EVIDENCE:result-2:START -->
## 相同 Claude-Opus-4.6 的独立系统对照

表 7；54 题，每题五次，按数据集宏平均；同一 Claude-Opus-4.6；与上表五模型主实验不同；私有框架与语义层共同变化。

| 系统 | pass@1（0–1） |
| --- | --- |
| PromptQL | 0.51 |
| ReAct | 0.44 |

事实位置：第 3.4 节与表 7，PDF 第 11 页 · [来源](https://arxiv.org/pdf/2603.20576v1)
<!-- EVIDENCE:result-2:END -->

<!-- EVIDENCE:limitations:START -->
## 结果解读、来源限定与下一步

PromptQL 对照使用相同 Claude-Opus-4.6、每题五次，属于独立系统对照。其语义层与私有提示／编排同时变化，0.44→0.51 不能单独归因于共享表示。错误分析的 85% 来自 1,147 条“已提交但错误”的抽样轨迹，经 GPT-5 分类，排除了不提交与运行错误，因此不是全部失败的占比。

2026 年 6 月 12 日官方用新验证器及重生成的 PATENTS 真值重新评分；8 月 18 日又允许 DEPS_DEV_V1 并列第五名的任一合法包。所以下面的 v1 数字是历史协议结果，尤其不能继续将 patents 的旧零分解释为当前不可解。当前榜还区分提示定制、hints、缺失及污染运行，不能用新版高分直接做单组件因果结论。

固定当前验证器、提示、模型和预算，比较无 hints／固定 hints，并单独增加有类型的文本提取或可复用数据概要；同时报告精确完整答案、召回式旧检查、费用和跨数据集宏平均，防止评分器变化被当成代理进步。

[来源](https://arxiv.org/pdf/2603.20576v1)
<!-- EVIDENCE:limitations:END -->
