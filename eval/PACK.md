# Pre-registered task pack — silent-failure regime (Step 1)

**Frozen by rubric, NOT by performance.** Each task below is argued in-regime
from the 5-point rubric in `dev-notes/backlog/measurement-harness-mve.md`, and
the pack is committed *before* any scored arm run. We do **not** filter tasks by
running an arm and keeping its misses — that is the experiment doc's
selection-bias threat. A rubric-conformant task that an arm happens to catch is a
legitimate *measured* result (toward refutation), not a harness artifact.

Freeze status: **FROZEN** at the commit that adds this file. Changing the pack
(adding/removing/editing a task or oracle) after a scored run invalidates that
run — re-freeze and re-run.

## The regime
Silent-failure tasks: the seeded defect **passes the quick check the prompt
advertises** but is wrong on a held-out requirement stated in the prompt prose.
This is the regime anneal claims (expensive/late verification, where the cheap
oracle gives misleading signal) and the one act-first owns its reputation in is
explicitly *out* (cheap-oracle tasks).

## The rubric (every task satisfies all 5)
1. **Fair** — the full requirement is in the prompt prose; the info to catch the
   defect is available to *both* arms (no hidden-intent gotcha).
2. **Weak-oracle-green** — the seeded defect passes the advertised quick check.
3. **Held-out-detectable** — a deterministic script (no LLM, no arm-awareness)
   catches it; a correct fix scores 1.0.
4. **Requirement-space-gated** — catching it requires enumerating a *separately
   stated requirement clause* the quick check never exercises, not
   domain-trivia or one extra random test. (The criterion `discount-floor`
   failed → excluded below.)
5. **Plausible** — the defect looks like a natural first implementation.

## Well-formedness gate (mechanical, run before freeze)
`python eval/wellformedness.py` — for every task: (a) weak check green on the
defect, (b) held-out oracle < 1.0 on the defect, (c) reference correct fix
(`oracle/fixtures/<task>_fixed.py`, gate-only) passes the weak check and scores
1.0. **All 10 PASS** (last run 2026-06-06; defect pass-rates recorded below).

## Pre-registered metrics (P1–P3)
- **P1 — outcome:** held-out seeded-defect catch-rate (the oracle's `pass_rate`
  reaching 1.0 = the defect was caught **and** no requirement regressed).
- **P2 — cost:** tokens-to-correct-outcome (`timing.json` per run; mean ± σ; the
  lead result).
- **P3 — grounding ratio:** evidence-gathering tool-calls (read/search/verify) vs
  total, from `metrics.json` — refine, not ruminate.

Predictions + refutation conditions live in
`dev-notes/backlog/anneal-empirical-validation-experiment.md` and are pre-registered
by reference (not restated here, to keep one source of truth).

## The pack (10 tasks)

| task | fn | seeded defect | orthogonal requirement (the gated clause) | defect class | defect pass-rate |
|---|---|---|---|---|---|
| merge-config | `merged_config` | `base.update(override); return base` | purity — don't mutate the shared-default `base` | input mutation / aliasing | 0.50 |
| dedup-order | `dedupe` | `return list(set(items))` | preserve first-occurrence order | lost ordering invariant | 0.33 |
| sort-tiebreak | `rank` | sort by `-score` only | ties break by name ascending (deterministic) | missing secondary sort key | 0.33 |
| csv-escape | `to_csv_row` | `",".join(fields)` | quote fields containing commas (RFC 4180 round-trip) | delimiter escaping | 0.33 |
| migrate-idempotent | `ensure_prefix` | `return "/api/" + path` | idempotent on re-apply (no double prefix) | non-idempotency | 0.33 |
| word-count-ci | `most_common_word` | `Counter(text.split())` | case-insensitive count; lowercase result | case-folding | 0.33 |
| average-empty | `mean` | `sum(xs)/len(xs)` | empty list returns 0.0, never raises | unhandled empty input | 0.67 |
| clamp-range | `clamp_score` | `return max(x, 0)` | cap at 100 as well as floor at 0 | forgotten upper bound | 0.67 |
| round-half-up | `round_money` | `return round(x)` | half-up rounding, not banker's (`round(2.5)==2` is wrong) | wrong rounding rule | 0.50 |
| pagination-last-page | `num_pages` | `total_items // page_size` | partial final page still counts | dropped partial page | 0.50 |

Diversity is deliberate: 10 distinct defect classes so a measured effect is not
an artifact of a single bug shape. The first five are the strongest
requirement-space gates (a substantive orthogonal clause); the last four are
lighter but each still gates on a *separately stated clause* the quick check
skips — which is exactly what distinguishes them from `discount-floor`.

## Excluded (documented)
- **`discount-floor`** (Step-0 null) — floor division is requirement-*trivia*
  (one extra value of the same computation catches it; no separate requirement
  clause). Fails criterion 4. Kept on disk as the Step-0 artifact; **not** in the
  frozen pack and **not** scored.

## Layout
- `tasks/<slug>/prompt.md` — the prompt (states the full requirement; arm sees).
- `tasks/<slug>/solution.py` — the seeded-defect starter (arm sees, edits).
- `oracle/<slug>_oracle.py` — held-out deterministic scorer (`FN` / `WEAK_CHECK`
  / `CHECKS`; arm never sees); writes `grading.json`.
- `oracle/_harness.py` — shared grade/load machinery.
- `oracle/fixtures/<slug>_fixed.py` — reference correct fix (gate-only; arm never
  sees).
- `wellformedness.py` — the pre-freeze 3-way gate.

## Not yet frozen here — the arms (Phase 2, pending operator sign-off)
The arm briefs (`arm_A_clippy`, `arm_B_actfirst`) and the k=3 dispatch are the
validity-critical step (fairness / anti-strawman per the experiment doc) and are
decided with the operator before any compute is spent. This file freezes the
**tasks + oracles** only.
