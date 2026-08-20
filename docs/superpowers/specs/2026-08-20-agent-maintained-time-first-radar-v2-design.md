# Agent-Maintained Time-First Radar v2

Date: 2026-08-20

## Purpose

The four Radar repositories are not human-maintained awesome lists. A scheduled Daily Agent is the editor-in-chief: it discovers work, resolves identity, performs full-text reading, challenges claims, updates canonical records, derives public views, validates the repository, and publishes one atomic transaction.

This design makes time the default reader entry without reducing the repositories to feeds. A returning reader should quickly answer three questions in this order:

1. What was newly accepted by this Radar?
2. What changed over the last week or month?
3. Did the field map actually move?

Scope: Agent Benchmark Radar, Agent Memory Radar, Agentic RAG Radar, and Data Agent Radar; their Chinese and English READMEs; repository-owned Daily Agent contracts; canonical time semantics; weekly/monthly compaction; deterministic validation; and the four existing Scheduled Agent prompts.

Non-goals: GitHub Pages; a public candidate queue; requiring a human approval gate; publishing abstract-only judgments; merging all four repositories; duplicating benchmark genealogy in domain repositories; or treating every accepted paper as a field-map change.

## External project lessons

The design borrows mechanisms, not page shapes:

- [OSU GUI Agents Paper List](https://github.com/OSU-NLP-Group/GUI-Agents-Paper-List): one structured source can support recent, topic, year, and statistical views; Radar adds editorial evidence and inline explanation.
- [LLMSys Paper List](https://github.com/AmberLJC/LLMSys-PaperList): trends before exhaustive navigation help readers form a field model; Radar makes trends time-bounded and evidence-gated.
- [SJTU Awesome Data Agent Papers](https://github.com/SJTU-DMTai/Awesome-Data-Agent-Papers): automated discovery and deterministic generation reduce maintenance drift; Radar replaces its human shortlist gate with a full Daily Agent research transaction.
- [Track Awesome List](https://github.com/trackawesomelist/trackawesomelist): static lists create demand for an explicit change layer; Radar owns chronology rather than outsourcing it.
- [awesome-selfhosted-data](https://github.com/awesome-selfhosted/awesome-selfhosted-data): source data and rendered views should be separate, with deterministic checks; Radar preserves its heterogeneous canonical schemas rather than forcing a risky bulk migration.

The design deliberately does not copy badge-heavy first screens, long taxonomy tables, permanent `NEW` markers, alphabetical default order, or human PR backlogs. Those patterns suit directories better than autonomous research radars.

## Binding decisions

1. **Daily Agent is the only writer.** It may delegate independent research roles, but only its orchestrator mutates the repository or GitHub state.
2. **Research is complete before public visibility.** Discovery, identity resolution, scope judgment, full-text evidence extraction, skeptical audit, editorial decision, and publication happen in one transaction. Blocked or abstract-only items remain internal and are retried; they are not shown as public `pending` entries.
3. **Time first, map last.** Public order is `Latest Timeline → 7-day / 30-day synthesis → Field Map → Reading Paths → Library`.
4. **No fixed item cap.** The Latest Timeline shows every native-v2 accepted record whose `radar_published_at` is within the repository's current 30-day window, followed during migration by the repository's fixed explicit-legacy compatibility projection. Other older items remain reachable in Library. A high-volume period may be grouped by day, but records may not be silently dropped.
5. **One compact line, one inline explanation.** Every timeline record is a `<details>` item. Its closed summary contains date, title, domain/problem label, and one-sentence research delta. Opening it reveals enough evidence and caveat to understand the result without leaving the README.
6. **Period synthesis is not recursive summarization.** Seven-day and 30-day synthesis use `radar_published_at` to re-read native canonical records and deep notes in the window. Legacy records may provide context but are not window support. Weekly summaries are never summarized to produce monthly claims.
7. **One paper is not a trend.** An accepted record may enter Timeline immediately. A one-record direction is `new_signal` only when its `map_delta` is `early_signal`; `reinforced` requires at least two distinct in-window native records, and `revised` requires support. Field Map changes require an explicit `map_delta` and historical comparison.
8. **Chinese and English are projections of one judgment.** Identity, dates, evidence scope, decisive result, caveat, map position, and links must match across languages.

## Reader architecture

Each root README uses the following conceptual order. Natural Chinese and English headings may differ, but anchors and semantics remain paired.

```text
Title + family route + depth navigation
Latest Timeline                       # native radar_published_at desc + fixed legacy projection
7-day / 30-day synthesis              # direction changes, not a second paper list
Field Map                             # durable problem/design structure
Reading Paths                         # question-led first read and next reads
Research Library                      # complete history and alternate routes
Scope / About / Contributing
```

Agent Benchmark Radar remains the family entry and horizontal evaluation layer. Its Timeline combines newly accepted benchmark/protocol events across Memory, RAG, and Data Agents. Domain repositories show their own method/system Timeline and link to the corresponding evaluation coordinate in Benchmark Radar.

### Timeline summary contract

Closed form:

```text
YYYY-MM-DD · Title · Domain / research problem — one-sentence research delta
```

`YYYY-MM-DD` is `radar_published_at`, because the section answers what is new to the Radar. During migration, a legacy record whose Radar acceptance time cannot be reconstructed may display its existing `published_at`/`released` value (including honest `YYYY-MM` month precision) under one section-level legacy notice. When the two dates differ materially, the open content states the original publication date and whether this is a historical backfill, version correction, or newly discovered work. Historical work added today must never be phrased as newly published research.

Open form contains these semantic fields, expressed naturally rather than as repetitive form labels when prose reads better:

- research question;
- smallest real delta and closest meaningful control;
- decisive evidence, including a quantitative result only when it changes interpretation;
- strongest limitation or alternative explanation;
- map position and `map_delta` status;
- primary paper/project link and local deep note.

The closed summaries are the complete current list. The open bodies are the same-layer 60–90 second reading surface. Deep notes remain the claim-audit layer.

### Seven-day and 30-day synthesis

The first subsection states its exact inclusive date window and last synthesis time. Each direction item contains:

```text
Direction change → supporting accepted records → confidence → implication for research design
```

Stable bilingual metadata carries the direction key, state, ordered support identities, confidence, research-design implication, and `radar_published_at` timing basis. Only native-v2 records whose Radar acceptance lies in the stated window may appear as support.

The section distinguishes:

- `new_signal`: one credible record changes what should be watched;
- `reinforced`: at least two independent accepted records support the same direction;
- `revised`: evidence weakens or materially qualifies an existing direction;
- `no_material_change`: the period has no defensible direction-level change and may have no supporting native record.

The Scheduled Agent may update this section on any run with material evidence. On the first successful run after an ISO week or calendar month closes, it also writes an immutable digest for the complete previous period. Separate weekly/monthly writers remain disabled to avoid concurrent edits.

### Field Map gate

Every accepted record receives one of:

```text
none | early_signal | reinforces | revises | splits | retires
```

`early_signal` changes Timeline and may appear in period synthesis, but does not rewrite a durable map node. `reinforces` requires independent evidence beyond a single work. `revises`, `splits`, and `retires` require a claim-level explanation of the prior map state, the new evidence, and the smallest reversible map edit.

## Canonical time semantics

All new accepted records must carry three distinct strict UTC timestamps:

| Field | Meaning | Reader use |
|---|---|---|
| `published_at` | Earliest public version of the work or protocol event | Research chronology |
| `first_seen_at` | First time this Radar's discovery process observed the identity | Discovery latency and audit |
| `radar_published_at` | First accepted public publication in this Radar | Latest Timeline order |

Untouched legacy records with none of the v2 fields remain valid. If any v2 field is present, the record must provide the complete explicit-legacy or native-v2 combination. Native records use `YYYY-MM-DDTHH:MM:SSZ`, satisfy `published_at <= first_seen_at <= radar_published_at`, set `time_provenance=native_v2`, and carry one valid `map_delta`. Explicit legacy records copy the honest month/day `released` value to `published_at`, keep `first_seen_at` and `radar_published_at` null, set `time_provenance=legacy_unknown`, and carry one valid `map_delta`; unknown precision is never fabricated. The v2 activation time is `2026-08-20T00:00:00Z`.

Corrections do not overwrite these times. A material version/protocol correction adds a version event and preserves the original identity and publication event. Backfills set `radar_published_at` to the acceptance date and explicitly preserve the historical `published_at`.

## Internal agent protocol

The repository-owned protocol is authoritative; Scheduled Agent prompts remain thin launchers. The orchestrator freezes `run_id`, repository head, time window, policy version, and source lanes before delegation.

```text
Source Scouts
  → Identity Resolver
  → Domain Judge
  → Full-Text Readers
  → Skeptical Reviewer
  → Period / Map Synthesizer
  → Publisher + QA
```

Only the orchestrator writes. Independent roles do not inherit another role's prose conclusion as evidence.

### Internal state machine

```text
DISCOVERED → ID_RESOLVED → IN_SCOPE → EVIDENCE_READY
→ SKEPTIC_AUDITED → ACCEPTED → PROJECTED → PUBLISHED
```

Internal side states are `DUPLICATE`, `DEFERRED`, `REJECTED`, and `BLOCKED(retry_at, reason)`. They may be kept only in ignored `.radar-private/` artifacts or ephemeral Agent memory, and are not reader-facing inventory. An item may not reach `ACCEPTED` without full text or equivalent primary protocol evidence and a skeptical audit.

### Role contracts

- **Source Scouts:** maximize recall across declared source lanes; report source failures; never assign importance or claim novelty.
- **Identity Resolver:** canonicalize arXiv, DOI, venue, repository, renamed-version, and protocol-release identities before scope judgment; never merge on title similarity alone.
- **Domain Judge:** apply repository `CURATION.md`; separate verifiable facts from relevance/priority judgment; never promote author reputation into evidence.
- **Full-Text Reader:** extract mechanism, closest comparison, decisive evidence, negative result, costs, and source locations; author claims remain labeled as claims.
- **Skeptical Reviewer:** state the strongest alternative explanation, mismatched controls, missing evidence, and publication ceiling; never add new facts.
- **Period / Map Synthesizer:** compare accepted canonical records with existing history; produce direction and `map_delta`; never infer causality from temporal proximity.
- **Publisher + QA:** derive Chinese/English README, digests, and library routes, validate them, and preserve public provenance in one atomic Git commit; never invent or soften research judgments during rendering.

## Domain adapters

The shared pipeline is stable; the acceptance question changes by repository.

| Radar | Controlled object | Minimal loop | Success contract | Characteristic failure |
|---|---|---|---|---|
| Benchmark | Evaluation object and protocol | task/environment → harness → trajectory → evaluator | Claim is supported under stated controls | Harness/model/budget confounds component attribution |
| Memory | Persistent agent state | write → access → reconstruct → update/forget | Future behavior changes correctly | Stale or wrong memory misguides action |
| Agentic RAG | External information environment | search → inspect → continue/redirect/stop | Evidence is sufficient and cost is attributable | Interface/harness effects masquerade as policy gains |
| Data Agent | Analytic workspace | ground → execute → verify → recover → deliver | Artifact and business meaning are correct | Execution succeeds while semantics are wrong |

Each `docs/DAILY_WORKFLOW.md` supplies source lanes, inclusion rules, canonical record locations, note contracts, local validation commands, and domain-specific `map_delta` tests.

## Daily transaction and cadence

```text
preflight
→ discovery
→ identity resolution
→ scope judgment
→ parallel full-text reading
→ skeptical audit
→ editorial acceptance
→ canonical update
→ Timeline projection
→ 7-day / 30-day synthesis when material
→ closed-period digest when boundary crossed
→ Field Map update only when gated
→ bilingual generation
→ validation
→ one commit
```

Normal day: update canonical records, deep notes, Timeline, and rolling periods when material, then publish one atomic Git commit.
First successful run after Monday 00:00 local time: ensure the previous full ISO-week digest exists.
First successful run of a new month: ensure the previous full calendar-month digest exists.
Any day: update the map only when accepted evidence satisfies the map gate.
No material change: validate the repository and exit without a content commit or notification.

The orchestrator rechecks remote head immediately before publication. If head moved, it aborts the write transaction, rebases/re-reads affected canonical state, revalidates, and retries once. It never force-pushes.

### No public operational run logs

`runs/README.md` is static policy only. The Daily Agent never commits a file under `runs/daily/` or another public operational path. Private scout, candidate, lane, retry, and validation traces live only in ignored `.radar-private/` state or ephemeral Agent memory. Canonical data, the complete bilingual Timeline, any due digest, and one atomic Git commit are the public provenance.

## Failure and retry contract

- Source failure is recorded per lane; other lanes continue. A run may succeed with partial discovery only when the gap is visible in its internal run report.
- Full text unavailable, identity ambiguous, or decisive evidence missing results in `BLOCKED`/`DEFERRED` with a retry trigger. Nothing public is published for that candidate.
- Conflicting reader and skeptic conclusions remain explicit. The orchestrator resolves the publication ceiling from claim-level evidence, not majority vote.
- Bilingual drift, invalid time semantics, unresolved local links, or validator failure aborts the transaction.
- Period synthesis failure must not block a valid new Timeline item; the run publishes neither if both are edited in one inconsistent transaction. The orchestrator may split the work into a later clean transaction only after restoring a valid tree.

## Deterministic validation

Every repository validates:

- conceptual top-level order in both languages;
- Timeline item identity/order parity across languages;
- reverse-complete current-window native Timeline membership in full `radar_published_at` order, followed by the fixed explicit-legacy projection;
- every closed summary includes date, identity, problem/domain label, and delta;
- every open item exposes evidence, limitation, map position, and deep/primary links;
- no hard-coded 6–8 or 8–10 Latest cap remains;
- exact date windows are present for 7-day / 30-day synthesis;
- stable period metadata, native-only `radar_published_at` window support, bilingual direction parity, and one-record/`reinforced` cardinality rules;
- local links resolve and canonical identities exist;
- no `BLOCKED`, `DEFERRED`, or abstract-only candidate appears in public projections;
- paired Chinese/English high-visibility claims preserve the same identity, dates, evidence scope, map status, and primary links.

Validators test observable behavior against fixtures or repository surfaces; they do not merely grep for one exact source line.

## Repository and Scheduled Agent migration

1. Add the same versioned `docs/RADAR_AGENT_PROTOCOL.md` to all four repositories.
2. Rewrite each `docs/DAILY_WORKFLOW.md` as a thin domain adapter to that protocol while preserving valuable existing evidence and bilingual rules.
3. Restructure both READMEs to the v2 order. Convert current visible records into compact, inline-expandable Timeline items without deleting deep notes or canonical history.
4. Rename/reframe the current direction section as explicit 7-day / 30-day synthesis and state exact current windows. Preserve the strongest existing direction judgments.
5. Remove fixed Latest-count assumptions from validators; add time-first ordering, inline-detail, period-window, and bilingual parity checks.
6. Add or extend tests before changing validator behavior, and run every repository's existing validation commands.
7. Update the four active Scheduled Agent prompts only after the repository contracts are merged. Prompts point to repository files and do not duplicate the full workflow.
8. Keep separate RAG weekly/monthly Scheduled Tasks disabled; the Daily Agent owns period boundaries.

## Acceptance criteria

A reader can scan every current accepted Timeline record without scrolling through expanded prose; open any record in place for a 60–90 second evidence-aware explanation; see what changed in explicit recent windows; then move into a stable Field Map or a question-led path.

The Daily Agent can execute the full research and editorial transaction without a human gate; distinguish original publication, discovery, and Radar publication times; retry blocked research internally; create weekly/monthly compactions at boundaries; avoid map churn; and publish one bilingual, validated commit.

## Unknown unknowns to monitor

1. **Timeline truth may diverge from research chronology.** `radar_published_at` is honest about editorial novelty but can overweight rediscovery/backfill. The UI must surface both dates and event type.
2. **Compaction can manufacture momentum.** Repeatedly naming a direction in 7-day and 30-day prose may make weak evidence feel mature. Confidence and supporting identities must remain explicit, and monthly synthesis must re-read records rather than weekly prose.
3. **Independent agents can still share hidden bias.** Different roles may use the same model or source corpus. Structured dissent and closest-control checks reduce, but do not eliminate, correlated judgment error.
