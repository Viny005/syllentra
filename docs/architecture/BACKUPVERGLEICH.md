# Unabhängige Sicherung — Verfahren und Anbieter

**Version:** 0.1 · **Stand:** 22.10.2026 · **Status:** Empfohlen / Zur Entscheidung

## 1. Verbindlicher Rahmen

DEC-49 und [S3.6](../spec/S3-inbetriebnahme.md#s36-unabhängige-sicherung-und-nachgewiesener-restore) verlangen unabhängigen EU-Speicher, sichere getrennte Schlüssel/Zugänge, endliche Retention und tatsächlichen Restore mit heutigen Rechten/Löschungen. Ein Cloudbucket ist nur Speicher, ein Replikat kopiert auch Fehler/Löschungen, Archivierung hält Daten nach eigenem Zweck; erst konsistente Fassungen, Wiederherstellbarkeit und geprüfter Lifecycle ergeben ein Backup.

## 2. Vergleich

| Kandidat | EU / Unabhängigkeit | Kosten-/Lizenzbeleg | Sicherheits-/Betriebsgrenze |
|---|---|---|---|
| restic zu unabhängigem S3-Objektspeicher | Vom Primäranbieter unabhängiger Betreiber und geeignete EU-Jurisdiktion nötig | restic BSD-2-Clause gelesen; keine Lizenzgebühr, Speicher/Requests/Transfer/Pflege trotzdem Kosten | Clientseitig verschlüsselte versionierte Sicherung; Passwort/Schlüssel außerhalb nur primärer Plattform wiederherstellbar; DBkonsistenz zusätzlich herstellen |
| Cloudflare R2 Standard mit **EU-Jurisdiction** | Offizieller Dokumentationsquelltext bestätigt `eu`-Jurisdiktion für Objekte; **Location Hint allein garantiert keinen Ort** | Offizielle Preisquelle gelesen: 10 GB-Monat Standard, 1 Mio. A-/10 Mio. B-Requests frei; darüber 0,015 USD/GB-Monat, 4,50/0,36 USD je Mio.; Details in Kostenanalyse | Attraktiver unabhängiger S3-Kandidat, aber gesamte Metadaten-/Steuerungs-/Supportverarbeitung, Verträge, Löschschutz und Kontoaktivierungsbedingungen nicht vollständig verifiziert. Daher noch kein DSGVO-/DEC-49-Gesamtnachweis. |
| Hetzner Storage Box mit restic über unterstützten Zugriff | Unabhängig von OCI/Scaleway; konkreten EU-Standort prüfen. Nicht als unabhängiger Anbieter zählen, wenn Hetzner Primärhost ist. | Aktueller Tarif, Protokoll-/Snapshot-/Limitdetails **nicht verifiziert**, Angebotsseite 403 | Wenige Bausteine möglich; Schreib-/Lösch-/Restorezugriff und Schutz gegen kompromittierten Primärserver gesondert prüfen. Server-Snapshots allein kein verifizierter Schutz. |
| Scaleway Object Storage mit restic | Unabhängig von OCI/Hetzner; nicht vom eigenen Scaleway-Primärhost unabhängig | Aktuelle Preise, Regionen, Retention-/Object-Lockfähigkeiten **nicht verifiziert** | S3-Portabilität plausibel; Request-/Egress-/Mindesthaltungs- und Löschrechte prüfen |
| Backblaze B2 mit restic | Konkreten EU-Speicherort, Accountregion, Verträge und Kopien prüfen | Aktuelle Preise/Gratislimits **nicht verifiziert**, offizieller Abruf 403 | S3-kompatibler Kandidat; Regionswechsel, Restorekosten und Manipulations-/Löschschutz nicht pauschal zusagen |
| Borg/verschlüsselte Remote-Sicherung | Getrennter geeigneter EU-Server, SSH-/Schlüssel-/Kapazitätsbetrieb | Aktuelle Lizenz/Release hier nicht separat geprüft | Sinnvolle Alternative bei administriertem Remoteziel; kein notwendiger privater Dauer-PC, kein Gratisserver unterstellt |

[R2-Quelle](https://raw.githubusercontent.com/cloudflare/cloudflare-docs/production/src/content/docs/r2/reference/data-location.mdx) unterscheidet Garantien für Bucketobjekte von bloßer Platzierungsempfehlung. Das ist kein Beleg, dass jede Betriebs-/Telemetrie-/Vertragsdatenverarbeitung automatisch nur EU erfolgt. Keine Auswahl vor Datenschutzprüfung. [Quellenregister](QUELLEN.md), Abruf 22.10.2026.

## 3. Wiederherstellbarkeit und Kompromittierung

Konsistenten PostgreSQL-Sicherungsstand, Dokumentversionen, freigegebene Konfiguration/Schema-/Softwarebezüge und heutigen Lösch-/Entzugsstand zusammen erfassen. Temporäre Transkripte, Cloudklartext, Logs und aktive Tokens nicht als unkontrolliertes Dauergedächtnis mitsichern. Persönlicher Export enthält keine technischen Server-/IdP-/Admincredentials; getrennte Betriebsrecovery benötigt eigenen geschützten Umfang.

Erstellen/Lesen/Prunen/Löschen mit passenden begrenzten Rechten trennen. Ein voll berechtigtes Backupcredential auf kompromittiertem Primärserver erlaubt eventuell Backupzerstörung: append-only bzw. nachweisbare getrennte Löschautorität/Retention prüfen, keine R2-Object-Lock-Unterstützung ohne Quelle behaupten. Recoveryzugang und Backupschlüssel unabhängig vom Hauptaccount, ohne private Dokumentenschlüssel im Backend. Schlüsselrotation darf vorhandene Sicherungen nicht unbemerkt unlesbar machen.

Restores zuerst isoliert, Konten-/Quellschutz/Rechte/Integrität prüfen, aktuelle Löschungen/Entzüge priorisieren; alte Integrations-/MFA-/Session-/Supportzustände nicht aktivieren. Fehlender heutiger Kontrollstand oder Schlüssel sperrt Wiederfreigabe. RPO/RTO und Retention nach S3-Methode bestätigen, kein beliebiges tägliches Intervall. Primärplattformverlust und Backup-/Schlüsselkompromittierung als getrennte Szenarien wirklich üben, erst nach eigener Autorisierung. In Mission 5 keine Sicherung, Installation, Ressource oder Probe ausgeführt.
