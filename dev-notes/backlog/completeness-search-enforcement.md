# Completeness-search correctness is under-enforced (wrap-tolerance + boundary-regex)

**Status:** OPEN QUESTION — filed 2026-06-03 (operator-requested). **Not** a
settled "needs a structural fix" item: the question is *whether* completeness-search
wrap-tolerance should be mandated/structurally-enforced at all, or whether the
current enforcement (AI-discipline at search-time + the convergence-cycle
falsification pass as the safety net) is adequate. The observations below are
real; the disposition is genuinely undecided. If a fix is ever warranted it lands
in the basis rule (`spec/core.md` §3.2 true-unit basis) + practice 4
(`development-process.md` audit-artifact); method-kernel.

## The rule

A load-bearing completeness claim (a scope, a set of dependents, a flaw class's
instances) must rest on a **re-runnable wrap-tolerant search** — "the corpus wraps
prose, so a multi-word pattern can split across a newline and evade a line grep;
use a distinctive single token **or** flatten newlines before matching (a bare
multi-word line-grep is an incomplete audit)" (`development-process.md` practice 4;
`core.md` §3.2 true-unit basis). The point: the search must not **silently
under-count**, or the completeness claim is false.

## The finding — enforced by AI-discipline only, tripped twice this session

Both trips are the SAME failure family — *a load-bearing completeness search
silently under-counts* — under two different mechanisms:

1. **Over-clever boundary regex (run 1, §4 cleanup).** The `§4.2` cite-count used
   `§4\.2([^.0-9]|$)`; the `[^.0-9]` class (meant to exclude `§4.2.x`) also
   excluded the sentence-terminating period in `§4.2.`, silently dropping 3
   sentence-final cites — true count 23, claimed 20. **Caught by the convergence
   cycle's falsification pass** (run tracker `framework-spec-cleanup-pipeline`, F7),
   which forced the scope decision to re-form.
2. **Bare multi-word line-grep (S3 run).** Several searches used multi-word
   line-greps (`three forms`, `two passes|exactly two`) despite the rule naming
   that exact form "an incomplete audit." Re-checked with newline-flattening on
   operator catch — no actual miss this time (the terms happened not to wrap), but
   the discipline was not followed; the load-bearing claims were saved only by
   *redundant* single-token searches + luck.

The common root: wrap-tolerance / search-completeness is a **prose "must" the AI
follows or doesn't** — the weakest enforcement form. The framework's own
philosophy (evidence-bearing-artifact rule) predicts this fails.

## The open question — enforce at all, or rely on the safety net?

Do NOT presume a fix. The honest question is whether mandating/structurally-enforcing
wrap-tolerance is worth it. Inputs both ways:

**For leaving it as-is (don't mandate):**
- The **safety net already works**: the convergence-cycle falsification pass caught
  the run-1 §4.2 under-count (F7) and forced the scope to re-form; the operator
  caught the S3 multi-word line-greps. Neither false claim shipped.
- Mandating adds **friction** to every completeness search.
- **The obvious structural fix is itself hazardous.** The natural "wrap-tolerant"
  form — `tr '\n' ' ' < file | grep …` iterated over files — wants a shell **loop**,
  and multi-line shell loops **hang** under this harness's Bash tool: it wraps the
  command as `zsh -c '… eval "<cmd>"'` and flattens newlines onto one line, so a
  `for … do … done` loses the separators that terminate it → unterminated loop →
  a child `grep`/`ugrep` blocks on stdin → the command is auto-backgrounded and
  looks "stuck" (cost us a stalled falsification subagent this session, 2026-06-03).
  So a flatten-and-loop helper would *create* a new failure mode. Any enforcement
  must use single-line / `;`-separated / script-file forms, never a multi-line loop.

**For mandating (if the safety net proves inadequate):**
- The safety net is **downstream** (catches after the false claim is recorded) and
  depends on the falsification dispatch-brief saying "be wrap-tolerant" — which is
  itself an un-enforced instruction.
- Two trips in one session suggests the search-time discipline is too soft.

**If a fix is ever chosen**, the three-form options (practice 8) to weigh: mechanical
(hard — can't auto-verify an arbitrary grep is wrap-safe); structural (a basis-shape
check: a completeness-claim's recorded search must be single-token-or-flattened —
but see the loop-hang hazard above); safety-net (the convergence pass, already in
place — perhaps just make its wrap-tolerance brief non-optional). **Decide whether
to act before designing any of these.**

## Side finding (operational, not framework) — multi-line shell loops hang

Independent of the wrap-tolerance question: **multi-line shell control structures
(`for`/`while` loops) in Bash-tool commands hang** — the harness flattens newlines,
the loop loses its terminator, a child process blocks on stdin, the command
auto-backgrounds. Observed repeatedly this session. Operational workaround: write
shell as single-line `;`-separated commands, or put a script in a file and run it;
never rely on newlines as statement separators in a loop. (Captured here because it
*informs* the question above; may warrant its own operational note / CLAUDE.md entry.)

## Relates to
- `framework-spec-cleanup.md` — surfaced during it (both trips were in its runs); the basis-rule/practice-4 home is method-kernel, so a future cleanup run could carry it.
- `archive/skill-craft-hook-subagent-dispatch-block.md` — same shape (a soft, AI-discipline rule that needed a structural enforcement to stop tripping).
