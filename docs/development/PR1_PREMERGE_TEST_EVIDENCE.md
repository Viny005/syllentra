# Testnachweis: PostgreSQL-Validierung der PR #1 (Pre-Merge-Hardening)

**Datum:** 28.10.2026  
**Quelle:** Antigravity — Mission 31D  
**Getesteter Commit:** [`9c8311eaff086bebe0829a944addfe38f22df85a`](https://github.com/Viny005/syllentra/commit/9c8311eaff086bebe0829a944addfe38f22df85a)  
**Branch:** `fix/pr1-premerge-hardening`  
**Status:** Erfolgreich ausgeführt (synthetische Testumgebung)

---

## 1. Testumgebung

Die dynamische Validierung der PostgreSQL-Besitzprüfung, Advisory-Locks und Isolationstests
wurde in einer isolierten Linux-Containerumgebung ohne Host-Port-Exponierung ausgeführt:

* **PostgreSQL:** Version 17.11 (Debian 17.11-1.pgdg12+2, 64-Bit), fixiert per Digest
  `postgres@sha256:858bb5e98eed02eb8cafbcdc007f9a65d1b613972028944a8ec2133ccaf80d27`.
* **Python / uv:** Python 3.12.12 und uv 0.9.30 (Debian Bookworm), fixiert per Digest
  `ghcr.io/astral-sh/uv:python3.12-bookworm-slim@sha256:e5b65587bce7de595f299855d7385fe7fca39b8a74baa261ba1b7147afa78e58`.
* **Container-Architektur (Option B):** Zwei dedizierte, kurzlebige Testcontainer
  (`syllentra-mission31d-postgres` und `syllentra-mission31d-runner`) im gemeinsamen
  Netzwerk-Namespace (`--network container:...`), Kommunikation ausschließlich über
  internes Loopback `127.0.0.1:55439`.
* **Datenintegrität:** Flüchtiges `tmpfs`-Dateisystem für das PostgreSQL-Datenverzeichnis.
  Ausschließlich synthetische Testdaten.
* **Schutz bestehender Ressourcen:** Kein Zugriff auf Cloud- oder Produktivsysteme. Die bereits
  vorhandenen gestoppten Container (`syllentra-mission9-local`, `syllentra-mission14-uv`)
  wurden weder gestartet, verändert noch gelöscht.

---

## 2. Testergebnisse

| Testbereich | Ausgeführter Prüfumfang / Befehl | Ergebnis | Dauer |
|---|---|---|---|
| **Code-Qualität (Ruff)** | `ruff check scripts/test_db.py tests/test_isolation.py tests/conftest.py` *(gezielte Dateiprüfung, kein Verzeichnischeck)* | 0 Fehler, 0 Warnungen | < 1 s |
| **Typ-Prüfung (Mypy)** | `mypy --config-file pyproject.toml scripts/test_db.py` *(beschränkt auf `test_db.py`)* | 0 Fehler (Success) | 1 s |
| **Locks & Besitz (Phasen B–D)** | Gezielte dynamische Prüfskripte (Verbindung, Advisory-Locks, Fail-closed, Concurrency) | Alle Prüfpfade bestanden | 4 s |
| **PostgreSQL-Isolation (Phase E)** | `pytest -q -x -p no:cacheprovider tests/test_isolation.py` | **24 / 24 bestanden** (100 %) | 7,4 s |
| **Backend-Gesamtsuite (Phase F)** | `pytest -q -x -p no:cacheprovider` | **116 / 116 bestanden** (100 %) | 76,5 s |

### Wichtigste dynamisch verifizierte Invarianten auf echtem PostgreSQL

1. **Advisory-Locks in `pg_locks`:** Korrekte Repräsentation des 64-Bit-Schlüssels als
   `classid` (obere 32 Bit), `objid` (untere 32 Bit), `objsubid = 1` und `granted = true`.
2. **Besitzprüfung:** `assert_owned()` verifiziert den exklusiven Besitz-Lock; bei geschlossener
   oder verlorener Verbindung greift sofortiges *Fail-closed* (`OwnershipError`).
3. **Schutz aktiver Verbindungen:** `drop_run_database()` verweigert das Löschen bei offenen
   Client-Verbindungen (`DatabaseInUseError`), behält jedoch die Besitzverbindung offen. Erst nach
   Schließen der Clients gelingt das Löschen.
4. **Orphan-Bereinigung (`reclaim_orphaned_database` / `sweep`):** Verwaiste Datenbanken werden
   nur unter frisch erworbenem Run-Lock übernommen; unmarkierte Datenbanken werden strikt
   abgewiesen (`UnmarkedDatabaseError`).
5. **Vollständige Bereinigung:** Vor und nach dem gesamten Testlauf enthielt die PostgreSQL-Instanz
   exakt dieselben fünf Datenbanken (`postgres`, `syllentra_prototype`, `syllentra_test`,
   `template0`, `template1`). Alle temporären Testdatenbanken wurden vollständig gelöscht.
6. **Container-Bereinigung:** Beide Testcontainer wurden unmittelbar nach Abschluss gestoppt
   und entfernt (`docker rm`).

---

## 3. Wichtige Einschränkungen und bekannte Betriebsgrenzen

* **Enthaltene Tests:** Die 24 Isolationstests sind eine Teilmenge der 116 Backendtests.
* **Prüfumfang von Linter und Typprüfung:** Die statischen Prüfungen in Mission 31D beschränkten
  sich auf die betroffenen Dateien (`scripts/test_db.py`, `tests/test_isolation.py`,
  `tests/conftest.py` für Ruff; `scripts/test_db.py` für Mypy). Sie stellen keinen vollständigen
  Verzeichnischeck des gesamten Repositories dar.
* **Unabhängige Wiederholung:** Das unabhängige Codex-Audit (Mission 32) hat den bereitgestellten
  Testbericht und den Code geprüft, die PostgreSQL-Läufe jedoch nicht in eigener Infrastruktur
  wiederholt.
* **Rohlogs:** Vollständige Terminal-Rohlogs wurden Codex nicht als persistente Datei übergeben,
  da die ephemeren Testcontainer planmäßig gelöscht wurden und Container-Logs flüchtig waren.
* **Formatierungsprüfung:** `ruff format --check` meldet weiterhin rein kosmetische
  Abweichungen (u. a. Einzeiler-Kompaktierung), die absichtlich nicht verändert wurden, um
  keine unnötigen Diffs zu erzeugen.
* **Geltungsbereich:** Frontend-E2E-Tests, Penetrationstests und produktive Sicherheitsnachweise
  sind ausdrücklich nicht Gegenstand dieser isolierten PostgreSQL-Validierung.
* **Keine Aussage über produktive V1-Freigabe:** Die erfolgreichen Tests belegen das sichere
  Verhalten des Prototyps unter synthetischen Bedingungen, stellen jedoch keine Freigabe für
  den Produktivbetrieb (V1) dar.
* **Bekannte Betriebsgrenze bei Verbindungsverlust:** Ein verlorener PostgreSQL-Advisory-Lock
  beweist nicht zwingend, dass der ursprüngliche Besitzerprozess beendet ist (z. B. bei
  Netzwerkunterbrechung der Maintenance-Verbindung). Verwaiste Datenbanken werden durch `sweep()`
  erst nach Ablauf des Schwellenwerts und bei Abwesenheit aktiver Verbindungen bereinigt.

---

## 4. Zugehörige Dokumente

* Betriebsregeln und Sicherheitsgrenzen: [prototypes/backend/README.md](../../prototypes/backend/README.md)
* Implementierung der Testdatenbank-Verwaltung: [prototypes/backend/scripts/test_db.py](../../prototypes/backend/scripts/test_db.py)
* Integrationstests: [prototypes/backend/tests/test_isolation.py](../../prototypes/backend/tests/test_isolation.py)
