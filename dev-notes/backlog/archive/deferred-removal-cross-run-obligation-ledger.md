# Cross-run owed-removal has no forcing-function ("delete X at the future cutover" → forgotten)

**Status:** [DESIGN] — surfaced 2026-06-07 by a beat-the-books runs-investigation (operator-driven, the
companion to `co-producer-format-parity`). Empirical n=1 rich (the `unit_014`-cutover-never-ran →
Unit-26-divergence → already-bet re-alert production bug, fully quotable from `.clippy/runs/`) + 3
clean counter-examples isolating the failure to *cross-run* removals. **Adherence-failure-driven, but
the recurrence-reducing fix is a framework sharpening** (a missing cross-run obligation construct, not
laziness). Framework-level (a deferral-time obligation + a later-run falsifier), rendered to instances.

## The failure mode
A run SUPERSEDES code but DEFERS deleting the old version to a *future* run / cutover — "delete X at
the unit_NNN cutover", "retire the legacy after the shadow window", "Task #N follow-up to remove". That
deferral creates a **cross-run owed-removal**: an obligation one run creates that a *different, future*
run must discharge. Nothing in the framework registers it as a tracked, falsifiable artifact — it lives
only in **source comments + operator memory**. So it is forgotten; and while it stays outstanding, any
later run that *extends* the soon-to-be-deleted artifact diverges it silently.

## The index case (beat-the-books)
- **Refactor #58** created `build_signal_id` as a byte-identical SHADOW TWIN of the older
  `_build_autobet_signal_id`, and scoped the old one's deletion to a future "unit_014 cutover"
  (`services/autobet_pipeline/signal_id.py:29-30` "After unit_014 cutover the OLD helper is removed and
  this becomes the only signal_id builder"; markers also at `autobet_pipeline/__init__.py:19-22`,
  `telegram_notifier.py:1974` "Task #51 follow-up"). **unit_014 never ran** (no commit / checkpoint /
  tracker discharges it).
- **Unit 26** then extended ONLY `build_signal_id` (7→10 components). The forgotten twin stayed at 7.
  The announce-suppress compared 7-comp keys against 10-comp stored bets → never matched → already-bet
  opportunities re-alerted every cycle (blast radius = all autobet signals since Unit 26).
- Discharged only *partially* on 2026-06-07 (`b45cd02a`, which re-deferred the actual twin deletion as
  `D6`), and the owed-removal was finally re-tracked as **Unit 30** in the roadmap — *reactively, after
  it caused a production bug.*

## Why the framework doesn't catch it (the gap)
The owed-removal falls in the gap between two adjacent mechanisms:
1. **Dead-code detection is a verify-time, IN-RUN lens.** It fires on what is present in *this run's*
   diff. When removal is the run's own charter, or the dead code is created within the run, it is
   caught — see the counter-examples below.
2. **`deferred-finding-owed-artifact-forcing-function`** (archived — shipped at `spec/core.md §5.1`
   sub-case (c)) forces an owed *artifact's path to exist*, but **intra-run** — a finding deferred to a
   to-be-authored artifact, re-checked by the *same run's* verify.

The owed-removal is neither: it is a **cross-run obligation** ("a future run must delete X"). Nothing
(a) registers it as a tracked falsifiable artifact at deferral-time, nor (b) re-surfaces / fails when a
later run extends the still-undeleted artifact. It relies entirely on operator memory + code comments.
**The shadow-twin shape compounds it:** two parity-by-discipline artifacts where *deletion is the only
structural guarantee of parity* — so while deletion stays deferred, parity is "willed, not structural,"
and any extension of one twin silently breaks the equality (the exact Unit-26 → bug path).

Distinction to preserve: **dead-code detection** (verify-time, in-run, fires on the present diff) ≠
**deferred-removal tracking** (a cross-run obligation that fires at deferral-time and must persist +
re-surface in later runs). The framework has the former; this failure needs the latter.

## Counter-examples — removal-as-run-charter ALWAYS completes (isolates the failure to *cross-run*)
- **Unit 8 — OLD-arb retirement** (`.clippy/runs/2026-05-27-unit-8-arb-strategy.md`): the deletion was
  the run's own deliverable, enumerated by an exhaustive sink-grep, re-run as a convergence falsifier
  each cycle; U4/U5 deleted the files + dropped the tables. Same-run, no memory dependency.
- **Unit 28 — inert risk knobs** (`2026-06-06-units-26-27-28-...md`, D13): flagged write-only, REMOVED
  in the same run; D13 explicitly *rejected* deferral ("present-but-inert is worse than absent").
- **Unit 18 — `runner_enabled`** removed in-run across 22 references.
- **Snapshot run** (`2026-06-04-remove-snapshot-azuro-enrichment.md`, F7→D7): verify caught an abandoned
  `_BothUoWPatches` test helper and the loopback deleted it *in-run*.

The corpus is generally disciplined about *surfacing* deferred feature/fix findings to the operator
(Unit 5 D8/D10, Unit 7 F33/F34, Unit 19 D4 — all discharged or surfaced). The failure is specific to
**cross-run owed-removals**, which have no equivalent forcing-function.

## The sharpening (candidate)
Mirror how `deferred-finding-owed-artifact-forcing-function` made an owed artifact's *path* the
un-fakeable artifact — but for a cross-run removal:
- **At deferral-time**, an owed-removal must cite a **tracked discharge target** (a roadmap unit /
  backlog slug — Unit 30 is the manual, reactive version of exactly this) rather than a bare
  source-comment "delete later".
- **Register the to-be-deleted symbol as a parity/removal-debt invariant** (composes with
  `instance-domain-invariant-register`) so that any *later run touching or extending that symbol* trips
  a falsifier — "the symbol owed-for-deletion still exists AND was just extended" → falsified — instead
  of silently diverging. This converts a memory-dependent obligation into a structural one.

## Relates to
- `deferred-finding-owed-artifact-forcing-function` (**archived — shipped**): the **mechanism
  precedent** — owed-artifact forcing-function — but **intra-run**. This item is its **cross-run
  counterpart**; the owed thing is a *removal a future run must do*, not an artifact this run's verify
  re-checks. Do not fold (conflates single-run finding-discipline with a cross-run obligation ledger).
- `co-producer-format-parity` (OPEN, the run that spawned this): the **deferred-removal half of the
  shared Refactor-58 root**. That item's payload is *enumeration-blindness* (a co-producer is unreachable
  by a symbol-grep — the Unit-26 "opaque key" slip); this item is the **orthogonal half** — even when
  the twin is *known and documented*, nothing forces its deletion. Cross-link, keep separate.
- `instance-domain-invariant-register` (OPEN): the nearest cross-run construct, but it *locks corpus
  primitives as verify anchor-sources*, not *owed-removal obligations with a discharge gate*. A "known
  duplicated producer = debt-until-deleted" could be one **registered invariant** → this item is a
  candidate **consumer** of the register, not the same thing.
- The in-flight `enumeration-target-blindness` anneal-dev formalization (operator's active run as of
  2026-06-07) is the *enumeration* meta-class home (co-producer + replacement-side-effect); this item is
  the distinct *deferred-removal forcing-function* axis — orthogonal, not a fold.
- Origin: beat-the-books runs-investigation 2026-06-07 (operator-driven, companion to the signal_id
  re-alert root-cause).
