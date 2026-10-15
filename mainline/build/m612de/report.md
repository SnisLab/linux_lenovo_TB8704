# M6.12de — Build- und Initialisierungsbericht

## Quellenstand

Für M6.12de liegt im Checkout kein Build-Log, Konfigurationsfragment,
Initialisierungs-Log oder ursprünglicher Bericht vor. Daher werden keine
Ergebnisse aus dem Namen des Meilensteins, aus einem DT-Knoten oder aus
allgemeiner MSM8953-Unterstützung abgeleitet. Die verfügbare Gerätebasis ist
Linux 6.12 mit Teil-DTS; siehe `docs/tb8704/mainline-baseline.md` und
`arch/arm64/boot/dts/qcom/apq8053-lenovo-tb8704f.dts`.

## Komponentenmatrix

| Komponente | SoC-Unterstützung | Build-/Konfigurationsevidenz | Initialisierungsevidenz | TB-8704F-Laufzeitevidenz | Status | Evidenzklasse | Belegte Funktion | Einschränkung / zulässige Schlussfolgerung | Quelle; Vertrauen |
|---|---|---|---|---|---|---|---|---|---|
| Linux 6.12-Arbeitsbasis | MSM8953-Integration vorhanden | Versionsbasis und gepinnter Upstream-Stand dokumentiert; kein M6.12de Buildbeleg | nicht für M6.12de dokumentiert | keine M6.12de-Evidenz | unbekannt | Provenienz, keine Build-Evidenz | Quellbasis identifiziert | Quellenstand beweist keinen M6.12de-Build oder Geräteboot | `docs/tb8704/mainline-baseline.md`; Vertrauen hoch |
| TB-8704F DTS | SoC-Basis ist `msm8953.dtsi` | Teil-DTS im Baum; Ziel-DTB-Build nicht für M6.12de belegt | keine | keine | unbekannt | DT-Quelltext | Boardidentität, Konsole, Taste, Regler, SDHC teilweise beschrieben | Vorhandener DTS-Quelltext beweist weder erfolgreiche Kompilierung noch Probe/Funktion | `arch/arm64/boot/dts/qcom/apq8053-lenovo-tb8704f.dts`; Vertrauen hoch für Inhalt |
| UART-Konsole | UART-Treiberbestand im SoC-Baum | DTS setzt `uart_0` auf `okay` | keine M6.12de Init-Logs | keine | unbekannt | DT/Konfiguration | UART-Konfiguration vorhanden | Keine Aussage über Konsole bei Build oder Laufzeit | DTS:37-43,66-71; Vertrauen hoch |
| SDHC/eMMC | SDHC-Treiberbestand im SoC-Baum | `sdhc_1`-Knoten samt Versorgungen im DTS | keine M6.12de Init-Logs | keine | unbekannt | DT/Konfiguration | SDHC wird beschrieben | Kein Compile-, Probe- oder Block-I/O-Nachweis | DTS:97-102; Vertrauen hoch |
| PMIC-Regler | PM8953/PMI8950-Basis eingebunden | RPM-Reglerbeschreibung in DTS | keine M6.12de Init-Logs | keine | unbekannt | DT/Konfiguration | begrenzte Reglerdeklarationen vorhanden | Keine Aussage über korrekte Spannungen oder Verbraucherfunktion | DTS:14-17,73-95; Vertrauen hoch |
| Display, Touch, USB, Funk, Audio, GPU, Akku/Laden, Suspend | SoC-Support je nach Subsystem im Kernelbaum | kein M6.12de gerätespezifischer Buildbeleg | keine | keine | nicht getestet | Quellenprüfung | keine TB-spezifische Funktion belegt | Fehlende Evidenz ist weder Funktions- noch Fehlernachweis | Teil-DTS und Baseline; Vertrauen hoch |

## Statuskategorien

Dieser Bericht verwendet ausschließlich die Kategorien **Laufzeit erfolgreich
bestätigt**, **teilweise funktionsfähig**, **nur Build oder Initialisierung
bestätigt**, **nicht getestet**, **fehlerhaft** und **unbekannt**. Derzeit ist
für M6.12de keine gerätespezifische Build- oder Initialisierungsaussage
hinreichend belegt; unbekannte Befunde sind nicht als Fehler klassifiziert.
