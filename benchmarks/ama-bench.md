# AMA-Bench：轨迹问答、工具检索与有限执行验证

<!-- RELEASE-REFERENCE:START -->
> **发布时最佳结果（历史参考）** · 2026-02 · 论文 v1<br>
> **AMA-Agent — Average accuracy: 57.22%**<br>
> 首版摘要报告的 AMA-Agent 平均准确率最佳；属于记忆问答协议，不是环境行动成功率。 [原始来源](https://arxiv.org/html/2602.22769v1)<br>
> 仅供了解当时难度，不代表当前最佳；不同任务、版本和实验条件不能直接混比。
<!-- RELEASE-REFERENCE:END -->

**中文** | [English](ama-bench.en.md)

<!-- EVIDENCE:reading:START -->
## 阅读范围与版本

已核对所述论文版本的方法、实验设置、关键结果与局限；未独立复现实验。

已阅读v4正文第1—7节及附录A—L，包括PDF中的构造、路由、代码提示及WebArena、BabyAI、TextWorld案例；核对跨表差异，未复现实验。

[arXiv 2602.22769v4 (2026-05-27)](https://arxiv.org/html/2602.22769v4)

[补充来源 2602.22769v4，2026-09-30 核对](https://arxiv.org/pdf/2602.22769v4)

页首历史参考原样保留；正文的新版本结果不能代替原始发布成绩。
<!-- EVIDENCE:reading:END -->

<!-- EVIDENCE:method:START -->
## 任务怎样产生记忆需求

基准对行动—观察轨迹提出回忆、因果依赖、状态变化和抽象问题。AMA-Agent是另一个方法：LLM提取状态图，先取top5节点，再按需查邻域或用Python搜索原始轨迹JSON。

定位比较：与LoCoMo、LongMemEval的用户对话不同，AMA-Bench以智能体执行轨迹为记忆来源，增加因果、状态更新和状态抽象问题。v4又加入有限在线执行检查，因此轨迹问答与实际任务结果应并列但分开报告。 这里是评测坐标比较，不表示直接继承了前者的数据。
<!-- EVIDENCE:method:END -->

<!-- EVIDENCE:setup:START -->
## 实验设置与评分对象

表9：六领域、208轨迹/2496QA，平均57,506tokens；合成集1200QA覆盖8K–128K。核心协议一次建记忆，独立回答问题，题间冻结。Qwen3-32B作二元裁判，主方法比较也用该模型回答。LongContext的32,768token窗口预留4K输出，超长时删去中间。
<!-- EVIDENCE:setup:END -->

<!-- EVIDENCE:result-1:START -->
## 固定Qwen3-32B时，四种能力分别怎样变化

准确率为0–1，原表括号是F1，不是误差范围。共用Qwen3-32B，记忆和工具流程不同。

2496个问答：回忆839、因果596、更新647、抽象414；总均值不是四类等权。

| 系统 | 回忆 | 因果推断 | 状态更新 | 状态抽象 | 平均准确率 |
|---|---|---|---|---|---|
| AMA-Agent | 0.6238 | 0.6145 | 0.5305 | 0.4719 | 0.5722 |
| MemoRAG | 0.4708 | 0.5497 | 0.4257 | 0.3659 | 0.4606 |
| EMem | 0.4631 | 0.4925 | 0.4512 | 0.3421 | 0.461 |

定位：v4表5 · [原文](https://arxiv.org/html/2602.22769v4)
<!-- EVIDENCE:result-1:END -->

<!-- EVIDENCE:result-2:START -->
## 删除图或工具，是组合流程干预

准确率为0–1。去图条件改用Qwen3-Embedding-4B上下文索引，去工具条件禁用调用；不能把差值全部归于图的因果语义。

同一轨迹问答套件，改变AMA-Agent内部流程。

| 配置 | 平均准确率 |
|---|---|
| AMA-Agent | 0.57 |
| AMA-Agent without causality graph | 0.43 |
| AMA-Agent without tool retrieval | 0.44 |

定位：v4表7 · [原文](https://arxiv.org/html/2602.22769v4)
<!-- EVIDENCE:result-2:END -->

<!-- EVIDENCE:result-3:START -->
## v4已有有限的在线执行检查

沿用表6，分数为0–100。同一Qwen3-32B执行智能体，但Table19另报TextWorld 50.5%，差异未解释。

表格与附录没有明确给出执行样本数，不能借用2496个离线问答作分母。

| 系统 | TextWorld执行（%） | TextWorld QA（%） | Spider2执行（%） | Spider2 QA（%） |
|---|---|---|---|---|
| AMA-Agent | 51.5 | 40.4 | 26.2 | 57.4 |
| LongContext | 47.5 | 33.0 | 23.5 | 50.9 |

定位：v4表6；与表19的差异见局限 · [原文](https://arxiv.org/html/2602.22769v4)
<!-- EVIDENCE:result-3:END -->

<!-- EVIDENCE:result-4:START -->
## 裁判校准只覆盖一个回答模型

混淆矩阵计数，裁判一致率92.67%；不能代表全部系统和题目。

300个GPT-5.2回答，每领域50个，人工裁决。

| 判定 | 条目数 |
|---|---|
| 真阳性 | 190 |
| 假阳性 | 7 |
| 假阴性 | 15 |
| 真阴性 | 88 |

定位：v4表17 · [原文](https://arxiv.org/html/2602.22769v4)
<!-- EVIDENCE:result-4:END -->

<!-- EVIDENCE:limitations:START -->
## 结论边界与下一步验证

证据支持轨迹QA改进及有限的执行验证。图提取仍是有损语义抽象，代码后备路径可访问原始日志。六个系统间的相关性不能证明单题QA可预测执行。不能据此声称跨任务迁移。

表6的AMA-Agent TextWorld成功率为51.5%，表19却为50.5%，不自行调和。表22的Qwen3-32B AMA分数0.5629也不同于主表0.5722。摘要的11.16个百分点对应MemoRAG，不是表5新增的EMem。EMem/HiMem引用仍有Anonymous/TODO身份缺口。图构造提示接收previous_state_text，不能声称完全独立抽取且绝无历史错误传播。

下一步：匹配原始日志访问、工具调用、嵌入和token预算，对比状态图与同等细节的非图记录。保留执行验证，并增加匹配的未见后续任务来测经验迁移。
<!-- EVIDENCE:limitations:END -->
