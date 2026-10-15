"""Regression checks for the KERN-1 development-status deliverable."""

from pathlib import Path
import unittest


REPORT = Path(__file__).resolve().parents[1] / "docs/TB8704F-DEVELOPMENT-STATUS.md"


class DevelopmentStatusReportTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.text = REPORT.read_text(encoding="utf-8")

    def test_required_deliverables_and_decisions_are_present(self):
        required = (
            "## Zusammenfassung",
            "## Technische Projektübersicht und Grenzen",
            "## Chronologie und Branchvergleich",
            "## Evidenz- und Belegmatrix",
            "## Recoverybewertung",
            "## Offene Probleme und priorisierte Folgearbeiten",
            "## Kernelroadmap",
            "## Android-16-Bewertung",
            "## Nicht erreichbare Informationsquellen und Vollständigkeitsauswirkung",
            "Ampel: GELB",
            "Unmittelbar nächste Schritte",
            "mindestens drei",
            "9ce1a245",
            "ARM64",
            "Loaderdekompression",
        )
        for item in required:
            with self.subTest(item=item):
                self.assertIn(item, self.text)

    def test_diagnostic_branches_and_evidence_limits_are_documented(self):
        branches = (
            "diag/m6.12-pinctrl-checkpoints",
            "diag/m6.12-pinctrl-mmio-checkpoints",
            "diag/m6.12-pinctrl-no-get-direction",
            "diag/m5.12-par-text",
            "diag/m5.13-pte-walk",
            "diag/m5.14-nofault-pgwalk",
            "diag/m5.14d-nofault-pgwalk",
            "diag/m5.14i-return-only-helper",
        )
        for branch in branches:
            with self.subTest(branch=branch):
                self.assertIn(branch, self.text)
        self.assertIn("GPIO135", self.text)
        self.assertIn("0x87000", self.text)
        self.assertIn("Ursache", self.text)
        self.assertIn("nicht bootfähig", self.text)

    def test_sources_are_distinguished_by_provenance(self):
        self.assertIn("Quellenkonvention", self.text)
        self.assertIn("Extern (Projektquelle", self.text)
        self.assertIn("Kernel-Git", self.text)
        self.assertIn("nicht erreichbar", self.text)

    def test_status_categories_and_android_targets_are_distinguished(self):
        for status in (
            "Laufzeit erfolgreich bestätigt",
            "teilweise funktionsfähig",
            "nur Build oder Initialisierung bestätigt",
            "nicht getestet",
            "fehlerhaft",
            "unbekannt",
        ):
            with self.subTest(status=status):
                self.assertIn(status, self.text)
        self.assertIn("AOSP Android 16", self.text)
        self.assertIn("PixelOS", self.text)
        self.assertIn("Android second-stage init", self.text)
        self.assertIn("Framework/UI", self.text)

    def test_recovery_readiness_and_actionable_plan_are_evidenced(self):
        for evidence in (
            "TWRP 12.1",
            "TWRP 3.7.0_9-0",
            "FDE",
            "Recovery-only-Restore",
            "menschliche Freigabe",
            "Abbruch",
            "Erfolgskriterien",
        ):
            with self.subTest(evidence=evidence):
                self.assertIn(evidence, self.text)

    def test_chronology_distinguishes_baseline_ticket_base_and_current_head(self):
        self.assertIn("Historische Projektbaseline `62969f1eb5e42e596760924c0845bfdb384851d9`", self.text)
        self.assertIn("KERN-1-Ausgangscommit `9ce1a2452913170159c00d439d02dced337610c6`", self.text)
        self.assertIn("Historische Projektbaseline: `62969f1eb5e42e596760924c0845bfdb384851d9`", self.text)
        self.assertIn("Historischer KERN-1-Ausgangscommit: `9ce1a2452913170159c00d439d02dced337610c6`", self.text)
        self.assertIn("Letzter gesicherter KERN-1-Ticketstand nach Manual QA v3: `ad16c232750a8b03970b5d610d527a14c528fcab`", self.text)
        self.assertNotRegex(self.text, r"62969f1[^\n]*KERN-1-(?:Ausgangs)?basis")

    def test_provenance_convention_avoids_absolute_machine_paths(self):
        self.assertIn("Extern (Projektquelle; Mainline-Projektwurzel)", self.text)
        self.assertIn("Extern (Projektquelle; Recovery-Projektwurzel)", self.text)
        self.assertNotRegex(self.text, r"/work/tb8704f(?:/|\b)")
        self.assertNotRegex(self.text, r"/restore(?:/|\b)")
        self.assertNotRegex(self.text, r"/tb8704f(?:/|\b)")


if __name__ == "__main__":
    unittest.main()
