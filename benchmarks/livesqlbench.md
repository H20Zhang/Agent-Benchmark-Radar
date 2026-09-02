# LiveSQLBench：SQL benchmark 本身也会 drift，且 enterprise database 不只有 query

**中文** | [English](livesqlbench.en.md) · [返回入口](../README.md) · [Benchmark Library](../library/README.md)

[项目页](https://livesqlbench.ai/)

## 它在测什么

LiveSQLBench 包含 Base-Lite（约 270 tasks/18 DBs）、Base-Full（约 600/22）与 Large-v1（约 480/18 industrial databases，平均约 1K columns/54 tables）等 tracks，覆盖 query SQL 与 management/DDL-style tasks，并维护 model/agent tracks 与 hidden/evolving releases。

## 相比什么前进了

Spider/BIRD 是固定 benchmark snapshot。LiveSQLBench 把 dataset/validator evolution 与更大 enterprise schema 放进 benchmark lifecycle，避免模型只对刷旧题库，同时扩展到数据库操作而不仅是 SELECT。

## 分数边界

success rate 只对具体 track/release/harness 有意义。随着 hidden tests、rules 或 schema 更新，旧结果不能无条件与新结果横比，因此成绩必须版本化而不是维护一个永恒 SOTA。

## 公平比较条件

锁定 Base/Large track、release date、schema hints、DB engine、model/agent mode、tool budget 与 evaluator rules。

## 下一步评测坐标

下一步应把 SQL execution 与业务 semantic layer、multi-system integration 和 persistent operational state 连接起来。
