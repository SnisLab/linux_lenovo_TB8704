# Priorisierte nächste Kernel-Arbeitstickets

Stand: 2026-10-15. Dies sind Folgearbeits-Empfehlungen; keine Änderungen,
Diagnoseexperimente, Builds oder Gerätetests wurden im Rahmen dieses Plans
ausgeführt. Evidenzbasis: `state/current-status.md`,
`mainline/build/m612cw/report.md`, `mainline/build/m612de/report.md` und
`docs/tb8704/m6.12-handoff-status.md`.

Die Recovery-Statusdatei `recovery/src/android_recovery_lenovo_TB8704/docs/status.md`
ist im isolierten Worktree nicht vorhanden. Die Recovery-Freigabe ist deshalb
hier **nicht bestätigt**. Vor jedem Gerätetest muss der Owner den unabhängigen,
für genau dieses Gerät getesteten Rettungsweg schriftlich bestätigen.

## Gemeinsamer Ablauf und Sicherheitsgrenzen

Für spätere Implementierungen sind vorhandene Kernel-, Recovery- und
Android-Docker-Build-Container sowie Skripte und Toolchains wiederzuverwenden;
ADB/Fastboot stehen im Ubuntu-26.04-LXC bereit. Build-Skripte müssen den
isolierten LoopTroop-Worktree explizit als Quellmount und Arbeitsverzeichnis
verwenden. Vor/nach Build Quelle, Host- und Containerpfad, Git-HEAD, Dirty-Diff,
Konfiguration, Skriptargumente, Toolchain, Log und Artefakthashes erfassen.
Build-Abbruch, falls Quellpfad oder Quellcommit im Container nicht eindeutig
dem Worktree zuzuordnen ist. Keine Toolchain installieren und keine fremden
Checkout-/Ausgabedateien überschreiben.

Gerätezyklus für ein später separat freigegebenes Ticket: Codeänderung →
Docker-Build → Boot-Image-Erstellung → Artefakt-/Hashprüfung → kontrollierter
ADB/Fastboot-Test → Rohlog-/pstore-Sicherung und Zuordnung zu Build, Commit,
Lauf-ID. Zunächst nur nichtdestruktive Inspektion und temporäres `fastboot boot`.
Flashen bleibt gesperrt, bis ein Mensch Zielpartition, Artefakthash,
Backup-/Wiederherstellungsweg und Zeitfenster ausdrücklich freigegeben hat.
Bootloader/Firmware nie überschreiben; nicht entsperren, löschen, formatieren,
partitionieren oder ungeprüfte Daten schreiben. Zeitlimits: Hand-off 120 s,
frühe Konsole 180 s, Diagnoseshell 300 s; danach keine automatische
Wiederholung, einmal kontrolliert in den bestätigten Recovery-Pfad zurück.
Abbruch und menschliche Hilfe bei Offline-/mehrdeutigem Gerät, unerwartetem
Reset, Recovery-Verlust, Strom-/Temperaturauffälligkeit oder nicht erklärtem
Schreibzugriff. Logs sichern, wo möglich, und Gerätekennungen redigieren.

## P0 — Rettungsweg und Geräteschranke bestätigen

- **Ziel/Befund/Vertrauen:** Bootpfad bleibt ungeklärt; der Handoff-Bericht
  erlaubt nur nichtdestruktive Inspektion/temporäres Booten und verbietet
  persistente Modifikation. Kein Recovery-Ergebnis liegt hier vor. Vertrauen:
  hoch für dokumentierte Grenzen, keine Aussage zur Recovery-Wirksamkeit.
- **Komponenten:** TWRP 12.1/8.1, ADB/Fastboot, Rückkehr zu Android.
- **Abhängigkeiten:** Recovery-Bewertung `assess-recovery-readiness`; vor allen
  Gerätetickets.
- **Voraussetzungen:** Recovery-Owner liefert versionsbezogenen Boot- und
  Rückkehrnachweis, Prüfsummen und schriftliche Freigabe; Geräte-Owner bestätigt
  Identität und zulässige Aktionen.
- **Änderung/Diagnose:** ausschließlich Status-/Freigabedokumentation ergänzen;
  keine Recoveryänderung.
- **Risiko:** Rettungsweg nur angenommen, falsches Gerät oder nicht erreichbare
  Recovery.
- **Validierung:** zunächst Dokument-/Hashprüfung, ggf. separat freigegebene
  lesende ADB/Fastboot-Identifikation.
- **Erwartete Belege:** Recovery-Version/Commit, Artefakthash, datierter
  tatsächlicher Wiederherstellungsnachweis, Owner-Freigabe.
- **Erfolg:** unabhängige Rückkehroption ist am TB-8704F belegt und schriftlich
  freigegeben. **Abbruch/Rückfall:** Nachweis fehlt oder weicht ab → keinerlei
  Gerätetest, unveränderte bestehende Recovery erhalten.
- **Menschliche Freigabe:** Recovery-Owner und Geräte-Owner zwingend.

## P1 — ARM64 Loader-/Image-/DTB-Handoff belegen

- **Ziel/Befund/Vertrauen:** Historische Kerneladresse `0x80008000` ist bei
  `text_offset=0` nicht 2-MiB-ausgerichtet; Ramdisk-Überlappung ist möglich,
  falls Adressen literal sind. Loaderverhalten ist unbekannt. `Image.gz` ist
  gzip-`Image`, kein selbstentpackendes zImage. Vertrauen hoch für statische
  Fakten, niedrig für tatsächliche Loader-Interpretation.
- **Komponenten:** ARM64 Kernel, Bootheader, Loader, DTB, initramfs.
- **Abhängigkeiten:** P0 für jedes Gerät; zunächst rein offline.
- **Voraussetzungen:** Originalartefakt und Loadervertrag/-quelle; vorhandene
  Analysewerkzeuge aus den Docker-Umgebungen.
- **Diagnose (nicht ausgeführt):** Bootartefakt offline zerlegen, Header,
  Offsets, Ausrichtung und Überlappungen erfassen; Handoff-Kontrakt aus
  belastbarer Quelle bestimmen.
- **Hypothese/Erwartung:** historische Adresswerte sind kein nachgewiesener
  finaler Platzierungsvertrag; verlässlicher Loaderbeleg liefert gültige
  Kernel-/DTB-/initrd-Übergabe.
- **Testmethode/Logs:** reproduzierbare Header-/Offset-Analyse, Hashmanifest;
  erwartete Signaturen: konsistente Headerfelder, nicht überlappende gültige
  Bereiche und belegte Übergabe-Semantik.
- **Risiko:** geratenes Layout kann nicht bootfähiges Image erzeugen.
- **Validierung/Belege:** Quellartefakt-Hash, Toolversion, Ergebnis und
  referenzierter Loaderbeleg. Erfolg: kein ungeklärter Adress-/Übergabepunkt.
- **Abbruch/Rückfall:** Spezifikation fehlt → kein Kandidatenpaket booten,
  Annahmen als offen dokumentieren.
- **Menschliche Freigabe:** Owner genehmigt Handoff und jeden späteren
  temporären Boot explizit.

## P2 — Reproduzierbarer Build aus isoliertem Worktree

- **Ziel/Befund/Vertrauen:** Teil-DTS besteht, aber M6.12de-Build/Init ist nicht
  belegt; DTS ist ausdrücklich unvollständig. Vertrauen hoch.
- **Komponenten:** Linux 6.12, TB-DTS/DTB, existierende Kernel-Docker-Umgebung,
  Build- und Boot-Image-Skripte.
- **Abhängigkeiten:** P0; P1 vor Gerätetest/Paketübergabe.
- **Voraussetzungen:** vorhandene Container und Skripte lesen und
  Worktree-Mount, Arbeitsverzeichnis, Output-Pfad und Cache-Verhalten belegen.
- **Änderung:** separates Umsetzungsticket für Worktree-aware Skriptaufruf,
  isolierte Ausgabe und Hashmanifest; hier kein Build und kein Boot.
- **Risiko:** falscher Checkout oder Cache wird kompiliert, fremde Dateien
  überschrieben.
- **Validierung:** prüfen, dass Containerpfad/HEAD/Dirty-Diff dem Host-Worktree
  entsprechen und Buildlog/DTB/Image-Hashes dieser Quelle zugeordnet sind.
- **Erwartete Belege:** strukturierte Skriptargumente, Container/Toolchain,
  Pfad, Commit, Konfiguration, Log und Artefakthashes.
- **Erfolg:** reproduzierbarer Build aus genau diesem Worktree ohne
  Seiteneffekte außerhalb isolierter Ausgabe. **Abbruch/Rückfall:** unklarer
  Quellpfad oder nicht isolierbare Ausgabe → stoppen, keine Geräteartefakte.
- **Menschliche Freigabe:** Maintainer für Skript-/Outputänderung; getrennte
  Gerätefreigabe bleibt erforderlich.

## P3 — Frühe UART-Konsole und drei unabhängige Diagnoseshell-Boots

- **Ziel/Befund/Vertrauen:** UART ist beschrieben, nicht am Gerät bestätigt;
  historische Linux-Eintritts-/`/system`-/second-stage-Aussagen sind nur
  sekundär referenziert. Vertrauen hoch für Lücke, mittel für historische
  Aussagen.
- **Komponenten:** UART/Pinmux, minimales DT, ARM64-Handoff, Diagnose-initramfs,
  pstore.
- **Abhängigkeiten:** P0–P2; P4 erst danach.
- **Voraussetzungen:** bestätigter Rettungsweg, Handoff-Vertrag, exakte
  Artefakthashes, geprüfte serielle Verbindung und individuelle Freigabe pro
  temporärem Boot.
- **Diagnose (nicht ausgeführt):** minimales Diagnoseimage ohne unnötige
  Peripherie temporär starten und interaktive Shell erreichen.
- **Hypothese/Erwartung:** UART meldet frühe Kernelinitialisierung und
  initramfs erreicht kontrolliert eine Shell.
- **Testmethode/Logsignaturen:** drei unabhängige Kaltstart-/Neuinitialisierungs-
  Läufe mit Lauf-ID, Build/Commit-Zuordnung, Roh-UART- und Hostlogs; nach
  `Booting Linux`, UART-Probe, `Run /init`/Prompt, Panic/Oops, Watchdog und
  Resetgrund suchen. pstore pro Lauf sichern.
- **Risiko:** Handofffehler, Reset, fehlender Rettungsweg.
- **Validierung/Belege:** zuerst Offline-Paketprüfung, einzeln freigegebene
  temporäre Läufe, Logs/Hashes/Hostereignisse; Zeitlimits 120/180/300 s wie oben.
- **Erfolg/Stabilität:** drei von drei unabhängigen Läufen erreichen die
  interaktive Shell. Fehler separat zählen: jeder Panic/Oops, Watchdog,
  spontaner Reset, Datenkorruption, Strom-/Temperaturproblem oder
  Handoff-/DTB-Verlust ist kritisch und lässt das Gate scheitern, selbst wenn
  andere Läufe erfolgreich sind. Nichtkritische Warnungen mit Häufigkeit und
  Wirkung bewerten; keine Aggregation, die Einzelfehler verschleiert.
- **Abbruch/Rückfall:** erster unerwarteter Reset, Schreibzugriff oder
  Recoveryproblem stoppt die Serie; einmal kontrolliert zur bestätigten
  Recovery, keine automatischen Wiederholungen.
- **Menschliche Freigabe:** Geräte-Owner pro Lauf; niemals Flashen in diesem
  Ticket.

## P4 — eMMC-Probe und ausschließlich lesender Zugriff

- **Ziel/Befund/Vertrauen:** SDHC1/Versorgungen im DTS, aber Linux-Probe und
  I/O unbekannt; Android `/system` am Controller ist nur sekundär berichtet.
  Vertrauen hoch für DTS, mittel für historische Laufzeitaussage.
- **Komponenten:** SDHC1/eMMC, Regulatoren, Blockgerät, initramfs.
- **Abhängigkeiten:** P0–P3; Root-/Partitionspolicy dokumentiert.
- **Voraussetzungen:** drei stabile Shellboots, unveränderte Partitionstabelle,
  read-only-Verfahren und Owner-Freigabe.
- **Änderung/Diagnose:** zunächst Diagnose ohne Schreibzugriff; DTS-/Treiber-
  Änderung nur als separates Ticket mit konkretem Probe-Befund.
- **Risiko:** falsche Spannung/Zuordnung, Storage-Schaden.
- **Validierung:** Probe-Logs und Blockgerätekennung, ausschließlich
  freigegebene read-only Abfragen/Mount `ro`; keine fsck-/Schreibtests.
- **Erwartete Belege:** SDHCI-/Regulator-Probezeilen, Größe/Zuordnung,
  Mountoptionen und Fehlerlogs.
- **Erfolg:** reproduzierbare Erkennung in drei Boots und read-only Zugriff
  ohne I/O-Fehler. **Abbruch/Rückfall:** jeder Schreibintent, I/O-Fehler oder
  unerwartete Partition stoppt; keine automatische Reparatur.
- **Menschliche Freigabe:** Owner genehmigt konkret Gerät und Partitionen;
  jeder Schreibtest ist ein neues Ticket mit separater Freigabe.

## P5 — Je ein einzelnes, hardwarebelegtes Peripherie-Ticket

- **Ziel/Befund/Vertrauen:** Display, Goodix-Touch, USB/VBUS, Funk, Audio,
  Akku/Laden und Suspend sind nicht getestet/unbekannt. Referenzgeräte belegen
  keine TB-8704F-Gleichheit. Vertrauen hoch für Evidenzlücke.
- **Komponenten:** je eigenes Ticket für exakt identifiziertes Bauteil; keine
  Bündelung unabhängiger Subsysteme.
- **Abhängigkeiten:** P0–P3 sowie jeweilige Bus-/Regulatorvoraussetzungen.
- **Voraussetzungen:** TB-spezifischer Bauteil-/Pin-/Spannungsbeleg und
  passendes Upstream-Binding; keine Aktivierung aus ähnlichem DT-Namen.
- **Änderung/Diagnose:** erst DT-/Treiber-Probe, danach separat messbarer
  Funktionsschritt; Diagnoseexperimente vor Ausführung ausdrücklich als
  Empfehlung belassen.
- **Risiko:** falsche Pins/Spannung, Hardwarebelastung oder Bootregression.
- **Validierung:** Binding-/Buildprüfung, eine Änderung pro Ticket, Vorher-/
  Nachher-Logs und kontrollierter Rückfall auf vorheriges temporäres Image.
- **Erwartete Belege:** Hardwarequelle, Commit/DT-Diff, Probe-/Funktionslogs,
  Fehlerbilder und gemessene Akzeptanzwerte.
- **Erfolg:** nur die konkrete TB-Funktion wird belegt; Boot-Stabilitätskriterien
  bleiben erfüllt. **Abbruch/Rückfall:** kritischer Fehler oder elektrische
  Auffälligkeit → Komponente deaktivieren, vorheriges Image nutzen, stoppen.
- **Menschliche Freigabe:** pro Subsystem; elektrische Tests zusätzlich durch
  Hardware-Owner.
