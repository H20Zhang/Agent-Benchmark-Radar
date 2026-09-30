# membench：当前事实命中与旧事实污染的权衡

<!-- RELEASE-REFERENCE:START -->
> **发布时最佳结果（待核验）** · 基准记录日期：2026-08-22<br>
> 尚未核验原始发布版本中可定位到模型、指标和协议的最佳成绩。 [原始来源](https://github.com/Ps23102004/membench)<br>
> 不以最新榜单、单条基线或后续论文成绩代替；未知不代表零分或原作者未报告。
<!-- RELEASE-REFERENCE:END -->

**中文** | [English](membench-staleness.en.md)

<!-- EVIDENCE:reading:START -->
## 阅读范围与版本

已阅读固定版本的官方协议、设置、结果记录与局限；未独立复现实验。

完整阅读固定提交README、运行器、评分器、聚合指标和recency后端；检查时间范围场景及完整冻结榜单JSON。未执行后端或逐项审计所有场景和适配器。

[固定版本 eff49d990416](https://github.com/Ps23102004/membench/blob/eff49d9904164a0bc3e4e5f6c261bffe4ff8663b/README.md)

[辅助材料（2026-09-30查阅）](https://github.com/Ps23102004/membench/blob/eff49d9904164a0bc3e4e5f6c261bffe4ff8663b/membench/runner.py)

[辅助材料（2026-09-30查阅）](https://github.com/Ps23102004/membench/blob/eff49d9904164a0bc3e4e5f6c261bffe4ff8663b/membench/grader.py)

[辅助材料（2026-09-30查阅）](https://github.com/Ps23102004/membench/blob/eff49d9904164a0bc3e4e5f6c261bffe4ff8663b/membench/metrics.py)

[辅助材料（2026-09-30查阅）](https://github.com/Ps23102004/membench/blob/eff49d9904164a0bc3e4e5f6c261bffe4ff8663b/membench/backends/recency_backend.py)

[辅助材料（2026-09-30查阅）](https://github.com/Ps23102004/membench/blob/eff49d9904164a0bc3e4e5f6c261bffe4ff8663b/results/leaderboard-2026-08-22.json)

[辅助材料（2026-09-30查阅）](https://github.com/Ps23102004/membench/blob/eff49d9904164a0bc3e4e5f6c261bffe4ff8663b/scenarios/temporal_scoping.json)

页首历史参考原样保留；正文的新版本结果不能代替原始发布成绩。
<!-- EVIDENCE:reading:END -->

<!-- EVIDENCE:method:START -->
## 任务怎样产生记忆需求

membench将每套手写多会话故事按时间写入小型记忆库，在不同阶段查询；每套开始清空，后续信息不会提前可见。查询只要求返回已存文本，没有回答模型。预期子串在前k出现算命中；禁用子串排第一算staleness@1，出现在任意返回位置则算leak_rate@k。它能揭示“新旧都取回，因此召回很高”的假象。

谱系：这是一套独立的更新语义单元测试，没有继承LongMemEval数据。与其知识更新QA相比，这里把评分停在文本排名，分开首位旧事实、剩余位置污染和当前事实缺失。它与StateMemBench可作跨尺度对照，但不能互换总体分数。
理解评分的示意：旧记录说项目联系人是A，后续更新为B；返回列表包含B就可能命中，但A若仍排第一则同时记为旧事实污染。高召回因此可以与错误优先级并存。
<!-- EVIDENCE:method:END -->

<!-- EVIDENCE:setup:START -->
## 实验设置与评分对象

五套各12探针：替代、否定、实体混淆、时间范围、干扰负载，共60；每库约12—52事实，k=5。冻结2026-08-22记录使用Ollama 0.32.15、nomic-embed-text:latest，摘要0a109f422b47。embed纯余弦，recency先取max(3k,10)=15语义候选再按时间排序，grep按关键词重叠并以新近性打破平局。默认写入元数据仅时间戳与会话ID，手写实体/主题答案标签被剥离。空返回使召回为0，并从staleness/leak分母排除，单列弃答率；所以要同时看三项。
<!-- EVIDENCE:setup:END -->

<!-- EVIDENCE:result-1:START -->
## 少旧事实可能伴随更多正确事实缺失

命中和旧事实可以同题同时发生；所有后端弃答率0，因此本次stale分母均为60。区间为Wilson二项式区间，但探针共享故事、不是独立样本，实际泛化不确定性可能更大。词元为字符数除4的近似，不是实际tokenizer计费。

每后端60探针、每套12，所有后端弃答为0；计数与冻结取整比例对应。

| 后端 | 命中数/60 | stale首位数/60 | staleness@1的95%区间 | Leak@5 | 平均近似词元 |
|---|---|---|---|---|---|
| embed | 59 | 28 | 0.346–0.591 | 1 | 70.3 |
| grep | 56 | 24 | 0.286–0.526 | 0.95 | 67.8 |
| recency | 45 | 3 | 0.017–0.137 | 0.167 | 73.9 |

定位：冻结榜单：全量结果 · [原文](https://github.com/Ps23102004/membench/blob/eff49d9904164a0bc3e4e5f6c261bffe4ff8663b/README.md)
<!-- EVIDENCE:result-1:END -->

<!-- EVIDENCE:result-2:START -->
## 替代子集与全部题目分别报告

只看替代子集，不能把11/12推广到全部60探针。新事实优先要求新值出现且排在旧值前，或新值出现而旧值不出现；仅删除旧值并不能得分。

12道替代探针；只在声明supersedes的题上计算新事实优先率。

| 后端 | 命中数/12 | stale首位数/12 | 前五旧事实泄漏率 | 新事实优先率 |
|---|---|---|---|---|
| embed | 11 | 11 | 1 | 0 |
| grep | 10 | 5 | 0.833 | 0.333 |
| recency | 10 | 0 | 0 | 0.833 |

定位：冻结榜单：替代子集 · [原文](https://github.com/Ps23102004/membench/blob/eff49d9904164a0bc3e4e5f6c261bffe4ff8663b/README.md)
<!-- EVIDENCE:result-2:END -->

<!-- EVIDENCE:result-3:START -->
## 降低污染不是对所有问题单调有益

0—1比例。实体精确匹配可占首位但相似实体仍污染其余位置；新近性在干扰子集反而使首位错误从0升至25%。

每行12探针，无弃答。

| 子集与后端 | Recall@5 | staleness@1 | Leak@5 |
|---|---|---|---|
| 实体混淆／embed | 1 | 0 | 1 |
| 实体混淆／recency | 0.667 | 0 | 0.333 |
| 干扰负载／embed | 1 | 0 | 1 |
| 干扰负载／recency | 0.583 | 0.25 | 0.5 |

定位：冻结榜单：其他子集的权衡 · [原文](https://github.com/Ps23102004/membench/blob/eff49d9904164a0bc3e4e5f6c261bffe4ff8663b/README.md)
<!-- EVIDENCE:result-3:END -->

<!-- EVIDENCE:limitations:START -->
## 结论边界与下一步验证

这支持新近性与召回存在权衡，不能称recency已经解决更新问题。staleness包括旧值、错误实体和过期值，名称不能替代具体错误类型。时间范围和复杂会话例子已经存在，下一步应扩展其规模与组合难度。确切子串评分可能错判同义回答，也可能把包含正确词与错误语境的文本算命中。没有测真实下游答案、行动、检索时延或长期扩展性。

不能把staleness@1视为所有后端都与k无关，recency的候选池随k变化。README描述三个embed子集首位几乎不旧，但表中只有实体和干扰为0，时间范围为0.5。子串分数也可能假阳性，不能一概称推理系统真实能力的下界。



下一步：与LongMemEval或StateMemBench配对，保留当前60探针作回归集，另外建立按故事留出的自然改写、多步替代与更多干扰项；固定语义候选池再改变返回k，以隔离recency候选变化。报告无答案任务的正确弃答与可答任务召回，增加语义人工审核和下游回答。
<!-- EVIDENCE:limitations:END -->
