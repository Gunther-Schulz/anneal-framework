# Deferred-finding owed-artifact forcing function — a finding deferred to a to-be-authored validation-watch entry owes that entry; nothing forces it to exist

**Status:** OPEN — framework-spec gap, surfaced 2026-06-04 by **F-DC1** (the
`foundation-invariants-register` run's verify [ISSUES FOUND] loopback). Method-kernel
finding (`foundations.md` finding-state) → anneal-dev + kernel-independent verify.

## The gap
`foundations.md` finding-state #3 **`deferred`** disposition requires a *trigger
condition* (a named observable event class) — but NOT that an **owed, to-be-authored
artifact** exists. The standard practice-8 home for a genuine-uncertainty finding is a
**validation-watch V-entry**, so "finding → deferred to a V-entry I will author" is a
common disposition shape. Nothing forces that V-entry to EXIST before the finding counts
terminal or before [READY]'s "no load-bearing finding short of [VERIFIED]" gate.

**This run:** F13 (register focus-payoff unproven) was disposed "→ validation-watch entry
(to be authored at implement)". The entry was never authored — it slipped to persist and
was lost; verify's design-completeness audit caught the missing artifact (F-DC1) →
loopback → V-29 authored.

## Root-cause triage (practice 1)
Primarily a **spec gap**: the `deferred` rule was loose enough to admit "defer the
authoring and lose it" — underspecification, which fails the evidence-bearing standard
(violating it produced no artifact-absence signal until verify's *incidental* catch).
There is an adherence component (the disposition was committed "at implement" but not made
an impl unit), but per practice 1's underspecification test the loose rule makes it a spec
gap. Verify caught it as a **backstop**; the intended discipline (practice 1: backstop ≠
intended discipline) catches it at **source** (disposition-time).

## Candidate fix (classifiable — structural enforcement, earns n=1)
The deferred-to-V-entry disposition's **evidence-bearing artifact = the V-entry file
existing** (cite its path): a finding cannot be recorded `[VERIFIED — deferred to <path>]`
unless `<path>` exists. The V-entry file is the un-fakeable artifact (faking it requires
authoring it — which is the work). Equivalent [READY]/verify mechanical check: every
finding deferred to a to-be-authored artifact cites the artifact's path, checked present.
(Distinguish from `deferred` case (a)/(b), which cite an existing decision / a trigger —
this is a third sub-shape: deferred-pending-authoring, where the authored artifact is the
discharge.)

## Relates to
- `loopback-root-cause-triage.md` — the META-mechanism that would have auto-surfaced THIS
  gap at the loopback moment (F-DC1 is fresh n=3 for it; the operator again had to ask).
- `foundations.md` finding-state #3 (`deferred`) — the edit site; the validation-watch
  lifecycle (`dev-notes/validation-watch/README.md`) — the owed artifact's home.
- Origin: the `foundation-invariants-register` run (F-DC1; tracker in `.anneal-dev/runs/`).
