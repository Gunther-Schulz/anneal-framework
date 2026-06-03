# Adoption: retire development-process.md's shadow-copy method, delegate to anneal-dev

**Status:** **IMPLEMENTED 2026-06-02** — corpus change verify-clean (two
separate-context reviews, PASS-with-fixes, fixes applied), pending operator commit
approval at the step-4 discharge. The adoption phase of [[framework-dev-as-anneal]].
**FOUNDATIONAL.**

## Implemented (2026-06-02)

**Shipped (6 corpus files):** `development-process.md` reframed (two-regime →
one-process intro; "three levels" collapsed to a `foundation.md` pointer; practice 2
thinned to its canonical homes; validation-watch path-fixes ×3; release-loop framing
note) + process-pointers re-pointed to the model in `CLAUDE.md` (grounding gate),
`instantiation-guide.md` (§6 + seed block), `instance-template/CLAUDE.md`,
`README.md`, `spec/README.md`.

**The B1 table over-scoped — the real reduction was surgical.** Most practices are
genuine framework-dev machinery the bootstrap regime applies directly (this cycle
*used* P3/P4/P9/P11). Only ad-hoc *method-paraphrase* thinned (P2, the three-levels
prose). P1 + P3–P12 + the release machinery **stayed**.

**Decision 1 reversed:** the render/spec/adherence triage **stays in P1** — moving it
into the rendered `post-run-review.md` would multiply copies (the fragmentation the
effort fights). Avoided re-pointing `post-run-review.md` / `modules.md` / `glossary.md`.

**Bootstrap rule refined (operator-driven, mid-cycle) → [[framework-dev-as-anneal]].**
Not "kernel work is hands-off anneal-dev." Accurate invariant: **everything runs
through anneal-dev; a *method-kernel edit* (file in `anneal-framework/spec/*` /
`foundation.md` / `anneal-dev/spec/*`) adds one rule — anneal-dev never self-certifies
its own foundation, so verify adds a kernel-independent review = skill-craft (form) +
operator (soundness).** Driving is never optional (no trivial-edit carve-out — that's
the general V-27 ceremony question, not a kernel rule).

**Follow-ups filed:** [[anneal-dev-packaging]] (install so "run anneal-dev" is
invocable, not just followed-in-context); [[adoption-instance-settlement]] (re-point
clippy/daneel/campaign CLAUDE.md seed blocks); [[skill-craft-pre-edit-hook-findings]]
Finding 3 **elevated** (the hook ↔ anneal-dev subagent-dispatch seam is now the dev
process's normal path, not a dogfood edge).

## What the classification found (subagent `aded70906aad5656f`, full citations there)

`development-process.md` (666 lines, 12 practices + release loop + "three levels")
splits into **three layers**, not two:

1. **Generic anneal method** → now carried by **anneal-dev** (the instance).
   Practices 2, 3, 6, 9, 10, release-loop steps 1–4, and the method-halves of
   1/4/5/7/8/11/12. These re-point to anneal-dev's phases / foundations / lenses /
   verify battery.
2. **Corpus-evolution domain bindings** → **already in `anneal-dev/spec/bindings.md`**:
   the three-level architecture, the wrap-tolerant + multi-repo practice-4
   search/scope, the lens set, the verify battery. (anneal-dev *has* slots for these.)
3. **Framework-dev-PROCESS machinery** → has **NO anneal-dev slot** (correctly — it
   is neither generic method nor corpus-evolution domain-binding; it is "how *this
   team* ships changes to *these* repos"):
   - validation-watch (V-N register) governance — practice 8 ¶3–4 + practice 12
     trigger (the **most-cited** content: 18 `validation-watch.md` sites);
   - the **skill-craft pre-edit hook gate** (practice 5) — operator-session
     PreToolUse discipline, and it *collides* with anneal-dev's subagent dispatch
     (forced spawn-fallback in the dogfood);
   - the **release / marketplace loop** (steps 5–6: commit/push/version-bump/
     `claude plugin update`/`/reload-plugins`) — post-verify operator-side packaging;
   - the **coherence-audit cadence** (practice 12: N-cycles + `Coherence-audit-handoff:`
     git marker) — cross-commit release-cadence;
   - the **practice-11 findings-table** + **practice-4 audit-artifact** shapes —
     operator-presentation/discharge conventions (anneal-dev presents via its closed
     artifact, not these).

## The decision (B1 vs B2)

- **B1 — three-layer split (RECOMMENDED).** Delete the duplicated *method* from
  development-process.md (re-point to anneal-dev); keep the doc as the **home of
  layer-3** (the framework-dev-process machinery above), much slimmer. "Run
  anneal-dev for dev work + these residual dev-process bindings."
- **B2 — migrate layer-3 into anneal-dev + retire dev-process to a redirect stub.**
  **Rejected:** layer-3 has no anneal-dev slot, and the instantiation-guide slot set
  is **closed** (instances fill declared slots, don't invent). Forcing layer-3 in
  either violates that contract or pollutes anneal-dev's clean per-run instance model
  with cross-run / operator-session / release machinery that isn't its concern.

**Decision: B1 — LOCKED 2026-06-02 (operator).** The shadow-copy *method* dies (the effort's goal); the
genuinely-residual layer-3 stays where it belongs (a framework-dev doc), because
it is not domain-binding and anneal-dev correctly has no home for it.

## Practice-4 dependent scope (~84 sites / 28 files; full table in the subagent report)
- **method-references (~22)** → re-point to anneal-dev (+ glossary/modules where the
  triage already lives): the practice-1 render/spec/adherence-gap triage cluster.
- **binding-references (~30, dominated by validation-watch's 18)** → re-point to the
  residual dev-process layer-3 doc (or foundation.md for the three-level/contract refs).
- **process-pointers (~32)** → re-point to the slimmed dev-process / dual-source.

## Hard cases the implementation must resolve (condensed; full list in subagent report)
1. **CLAUDE.md per-edit-cycle grounding gate assumes ONE governing doc** (`CLAUDE.md:7`;
   instance-template + clippy/daneel CLAUDE.md "the procedure is development-process.md").
   Must re-point to dual source (anneal-dev method + residual layer-3 doc), and
   `instantiation-guide.md:435` seeds this into every future instance.
2. **The pre-edit hook** cites "practice 5" + regex-matches `development-process.md` as
   a gated path — update citations; decide if the gate survives as layer-3 (it has no
   anneal-dev slot and collides with dispatch).
3. **Release loop** is an M/B/P braid — steps 1–4 → anneal-dev; the operator-approval-
   before-commit gate maps to anneal-dev's *downstream* commit gate (not a battery check);
   steps 5–6 → layer-3 (at most the re-render+diff maps to the `on-verify-PASSED` extension).
4. **Validation-watch governance** (18+ sites, spec-wired) → layer-3; re-point all.
5. **Practice-1 triage** splits — its placement-rule is layer-3, its triage is already
   M (glossary + modules §4 + rendered post-run-reviews); don't orphan the triage's
   home of record.
6. **Practice-11 table / practice-4 artifact shapes** — layer-3 presentation conventions
   or dropped for anneal-dev's native artifacts.
7. **Release-loop step 7's self-referential "process changes back into this document"** —
   rewrite (method-changes → anneal-dev/spec; binding-changes → layer-3 doc) or it
   instructs maintaining the shadow copy.
8. Two micro-fix backlog items (`dev-process-validation-watch-path`, `backlog/README:89`
   stale cross-ref) are absorbed/mooted by adoption — fold in, don't separately track.

## Open sub-questions folded in (not separate efforts)
- **Enforcement hook** ("always use anneal-dev for dev work") — decide here, not
  reflexively. Lean: no new hook; existing gate + a CLAUDE.md "invoke anneal-dev"
  discipline likely suffices (practice-8 mitigation-form decision).
- **Packaging anneal-dev** for real install (marketplace.json + register) — sequence
  with adoption (so promotion + install land together).

## Next action
**B1 locked.** Next: a dedicated implementation cycle (its own focused session —
foundational, high self-validation risk): re-ground in development-process.md (per
edit cycle), extract the duplicated method → re-point the ~84 dependents → reduce
dev-process to the layer-3 home → separate-context review. Resolve the 8 hard cases
above; the enforcement-hook + anneal-dev packaging questions fold in here. Relates to [[framework-dev-as-anneal]],
[[skill-craft-pre-edit-hook-findings]] (the hook re-citation), [[harness-tool-runstate-unsourced]].
