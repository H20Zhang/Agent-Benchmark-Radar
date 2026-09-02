# GateMem：shared memory 必须同时有 utility、access control 与 forgetting

**中文** | [English](gatemem.en.md) · [返回入口](../README.md) · [Benchmark Library](../library/README.md)

[论文](https://arxiv.org/abs/2606.18829) · [代码](https://github.com/rzhub/GateMem)

## 它在测什么

GateMem 有 91 个 multi-party episodes、2,218 个 hidden checkpoints，跨 medical、office、education、household。它联合评估 legitimate utility、unauthorized disclosure 与 deletion 后是否还能恢复信息，让 multi-principal governance 成为 memory contract 的一部分。

## 相比什么前进了

传统 memory benchmark 把“能检索回来”当好事。GateMem 明确指出 shared memory 中同一条信息对不同 principal 可能该可见、不可见或已删除，因此 memory quality 必须和 access boundary、active forgetting 一起优化。

## 分数边界

Memory Governance Score 支持 behavioral access/forgetting under the synthetic policy 与 harness；它不能证明 bytes 被物理擦除，也没有真实 authentication/authorization infrastructure。因此 deletion success 应解释为 non-retrievability under protocol，而非存储层安全证明。

## 公平比较条件

锁定 authorization policy、agent harness、backbone、judge 与 retrieval budget。不同 principal policy 或 deletion semantics 必须独立 track。

## 下一步评测坐标

下一步要接入真实身份、权限与 storage lifecycle，验证 revocation 后缓存、索引与派生 representation 都能一致删除。
