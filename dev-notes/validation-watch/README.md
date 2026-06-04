# Anneal Framework — Validation Watch

Companion to the Anneal-framework spec; not part of it. The spec
states fixed decisions. Some were made best-effort, under genuine
uncertainty. This doc records those — the decision, why it was
uncertain, and the production signal that would prompt revisiting it.
The spec stays pure prescription; the uncertainty is tracked here.

Production signals come from any instance's real runs — Clippy's, or
a future sibling's.

**n=1 convention.** Closing criteria are n=1 — one observed instance
is sufficient evidence to transition. The post-run review's
self-review surfaces n=1 evidence per run. Multi-run thresholds
("3+ consecutive runs", "n≥2 distinct shapes", "5+ runs show
absence of recurrence", etc.) are cost-gating dressed as epistemic
humility (per `development-process.md` practice 8) — they defer
classifiable fixes that the lifecycle is designed to process on
first observation. RESOLUTION requires one load-bearing instance;
INVALIDATION requires one recurrence under the fixed spec; entries
are not held open waiting for repetitions.

## Entry lifecycle

Each V-N entry carries a **Status** with one of four values:

- **WATCHING** — uncertainty exists; no structural fix shipped yet.
  Production signal is being watched. If the signal observes per
  `development-process.md` practice 8 (classifiable structural
  fix), ship the fix at n=1 and transition to FIX-SHIPPED.

- **FIX-SHIPPED** — structural fix in spec, dated + commit-cited.
  Still watching, but now for **load-bearing instances** of the
  mitigation: a post-run review identifies a finding the
  mitigation actively caught that would have escaped under the
  pre-mitigation protocol. One observed instance is sufficient
  evidence the mitigation works.

- **RESOLVED** — at least one load-bearing instance observed via
  post-run review. Closing requires **positive evidence** (active
  catch counter-factually shown to require the mitigation), not
  mere absence-of-recurrence — absence is indistinguishable from
  "failure shape didn't surface this run." Once RESOLVED, the
  entry is dormant unless later recurrence reopens it as
  INVALIDATED.

- **INVALIDATED** — production signal recurred under the
  fix-shipped spec. The mitigation didn't hold. Requires new
  analysis; the entry doesn't move forward without a fresh
  structural fix proposal.

**Transitions:**
- WATCHING → FIX-SHIPPED at fix-ship commit
- FIX-SHIPPED → RESOLVED on first observed load-bearing instance
- FIX-SHIPPED → INVALIDATED on first recurrence under new spec
- RESOLVED → INVALIDATED on later recurrence

**Post-run review (Q7) reads status and responds per state.**
FIX-SHIPPED entries are walked for `mitigation load-bearing` /
`mitigation not exercised` / `mitigation evaded` classification.
RESOLVED entries are skipped. WATCHING entries follow the original
production-signal walk.

A V-N's structural design — Decision, Why uncertain, Production
signal to watch, Resolution (when FIX-SHIPPED or beyond) — remains
unchanged. Status is a single line at the top of the entry.

On RESOLVED (or a superseded INVALIDATED), the entry's file is
`git mv`d to `archive/` — no stub; the V-N number lives in the
filename, the stable key. On a later recurrence, `git mv` it back and
set INVALIDATED. The folder's active files = WATCHING/FIX-SHIPPED;
`archive/` = resolved bodies. `ls` is the index.

---

## Vocabulary

Canonical home for the validation-watch terms (relocated here out of
the methodology glossary).

- **Production signal** — a real-run observation that confirms or
  refutes a watch entry's hypothesis about an uncertain design choice.
  Production signals come from any instance's real runs.

- **Watch-entry lifecycle states** — the four states an entry carries
  on its Status line: **WATCHING** (uncertainty exists; no fix shipped
  yet) / **FIX-SHIPPED** (structural fix in spec; watching for a
  load-bearing instance) / **RESOLVED** (a load-bearing instance has
  been observed — positive evidence) / **INVALIDATED** (the signal
  recurred under the fixed spec; the mitigation didn't hold). Distinct
  from the `[INVALIDATED]` *tracker status tag* (a finding/decision
  state in an anneal-dev run) — this is a watch-entry state.

- **Load-bearing instance** — a finding the entry's mitigation actively
  caught that would have escaped under the pre-mitigation protocol; the
  positive-evidence criterion for the FIX-SHIPPED → RESOLVED
  transition. Distinct from the "Load-bearing" descriptor (the
  claims/premises a decision rests on).

