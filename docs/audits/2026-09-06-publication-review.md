# Publication review: bilingual evidence and executable browser contracts

Review base: `b593711f1206f3478ce7d59883e3b57f4b680e8d` (PR #41 candidate), not the older deployed main. Temporary source export does not change the product. Findings were reproduced against this candidate before editing.

## Release-blocking findings and acceptance criteria

| ID | Reproduced failure | Repair and acceptance |
|---|---|---|
| R01 | A valid legacy capability/environment/protocol filter or repeated year was silently lost when state was reconstructed from visible controls. | Canonical URL state owns the workspace. Editing one dimension preserves every other valid condition; reload and language handoff retain the exact visible IDs. Ambiguous old facet aliases stay restrictive and show a warning. |
| R02 | Availability (`tracked`) and result source type (`paper-snapshot`) were ORed together as one facet, widening the result set. | Separate `status` and `source`, AND across them. A tracked paper query equals exactly the paper-snapshot set; untracked plus paper yields zero. Historical source-type URLs migrate explicitly. |
| R03 | Chinese query `长期` returned seven records in Chinese but zero in English. | Both languages use the same bilingual search corpus. All 131 card corpora match; live navigation, language switch and reload preserve the seven IDs. |
| R04 | Five result-entry budgets existed in the data but were absent from both rendered result panels. | Every available context/budget is rendered without dropping the source conditions. Missing values are explicitly unreported. A full-site assertion checks all entries, not only these five. |
| R05 | Compare encoded task/split/protocol metadata but never displayed it, inviting comparisons without the underlying conditions. | The table now shows task, split, protocol version, context, budget, report date and verification date. It still does not rank systems across benchmarks. |
| R06 | Historical substring matches had been frozen into explicit facets: a frozen-repository retrieval benchmark appeared under live retrieval; BRIGHT/BEIR under code workspaces; SearchAudit rubric grading under executable success. | Targeted membership review removes these mismatches, records reviewed dimensions and provenance, and leaves unreviewed dimensions honestly identified as imported heuristics. |
| R07 | SGR-Bench English omitted Row-F1 and the failure-subset denominator. RAGCap English omitted strict exact-match results, materially weakening the interpretation of high partial-credit scores. | Preserve Item/Row-F1, strict EM versus F1, model, prompt/version and failure-subset boundaries in both languages. Numeric/model parity contracts cover the corrected notes. |
| R08 | EvoBrowseComp English named LiveBrowseComp as the reported baseline and omitted language/tool/backbone conditions. Bright-Pro English omitted the separation of static, fixed-round and adaptive results. | Distinguish the paper's BrowseComp/BrowseComp-ZH comparison from complementary benchmarks; retain separate language/tool settings. Separate Bright-Pro static set and 175-query agentic subset and identify each backbone/budget. |
| R09 | SearchAuditBench repair-rubric success was described as successful repair execution. | FPS is diagnosis plus expert-rubric pass judged by DeepSeek-V4-Flash, not re-execution of search. Correct both authored notes, registry summary, taxonomy and result tasks. Actual online re-execution remains a proposed experiment. |
| R10 | Nine paper-only result records were displayed as leaderboard tracking snapshots. | Reclassify as paper snapshots. Validation rejects `live` when every recorded result source is a paper. This is a provenance classification correction, not a claim that scores were freshly re-verified. |

## Additional navigation, bilingual and visual fixes

- Translate note fragments during language handoff using paired heading identities. Keep old authored anchors; fall back explicitly to the interpretation section where no counterpart exists.
- Extract authored claim boundaries and controls using semantic heading aliases instead of returning generic boilerplate when headings differ across languages.
- Preserve block boundaries when extracting brief text from Markdown.
- Retain Core/Complement roles in the suite selection and Markdown export. Custom sets carry unverified roles and do not regain the original claim.
- Give the narrow Frontier table a bounded horizontal scroll region rather than squeezing dates and sources into unreadable columns.
- Keep mobile library controls compact and active constraints visible, localized and individually removable.

## Primary source checks for substantive content changes

- RAGCap-Bench v2, Table 3: <https://arxiv.org/html/2510.13910v2>. Informative-prompt three-run evaluation; Overall F1 81.05, evidence EM 42.02 and grounded reasoning EM 57.23 refer to different named models and metrics.
- SGR-Bench v1, main results and Appendix E: <https://arxiv.org/html/2605.22219v1>. CLI Item-F1 66.18 versus Row-F1 43.37; 156 analyzed failed trajectories are not the full benchmark denominator.
- EvoBrowseComp v1, sections 3–4 and Tables 2–3: <https://arxiv.org/html/2606.13120v1>. Baseline identity, 128K context, 40 tool calls, language slices, generation models and judge verified.
- SearchAuditBench v1, section 5.1 and Table 2: <https://arxiv.org/html/2608.05212v1>. FPS rubric semantics and auditor-backbone conditions verified.
- Bright-Pro, ACL paper Tables 2–4 (PDF pages 6–7 inspected): <https://aclanthology.org/2026.acl-long.1705.pdf>. Static alpha-nDCG, fixed-round answer quality and adaptive efficiency are distinct comparisons.
- Agent Retrieval Bench abstract/protocol: <https://arxiv.org/abs/2607.24882>. Frozen repository base commits, file retrieval and abstention are not live-web retrieval.

## Verification gates

`web/tests/review-semantic-regressions.test.mjs` checks state semantics, facet migration, paired fragments, budget provenance and bilingual load-bearing values. `web/scripts/verify-site.py` checks every generated route, internal target/fragment, bilingual corpus and result conditions, then runs real HTTP browser workflows in CI. Local offline screenshots are supplementary: they cannot validate navigation or deployment.

The deployment workflow stamps every page with `radar-build` and runs `web/scripts/smoke-live.py` against public Pages after deployment. The expected commit must be visible in the public response, not merely accepted by the deployment API. Evidence is retained as workflow artifacts.

Scope: this review does not claim independent replication of benchmark scores, exhaustive factual re-verification of all 131 papers, or Safari/WebKit testing. The five substantive bilingual note corrections were checked against the named first-party papers. Remaining raw English result-condition strings are labeled source originals rather than presented as machine-translated Chinese.
