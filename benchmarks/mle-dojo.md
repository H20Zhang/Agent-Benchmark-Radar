# MLE-Dojo：带评分反馈的迭代机器学习环境

<!-- RELEASE-REFERENCE:START -->
> **发布时最佳结果（待核验）** · 基准记录日期：2025-05-12<br>
> 尚未核验原始发布版本中可定位到模型、指标和协议的最佳成绩。 [原始来源](https://arxiv.org/abs/2505.07782)<br>
> 不以最新榜单、单条基线或后续论文成绩代替；未知不代表零分或原作者未报告。
<!-- RELEASE-REFERENCE:END -->

**中文** | [English](mle-dojo.en.md) · [首页](../README.md) · [基准库](../library/README.md)

<!-- EVIDENCE:reading:START -->
## 阅读范围与版本

已完整阅读所列主版本的实质正文与附录；未独立复现实验。

完整阅读 36 页 v1 的实质正文与附录 A–I，包括完整任务清单、指标定义、提示词、示例与两种 agent 集成。

[arXiv 2505.07782v1 · 2025-05-12](https://arxiv.org/pdf/2505.07782v1)
<!-- EVIDENCE:reading:END -->

<!-- EVIDENCE:method:START -->
## 方法与测量对象

MLE-Dojo 在迭代环境中提供竞赛分数反馈。HumanRank 平均公榜与私榜的相对排名，不是任务成功率。AUP 汇总跨任务性能分布，不是连续动作带来的提升曲线。

<!-- EDITORIAL-METHOD:START -->
环境将 200 个竞赛组织为可重置任务，代理提交预测后获得评分反馈并继续修改；因此既可用于评测，也为未来策略训练提供接口。示意流程是读取数据、训练初始模型、提交、据公开／私有榜单映射后的反馈调整特征，再选择最终版本。这个循环测反馈条件下的优化，和不知道最终测试分数的单次提交不同。HumanRank 衡量相对历史参与者的位置，不能理解为完成了多少任务或超过了多少独立专家。

编辑比较：MLE-bench 是最直接的竞赛交付参照，MLE-Dojo 增加可迭代奖励和训练／评估任务划分。演化含义是将评测环境同时变为潜在学习环境，但存在训练接口不代表论文已经证明训练后迁移。
<!-- EDITORIAL-METHOD:END -->
<!-- EVIDENCE:method:END -->

<!-- EVIDENCE:setup:START -->
## 实验设置

主结果采用 MLE Agent，两次运行取优，最多 15 步、12 小时，GPU 显存上限 32 GB，输入上限 50k token、输出上限 8,192 token。语料包含 150 项训练任务、50 项评测任务。
<!-- EVIDENCE:setup:END -->

<!-- EVIDENCE:results:START -->
## 精选定量证据

v1 表 2；同一 MLE Agent 与两次取优反馈协议。HumanRank 为平均排行榜百分位，越高越好。

| 系统／比较项 | 数据集／分母 | 指标／单位 | 结果 | 条件 | 来源 |
| --- | --- | --- | --- | --- | --- |
| Gemini-2.5-Pro · Tabular | 表格数据；10 项评测任务 | 平均 HumanRank（%） | 42.64% | exp-3-25；统一框架 | 表 2, 第 9 页; 表 4, 第 25–26 页 |
| DeepSeek-r1 · Tabular | 表格数据；10 项评测任务 | 平均 HumanRank（%） | 38.13% | 统一框架 | 表 2, 第 9 页; 表 4, 第 25–26 页 |
| Gemini-2.5-Pro · CV | 视觉；10 项评测任务 | 平均 HumanRank（%） | 42.83% | exp-3-25；统一框架 | 表 2, 第 9 页; 表 4, 第 25 页 |
| o3-mini · CV | 视觉；10 项评测任务 | 平均 HumanRank（%） | 35.02% | 2025-01-31；统一框架 | 表 2, 第 9 页; 表 4, 第 25 页 |

事实来源：[表 2, 第 9 页; 表 4, 第 25–26 页; 表 2, 第 9 页; 表 4, 第 25 页](https://arxiv.org/pdf/2505.07782v1)
<!-- EVIDENCE:results:END -->

<!-- EVIDENCE:limitations:START -->
## 局限与解释边界

该划分为后续训练实验提供条件，但论文没有展示学到的策略迁移。MLE-Lite 数量不一致：脚注写 22，评测清单列 21。下表的表格数据与视觉子集各有十项任务。AUP 的公式与报告口径也有差异，澄清前不宜作精确比较。

<!-- EDITORIAL-NEXT:START -->
下一步对同一任务比较不看分、仅看公开验证分和完整反馈三种条件，统一步数及硬件，并用独立最终留出集验证。将 best-of-two 改为预先规定的选择策略，区分反馈过拟合与可迁移改进。
<!-- EDITORIAL-NEXT:END -->
<!-- EVIDENCE:limitations:END -->
