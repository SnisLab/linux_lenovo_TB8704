# M6.12cw — Laufzeitstatus und Komponentenmatrix

## Quellenstand

Die frühere, ausführliche M6.12cw-Berichtsdatei sowie das referenzierte
`state/current-status.md` waren im Checkout nicht vorhanden. Die einzige
erhaltene Zusammenfassung steht in `README.tb8704.md` (Abschnitt
„Status and provenance“): Linux 6.12-Eintritt, read-only `/system`-Mount und
Android second-stage init seien erreicht worden. Diese Angaben sind hier als
sekundär referenzierte Laufzeit-Evidenz erfasst. Original-Logs, Testschritte,
Build-Konfiguration und Geräteidentifikation sind nicht verfügbar; keine
weiteren Resultate werden daraus abgeleitet.

## Befunde

| Komponente | SoC-Unterstützung | Build/Konfiguration | Initialisierung | TB-8704F-Laufzeit | Status | Evidenzklasse | Belegte Funktion | Einschränkung / zulässige Schlussfolgerung | Quelle; Vertrauen |
|---|---|---|---|---|---|---|---|---|---|
| Kernelstart | MSM8953-Support im 6.12-Baum | Builddetails in diesem Bericht nicht erhalten | Linux 6.12 wurde laut README erreicht | Linux-Eintritt berichtet | teilweise funktionsfähig | Laufzeit (sekundär) | Kontrollübergabe an Linux und Eintritt | Kein Nachweis für stabilen Betrieb oder vollständigen Userspace; kein Original-Log vorhanden | `README.tb8704.md`, Statusabschnitt; Vertrauen mittel |
| `/system` | keine SoC-spezifische Aussage | Mountkonfiguration unbekannt | Mount berichtet | read-only-Mount berichtet | Laufzeit erfolgreich bestätigt | Laufzeit (sekundär) | `/system` read-only gemountet | Nicht auf Schreibzugriff, weitere Partitionen oder vollständigen Android-Start verallgemeinern | `README.tb8704.md`; Vertrauen mittel |
| Android second-stage init | keine SoC-spezifische Aussage | initramfs-/Bootparameter-Evidenz fehlt | second stage berichtet gestartet | Laufzeitstart berichtet | Laufzeit erfolgreich bestätigt | Laufzeit (sekundär) | Android second-stage init startet | Kein Framework/UI, spätere Vendor-Mounts oder vollständige Initialisierung belegt | `README.tb8704.md`; Vertrauen mittel |
| Framework/UI | nicht einschlägig | unbekannt | nicht belegt | ausdrücklich nicht nachgewiesen | nicht getestet | Negativabgrenzung des Berichts | keine bestätigte Funktion | Nicht als Fehler einstufen: kein dokumentierter Fehlversuch | `README.tb8704.md`; Vertrauen mittel |
| Spätere Vendor-Mounts | nicht einschlägig | unbekannt | nicht belegt | ausdrücklich nicht nachgewiesen | nicht getestet | Negativabgrenzung des Berichts | keine bestätigte Funktion | Keine Aussage über Ursache oder Fehlerzustand | `README.tb8704.md`; Vertrauen mittel |
| Reboot-Ursache | nicht einschlägig | unbekannt | unbekannt | Ursache ausdrücklich offen | unbekannt | fehlende Evidenz | keine | Nicht als fehlerhaft klassifizieren, solange Ursache/Fehlerbeleg fehlt | `README.tb8704.md`; Vertrauen mittel |

## Klassifikationsschlüssel

Verwendete zulässige Statuskategorien sind exakt: **Laufzeit erfolgreich
bestätigt**, **teilweise funktionsfähig**, **nur Build oder Initialisierung
bestätigt**, **nicht getestet**, **fehlerhaft**, **unbekannt**. Der überlieferte
M6.12cw-Text belegt keinen dokumentierten Komponentenfehler. Build-Erfolg und
Fastboot-Annahme dürfen nicht als Laufzeitnachweis gewertet werden.
