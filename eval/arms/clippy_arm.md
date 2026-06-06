# Arm A — clippy (full anneal discipline)

The treatment arm: the same task, addressed under the anneal method via the
clippy skill (investigate → design → implement → verify, with independent
verification grounded in the stated requirements). Same base model (opus) and
same tools as arm B; the *method* is the only manipulated variable.

## Dispatch prompt (parametrized per run)
> Invoke the **clippy** skill (via the Skill tool) and use its full
> investigate-design / implement / verify discipline to address the task below.
> Treat the stated requirements as the spec to satisfy and verify against.
>
> **Scope (hard rule):** the ONLY file you may read or edit is
> `{WORKDIR}/outputs/solution.py`. Do not read, list, or touch anything outside
> `{WORKDIR}` — in particular there is no wider repository, hidden test suite, or
> scoring oracle to find or consult. Everything the task needs is in the task
> text and that one file.
>
> --- TASK ---
> {PROMPT}
> ---
> The file to edit: `{WORKDIR}/outputs/solution.py`. Keep the function signature.
> When the clippy verify step passes, stop.

Model: opus. Tools: clippy skill + default. If the clippy skill is unavailable
in the subagent, that is a harness finding to report — do NOT silently fall back
to act-first (it would void the arm contrast).
