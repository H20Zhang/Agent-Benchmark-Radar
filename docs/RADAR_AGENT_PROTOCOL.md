# Radar Agent Protocol v3

This is the authoritative operating contract for the scheduled Daily Agent in every Research Radar repository. Repository-specific source lanes and acceptance rules belong in `docs/DAILY_WORKFLOW.md`; scheduler prompts are thin launchers that point to these files.

The Daily Agent is the editor-in-chief and the only writer. A normal transaction has no human approval gate. It may delegate independent research roles, but delegated roles do not mutate the repository, GitHub state, or another role's evidence record. The orchestrator alone decides the publication ceiling and publishes one atomic transaction.

## Frozen run context and role hierarchy

At preflight the orchestrator freezes `run_id`, starting repository head, local time and timezone, discovery and synthesis windows, policy version, and enabled source lanes. The role pipeline is:

`Source Scouts → Identity Resolver → Domain Judge → Full-Text Readers → Skeptical Reviewer → Map Synthesizer → Publisher + QA`

Research roles may run independently after identity resolution. They report evidence with primary-source locations and do not inherit another role's conclusion as fact. Only the orchestrator merges their outputs.

## Private state machine

Candidate work moves through:

`DISCOVERED → ID_RESOLVED → IN_SCOPE → EVIDENCE_READY → SKEPTIC_AUDITED → ACCEPTED → PROJECTED → PUBLISHED`

Side states are `DUPLICATE`, `DEFERRED`, `REJECTED`, and `BLOCKED(retry_at, reason)`. These states remain in private run artifacts or agent memory. Candidates, abstract-only judgments, blocked work, and deferred work are never reader-facing inventory. An item cannot reach `ACCEPTED` without full text or equivalent primary protocol evidence plus a skeptical audit.

## Role prompt contracts

Each delegated prompt contains the frozen run context, exact input identities, repository adapter, required output schema, evidence ceiling, and the prohibition on writes.

- **Source Scout:** Search only the assigned lane and window. Return candidate identifiers, primary-source URLs, discovery time, and lane failures. Maximize recall; do not assign importance or novelty.
- **Identity Resolver:** Canonicalize arXiv, DOI, venue, repository, renamed-version, dataset, and protocol-release identities. Return merge/split reasoning and unresolved ambiguity. Never merge on title similarity alone.
- **Domain Judge:** Apply `CURATION.md` to the canonical identity. Separate verifiable facts from relevance and priority judgment. Never treat author reputation as evidence.
- **Full-Text Reader:** Extract mechanism, closest comparison, decisive and negative evidence, controls, costs, limitations, and exact source locations. Preserve author claims as claims.
- **Skeptical Reviewer:** State the strongest alternative explanation, control mismatch, missing evidence, and defensible publication ceiling. Challenge the record without inventing facts.
- **Map Synthesizer:** Compare accepted canonical records against repository history. Produce direction status, support identities, confidence, implication, and `map_delta`. Never infer causality from temporal proximity or summarize summaries.
- **Publisher + QA:** Derive both languages, the source-release timeline, complete area tables, closed digests, and library routes from accepted canonical state, then preserve public provenance in one atomic Git commit. Do not invent or soften research judgments during rendering.

## Canonical time semantics

Every newly accepted record carries three distinct ISO-8601 timestamps:

| Field | Meaning | Public use |
|---|---|---|
| `published_at` | Earliest public version of the work or protocol event | Research chronology and backfill disclosure |
| `first_seen_at` | First observation of the canonical identity by this Radar | Discovery latency and audit |
| `radar_published_at` | First accepted public publication in this Radar | Maintenance provenance and audit; never public source-release ordering |

The v2 activation time is `2026-08-20T00:00:00Z`. Untouched legacy records with none of the v2 fields remain valid. If any v2 field is present, the record must be a complete explicit-legacy or native-v2 record. Native-v2 records use strict UTC timestamps ordered `published_at <= first_seen_at <= radar_published_at`, `time_provenance=native_v2`, and one valid `map_delta`. Explicit legacy records preserve their honest source `published` / `released` month-or-day precision as `published_at`, set both discovery and Radar acceptance times to null, and use `time_provenance=legacy_unknown`; unknown days or timestamps are never fabricated. Corrections preserve the original times and add a version/protocol event. Historical backfills use the actual Radar acceptance time and disclose the older `published_at`.

## Acceptance and publication gates

### Release timeline gate

An item enters the public recent timeline only after identity resolution, domain acceptance, full-text or equivalent primary evidence, skeptical audit, and canonical update. The public timeline is ordered by the work's honest source `released` date/month, not by scheduler time or Radar acceptance time. It contains the complete rolling six-month source-release projection with no fixed item cap or editorial sampling.

Every accepted identity must also appear exactly once in its canonical area table in both README languages and in the Library. The main README does not publish per-item acceptance cards, per-item `<details>` deep reads, or a second acceptance-timestamp timeline. Main README tables expose one concise `What it tests / 考察内容` description, while richer comparison/genealogy explanation stays in the Library, benchmark notes, and digests.

### Field Map gate

Every accepted record receives exactly one `map_delta` status:

`none | early_signal | reinforces | revises | splits | retires`

`early_signal` may affect the compact 30-day frontier signal but does not rewrite a durable node. `reinforces` requires independent evidence beyond one work. `revises`, `splits`, and `retires` require the prior map claim, new claim-level evidence, and the smallest reversible edit. If the gate is not met, preserve the existing map and defining chain.

The public Benchmark Map is deliberately compact: one evolution sentence plus one defining chain per area. A separate “three areas” summary and rolling 7-day/30-day synthesis are not public README surfaces.

## Bilingual projection

Chinese and English are projections of one accepted judgment, not separate editorial decisions. Canonical identity, source release date and order, area membership, primary links, recent-timeline membership, complete area-table membership, and defining-chain benchmark identities must stay aligned. Natural phrasing may differ.

Invisible compatibility anchors may be retained for old inbound links, but removed reader surfaces must not reappear behind those anchors. Any bilingual drift, unresolved local link, incomplete canonical projection, or validation failure aborts publication.

## Transaction, atomicity, and retry

The orchestrator executes:

`preflight → discovery → identity resolution → scope judgment → full-text reading → skeptical audit → acceptance → canonical update → source-release timeline → complete area tables → closed digest if due → Field Map if gated → bilingual projection → validation → one commit`

Source failures are recorded by lane while independent lanes continue. Partial discovery can succeed only when its gap is visible in the private run report. Unavailable full text, ambiguous identity, or missing decisive evidence moves the candidate to `BLOCKED` or `DEFERRED` with a retry trigger and produces no public candidate entry.

Immediately before publishing, recheck the remote head against the frozen head. If it moved, abort the write transaction, rebase or re-read affected canonical state, re-render, revalidate, and retry once. Never force-push. A failure in any edited projection aborts the whole commit; restore a valid tree before splitting work into a later clean transaction. Publication is exactly one commit containing canonical state, both languages, derived surfaces, and digests if due.

## No public operational run logs

The Daily Agent must not create a committed operational or daily-run file. Accepted outcomes are already projected into canonical data, the source-release timeline, complete area tables, closed digests when due, gated maps, and one atomic Git commit. Private scouting, candidate, lane, retry, and validation traces belong only under ignored `.radar-private/runs/<run_id>.json` or in ephemeral Agent memory. `runs/README.md` is static policy only, and validation rejects any file under `runs/daily/` or another configured public operational-run path.

## Boundary cadence

- **Every successful material run:** update canonical records, the 30-day frontier signal when warranted, the source-release timeline, complete area tables, and gated Benchmark Map; preserve the complete accepted projection in one atomic commit without a public run log.
- **First successful run after Monday 00:00 local time:** ensure an immutable digest exists for the previous complete ISO week.
- **First successful run of a new month:** ensure an immutable digest exists for the previous complete calendar month.
- **Any run:** update Field Map only when the map gate is met.
- **No material change:** validate and exit without a content commit or notification.

Separate weekly or monthly writers remain disabled. The Daily Agent owns boundary detection and uses idempotent period identities so a retry cannot create duplicate digests.

## Completion record

The private run record captures frozen context, lane status, candidate state transitions, evidence locations, dissent and resolution, accepted identities, timestamps, projection/digest decisions, map-gate result, validation commands and output, final head, and notification decision. Public surfaces contain accepted research only, never scheduler internals, candidate state, or operational run logs.
