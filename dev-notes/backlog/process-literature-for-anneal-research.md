# Mine the established process/methodology literature for anneal (research)

**Status:** RESEARCH RUN DONE (clean solo re-run `wf_2e04dc82-38b`, task `w9dtzvm33`, 2026-06-03;
the first concurrent attempt `wzda05eyc` broke in the 3-run overload). 22 sources, 100 claims,
top-25 adversarially verified (22 confirmed / 3 killed) — unusually strong (canonical
peer-reviewed primaries). Raw at `dev-notes/research/process-literature-deep-research-2026-06-03.raw.json`.
**The most actionable run of the session: it found concrete disciplines to ADOPT.** Verdict below.

## VERDICT (2026-06-03)
**Established methodology literature strongly VALIDATES anneal's architecture AND surfaces three
adoptable sharpenings + a reject-column.** Anneal-mappings are analogies (sources don't mention
anneal); each is well-sourced.

**Validation (anneal's pillars ≈ canonical disciplines):**
- evidence/basis rule ≈ **Zave & Jackson "designation"** (every primitive term grounded in a
  written, maintained, re-checkable environment referent; the paper notes *most methods fail to
  enforce this* — anneal does). ACM TOSEM 1997, canonical.
- coherent-complete-state ≈ **S,K⊢R completion criterion** + a consistency proof (same paper).
- structured convergence (loopback) ≈ **Platt's "recycle" step (1')**; falsification ≈ Popper/Platt.
- independent verify ≈ Cleanroom pre-execution review — but the strong *lineage* claim was REFUTED
  (1-2); only the design-first **economics** survive (and 90%/60% is originator self-report,
  medium-confidence, directionally corroborated by Selby & Basili).

**⭐ THREE adoptable sharpenings (candidate kernel edits → must route through anneal-dev + skill-craft + operator-soundness):**
1. **Multiple working hypotheses (Chamberlin 1897 / Platt) — the genuine GAP.** Carry several rival
   designs *in parallel* during investigate-design, none personally owned → neutralizes the
   "parental affection" attachment bias + forces completeness. The run **checked anneal's actual
   corpus**: `investigate-design.md` drives to a SINGLE committed recommendation; the operator is
   never posed rivals; the "considered" field is optional/post-hoc; falsification probes an
   already-LOCKED single decision. So anneal genuinely lacks this. **Partial mitigation:**
   separate-context verify attacks the same bias by a different route. **Design tension to resolve
   (key):** can rivals be carried *internally* during investigate-design while still surfacing ONE
   committed recommendation (anneal's deliberate anti-menu-paralysis stance)? — or do they conflict?
2. **Exclusion / soundness obligation at verify (Gunter et al. WRSPM, ICRE 2000).** "Entailment +
   nothing-dropped" is **provably insufficient**: the S1∨S2 disjunctive counterexample passes
   adequacy + consistency yet "breaks as soon as deployed." Fix: verify must **EXCLUDE rival/broken
   accounts of the state, not merely confirm one.** Converges with Platt's *"any conclusion that is
   not an exclusion is insecure and must be rechecked."*
3. **Falsifiability gate on the basis rule (cheapest, highest-leverage sharpening).** Every basis
   claim must state **what would disconfirm it** — strictly SHARPER than "grounded in re-checkable
   evidence" (re-checkability is satisfiable by confirming-only evidence; falsifiability is not).
   Low cost — mostly a phrasing/discipline change to an existing rule.

**Reject-column (adopt the discipline, NOT the over-claims):** O'Donohue & Buchanan (2001) +
Quine-Duhem show Strong Inference's strong promises fail — a single "crucial experiment" is
logically inconclusive; complete hypothesis-enumeration is impossible for open problems. So take
multiple-hypotheses + exclusion, but **never** import "one decisive falsification settles it."
**Quine-Duhem actually REINFORCES anneal:** if even a falsification is provisional, a *non*-falsified
claim is a fortiori not-yet-settled → exactly anneal's recheck/loopback posture.

**Lightweight / probably-reject:** IBIS/gIBIS (Issue/Position/Argument grammar) — anneal's
basis + "considered" field captures rationale more lightly; full IBIS is heavyweight capture
overhead that conflicts with the committed-recommendation style.

**Honesty gaps (open):** **Boehm's cost-escalation curve / 1:10:100 was NOT verified** (may be a
repeated estimate — design-first economics here rest on Cleanroom, not Boehm); **FMEA/HAZOP/Fagan
produced ZERO surviving claims** → "anneal's lens-set is FMEA-like" is unverified; warrants a
dedicated follow-up. Toulmin = framing only, unverified.

## Origin
The placement deep-research found APF (arXiv 2602.19065) is built on **Problem Frames**
(Michael Jackson) — which revealed an unmined vein: **anneal is essentially a
requirements-and-evidence discipline for open-ended AI work, and classical RE / process
literature has decades of relevant thinking anneal has never sourced.** Highest-value vein.

## Veins researched (leads)
- **Requirements engineering** — Problem Frames (Jackson); Zave & Jackson, *"Four Dark Corners
  of Requirements Engineering"*; the `S, K ⊢ R` entailment as a *completion* criterion. Richest.
- **Popper / Platt "Strong Inference" (1964)** — the methodology behind anneal's falsification step.
- **Design rationale / argumentation** — Toulmin (claim–grounds–warrant); IBIS/gIBIS.
- **Software inspection** — Fagan inspections; Cleanroom SE — the independent-review lineage.
- **Failure-mode methods** — FMEA, HAZOP — anneal's lens-set is FMEA-like.
- **SE economics of design-first vs iterative ordering** — Boehm's cost-of-defect-escalation
  curve (defect cost rises with detection lateness); upfront-design-vs-agile evidence. (The
  *agent-space* side of the ordering question is the separate `design-first-vs-act-first-research.md`
  run; this vein is the *established-SE* economics only — kept disjoint to avoid overlap.)

## Sharpened deep-research question (as fired)
> Survey the established process/methodology literature for reliable knowledge-work; identify
> disciplines the Anneal framework could ADOPT or should consciously REJECT. Cover the six veins
> above. For EACH: (a) borrowable mechanism, (b) what anneal already has equal/better, (c) cost
> of adopting. Do NOT default to "anneal already covers it" — hunt for a genuinely missing
> discipline. Adversarially verify; cite; flag peer-reviewed vs preprint vs textbook.

## Relates to
- `anneal-placement-and-improvement-research.md` (sibling research; the APF → Problem-Frames
  origin that surfaced this).
- `design-first-vs-act-first-research.md` (the agent-space side of the ordering question; this
  run carries the SE-economics side).
- `multivoter-verify-no-predicate-claims.md` + `verify-techniques-research.md` (Fagan/Cleanroom
  inspection lineage overlaps the verify-techniques run — the SE-process vs LLM-technique split
  keeps them disjoint).
