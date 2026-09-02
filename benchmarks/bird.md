# BIRD：text-to-SQL 开始面对大数据库、脏值与 external knowledge

**中文** | [English](bird.en.md) · [返回入口](../README.md) · [Benchmark Library](../library/README.md)

## 它在测什么

BIRD 含 12,751 个 text-to-SQL pairs、95 个 databases（约 33.4GB）、37 个 domains，并引入 database values 与 external knowledge，要求模型在更大、更真实的 schema 和数据内容上生成 SQL。

## 相比什么前进了

Spider 的 schema 更复杂，但数据库规模与真实 value grounding 仍有限。BIRD 把 large database content、dirty/value reasoning 与 external knowledge 拉进 text-to-SQL，使“理解 schema”不足以解决所有问题。

## 分数边界

execution accuracy 支持当前 BIRD release、value access 与 knowledge setup 下的 SQL correctness；它仍是 query answering，不覆盖多数据库 integration、Python analysis、reporting 或业务语义层。

## 公平比较条件

锁定 dataset/version、DB contents、external-knowledge access、schema/value retrieval、execution engine 与 prompt budget。不同 knowledge hints 应分 track。

## 下一步评测坐标

LiveSQLBench 将 drift、management SQL 与 evolving schemas 加入；Data Agent Benchmark 则进一步跨多个 DBMS 和非结构化文本。
