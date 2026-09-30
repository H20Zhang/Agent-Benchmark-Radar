# The Compaction Cliff：保留指标、行为效果与预算边界

<!-- RELEASE-REFERENCE:START -->
> **发布时诊断结果（历史参考）** · 2026-08-24 · 论文 v1 快照<br>
> **TypeCompact — Constraint recall after five compaction rounds: 96%** (五轮压缩后的约束保留率)<br>
> TypeCompact 确定性算子的五轮约束保留诊断；Claude Sonnet 是独立对照，不是该算子的回答模型。公开工件为 20 个配置、五次名义 50% 压缩目标，约数 96%。 [原始来源](https://arxiv.org/html/2608.22752v1)<br>
> 公开实现传递未截断的类型化状态，而 LLM 传递截断文本；此诊断不证明同等可行预算下的优势或通用安全保证。未重跑实验。
<!-- RELEASE-REFERENCE:END -->

**中文** | [English](compaction-cliff.en.md)

<!-- EVIDENCE:reading:START -->
## 阅读范围与版本

已核对所述论文版本的方法、实验设置、关键结果与局限；未独立复现实验。

已阅读全部六节正文、十张表、算法与局限，本版本无附录。完整阅读固定提交a6ceb01a3368cee25ef7ebcf05ebdab8c9be24a4的README、三个算子、保留评分、SafetyMargin及多轮实验脚本，核对多轮冻结JSON。未独立执行或审计全部行为轨迹。

[arXiv 2608.22752v1 (2026-08-24)](https://arxiv.org/html/2608.22752v1)

[辅助材料（2026-09-30查阅）](https://github.com/searchsim-org/cikm26-knowledge-triage/blob/a6ceb01a3368cee25ef7ebcf05ebdab8c9be24a4/README.md)

[辅助材料（2026-09-30查阅）](https://github.com/searchsim-org/cikm26-knowledge-triage/blob/a6ceb01a3368cee25ef7ebcf05ebdab8c9be24a4/knowledge_triage/operators.py)

[辅助材料（2026-09-30查阅）](https://github.com/searchsim-org/cikm26-knowledge-triage/blob/a6ceb01a3368cee25ef7ebcf05ebdab8c9be24a4/knowledge_triage/preservation.py)

[辅助材料（2026-09-30查阅）](https://github.com/searchsim-org/cikm26-knowledge-triage/blob/a6ceb01a3368cee25ef7ebcf05ebdab8c9be24a4/knowledge_triage/safety_margin.py)

[辅助材料（2026-09-30查阅）](https://github.com/searchsim-org/cikm26-knowledge-triage/blob/a6ceb01a3368cee25ef7ebcf05ebdab8c9be24a4/experiments/multiturn_stability.py)

[辅助材料（2026-09-30查阅）](https://github.com/searchsim-org/cikm26-knowledge-triage/blob/a6ceb01a3368cee25ef7ebcf05ebdab8c9be24a4/results/multiturn_stability.json)

页首历史参考原样保留；正文的新版本结果不能代替原始发布成绩。
<!-- EVIDENCE:reading:END -->

<!-- EVIDENCE:method:START -->
## 任务怎样产生记忆需求

本文既提出Knowledge Triage方法，也提供压缩、分区、检索和行为测试。它先把每行信息分为约束、程序、信念、偏好、事件，再决定保留方式：TypeCompact固定约束和程序；TypeDecompose将约束复制到所有适用分区；TypeRetrieve优先返回适用约束。SafetyMargin让模型判断删除某条信息是否会使行动不安全，这是模型估计，不是真实行动干预。例如“存在某种过敏”虽没有“禁止”词，也可能需要进入硬保留区。

谱系：论文以MaRS的类型化记忆与单一效用选择为最近的方法比较，改变的是每种信息的保真要求；MaRS-FL是作者重实现，不是原方法官方运行。与LLMLingua-2的压缩目标相比，它优先保护约束。数据层面新建AAC配置语料，并借用零售、航空、检索等既有任务；不能把这些不同协议汇成一个安全分数。
<!-- EVIDENCE:method:END -->

<!-- EVIDENCE:setup:START -->
## 实验设置与评分对象

AAC包含来自54628个公开仓库的396934份配置材料；这不是每项实验的分母。类型分析用2000条标注；压缩结构对照50份配置，LLM和多轮对照20份；分区200份；检索为1000篇scifact干扰文档加33块零售政策、50个手写查询。检索金集合是分类器标出的22块约束中与查询主题相交的部分，平均每查询12块，并非人工发现全部真实约束。自动保留指标检查最多五个关键词是否出现在整个输出，允许语义削弱漏检。声明的算子保证依赖正确分类、作用域和足够预算，不等于行动合规。
<!-- EVIDENCE:setup:END -->

<!-- EVIDENCE:result-1:START -->
## 单轮目标和五轮累计损失分别读

0—1约束保留率，按配置平均；前三列是单轮目标，末列另用每轮50%的五轮实验，不是同一压缩比例。LLM输出截到预算后评分。零推理词元只指算子阶段，未计先前分类成本。

LLM与多轮对照为20份配置；MaRS-FL无对应五轮数据。

| 方法 | 单轮50%预算 | 单轮25%预算 | 单轮10%预算 | 第五轮 |
|---|---|---|---|---|
| TypeCompact | 1 | 0.95 | 0.8 | 0.96 |
| MaRS-FL | 0.99 | 0.75 | 0.43 | — |
| Sonnet 4.6 | 0.53 | 0.39 | 0.24 | 0.1 |

定位：表6与图3：部分约束保留结果 · [原文](https://arxiv.org/html/2608.22752v1)
<!-- EVIDENCE:result-1:END -->

<!-- EVIDENCE:result-2:START -->
## 93%是存在违规的配置比例

论文报告的两种违规口径必须分开。标题式主题标记确定作用域，各组共享；复制成本中位数0、最坏219%。实现中的分区预算边界另见局限。

200份配置，单分区目标为总词元的25%。

| 方法 | 平均违规率% | 存在违规的配置% | 平均额外词元% |
|---|---|---|---|
| chunk_by_tokens | 32 | 93 | 0 |
| chunk_by_topic | 13 | 40 | 0 |
| TypeDecompose | 0 | 0 | 14.5 |

定位：表7：部分分区结果 · [原文](https://arxiv.org/html/2608.22752v1)
<!-- EVIDENCE:result-2:END -->

<!-- EVIDENCE:result-3:START -->
## 召回优势取决于比较对象与预算

召回率只覆盖分类器判为约束且主题匹配的项目。Sonnet从稠密检索前100项选择并排序；TypeRetrieve直接固定适用集合。100%依赖k足够大，不能推广到k=5。

1033条混合材料、50个查询，金约束每查询平均12条。

| 检索器 | Recall@5% | Recall@20% | Recall@50% |
|---|---|---|---|
| Dense (octen) | 34 | 67 | 91 |
| Sonnet 4.6 | 34 | 61 | 73 |
| TypeRetrieve | 40 | 96 | 100 |

定位：表8：部分检索对照 · [原文](https://arxiv.org/html/2608.22752v1)
<!-- EVIDENCE:result-3:END -->

<!-- EVIDENCE:result-4:START -->
## 通过率必须保留共同样本与词元条件

分层基线是保留开头文本，不是通用LLM摘要。零售115题×三模型，共345潜在模型—任务对，剔除未完整完成的对后329；航空50题×三模型后117。SafetyMed另有Sonnet压缩器通过率92.5%、保留率81%，TypeCompact相应97%和95.5%。

SafetyMed 200例；零售329、航空117个完整配对，排除未完整完成的条件。零售完整/分层/TypeCompact为1338/669/1136词元，航空分层/TypeCompact为718/647。

| 设置 | 完整政策通过率% | 分层截断通过率% | TypeCompact通过率% | 共同配对数 |
|---|---|---|---|---|
| SafetyMed | 96.5 | 98 | 97 | 200 |
| Retail | 28.6 | 29.2 | 37.7 | 329 |
| Airline | 34.2 | 15.4 | 26.5 | 117 |

定位：第4.5节与表10：行为结果 · [原文](https://arxiv.org/html/2608.22752v1)
<!-- EVIDENCE:result-4:END -->

<!-- EVIDENCE:result-5:START -->
## 人工之间一致不等于自动评分可靠

前两行是已知为约束的50条规则的陈述式改写；后两行是压缩结果审核，κ与一致率不是同一指标。分类器五分类与人工κ仅0.45，约束二分类κ为0.79。

前两行为50条规则的陈述式变体；压缩审核100格，其中80格双人标注。

| 检查 | 数值 | 分母 |
|---|---|---|
| 语法分类器陈述式召回 | 0.62 | 50 |
| SafetyMargin陈述式召回 | 0.9 | 50 |
| 人工之间二分类κ | 0.92 | 80 |
| 自动指标与人工一致率 | 0.79 | 100 |

定位：第4.4—4.5节：分类与评分审核 · [原文](https://arxiv.org/html/2608.22752v1)
<!-- EVIDENCE:result-5:END -->

<!-- EVIDENCE:limitations:START -->
## 结论边界与下一步验证

保留率不是行为正确率，完整政策也不是普遍上限：零售TypeCompact高于完整政策，航空低于完整政策且差异未显著，不能把“未显著”写成等价。零售额外保留词元混淆机制归因；航空预算方向相反但不是同一任务的等词元控制。人工审核显示自动指标会把丢限定词的规则算作保留，不能用人工之间κ=0.92宣称自动评分同样可靠。

固定实现还与论文算法有实质差异：operators.py的TypeCompact没有描述的恢复校验器；TypeDecompose复制约束后没有再次平衡预算；多轮脚本忽略COMPACTION_UNSAFE，按每词元四字符截断评分，下一轮却继续传未截断对象，LLM则传截断文本。故96%只作为该报告诊断，不能据此认证安全预算不变量。作用域和分类错误、无法容纳全部约束时的行为，均需单独测试。

表6的LLMLingua-2为0.21/0.08/0.01，消融正文却给0.55/0.18/0.02，未解释设置差异；局限中的19—42%也与主表不合。README把73%误写为稠密检索，论文表8实际对应Sonnet，稠密检索为91%。局部性辅助函数统计有任一覆盖遗漏的约束数，与正文按违规分区描述不同，未重算表7。完整AAC需数据使用协议，本次未尝试受限下载。



下一步：与GateMem的行为门控及MemoryAgentBench的修订任务配对，先修正并测试预算、Unsafe返回和跨轮状态的一致性；在相同保留词元下比较分类标签、固定约束和校验器。分别报告分类召回、真实语义保留、作用域覆盖、合规及合法任务完成，纳入低置信度规则和约束总量超过预算的例子。
<!-- EVIDENCE:limitations:END -->
