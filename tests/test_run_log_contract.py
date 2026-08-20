from pathlib import Path
import subprocess
import sys
import tempfile
import unittest


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import validate_reading


class NoPublicRunLogContractTest(unittest.TestCase):
    def test_repository_has_no_public_daily_run_files(self):
        errors = validate_reading.validate_no_public_run_files(
            validate_reading.PUBLIC_OPERATIONAL_RUN_PATHS
        )
        self.assertEqual([], errors)

    def test_any_file_under_public_run_path_is_rejected(self):
        with tempfile.TemporaryDirectory() as temporary_directory:
            public_path = Path(temporary_directory) / "daily"
            forbidden = public_path / "2026" / "08" / "21.md"
            forbidden.parent.mkdir(parents=True)
            forbidden.write_text("# Operational state\n", encoding="utf-8")
            errors = validate_reading.validate_no_public_run_files((public_path,))
        self.assertTrue(any(str(forbidden) in error for error in errors), errors)

    def test_public_run_path_cannot_itself_be_a_file(self):
        with tempfile.TemporaryDirectory() as temporary_directory:
            forbidden = Path(temporary_directory) / "daily"
            forbidden.write_text("# Operational state\n", encoding="utf-8")
            errors = validate_reading.validate_no_public_run_files((forbidden,))
        self.assertTrue(any(str(forbidden) in error for error in errors), errors)

    def test_broken_symlink_cannot_hide_a_public_run_artifact(self):
        with tempfile.TemporaryDirectory() as temporary_directory:
            public_path = Path(temporary_directory) / "daily"
            public_path.mkdir()
            forbidden = public_path / "latest.md"
            forbidden.symlink_to(public_path / "missing.md")
            errors = validate_reading.validate_no_public_run_files((public_path,))
        self.assertTrue(any(str(forbidden) in error for error in errors), errors)

    def test_private_run_state_directory_is_git_ignored(self):
        result = subprocess.run(
            ["git", "check-ignore", ".radar-private/runs/example.json"],
            cwd=ROOT,
            text=True,
            capture_output=True,
            check=False,
        )
        self.assertEqual(0, result.returncode, result.stderr)

    def test_static_policy_and_authoritative_guidance_share_boundary(self):
        policy = (ROOT / "runs" / "README.md").read_text(encoding="utf-8")
        self.assertIn("No public operational run logs", policy)
        self.assertIn("static policy", policy.lower())
        self.assertIn(".radar-private", policy)
        self.assertNotIn("Daily maintenance logs live", policy)

        documents = (
            ROOT / "docs" / "RADAR_AGENT_PROTOCOL.md",
            ROOT / "docs" / "DAILY_WORKFLOW.md",
            ROOT / "docs" / "BILINGUAL_PUBLICATION.md",
            ROOT / "docs" / "RADAR_FAMILY.md",
            ROOT
            / "docs"
            / "superpowers"
            / "specs"
            / "2026-08-20-agent-maintained-time-first-radar-v2-design.md",
            ROOT
            / "docs"
            / "superpowers"
            / "specs"
            / "2026-08-20-research-radar-reading-architecture-v1-design.md",
        )
        stale_directions = (
            "Write one run log",
            "and the run log",
            "and one run log",
            "→ log →",
            "Validation and run log",
            "`runs/*` remain single-source",
        )
        for path in documents:
            text = path.read_text(encoding="utf-8")
            with self.subTest(path=path.relative_to(ROOT)):
                self.assertIn("No public operational run logs", text)
                self.assertIn(".radar-private", text)
                for stale in stale_directions:
                    self.assertNotIn(stale, text)


if __name__ == "__main__":
    unittest.main()
