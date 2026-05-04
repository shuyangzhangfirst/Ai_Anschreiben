Dieses Projekt ist ein KI-gestützter Generator für deutsche Bewerbungsanschreiben (Anschreiben).

Das System erstellt automatisch ein personalisiertes Anschreiben basierend auf deinem Profil und deiner Zielstelle und exportiert das Ergebnis als PDF-Datei.

Das Projekt befindet sich aktuell noch in der aktiven Entwicklung, aber die Kernfunktionalität ist bereits funktionsfähig.


🚀 Aktuelle Funktionen


1) Automatische Erstellung von Bewerbungsanschreiben mit KI

2) Personalisierte Inhalte basierend auf Benutzerprofil

3) Strukturierte Prompt- und Output-Verarbeitung

4) HTML-Template-Rendering

5) PDF-Generierung

6) Vollautomatisierte Pipeline

Ein Beispiel für die generierte Ausgabe befindet sich im Repository:

/anschreiben.pdf

Diese Datei zeigt die aktuelle Qualität der generierten Ergebnisse.

⚙️ Verwendung

1️⃣ Gemini API Key einfügen

Öffne die Datei:ai anschreiben.py

Füge dort deinen Gemini API Key ein: GEMINI_API_KEY = "dein_api_key_hier"

2️⃣ Persönliche Informationen konfigurieren

Bearbeite die Datei:

my_profile.json

In der Datei:ai anschreiben.py

findest du die Funktion:set_target_job(...)

Dort bitte die Informationen zur Zielstelle bzw. zum Unternehmen eintragen.

4️⃣ Programm ausführen

Starte das Projekt mit:

python ai anschreiben.py

Nach der Ausführung wird folgende Datei generiert:

anschreiben.pdf

Dies ist dein fertiges, KI-generiertes Bewerbungsanschreiben.