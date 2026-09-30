# DataSciBench：多步数据科学任务的分项检查与总体成功

<!-- RELEASE-REFERENCE:START -->
> **发布时最佳结果（历史参考）** · 2025-02 · 论文 v1<br>
> **GPT-4o-2024-05-13 — Table 2 overall Score: 64.51**；**GPT-4o-2024-05-13 — Collected-prompts success: 19.82%**<br>
> 分别是表 2 综合评分最佳与表 5 自采集问题成功率最佳；后者不是整个混合题集的准确率。 [原始来源](https://arxiv.org/html/2502.13897v1)<br>
> 仅供了解当时难度，不代表当前最佳；不同任务、版本和实验条件不能直接混比。
<!-- RELEASE-REFERENCE:END -->

**中文** | [English](datascibench.en.md) · [主入口](../README.md)

<!-- EVIDENCE:reading:START -->
## 阅读范围与版本

已完整阅读下述版本的正文与可用附录，并核对所用结果；未独立复现实验。

完整阅读 40 页正文与附录 A.1–A.13、B，包括代码和示例；核对表 2、5、6。

[arXiv 2502.13897v1 · 2025-02-19](https://arxiv.org/html/2502.13897v1)
<!-- EVIDENCE:reading:END -->

<!-- EVIDENCE:method:START -->
## 方法与测量对象

DataSciBench 将数据科学要求拆成任务—功能—检查三层（TFC），用参考解法产生可执行检查。222 题中，167 题来自 BigCodeBench，另外 55 题为其他收集任务；共形成 519 项检查。评测以 DataInterpreter 式规划与执行框架运行 23 个模型，既测结果能否产生，也测是否遵循要求及可视化质量。

[来源](https://arxiv.org/html/2502.13897v1)

<!-- EDITORIAL-METHOD:START -->
编辑比较：DS-1000 检查给定上下文中的代码片段，DataSciBench 将终点扩展为多步数据科学请求，并用按任务选择的检查项核对结果。它比单一字符串或执行通过率更细，但分项、图像与总体成功的尺度不同，不能把所有检查视为同一种正确性。
<!-- EDITORIAL-METHOD:END -->
<!-- EVIDENCE:method:END -->

<!-- EVIDENCE:setup:START -->
## 评分与实验条件

每题运行 10 次，SR 估计单次通过所有 TFC 检查的 pass@1，而不是十次中最好一次的成功率。CR 将缺失／失败、完成但不合要求、符合要求分别记为 0／1／2。综合分数把 65% 权重给 CR，再对 SR、视觉评分与五项功能分数各给 5%；视觉裁判为 GPT-4o-mini，其原始量表是 0–5，不能自行按百分制改写。论文未完整报告温度、工具步数、token 或时间上限。

[来源](https://arxiv.org/html/2502.13897v1)
<!-- EVIDENCE:setup:END -->

<!-- EVIDENCE:result-1:START -->
## 全部222题的选定结果，Table2

全部 222 题、519 项 TFC；每题 10 次，SR 为 pass@1 估计，CR 上限为每项 2 分；DataInterpreter 式框架和 GPT-4o-mini 视觉裁判；其余预算未完整披露。

| 模型 | SR（%） | CR（%） | 综合分数 |
| --- | --- | --- | --- |
| GPT-4o-2024-05-13 | 66.31 | 68.44 | 64.51 |
| Deepseek-Coder-33B-Instruct | 55.86 | 61.23 | 56.76 |
| o1-mini | 29.77 | 45.26 | 38.78 |

事实位置：第 3.2–3.3、4.2 节，公式 2–4；表 2，PDF 第 6 页 · [来源](https://arxiv.org/html/2502.13897v1)
<!-- EVIDENCE:result-1:END -->

<!-- EVIDENCE:result-2:START -->
## GPT-4o同一模型的题源分项，Tables5–6

同一 GPT-4o-2024-05-13；题源分组，55 与 167 是各自分母，每题十次；不是难度匹配的配对干预。

| 模型／题源 | 题数 | SR（%） |
| --- | --- | --- |
| GPT-4o-2024-05-13／其他来源 | 55 | 19.82 |
| GPT-4o-2024-05-13／BigCodeBench 来源 | 167 | 81.62 |

事实位置：第 3.2、5.2 节；附录 A.8 表 5–6，PDF 第 15 页 · [来源](https://arxiv.org/html/2502.13897v1)
<!-- EVIDENCE:result-2:END -->

<!-- EVIDENCE:limitations:START -->
## 结果解读、来源限定与下一步

同一 GPT-4o 在 167 道 BigCodeBench 来源题上的 SR 为 81.62%，在其余 55 题上仅 19.82%。这体现题源和难度组成对总分的影响，不能把 64.51 综合分数替代端到端正确率。

视觉分数与其他检查的尺度不同，必须沿用论文公式与各指标单位。题源分组不是匹配难度实验。

固定框架和预算，按题源与难度分层报告全部检查通过率、部分完成程度和视觉裁判分歧；加入相同底层数据的要求扰动，区分执行能力与要求遵循。

[来源](https://arxiv.org/html/2502.13897v1)
<!-- EVIDENCE:limitations:END -->
