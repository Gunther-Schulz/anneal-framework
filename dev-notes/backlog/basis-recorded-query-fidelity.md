# Recorded-basis-query fidelity isn't mechanically enforced (only conclusion-correctness is)

**Status:** OPEN — **watch-bearing backlog item** (n=1; no fix now, watch for recurrence), disposition set 2026-06-05 by campaign ③ run `campaign3-enforcement-fidelity` (D2). Kept here as a **backlog item carrying its watch criteria inline** — NOT converted to a validation-watch V-entry — per the operator's V-vs-backlog clarification (a V-entry is a *post-ship effect-watch*; a not-yet-implemented consideration stays a visible backlog item; see `v-entry-is-post-ship-only.md`). The decision: do NOT build the forcing-function at n=1 (practice 7 no-over-build); **soundness is preserved by the separate-checker re-deriving the conclusion** — only the audit trail degrades (campaign ③ F5/F6, verified by the cycle-3 intent pass).

**Watch criteria (inline):**
- **watch-kind:** recorded-query-fidelity (correctness/audit-trail).
- **catcher:** the convergence coverage-check (`core.md` §4.1.4) / a future operator catch.
- **closing rule (→ build the forcing-function):** a recorded-but-false-**as-written** query passes the mechanical check (the conclusion was re-derived correct but the cited query, re-run verbatim, does NOT reproduce it AND that slips), **OR** n≥2 distinct recurrences. Then build candidate-(b): the coverage-check compares the AI's recorded query against the subagent's re-derived candidate and flags a mismatch (a §4.1.4 coverage-check clause — mechanical predicate, not narrative goodwill).
- **how the signal accrues:** post-run-review attribution (which pass surfaced the basis defect) — no dedicated instrument.

Original framing — method-kernel dogfood observation, **n=1**, surfaced 2026-06-04 by the
`verify-vs-original-requirements` anneal-dev run (cycle-4 convergence falsification, handoff
`a3ce2e1c8a1d14f59`, on its `D1` basis). Framework-spec (§3.2 basis rule + §4.1.4 falsification) → anneal-dev
+ kernel-independent verify when/if pursued.

## The observation
The basis rule (`core.md` §3.2 / `foundations.md`) requires a completeness claim's basis to be **the
re-runnable search itself — the executable query, not a paraphrase**. In the run, `D1`'s recorded basis
was a *reconstructed* glob (`ls */phases/investigate-design.md → 3`) that resolves to **1** from the
repo root (the corpus is multi-repo; the instances are sibling repos) — i.e. an imprecise recording of
the actual multi-repo search that was run. **The convergence/falsification pass caught it — but via the
subagent's narrative side-note ("reported, not judged"), NOT a mechanical predicate.** The mechanical
falsification validated the *conclusion* (the subagent re-derived the scope with its **own** correct
search → HELD); it did not check whether the AI's **recorded query is itself re-runnable-as-written**.

**The gap, precisely:** the convergence coverage-check mechanically verifies a basis's **conclusion**
(by independent re-derivation); it does **not** mechanically verify **recorded-query fidelity** (does
the cited query, re-run, reproduce the claimed result?). A reconstructed-but-conclusion-true basis
passes the mechanical check.

## Soundness vs audit-trail (why it's subtle, not a hole)
**Soundness is preserved** — the separate checker re-derives the conclusion independently, so an
imprecise recorded query doesn't corrupt the verdict. What degrades is the **audit trail**: the
recorded basis isn't faithfully re-runnable, so a future reader/re-check can't rely on the cited query
as written. The framework's "weak artifact + separate checker" design absorbed it (this is mostly the
method **working** — the convergence cycle caught an authoring error). The residual is that the catch
rested on subagent *diligence*, not a forcing function.

## Triage (practice 1)
- Primarily **adherence** — the rule forbids paraphrasing a search; it was violated and caught.
- Possible **spec-sharpening** (genuine uncertainty → the validation-watch flavor): is the
  separate-checker sufficient (practice-7 no-over-build), or add a forcing function? Candidates if
  pursued: (a) a write-time discipline — "record the **verbatim executed** query, not a reconstruction";
  (b) the falsification coverage-check compares the AI's recorded query against the subagent's
  re-derived candidate and flags a mismatch (a mechanical predicate, not narrative goodwill).
- **Recommendation:** do NOT reflexively add machinery at n=1; watch for recurrence. If it recurs
  (n≥2) or a recorded-but-false basis ever passes mechanically, the forcing-function (b) earns its
  place (practice 8 structural enforcement).

## Relates to
- `verified-integrity-consolidation` — DISTINCT: that is [VERIFIED]-claims-more-than-checked at the
  *conclusion* level; this is *recorded-query fidelity* with the conclusion intact.
- `structural-change-dependent-enumeration` (Missed-dependents / basis-completeness family).
- Origin run: `.anneal-dev/runs/verify-vs-original-requirements.md` (D1 + its cycle-4 basis sub-annotation).
