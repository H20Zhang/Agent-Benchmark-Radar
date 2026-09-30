# MemProbe：区分有效更新与抗干扰保留

<!-- RELEASE-REFERENCE:START -->
> **发布时结果（历史参考，非最佳声明）** · 2026-09-24 · 论文首版<br>
> **A-MEM (Gemini-3-Flash-preview reader) — Overall probe accuracy: 88.4%**<br>
> 主套件 56 情节、224 探针；A-MEM 适配配置，Gemini-3-Flash-preview 最终阅读器。选录历史结果，不声明跨系统最佳。 [原始来源](https://arxiv.org/abs/2609.30558v1)<br>
> 不同适配器的检索预算、摄入失败和元数据访问并未统一；此结果不证明架构的因果优势，也不代表当前排行榜。
<!-- RELEASE-REFERENCE:END -->

**中文** | [English](memprobe-stability-plasticity.en.md) · [主入口](../README.md) · [基准资料库](../library/README.md)

[论文首版](https://arxiv.org/abs/2609.30558v1) · [全文](https://arxiv.org/html/2609.30558v1) · [代码与数据](https://github.com/jq-ding/MemProbe) · [固定版本实现说明](https://github.com/jq-ding/MemProbe/blob/9068d8d9a2a47268fe6f7601b99a56a283c37be5/IMPLEMENTATION_DETAILS.md)

## 身份与测量对象

这里收录的是 Jiaqi Ding、Guorong Wu 的 *Probing Stability-Plasticity Tradeoffs in Agent Memory through Cognitive Experimental Paradigms*，于 2026 年 9 月 24 日首次提交。它与 Ma 等人的 6 月研究 [MEMPROBE / MemAudit](memprobe.md) 不同；后者从最终记忆产物恢复隐藏用户状态。同名不能作为合并身份或版本谱系的依据。

可复用贡献是范式说明与评分协议，并以受控诊断套件实例化：记忆是否接受有效更新、抵抗不可靠证据对已有事实的覆盖，并保留历史、来源和时间顺序？主套件包含 56 个情节、1,246 个会话、224 个探针；干扰、误导、巩固和再巩固四种范式各有 14 个情节。内容为英文文本中的合成或改编个人、工作及工具状态事实。这些受控情节不代表真实系统运行多年的观察。参见[附录 B 表 8](https://arxiv.org/html/2609.30558v1)。

## 相比前身多测了什么

LongMemEval 和 MemoryAgentBench 已覆盖更新、时间行为及遗忘。这个版本通过可复用范式说明和类型化探针，把更新、抗干扰保留及来源追溯分别诊断。它与 MemoryArena 的闭环行动效用互补。一篇论文增加诊断坐标，只能构成早期信号，不足以据此重写稳定的领域地图。

## 评测协议与公平比较

每个情节使用全新的记忆存储，按顺序摄入会话，再由共同的 Gemini-3-Flash-preview 最终阅读器回答探针。报告设置中的记忆内部模型调用使用 Gemini-2.5-Flash。类型化字段评分分别得到总体探针准确率、可塑性／更新准确率、稳定性／保留准确率、二者的调和均值，以及历史、来源和时间保真度。公开分析以情节为单位进行 2,000 次自助重采样。参见[第 4.1—4.2 节及附录 C](https://arxiv.org/html/2609.30558v1)。

统一最终阅读器并没有统一上游流程。实现说明中，Mem0 和 LangMem 提交全部最终事实，Graphiti 提交前 15 条关系事实，Cognee 提交前 15 项图上下文，A-MEM 提交前 15 条笔记，Naive RAG 和 Time-aware RAG 使用前 5 项关键词检索证据；各系统的嵌入和补丁也不同。Graphiti 约 1,100 次会话添加中，约 178 次因 JSON 格式错误被跳过。A-MEM 还把会话类型作为标签／类别，这需要审计潜在的元数据优势，但不能直接断言发生了信息泄漏。即使检索条数相同，证据量和词元预算也未必相同。参见[固定版本适配说明](https://github.com/jq-ding/MemProbe/blob/9068d8d9a2a47268fe6f7601b99a56a283c37be5/IMPLEMENTATION_DETAILS.md)。

## 决定性证据与成绩边界

表 1 报告，主阅读器设置下 A-MEM 的总体探针准确率为 88.4%，完整上下文参考为 88.8%，Oracle 为 93.3%。它们是特定配置的报告结果，不代表当前排行榜或普适上限。表 2 中 A-MEM 的可塑性为 91.1%、稳定性为 85.7%、调和均值为 88.3%；Cognee 则表现为较低可塑性与较高稳定性的取舍。更换阅读器会改变绝对分数和部分顺序。参见[表 1—2](https://arxiv.org/html/2609.30558v1)。

[结构化来源记录](../data/results/memprobe-stability-plasticity.json) 为每个适配配置保留独立的单项轨道，不据此排出跨适配器冠军。日期指论文首版报告日期，实验执行日期尚未确认。[固定版本自助分析文件](https://github.com/jq-ding/MemProbe/blob/9068d8d9a2a47268fe6f7601b99a56a283c37be5/results/suite56/analysis/bootstrap_ci.json) 保留更精细的原始数值。本次未独立复现实验。

## 最强混杂因素与未覆盖缺口

探针失败可能来自摄入、存储、检索或答案理解。检索上下文中没有某条证据，并不证明存储中也没有。Oracle 同时提供正确证据并移除干扰，因此不能据其增益单独定位某个环节的因果贡献。范式轴之间的相关性和较小的合成套件也限制因果归因。

另一个 40 情节套件同时更换生成器、阅读器、情节长度与事实分布；不能与主套件合并评分，也不能视为单因素复现。主代码和主套件采用 MIT 许可，suite40 及衍生输出采用 CC BY-NC 4.0。开放世界行动质量、持续运行成本和多语言泛化仍未覆盖。

<!-- RESEARCH-DECISION:START -->

## 研究决策卡

### 什么时候用它

在把记忆总分解释为可信状态管理能力之前，用它区分有效更新、不当覆盖和来源保留的失败。

### 一个具体任务是什么样

示意任务：用户明确修改工作偏好，后续会话又给出一条不确定的相反回忆。系统应接受有效更新，避免较弱陈述覆盖新状态，并保留变更来源。

### 最有区分力的下一步实验

固定摄入成功率、嵌入、阅读器、证据／词元预算和元数据访问，分别比较直接提供正确证据、检索证据、直接审计存储三种设置。按探针类型报告更新与保留错误，同时报告摄入失败和自助区间，再讨论架构差异。

### 搭配哪些基准

[LongMemEval](longmemeval.md) · [MemoryAgentBench](memoryagentbench.md) · [StateMemBench](statemembench.md) · [MEMPROBE / MemAudit](memprobe.md) · [MemoryArena](memoryarena.md)

<!-- RESEARCH-DECISION:END -->

证据核验日期：2026-09-30。本次阅读了原始论文及固定版本的公开实现、结果资料；结构校验不等于事实认证或独立复现。
