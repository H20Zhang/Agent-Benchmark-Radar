/** Date intervals preserve source precision. An unknown day is never fabricated. */
export function dateInterval(value) {
  if (!/^\d{4}-\d{2}(?:-\d{2})?$/.test(value || ""))
    throw new Error(`Invalid date: ${value}`);
  const [year, month, day] = value.split("-").map(Number);
  if (month < 1 || month > 12) throw new Error(`Invalid month: ${value}`);
  const endDay = new Date(Date.UTC(year, month, 0)).getUTCDate();
  if (day !== undefined && (day < 1 || day > endDay))
    throw new Error(`Invalid day: ${value}`);
  const start = Date.UTC(year, month - 1, day ?? 1);
  return {
    start,
    end: Date.UTC(year, month - 1, day ?? endDay),
    precision: day === undefined ? "month" : "day",
  };
}
export function releaseDate(item) {
  for (const field of [
    "first_public_at",
    "publication_at",
    "data_release_at",
  ]) {
    if (item[field])
      return {
        date: item[field],
        field,
        ...item.release_date_evidence?.[field],
      };
  }
  const legacy = item.release_date_evidence?.legacy_recorded_at;
  return {
    date: legacy?.date || item.released,
    field: "legacy_recorded_at",
    precision: (legacy?.date || item.released).length === 7 ? "month" : "day",
    ...legacy,
  };
}
export function releaseLabel(release, lang = "en") {
  const labels =
    lang === "zh"
      ? {
          first_public_at: "最早已核验公开版本",
          publication_at: "正式发表",
          data_release_at: "数据开放",
          legacy_recorded_at: "历史记录 · 事件类型待复核",
        }
      : {
          first_public_at: "Earliest verified public version",
          publication_at: "Publication",
          data_release_at: "Data release",
          legacy_recorded_at: "Recorded date · event type unclassified",
        };
  return labels[release.field];
}
export function calendarWindow(asOf, months = 6) {
  const end = dateInterval(asOf).end;
  const d = new Date(end);
  const first = new Date(
    Date.UTC(d.getUTCFullYear(), d.getUTCMonth() - months, 1),
  );
  const day = Math.min(
    d.getUTCDate(),
    new Date(
      Date.UTC(first.getUTCFullYear(), first.getUTCMonth() + 1, 0),
    ).getUTCDate(),
  );
  return {
    start: Date.UTC(first.getUTCFullYear(), first.getUTCMonth(), day),
    end,
  };
}
export function dayWindow(asOf, days = 30) {
  if (!Number.isInteger(days) || days < 1)
    throw new Error("Window must contain at least one day");
  const end = dateInterval(asOf).end;
  return { start: end - (days - 1) * 86400000, end };
}
export const isoDay = (time) => new Date(time).toISOString().slice(0, 10);
export function inReleaseWindow(item, window) {
  const interval = dateInterval(releaseDate(item).date);
  return interval.end >= window.start && interval.start <= window.end;
}
export function releaseWindowStatus(item, window) {
  if (!inReleaseWindow(item, window)) return "outside";
  const interval = dateInterval(releaseDate(item).date);
  return interval.start < window.start || interval.end > window.end
    ? "overlap"
    : "inside";
}
export const isPublishedRecord = (item) =>
  ["active", "verified"].includes(item.status);
export function chronological(items) {
  return [...items].sort(
    (a, b) =>
      releaseDate(b).date.localeCompare(releaseDate(a).date) ||
      a.name.localeCompare(b.name),
  );
}
