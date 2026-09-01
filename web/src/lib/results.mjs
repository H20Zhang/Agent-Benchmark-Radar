import { existsSync, readFileSync, readdirSync } from "node:fs";
import { join } from "node:path";

import { loadRegistry } from "./registry.mjs";
import { fromRepositoryRoot } from "./repository-path.mjs";

const RESULT_DIRECTORY = fromRepositoryRoot("data", "results");
const TRACKING_STATES = new Set(["live", "paper-snapshot", "verified-snapshot"]);
const DIRECTIONS = new Set(["higher", "lower"]);
let resultCache;

function round(value, digits = 4) {
  const factor = 10 ** digits;
  return Math.round((value + Number.EPSILON) * factor) / factor;
}

function scoreComparator(direction) {
  return direction === "lower"
    ? (left, right) => left.score - right.score || left.method.localeCompare(right.method)
    : (left, right) => right.score - left.score || left.method.localeCompare(right.method);
}

function validateResultSet(resultSet, registryById) {
  const item = registryById.get(resultSet.benchmark_id);
  if (!item) throw new Error(`Result set references unknown benchmark ${resultSet.benchmark_id}`);
  if (!TRACKING_STATES.has(resultSet.tracking_status)) throw new Error(`${resultSet.benchmark_id} has invalid tracking_status`);
  if (!/^\d{4}-\d{2}-\d{2}$/.test(resultSet.verified_at || "")) throw new Error(`${resultSet.benchmark_id} has invalid verified_at`);
  if (!Array.isArray(resultSet.tracks) || resultSet.tracks.length === 0) throw new Error(`${resultSet.benchmark_id} has no result tracks`);

  const trackIds = new Set();
  for (const track of resultSet.tracks) {
    if (!track.track_id || trackIds.has(track.track_id)) throw new Error(`${resultSet.benchmark_id} has duplicate track ${track.track_id}`);
    trackIds.add(track.track_id);
    if (!DIRECTIONS.has(track.metric?.direction)) throw new Error(`${resultSet.benchmark_id}/${track.track_id} has invalid metric direction`);
    if (!Array.isArray(track.entries) || track.entries.length === 0) throw new Error(`${resultSet.benchmark_id}/${track.track_id} has no entries`);
    const range = track.metric.range;
    if (range && (!Array.isArray(range) || range.length !== 2 || range[0] >= range[1])) throw new Error(`${resultSet.benchmark_id}/${track.track_id} has invalid metric range`);
    const target = track.metric.reference_target;
    if (target && (!Number.isFinite(target.value) || !/^https:\/\//.test(target.source || ""))) {
      throw new Error(`${resultSet.benchmark_id}/${track.track_id} has unsourced reference target`);
    }

    const entryIds = new Set();
    for (const entry of track.entries) {
      if (!entry.id || entryIds.has(entry.id)) throw new Error(`${resultSet.benchmark_id}/${track.track_id} has duplicate entry ${entry.id}`);
      entryIds.add(entry.id);
      if (!Number.isFinite(entry.score)) throw new Error(`${resultSet.benchmark_id}/${track.track_id}/${entry.id} has invalid score`);
      if (range && (entry.score < range[0] || entry.score > range[1])) throw new Error(`${resultSet.benchmark_id}/${track.track_id}/${entry.id} is outside metric range`);
      if (!/^https:\/\//.test(entry.source || "")) throw new Error(`${resultSet.benchmark_id}/${track.track_id}/${entry.id} has invalid source`);
      if (!/^\d{4}-\d{2}-\d{2}$/.test(entry.date || "")) throw new Error(`${resultSet.benchmark_id}/${track.track_id}/${entry.id} has invalid date`);
    }
  }
}

export function loadAllResultSets() {
  if (resultCache) return resultCache;
  const registryById = new Map(loadRegistry().map((item) => [item.id, item]));
  const resultSets = new Map();
  if (existsSync(RESULT_DIRECTORY)) {
    for (const filename of readdirSync(RESULT_DIRECTORY).filter((name) => name.endsWith(".json")).sort()) {
      const resultSet = JSON.parse(readFileSync(join(RESULT_DIRECTORY, filename), "utf8"));
      validateResultSet(resultSet, registryById);
      if (resultSets.has(resultSet.benchmark_id)) throw new Error(`Duplicate result set ${resultSet.benchmark_id}`);
      resultSets.set(resultSet.benchmark_id, Object.freeze(resultSet));
    }
  }
  resultCache = resultSets;
  return resultCache;
}

export function loadResultSet(id) {
  return loadAllResultSets().get(id);
}

export function summarizeTrack(track) {
  const entries = [...track.entries].sort(scoreComparator(track.metric.direction));
  const best = entries[0];
  const chronological = [...track.entries].sort((left, right) => left.date.localeCompare(right.date) || left.id.localeCompare(right.id));
  const first = chronological[0];
  const latest = chronological.at(-1);
  const improvement = track.metric.direction === "lower" ? first.score - latest.score : latest.score - first.score;
  const target = track.metric.reference_target;
  const range = track.metric.range;
  let headroom;
  if (target && range) {
    const span = range[1] - range[0];
    const raw = track.metric.direction === "lower" ? best.score - target.value : target.value - best.score;
    headroom = round(Math.max(0, raw) / span * 100);
  }
  return { best, first, latest, headroom, improvement: round(improvement), entryCount: entries.length };
}

export function getProgressPoint(item, resultSet, now = new Date()) {
  const released = new Date(`${item.released.length === 7 ? `${item.released}-01` : item.released}T00:00:00Z`);
  const primary = resultSet.tracks.find((track) => track.primary) || resultSet.tracks[0];
  const summary = summarizeTrack(primary);
  const allEntries = resultSet.tracks.flatMap((track) => track.entries);
  const lastResultDate = allEntries.map((entry) => entry.date).sort().at(-1);
  return {
    benchmarkId: item.id,
    trackingStatus: resultSet.tracking_status,
    ageDays: Math.floor((now.getTime() - released.getTime()) / 86_400_000),
    headroom: summary.headroom,
    improvement: summary.improvement,
    activity: allEntries.length,
    lastResultDate,
    metricFamily: primary.metric.family,
    best: summary.best.score,
  };
}
