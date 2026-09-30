# Agent Memory Bench：编码检索收益、接入检查与历史污染

<!-- RELEASE-REFERENCE:START -->
> **发布时最佳结果（待核验）** · 基准记录日期：2026-08-22<br>
> 尚未核验原始发布版本中可定位到模型、指标和协议的最佳成绩。 [原始来源](https://github.com/GiulioDER/agent-memory-bench)<br>
> 不以最新榜单、单条基线或后续论文成绩代替；未知不代表零分或原作者未报告。
<!-- RELEASE-REFERENCE:END -->

**中文** | [English](agent-memory-bench-coding.en.md)

<!-- EVIDENCE:reading:START -->
## 阅读范围与版本

已阅读固定版本的官方协议、设置、结果记录与局限；未独立复现实验。

已完整阅读固定提交的README、方法页、状态文档、复现指南、预登记000/026、pilot-001分析、official-003摘要/分析/审计；定点检查配对统计与榜单加载代码。没有论文全文可通读，证据来自官方协议和记录；未执行项目代码或付费模型实验，未全面重审后来加入的厂商运行。

[官方协议，固定版本 695dd26a6732174a59386fa28aa844ad31d31a48](https://github.com/GiulioDER/agent-memory-bench/blob/695dd26a6732174a59386fa28aa844ad31d31a48/docs/STATUS.md)

[官方来源，固定版本 695dd26a6732174a59386fa28aa844ad31d31a48](https://github.com/GiulioDER/agent-memory-bench/blob/695dd26a6732174a59386fa28aa844ad31d31a48/README.md)

[官方来源，固定版本 695dd26a6732174a59386fa28aa844ad31d31a48](https://github.com/GiulioDER/agent-memory-bench/blob/695dd26a6732174a59386fa28aa844ad31d31a48/site/method.html)

[官方来源，固定版本 695dd26a6732174a59386fa28aa844ad31d31a48](https://github.com/GiulioDER/agent-memory-bench/blob/695dd26a6732174a59386fa28aa844ad31d31a48/docs/REPLICATION.md)

[官方来源，固定版本 695dd26a6732174a59386fa28aa844ad31d31a48](https://github.com/GiulioDER/agent-memory-bench/blob/695dd26a6732174a59386fa28aa844ad31d31a48/preregistration/000-pilot.md)

[官方来源，固定版本 695dd26a6732174a59386fa28aa844ad31d31a48](https://github.com/GiulioDER/agent-memory-bench/blob/695dd26a6732174a59386fa28aa844ad31d31a48/preregistration/026-official-003-fair-instruction.md)

[官方来源，固定版本 695dd26a6732174a59386fa28aa844ad31d31a48](https://github.com/GiulioDER/agent-memory-bench/blob/695dd26a6732174a59386fa28aa844ad31d31a48/results/pilot-001/analysis.json)

[官方来源，固定版本 695dd26a6732174a59386fa28aa844ad31d31a48](https://github.com/GiulioDER/agent-memory-bench/blob/695dd26a6732174a59386fa28aa844ad31d31a48/results/official-003/leaderboard_summary.json)

[官方来源，固定版本 695dd26a6732174a59386fa28aa844ad31d31a48](https://github.com/GiulioDER/agent-memory-bench/blob/695dd26a6732174a59386fa28aa844ad31d31a48/reports/official-003-analysis.md)

[官方来源，固定版本 695dd26a6732174a59386fa28aa844ad31d31a48](https://github.com/GiulioDER/agent-memory-bench/blob/695dd26a6732174a59386fa28aa844ad31d31a48/reports/official-003-audit.md)

页首历史参考原样保留；正文的新版本结果不能代替原始发布成绩。
<!-- EVIDENCE:reading:END -->

<!-- EVIDENCE:method:START -->
## 任务怎样产生记忆需求

给各记忆配置相同的逐字会话语料，在隔离仓库中执行相同任务、种子和环境。智能体产出代码后，由沙箱外隐藏输入的可执行检查器判通过/失败，不使用LLM裁判。接入检查验证工具已列出、钩子触发、文件摘要和配置隔离，不能单独证明智能体真的检索并使用记忆。比如时区任务要求遵循只写在旧会话里的约定；原始记录加grep、无记忆、静态说明和无信息占位文本均为对照。

定位比较：与一般记忆问答相比，这个官方协议把记忆接到编码任务的通过/失败结果，并安排空白、安慰剂、项目说明和检索记忆实验臂。它测预填语料的检索效用；没有观察长期记忆形成，且泄漏审计限制旧成绩的解释。 这里是评测坐标比较，不表示直接继承了前者的数据。
<!-- EVIDENCE:method:END -->

<!-- EVIDENCE:setup:START -->
## 实验设置与评分对象

当前套件34个可执行任务，official-003只用26个任务：73个任务—条件组合×5种子×8配置，共2920次会话；365个计划配对单元中317个通过接入检查、48个剔除，每单元每配置只运行一次。模型为deepseek/deepseek-v4-flash，经Claude Code。五条件为证据存在、缺失、被新事实取代、无日期冲突、属于相邻子系统。每条件约4900篇文档预先摄入，运行期间不写入记忆，因此测检索而非完整写入/巩固生命周期。
<!-- EVIDENCE:setup:END -->

<!-- EVIDENCE:result-1:START -->
## 主运行：正向点估计尚未排除零效应

比例与绝对差均为0–1；基线的[0,0]只是自比较，不是成功率置信区间。其余为原样报告的差值区间，均跨零；存在已披露的标签暴露。

26个任务、317个通过接入检查的任务/种子/条件配对单元；区间不含整次运行之间的波动。

| 配置 | 成功率 | 相对claude_md差值 | 95%区间下界 | 95%区间上界 |
|---|---|---|---|---|
| claude_md | 0.5773 | 0 | 0 | 0 |
| recall | 0.6593 | 0.082 | -0.0063 | 0.1808 |
| bare | 0.6593 | 0.082 | -0.0195 | 0.1963 |
| placebo | 0.6719 | 0.0946 | -0.0369 | 0.2493 |

定位：official-003结果汇总：部分实验臂 · [原文](https://github.com/GiulioDER/agent-memory-bench/blob/695dd26a6732174a59386fa28aa844ad31d31a48/results/official-003/leaderboard_summary.json)
<!-- EVIDENCE:result-1:END -->

<!-- EVIDENCE:result-2:START -->
## 旧先导的全部任务和筛选子集不能混用

旧先导实验，差值为按任务平均的recall−claude_md；95%区间按任务聚类重采样，不含整次运行波动。两种范围McNemar p均为1.0。不可与official-003作直接进步对比。

旧先导计划24题×3种子=72单元，实际71个接入有效；13个筛选后任务保留38单元。

| 分析范围 | 任务数 | 配对单元数 | recall差值 | 95%下界 | 95%上界 |
|---|---|---|---|---|---|
| 全部任务 | 24 | 71 | 0.0139 | -0.0278 | 0.0556 |
| 按难度筛选后任务 | 13 | 38 | 0.0256 | 0 | 0.0769 |

定位：pilot-001分析：全任务与筛选子集分开 · [原文](https://github.com/GiulioDER/agent-memory-bench/blob/695dd26a6732174a59386fa28aa844ad31d31a48/results/pilot-001/analysis.json)
<!-- EVIDENCE:result-2:END -->

<!-- EVIDENCE:result-3:START -->
## 同一配置在不同证据条件下表现不同

执行检查器二元通过数；不同条件难度和样本集合不同，不能用两行差异估计条件的纯因果效应。

分母为各条件通过接入检查的配对单元。

| 条件 | 配对单元 | recall通过数 | claude_md通过数 |
|---|---|---|---|
| present | 111 | 56 | 43 |
| contradictory | 51 | 37 | 39 |

定位：official-003汇总：部分条件计数 · [原文](https://github.com/GiulioDER/agent-memory-bench/blob/695dd26a6732174a59386fa28aa844ad31d31a48/results/official-003/leaderboard_summary.json)
<!-- EVIDENCE:result-3:END -->

<!-- EVIDENCE:limitations:START -->
## 结论边界与下一步验证

不能把该结果描述为干净的记忆产品因果排名。official-003在运行开始后才登记协议，且没有提前公告；9月26日审计发现文档名暴露stale_/rival_角色，工作目录/命名空间也暴露条件名。修复没有消除旧成绩的污染，需要重新运行。配对接入剔除会改变样本集合，预算也未匹配。检查器拒绝朴素参考解并不证明基础模型不可能另找正确解。Recall由基准作者开发，需披露。无正向显著差异不等于记忆无用；先导13个保留任务也不能替代全24题估计。

旧笔记把13个筛选后任务和全部24题的0.0139差值混在一起；本页分别列出。接入可用不等于实际使用。源码与语料在旧运行之后多次修复，当前工具验证通过也不证明旧实验无混杂。稍后的厂商运行使用不同的交集样本，还存在各自适配器和协议偏离，本页不把它们并入317单元主表。



下一步：用不泄露条件或文档角色的命名重新冻结语料，提前登记统计与剔除规则，并同时报告全部分配样本和通过接入样本。区分接入可用、搜索发生、证据到达和最终执行成功；匹配完整成本，重复整个运行，再单独加入跨会话写入/更新任务。
<!-- EVIDENCE:limitations:END -->
