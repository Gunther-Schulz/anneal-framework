# PBS-Handover-Brief 3 (2026-07-17) — Provenienz: Scratchpad der PBS-Projekt-Session (25-06 Georgendorf), hierher gesichert als Session-Kontinuitäts-Artefakt (flüchtiges /tmp)

# Brief 3 an die anneal-framework-Session: Die Design-Grenze (R8/E6) — was anneal ehrlich NICHT leistet, und wie man das Residuum misst und schrumpft

Kontext wie in Brief 1+2: Analyse hier (PBS-Session, Evidenz im Kontext),
Disposition dort (Operator dispositioniert; Status-Übergänge nur nach
Operator-Wort; ich schreibe nicht ins anneal-framework-Repo).

Anlass: Betreiber-Frage 17.07. „R8 = Fallback-Punkt — kann man den noch
lösen?" Die PBS-Antwort ist gebucht (pbs-office pending-actions RADAR,
Commit 9bcc7b7); dieser Brief trägt die FRAMEWORK-Seite des Themas rüber —
die in Brief 1 (Arbeitspakete) und Brief 2 (Stellschrauben) noch fehlte.

## Die Empirie (frisch, 16.07., beide Richtungen)

1. **E6 = FAIL (Design-Klasse unter Opus, trotz vollständigem Regelwerk +
   Wächternetz).** Eval-Fall der Kategorie „System-Weiterentwicklung/neue
   Komponente" (RUNBOOK R8): der Prüfling hatte alle Regel-Heimaten, alle
   Guards, einen sauberen Brief — und scheiterte an der offenen
   Design-Entscheidung selbst. Fable-Re-Benotung bestätigte FAIL
   (pbs-office entscheide/eval-disziplin-2026-07-16.md §Fable-Re-Benotung).
   Konsequenz PBS-seitig: R8-Klasse = Fallback-Punkt (Eskalation an
   Top-Tier/Operator), Verdikt „Opus alltags-ready mit 3 Grenzen".
2. **Gegenrichtung, gleicher Tag:** Die Urteil→Aufmerksamkeit-Linsen fingen
   Fehler AUCH am Top-Tier (Worked-Boundary fing den Fable-Spec-Widerspruch
   im Fristen-Monitor; 7 Befunde im Fable-eigenen M13-Entwurf durch
   Frisch-Kontext-Review). Beleg-Refs stehen in Brief 2 §Empirie-Anker.

Zusammen ergibt das die saubere Zwei-Klassen-Aussage:
**Zeremonie konvertiert benannte Urteile in prüfbare Aufmerksamkeit — sie
erzeugt kein offenes Design-Urteil.** Anneal macht einen Produzenten
GRÜNDLICHER, nicht URTEILSFÄHIGER. Das ist Grenze A (Merksatz der
PBS-Session: „A heilt das bessere Modell, B heilt nur Mechanik").

## Item-Kandidaten fürs Framework (Operator dispositioniert)

15. **Honest-Limit-Klausel (Doku-Item, klein).** Das Framework behauptet
    nirgends explizit, was es NICHT kann. Kandidat: ein kurzer Abschnitt
    in README/Grundsatz-Doku — „anneal hebt Sorgfalt auf Produzenten-Tier X,
    es hebt nicht die Design-Fähigkeit über Tier X" — mit E6 als Beleg.
    Schützt vor der naheliegenden Fehl-Erwartung, mit genug Zeremonie könne
    ein schwächeres Modell Design-Arbeit übernehmen (genau diese Erwartung
    lag dem 16.07.-Setup implizit zugrunde). Relates:
    dev-notes/modellwahl-und-anneal.md (dort steht die Nutzungs-Seite;
    hier geht es um die Framework-SELBST-Aussage).
16. **Design-Residuum als Messgröße.** Wenn Linsen Design-Behauptungen in
    ausführbare Checker präzipitieren (Brief-2-Kandidat 5,
    Executable-Invariant-Compilation), dann ist der interessante Verlaufs-
    Indikator: WELCHER ANTEIL der Design-Entscheidungen eines Laufs blieb
    unkonvertiert = reines offenes Urteil? Dieser Anteil IST die messbare
    R8-Klasse. Sinkt er über Läufe, schrumpft die Klasse, die zwingend
    Top-Tier braucht. Relates: measurement-harness-mve.md (wäre eine
    Metrik darin), judgment-to-mechanical-lens-candidates.md (dessen
    Erfolgsmaß).
17. **Tier-Verdikt-Invalidierung (Konzept-Item).** PBS hat jetzt Retest-
    Trigger für das E6-Verdikt gebucht (Modell-Sprung im Tier ·
    Kern-Adoption der Linsen · Betriebs-Instanzen live). Framework-
    Verallgemeinerung: ein Verdikt der Form „Tier X schafft Klasse Y nicht"
    trägt seine Invalidierungs-Bedingungen BEI GEBURT (analog
    Verfallsbedingung im PBS-Behelfs-Register). Sonst überlebt das Verdikt
    still seine eigene Grundlage — dieselbe Verrottungs-Klasse, gegen die
    das PBS-M13 gebaut wurde. Relates: model-tier-Binding (das Binding
    kennt sein Tier), tier-aware-dosing (Brief 2 Nr. 14 — dieselbe Achse,
    dritte Verwendung).

## Abgrenzung (damit nichts doppelt läuft)

- Brief 2 Nr. 14 (tier-aware dosing) regelt die DOSIS je Tier — dieser
  Brief regelt die ERWARTUNG je Tier (was Dosis prinzipiell nicht kauft)
  und die HALTBARKEIT von Tier-Verdikten.
- Die PBS-seitigen Konsequenzen (Eskalations-Semantik, RADAR-Retest) sind
  DORT gebucht und brauchen hier nichts — nur die drei Framework-Items
  oben sind zu dispositionieren.

Grenzen wie immer: nur anneal-framework-Repo schreiben; Status-Übergänge
nur nach Operator-Wort; bei Übernahme bitte relate-before-add gegen die
bestehenden Items prüfen (Nr. 15–17 sind als Fortsetzung der Brief-2-
Nummerierung benannt).
