# TB-8704F Linux-Status und Komponentenmatrix

Stand: 2026-10-15. Dieses Dokument trennt SoC-Unterstützung, Build-/DT-Evidenz,
Initialisierung und direkte TB-8704F-Laufzeitevidenz. Ein vorhandener Treiber,
Konfigurationseintrag oder DT-Knoten ist kein Nachweis für Gerätefunktion.

## Statusdefinitionen

- **Laufzeit erfolgreich bestätigt**: direkte, reproduzierbar dokumentierte
  TB-8704F-Laufzeitbeobachtung belegt die genannte Funktion.
- **teilweise funktionsfähig**: direkte Laufzeitbeobachtung belegt einen Teil,
  aber nicht den vollständigen Funktionsumfang.
- **nur Build oder Initialisierung bestätigt**: Build oder erfolgreiche
  Initialisierung ist belegt; Gerätefunktion ist nicht nachgewiesen.
- **nicht getestet**: Teststatus ist ausdrücklich nicht erhoben/dokumentiert.
- **fehlerhaft**: direkte Evidenz dokumentiert ein Fehlverhalten.
- **unbekannt**: ausreichende Evidenz zur Einordnung fehlt.

Vertrauensgrad bezieht sich auf die belegte Aussage, nicht auf vermutete
Funktion. Quellen verweisen auf versionierte Dateien/Commits dieses Baums.

## Komponentenmatrix

| Komponente | SoC-Unterstützung | Build-/Konfigurationsevidenz | Initialisierungsevidenz | TB-8704F-Laufzeitevidenz | Status | Evidenzklasse | Belegte Funktion | Einschränkungen / zulässige Schlussfolgerung | Quelle; Vertrauen |
|---|---|---|---|---|---|---|---|---|---|
| Linux-Boot / Kernel | MSM8953-Unterstützung im 6.12-Arbeitsbaum; board-spezifischer Bootpfad ist separat | Arbeitsbaum und Teil-DTS vorhanden | Linux-6.12-Eintritt im historischen Laufzeitbericht erwähnt | Eintritt auf Gerät dokumentiert | teilweise funktionsfähig | Laufzeit | Kernel erreicht Linux | Kein Nachweis für vollständigen Boot, stabile Laufzeit oder alle Peripheriegeräte | `README.tb8704.md`; `mainline/build/m612cw/report.md` (letzterer fehlt im Checkout); Vertrauen mittel, Einzelaussage sekundär referenziert |
| `/system`-Mount | generisch verfügbar; kein TB-spezifischer SoC-Befund | Bericht erwähnt den Mount | read-only-Mount im Bericht vermerkt | read-only `/system` auf Gerät belegt | Laufzeit erfolgreich bestätigt | Laufzeit | read-only `/system`-Mount | Keine Aussage zu weiteren Partitionen, Schreibzugriff oder vollständiger Android-Userspace-Funktion | `README.tb8704.md`; `mainline/build/m612cw/report.md` fehlt; Vertrauen mittel |
| Android second-stage init | nicht SoC-spezifisch | Bericht erwähnt Android-Init | Start der second stage berichtet | Start auf Gerät belegt | Laufzeit erfolgreich bestätigt | Laufzeit | Android second-stage init startet | Kein Nachweis für Framework/UI, spätere Vendor-Mounts oder vollständigen Systemstart | `README.tb8704.md`; `mainline/build/m612cw/report.md` fehlt; Vertrauen mittel |
| eMMC / SDHC | MSM8953 SDHC-Controller-Unterstützung vorhanden | `&sdhc_1` und Spannungsversorgungen im TB-DTS; Buildbericht dieser Revision fehlt | nicht dokumentiert | keine direkte TB-8704F-Evidenz im vorliegenden Statusmaterial | unbekannt | DT/Konfiguration | DT beschreibt einen SDHC-Controller | Knoten und Versorgungseinträge beweisen weder Build noch Erkennung oder I/O | `arch/arm64/boot/dts/qcom/apq8053-lenovo-tb8704f.dts:97-102`; Vertrauen hoch für DT, keine Funktionsaussage |
| UART-Konsole | MSM8953 UART-Treiber im Kernelbaum | `uart_0` als `okay`, stdout-path 115200n8 | keine gerätespezifischen Init-Logs vorliegend | keine direkte TB-Laufzeitevidenz dokumentiert | unbekannt | DT/Konfiguration | Konsole ist beschrieben | Kein Nachweis von Signal, Pinmux, Ausgabe oder Empfang | DTS:38-43,66-71; Vertrauen hoch für Beschreibung |
| GPIO Volume-Up | TLMM/GPIO-Key Infrastruktur im Baum | GPIO 85 und KEY_VOLUMEUP im DTS beschrieben | keine | keine direkte Laufzeitevidenz | unbekannt | DT/Konfiguration | Taste ist beschrieben | Elektrische Polarität/Pinbelegung und Eingabeereignis nicht am Gerät bestätigt | DTS:45-56; Vertrauen hoch für DT, niedrig für Hardwarezuordnung |
| Ramoops / pstore | generische ramoops-Unterstützung verfügbar | reservierter Bereich und ramoops-Knoten beschrieben | nicht dokumentiert | keine Laufzeit-/Persistenzprüfung | unbekannt | DT/Konfiguration | Speicherbereich ist deklariert | Kein Nachweis, dass Firmware den Bereich freihält oder pstore Daten schreibt/liest | DTS:26-35; Vertrauen hoch für Beschreibung |
| Display / DSI | MSM8953-SoC-Infrastruktur verfügbar | TB-Panel-/DSI-Beschreibung in Teil-DTS nicht enthalten | nicht dokumentiert | nicht dokumentiert | nicht getestet | SoC/DT-Abgleich | keine TB-spezifische Funktion belegt | SoC-Unterstützung ist keine Panel-, Backlight- oder Bildausgabe-Evidenz | Teil-DTS; `docs/tb8704/mainline-baseline.md`; Vertrauen hoch |
| Touchscreen | SoC-seitige Bus-/GPIO-Infrastruktur grundsätzlich vorhanden | kein TB-Touchcontroller im Teil-DTS belegt | nicht dokumentiert | nicht dokumentiert | nicht getestet | DT-Abgleich | keine TB-spezifische Funktion belegt | Keine Übertragung von Referenzgeräte-Evidenz zulässig | Teil-DTS; Vertrauen hoch |
| GPU / Beschleunigung | Adreno/MSM-Treiberunterstützung im Kernelbaum vorhanden | kein TB-spezifischer Laufzeitbericht | nicht dokumentiert | nicht dokumentiert | nicht getestet | SoC-Unterstützung | keine TB-Funktion belegt | Treiberpräsenz bedeutet weder GPU-Probe noch Rendering | Kernelbaum; Vertrauen hoch für Treibervorhandensein |
| Wi-Fi / Bluetooth | SoC allein identifiziert Funkmodule nicht | TB-Modul-/Firmwarekonfiguration hier nicht belegt | nicht dokumentiert | nicht dokumentiert | unbekannt | Hardware unbekannt | keine Funktion belegt | Modulidentität und Firmware fehlen in der vorliegenden Quelle | `docs/tb8704/mainline-baseline.md`; Vertrauen hoch für Evidenzlücke |
| Audio | SoC-Audioinfrastruktur im Kernelbaum | kein TB-spezifisches Codec-/Routing-Setup belegt | nicht dokumentiert | nicht dokumentiert | nicht getestet | DT-Abgleich | keine TB-spezifische Funktion belegt | Codec, Verstärker, Routing und Aufnahme nicht verifiziert | Teil-DTS; Vertrauen hoch |
| Akku / Laden | PMIC-Treiberinfrastruktur vorhanden | PM8953/PMI8950 inkludiert, Teilregler beschrieben | keine TB-Akkutreiberinitialisierung belegt | keine direkte Laufzeitevidenz | unbekannt | DT/Konfiguration | einzelne Regler werden beschrieben | Kein Nachweis für Fuel Gauge, Ladepfad oder Messwerte | DTS:14-17,58-95; Vertrauen hoch für Beschreibung |
| USB | MSM8953-USB-SoC-Support vorhanden | TB-spezifische USB-Konfiguration nicht belegt | nicht dokumentiert | keine direkte TB-Laufzeitevidenz | nicht getestet | SoC-Unterstützung | keine TB-spezifische Funktion belegt | Host-/Device-Modus und physischer Anschluss offen | Kernelbaum; Vertrauen hoch für SoC-Treiberbestand |
| Suspend / Wake | generische Plattforminfrastruktur | keine TB-spezifische Power-Konfiguration belegt | nicht dokumentiert | nicht dokumentiert | nicht getestet | keine Laufzeitevidenz | keine Funktion belegt | Kein Schluss aus PMIC- oder SoC-Unterstützung zulässig | Teil-DTS; Vertrauen hoch |

## Umfang und Quellenlage

Die versionsweise Kernel-Upgradeplanung einschließlich LTS-Auswahlkriterien
und der getrennten Android-16-Bewertungen für AOSP und PixelOS steht in
`state/kernel-android-roadmap.md`. Sie ist eine Bewertung/Planung, keine
zusätzliche Laufzeit- oder Kompatibilitätsevidenz.

Die vorhandene `README.tb8704.md` verweist auf `state/current-status.md` und
M6.12cw-Unterlagen, die in diesem Checkout nicht vorlagen. Deshalb sind die
dort wiedergegebenen Laufzeitaussagen als sekundär referenzierte Evidenz mit
mittlerem Vertrauen markiert; Original-Logs werden nicht ergänzt oder als
direkt geprüft ausgegeben. `mainline/build/m612cw/report.md` dokumentiert
transparent diese Evidenzlücke; `mainline/build/m612de/report.md` hält fest,
dass für diesen Meilenstein keine Build- oder Initialisierungsergebnisse
gesichert vorliegen.

## Entwicklungschronologie

Die aktuelle Arbeitsbasis ist Linux 6.12 mit Teil-DTS, kein vollständiger
Board-Port. Historische Build- und Bootaussagen sind keine Aussage zum aktuellen
DTS-Stand. Der Verweis auf eine Rettungsumgebung oder Fastboot-Übernahme ist
keine Hardwarefunktions-Evidenz.
