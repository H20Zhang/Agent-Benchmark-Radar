# Spider 2.0：企业数据库中的交互式工作流

<!-- RELEASE-REFERENCE:START -->
> **发布时结果（历史参考，非最佳声明）** · 2024-11-12 · 论文 v1<br>
> **o1-preview + paper code-agent framework — Task success: 17.0%**<br>
> 首版摘要中的代码智能体结果，对应原版任务集合；不与后来的 Lite、Snow 或修改后的任务集混比。 [原始来源](https://arxiv.org/abs/2411.07763v1)<br>
> 仅供了解当时难度，不代表当前最佳；不同任务、版本和实验条件不能直接混比。
<!-- RELEASE-REFERENCE:END -->

**中文** | [English](spider-2.en.md) · [首页](../README.md) · [基准库](../library/README.md)

<!-- EVIDENCE:reading:START -->
## 阅读范围与版本

已完整阅读所列主版本的实质正文与附录；未独立复现实验。

完整阅读 45 页 v1，包括附录 A、B.1–B.8、C.1–C.6 中的评测、标注、数据库、文档、框架、成本、案例与提示词。

[arXiv 2411.07763v1 · 2024-11-12](https://arxiv.org/pdf/2411.07763v1)
<!-- EVIDENCE:reading:END -->

<!-- EVIDENCE:method:START -->
## 方法与测量对象

Spider 2.0 结合代码、文档与执行反馈评测数据库工作流。Lite 是另一条 SQL 输出赛道。评测器检查任务指定的输出部分，并非统一比较整张结果表。

<!-- EDITORIAL-METHOD:START -->
任务将自然语言请求放入带数据库、文档和项目文件的工作区。代理需要查模式与方言说明、检查数据值、编辑 SQL 或项目代码、运行并据错误调整，最终提交指定产物；Lite 则只要求 SQL。示意流程是阅读指标定义、定位多个表的连接键、编写查询并修正方言错误，再输出所需结果文件。标注的参考流程让“会生成一条 SQL”与“能发现完成任务所需上下文”分开，指定输出检查仍可能忽略未覆盖的副作用或多余内容。

编辑比较：这是对 Spider／BIRD 静态问题加模式输入的一次工作流扩展，新增文档利用、项目定位和执行反馈。不同轨道与老基准的分数不能组成同模型难度曲线；该坐标变化本身比一个跨协议总分更重要。
<!-- EDITORIAL-METHOD:END -->
<!-- EVIDENCE:method:END -->

<!-- EVIDENCE:setup:START -->
## 实验设置

原始 agent 赛道报告 632 题，Lite 为 547 题。Agent 提示要求约 30 步，连续三次重复结果或单动作超过 120 秒时终止。Lite 使用温度 0 和 128K 上下文，省略 BigQuery 取值链接。
<!-- EVIDENCE:setup:END -->

<!-- EVIDENCE:results:START -->
## 精选定量证据

v1；只作赛道内比较。SR 是指定输出的任务成功率，Lite EX 是指定执行结果的一致率。参考计划属于额外提供的特权输入。

| 系统／比较项 | 数据集／分母 | 指标／单位 | 结果 | 条件 | 来源 |
| --- | --- | --- | --- | --- | --- |
| Spider-Agent + o1-preview | 原始赛道；报告为 632 题 | SR（%；计数分母不自洽） | 17.01% | 代码、文档与工具；温度设置冲突 | 表 4, 第 7 页; C.1, 第 35 页 |
| Spider-Agent + GPT-4o | 原始赛道；报告为 632 题 | SR（%） | 10.13% | 同名框架 | 表 4, 第 7 页 |
| DAIL-SQL + GPT-4o | Spider2.0-lite；547 题 | EX（%） | 5.68% | T=0；采样值与文档；无参考计划 | 表 5/10, 第 7/9 页 |
| DAIL-SQL + GPT-4o + 参考计划 | Spider2.0-lite；547 题 | EX（%） | 8.78% | T=0；人工参考计划 | 表 10, 第 9 页 |

事实来源：[表 4, 第 7 页; C.1, 第 35 页; 表 4, 第 7 页; 表 5/10, 第 7/9 页; 表 10, 第 9 页](https://arxiv.org/pdf/2411.07763v1)
<!-- EVIDENCE:results:END -->

<!-- EVIDENCE:limitations:START -->
## 局限与解释边界

91.2/73.0/17.0 将先前 GPT-4 方法与 Spider-Agent+o1-preview 并列，不是匹配迁移实验。表 4 的 17.01% 与结论的 18.8% 冲突，也不能在 632 题上还原一致的整数成功数。正文温度 0 与 agent 附录 C.1 的 1.0、top-p 0.9 同样冲突，应保留这些未解决差异。

<!-- EDITORIAL-NEXT:START -->
下一步在同一代理轨道固定模型与预算，依次提供正确文件、相关文档或参考计划，记录发现、执行和产物错误。参考计划带来增益的替代解释是直接泄露任务分解，而非可迁移规划能力。
<!-- EDITORIAL-NEXT:END -->
<!-- EVIDENCE:limitations:END -->
