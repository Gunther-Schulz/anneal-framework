# PBS-Handover-Brief 1 (2026-07-16) — Provenienz: PBS-Session-Scratchpad, hierher gesichert als Session-Kontinuitäts-Artefakt (Session 2026-07-16 abend)

# Brief: anneal-framework-Session (Übergabe aus der PBS-Session, 2026-07-16 Abend)

## Auftrag in einem Satz
Die zwei frisch gebuchten Backlog-Items aus dem heutigen PBS-Feld-Datenpunkt
dispositionieren und (nach Operator-Entscheid) als kleine Kampagne umsetzen:
Modell-Achse im Verify + die drei Urteils-zu-Aufmerksamkeit-Linsen.

## Repo + Konventionen (zuerst lesen)
- Repo: `/home/g/dev/Gunther-Schulz/anneal-framework` (gepusht, Stand `25b39c6`).
- `dev-notes/backlog/README.md` — Konventionen-Block oben (relate-before-add;
  Status-Tokens [READY|DESIGN|PARKED|GATED|PARTIAL]; Status-Übergänge
  dispositioniert der OPERATOR, nie unilateral; „the folder IS the index";
  shipped → git mv archive/) und dann die zwei neuesten READ-FIRST-Sektionen
  (beide 2026-07-16: „Model-axis datapoint" + „Cross-instance datapoint").
- Kernel-Änderungen laufen selbst durch anneal-dev-Zyklen (Selbst-Hosting);
  Kampagnen-Struktur siehe ▶ Campaign map im README.

## Die Faktenlage (Provenienz)
Am 16.07. lief die PBS-Bau-Session unbemerkt auf opus-4.8 statt fable-5
(entdeckt am Modell-Umschalter; Provenienz je Commit via Co-Authored-By-
Trailer). Vier frische Fable-Cross-Tier-Reviews über das Opus-Tagwerk
ergaben einen sauberen Split: Aufmerksamkeits-Klasse-Defekte hatten die
Same-Tier-anneal-Pässe überwiegend selbst gefangen; **vier Urteils-Klasse-
Defekte passierten Same-Tier-Verify und fielen NUR Cross-Tier** (Rechts-
Fencepost + Unter-Erzwingung max(1 Monat, 30 Tage); rechtlich überclaimende
Meldung; Ermessen-als-Automatik in gebautem Text; staler-Kommentar-über-
Daten-Grounding-Fehler). Erster False-Accept-Beleg — bisher gab es nur
True-Positive-Evidenz für die intent-falsification.
PBS-seitige Anker: pbs-wissen/GOVERNANCE.md §Weiterentwicklung Nr. 8b
(„Modell-Achse") · pbs-office/entscheide/pruefer-modell-achse-2026-07-16.md
(DECISION mit voller Empirie) · Framework-Commits f790906 (Buchung) +
25b39c6 (Zähler-Korrekturen am Artefakt nachgezählt + Index-Zeile).

## Arbeitspakete (in dieser Reihenfolge)

1. **Disposition `verify-model-diversity.md`** (heute [PARKED], §2026-07-16
   trägt den Reopen-Datenpunkt): Der Operator hatte den Trade („Verify läuft
   Same-Tier wegen Model-Tier-Floor") 2× bewusst akzeptiert — mit dem
   expliziten Vorbehalt „revisit wenn Evidenz kommt". Die Evidenz ist da.
   Fork: (a) Verify-Carve-out aus dem Floor (Verify-Tier ≥ Actor-Tier bzw.
   Cross-Model), (b) Diversität innerhalb des Top-Tiers, (c) Trade erneut
   halten. Empfehlung der PBS-Session: (a), mindestens für die Urteils-
   Klasse-Legs (intent-falsification). OPERATOR ENTSCHEIDET — Item-Status
   erst nach seinem Wort transitionieren.
2. **`judgment-to-mechanical-lens-candidates.md` [DESIGN]:** die drei
   Kandidaten (Domain-Claim-Re-Derivation inkl. „data beats commentary" ·
   Worked-Boundary-Example-Pflicht · Closed-Set-Sweep). Design-Fork laut
   Item: standardisierter Lens-Satz vs. Falsifikations-Dispatch-Brief-
   Disziplin (Lens-Crowding-Kosten, siehe lens-crowding-vs-broad-search.md).
   Kernel-Constraints wahren: core.md hält Urteil AUS dem mechanischen
   Falsifikations-Pass heraus; foundations.md verbietet Operator-Detection-
   Dependence — die Integrationsskizze in verify-model-diversity.md
   (fresh-context + CONDITIONAL/AUTO-ACCEPTED-Split) ist der Präzedenzweg.
3. **Cross-Repo-Verfallsbedingung notieren:** Das PBS-Binding fährt die drei
   Linsen bereits als getrackten Vorgriff
   (pbs-office/anneal-dev.config/lenses.md §Kern-Kandidaten-Vorgriff,
   Verfallsbedingung = Kern-Adoption). WENN die Kernel-Adoption shippt:
   im Abschluss-Bericht ausdrücklich vermerken, damit eine PBS-Session die
   Vorgriffs-Sektion löscht (Dedup Kern ∪ Supplement). NICHT selbst in
   PBS-Repos schreiben — die gehören anderen Sessions (Ein-Schreiber).
4. **Optional (Operator-Call, vorbestehend):** Index-Drift-Grooming — die
   „N open"-Zähler-Erzählung im README driftet seit ≥10.07. gegen den
   Dateibestand (heutige Buchungs-Review-Feststellung; nur benannt, nicht
   behoben).

## Grenzen
- Diese Session besitzt NUR `/home/g/dev/Gunther-Schulz/anneal-framework`.
  Keine Writes in Planungsbüro-Schulz-Repos (PBS-Hauptsession + eine
  pausierte Festsetzungs-Session arbeiten dort).
- Commit-Stil des Repos: `backlog: …`-Messages, direkt pushen.
- Statuswechsel/Archivierungen nur nach Operator-Wort im Chat.
