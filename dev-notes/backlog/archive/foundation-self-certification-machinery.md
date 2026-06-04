# Foundation self-certification machinery — externalize the soundness half of the kernel-edit verify

**Status:** CLOSED — SHIPPED 2026-06-04 via the `foundation-invariants-register` anneal-dev run (verify
[PASSED]; release pending operator approval). Built candidate (1): the foundation-invariants register
(anchor-gated; 5 externally-anchored invariants) + the per-touched-invariant focusing artifact wired into
the method-kernel-edit verify (`development-process.md` §2 / step-4 / `CLAUDE.md`) + the
Invariant-change-ratified protection (`hooks/commit-msg`). Candidates (2)/(3) rehomed:
`canonical-scenario-regression-suite` + the reframed `multivoter-verify-no-predicate-claims` (single
intent-falsification; kernel-integration design captured). Spawned follow-ups:
`intent-falsification-soundness-sweep`, `deferred-finding-owed-artifact-forcing-function`. Watch:
`validation-watch/V-29-register-focus-payoff`. Archived.

## The problem
anneal-dev **can't self-certify its own foundation** (Gödelian bootstrap: checks built *from* the kernel
inherit the kernel's blind spots; a foundation can't be fully validated by checks resting on it). That is
why the repo discipline mandates a review **grounded outside the anneal kernel** for method-kernel edits:
- **skill-craft (form)** — a separate corpus; checks skill-quality/form. **Already wired in** (used in the
  `verify-vs-original-requirements` verify: "skill-craft FORM review — clean"). This axis is mechanized.
- **the operator (soundness)** — methodology-correctness; skill-craft explicitly does NOT cover this.

**Open axis:** soundness. Today only the operator covers it. Question (operator): can machinery do more of
that half?

## The hard limit (state it up front — don't sell past it)
Machinery helps **only to the degree it is grounded outside the kernel**. It can **shrink + sharpen** the
operator's residual; it **cannot remove** it. A machine that "passes" novel soundness would BE the
rubber-stamping the verify-techniques research warned against. The operator stays structurally required.

## Candidate machinery (each grounded externally; compose, don't pick blindly)
1. **Foundation-invariants register (the operator's "md").** Load-bearing kernel invariants (every claim
   carries a basis; no operator-detection dependence; verify isolation; grounded-claims + coherent-complete
   picture; …) each paired with its **external anchor**. **Crux that makes it non-circular: its value is
   ENTIRELY the anchors.** A register that re-lists anneal's own rules checks anneal against a copy of
   itself = bloat. The anchors already exist — the **process-literature research** (`dev-notes/research/`)
   found them: basis-rule ≈ Zave-Jackson *designation*; complete-state ≈ S,K⊢R; loopback ≈ Platt *recycle*;
   the two verify channels ≈ APF *Callback/Confirm*. A kernel edit re-checks any touched principle against
   its named anchor (evidence-bearing per the basis rule: a per-invariant holds/violates artifact).
2. **Canonical-scenario regression suite (the stronger complement).** A frozen set of corpus-evolution
   scenarios with operator-ratified expected outcomes — "executable verification" *for the method itself*.
   Catches soundness flaws that violate **no stated invariant** but DO break a known-correct outcome — which
   a static invariants list misses. Lightweight cousin of `anneal-empirical-validation-experiment`.
3. **Different-model soundness checker.** The *checker* that runs against (1)/(2) (verify-techniques:
   model-diversity > vote-count). Needs (1)/(2) as stable ground — without a written register it re-derives
   anchors each run, which the basis rule rejects as recall. Complements, doesn't replace, (1)/(2).

## Structural catches to design around
- **Protection.** Changing an invariant must be **operator-gated high-ceremony** (NOT an ordinary
  anneal-dev run) — else a run edits the invariant to permit its own flaw and the circularity returns.
- **Anti-false-comfort.** The artifact must carry, in itself, the honest residual ("known-invariant
  violations only; novel soundness still needs the operator") so "register-clean" is never read as "sound."
- **Anti-bloat.** Earns its place only via the external anchors; a spec restatement is circular and useless.

## What it buys
The operator's soundness pass becomes **focused** (which invariants this edit touches, which anchors it must
still satisfy) instead of open-ended "is this sound?". Known-invariant breaks become mechanical findings;
the irreducible residual (novel soundness) is shrunk and made legible — not closed.

## ▶ NEXT-UP (session-5 handoff, 2026-06-04) — start here next session
**Operator picked this as the next item.** It's corpus-evolution (touches `development-process.md`'s
kernel-edit verify discipline + a new dev-notes invariants register) → runs through anneal-dev + the
kernel-independent review. The run-gate hook (`hooks/anneal-dev-run-gate.py`) now *enforces* that — the
edits to `development-process.md` will require an active run, so the two compose.

**The design has real open forks — settle them WITH the operator first (decide-ahead), THEN run anneal-dev.**
The forks: (a) which machinery — the invariants register alone, or + the canonical-scenario suite, or +
the different-model checker; (b) how the invariants are anchored externally (the anchors already exist in
`dev-notes/research/` — process-literature run); (c) the protection mechanism (operator-gated invariant
changes).

**Framing crystallized this session (so it survives `/clear`):**
- The need exists ONLY for **foundation edits** — files anneal-dev *depends on* (`spec/*`, `foundation.md`,
  `anneal-dev/spec/*`). Editing files it does NOT depend on (clippy/daneel/ad-hoc) self-certifies cleanly
  (verify is a real independent check — doctor examining a patient). Foundation edits = doctor examining
  *themselves*: fine for the mechanics, but can't be their own second opinion on soundness.
- **Empirical grounding:** session 5 shipped **3 foundation edits via anneal-dev**, each closed by the
  operator's soundness "ship it." That operator step is *exactly* what this machinery would lighten —
  catch the known-invariant breaks mechanically so the soundness pass is small + sharp.
- **The hard limit (restate every time):** it's "dogfood **+** an outside check," never "dogfood alone."
  The machinery shrinks the operator's role; the operator is irreducible (Gödel). Removing them = the
  rubber-stamping the framework exists to prevent.

## Relates to
- skill-craft (the form half — already the external form ground; this is its soundness sibling).
- The verify-side cluster: `multivoter-verify-no-predicate-claims` (different-model verifier; decompose
  judgment claims) + criteria-first / exclusion-obligation / falsifiability-gate sharpenings.
- The research runs: `dev-notes/research/` process-literature anchors (the raw material for the register).
- `anneal-empirical-validation-experiment` + `anneal-reliability-measurement` (the canonical-scenario suite
  is a lightweight relative).
- The repo discipline that states the rule today: `CLAUDE.md` "Development process grounding"
  (method-kernel verify = skill-craft form + operator soundness; "anneal-dev never self-certifies its own
  foundation").
