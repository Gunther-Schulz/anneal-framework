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
are not held open waiting for repetitions. What *licenses* n=1 is
the opportunity-requirement on closing (Entry lifecycle below): one
genuine opportunity handled is dispositive, so repetition adds
nothing.

## Entry lifecycle

Every entry is one of two **watch kinds**, set by what its fix is:

- a **correctness-watch** — the fix is a **catcher** (a check, lens,
  or phase that catches the failure when it would otherwise ship);
- a **quality-watch** — the fix is a **form-change** with no catcher;
  it changes *what gets produced* (e.g. V-13's citation+fact basis
  form replacing verbatim code-quote).

The kind drives how the entry closes (the closing rule below): a
correctness-watch closes on a *caught* instance, a quality-watch on a
*produced-clean* one.

Each V-N entry carries a **Status** with one of four values:

- **WATCHING** — uncertainty exists; no structural fix shipped yet.
  Production signal is being watched. If the signal observes per
  `development-process.md` practice 8 (classifiable structural
  fix), ship the fix at n=1 and transition to FIX-SHIPPED.

- **FIX-SHIPPED** — structural fix in spec, dated + commit-cited.
  Still watching, but now for a **load-bearing instance** of the
  fix: a run where the failure's opportunity genuinely arose and the
  fix handled it (the closing rule below). The entry **names how its
  failure would be exhibited** — its **catcher** (correctness-watch:
  the check/lens/phase that catches it) or its **opportunity-test**
  (quality-watch: what a run looks like where the *old* form would
  have produced the bad artifact). One observed instance is
  sufficient evidence the fix works. (A fix that is
  **correct-by-construction** — the failure literally can't be
  expressed under the new spec — is *not a watch entry at all*: there
  is no residual uncertainty to watch.)

- **RESOLVED** — at least one **opportunity-exercised** instance
  observed via post-run review. Closing requires a run where the
  failure's **opportunity genuinely arose AND the fix handled it** —
  **caught** (a correctness-watch's catcher fired on a
  would-have-shipped failure, counterfactual shown) or
  **produced-clean** (a quality-watch's form-change held where the
  *old* form would have produced the bad artifact, counterfactual
  shown). **Pure non-occurrence never closes**: "no such opportunity
  arose this run" is *no evidence yet*, not RESOLVED — absence is
  indistinguishable from "the failure shape didn't surface this run."
  Once RESOLVED, the entry is dormant unless later recurrence reopens
  it as INVALIDATED.

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
FIX-SHIPPED entries are walked against this closing rule —
opportunity-handled (`caught` / `produced-clean`, per kind),
`opportunity not exercised`, or `fix evaded`. RESOLVED entries are
skipped. WATCHING entries follow the original production-signal walk.
The README carries the closing rule; Q7 carries the walk procedure.

A V-N's structural design — Decision, Why uncertain, Production
signal to watch, Resolution (when FIX-SHIPPED or beyond) — remains
unchanged. Status is a single line at the top of the entry.

On RESOLVED (or a superseded INVALIDATED), the entry's file is
`git mv`d to `archive/` — no stub; the V-N number lives in the
filename, the stable key. On a later recurrence, `git mv` it back and
set INVALIDATED. The folder's active files = WATCHING/FIX-SHIPPED;
`archive/` = resolved bodies. `ls` is the index.

**Archive-check before a new entry.** `archive/` is the **registry of
known-and-fixed failure modes**. Before filing a **new** `V-` for a
seemingly-new issue, **scan `archive/`** for a matching — or
**adjacent** (same root, different manifestation) — RESOLVED entry. If
found, the issue is a **recurrence/regression**, not a new entry:
`git mv` that entry back to the active folder and set **INVALIDATED**
(this is the trigger for the RESOLVED → INVALIDATED transition above).
Only a genuinely-novel issue — clean archive scan — gets a new `V-`.
The check catches a re-introduction from **any** source: the original
fix quietly weakening, *or* an unrelated later change regressing a
long-resolved issue — a methodology-level regression net. With the
n=1 fast-close, the archive-check is the **safety hatch** that bounds
the cost of closing too eagerly: a wrong close reopens the moment its
failure mode reappears.

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

- **Load-bearing instance** — a run where the failure's opportunity
  genuinely arose and the fix handled it (caught or produced-clean);
  the opportunity-exercised criterion for the FIX-SHIPPED → RESOLVED
  transition. Distinct from the "Load-bearing" descriptor (the
  claims/premises a decision rests on).

- **Correctness-watch** — an entry whose fix is a **catcher**; it
  closes on a *caught* instance.

- **Quality-watch** — an entry whose fix is a **form-change** (no
  catcher) that alters what gets produced; it closes on a
  *produced-clean* instance.

- **Catcher** — the specific check, lens, or phase that catches *this
  entry's* failure when it would otherwise ship; the correctness-watch
  closing mechanism. Distinct from `post-run-review.md`'s generic
  phrase "the framework's primary catcher" (post-run-review / verify
  broadly) — a watch entry's catcher is one named instance, not that
  whole-framework descriptor.

- **Opportunity-test** — for a quality-watch, the description of what a
  run looks like where the *old* form would have produced the bad
  artifact; closing requires such an opportunity, with the new form
  producing clean where the old would not have.

