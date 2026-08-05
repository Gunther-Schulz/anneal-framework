# A wrong "non-issue" disposition at recording time shields the design from the entire lens apparatus

**Status:** [GATED] — surfaced 2026-06-06 by a **clippy** Unit-24 auto-battle run (project beat-the-books,
run `.clippy/runs/2026-06-06-unit-24-rejection-taxonomy.md`; carried in by the operator). A
**method-kernel** candidate (`spec/core.md` §3.x disposition definition + the falsification/verify
scope) + its instance render (`tracker.md` finding-state #3, `lenses.md`) → anneal-dev + kernel-
independent verify when pursued. **Deliberate, not now** — classify before any edit; respects the
bounded proof-first batch (see "Sequencing" below). Cross-instance datapoint (a sibling instance hit
a kernel gap — exactly the cross-instance value the framework is for).

## The failure (clippy Unit 24)
Investigation correctly surfaced: `autobet_decisions` carries no provider/book column — the
TicketCoordinator holds the provider in memory but doesn't write it to the decision row
(investigation's own words: "provider context available in memory but not written to audit"). That is
the textbook **Canonical-ID-dropped-at-handoff** shape. But it was recorded as:

> `F6 [VERIFIED — non-issue]` signal_id ends with `_<provider>` → provider extractable without migration

**The premise (provider not written to the row) is TRUE.** signal_id encoding the provider is a
**workaround** (recover the consequence by string-parsing a format convention), not a
**contradiction** of the premise. The disposition confused "a workaround exists" with "the premise is
false."

**Cascade:** `non-issue` → no D-entry → the design (D2) built provider categorization via
`signal_id.rsplit('_',1)[-1]` (string extraction) instead of a typed `book` column (matching the
existing `autobet_bets.book`). Two lenses never fired: **Canonical-ID-dropped-at-handoff** and
**Thorough-fix-default** (column = thorough; string-extraction = cost-clipped).

## Why it matters at the framework level — the two findings
**(A) The text is substantively correct but willed (loaded-but-inert).** Strict reading: form (b) of
`non-issue` requires "an observable fact **contradicting** the premise." A workaround does not
contradict the premise → clippy **misapplied** the existing text → adherence failure. BUT a competent
run misread it under cost pressure — the exact **loaded-but-inert / rigor-depends-on-choosing** class
(now named in `core.md` Purpose, the `purpose-mechanism-clause` run). The framework's own answer is
NOT "adhere harder" — make it structural. **Candidate (A):** sharpen `non-issue` to require the fact
make the **premise FALSE** (the dropped/missing/broken thing is actually present/correct), explicitly
excluding "the consequence is **recoverable** by other means." A recovery/workaround path is
`addressed` (a D-entry does the recovery) or stays `[PENDING]` (a design decision is owed) — **never**
`non-issue`. Converts a soft judgment into a bright-line test.

**(B) The deeper one — the disposition step is where cost-clipping hides from the thorough-fix lens,
and `non-issue` findings get the weakest separate-checking.**
- The cost-clip ("no migration", cheaper) **migrated into the finding disposition**, *upstream* of any
  D-entry. **Thorough-fix-default** is scoped to design **decisions** — it never sees a cost-clip that
  hid in a **finding closure**. So the disposition step is a blind spot for the thorough-fix discipline.
- A `[VERIFIED — non-issue]` finding that spawns **no D-entry** has the weakest separate-checking: the
  convergence **mechanical** pass iterates [VERIFIED] **D-entries** (not finding dispositions); and
  `verify-disposition-citation-reopen-explicit-leg` re-opens the citation's **truth** — but here the
  citation IS true (signal_id really does encode the provider). The defect is the **inference** (true
  fact → "contradicts premise"), which **nothing independently re-derives**. Per the just-shipped §3.1
  framing: the disposition is a **weak artifact** (a self-classification) that currently lacks a
  separate checker. **Candidate (B):** the falsification/verify apparatus should attack
  `[VERIFIED — non-issue]`/`deferred` **finding dispositions'** inference-validity (does the cited fact
  make the premise false, or merely recover its consequence?), not only D-entry bases + citation truth.

## Answering the operator's question
"Is the definition tight enough, or is this purely an adherence failure?" — **Both, and the dichotomy
is false.** Strictly it's an adherence failure (workaround ≠ contradiction, by correct reading). But
that a competent run misread it under cost pressure is the loaded-but-inert signal, so a structural
sharpening (A) IS warranted — not because the text is wrong, but because a willed judgment leaked. The
higher-value move is (B): the disposition step is an unguarded cost-clip-hiding locus.

## Sequencing (respect the bound)
This is the **same diagnosis** as the bounded proof-first enforcement-fidelity batch ("behavioral rule
loaded-but-doesn't-fire → structural enforcement"). The batch is **deliberately bounded**
(`convergence-cycle-mechanical-enforcement` + `skill-craft-antipatterns-loaded-but-inert`) — the bound
is what keeps fix-first finite. So **do NOT expand the batch with this**; slot it behind the proof
order (a sibling enforcement-fidelity item), or fold (A) opportunistically into a future
disposition/§4.3 de-pollution cycle.

## Relates to
- `verify-disposition-citation-reopen-explicit-leg` — **complementary, distinct**: that re-opens the
  citation's *truth*; this attacks the disposition's *inference-validity* (a true fact misused). The F6
  case re-opens citation-clean yet is still wrong → that leg would NOT catch it.
- `skill-craft-antipatterns-loaded-but-inert` / `convergence-cycle-mechanical-enforcement` — same
  loaded-but-inert family; same fix-shape (structural enforcement, not adhere-harder).
- `post-run-review-failure-class-register` — **a new class to catalog**: "disposition-misclassification
  shields design from lenses" / "workaround-as-contradiction."
- `convergence-surfaced-finding-action-brake` — the *mirror*: that brakes over-action on a finding
  (gold-plating); this catches under-action (a finding dodged via a wrong `non-issue`). The pair
  bracket the finding→action step on both sides.
- `core.md` Purpose "Mechanism: structural, not willed" (`purpose-mechanism-clause`) — this finding is
  a textbook instance of the class that clause names.
- Origin: clippy Unit-24 run (operator-carried, 2026-06-06).
