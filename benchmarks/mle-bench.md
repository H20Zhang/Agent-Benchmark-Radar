# MLE-bench：竞赛预测交付与历史奖牌阈值

<!-- RELEASE-REFERENCE:START -->
> **发布时最佳结果（历史参考）** · 2024-10-09 · 论文 v1<br>
> **o1-preview + AIDE — Competitions with at least bronze: 16.9%**<br>
> 首版 75 场 Kaggle 竞赛的最佳主实验配置；不是单题准确率或后续延长预算的榜单结果。 [原始来源](https://arxiv.org/abs/2410.07095v1)<br>
> 仅供了解当时难度，不代表当前最佳；不同任务、版本和实验条件不能直接混比。
<!-- RELEASE-REFERENCE:END -->

**中文** | [English](mle-bench.en.md) · [首页](../README.md) · [基准库](../library/README.md)

<!-- EVIDENCE:reading:START -->
## 阅读范围与版本

已完整阅读所列主版本的实质正文与附录；未独立复现实验。

完整阅读 27 页 v1 的实质正文与附录 A.1–A.8，包括完整竞赛划分清单、框架配置及混淆任务示例。

[arXiv 2410.07095v1 · 2024-10-09](https://arxiv.org/pdf/2410.07095v1)
<!-- EVIDENCE:reading:END -->

<!-- EVIDENCE:method:START -->
## 方法与测量对象

MLE-bench 用历史私有排行榜奖牌阈值评测最终预测文件。提交检查器只反馈格式是否有效，不反馈测试成绩。AIDE 搜索候选方案，即使生成模型不同，也使用 GPT-4o 提供反馈。

<!-- EDITORIAL-METHOD:START -->
该基准重新打包 75 场 Kaggle 竞赛，让代理读取描述和训练数据、进行本地实验并输出 submission 文件，再用隐藏评测和原竞赛奖牌线判断结果。AIDE 在候选代码树中调试、扩展及改善方案；OpenHands 则按交互式软件工作流操作。示意任务是根据训练标签构建预测器、在本地验证集选方案、最后生成与测试行对齐的预测。验证器只检查提交格式，所以代理不能借它反复查询隐藏分数；历史网页知识与公开方案仍可能影响结果。

编辑比较：MLAgentBench 侧重相对给定基线的提升，MLE-bench 转向完整竞赛交付及历史奖牌档位；MLE-Dojo 又显式提供迭代分数反馈。这里要区分无隐藏分数反馈的最终交付与可反复看分的优化环境。
<!-- EDITORIAL-METHOD:END -->
<!-- EVIDENCE:method:END -->

<!-- EVIDENCE:setup:START -->
## 实验设置

每次运行允许 24 小时，配置一张 24 GB 显存的 A10、36 个 vCPU 和 440 GB 宿主机内存。OpenHands 子容器额度为 100 GiB。正文规定 AIDE 的 500 个节点，附录配置却列出 2,000 步，两者关系未明确。
<!-- EVIDENCE:setup:END -->

<!-- EVIDENCE:results:START -->
## 精选定量证据

v1；75 项竞赛。Any Medal 为至少达到铜牌的运行占比，并跨种子平均；报告均值 ± SEM。

| 系统／比较项 | 数据集／分母 | 指标／单位 | 结果 | 条件 | 来源 |
| --- | --- | --- | --- | --- | --- |
| o1-preview + AIDE | 75 项竞赛 × 16 个种子 | Any Medal（%） | 16.9 ± 1.1% | 24 h；GPT-4o 反馈 | 表 2, 第 6 页 |
| GPT-4o + AIDE | 75 项竞赛 × 36 个种子 | Any Medal（%） | 8.7 ± 0.5% | 2024-08-06；24 h | 表 2, 第 6 页 |
| GPT-4o + OpenHands | 75 项竞赛 × 3 个种子 | Any Medal（%） | 4.4 ± 1.4% | 2024-08-06；24 h；100 GiB | 表 2, 第 6 页; A.6.2, 第 18 页 |
| GPT-4o + AIDE · pass@6 | 75 项竞赛；由 36 个种子估计 | 任一次成功的覆盖率（%） | 17.0% | 6 次独立尝试 × 24 h | 第 3.2 节, 第 6 页; 图 3, 第 7 页 |

事实来源：[表 2, 第 6 页; 表 2, 第 6 页; A.6.2, 第 18 页; 第 3.2 节, 第 6 页; 图 3, 第 7 页](https://arxiv.org/pdf/2410.07095v1)
<!-- EVIDENCE:results:END -->

<!-- EVIDENCE:limitations:START -->
## 局限与解释边界

奖牌率包含失败运行；SEM 描述种子间变异。pass@6 表示任一次成功的覆盖率，不是经过验证的提交选择策略。重建留出集与后来的方法，使历史人类对照更复杂。不同框架和内存额度也不支持单组件因果归因。

<!-- EDITORIAL-NEXT:START -->
下一步在相同模型、硬件和预算下比较候选树搜索与线性修改，评估不依赖隐藏成绩的候选选择策略；在新竞赛或去标识版本上复验。pass@6 的覆盖优势不能替代部署时如何挑选六个结果的证据。
<!-- EDITORIAL-NEXT:END -->
<!-- EVIDENCE:limitations:END -->
