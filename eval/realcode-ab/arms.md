# Arm prompts — real-codebase A/B (VERBATIM; wording is load-bearing)

**Do NOT paraphrase.** This session's headline lesson: prompt wording flipped results
(effort framing, blind-vs-non-blind, the disciplines block). Reproduce/extend by copying these
exactly. `{DIR}` = a `/tmp/bt-eval/copy_N` from `build-tree.sh`.

## Shared task — NON-BLIND (steers attention; produced the inflated early "ladder")
> You are doing a pre-ship CORRECTNESS REVIEW … the **replay engine** under
> `src/beat_the_books/services/analysis/replay/` … Review its **pick-settlement pipeline
> END-TO-END** for correctness — every step: 1. how it fetches/selects each game's score, 2. how
> it matches a score to a given pick, 3. how it derives won/lost/void, 4. how it computes PnL.
> Report every correctness bug (`file:line` — what — why). **Think about whether each *kind* of
> pick gets matched to the *right* score and settled correctly.**

## Shared task — BLIND (no step-list, no hint; the fair version)
> You are doing a correctness review of one component … at `{DIR}`. The code under
> `src/beat_the_books/services/analysis/replay/` is a **replay engine**: it re-scores historical
> betting "picks" against game results to evaluate strategy variants. Review this code for
> **correctness** and report any bugs you find — for each: `file:line`, what's wrong, and why it
> matters.

Both end with: scope = work ONLY within `{DIR}`, no git/docs/tracker, don't modify; final message =
findings list.

## Method blocks (the manipulated variable)
- **act-first (non-blind):** *"review the way an experienced senior engineer would under normal time
  pressure … keep it efficient."* ← carries an EFFORT confound vs the discipline arms; do not reuse
  for a clean test.
- **act-first-blind:** NO method block, NO effort sentence. (Clean baseline.)
- **vanilla (generic disciplines):**
  > Method — apply these review disciplines, by hand. Do NOT invoke any skill.
  > 1. Ground every claim in the actual code — cite file:line; never assume.
  > 2. Investigate thoroughly before judging.
  > 3. Verify each code path/branch against what the requirement demands — not just the happy path.
  > 4. Actively try to falsify "this is correct" — look for an input where it produces a wrong result.
- **adhoc (= vanilla + the two FOCUSED directives):** vanilla's 1–4 **plus**
  > 2'. Trace the full data flow end-to-end — for each value, where it is *produced*, what carries it,
  >     every place it is consumed.   ← the provenance directive (lifts market_id/closing_lines)
  > 3'. For each field the input data carries, follow it to its consumers — notice a field carried
  >     but *not used* where you'd expect.   ← the completeness directive
- **Effort framing:** the earlier runs put "Be thorough; cost is not a concern" on vanilla/adhoc but
  NOT act-first → CONFOUND. For any clean run, **either omit effort framing from all, or apply it to
  all identically.** The blind runs omitted it from both (correct).

## What's been run (✓) vs not (✗) — see `../../dev-notes/backlog/anneal-empirical-validation-experiment.md`
- NON-BLIND ×5 each: act-first ✓, vanilla ✓, adhoc ✓  (the "ladder" — confounded by effort + non-blind)
- BLIND ×5 each: act-first ✓, vanilla ✓  (gap collapsed to a tie)
- BLIND adhoc ✗ (the provenance directive untested blind — re-test before trusting the 2/5→5/5 result)

## THE PENDING TEST — prompt-constant, PROCESS-varied (the framework's actual test)
Hold the prompt **identical** for both arms (give BOTH the disciplines block — or neither; just match);
vary **only the process**. Blind task, no effort framing, k≥5.
- **Arm A — single pass:** one review subagent, stop.
- **Arm B — real anneal cycle (orchestrated across dispatches):**
  1. Investigate/draft-findings subagent (same prompt as A).
  2. **Separate, fresh-context** verify/falsify subagent that is given Arm-A/draft's *findings + the code*
     and told to independently attack them + find what was missed — it must NOT see the first agent's
     reasoning (independence is the lever; a single agent can't self-run this — same-context self-verify
     under-detects, the framework's own finding).
  3. Loop until convergence (no new findings).
- Pre-commit as TERMINAL: if Arm B ties/misses vs Arm A, that is the answer (no "one more level").

## PREFERRED REAL arms (operator-flagged, session-11 close) — better than the synthetic construction above
Use the operator's **actual artifacts** instead of constructing Arm B. The clippy repo has a **legacy
monolithic clippy** (pre-anneal: NO adversarial falsification / convergence / lens-set) that the operator
found **≫ act-first in daily use**. So run the **factorial**, blind + identical task + k≥5:
- **act-first** (blind, no method block).
- **legacy-monolithic-clippy** (locate in the clippy repo; pin whether it's one elaborate *prompt* or a
  structured *multi-step* process) — isolates the value of **basic structured process**.
- **modern-anneal-clippy** (current skill, with falsification/convergence/lenses) — the step from
  monolithic → modern isolates the value of **the anneal additions** (the gold-plating question).
Operator's lived prior (CORRECTED — not gold-plating): **both jumps are real** — act-first < monolithic <
modern; the anneal additions *further improved* results in daily use. So the open question isn't "are the
additions worth it" (operator: yes) but **whether a controlled one-shot test can even capture this** — our
one-shot reviews came up null, which likely indicts the regime/instrument (one-shot ≠ sustained real use),
not the framework. See experiment-doc Addendum 3.

## Distributed-lens arm (crowding mitigation — gated; operator idea 2026-06-07)
Variant for the crowding test (`../../dev-notes/backlog/lens-crowding-vs-broad-search.md`): instead of
stacking the focused directives into one agent (current adhoc), **distribute across agents** — a
**broad-main agent with NO lenses** (preserves the omission sweep) + **one fresh-context lens-agent per
focus** (e.g. a provenance-agent), **findings merged**. Tests whether distribution recovers the broad
coverage stacking loses while keeping the focused depth (and gives the fresh-context independence for
free). Build/run only if the crowding ablation confirms crowding is real — else cost for no gain.
