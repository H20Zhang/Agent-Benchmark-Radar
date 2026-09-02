# ClaimProbe：Deep Research 报告的 claim-source 忠实度审计

**中文** | [English](claimprobe.en.md) · [返回入口](../README.md) · [Benchmark Library](../library/README.md)

[论文](https://arxiv.org/abs/2608.28643) · [代码](https://github.com/SalesforceAIResearch/claimwriter-deep-research)

**一句话：** ClaimProbe 在固定检索证据后逐 claim 审计“有没有依据、引对没引对、漏没漏引、关键事实有没有写进来”，从而把 writer-side faithfulness 与 retrieval/search 质量分开。

**问题。** DeepResearch Bench、DAS-Bench 与 LitReview Arena 已覆盖整体报告、citation/discourse 和专家偏好，但整体分数仍会把 retrieval、writer 与成品质感混在一起。

**证据。** Enterprise Deep Research 的 fixed-evidence writer intervention 中，hallucination 15.89→5.02、misattribution 18.94→5.43、necessary fact recall 36.83→45.85；上游 evidence 不变，因此支持 writer-side evidence materialization / attribution 改变，而不是 retrieval 或 planning 变好。

**限制。** 主 hallucination judge 与人工的一致性只有 Cohen κ=0.484，support search 还受 top-20 embedding shortlist 限制；动态更新只覆盖 5 个 DeepResearch Bench tasks，整体 RACE 变化也较小且 readability 有时下降。

**地图。** `early_signal`：新增 `retrieved evidence → written claim → cited source` 的独立诊断坐标，但单篇证据不改 durable Benchmark Map。

**链接。** [Primary](https://arxiv.org/abs/2608.28643) · [Code](https://github.com/SalesforceAIResearch/claimwriter-deep-research)
