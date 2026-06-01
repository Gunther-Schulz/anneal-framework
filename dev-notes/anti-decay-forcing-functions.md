# Anti-decay forcing functions (skill-craft + dev-process) — effort design capture

Durable design artifact for a **foundational, reflexive** framework
effort: stop the corpus from structurally decaying as it's worked on.
Written in-context 2026-06-01 so a fresh session resumes cold.
**Recommended to start fresh** — foundational + maximally
self-validation-prone, not tail-of-a-long-session work. Not spec.

## The problem: three modes of corpus structural decay

Working on the framework keeps producing the same mess:
- **Bloat** — files accrete walls of text (e.g. clippy `SKILL.md`).
- **Fragmentation** — one principle restated across N homes instead of
  stated once (e.g. FB-5 the `[VERIFIED]`-family; the slot-collapse).
- **Leakage** — domain concretions baked into domain-general homes
  (e.g. the contract-1 de-pollution cluster).

## Why it decays despite existing mechanisms

The disciplines exist but fire in a gap:
- **Per-edit** ones are **local-blind** — practice 6 itself says "the
  local check always passes while the whole degrades." Edit-as-Pareto
  checks the edit, not the document's drift.
- **Set-level** (coherence-audit) is **periodic** — drift accrues
  between runs (the first audit ever was 8 cycles overdue).
- So: **no cheap per-cycle set-level hygiene.** Decay accrues in the gap
  until a periodic audit or the operator notices.

**The root irony:** the framework preaches forcing-functions over naked
judgment (practice 8), yet its OWN anti-decay disciplines are advisory —
Amendment says *scan* all homes (no artifact), Edit-as-Pareto says *name*
what was removed (discretionary), domain-independence is a *checklist*.
Judgment-shaped, so they don't fire every time. The anti-decay rules
violate the framework's own core principle.

## The fix — two levels (the three-levels architecture)

skill-craft **defines** the anti-decay disciplines (general skill-design);
dev-process **enforces** them per-cycle (triad release loop). dev-process
can't force what skill-craft only advises → fix BOTH, source-first
(practice 1).

### skill-craft (the source — higher leverage, higher blast-radius)
Sharpen the disciplines from "do the check" → "produce the artifact"
(forcing-function shape, per skill-craft's own practice 8):
- **Amendment reduce/merge** → the all-homes scan becomes a *required
  artifact* (the grep across homes), not AI discretion.
- **Edit-as-Pareto** → "name what was removed/consolidated" becomes a
  required line, not advisory.
- **Domain-independence / Abstraction check** → produces an artifact
  (domain-term grep on the home), not a mental checklist.
- **Procedure-drift / word-count** → a budget *gate*, not advice.
Propagates to every skill-craft user (clippy / daneel / campaign-craft /
plugin-dev) — the high-leverage half, and the highest-care (canonical,
wide blast-radius).

### dev-process (the wiring)
Add a **per-cycle structural-hygiene check** to release-loop step-4 that
*consumes* those artifacts — three cheap, diff-computed checks:
- **Bloat** — file size/structure delta (grew past budget? prose where a
  list/reference belongs?). Mechanical.
- **Leakage** — domain-term grep on domain-general homes (the
  de-pollution grep, every cycle). Mechanical.
- **Fragmentation** — the forced all-homes scan artifact (from the
  sharpened Amendment discipline). Partly judgment, but the scan is
  forceable.
Composes with the periodic coherence-audit: per-cycle hygiene catches
*new* decay at the source; the periodic audit catches accumulated
residue. Smaller levers: tighten the audit cadence (lower N /
churn-triggered); give major files a declared structure budget step-4
checks against.

## Hard caveat — keep it CHEAP
The per-cycle check must stay cheap (it runs every cycle) or it becomes
the very ceremony/bloat it's fighting — three diff-computed checks, not a
mini-audit per cycle. Calibrating "minimal forcing function that catches
the 3 modes without taxing every cycle" IS the design work, and the thing
most likely to go wrong (over-forcing).

## Reflexivity caveat — non-negotiable separate-context review
This is skill-craft improving skill-craft + dev-process improving
dev-process — maximal reflexivity, the most self-validation-prone moment
(`CLAUDE.md`: "rule-edit subagent PASS may self-validate — pause + re-read
before push"). Separate-context review here is the whole ballgame, not a
formality.

## Sequencing
1. **skill-craft** — sharpen the disciplines to artifact-producing (source).
2. **dev-process** — wire the per-cycle step-4 hygiene check (enforcement).
3. **Thorough coherence-audit** — full-systematic pass with the now-forced
   lenses; surfaces the *current* decay corpus-wide.
4. **Refactors fall out** as the audit's work-list:
   - clippy `SKILL.md` de-bloat (move detail to `references/`, re-derive
     structure from the vision).
   - FB-5 verified-integrity consolidation.
   - (the de-pollution cluster is adjacent — same restructure altitude;
     could be folded or sequenced right after.)

## Why start fresh
Foundational (it governs how *all* future framework work goes) + maximally
reflexive (self-validation risk) + multi-corpus. Exactly the wrong thing
to rush at the tail of a long session. This doc is the durable handoff.
