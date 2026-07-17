# Brief an die PBS-Session (2026-07-17) — Feature-Auftrag: Projekt-Landkarte

Provenienz: verfasst in der anneal-framework-Session auf Operator-Wort
(2026-07-17, wörtlich): „als neues feature möchte ich so eine ‚Landkarte'
erstellbar machen für ein laufendes projekt. aber kürzer so eine bis max
2 seiten." Übergabe per Brief-Muster (Planungsbüro-Schulz/CLAUDE.md Nr. 8,
M8-Übergabe-Artefakt).

## Auftrag in einem Satz

Die Fähigkeit schaffen, für ein beliebiges **laufendes Projekt** (Auftrag/
Verfahren) eine **Projekt-Landkarte** nach dem Vorbild der Zielbild-
Landkarte zu erzeugen — nur kürzer: **max. 2 Seiten**.

## Das Vorbild (Grounding)

`pbs-office/zielbild/` — gelesen 2026-07-17 aus der anneal-Session:

- `zielbild-artifact.html` (345 Zeilen, maßgebliche Fassung, publiziert
  unter fester Artifact-URL, KI-gepflegt) — Sektionen u. a.: Das eine
  Muster · Drei Ebenen eines Auftrags · End-to-End-Ablauf · Wo was lebt ·
  Kanten · Governance · Akute Ist-Fehler · Zu lockende Entscheidungen.
- `ENDSTAND-REFERENZ.md` (79 Zeilen, Kurz-Textfassung für Review-Briefs,
  zieht bei Updates nach).
- `zielbild/README.md`: beide sind **Design-Referenz** (kein Regel-
  Dokument, keine Stufe B); Wahrheit über Entscheidungen bleibt
  Ledger/pending-actions.

## Harte Anforderungen (Operator-Wort)

- **A1** — „so eine Landkarte": gleiche Gattung wie das Zielbild
  (Orientierungskarte, auf einen Blick lesbar), nicht ein neues
  Regel-Dokument.
- **A2** — „erstellbar machen für ein laufendes projekt": eine
  **wiederholbare Fähigkeit** pro Projekt, kein Einzelstück für ein
  bestimmtes Projekt.
- **A3** — „kürzer … bis max 2 seiten": harte Obergrenze.

## Offene Design-Fragen — OPERATOR DISPOSITIONIERT

Nicht in diesem Brief entschieden; die PBS-Session klärt sie mit dem
Operator vor dem Bau:

1. **Inhaltsachse.** Das Zielbild ist Endstand-Referenz. Eine
   Projekt-Landkarte kann zeigen: (i) Struktur des Auftrags
   (Auftrag → Verfahren → Leistungen/Doctypes), (ii) Ist-Position im
   End-to-End-Ablauf (Gates, nächste Schritte, Fristen), (iii) die Kanten
   des Projekts (welche Artefakte konsumieren wen), (iv) Offenes
   (pending, markierte Lücken). Welche Auswahl in 2 Seiten passt,
   entscheidet der Operator.
2. **Spiegel-Frage (Governance).** GOVERNANCE kennt „keine handgepflegten
   Spiegel"; Projektzustand lebt in projektdaten.yaml / DOSSIER /
   verfahren.schritte[] / Ledger. Eine Ist-Stand-Landkarte ist ein
   Spiegel dieser Quellen → entweder **generiert** (aus den
   Wahrheitsquellen, drift-checkbar) oder ausdrücklich als **KI-gepflegte
   Design-/Orientierungs-Referenz** deklariert wie das Zielbild
   (README-Disclaimer-Muster). Weg festlegen, bevor gebaut wird.
3. **Form + Ablage.** HTML-Artifact mit fester URL je Projekt (wie das
   Zielbild) und/oder MD im Projektordner (`intern/`?). Auch: eine Karte
   je Auftrag oder je Verfahren (Drei-Ebenen-Lock 2026-07-15 beachten).
4. **Heimat der Fähigkeit.** Wo „erstellbar" verankert wird — Prozess-
   Stamm, RUNBOOK-Ritual, oder ein `pbs`-CLI-Strang — ist eine
   Heimat-Frage der PBS-Session (Zielbild-Landkarte-Einordnungspflicht
   aus BEREICHS-REGELN Nr. 7 gilt: erst einordnen, dann bauen).

## Grenzen

- Dieser Brief wurde in der anneal-framework-Session verfasst; die
  besitzt **nur** `/home/g/dev/Gunther-Schulz/anneal-framework` und hat
  in PBS-Repos nichts geschrieben (nur gelesen: zielbild/*,
  BEREICHS-REGELN.md, Planungsbüro-Schulz/CLAUDE.md, GOVERNANCE.md-
  Auszüge). Ablage des Briefs: anneal-framework
  `dev-notes/briefs/2026-07-17-brief-an-pbs-projekt-landkarte.md`
  (gepusht). Will die PBS-Konvention einen anderen Ablageort, kopiert
  die PBS-Session ihn dorthin (ihre Schreibhoheit).
- Keine Rückwirkung auf anneal-framework: das Feature ist reine
  PBS-Heimat. Kein Statuswechsel, nichts unilateral transitionieren —
  Operator dispositioniert.
