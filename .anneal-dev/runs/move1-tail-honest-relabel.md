# Run: move1-tail-honest-relabel

- **Status:** IN-PROGRESS
- **Phase:** investigate-design
- **Mode:** interactive
- **Task:** Finish the Move-1 honest bind/surface relabel across the sites
  deferred from keystone release `819e84e` — the remaining
  generic-binding-overclaim sites the keystone left untouched. Move-1 of the
  intent-falsification soundness sweep (`dev-notes/backlog/intent-falsification-soundness-sweep.md`).

## Requirements record (task-input; separated from the proposed FQ-list solution)

- **Verbatim operator request:** "yes" — in response to "Want me to start on the
  Move-1 tail (the cleanest next step — finishes a shipped keystone), or do you
  want to settle the Move-2 fork first?"
- **R1** — No load-bearing artifact in the corpus overclaims its *binding*: a
  self-recorded / presence-only artifact is not labelled "verified" / "un-fakeable"
  / "guaranteed"; the real binding terminus (external-fact checker, or the
  operator's irreducible verdict) is named, per the canonical §3.1 gradient.
- **R2** — The relabel is *consistent with* the canonical §3.1 bind/surface
  gradient already shipped (`819e84e`); it cross-references §3.1, it does not state
  a second (driftable) copy of the principle.
- **R3** — Removing overclaims must not *under-claim* the genuine binding legs:
  render-fidelity (no-in-context) binds, the operator step-4 soundness verdict
  binds, the git-log handoff leg binds. Honesty cuts both ways.
- **R4** — Completeness: every remaining Move-1-character overclaim site is either
  fixed *or* its deferral recorded with a cited basis (no silent drop); the FQ-B
  falsification-label residual is dispositioned, not assumed.

## F-track (findings)

- **F1** [VERIFIED — non-issue] Hook pass-line (`commit-msg:396` "Discharge
  artifact validation passed") has no external dependent: the only repo
  occurrences are the hook itself (`commit-msg:385`/`:396`) and the sweep backlog
  note — no test asserts the string (sole hook test is `test_skill_craft_pre_edit.py`;
  no `test_commit_msg*`). — basis: `grep -rniE 'validation passed|Discharge artifact validation'` (this cycle) → 3 hits, 2 self + 1 backlog; `ls hooks/*test*` → one file.
- **F2** [PENDING] Fragmentation guard: the bind/surface principle is canonical at
  `core.md` §3.1; both relabels (D2/D3) must *cross-reference* it, not restate the
  gradient (a second copy can drift). — basis: `core.md`:142-165 read this cycle (§3.1 carries the producer-independence bind test + strong-surfacer + operator-detection fence).
- **F3** [PENDING] Over-claimed-verification (reverse guard, R3): the relabels must
  not under-claim the real binding legs — render-fidelity no-in-context, operator
  step-4, git-log handoff all genuinely BIND. — basis: `core.md`:147-160 (binding termini enumerated) + `development-process.md`:548-551 (handoff-marker leg "**binds**") read this cycle.
- **F4** [VERIFIED — non-issue] FQ-B·pass7 (falsification "holds"/"clean" labels)
  Move-1-character residual is ALREADY discharged: the intent-falsification "clean"
  carries its honest caveat at point of use ("**not a soundness certificate**",
  "vacuously satisfiable", "feeds … never substitutes"); the mechanical "holds" is
  operationally defined (predicate-applied-to-result), carrying no generic binding
  overclaim. — basis: `core.md`:547-550 + :500-506; `modules.md`:435-442; mechanical pass `core.md`:454-481 read this cycle.

## D-track (design decisions)

- **D1** [VERIFIED] **Scope** = the corpus sites where a load-bearing artifact's
  *binding* is overclaimed in Move-1's generic-attribution character ("un-fakeable",
  an unqualified "validation passed" pass-signal, "the guarantee comes from …") AND
  not yet reconciled by the keystone. Members: {`hooks/commit-msg:396` (+the
  kernel-only narrow note 104-107/398-404), `development-process.md:438`}. — basis (completeness, this cycle): `un-?fakeable` → 2 hits (`core.md:122` = the honest gradient statement, NOT an overclaim; `development-process.md:438` = the overclaim, in); `Discharge artifact|validation passed` → `commit-msg:396`; `guarantee` → no remaining overclaim (`core.md:153` is the new honest "not a guarantee"); `structural(ly)? enforce` → all reconciled (`development-process.md:391`/:470/:546 read this cycle, each already weak-artifact/bind-surface-split).
- **D2** [PENDING] **FQ-5 — generalize the hook PASS-signal disclaimer.** Target:
  `hooks/commit-msg` PASS-path stdout (machinery). Shape (delta): the green-✓ line
  currently reads "Discharge artifact validation passed" unqualified, and the
  presence≠verification disclaimer (`FOUNDATION_INVARIANT_PASS_NOTE`) fires ONLY
  `if has_kernel` and only about the foundation-invariant check. Amend so the PASS
  output, for ALL rule-corpus commits, names what the gate actually binds (the
  discharge *form*: required checks present, N/A conditions, verdict-lines) and
  disclaims what it does NOT (soundness — the operator step-4 verdict and the
  binding verify legs are the real termini), referencing `core.md` §3.1's
  bind/surface gradient. Keep the kernel-specific invariant note as an additional
  kernel-only line. Acceptance: a non-kernel rule-corpus commit's PASS output
  carries the presence≠verification framing; `python hooks/test_skill_craft_pre_edit.py`
  still green (no commit-msg test exists). Realization wording at impl. — basis: F1 (no dependent), `commit-msg`:104-107/396-404 read this cycle.
- **D3** [PENDING] **dev-process:438 — relabel the practice-11 keep-as-is "un-fakeable
  evidence".** Target: `development-process.md:438` ("The named loss is the un-fakeable
  evidence the keep is defensible"). Shape (delta, one sentence): → "the named loss is
  the evidence the operator second-judges the keep on" (or equivalent) — a
  first-judge-authored named-loss is a *self-recorded* artifact (weak / strong-surfacer
  per §3.1), its correctness operator-re-derivable; not absolutely un-fakeable.
  Consistent with the SAME practice's own :470-474 ("the table is a **weak** artifact …
  surfaces for the operator second-judge") and §3.1. Acceptance: no "un-fakeable" left in
  `development-process.md`; the sentence coheres with :470-474 and :440 ("Operator's
  second-judge"). Realization wording at impl. — basis: `development-process.md`:438 + :440 + :470-474 read this cycle; `un-?fakeable` search (D1) leaves :438 as the sole remaining overclaim.
- **D4** [VERIFIED] **Defer FQ-B (falsification "holds"/"clean" labels) to Moves 3/5.**
  The Move-1-character relabel is already present (F4); the genuine residual is
  enum-exhaustiveness — the closed 3-shape/3-predicate enum needs an exhaustiveness
  basis or explicit residual (**Move-5**, the V-26-reversal root) — and carry-the-caveat-
  to-the-mechanical-"holds"-site (**Move-3**). Neither is Move-1's generic-binding-overclaim
  character. Committed deferral. — basis: F4 + the sweep item's own Move-3 (line 170) and Move-5 (lines 175-177) assignments of the "holds" site.

### Cycle 2 appends (design-completion — lock D2/D3, discharge F2/F3)

- **F2** [VERIFIED — addressed] Fragmentation guard addressed by D2/D3's contracts:
  both relabels cross-reference `core.md` §3.1 rather than restating the gradient
  (D2 references §3.1's bind/surface; D3 inherits the same-practice :470-474 weak-artifact
  framing which already cites §3.1). — basis: D2 + D3 acceptance criteria (this cycle) name the §3.1 cross-ref; no second gradient statement is authored.
- **F3** [VERIFIED — addressed] Reverse-guard addressed by D2/D3's contracts: D2 preserves
  the binding-leg naming (render-fidelity no-in-context + operator step-4 still named as the
  real termini); D3 reframes to "operator second-judges" (does not deny the named-loss is
  load-bearing evidence, only that it is *self*-recorded / operator-re-derivable). — basis: D2/D3 acceptance (this cycle); `core.md`:147-160 binding termini preserved verbatim in the design.
- **D2** [VERIFIED] FQ-5 hook PASS-signal disclaimer — realization-ready. Contract pinned
  (impl introduces no new design decision): on the PASS path, for ALL rule-corpus commits,
  the hook prints a disclaimer that (i) names what the gate binds — the discharge *form*
  (required checks present, N/A conditions, verdict-lines parsed) — and (ii) disclaims
  soundness (the operator step-4 verdict + the binding verify legs are the real termini),
  (iii) referencing `core.md` §3.1's bind/surface gradient; the existing kernel-only
  `FOUNDATION_INVARIANT_PASS_NOTE` stays as an additional `if has_kernel` line. Exact
  string = realization (impl). — basis: F1 (no dependent), F2/F3 (guards folded in), `commit-msg`:104-107/396-404 (the structure to amend) read cycles 1-2.
- **D3** [VERIFIED] dev-process:438 relabel — realization-ready. Contract pinned: replace the
  one sentence so the first-judge-named loss is framed as the evidence the operator
  *second-judges* the keep on (a self-recorded → weak/strong-surfacer artifact per §3.1),
  dropping the absolute "un-fakeable"; cohere with :440 + :470-474. Exact wording = realization
  (impl). — basis: F1 (no cross-ref dependent), `development-process.md`:438/:440/:470-474 read cycle 1; the `un-?fakeable` search leaves :438 the sole site.
