"""Structural evidence guards do not certify a paper was read or reproduced."""
from __future__ import annotations
from copy import deepcopy
import hashlib
import json
from pathlib import Path
import sys
import tempfile
import unittest
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from note_evidence_contract import validate_review, validate_evidence_state, note_hash

def block(key, text):
    return f"<!-- EVIDENCE:{key}:START -->\n{text}\n<!-- EVIDENCE:{key}:END -->"

def example():
    source = "https://example.org/paper-v1"
    texts = {}
    for lang in ("zh", "en"):
        texts[lang] = "\n\n".join([
            "# Example",
            block("reading", f"Full primary text reviewed. v1 2026-09-30 {source}"),
            block("method", "The task diagnoses state changes using controlled episodes."),
            block("setup", "Reader A, dataset D test split, five retrieved items."),
            block("results", "Dataset D; Reader A; top-5.\nAccuracy (%)\n"
                  "| System | Accuracy (%) |\n|---|---:|\n| A | 80.0 |\n| B | 70.0 |\n"
                  f"[Primary source]({source}), Table 1. References to Table 1 are permitted."),
            block("limits", "Unequal upstream processing prevents a causal architecture ranking."),
        ])
    review = {
        "status": "full-text-reviewed", "reviewed_at": "2026-09-30",
        "status_text": {lang: "Full primary text reviewed." for lang in ("zh", "en")},
        "evidence_mode": "quantitative",
        "sources": [{"url": source, "version": "v1", "kind": "paper-full-text",
                     "coverage": ["method", "experimental_setup", "results", "limitations"]}],
        "blocks": [
            {"id": "reading", "kind": "reading"},
            {"id": "method", "kind": "method"},
            {"id": "setup", "kind": "setup"},
            {"id": "results", "kind": "quantitative", "source_url": source,
             "source_locator": "Table 1", "row_ids": ["A", "B"],
             "conditions": {lang: "Dataset D; Reader A; top-5." for lang in ("zh", "en")},
             "metric_labels": {lang: ["Accuracy (%)"] for lang in ("zh", "en")}},
            {"id": "limits", "kind": "limitations"}],
    }
    review["note_sha256"] = {lang: note_hash(text) for lang, text in texts.items()}
    return texts, review

def errors(texts, review):
    review = deepcopy(review)
    review["note_sha256"] = {lang: note_hash(text) for lang, text in texts.items()}
    return validate_review("example", review, texts)

class NoteEvidenceContractTests(unittest.TestCase):
    def test_valid_displayed_evidence_keeps_table_references(self):
        texts, review = example()
        self.assertEqual([], errors(texts, review))

    def test_malformed_source_coverage_fails_without_crashing(self):
        texts, review = example()
        review["sources"][0]["coverage"] = {"method": True}
        self.assertTrue(any("coverage" in e for e in errors(texts, review)))

    def test_missing_full_read_coverage_fails(self):
        texts, review = example()
        review["sources"][0]["coverage"].remove("experimental_setup")
        self.assertTrue(any("coverage" in e for e in errors(texts, review)))

    def test_abstract_cannot_be_declared_full_text(self):
        texts, review = example()
        review["sources"][0]["kind"] = "abstract"
        self.assertTrue(any("full-text source" in e for e in errors(texts, review)))

    def test_method_and_setup_are_required_without_fixed_headings(self):
        texts, review = example()
        review["blocks"] = [b for b in review["blocks"] if b["kind"] != "setup"]
        self.assertTrue(any("setup block" in e for e in errors(texts, review)))

    def test_bare_reference_and_numeric_prose_are_not_an_evidence_table(self):
        texts, review = example()
        texts["en"] = texts["en"].replace("| System | Accuracy (%) |\n|---|---:|\n| A | 80.0 |\n| B | 70.0 |", "A scored 80.0; see Table 1.")
        self.assertTrue(any("table" in e for e in errors(texts, review)))

    def test_unsourced_numeric_block_fails(self):
        texts, review = example()
        texts["zh"] = texts["zh"].replace("[Primary source](https://example.org/paper-v1)", "Primary source")
        self.assertTrue(any("visible source" in e for e in errors(texts, review)))

    def test_unknown_source_is_not_accepted(self):
        texts, review = example()
        review["blocks"][3]["source_url"] = "https://example.org/unreviewed"
        self.assertTrue(any("reviewed source" in e for e in errors(texts, review)))

    def test_missing_conditions_fails(self):
        texts, review = example()
        texts["zh"] = texts["zh"].replace("Dataset D; Reader A; top-5.", "")
        self.assertTrue(any("conditions" in e for e in errors(texts, review)))

    def test_missing_metric_units_fails(self):
        texts, review = example()
        texts["en"] = texts["en"].replace("Accuracy (%)", "Result")
        self.assertTrue(any("metric" in e for e in errors(texts, review)))

    def test_numeric_language_drift_fails(self):
        texts, review = example()
        texts["zh"] = texts["zh"].replace("| A | 80.0 |", "| A | 81.0 |")
        self.assertTrue(any("numeric parity" in e for e in errors(texts, review)))

    def test_row_binding_prevents_swapped_model_scores(self):
        texts, review = example()
        texts["zh"] = texts["zh"].replace("| A | 80.0 |", "| A | 70.0 |").replace("| B | 70.0 |", "| B | 80.0 |")
        self.assertTrue(any("numeric parity" in e for e in errors(texts, review)))

    def test_real_zero_is_not_missing_evidence(self):
        texts, review = example()
        texts = {lang: text.replace("| A | 80.0 |", "| A | 0.0 |") for lang, text in texts.items()}
        self.assertEqual([], errors(texts, review))

    def test_duplicate_or_undeclared_block_fails(self):
        texts, review = example()
        texts["zh"] += "\n" + block("results", "Another result")
        self.assertTrue(any("exactly one" in e for e in errors(texts, review)))

    def test_subsequent_note_change_invalidates_review_hash(self):
        texts, review = example()
        texts["en"] += "\nChanged conclusion."
        self.assertTrue(any("reviewed note hash" in e for e in validate_review("example", review, texts)))

    def test_protocol_only_with_explicit_numerical_gap_needs_no_fake_table(self):
        texts, review = example()
        review["status"] = "primary-protocol-reviewed"
        review["status_text"] = {lang: "Primary protocol reviewed." for lang in ("zh", "en")}
        texts = {lang: text.replace("Full primary text reviewed.", "Primary protocol reviewed.") for lang,text in texts.items()}
        review["sources"][0]["kind"] = "official-protocol"
        review["evidence_mode"] = "protocol-only"
        review["non_numeric_reason"] = {lang: "No empirical numerical results verified." for lang in ("zh", "en")}
        review["blocks"] = [b for b in review["blocks"] if b["kind"] != "quantitative"]
        for lang in texts:
            start=texts[lang].index("<!-- EVIDENCE:results:START -->")
            end=texts[lang].index("<!-- EVIDENCE:results:END -->")+len("<!-- EVIDENCE:results:END -->")
            texts[lang] = texts[lang][:start] + texts[lang][end:]
            texts[lang] = texts[lang].replace("Primary protocol reviewed.", "Primary protocol reviewed. No empirical numerical results verified.")
        self.assertEqual([], errors(texts, review))

    def test_partial_review_requires_visible_gap(self):
        texts, review = example()
        review["status"] = "partial"
        self.assertTrue(any("gap" in e for e in errors(texts, review)))

    def test_invisible_comments_cannot_supply_missing_conditions(self):
        texts, review = example()
        texts["zh"] = texts["zh"].replace("Dataset D; Reader A; top-5.", "<!-- Dataset D; Reader A; top-5. -->")
        self.assertTrue(any("conditions" in e for e in errors(texts, review)))

    def test_localized_non_entity_row_labels_keep_numeric_binding(self):
        texts, review = example()
        review["blocks"][3]["row_labels"] = {"zh": {"A": "直接证据", "B": "检索证据"}, "en": {"A": "A", "B": "B"}}
        texts["zh"] = texts["zh"].replace("| A |", "| 直接证据 |").replace("| B |", "| 检索证据 |")
        self.assertEqual([], errors(texts, review))

    def test_unreviewed_legacy_is_backlog_and_any_edit_needs_review(self):
        texts, _ = example()
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root/"data").mkdir(); (root/"benchmarks").mkdir()
            for lang,suffix in (("zh", ""), ("en", ".en")):
                (root/"benchmarks"/f"example{suffix}.md").write_text(texts[lang])
            state={"schema_version":1,"legacy_baseline":{"example":{lang:note_hash(text) for lang,text in texts.items()}},"reviews":{}}
            (root/"data/note-evidence.json").write_text(json.dumps(state))
            self.assertEqual(([], ["example"]), validate_evidence_state([{"id":"example"}],root))
            (root/"benchmarks/example.md").write_text(texts["zh"]+"Changed claim.")
            found,_=validate_evidence_state([{"id":"example"}],root)
            self.assertTrue(any("needs a source-reading" in e for e in found))

    def test_legacy_baseline_cannot_be_rewritten_to_hide_edits(self):
        data=json.loads((ROOT/"data/note-evidence.json").read_text())
        digest=hashlib.sha256(json.dumps(data["legacy_baseline"],sort_keys=True,separators=(",",":")).encode()).hexdigest()
        self.assertEqual("b499dfec4e50dd18e32a1cc09dd226bc9c2cec09e7dacadd84fcb87888159bff",digest)
        self.assertEqual("baa003e6b845a5facefe28828f260203c9029e5a",data["legacy_baseline_commit"])

    def test_repository_notes_match_recorded_coverage(self):
        records=json.loads((ROOT/"data/benchmarks.json").read_text())
        found, _ = validate_evidence_state(records, ROOT)
        self.assertEqual([], found)

if __name__ == "__main__":
    unittest.main()
