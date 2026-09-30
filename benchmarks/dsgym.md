# DSGym：统一执行环境与无数据捷径过滤

<!-- RELEASE-REFERENCE:START -->
> **发布时最佳结果（待核验）** · 基准记录日期：2026-01-22<br>
> 尚未核验原始发布版本中可定位到模型、指标和协议的最佳成绩。 [原始来源](https://arxiv.org/abs/2601.16344)<br>
> 不以最新榜单、单条基线或后续论文成绩代替；未知不代表零分或原作者未报告。
<!-- RELEASE-REFERENCE:END -->

**中文** | [English](dsgym.en.md) · [首页](../README.md) · [基准库](../library/README.md)

<!-- EVIDENCE:reading:START -->
## 阅读范围与版本

已完整阅读所列主版本的实质正文与附录；未独立复现实验。

完整阅读 37 页 v1 的实质正文与附录 A–E，包括筛选、全部竞赛清单、案例、失败定义、训练设置与完整提示词；另检查表 3–5 和图 5。

[arXiv 2601.16344v1 · 2026-01-22](https://arxiv.org/pdf/2601.16344v1)
<!-- EVIDENCE:reading:END -->

<!-- EVIDENCE:method:START -->
## 方法与测量对象

DSGym 统一有状态 Docker/Jupyter 执行。五个模型中至少三个无需数据就能答对的任务会被剔除。SFT 使用 2,000 对合成问题与轨迹，经执行感知评审和语义多样性筛选。

<!-- EDITORIAL-METHOD:START -->
平台为数据分析与预测提供统一、持续的代码执行状态。分析题要求代理从实际文件计算答案；预测题要求建立模型并生成可评分输出。示意流程是查看数据列与分布、在 notebook 中清洗和计算、利用执行反馈修正，再提交结果。无数据过滤先让多个模型不读数据尝试答题，将易被知识或猜测解决的题剔除；合成轨迹再经执行和多样性筛选用于监督训练。这控制了一类捷径，但保留下来的题仍可能存在其他捷径。

编辑比较：相较把 DABStep 等题集分别接入不同执行器，DSGym 强调统一环境与无数据捷径审查；和 DataSciBench 的任务级分项检查相比，它也引入用合成执行轨迹训练的环节。环境统一、题目筛选与训练收益应分开归因。
<!-- EDITORIAL-METHOD:END -->
<!-- EVIDENCE:method:END -->

<!-- EVIDENCE:setup:START -->
## 实验设置

评测采用 CodeAct、温度 0，不启用额外工具，以允许数值容差的完全匹配计分。具体动作、时间、硬件限制、容差与重复次数未写明。SFT 训练六个 epoch，学习率为 2e-5。
<!-- EVIDENCE:setup:END -->

<!-- EVIDENCE:results:START -->
## 精选定量证据

v1 统一框架。分析准确率以实际评测任务为分母；DSBio 为 90 题，论文未明确 DABStep-hard 的实际评测数量。

| 系统／比较项 | 数据集／分母 | 指标／单位 | 结果 | 条件 | 来源 |
| --- | --- | --- | --- | --- | --- |
| Kimi K2 Instruct · DSBio | DSBio；90 题 | 准确率（%） | 43.33% | Kimi-K2-Instruct-0905；T=0 | 表 3, 第 10 页 |
| Qwen3-4B-DSGym-SFT-2k · DSBio | DSBio；90 题 | 准确率（%） | 21.11% | 一般分析 SFT；T=0 | 表 5, 第 13 页 |
| Qwen3-4B-DSGym-SFT-2k · DABStep-hard | DABStep-hard；数量未明确 | 准确率（%） | 33.07% | 种子含 DABStep；T=0 | 表 5, 第 13 页 |
| GPT-4o · DABStep-hard | DABStep-hard；数量未明确 | 准确率（%） | 7.41% | gpt-4o-2024-08-06；T=0 | 表 5, 第 13 页 |

事实来源：[表 3, 第 10 页; 表 5, 第 13 页](https://arxiv.org/pdf/2601.16344v1)
<!-- EVIDENCE:results:END -->

<!-- EVIDENCE:limitations:START -->
## 局限与解释边界

训练后的 4B 模型仅在 DABStep 简单／困难子集上超过 GPT-4o，并未胜过所有分析赛道。无数据筛选不能证明没有污染。DSPredict 报告比例的分母与语料规模关系不清楚，运行预算也未明确。同领域合成任务的种子与测试独立性同样未完整说明。

<!-- EDITORIAL-NEXT:START -->
下一步用未参与过滤的新模型复查捷径，并跨领域划分合成种子与测试题；在相同 CodeAct 与预算下比较未训练、随机轨迹训练和筛选轨迹训练，同时报告原始与过滤后题集表现。
<!-- EDITORIAL-NEXT:END -->
<!-- EVIDENCE:limitations:END -->
