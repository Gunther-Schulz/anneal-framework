# Method-kernel edit — where the operator's irreducible soundness verdict actually binds (the [READY]-vs-step-4 split)

**Status:** [READY] — process-clarity gap, surfaced 2026-06-05 by running the `move1-s3.1-honest-relabel`
anneal-dev cycle (a method-kernel edit). Low-to-medium severity; a specification/framing gap in
`development-process.md`'s method-kernel rule, not a behavior bug. **Next action:** decide whether to sharpen
the method-kernel-edit verify discipline to name the two soundness touchpoints explicitly; if so, a small
anneal-dev cycle on `development-process.md` §1 (+ `core.md`/`foundations.md` if the [READY] framing restates it).

## The gap
For a method-kernel edit, the framework says anneal-dev never self-certifies — verify **must** add a
kernel-independent review (skill-craft form + **operator soundness**), recorded at **release-loop step 4**
(`development-process.md` §1). But in an interactive run there are actually **two** operator soundness
touchpoints, and the process treats "the operator's soundness verdict" as a single moment:

1. **[READY] / `next phase`** — the operator locks the **design SHAPE** (the method change's correctness in
   the abstract). Per practice 5, the exact rule WORDING does not exist yet (drafting is file-bound, produced
   at impl).
2. **Release-loop step 4 (post-impl/verify)** — the kernel-independent review of the **rendered change** (the
   actual produced text), with the foundation-invariant focusing artifact.

**The problem:** the *soundness-critical* part can live in the realization WORDING, which is produced at impl
— **after** the [READY] soundness gate. Concrete instance: move-1's **F-B** finding was that the §3.1 text must
*fence* "operator surfaces / second-judges" (permitted) from "an author-side check downgraded to the operator"
(the forbidden operator-detection-as-enforcement, `core.md` L69-78) — and that fence is a **realization-wording**
judgment that doesn't exist at [READY]. So the thing most needing the operator's soundness eye isn't present at
the moment the run frames as "originates the soundness verdict."

The seam is real and handled in practice (step-4 catches the wording), but **which verdict binds where — and that
the wording-critical half is necessarily post-[READY] — is not crisply specified.** A run (or an AI presenting the
[READY] gate, as happened here) can conflate the two and over-state what the [READY] selection certifies.

## Possible shapes (not yet decided)
- Name the two touchpoints explicitly in the method-kernel rule: [READY] = design-shape soundness; step-4 =
  rendered-wording + kernel-independent review. Cheap clarification.
- At [READY] for a method-kernel edit, the closed artifact's recommendation explicitly flags "design-shape only;
  wording-soundness deferred to step-4" so the operator isn't misled.
- Consider whether any surfaced realization-wording residual (an F-B-shaped finding) should be a *required*
  carry-forward into the step-4 discharge, not just a [VERIFIED — surfaced] note.

## Relates to
- The method-kernel rule: `development-process.md` §1 ("Dev-on-anneal" / method-kernel edit) + release-loop
  step 4.
- `intent-falsification-soundness-sweep` — sibling: that sweep found the operator is the irreducible binding
  terminus; this item is about *where in the run* that terminus actually engages for a kernel edit.
- Surfaced from the `move1-s3.1-honest-relabel` run (F-B [VERIFIED — surfaced]; tracker in `.anneal-dev/runs/`).
