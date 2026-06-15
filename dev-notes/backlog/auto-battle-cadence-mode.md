# Interactive "auto-cycle to [READY]" menu affordance (auto-advance cycles, halt at the phase gate)

**Status:** [PARKED] — framework mode-mechanics idea, operator-raised 2026-06-04, **direction resolved
2026-06-04** (see Resolution). **Not for now** (filed per no-silent-deferral). Framework-spec
(`foundations.md`/`core.md` Modes + `SKILL.md` Modes + the closed-artifact menu) → anneal-dev +
kernel-independent verify when pursued. (Filename `auto-battle-cadence-mode` is legacy — the resolved
shape is an *interactive* affordance, NOT an auto-battle variant; renamed in-title, file slug kept as
the stable referent.)

## Resolution (operator, 2026-06-04) — candidate (b), NOT a 3rd mode
Keep **two named modes** exactly as they are — interactive and **auto-battle stays fully autonomous**
(reject candidate (c): do not add an auto-battle toggle). Interactive gains **one more menu entry**: a
"do all `(a)` cycles autonomously until `(n)` (the phase gate) is reached" affordance — the operator
selects it once and the cycle loop self-advances (taking the AI's recommended `another cycle` each
cycle) until the AI's recommendation becomes `next phase` at `[READY]`, where it **halts and presents
the closed artifact** for the operator's `(n)`/override. Supersedes the earlier "(a) one stop-at axis
that collapses the 3 apparent modes" lean: the operator wants the two modes to stay distinct, with the
cadence as an interactive *affordance*, not a re-parameterization of what interactive/auto-battle are.
(Implementation MAY still use an internal stop-at flag — that is a realization detail for the cycle,
not a surfaced 3rd mode.)

**Two properties to preserve in the design (why the affordance beats an auto-battle variant):**
- **`[CONDITIONAL]` resolution stays with the operator.** Because the loop halts at `[READY]` with the
  operator present, open `[CONDITIONAL]`s surface at the closed artifact for operator resolution — they
  do NOT silently `[AUTO-ACCEPTED]` as they would in auto-battle. The operator sheds per-cycle `(a)`
  clicks, never the load-bearing `[READY]` decision.
- **Method-kernel touchpoints still fire.** The affordance auto-takes `another cycle`; it does NOT
  auto-pass the kernel-independent-review / commit-approval gates. Surfacing at phase transitions +
  method-kernel touchpoints is unchanged.

**Dogfood datapoint:** the `verify-vs-original-requirements` run (2026-06-04) ran this exact cadence
**ad-hoc** via a session-cadence instruction ("interactive: auto-advance cycles; surface at phase
transitions + method-kernel touchpoints"). It worked — evidence the affordance is wanted and the
semantics above hold in practice. Formalizing it as a menu entry removes the need for the ad-hoc note.

**Dogfood datapoint 2 (2026-06-05, `move1-s3.1-honest-relabel`):** operator invoked it verbatim —
"auto-cycle please until (n)". The loop self-advanced cycles 2→5 (incl. the convergence cycle's
fresh-context falsification dispatches) and **halted at [READY]** with the closed artifact for the
operator's `(n)`. It also exercised the **menu-persistence + free-form interjection** property: the
operator interjected a question mid-auto-cycle ("what is F3 about?"); the question was answered and the
auto-cycle continued — exactly the SKILL.md interjection-handling. Both preserved-properties held: the
open `[CONDITIONAL]`s (D3/D4/D5) surfaced at `[READY]` for operator resolution (not silent
`[AUTO-ACCEPTED]`), and the method-kernel soundness touchpoint fired at the gate (it did NOT auto-pass
into implement). Strongest validation yet that the (b) affordance design is right.

**Capture decision (2026-06-05, operator ask "capture appropriate levels for all campaigns").** Rather than
build (b) now, the per-campaign **hands-off level is persisted as an annotation in the backlog README's
▶ Campaign map** ("Cadence per campaign": gated-kernel / fork-first / drain / deliberate). This is the **cheap
realization** of the (b) affordance — it records *where each campaign halts* so the operator need not re-state
"auto-cycle until (n)" each run — and lets (b) stay ⑦-**deferred** (no kernel cycle spent yet). Promotion to a
built menu entry remains the open option if per-campaign re-statement ever becomes felt friction.

**Datapoint 3 (2026-06-05, `campaign3-enforcement-fidelity`).** The cadence held across a full run: auto-cycled
investigate→falsify(intent cycle-2, intent+mechanical cycle-3)→[READY]→implement→verify, **halting only at [READY]
and step-4** as designed. It survived **two mid-cycle free-form interjections** (the "non-behavior-preserving?"
question, the "V-entries get lost" clarification — both answered, then the run continued) AND a **verify [ISSUES
FOUND] loopback** (the V-F1 connector fix + delta-verify) **without losing the gate structure**. **Map-annotation
result (the capture-decision's open question):** partial — the operator said "lets start" / "n" without
re-stating "auto-cycle until (n)" verbatim, so the map-annotated cadence *did* carry (reduced the re-statement);
but the operator still **named** the cadence at session top ("auto-battle for ③… halt at [READY] and step-4"),
so the map didn't fully eliminate the statement. Net: the affordance is robust and the map-annotation reduces
(not eliminates) re-statement — consistent with keeping (b) ⑦-deferred. No promotion warranted yet.

## The idea
Today there are **two modes** (`core.md`/`foundations.md` Modes): **interactive** (operator selects
`(a)nother-cycle` / `(n)ext-phase` at *every* cycle's closed artifact) and **auto-battle** (loop
self-advances all the way to [READY] with no operator). The operator wants a **middle cadence**:
auto-advance the *cycle loop* (no per-cycle `(a)/(n)` menu) but **stop at the phase-transition `(n)`** —
i.e. the operator is asked only at `[READY]` (and other genuine phase gates), not every cycle.

## The tension (the real design problem — don't just bolt on a 3rd mode)
A third *named* mode = **3 modes** (interactive + two auto-battle variants), which the operator judges
**too many**. The design work is a **unifying** solution, not a third mode. Candidates to weigh:
- **(a) one "auto-advance" axis with a `stop-at` parameter** (`per-cycle` / `per-phase` / `never`) —
  a single mode, parameterized; interactive = `stop-at: per-cycle`, full auto-battle = `stop-at: never`,
  the requested cadence = `stop-at: per-phase`.
- **(b) interactive gains a "run-until-(n)" affordance** at the menu (operator says "advance until
  ready"; cycles self-run meanwhile).
- **(c) auto-battle gains a `stop-at-[READY]` toggle.**
(Earlier lean was (a) — collapses 3 apparent modes into one parameterized axis. **Superseded: the
operator resolved toward (b)** — see Resolution above. (a)'s mechanism may survive as an internal flag,
but not as a surfaced re-parameterization of the modes.)

## Parked sub-idea
**Full auto-battle as the default** (vs interactive-by-default today). Operator-flagged, explicitly
*"not to discuss now"* — parked here so it's not lost. Couples to the unifying solution above (if mode
becomes a `stop-at` parameter, "default" = the default parameter value).

## Relates to
- `core.md`/`foundations.md` Modes + `SKILL.md` Modes (the two-mode definition this revises) — method-kernel.
- Mode-mechanics were a flagged coherence-audit deep-sweep target (`clippy-run-findings-dispatch-coupling` tail).
