# RetailBridge

<!-- RELEASE-REFERENCE:START -->
> **发布时最佳结果（待核验）** · 基准记录日期：2026-10-18<br>
> 尚未核验原始发布版本中可定位到模型、指标和协议的最佳成绩。 [原始来源](https://arxiv.org/abs/2610.25096v1)<br>
> 不以最新榜单、单条基线或后续论文成绩代替；未知不代表零分或原作者未报告。
<!-- RELEASE-REFERENCE:END -->

**中文** · [English](retailbridge.en.md) · [基准库](../library/README.md)

<!-- EVIDENCE:reading:START -->
## 阅读范围
已阅读原文构造方法、评测、基线设置及评审审计部分，并核对官方仓库说明与文件清单；未复现实验，也未独立检查图表像素。
[arXiv:2610.25096v1](https://arxiv.org/html/2610.25096v1)
<!-- EVIDENCE:reading:END -->

<!-- EVIDENCE:method:START -->
## 测量对象与构造方法
RetailBridge要求代理连接证据，而非从单篇文档直接作答。角色驱动的零售模拟生成五张表和三类文本。原子问题通过共享实体或中间答案组合，例如先找某位买家的最大订单，再定位相应评论解释。构造记录保留参考答案背后的SQL或检索链。共1,680题，三个生成模型各贡献相同题量，并分别标注深度、来源和模态。配套方法RetailRAG不是基准名称：它先概述模式，再进行按来源组织的计划和局部修复。
<!-- EVIDENCE:method:END -->

<!-- EVIDENCE:setup:START -->
## 协议与公平比较
主框架比较固定GPT-oss-120B、Qwen3-Embedding-8B与Qwen3.6-Plus，分别作为基础模型、嵌入模型和语义评审。表格使用SQLite，文本使用稠密索引，统一采用top-10检索。Acc是字符串包含判定，语义评审判断等价性，两者不能当作同一种精确正确率。各基线的控制流程和专属设置仍不同。官方仓库包含评测数据、RetailRAG、脚本与evaluate.py；可获得不代表本次已经运行。
<!-- EVIDENCE:setup:END -->

<!-- EVIDENCE:result-1:START -->
## 主要证据
表2：共享GPT-oss-120B基础模型，全部1,680题；平均字符串包含准确率、语义评审准确率与每题API调用次数。

| 设置 | 包含准确率 | 评审准确率 | API调用/题 |
|---|---|---|---|
| RetailRAG | 0.298 | 0.429 | 7.45 |
| HetaRAG | 0.149 | 0.293 | 25.21 |

这组比较支持所测整套框架的结果更好，不支持检索策略的普遍排名。较高的评审分数不能替换包含准确率。API调用较少也不意味着成本按比例下降，因为每次调用的提示长度、输出token、缓存与服务延迟均可能不同。
[arXiv:2610.25096v1](https://arxiv.org/html/2610.25096v1)
<!-- EVIDENCE:result-1:END -->

<!-- EVIDENCE:limitations:START -->
## 限制与下一步控制
模拟人群与组合式构造形成的是受控分布，不是真实生产需求。作者同时设计RetailRAG，因此应将基准设计和方法选择分别检验。论文审计了评审一致性，但答案评分不等于独立证明其证据支持全部结论。下一步应固定工具、模式暴露和总资源，同时保留两种答案指标，在新模式上测试人工编写的问题。构造链便于审计来源，但不应意外泄露给被测代理。它是异构证据编排的早期测量信号，而非证明单靠模型扩展一定不能解决企业检索。
<!-- EVIDENCE:limitations:END -->

[arXiv:2610.25096v1](https://arxiv.org/html/2610.25096v1) · [Official repository](https://github.com/DISL-Lab/RetailBridge)
