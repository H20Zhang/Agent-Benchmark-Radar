# MEMPROBE / MemAudit：任务做完后，记忆里究竟留下了什么

<!-- RELEASE-REFERENCE:START -->
> **发布时最佳结果（待核验）** · 基准记录日期：2026-06-23<br>
> 尚未核验原始发布版本中可定位到模型、指标和协议的最佳成绩。 [原始来源](https://arxiv.org/abs/2606.24595)<br>
> 不以最新榜单、单条基线或后续论文成绩代替；未知不代表零分或原作者未报告。
<!-- RELEASE-REFERENCE:END -->

**中文** | [English](memprobe.en.md) · [主入口](../README.md) · [基准资料库](../library/README.md)

<!-- EVIDENCE:reading:START -->
## 阅读范围与版本

已核对所述主论文版本的方法、设置、关键结果与局限；未独立复现实验。

论文v2主文与附录A—K，包含PDF提示及案例；另核对官方复现指南和结果说明。

[arXiv:2606.24595v2](https://arxiv.org/html/2606.24595v2) · [main@2026-09-30](https://github.com/sora1998/MEMAUDIT-bench/blob/main/docs/reproduction.md) · [main@2026-09-30](https://github.com/sora1998/MEMAUDIT-bench)

下列表格重新组织了有来源的选定事实。页首历史参考与正文采用的版本、切分和模型可能不同，不能跨表混合成绩。
<!-- EVIDENCE:reading:END -->

<!-- EVIDENCE:method:START -->
## 测量对象、方法与比较

MEMPROBE 是六月基准名称，论文在九月v2改名为 MemAudit；它与另一篇九月 MemProbe 稳定性—可塑性论文不是同一身份。交互先让智能体帮助一个模拟用户完成普通任务，随后冻结留下的最终记忆，再用两种访问方式恢复用户的隐藏结构化状态：完整存储读取，或每个目标检索前5条。这样把“当时任务做得如何”和“后来能从记忆恢复什么”分开。

[原文](https://arxiv.org/html/2606.24595v2)
<!-- EVIDENCE:method:END -->

<!-- EVIDENCE:setup:START -->
## 实验设置与分母

50名模拟用户，每人31个目标，共1,550个目标；交互上限25轮，重建读取和评判使用GPT-5.4-mini。恢复指标B先对各类目标求平均，再对5类等权平均；不是全部目标直接合并的二元准确率。表中SD是用户间标准差，不是置信区间。官方发表的Mem-T条件为memt_memonly：Mem-T-4B处理记忆，最终回答仍由共同骨干模型给出。

[设置来源](https://arxiv.org/html/2606.24595v2)
<!-- EVIDENCE:setup:END -->

<!-- EVIDENCE:result-1:START -->
## 同一最终存储，不同访问方式

论文v2表2，50用户×31目标；五类等权恢复分数，同一轨迹结束后的同一存储分别完整读取与前5条读取。

| 系统 | 完整存储B（0–1） | 完整存储SD | 前5条B（0–1） | 前5条SD |
|---|---|---|---|---|
| amem | 0.611 | 0.062 | 0.54 | 0.062 |
| longctx_full | 0.624 | 0.067 | 0.503 | 0.075 |
| mem0 | 0.613 | 0.06 | 0.473 | 0.079 |

完整读取和检索读取都可能失分，但不能把全部差距等同于存储删除：表示形式、读出、查询和截断都参与。longctx_full存的是原始对话，仍不是完美恢复。

事实来源：v2 表 2 · [原文](https://arxiv.org/html/2606.24595v2)
<!-- EVIDENCE:result-1:END -->

<!-- EVIDENCE:result-2:START -->
## 即时任务完成与持久恢复不是同一个指标

v2表2的无记忆对照；完成率和类别平衡恢复分数有不同测量对象与汇总，不能互换。

| 配置 | 任务完成率（%） | 完整存储B（0–1） |
|---|---|---|
| nomem | 99.935 | 0.0 |

这是一条诊断证据：普通协助接近完成，并不意味着记住了用户状态。未报告的无记忆前5条结果不能填成零。

事实来源：v2 表 2 · [原文](https://arxiv.org/html/2606.24595v2)
<!-- EVIDENCE:result-2:END -->

<!-- EVIDENCE:limitations:START -->
## 结论边界、缺口与下一步

恢复分数是按细则重建用户状态，不是对纯存储保真的直接测量；模拟用户、可披露属性筛选与分叉交互轨迹限制泛化和因果归因。Mem-T完整读取有上下文溢出，不能据此给它排“记忆最差”；论文v2报0.130±0.251，官方README报0.131±0.251，来源差异未解决。Mem-T还可用最多6步ReAct搜索，不是相同的单次近邻读取。官方说明当前main模拟器不同于paper-v1归档，不能把新的main运行叫做原实验重放。相比下游成功率，它补的是记忆产物审计；下一步固定轨迹、存储和读取预算，再同时观察恢复与后续个性化效用。页首首版历史参考与本节v2结果保持分开。

[原始证据](https://arxiv.org/html/2606.24595v2)
<!-- EVIDENCE:limitations:END -->

<!-- RESEARCH-DECISION:START -->

上述方法、对照与局限一起决定何时适合使用这个基准；表格不构成跨协议排行榜，结构校验也不证明事实正确或完成复现。

相关测量与对照：[LoCoMo](locomo.md) · [LongMemEval](longmemeval.md) · [MemProbe (stability–plasticity)](memprobe-stability-plasticity.md)

<!-- RESEARCH-DECISION:END -->
