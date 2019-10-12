> [Home](../README.md) / Git Grundlagen

# Git Grundlagen

In diesem Abschnitt wird nur ein grober Umriss über die wichtigsten Funktionen zur Datei-Versionierung mit Git gegeben. Auf die Behandlung von Branches, Merge-Konflikten u.ä. wird hier aus Zeitgründen verzichtet. Um solche Situation von vornherein zu vermeiden, sollte man Projektstände daher regelmäßig hochladen und auf all seinen Geräten immer vor der Bearbeitung den aktuellen Datei-Zustand herunterladen.

Die Anwendung von Software zur Datei-Versionierung soll weitere Eindrücke in das Berufsleben vermitteln. Mit der Veröffentlichung von Projektständen soll zudem die Langzeitmotivation und das Selbstbewusstsein der Teilnehmern gestärkt werden. Darüber hinaus erlaubt es, die Fortschritte der Teilnehmer zu beobachten! Teilnehmer die dies nicht wünschen, können auf Git komplett verzichten oder private Projekte auf Github u.ä. Online-Diensten anlegen.

## Konfiguration
- Ausschluss ausgewählter Dateien von der Versionierung über .gitignore Datei
- Besondere Behandlung ausgewählter (hier besonders großer) Dateien über .gitattributes Datei

## Kommandos
- Dateizustand im aktuellen Ordner prüfen: `git status`
- Dateizustand im aktuellen Ordner sowie den Unterordnern prüfen: `git status -u`
- Geänderte Datei für den nächsten Commit vorbereiten: `git add <Relativer Pfad>`
- Alle geänderten Dateien im aktuellen Ordner sowie den Unterordnern für den nächsten Commit vorbereiten: `git add .`
- Datei aus dem nächsten Commit zurücknehmen: `git reset <Relativer Pfad>`

- Aktuellen Zustand von Datei(en) festschreiben: `git commit`
- Herunterladen des letzten Standes aus dem Online-Repository: `git pull`
- Hochladen von Änderungen in das Online-Repository: `git push`
- Datei auf den letzten versionierten Stand zurücksetzen: `git checkout <Relativer Pfad>`
- Alle Dateien im aktuellen Ordner sowie den Unterordnern auf ihre letzten versionierten Stände zurücksetzen: `git checkout .`
