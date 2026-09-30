# AgenticDataBench：数据科学任务与细粒度技能评估

<!-- RELEASE-REFERENCE:START -->
> **发布时最佳结果（待核验）** · 基准记录日期：2026-07<br>
> 尚未核验原始发布版本中可定位到模型、指标和协议的最佳成绩。 [原始来源](https://arxiv.org/abs/2607.01647)<br>
> 不以最新榜单、单条基线或后续论文成绩代替；未知不代表零分或原作者未报告。
<!-- RELEASE-REFERENCE:END -->

**中文** | [English](agenticdatabench.en.md) · [主入口](../README.md)

<!-- EVIDENCE:reading:START -->
## 阅读范围与版本

已完整阅读下述版本的正文与可用附录，并核对所用结果；未独立复现实验。

完整阅读第 1–7 节及所有方法、设置、结果、技能诊断与预算讨论（14 页，含参考文献；无附录），检查表 4 和图 7–9。

[arXiv 2607.01647v1 · 2026-07-02](https://arxiv.org/pdf/2607.01647v1)
<!-- EVIDENCE:reading:END -->

<!-- EVIDENCE:method:START -->
## 方法与测量对象

AgenticDataBench 先从 6,510 个 Stack Overflow 解法提取 29,602 个步骤描述，再通过嵌入聚类、LLM 拆分合并与专家修订得到 433 项数据技能。它据此选择 102 个真实业务任务，并在公开数据上生成、人工校验 242 个任务，共 344 题、15 个领域。数据处理在 Docker 的 Bash、Python 和数据库环境内完成。四个代理框架分别配对 Qwen3.5-397B-A17B、Kimi-K2.5、Claude Sonnet 4.6；默认温度、不同框架预算：DA-Agent 最多 80 步、保留 15 步历史、每步 1 分钟，Smolagents 最多 40 个编码步骤、每步 5 分钟，Claude Code/CodeX 每题 60 分钟且步骤超时自适应。

[来源](https://arxiv.org/pdf/2607.01647v1)

<!-- EDITORIAL-METHOD:START -->
编辑比较：DataSciBench 与 DA-Code 以任务输出为主要终点，AgenticDataBench 进一步用细粒度技能标签描述同一执行任务。它增加的是诊断分辨率，而不是新的统一成功定义；跨框架的预算和软评分差异仍需独立保留。
<!-- EDITORIAL-METHOD:END -->
<!-- EVIDENCE:method:END -->

<!-- EVIDENCE:setup:START -->
## 评分与实验条件

任务评分结合表格、JSON、文本、图表检查和归一化建模指标，统一到 0–1 后报告百分制总分。另一个 LLM 根据参考解法、技能标注和评分反馈诊断技能使用情况，出现少于三次的技能不进入技能比较。技能诊断是解释层，不是独立的逐步骤可执行真值。

[来源](https://arxiv.org/pdf/2607.01647v1)
<!-- EVIDENCE:setup:END -->

<!-- EVIDENCE:result-1:START -->
## 固定 Kimi-K2.5 的框架与成本对照（选取结果）

344 个任务；任务分数混合二元与连续评分，完整聚合权重未说明；token 是轨迹均值；成功步骤占比以执行步骤为分母，不是答题正确率；预算随框架不同，不能作为等成本消融。

| 框架 | 任务总分（0–100） | 每轨迹 token（千） | 成功执行步骤占比（%） |
| --- | --- | --- | --- |
| Smolagents | 43.8 | 379.4 | 88.1 |
| DA-Agent | 44.8 | 145.4 | 94.1 |
| CodeX | 48.8 | 1091.2 | 59.5 |

事实位置：表 4–5，PDF 第 9–10 页；第 3.3、6.1 节 · [来源](https://arxiv.org/pdf/2607.01647v1)
<!-- EVIDENCE:result-1:END -->

<!-- EVIDENCE:limitations:START -->
## 结果解读、来源限定与下一步

同一 Kimi-K2.5 在不同框架的分数和 token 用量差异很大。CodeX 得分更高，同时平均步骤更多、成功执行步骤占比更低，反映探索与执行效率的取舍，不能仅按报错率排名。不同预算、上下文管理和提示适配共同变化，尚不足以把优势单独归因于技能覆盖或跨步数据复用。

表 4 将 Claude Code/Kimi-K2.5 总分记为 44.3，正文一处误写 43.3。本页采用表格。技能裁判模型、人工一致性验证、重复次数和完整总分权重未说明；最多抽十个失败任务的预算干预不能证明普遍预算不敏感。

固定模型、总时间和 token 预算，在同一框架内分别加入数据概要、跨步骤缓存和技能检索；以任务输出得分为主，同时人工抽检技能诊断准确度，并测量大文件重复读取量与失效缓存问题。

[来源](https://arxiv.org/pdf/2607.01647v1)
<!-- EVIDENCE:limitations:END -->
