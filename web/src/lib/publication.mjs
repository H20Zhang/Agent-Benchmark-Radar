import { readFileSync } from "node:fs";
import { fromRepositoryRoot } from "./repository-path.mjs";
import { calendarWindow, dayWindow } from "./release-time.mjs";
export function publicationWindow() {
  const freshness = JSON.parse(
    readFileSync(fromRepositoryRoot("data", "freshness.json"), "utf8"),
  );
  return {
    asOf: freshness.discovery_scan_at,
    recent: calendarWindow(freshness.discovery_scan_at),
    frontier: dayWindow(freshness.discovery_scan_at, freshness.window_days),
  };
}
