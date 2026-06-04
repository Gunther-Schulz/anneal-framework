## V-12. Basis-rule artifact form for file:line citations

**Status: FIX-SHIPPED (2026-05-26, commit [pending]).** §3.2 lead
sharpened to require the artifact form for any basis: a search
result with its executable query, OR a located read with the
verbatim content. Paraphrase, summary, or free-text claim of
having looked is explicitly not a basis. Converts §3.2 from
naked-judgment-shaped (the AI judges whether its cited basis is
sufficient) to artifact-bearing-shaped (the basis record includes
the un-fakeable content). Extends V-7's prior basis-rule sharpening
(`spec/core.md` §3.2.1 embedded-claims rule, commit c5e7ad9) along
a different axis — V-7 widened *which claims* carry the rule; V-12
sharpens *what counts as the artifact*.

**Closing criterion (FIX-SHIPPED → RESOLVED).** A post-run review
identifies a run where the artifact-form requirement was
load-bearing — caught a paraphrase-shape finding at finding-record
time that would have forced cascade convergence cycles to correct
under the pre-fix protocol. One observed instance is sufficient.

**Original observation preserved below for audit trail.**

---

The unit-14 run (beat-the-books continuation) had F31/F32 in cycle
1 citing paraphrased line ranges (`bets.py:359-425` was
approximated from recall rather than re-read). The wrong class was
implicit in the cited range; cycles 5 and 6 ran on the inaccurate
tracker; cycle 7 caught the discrepancy. The producing AI's
diagnosis: *"a tighter first cycle (actually read every cited
file:line, don't recall) would have cut probably 2 of the 8
cycles."*

§3.2 named the re-runnable basis requirement; compliance was
naked-judgment — the AI judged whether its cited basis satisfied
"located read of source" without producing the un-fakeable
artifact. The sharpening converts naked-judgment to artifact-
bearing: basis records include either the verbatim content at the
citation OR the executable search query and its output. Paraphrase
is no longer satisfiable as basis.

---

