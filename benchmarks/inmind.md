# InMind：直接记得，不代表间接问题会用上

<!-- RELEASE-REFERENCE:START -->
> **发布时诊断结果（历史参考）** · 2026-07 · 论文 v1<br>
> **Naive RAG / text-embedding-3-large / GPT-5-mini — Indirect application, Table 1: 16.0%**；**Always-in-state / GPT-5-mini — Indirect application, Table 2: 68.8%**<br>
> 125 题；分别保留表 1 检索配置最佳和表 2 常驻状态诊断。84.0% 的 oracle 不当成正常检索成绩。 [原始来源](https://arxiv.org/html/2607.24368v1)<br>
> 仅供了解当时难度，不代表当前最佳；不同任务、版本和实验条件不能直接混比。
<!-- RELEASE-REFERENCE:END -->

**中文** | [English](inmind.en.md) · [主入口](../README.md) · [基准资料库](../library/README.md)

<!-- EVIDENCE:reading:START -->
## 阅读范围与版本

已核对所述主论文版本的方法、设置、关键结果与局限；未独立复现实验。

主文第1—8节、补充第9—18节及PDF提示图，包括注入协议、适配器差异和人工评分审计。

[arXiv:2607.24368v1](https://arxiv.org/html/2607.24368v1)

下列表格重新组织了有来源的选定事实。页首历史参考与正文采用的版本、切分和模型可能不同，不能跨表混合成绩。
<!-- EVIDENCE:reading:END -->

<!-- EVIDENCE:method:START -->
## 测量对象、方法与比较

每道题包含个人事实、直接回忆问题，以及需要外部常识桥接的间接问题。内容过滤去掉明显词面或语义线索，再由专家核验关联和正确性。分别测量直接回忆、实际回答上下文是否包含目标事实，以及回答是否应用该事实。

[原文](https://arxiv.org/html/2607.24368v1)
原文案例说明这种落差：系统能在直接追问时说出用户的坚果过敏信息，却在间接的点心推荐中没有正确应用它。关键是让与当前措辞不相似的旧事实进入回答上下文。

<!-- EVIDENCE:method:END -->

<!-- EVIDENCE:setup:START -->
## 实验设置与分母

125道英文题覆盖10个领域，其中113道有公共来源依据，12道由专家编写。背景是同一条47会话LongMemEval-s轨迹。回答与裁判均为GPT-5-mini，多数记忆构建器为GPT-4o-mini。Naive RAG取5个原始片段，A-Mem取10条，其他系统预算不同。Always-in-State由GPT-5-mini更新，状态上限为200行、25,000字节。

[设置来源](https://arxiv.org/html/2607.24368v1)
<!-- EVIDENCE:setup:END -->

<!-- EVIDENCE:result-1:START -->
## 同一题集里，直接回忆和间接应用分开看

125题、GPT-5-mini回答与二元评判；目标召回不看生成答案。直接提供目标的骨干参考和各适配器证据访问不同。

| 配置 | 直接回忆（%） | 目标召回（%） | 应用（%） |
|---|---|---|---|
| Naive RAG (emb3-large) | 97.6 | 6.4 | 16.0 |
| MemoryOS (emb3-large) | 96.8 | 7.2 | 14.4 |
| A-Mem (emb3-large) | 100.0 | 12.0 | 9.6 |
| Backbone (GPT-5-mini) | — | 100.0 | 84.0 |

六种记忆框架最高14.4%与单独Naive RAG对照16.0%是不同范围，并不矛盾。应用高于目标召回也不证明记忆被正确使用，评判器可能把泛化提醒误判为个性化应用。

事实来源：表 1; §4.2–4.4 · [原文](https://arxiv.org/html/2607.24368v1)
<!-- EVIDENCE:result-1:END -->

<!-- EVIDENCE:result-2:START -->
## 始终可见状态是另一种干预

同一125题；Always-in-State使用GPT-5-mini更新器，200行／25,000字节状态预算，不是只切换检索开关。

| 配置 | 直接回忆（%） | 应用（%） |
|---|---|---|
| Always-in-State | 98.4 | 68.8 |

68.8%是该模型与可见状态组合的结果，不能将其与16.0%的全部差距归因于查询条件化。

事实来源：表 2; §5.2 · [原文](https://arxiv.org/html/2607.24368v1)
<!-- EVIDENCE:result-2:END -->

<!-- EVIDENCE:result-3:START -->
## 评分自身有多大误差

附录14.2各抽查100条记录；这些是评分审计计数，不是125题的模型准确率。

| 判定对象 | 人工审计条目数 | 一致条目数 | 假阳性条目数 |
|---|---|---|---|
| 目标召回 | 100 | 97 | 3 |
| 原应用指标 | 100 | 85 | 15 |

原应用评分15/100的假阳性需要和主表一起阅读；不能只用“有个性化的回答”反推成功检索了个人事实。

事实来源：附录 14.2 human audit · [原文](https://arxiv.org/html/2607.24368v1)
<!-- EVIDENCE:result-3:END -->

<!-- EVIDENCE:limitations:START -->
## 结论边界、缺口与下一步

这些结果揭示了特意构造的困难关联中，直接回忆与间接使用之间的明显落差，但不能估计日常流量中的发生率，也不能证明某种架构普遍更优。84.0%的骨干模型结果是模型条件下的参考值，而非硬上限；事后仅答案评分与主表应用指标应分别列出。

主文把目标经历38个后续会话讲得较宽，但附录中A-Mem、HippoRAG 2使用预建库加原始目标的适配路径。不能把所有行都描述成同样的长期摄入干预。相比LongMemEval中的显式回忆测试，这里将需要常识桥接的间接应用单独作为受控目标。

可与LongMemEval的显式回忆测试配对；固定记忆库与回答模型，仅改变检索扩展或同预算的可见状态策略。分别报告目标召回和应用，人工核验假阳性；在归因前匹配更新模型与目标暴露方式。

[原始证据](https://arxiv.org/html/2607.24368v1)
<!-- EVIDENCE:limitations:END -->

<!-- RESEARCH-DECISION:START -->

上述方法、对照与局限一起决定何时适合使用这个基准；表格不构成跨协议排行榜，结构校验也不证明事实正确或完成复现。

相关测量与对照：[LongMemEval](longmemeval.md) · [LoCoMo](locomo.md) · [LoCoMo-Plus](locomo-plus.md)

<!-- RESEARCH-DECISION:END -->
