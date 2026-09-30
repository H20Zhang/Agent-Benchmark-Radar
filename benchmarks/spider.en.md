# Spider: generalizing text-to-SQL to unseen database schemas

<!-- RELEASE-REFERENCE:START -->
> **Best at release (historical reference)** · 2018-09-24 · paper v1<br>
> **SQLNet — Database-split dev exact match: 14.3%**; **SQLNet — Database-split test exact match: 14.7%**<br>
> V1 Table 2 database-split results: 14.3% on development and 14.7% on test, each leading its split in that table. The abstract gives 14.3% without naming development; later revisions remain separate. [Original source](https://arxiv.org/abs/1809.08887v1)<br>
> Historical difficulty reference, not current SOTA; tasks, versions, and experimental conditions are not interchangeable.
<!-- RELEASE-REFERENCE:END -->

[中文](spider.md) | **English** · [Home](../README.en.md) · [Benchmark Library](../library/README.en.md)

<!-- EVIDENCE:reading:START -->
## Reading coverage and versions

Full substantive paper and appendix reading completed for the stated primary version; experiments were not independently reproduced.

Read all substantive v1 and EMNLP proceedings text, plus the complete one-page hardness supplement. The v5 check covers version metadata and Table 2 only; it is not a full v5 reading.

[arXiv 1809.08887v1 · 2018-09-24](https://arxiv.org/pdf/1809.08887v1) · [Proceedings · EMNLP 2018 · D18-1425](https://aclanthology.org/D18-1425.pdf) · [arXiv 1809.08887v5 · 2019-02-02](https://arxiv.org/pdf/1809.08887v5) · [Supplement · EMNLP 2018 · D18-1425 · supplement](https://aclanthology.org/attachments/D18-1425.Attachment.zip)
<!-- EVIDENCE:reading:END -->

<!-- EVIDENCE:method:START -->
## What the method measures

Spider tests SQL structure on unseen multi-table schemas. SQLNet uses a sketch decoder; TypeSQL additionally uses database contents. Exact matching ignores literal values, so it does not establish autonomous value retrieval.

<!-- EDITORIAL-METHOD:START -->
Annotators construct questions and SQL around relational schemas, then paraphrase the questions, covering joins, nesting, grouping and set operations. Database-disjoint evaluation prevents simple reuse of training-database name mappings. An illustrative workflow supplies an employee–department schema and a counting question: identify the join key, grouping target and condition, then emit SQL. Component evaluation checks clauses such as SELECT and WHERE before whole-query matching. This measures schema-linked structure, while omission of literal values limits end-to-end execution claims. The version table establishes the need to pin the evaluation contract, not parser progress across revisions.

Editorial placement: WikiSQL is the closest earlier single-table reference. Spider expands the coordinate to unseen multi-table schemas and compositional SQL, rather than introducing held-out tables for the first time. BIRD later emphasizes values and domain evidence. The useful distinction is single-table template generation versus relational composition on new schemas.
<!-- EDITORIAL-METHOD:END -->
<!-- EVIDENCE:method:END -->

<!-- EVIDENCE:setup:START -->
## Experimental setup

The v1 experiment adds six earlier datasets: 206 databases split 146/20/40 for train/dev/test. EMNLP instead uses 130/36/40. The paper adapts existing parsers; a comparable inference-token budget is unspecified.
<!-- EVIDENCE:setup:END -->

<!-- EVIDENCE:results:START -->
## Selected quantitative evidence

Version audit only; all values are exact match over queries, excluding literal values. Database counts describe the split, not the query denominator.

| System / comparison | Dataset / denominator | Metric / unit | Result | Conditions | Source |
| --- | --- | --- | --- | --- | --- |
| SQLNet · v1 test | Spider v1; 40 test databases | Exact match (% queries) | 14.7% | Question + schema | v1 Table 2, p. 8 |
| SQLNet · v1 dev | Spider v1; 20 dev databases | Exact match (% queries) | 14.3% | Same v1 protocol | v1 Table 2, p. 8 |
| TypeSQL · EMNLP | Spider EMNLP; 40 test databases | Exact match (% queries) | 9.7% | Content-assisted typing; changed split | EMNLP Table 2, p. 3918 |
| SQLNet · v5 | Spider v5; 40 test databases | Exact match (% queries) | 12.4% | Revised result; not initial release | v5 Table 2, p. 8 |

Fact source: [v1 Table 2, p. 8; EMNLP Table 2, p. 3918; v5 Table 2, p. 8](https://arxiv.org/pdf/1809.08887v1)

[EMNLP Table 2](https://aclanthology.org/D18-1425.pdf) · [arXiv v5 Table 2](https://arxiv.org/pdf/1809.08887v5)
<!-- EVIDENCE:results:END -->

<!-- EVIDENCE:limitations:START -->
## Limits and interpretation

The header uses v1: SQLNet obtains 14.3% on development and 14.7% on test. EMNLP and v5 appear in the body only for version auditing. The v5 value of 12.4% must not be backdated or treated as a cross-version progress ranking. Normalized schemas and exclusion of ambiguous/outside-knowledge questions limit enterprise extrapolation.

<!-- EDITORIAL-NEXT:START -->
Next, fix one version and question set, separately supply gold schema links, gold literal values and both, then report structural matching and execution consistency across multiple database instances. This separates schema linking, compositional decoding and accidental result equality instead of treating revision changes as progress.
<!-- EDITORIAL-NEXT:END -->
<!-- EVIDENCE:limitations:END -->
