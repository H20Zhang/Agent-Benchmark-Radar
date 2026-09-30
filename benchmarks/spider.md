# Spider：让 text-to-SQL 真正泛化到 unseen database schema

<!-- RELEASE-REFERENCE:START -->
> **发布时最佳结果（历史参考）** · 2018-09-24 · 论文 v1<br>
> **SQLNet — Database-split dev exact match: 14.3%**；**SQLNet — Database-split test exact match: 14.7%**<br>
> v1 表 2 的数据库切分结果：开发集 14.3%、测试集 14.7%，均为该表相应切分最佳；摘要只写 14.3%，未说明是开发集。后续版本分开比较。 [原始来源](https://arxiv.org/abs/1809.08887v1)<br>
> 仅供了解当时难度，不代表当前最佳；不同任务、版本和实验条件不能直接混比。
<!-- RELEASE-REFERENCE:END -->

**中文** | [English](spider.en.md) · [首页](../README.md) · [基准库](../library/README.md)

<!-- EVIDENCE:reading:START -->
## 阅读范围与版本

已完整阅读所列主版本的实质正文与附录；未独立复现实验。

完整阅读 v1 与 EMNLP 正式论文的实质内容，以及一页难度标准补充材料。v5 只核对版本信息和表 2，未声称完整阅读 v5。

[arXiv 1809.08887v1 · 2018-09-24](https://arxiv.org/pdf/1809.08887v1) · [正式论文 · EMNLP 2018 · D18-1425](https://aclanthology.org/D18-1425.pdf) · [arXiv 1809.08887v5 · 2019-02-02](https://arxiv.org/pdf/1809.08887v5) · [补充材料 · EMNLP 2018 · D18-1425 · supplement](https://aclanthology.org/attachments/D18-1425.Attachment.zip)
<!-- EVIDENCE:reading:END -->

<!-- EVIDENCE:method:START -->
## 方法与测量对象

Spider 考察未见多表模式上的 SQL 结构生成。SQLNet 使用结构模板解码器，TypeSQL 还使用数据库内容。精确匹配忽略字面值，不能据此证明自主检索取值的能力。

<!-- EDITORIAL-METHOD:START -->
数据由人工围绕关系模式编写问题与 SQL，再改写自然语言，覆盖连接、嵌套、分组及集合运算。按数据库而非随机问题划分，使测试时无法仅复用训练数据库的表名对应。示意流程是：输入问题及“员工—部门”两表模式，识别连接键、分组对象与计数条件，输出 SQL；评测拆分 SELECT、WHERE 等结构组件并检查整条查询。它要求结构与模式对齐，但原版忽略字面值，仍不是完整执行任务。下表的版本差异首先证明必须固定评测口径；单靠这些跨版本结果不能证明解析能力进步。

编辑比较：最接近的前序参照是 WikiSQL 的未见单表 SQL；Spider 将坐标扩展到未见多表结构与复杂组合。它不是首次做未见表测试，也不覆盖 BIRD 后来强调的值／领域证据问题。演化含义是把“会套单表模板”与“能组合新模式上的关系结构”分开。
<!-- EDITORIAL-METHOD:END -->
<!-- EVIDENCE:method:END -->

<!-- EVIDENCE:setup:START -->
## 实验设置

v1 实验加入六个旧数据集，将 206 个数据库按 146/20/40 划分训练、开发和测试集。EMNLP 则采用 130/36/40。实验改造已有解析器，但未规定可对齐的推理 token 预算。
<!-- EVIDENCE:setup:END -->

<!-- EVIDENCE:results:START -->
## 精选定量证据

下表仅核对版本；数值均为查询精确匹配率，不计字面值。数据库数量描述划分，并非查询数分母。

| 系统／比较项 | 数据集／分母 | 指标／单位 | 结果 | 条件 | 来源 |
| --- | --- | --- | --- | --- | --- |
| SQLNet · v1 测试集 | Spider v1；40 个测试数据库 | 精确匹配率（查询数占比，%） | 14.7% | 问题与模式 | v1 表 2, 第 8 页 |
| SQLNet · v1 开发集 | Spider v1；20 个开发数据库 | 精确匹配率（查询数占比，%） | 14.3% | 同一 v1 协议 | v1 表 2, 第 8 页 |
| TypeSQL · EMNLP | Spider EMNLP；40 个测试数据库 | 精确匹配率（查询数占比，%） | 9.7% | 借助内容确定类型；划分改变 | EMNLP 表 2, 第 3918 页 |
| SQLNet · v5 | Spider v5；40 个测试数据库 | 精确匹配率（查询数占比，%） | 12.4% | 修订稿结果；不是初版 | v5 表 2, 第 8 页 |

事实来源：[v1 表 2, 第 8 页; EMNLP 表 2, 第 3918 页; v5 表 2, 第 8 页](https://arxiv.org/pdf/1809.08887v1)

[EMNLP 会议版表 2](https://aclanthology.org/D18-1425.pdf) · [arXiv v5 表 2](https://arxiv.org/pdf/1809.08887v5)
<!-- EVIDENCE:results:END -->

<!-- EVIDENCE:limitations:START -->
## 局限与解释边界

页首采用 v1：SQLNet 在开发集为 14.3%、测试集为 14.7%；正文同时列出 EMNLP 和 v5 仅用于版本核对。v5 的 12.4% 不能回填为初版成绩，跨版本表也不是进展排名。规范化模式名称、排除含糊及外部知识问题，限制了企业场景外推。

<!-- EDITORIAL-NEXT:START -->
下一步固定同一版本和问题集，分别提供正确模式链接、正确字面值及两者；同时报告结构匹配与多数据库实例上的执行一致性。这样才能区分模式链接、组合解码和偶然结果相等，而不是把换版本后的差分算作进展。
<!-- EDITORIAL-NEXT:END -->
<!-- EVIDENCE:limitations:END -->
