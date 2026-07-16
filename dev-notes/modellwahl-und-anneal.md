# Modellwahl × anneal — Nutzungs- und Erwartungs-Referenz (Operator)

Betreiber-Referenz (Deutsch, bewusst): Was anneal je Produzenten-Modell
leistet, was nicht, und wie man es dosiert. Destillat des Feld-Datenpunkts
2026-07-16 (Modell-Verwechslungs-Vorfall pbs + vier Cross-Tier-Reviews);
Provenienz unten. Stand: n klein — als Baseline lesen, mit Empirie nachziehen.

## Die zwei Grenzen (das Denkmodell)

- **Grenze A — Urteil pro Werkstück** (Rechts-/Fach-Semantik, Fencepost-
  Arithmetik, richtiger Design-Schnitt). **Modell-sensitiv:** ein stärkeres
  Modell macht diese Fehler seltener.
- **Grenze B — Kohärenz über den Korpus** (verwaiste Producer, verpasste
  Dependents, Drift zwischen Kopien, vergessene Kaskaden). **Modell-
  unempfindlich** ab realer Korpusgröße: Buchhaltung, nicht Intelligenz.
  Heilt nur Mechanik (Register, Wächter, erzwungene Enumeration).

Merksatz: **A heilt das bessere Modell, B heilt nur Mechanik.**

## Was anneal je Modell liefert

| | Opus (Produzent) | Fable (Produzent) |
|---|---|---|
| Grenze A | Kompensiert TEILWEISE — Zyklen iterieren viele Urteils-Fehler heraus, aber Rest rutscht durch Same-Tier-Verify (belegt: 4 Would-Ship-Defekte fielen erst Cross-Tier) | Kaum nötig — Fehler entstehen großteils nicht; erwarte 2–3 Zyklen statt ~11 |
| Grenze B | Voller Wert | **Voller Wert (unverändert)** |
| Frischer-Kontext-Effekt | Voller Wert | **Voller Wert** — Selbst-Blindheit ist strukturell, nicht Intelligenz (Beleg: Fable-Reviewer fand 7 substanzielle Befunde im Fable-eigenen M13-Entwurf) |
| Kosten | Hoch (viele Konvergenz-Zyklen) | Niedrig (wenige Zyklen) — anneal wird billiger, nicht wertlos |

## Nutzungsregeln

1. **Mit Opus:** anneal auf breiter Aufgabenfläche fahren — es verdient dort
   auf mehr Klassen sein Geld (beide Grenzen lecken). Decision-complete
   gebriefte Arbeit ist die Opus-Sweet-Spot-Zone: das Gerüst schließt genau
   die Lücke, die Opus dort hat.
2. **Mit Fable:** proportional dosieren — volle Zeremonie NUR für schwere/
   korpusweite Änderungen (Regel-Korpus, neue Prozesse, Stufe-B-Klasse);
   leichte Edits ohne. (Deckt sich mit `backlog/proportional-cycle-weight.md`.)
3. **Prüfer-Tier ≥ Produzenten-Tier** — nie Same-Model-Selbst-Benotung für
   den Urteils-Gegencheck. Same-Model-Frischkontext bleibt wertvoll für
   Aufmerksamkeits-Klasse + Rahmungs-Blindheit; den Urteils-Deckel hebt nur
   das stärkere Modell. **Top-Tier-Grenzfall (Fable-Session):** ein höheres
   Prüfer-Tier existiert dann nicht — es gilt Frisch-Kontext-Prüfung (fängt
   auch same-model erstaunlich viel: 7 substanzielle Befunde im Fable-eigenen
   M13-Entwurf, davon urteilsnahe) + Regel 4 (Konvertierung); der
   verbleibende Urteils-Rest ist OFFEN BENANNTES Residuum mit
   Operator-Soundness als Backstop — nie eine stillschweigend erfüllte
   Achse. (pbs-Regel: GOVERNANCE §Weiterentwicklung Nr. 8b „Modell-Achse"
   inkl. Grenzfall-Klausel 9ec004e; die kanonische Carve-out-Form entscheidet
   der anneal-dev-Zyklus zu `backlog/verify-model-diversity.md` — danach
   diese Passage auf dessen Formulierung ziehen.)
4. **Urteil → Aufmerksamkeit konvertieren:** die drei Linsen-Kandidaten
   (Domain-Claim-Re-Derivation inkl. „data beats commentary" ·
   Worked-Boundary-Example · Closed-Set-Sweep) machen Urteils-Fehler
   mechanisch fangbar — dann fängt sie das Gerüst auf JEDEM Tier
   (`backlog/judgment-to-mechanical-lens-candidates.md`; pbs fährt sie als
   getrackten Vorgriff, pbs-office/anneal-dev.config/lenses.md).
5. **Dispatch-Heuristik:** Gerüst kompensiert Aufmerksamkeit, Prüfer-Tier
   kompensiert Urteil. Opus + anneal für gut gebriefte Umsetzung; Fable für
   offene Design-Entscheidungen und als Prüfer.
6. **Modell-Provenienz:** der `Co-Authored-By`-Trailer jedes Commits trägt
   das Modell — bei Zweifel, wer was produziert hat, ist er die erste
   Prüfquelle (so wurde der Vorfall überhaupt rekonstruierbar).

## Erwartungs-Kalibrierung (ehrlich)

- Opus fühlt sich schwächer an, weil er MEHR sichtbare Ausrutscher beider
  Klassen produziert; der spezifische Opus-Rückstand gegen Fable ist aber
  Grenze A. Fable driftet in Grenze B genauso — nur seltener und LEISER:
  weniger Warnsignale bei gleicher struktureller Entropie. Deshalb bleibt
  die Mechanik (Wächter/Register/Audit) unter Fable genauso pflichtig.
- Counterfactuals („wäre Fable an die Grenze gekommen?") sind begründete
  Schätzungen, keine Messwerte. Datenbasis 2026-07-16: erster
  False-Accept-Beleg für Same-Tier-Verify; n wächst mit jedem Lauf.

## Provenienz

- Feld-Datenpunkt + Messung: `backlog/verify-model-diversity.md`
  §2026-07-16 (Framework-Buchung f790906, Zähler-Korrektur 25b39c6).
- pbs-Seite: pbs-office/entscheide/pruefer-modell-achse-2026-07-16.md
  (DECISION mit voller Empirie) · pbs-wissen/GOVERNANCE.md Nr. 8b.
- Fable-prüft-Fable-Beleg: M13-Kohärenz-Review 2026-07-16 (7 substanzielle
  Befunde im Fable-eigenen Entwurf; pbs-Session).
