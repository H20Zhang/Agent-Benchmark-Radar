# LeakDojo：受控 RAG 配置中的内容泄露与防御评估

<!-- RELEASE-REFERENCE:START -->
> **发布时最佳结果（待核验）** · 基准记录日期：2026-04-07<br>
> 尚未核验原始发布版本中可定位到模型、指标和协议的最佳成绩。 [原始来源](https://aclanthology.org/2026.findings-acl.287/)<br>
> 不以最新榜单、单条基线或后续论文成绩代替；未知不代表零分或原作者未报告。
<!-- RELEASE-REFERENCE:END -->

**中文** | [English](leakdojo.en.md) · [主入口](../README.md)

<!-- EVIDENCE:reading:START -->
## 阅读范围与版本

已完整阅读所述版本的正文与可用附录，并核对所用结果；未独立复现实验。

完整阅读正式论文 22 页正文、局限及附录 A–B，涵盖接口与语料、所有指标公式、配置矩阵、预算／温度／阈值分析、成本和完整提示；核对表 3、9。未执行攻击。

[ACL Findings 2026 · 2026.findings-acl.287 · 5790–5811](https://aclanthology.org/2026.findings-acl.287.pdf)
<!-- EVIDENCE:reading:END -->

<!-- EVIDENCE:method:START -->
## 方法与测量对象

实验在公开 SciFact、NFCorpus、FiQA 和 Enron 语料的隔离 RAG 环境中进行，每个原始文档／邮件记录是独立、不重叠的检索单元。评测方知道语料，受测攻击者只通过查询和最终回复交互，至多知道领域。示意流程是安全评测者在有限查询内观察是否重复暴露同一段或不断暴露新记录，再启用输入意图检测／输出内容检测，检查保护效果及正常问答代价。六种既有策略的实现也做了适配，如 PIDE 使用新生成查询、RAG-Thief 借用另一代码框架，因此标签相同不等于逐字复现原攻击。

编辑比较：PoR、RAG-Thief 等既有研究分别给出特定泄露策略，LeakDojo 将查询生成、抽取指令、检索器和防御拆为可配置因素，在相同预算下比较。相较问答准确率或一般提示注入成功率，它新增重复查询中“取到多少不同内容、是否输出、复现多完整”的分解坐标；并非生产访问控制或跨租户隔离测试。

[来源](https://aclanthology.org/2026.findings-acl.287.pdf)
<!-- EVIDENCE:method:END -->

<!-- EVIDENCE:setup:START -->
## 评分与实验条件

默认预算 N=200，主表按原始 RAG、加重排、再加改写三个配置取平均。检索为 bge-large-en-v1.5、Chroma／MMR，候选池 40、相似阈值 0.75；重排为 bge-reranker-large，改写／摘要及多种辅助生成用 gpt-4.1-mini，生成默认贪心。CCL 是唯一泄露单元数除以理想检索量 kN，ARC 是唯一取到单元数除以 kN；两者都不是完整语料被恢复的比例。SLT 是回复与至少一个检索单元的 ROUGE-L recall 大于 0.5 的查询比例。CRR 只在成功触发查询中，计算最长匹配记录内长度至少 50 token 的连续重合块覆盖，再平均。输出防御却用 ROUGE-L F1 阈值，指标与防御标准不同。

[来源](https://aclanthology.org/2026.findings-acl.287.pdf)
<!-- EVIDENCE:setup:END -->

<!-- EVIDENCE:result-1:START -->
## 固定语料下，策略效果随模型反转

Enron 2015 公开语料，200 次查询，按三种 RAG 配置平均；CCL／ARC 分母是 kN，SLT 分母是查询数。88.3% 不表示恢复了 Enron 全库的 88.3%，跨模型也不是同等 token 成本。

| 模型／策略 | CCL（%） | SLT（%） | ARC（%） |
| --- | --- | --- | --- |
| Gemini-3-flash / PoR | 88.3 | 100 | 88.4 |
| DeepSeek-V3 / PoR | 6.8 | 12.0 | 75.4 |
| DeepSeek-V3 / RAG-Thief | 64.4 | 97.3 | 74.8 |

事实位置：表 2，论文集第 5795 页（PDF 第 6 页）；附录 A.3 · [来源](https://aclanthology.org/2026.findings-acl.287.pdf)
<!-- EVIDENCE:result-1:END -->

<!-- EVIDENCE:result-2:START -->
## 防御对旧配置有效，不代表所有测试配置都安全

FiQA、DeepSeek-V3、T2（重排＋改写）、200 次查询；仅展示原论文的受控评估结果，不提供攻击提示。CCL 以 kN 为分母；同时修改指令与防御的行不能解释为单一防御的因果效果。

| GEN-PIDE 配置 | CCL（%） |
| --- | --- |
| 默认配置／无防御 | 57.5 |
| 默认配置／输入检测 | 0.2 |
| CodeClaim／输入检测 | 59.6 |
| CodeClaim／输入与输出检测 | 26.5 |

事实位置：表 3，论文集第 5797 页（PDF 第 8 页） · [来源](https://aclanthology.org/2026.findings-acl.287.pdf)
<!-- EVIDENCE:result-2:END -->

<!-- EVIDENCE:limitations:START -->
## 解读、局限与下一步

同一策略在不同模型上排序反转，说明不能用某一次高分概括普遍泄露风险。CCL 近似 SLT×ARC 是经验拟合，不能证明组件统计独立；指令跟随与泄露的相关性也不是提升能力导致泄露的因果实验。摘要模块可降低近原文泄露，却损失依据完整性，但这不证明所有正确问答与安全之间存在不可避免冲突。只看当前防御拦住旧指令会高估安全：另一些测试配置仍暴露内容。英文公开语料、单元长度、预算和未全面匹配的生成成本限制生产外推。

摘要称 14 个模型，表 4 实际列出 15 行配置；主结果是六模型，其他补充设置不宜拼成统一数量。表 9 的 CCL 从温度 0 时 56.5 降至温度 0.8 时 39.4，不能简单接受正文“温度只影响很小”的概括。表 3 附近把 GEN-PIDE 新配置的 59.6 与 7.3 比较，后者实际是 TGTB 原配置；GEN-PIDE 的对应无防御值是 57.5。本页不沿用错配比较。检索同时列 top_k=10、最终 top_n=5，复现应绑定实际最终 k，不能自行从百分比倒推泄露条数。

仅在获授权的隔离语料中，固定最终检索深度、token／查询预算和记录长度，跨随机种子测原文泄露、语义泄露及正常问答正确率；同时报告相对 kN 与相对语料规模的覆盖。把防御选择与最终压力测试分开，检查误拦截和内容改写后的残余风险，而不是只看一种检测阈值。

[来源](https://aclanthology.org/2026.findings-acl.287.pdf)
<!-- EVIDENCE:limitations:END -->
