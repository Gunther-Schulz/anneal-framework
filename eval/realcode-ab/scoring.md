# Scoring — real-codebase A/B (the bug "oracle")

The replay engine at the pre-fix state (`1f62d57d^`) contains these real defects (confirmed by the
actual Unit-27 fix for #2/#3, by trace + the project's own fix for #1/#4, and #5 is the documented
depth-gap). An arm **"found"** a bug iff its findings list identifies it (file:line or unambiguous
description). Count a "lower-confidence / uncertain" flag **conservatively as NOT found**. Judgment-scored
(no automated oracle — these are real-codebase reviews, not the synthetic seeded-defect tasks).

| # | bug | locus | shape | catch requires |
|---|---|---|---|---|
| 1 | **market_id wrong-provider** | `re_score.py:659` (vs `ev_plus.py:338`) | cross-module provenance; var misnamed `pinnacle_market_id` | trace leg's market_id to its producer (betting-provider, not Pinnacle); distrust the name |
| 2 | **team_qualifier crash** | `outcome_derivation.py:133` (fed `re_score.py:678`) | wrong-logic in focal fn + crash | spreads have `team_qualifier=None`; the guard raises |
| 3 | **handicap sign (AWAY spread)** | `outcome_derivation.py:141` | wrong-logic in focal fn | HOME-perspective handicap unflipped for AWAY |
| 4 | **closing_lines CLV backfill** | `closing_lines.py:254` | provenance (sibling of #2) | `team_qualifier == outcome` never matches `None` spreads → NULL spread CLV |
| 5 | **period omission** | `derive_outcome_result` (no `period` param) | **negative-space / dropped dimension** | notice picks carry `period` but settlement uses a full-game-only score → non-full-game picks mis-settled |

Bonus (seen, outside the core 5): `max_bet=0` sentinel zeroes stakes when no provider cap; multi-leg arb
only settles `legs[0]`. Both real; not used in the headline tally.

## Per-shape catchability (the qualitative finding)
- **#2,#3 (wrong-logic, in the focal fn):** everyone catches under a non-blind task that names the
  derivation step; **act-first under a BLIND task drops these** (no step-list steering).
- **#1,#4 (provenance, cross-module):** only the explicit trace-to-producer directive (adhoc) catches
  reliably non-blind; generic discipline ≈ act-first; under a blind task, *act-first* drifts toward #1.
- **#5 (omission):** missed by **every single-pass arm, every framing (0/15+).** Needs independent /
  convergence pass (the pending process test) — generic thoroughness ("verify each kind") catches it only
  ~half the time non-blind, and that was a task-framing artifact.

## Result tables
The ×5 finding-rate tables (non-blind act-first/vanilla/adhoc; blind act-first/vanilla) live in
`../../dev-notes/backlog/anneal-empirical-validation-experiment.md` (Addendum 1 + Addendum 2) — single
source of truth, not duplicated here to avoid drift. Headline: non-blind looked like a dose-response
(2.6/3.4/4.4); **blind collapsed it to a tie (2.2 vs 2.4)** → the prompt-disciplines effect was a framing
artifact; the framework-as-process remains untested.
