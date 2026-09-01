import assert from "node:assert/strict";
import test from "node:test";

import { loadRegistry } from "../src/lib/registry.mjs";
import {
  getProgressPoint,
  loadAllResultSets,
  summarizeTrack,
} from "../src/lib/results.mjs";

const higherIsBetter = {
  track_id: "success",
  metric: {
    id: "success-rate",
    family: "success-rate",
    label: "Success rate",
    unit: "%",
    direction: "higher",
    range: [0, 100],
    reference_target: { value: 100, type: "benchmark-ceiling", source: "https://example.com" },
  },
  entries: [
    { id: "a", method: "A", model: "M1", score: 63.7, date: "2026-05-01", source: "https://example.com/a" },
    { id: "b", method: "B", model: "M2", score: 82.1, date: "2026-07-01", source: "https://example.com/b" },
  ],
};

const lowerIsBetter = {
  track_id: "cost",
  metric: { id: "cost", family: "cost", label: "Cost", unit: "USD", direction: "lower", range: [0, 100] },
  entries: [
    { id: "a", method: "A", model: "M1", score: 2.4, date: "2026-05-01", source: "https://example.com/a" },
    { id: "b", method: "B", model: "M2", score: 1.8, date: "2026-07-01", source: "https://example.com/b" },
  ],
};

test("best score respects metric direction", () => {
  assert.equal(summarizeTrack(higherIsBetter).best.score, 82.1);
  assert.equal(summarizeTrack(lowerIsBetter).best.score, 1.8);
});

test("headroom is emitted only with a sourced bounded target", () => {
  assert.equal(summarizeTrack(higherIsBetter).headroom, 17.9);
  assert.equal(summarizeTrack(lowerIsBetter).headroom, undefined);
});

test("progress point separates age, activity, improvement, and headroom", () => {
  const point = getProgressPoint(
    { id: "demo", released: "2026-04-01" },
    { benchmark_id: "demo", tracking_status: "live", verified_at: "2026-08-31", tracks: [higherIsBetter] },
    new Date("2026-09-01T00:00:00Z"),
  );

  assert.equal(point.ageDays, 153);
  assert.equal(point.headroom, 17.9);
  assert.equal(point.improvement, 18.4);
  assert.equal(point.activity, 2);
});

test("repository result sets are source-backed and canonical", () => {
  const ids = new Set(loadRegistry().map((item) => item.id));
  const resultSets = loadAllResultSets();
  assert.ok(resultSets.size >= 6);

  for (const [id, resultSet] of resultSets) {
    assert.ok(ids.has(id), id);
    assert.equal(resultSet.benchmark_id, id);
    assert.match(resultSet.verified_at, /^\d{4}-\d{2}-\d{2}$/);
    for (const track of resultSet.tracks) {
      assert.ok(track.entries.length > 0);
      for (const entry of track.entries) assert.match(entry.source, /^https:\/\//);
    }
  }
});
