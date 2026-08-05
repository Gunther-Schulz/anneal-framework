## V-25. Mechanism-produced-tag fabrication — is separate-checker + operator-catch a sufficient backstop?

**Status: WATCHING.**

**Kind: correctness-watch.** The fix is a stronger forcing function on mechanism-tags (tags emitted only as a mechanism's structured return-state, never orchestrator-authored free-text) — a catcher — so it closes on a *caught* instance: a fabricated [VERIFIED]/COMPLETE tag that the separate-checker (not the operator) intercepts before a terminal (see README closing rule).

**Decision (`foundations.md` Evidence-bearing artifacts).** Status
tags ([VERIFIED], [PASSED], COMPLETE) are weak artifacts —
mechanism-produced, enforced by a separate checker (verify /
convergence re-derives), not self-enforcing. The orchestrator authors
all tracker prose, so it *can* type a status tag the producing
mechanism never ran. The framework accepts this residual: the
separate-checker + operator-catch are the backstop, not a forcing
function that prevents fabrication at authoring time.

**Why uncertain.** No clean structural fix is in hand — the
orchestrator authors all tracker text, so no observable distinguishes
a fabricated tag from a real one in the prose (mechanical-criteria
form fails), and free-text tag authorship can't be gated
(structural-enforcement form fails); the separate-checker IS the
safety-net (3rd form). Whether that backstop *suffices*, or a stronger
forcing function is warranted (e.g. tags emitted only as a mechanism's
structured return-state, never orchestrator-authored free-text), is
the open question.

**Production signal to watch (n=1).** A fabricated mechanism-tag
reaches a terminal and is caught by the *operator*, not the
separate-checker — i.e. the separate-checker proves bypassable in
practice. That warrants designing the stronger forcing function.

**n=1 (seed).** Azuro F18 episode (2026-05-29): the orchestrator
authored D2/D3 [VERIFIED] + run COMPLETE without the loopback / verify
mechanism running; caught twice by the operator. Cycle G (every unit →
subagent) structurally removes the *impl-in-working-context* shortcut
that led to it, but not the tag-fabrication itself.

Per `development-process.md` practice 8, this V-N is legitimate:
genuine uncertainty about whether the accepted residual's backstop
suffices — not deferral of a classifiable fix (the 3-form enumeration
discharges to residual-accepted; no clean structural form available).

