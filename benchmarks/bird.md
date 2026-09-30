# BIRD：让 text-to-SQL 真正面对大型、脏的 database content

<!-- RELEASE-REFERENCE:START -->
> **历史论文结果（非首版参考）** · 2023-11-15 · 论文 v3<br>
> **ChatGPT + CoT — Test execution accuracy with evidence: 40.08%**<br>
> v3 表 2 的 ChatGPT + CoT、给定知识证据、1,789 题测试集结果；不是普通 ChatGPT，也不是摘要中的 GPT-4 54.89%。这是后续版本的选定历史基线，不声称首版最佳。 [原始来源](https://arxiv.org/html/2305.03111v3)<br>
> 仅供了解当时难度，不代表当前最佳；不同任务、版本和实验条件不能直接混比。
<!-- RELEASE-REFERENCE:END -->

**中文** | [English](bird.en.md) · [首页](../README.md) · [基准库](../library/README.md)

<!-- EVIDENCE:reading:START -->
## 阅读范围与版本

已完整阅读所列主版本的实质正文与附录；未独立复现实验。

完整阅读 28 页 v3 的实质正文及附录 A.1–A.7、B.1–B.13，包括提示词、执行与 VES 定义，以及人类评测。

[arXiv 2305.03111v3 · 2023-11-15](https://arxiv.org/pdf/2305.03111v3)
<!-- EVIDENCE:reading:END -->

<!-- EVIDENCE:method:START -->
## 方法与测量对象

BIRD 评测依赖数据库取值的 SQL，并比较有无专家知识证据。EX 比较结果集合，忽略重复行与顺序。VES 在全部问题上平均“正确性乘以参考／预测运行时间比的平方根”，错误输出记零。

<!-- EDITORIAL-METHOD:START -->
BIRD 从多个领域收集真实数据库，保留非规范取值和实际规模，人工编写问题、SQL 与外部知识说明，再经复核形成参考。示意流程是：用户以业务简称问一类记录的统计量，模型要把简称映射为真实列值、选择过滤及连接，并输出可在 SQLite 执行的查询；给定证据可直接补充这类映射或计算定义。它因此同时考验模式解释与内容依据。效率指标 VES 只在结果正确时奖励较快执行，并在全部题上聚合，不能单独当作运行速度。

编辑比较：Spider 主要把新模式上的 SQL 结构作为难点，BIRD 增加数据值、外部知识与效率坐标；Spider 2.0 又进一步引入文档、项目代码和交互工作流。BIRD 的大数据库不自动等于已测跨系统发现或生产可靠性。
<!-- EDITORIAL-METHOD:END -->
<!-- EVIDENCE:method:END -->

<!-- EVIDENCE:setup:START -->
## 实验设置

v3 测试集包含 15 个数据库上的 1,789 道题。GPT-4 使用零样本编程提示与温度 0；ChatGPT+CoT 加入一个伪示例。DIN-SQL 还加入检索、示例和自我修正，但未完整报告 token 与重试预算。
<!-- EVIDENCE:setup:END -->

<!-- EVIDENCE:results:START -->
## 精选定量证据

v3 表 2；SQLite 测试集；EX 的分母为全部 1,789 题。仅前两行在同名模型下直接比较是否提供证据。

| 系统／比较项 | 数据集／分母 | 指标／单位 | 结果 | 条件 | 来源 |
| --- | --- | --- | --- | --- | --- |
| GPT-4 · 无证据 | BIRD 测试集；1,789 题／15 个数据库 | EX（%） | 34.88% | gpt-4-32k；T=0 | 表 2, 第 7 页 |
| GPT-4 · 有证据 | BIRD 测试集；1,789 题／15 个数据库 | EX（%） | 54.89% | gpt-4-32k；T=0 | 表 2, 第 7 页 |
| ChatGPT + CoT | BIRD 测试集；1,789 题／15 个数据库 | EX（%） | 40.08% | gpt-3.5-turbo；有证据；T=0 | 表 2, 第 7 页 |
| GPT-4 + DIN-SQL | BIRD 测试集；1,789 题／15 个数据库 | EX（%） | 55.90% | 有证据；扩展框架 | 表 2, 第 7 页 |

事实来源：[表 2, 第 7 页](https://arxiv.org/pdf/2305.03111v3)
<!-- EVIDENCE:results:END -->

<!-- EVIDENCE:limitations:START -->
## 局限与解释边界

页首保留后续 v3 的选取模型结果：有证据的 ChatGPT+CoT 为 40.08%，并非普通 ChatGPT，也非本版最佳结果。v3 日期为 2023-11-15，不冒充初版。92.96% 的人类参考来自专家纠错前的受训标注者，与模型预算不匹配。EX 可能遗漏排序敏感的错误。

<!-- EDITORIAL-NEXT:START -->
下一步对同题分别给正确值映射、正确业务规则和两者，保留 GPT-4 有无证据这一较干净对照；同时对排序／重复敏感题增加精确验证，并统一 DIN-SQL 的重试与 token 预算。否则“框架更好”可能只是额外指导或计算。
<!-- EDITORIAL-NEXT:END -->
<!-- EVIDENCE:limitations:END -->
