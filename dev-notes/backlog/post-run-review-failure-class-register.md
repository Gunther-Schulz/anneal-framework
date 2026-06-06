# Post-run review should probe a maintained failure-class register (proactive per-class, not only reactive defect-listing)

**Status:** OPEN — operator-raised 2026-06-05 (during the clippy 6-bug retrospective integration; "I want [the self-review] to capture as many failure classes as possible"). Framework-spec (`spec/modules.md` §4 post-run-review minimum-shape — **method-kernel**) + `post-run-review.md` (the procedure, corpus-evolution) → anneal-dev + kernel-independent verify (the modules §4 part is method-kernel). NOT urgent; a design to work out.

## The gap
The post-run review's **Q1 (Misses)** is **reactive**: "list every design defect the run *produced*, classify escape/operator-catch, name which check should have caught it (or 'no existing check covers this class')." But the dominant failure shape (`design-decision-implication-depth-gaps`: *"saw the fact, didn't connect it to the decision"*) means **a model that missed an implication in-run also misses flagging it in self-review** — the same reasoning-depth ceiling operates in both passes. Q1 catches what the model spontaneously recognizes as a defect; it does NOT *proactively* ask "did this run exhibit failure-class X?" for each known class. So a run that exhibited a known class without the model noticing slips Q1.

The clippy retrospective was, in effect, a **manual cross-run post-run review** — and it caught classes the per-run post-run review didn't. That's the evidence the self-review under-probes.

## The fix shape (anneal-native — a register the self-review consumes)
A maintained **failure-class register** the post-run-review self-review probes **per-run**: for each catalogued class, "did this run exhibit it? — cite evidence (quote/file:line) or `clean`." Artifact-forcing per `modules.md` §4.4 (per-class evidence, not generic mush). **Additive**, not a replacement.

**Consolidates the scattered catalogs** (Pareto — one probe-list vs N scattered):
- V-30 `form-not-binding-class-recurrence` classes (i)–(iv).
- `design-decision-implication-depth-gaps` — reasoning-depth-at-design-lock (premature-categorization, execution-context, write-without-reader).
- `framework-blindspot-class-analysis` — proactively-enumerated classes (the register is where its output lands — that item currently feeds "tier-4 + the sweep"; add "+ the post-run-review register").
- `instance-domain-invariant-register` — cross-unit-invariant / inherited-surface classes (instance layer).

**Likely layered** (framework ∪ instance), mirroring `foundation-invariant register` (framework) ↔ `instance-domain-invariant-register` (instance): general classes (reasoning-depth, write-without-reader) at the framework layer; domain classes (execution-context = coding; cross-unit-invariant = clippy) at the instance layer. A failure-class register is the **dual** of the invariant registers — invariants = what must hold (positive); failure-classes = what tends to break (negative).

## Load-bearing disciplines (state both in the design, or it oversells)
1. **Additive, not blinders.** The operator's own lens-narrowness insight applies to the register itself: a fixed catalog becomes blinders if it *replaces* the open-ended probe. It MUST compose with Q1's "no existing check covers this class" (the novel-class surfacer), and **novel classes found feed BACK into the register** (it grows; it is the accumulated institutional memory of failure modes, not a frozen list).
2. **Regression-guard, not ceiling-fix.** A register-probe catches **known** classes recurring. It does NOT fix the underlying reasoning-depth ceiling (`design-decision-implication-depth-gaps` cross-class obs 3: *reducible, not eliminable* by process). It raises the floor, not the ceiling — say so, so it isn't sold as solving "saw it, didn't connect it."

## Design-quality probe-templates (operator's proving-questions — 2026-06-06)
A **second kind of probe** the self-review should run, distinct from the failure-class register
above: not "did this run exhibit known defect X?" (reactive pattern-match) but a **fresh
adversarial interrogation of each load-bearing decision's SHAPE / quality**. Surfaced
empirically — across a long 2026-06-06 session the operator's recurring "proving-questions"
repeatedly found gaps the framework's own checks (basis, missed-dependents, lenses,
intent-falsification) passed clean:
- **workaround-vs-principle** — "is this sound, or a workaround?"
- **proportionality** — "are we over-building / nitpicking?" (the additive-reflex)
- **default-justification** — "why this default — why not the opposite?"
- **altitude / scope** — "is this the right level?"
- **front-loading / simplicity** — "can this be caught earlier / done simpler?"
- **precedent-linking** — "does this connect to a known pattern / backlog item?"

These attack the decision's **quality**, not its basis (the mechanical checks cover basis).
They are **design-time-cheapest** — the convergence **intent-falsification pass** is the natural
home to ADD them as attack-criteria (catch them before ship) — AND a **post-review backstop**
(the retrospective notices "did the run lean on the operator's live probing to find gaps the
framework should have caught?").

**Load-bearing caveats (state both, or it oversells):**
1. **Floor, not ceiling.** Encoding the probes raises the floor but cannot replace the operator:
   a self-asked adversarial question can be **vacuously satisfied** (the intent-pass's own
   acknowledged weakness — `core.md §4.1.4`: the per-R# line "can be vacuously satisfied"). A
   fresh *human* adversary asking "is this a workaround?" is harder to fool than the AI asking
   itself. The operator's live probing keeps irreducible value — same reducible-not-eliminable
   ceiling as `design-decision-implication-depth-gaps` cross-class obs 3.
2. **Seed, not bound.** The probe-list seeds the interrogation; it must not become a fixed
   checklist the AI runs-and-stops (skill-craft "Checklist as ceiling"). Trace each probe's
   lead beyond the list.

**Empirical base (2026-06-06 session):** workaround-probe pressure-tested the integrity-check fix
(confirmed sound — but the question forced the justification); proportionality caught the
v-entry gold-plating (→ `convergence-surfaced-finding-action-brake`); default-justification
flipped runs-data off→on; altitude reframed runs-data this-repo→framework; front-loading
simplified archive→track-in-place; precedent-linking surfaced
`design-decision-implication-depth-gaps`.

## Design questions to resolve (anneal-dev cycle)
- Register home + layering (framework vs instance; one file or a slot like the invariant registers).
- Probe shape in `modules.md` §4 / `post-run-review.md` Q-set: a new Q (Q8?) or an extension of Q1; the per-class evidence/clean artifact.
- The feed-back loop (novel class → register entry) — who adds, when (at post-run review close?).
- Composition with V-30 (the recurrence WATCH) — is the register V-30's catalog made first-class? (V-30 currently lists the 4 classes inline.)
- Composition with `framework-blindspot-class-analysis` (the proactive enumeration that POPULATES the register).

## Relates to
- `framework-blindspot-class-analysis` — the proactive-enumeration method that POPULATES the register (its output sink); composes.
- V-30 `form-not-binding-class-recurrence` — the recurrence WATCH whose 4-class catalog this register would make first-class.
- `design-decision-implication-depth-gaps` + `instance-domain-invariant-register` — two source catalogs (the clippy retrospective's two halves).
- `surface-non-task-observations` (campaign ③) — sibling "surface what the agent notices" channel; distinct (that = outside-task observations; this = a known-failure-class probe in the self-review).
- `spec/modules.md` §4 + `post-run-review.md` — the edit sites; `foundation-invariant register` (`dev-notes/foundation-invariants/`) — the architectural sibling (a register a pass probes).
- Origin: the clippy 6-bug retrospective (operator, 2026-06-05).
