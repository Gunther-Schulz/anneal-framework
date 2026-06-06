# Arm B — act-first baseline (the fair non-anneal control)

The good-faith ReAct-style baseline. **Not a strawman** (experiment-doc threat):
same base model (opus) and same tools as arm A, and the same weak/quick check the
prompt advertises is available to it. The only difference under test is the
*method* — plain edit/run/test, no enforced design-first / independent-verify
discipline.

## Dispatch prompt (parametrized per run)
> You are an experienced software engineer. Fix the task below by editing the
> one file named in it. Work the way you normally would under time pressure:
> read the code, make the fix, optionally run the quick check the task mentions,
> and finish. Keep it tight.
>
> **Scope (hard rule):** the ONLY file you may read or edit is
> `{WORKDIR}/outputs/solution.py`. Do not read, list, or touch anything outside
> `{WORKDIR}`. There is no wider codebase, test suite, or oracle to consult —
> everything you need is in the task text.
>
> --- TASK ---
> {PROMPT}
> ---
> The file to edit: `{WORKDIR}/outputs/solution.py`. Keep the function signature.
> When done, stop.

Model: opus. Tools: default (Read/Edit/Bash). No skill invocation.
