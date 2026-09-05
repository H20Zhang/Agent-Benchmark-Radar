# AuthMem-Bench：记住内容还不够，还要记住它有没有权威

**中文** | [English](authmem-bench.en.md) · [返回 Radar](../README.md) · [Benchmark Library](../library/README.md)

[论文](https://arxiv.org/abs/2608.01679)

## 它到底测什么

AuthMem-Bench 测 persistent-memory consolidation 是否保留 **source authority**。它用配对设计固定要记住的 claim 与下游任务，只改变来源的权威条件，从而检查同一内容在被整理进长期记忆后，会不会失去“谁有资格让系统把它当成事实或指令”的边界。

## 相比此前评测多测了什么

GateMem 等工作已经把共享记忆的 access control 变成评测对象；AuthMem-Bench 更进一步把风险定位到 **consolidation boundary**：即使最终记忆文本本身没有明显恶意内容，来源约束也可能在摘要、抽取或归一化时被洗掉。

## 决定性证据

论文报告，在 7 种 consolidator × 7 个 LLM backbone 的 49 个配置中，48 个观察到 authority collapse；在受控 action-grounded 条件下，缺少 authority metadata 的 collapsed memory 平均 unauthorized-action rate 为 50.3%。端到端实验中，自动预测并持久保存 authority label 后，观察到的 unauthorized-action rate 从 16.9% 降到 0.0%，同时 benign task success 基本不变。

## 这个分数能证明什么

它支持“某个 memory pipeline 是否在写入/整理过程中保持来源权威边界”的判断。它不能单独证明完整权限系统安全，因为身份认证、真实 ACL、跨租户隔离、provenance spoofing 与物理删除不在同一个受控对象里。

## 公平比较契约

固定 consolidator 输入、LLM backbone、authority-label policy、memory write/read policy 与 downstream action harness；尤其不能把人工提供 authority metadata 的系统与需要自行恢复 authority 的系统直接归因为同一组件能力。

## 还没有测什么

真实多主体身份系统、恶意 provenance 伪造、长期多次 consolidation 后的 authority drift，以及生产 memory store 中的治理代价。

## 下一步最有判别力的验证

做 `same claim × same downstream task × different source authority × repeated consolidation depth` 的 factorial control，并在正确 authority metadata 直接给定条件下建立 oracle ceiling，区分 authority extraction、persistence 与 action policy 三层失败。

<!-- RESEARCH-DECISION:START -->
## 研究决策卡
### 什么时候值得用
如果你的 claim 是 memory consolidation、summary、experience extraction 或 self-evolving memory 不应把来源约束洗掉，AuthMem-Bench 是比一般 recall benchmark 更直接的安全坐标。
### 一个具体任务长什么样
示意任务：相同一句陈述分别来自有权设定规则的用户与低权限外部来源；经过 consolidation 后，后续 action request 看起来完全相同。正确系统必须只在授权来源条件下把记忆当成可执行约束。
### 最有判别力的实验
固定 claim 与 action，只改变 authority 和 consolidation depth；同时给出 oracle authority metadata，测收益究竟来自正确识别来源还是下游 policy。
### 建议搭配
[GateMem](gatemem.md) · [InjecMEM](injecmem.md) · [Utility Under Attack](utility-under-attack.md)
> **读分数的原则：** authority preservation 是 memory lifecycle 的一层，不等价于完整部署权限安全。
<!-- RESEARCH-DECISION:END -->

## 演化位置
`recall → shared-memory governance → provenance / authority-preserving consolidation`
