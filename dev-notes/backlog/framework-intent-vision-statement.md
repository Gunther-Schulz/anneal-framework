# Framework intent / vision statement — candidate articulation (ratify, don't canonize)

**Status:** OPEN — surfaced 2026-06-06 (operator's strategic step-back: "what's the intent as you
see it? is it worth it / do we ever reach V1?"). **LOW-gating** — a foundation-level articulation;
does NOT block the proof-first order (harness → enforcement-batch → verdict). Foundation-level edit
→ `foundation.md` (or a dedicated VISION), via anneal-dev + **irreducible operator soundness** (the
intent is operator-owned — see caveat 1).

## Candidate articulation (Claude's synthesis 2026-06-06 — for the operator to RATIFY or correct)
> The framework is a **trust-manufacturing process for AI work**. Its rubric (`foundation.md`:
> "grounded claims + a complete, coherent picture") is about output you can **trust without
> re-checking it yourself**. The mechanism is specific: **replace AI self-discipline with
> structural enforcement on the load-bearing steps** — un-fakeable artifacts, fresh-context
> verification, falsification, the operator as irreducible gate. Because the AI is a *satisficing*
> reasoner, anything that depends on it *choosing* rigor leaks (the loaded-but-inert class). So the
> deepest move is to make rigor **structural, not willed**. Seen that way the gap-hunt has a shape:
> each gap is a place the framework still leans on the AI's *will* instead of structure — finite,
> asymptoting toward **"rigor enforced, not hoped for."**

## Caveats (load-bearing — the reason this is a candidate, not a done edit)
1. **Ratify, don't canonize.** This is *Claude's synthesis* — grounded (it falls out of foundations'
   "grounded + complete" rubric + the session-9 structural-enforcement-vs-self-discipline theme) but
   an **interpretation**. The intent is exactly what only the operator can certify; baking Claude's
   reading into the canonical spec as the stated intent is the "launder my view as authoritative"
   risk. The operator confirms / corrects / rewrites before it enters the spec.
2. **Home is NOT `foundation.md`** (corrected 2026-06-06 — see Grounding below; foundation.md is 3
   architectural *contracts*, not a why-doc). And the *trust* half is **already canonized** (README
   tagline + core.md Purpose); only the **mechanism + asymptote** half is net-new. Real home options
   in Grounding.
3. **Discipline:** foundation-level kernel edit → anneal-dev + operator soundness (fitting: the
   soundness gate is the operator, and the intent is the thing only they can certify).

## Grounding (2026-06-06 — where intent already lives + what's actually new)
Checked the canon before treating the candidate as net-new:
- **Already canonized (the trust half):** README tagline **"Convert AI confidence into AI evidence"**
  (the north-star one-liner) + `spec/core.md` **Purpose** (the rubric: grounded claims + a coherent,
  complete picture, operating within the 3 `foundation.md` contracts). The candidate's
  "trust-manufacturing / trust-without-re-checking" framing *restates* these — not new.
- **NOT canonized (the new half, worth persisting):** the **mechanism** (replace the *AI's*
  self-discipline with structural enforcement on load-bearing steps) + the **V1 asymptote** ("rigor
  enforced, not hoped for"; each gap = a place still leaning on AI will). core.md Purpose states the
  *goals*, never the *how*. This is the genuinely-additive contribution.
- **Real home options** (foundation.md ruled out): **(a)** a one-paragraph "Mechanism" clause
  appended to core.md's **Purpose** (goals → how they're secured; keeps goals + mechanism + the
  contract-reference co-located — *lean*); or **(b)** a dedicated short root `VISION.md` the README
  tagline points at (philosophy out of the spec spine).

## Two analog-sharpenings the candidate needs before canonizing (it overclaims twice)
1. **"structural, not willed" vs the operator gate.** The operator is the *deliberately-irreducible
   willed* gate (foundation + `core.md §3.1`: the AI can't certify its own foundation). Precise
   claim: structural enforcement replaces the **AI's** self-discipline; the operator's judgment is
   the load-bearing willed *exception*, NOT a gap to close. Asymptote = "all rigor that *can* be made
   structural is, leaving the irreducibly-human gate" — not "no willed rigor anywhere." Un-carved,
   the every-edit test ("does this move rigor willed→structural?") would wrongly target the operator
   gate for elimination.
2. **"the AI is a satisficing reasoner"** → state the *observed failure mode* (rules load but don't
   fire — the loaded-but-inert class; clippy Unit-18, skill-craft-antipatterns), which is
   evidence-backed per the grounded-claims rubric, rather than a categorical cognitive assertion.

## Why it's worth doing (composes with the V1 question)
A crisp intent statement is **half of what makes "V1" definable**: V1 = the intent's
structural-enforcement asymptote reached to a *tolerable residual* (the AI reasoning-ceiling is
irreducible — `design-decision-implication-depth-gaps` obs 3) **AND measurably validated** (the
proof thread). Intent statement + measurement = the answer to "do we ever arrive." It also gives
every future edit a test: *does this move rigor from willed → structural?*

## Relates to
- `spec/core.md` **Purpose** — where the "grounded + coherent/complete" rubric actually lives (+ the
  lean home option (a)); `README.md` tagline "Convert AI confidence into AI evidence" — the existing
  north-star. `foundation.md` — the 3 contracts the Purpose operates within (NOT a vision home).
- `anneal-empirical-validation-experiment` / `measurement-harness-mve` — the *measurement* half of
  the V1 definition (the intent statement is the *target* half).
- `skill-craft-antipatterns-loaded-but-inert` / `convergence-cycle-mechanical-enforcement` — the
  structural-enforcement-over-self-discipline theme this articulates (the gaps ARE "still leaning
  on will").
- Origin: operator strategic step-back, 2026-06-06.
