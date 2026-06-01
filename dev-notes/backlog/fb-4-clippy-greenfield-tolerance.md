# FB-4. Clippy greenfield tolerance — verify (and maybe other bindings) assume existing code

**Status:** open finding — instance-level (clippy), low-priority / parked. Origin: `../planner-instance-exploration.md` finding 1.

**Gap.** Clippy assumes a *brownfield* project (existing code to ground
against). The assumption is concentrated in `verify.md:50` — "run the
project's test suite, build, and linters" — which silently assumes those
exist. On a brand-new / empty project there's nothing to run, so verify
has no footing.

**Not a framework change.** The framework (anneal) is already
greenfield-tolerant *as written*: the basis rule (§3.2) treats absent
evidence as a first-class assumption (not error); scope search returns
legitimately-empty sets; it leans on [CONDITIONAL] / [AUTO-ACCEPTED]
early and self-heals as the project grows. The framework must **not**
grow a greenfield *mode* — that would leak a corpus-state distinction
into the domain-agnostic core (a contract-1 violation, same discipline
as the de-pollution cluster). So this is an **instance-level** clippy
fix.

**Work.** Sweep clippy's bindings for the brownfield assumption and make
each degrade gracefully on an empty project. Only `verify.md:50` is
confirmed by read; `lenses.md` and `investigate-design.md` are unchecked
and likely carry the same assumption.

**Urgency.** Low — only bites when clippy is pointed at an empty repo.
Orthogonal to the planner build (clippy grounds against *code*; an empty
repo has none regardless of spec quality).
