# PBS-Handover-Brief 2 (2026-07-16) — Provenienz: PBS-Session-Scratchpad, hierher gesichert; Disposition offen (Task-Batch nach der Model-Achsen-Kampagne)

# Brief 2 an die anneal-framework-Session: Stellschrauben-Kandidaten aus der PBS-Tages-Empirie (2026-07-16)

Kontext: Diese Kandidaten wurden in der PBS-Session analysiert, weil dort die
Tages-Empirie im Kontext lag (Modell-Verwechslungs-Vorfall, 4 Cross-Tier-
Reviews, 3 anneal-gestützte Bau-Dispatches, 2 Linsen-Treffer live). Die
DISPOSITION gehört hierher — relate-before-add: die Zuordnung zu bestehenden
Items ist unten je Kandidat vorgenommen; Operator dispositioniert.

## A. Subtile Performance-Schrauben

1. **Inkrementelle Falsifikation (NEU — Item-Kandidat).** Empirie: die
   Zyklus-Kosten werden von der Per-Konvergenz-Falsifikation dominiert, die
   je Versuch ALLES re-prüft (proportional-cycle-weight, Kalibrier-Signal i).
   Kandidat: delta-scoped re-verify — nur Claims neu prüfen, die der letzte
   Fix berührt (Dirty-Flag über den Claim-Graph). Relates:
   proportional-cycle-weight.md (Kostenstruktur-Beleg dort).
2. **Linsen-Hit-Rate-Telemetrie → Pruning (NEU-teilweise).** Die Run-Tracker
   enthalten bereits, welche Linse je Zyklus was fing — auswerten, Linsen
   ohne Treffer über N Läufe in einen On-Demand-Pool verrenten. Relates:
   lens-crowding-vs-broad-search.md (bekommt damit Daten statt Geschmack),
   measurement-harness-mve.md (Infrastruktur).
3. **Criteria-first mechanisieren.** Heute Disziplin-Grade (als Strain ii im
   Cross-instance-Datenpunkt gebucht): erzwingbar per Zwei-Stufen-Dispatch
   (Subagent emittiert Erfolgs-Kriterien aus dem Requirements-Record, DANN
   erst erhält er das Design). Relates: der Strain in README-READ-FIRST
   2026-07-16 + intent-falsification-soundness-sweep.md.
4. **Design-time Trace-Clause umsetzen.** These existiert
   (design-decision-implication-depth-gaps.md ~Z.227: reduziert Zyklen);
   heute doppelt bestätigt (2 von 4 Nicht-Konvergenz-Deltas self-inflicted;
   zweiter Lauf reproduzierte die Form). Von These auf [READY] heben?

## B. Radikale Design-Alternativen (clippy-Erbe hinterfragen)

5. **Executable-Invariant-Compilation (NEU — Kern-These-Kandidat).** Statt
   Prosa-Linsen über Prosa-Designs: jede Design-Behauptung emittiert bei
   Geburt ihren AUSFÜHRBAREN Checker (Test/Grep-Prädikat/Schema-Constraint)
   — anneal als Compiler, „Wächter statt Vorsatz all the way down". Das
   pbs-Deployment ist organisch schon auf diesem Weg (Closed-Set-Sweep-Tests,
   Signatur-Registry, Behelfs-Register mit Leser). Stärkster Paradigmen-
   Kandidat; kollidiert bewusst mit der Prosa-Lens-Architektur.
6. **Live-Adversary statt Etappen-Falsifikation.** Permanenter Red-Team-
   Agent WÄHREND des Designens (Pair-Modus) statt Falsifikations-Pässe
   danach — fängt vor dem Einbau, zahlt Parallelität statt Zyklen. Relates:
   intent-falsification (dessen kontinuierliche Form).
7. **Tournament-Design.** N unabhängige Entwürfe + Judge statt
   iterate-one — überlegen bei breitem Lösungsraum, teurer bei engem.
   Vermutlich neues Item; Abgrenzung zu bestehenden Judge-Mustern prüfen.
8. **Messgetriebene Zeremonie (SPC).** Defekt-Escape-Rate je Stufe über
   Läufe tracken; Zeremonie-Dosis aus Daten statt Klassen-Intuition.
   Relates: measurement-harness-mve.md (wäre dessen Ausbaustufe).

## C. Rausschmiss-Kandidaten

9. **Quorum/Multi-Voting:** bleibt tot (bereits entschieden — nur bestätigt).
10. **Render-zentrische Verify-Batterie als DEFAULT:** Instanz definiert
    ihre Batterie (verify-battery-nonrender-instance.md existiert) —
    konsequent: Default streichen, nicht nur überschreibbar machen.
11. **Voll-Zeremonie als Default:** proportional-cycle-weight zu Ende
    gedacht = Voll-Zeremonie wird begründungspflichtige AUSNAHME (schwere/
    korpusweite Klasse), nicht Normalfall.
12. **Per-Versuch-Voll-Refalsifikation:** entfällt mit Kandidat 1.
13. **NICHT rausschmeißen** (heutige Gegen-Evidenz): frischer Kontext +
    Intent-Falsifikation — lieferten heute gegen BEIDE Modell-Tiers
    (Opus-Tagwerk-Befunde; 7 Befunde im Fable-eigenen M13-Entwurf; Juli-
    Fencepost-Fund der Worked-Boundary-Linse gegen eine Fable-Spec).

## Frische Empirie-Anker (für die Item-Bodies)

- Worked-Boundary-Linse fing einen FABLE-Spec-Widerspruch beim Bau
  (Fristen-Monitor: Juli-Beispiel vs. max(Kalendermonat,30)-Regel; pbs-office
  entscheide/design-fristen-monitor §Korrektur 2026-07-16) — Beleg, dass
  Urteil→Aufmerksamkeit-Konvertierung auch am Top-Tier greift.
- Closed-Set-Sweep-Linse produzierte in 3 Bau-Dispatches je einen
  Enumeration-aus-der-Quelle-Test (pbs-projekt signaturen/fristen/behelfe) —
  die Linse präzipitiert natürlich in Executable Invariants (stützt Kandidat 5).
- Review-Scoping-Lehre (PBS-seitig gemintet): Review-Scope braucht zwei
  Achsen — Provenienz UND Kritikalität; ein Entscheidungsinstrument wird
  adversarial geprüft, egal wer/wann es schrieb.

Grenzen wie im ersten Brief: nur anneal-framework schreiben; Status-
Übergänge nur nach Operator-Wort.

## Nachtrag (Betreiber-Frage: anneal-dev-lite für Fable?)

14. **Tier-aware Dosing — KEIN Fork, KEIN Status quo (Operator-Frage
    2026-07-16 abends).** Bewertung aus der PBS-Session: Ein Fable-Lite-Fork
    dupliziert das Skeleton (Drift, M2-Analog); „transparent kompatibel"
    stimmt aber auch nicht — die Zeremonie-Defaults sind auf schwächere
    Produzenten kalibriert (clippy-Erbe), Voll-Zeremonie am Top-Tier
    überzahlt (avoidable-churn-Klasse). Richtige Form: **Produzenten-Tier
    als zweite Achse in die bestehende Dosierungs-Funktion** — Dosis =
    f(Aufgaben-Klasse, Tier). Tier-skalierend: Konvergenz-Budget,
    Iterations-Erwartung. NIE tier-skalierend (2026-07-16-Evidenz, fing
    Fable-Fehler): Frisch-Kontext-Isolation, mechanische Falsifikation,
    Urteil→Aufmerksamkeit-Linsen, verify-Batterie. Relates:
    proportional-cycle-weight.md (dieselbe Funktion, zweite Achse) ·
    model-tier-Config-Slot (das Binding kennt sein Tier bereits) ·
    dev-notes/modellwahl-und-anneal.md Regeln 1–2 (deren Mechanisierung).
