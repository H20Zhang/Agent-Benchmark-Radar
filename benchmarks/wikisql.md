# WikiSQL：未见单表上的 SQL 生成

<!-- RELEASE-REFERENCE:START -->
> **发布时最佳结果（历史参考）** · 2017-08-31 · 论文 v1<br>
> **Seq2SQL — Execution accuracy: 60.3%**；**Seq2SQL — Logical-form accuracy: 49.2%**<br>
> 首版 Seq2SQL 的执行准确率与逻辑形式准确率；v1 数据规模为 87,726 例。后续 v7 的 59.4%／48.3% 与 80,654 例另列，不能归到首版。 [原始来源](https://arxiv.org/abs/1709.00103v1)<br>
> 仅供了解当时难度，不代表当前最佳；不同任务、版本和实验条件不能直接混比。
<!-- RELEASE-REFERENCE:END -->

**中文** | [English](wikisql.en.md) · [首页](../README.md) · [基准库](../library/README.md)

<!-- EVIDENCE:reading:START -->
## 阅读范围与版本

已完整阅读所列主版本的实质正文与附录；未独立复现实验。

完整阅读 v1 与 v7 的实质正文及附录 A–C，包括数据收集、基线细节与预测示例。

[arXiv 1709.00103v7 · 2017-11-09](https://arxiv.org/pdf/1709.00103v7) · [arXiv 1709.00103v1 · 2017-08-31](https://arxiv.org/pdf/1709.00103v1)
<!-- EVIDENCE:reading:END -->

<!-- EVIDENCE:method:START -->
## 方法与测量对象

WikiSQL 保留未见表作为测试，但每条查询只涉及单表。Seq2SQL 分别预测聚合与选择列，再用执行奖励训练 WHERE 生成。这是训练反馈，不是推理阶段的修复循环。

<!-- EDITORIAL-METHOD:START -->
题目从 Wikipedia HTML 表格生成 SQL 模板后，由众包改写为自然语言并验证；输出限制为选择列、可选聚合和 WHERE 条件，不包含跨表连接。示意输入是某张运动员表及“某国运动员的平均年龄”，输出选择年龄列、AVG 和国家过滤条件。Seq2SQL 用受限指针词表减少无效符号，再分开预测聚合、选择列与条件；WHERE 条件的次序不改变语义，因此执行奖励允许不同有效顺序，比只模仿某条参考序列更合适。

编辑比较：相较普通序列到序列语义解析，WikiSQL 提供较大规模的跨表划分与可执行监督；Spider 则把这一坐标继续扩展到多表和嵌套 SQL。这里的进展是训练目标与 SQL 结构的结合，不是已经实现交互式数据库代理。
<!-- EDITORIAL-METHOD:END -->
<!-- EVIDENCE:method:END -->

<!-- EVIDENCE:setup:START -->
## 实验设置

v7 包含 80,654 个样本、24,241 张表。最多训练 300 个 epoch，以开发集执行成绩提前停止。推理使用问题和模式；表内容用于训练奖励及评测。
<!-- EVIDENCE:setup:END -->

<!-- EVIDENCE:results:START -->
## 精选定量证据

v7 表 2；测试表与训练表不重叠。EX 为执行准确率，LF 为逻辑形式准确率，分母均为测试样本；采用同一组训练与评测设置。

| 系统／比较项 | 数据集／分母 | 指标／单位 | 结果 | 条件 | 来源 |
| --- | --- | --- | --- | --- | --- |
| Aug Ptr Network | WikiSQL v7 测试集 | EX / LF（%） | 53.3% / 43.3% | 限制指针输出空间 | 表 2, 第 7 页 |
| Seq2SQL (no RL) | WikiSQL v7 测试集 | EX / LF（%） | 57.1% / 47.4% | 结构化解码；教师强制训练 | 表 2, 第 7 页 |
| Seq2SQL | WikiSQL v7 测试集 | EX / LF（%） | 59.4% / 48.3% | 预训练后用策略梯度训练 WHERE | 表 2, 第 7 页 |

事实来源：[表 2, 第 7 页](https://arxiv.org/pdf/1709.00103v7)
<!-- EVIDENCE:results:END -->

<!-- EVIDENCE:limitations:START -->
## 局限与解释边界

无 RL 对照支持 v7 的 EX 提升 2.3 个百分点，完整基线差距则混合多项改变。页首是真正 v1 的 EX 60.3%、LF 49.2%：当时有 87,726 个样本、训练上限 100 个 epoch；正文 v7 则为 80,654 个样本及 300 个 epoch，必须分开。LF 可能误拒等价 SQL，EX 可能接受碰巧一致的结果。

<!-- EDITORIAL-NEXT:START -->
下一步固定指针网络和数据划分，只替换 WHERE 训练目标，并增加能区分碰巧等价结果的表内容扰动。随后加入连接任务，检查执行奖励的优势能否迁移，而不是从单表成绩直接推断跨库能力。
<!-- EDITORIAL-NEXT:END -->
<!-- EVIDENCE:limitations:END -->
