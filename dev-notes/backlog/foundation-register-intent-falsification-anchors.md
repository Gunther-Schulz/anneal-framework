# Foundation-invariants register — anchor the intent-falsification (validation) leg

**Status:** OPEN — operator-requested 2026-06-04, from a literature pass on
"the way we interpret intent falsification." A **foundation/method-kernel edit** to
`dev-notes/foundation-invariants/` → runs through **anneal-dev + the operator's
step-4 soundness pass** (`development-process.md` §2); per CLAUDE.md, re-ground in the
live co-located spec first. Adding a *new* invariant file is exempt from the
`Invariant-change-ratified:` marker (extending the register does not weaken the
foundation), but it is still foundation work — not a casual append.

## Why (the discovery)
A verified literature pass found that our **intent-falsification pass** (criteria-first
judgment attack on whether a locked design *serves its intent* — `spec/core.md` §4.1.4)
is a **composite of well-established, separately-authoritative ideas**, yet the register
currently anchors only the **mechanical/exclusion leg** (INV-4, INV-5 → Platt + WRSPM).
The **validation leg** — "does the design serve its intent," independent + criteria-first
— has **no anchored invariant**. Gap, not absence-of-source: the anchors exist and were
verified.

## Component → authoritative source (verified 2026-06-04)
- **Target — "does the design serve its *intent*" (≠ "is it built right")** →
  **Boehm**, validation vs verification ("are we building the right product?" =
  validation; "…the product right?" = verification). IEEE Software, 1984. Our
  intent-falsification pass *is* validation; the mechanical pass ≈ verification.
- **Independence lever (separate checker)** → **NASA IV&V**, formal three-fold
  independence (technical / managerial / financial); the IV&V org independently
  selects what to analyze. (NASA SWE-141; IEEE.)
- **Criteria-first precondition (a requirement must admit a falsifying check)** →
  **ISO/IEC/IEEE 29148** requirement *verifiability/testability*. Supporting citation
  only — a standalone "falsifiability-gate" was already *considered and excluded* from
  the register (README "Considered and excluded"); do not re-propose it as a slot.
- **Adversarial-role assignment (job is to attack, not approve)** → **Mason & Mitroff**,
  dialectical inquiry & devil's advocacy (*Challenging Strategic Planning Assumptions*,
  1981; Schwenk/Schweiger/Sandberg-Ragan empirics, 1980s AMJ/SMJ — both beat consensus).
  Roots: Churchman's dialectical inquiring systems.
- **Disconfirmation-first, in practice (AI-or-not)** → **Heuer**, Analysis of Competing
  Hypotheses (*Psychology of Intelligence Analysis*, CIA, 1999): seek facts that *refute*;
  reject the hypothesis with the most inconsistent evidence.
- **AI-native form** → **Irving, Christiano & Amodei**, "AI safety via debate"
  (arXiv:1805.00899, 2018): adversarial structure makes lying harder than refuting a lie;
  a **judge** (= our operator) decides — scalable oversight. Our criteria-first
  fresh-context attacker-feeding-the-operator ≈ single-sided debate-as-oversight.
  Near-misses to note (NOT anchors — they lack criteria-first independence):
  LLM-as-judge, CriticGPT, Constitutional-AI self-critique.

## Proposed register distribution (for the anneal-dev pass to weigh — not pre-decided)
1. **Supplement INV-3** (verify-isolation) with **NASA IV&V** — today it rests only on the
   AI self-preference-bias citation; IV&V adds the systems-engineering institutional warrant
   for verifier ≠ actor.
2. **Candidate INV-6** — the intent-falsification (validation) leg: a live load-bearing
   kernel rule (`core.md` §4.1.4) that passes the anchor gate (genuine external anchors:
   Boehm validation = target, Mason & Mitroff = adversarial-role, Heuer/ACH = disconfirmation
   stance, Irving et al. = AI-native form; ISO 29148 = precondition). Multi-anchor composition,
   register-well-formed (cf. INV-5's two-work composition). **Anchor-gate check the pass must
   run:** is this genuinely a *distinct* held invariant, or already covered by INV-5? (INV-5 is
   the *mechanical/runnable* falsifier; the validation leg is the *criteria-first judgment*
   attack — argued distinct, but the pass must confirm, not assume.)

## The seam the sources do NOT cover (record, don't anchor)
Two recombinations had no single authoritative home: (a) **criteria-first as an explicit
anti-anchoring lever** + full-requirements coverage as an audit bound; (b) **the route split**
— force-fix the mechanically-checkable subset, honestly-surface the judgment residual to the
operator. These are ours; they are *not* register material (no external anchor — that is the
gate working, per INV README).

## Relates to
- `intent-falsification-soundness-sweep.md` — same `core.md` §4.1.4 mechanism; that item is the
  retrospective enforcement audit, this is the foundation-anchoring of the same leg.
- `dev-notes/foundation-invariants/README.md` — membership rule (anchor-gated), the
  "Considered and excluded" precedent the ISO-29148 caution mirrors.
- Source-map verified via web search 2026-06-04 (Boehm/IV&V/29148/Mason-Mitroff/Heuer/Irving);
  raw research dumps in `dev-notes/research/` are a separate, uncurated corpus.
