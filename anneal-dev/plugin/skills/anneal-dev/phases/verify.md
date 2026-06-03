# verify

The final phase of an anneal-dev run: it checks the completed rule-text
against the locked design and the standardized lenses, and ends
[PASSED] or [ISSUES FOUND].

## Isolation

verify is conducted in a context **isolated** from the run's working
context — the one that ran investigate-design and implement. The context
that wrote the rule-text does not check it: an actor checking its own
work carries its anchoring and blind spots into the check — and a
renderer is blind to its own flattening (the renderer reads its output
as faithful). verify works from artifacts alone — the current run's
tracker (`.anneal-dev/runs/<this-run>.md`), `lenses.md`, the produced
rule-text — so the isolated context is fully equipped. Prior-run
trackers are not basis material (`foundations.md`); the current tracker
must carry re-grounded basis for anything verify checks against. The
isolation is the load-bearing property; the orchestrator (`SKILL.md`)
establishes that isolation (in anneal-dev, via a subagent spawn) each
time verify runs. The property is unconditional, not a per-task
judgment; the mechanism for achieving it is instance-specific.

verify's recorded result names the context it was conducted in
(isolated, or without isolation), so a [PASSED] carries whether the
check was independent. If an isolated context genuinely cannot be
established — no subagent can be spawned — verify is still conducted,
without isolation — the spawn-fallback — and its result records that; an
un-isolated verify is never silently taken as though it were
independent.

## The three checks

verify runs three checks over the completed work:

1. **Planned vs actual.** Check every locked design decision
   (`tracker.md`) against what the rule-text actually does. **Also check
   the rule-text for material elements not covered by any locked
   decision** (design-completeness audit): a material element surfaces
   as a finding classifying why it wasn't surfaced at design time
   (judged-non-material, forgotten, scope-overflow, missed-pattern, or
   cited-other). "Material" means: implementing the same locked decision
   in a way that yields a different value at a named **contract surface**
   (`anneal-framework/spec/glossary.md`; instance-defined — for
   corpus-evolution: the AI behavior a rule forces, the
   evidence-bearing artifact it requires, the closed set it names, a
   cross-reference a dependent resolves through, a "must" a render
   carries structurally). Realization-output detail (the exact wording,
   synonym choice, internal section ordering that changes no rule) does
   not yield such a value-change.
2. **Standardized lenses.** Apply the standardized lens set
   (`lenses.md`) to the produced rule-text.
3. **Executing the verification.** Run the domain's executable
   verification — anneal-dev's **3-check battery** (`bindings.md`
   Verification battery) — and show its output. "Executable" means each
   check is **dispatched/run, not asserted**. verify does not pass on
   static inspection alone. The battery's three dispatched checks:
   - **(a) Render-fidelity (separate-context).** For every changed rule
     that is rendered into a plugin, the rendered clause is checked
     **clause-by-clause against its source spec** in a context isolated
     from the one that wrote the render. This inherits verify's
     framework-mandated isolation: verify as a whole runs in a context
     separate from the one that produced the work, so the
     render-fidelity check is conducted by a context that did not write
     the render. The check confirms structural mechanisms survive as
     structural — closed enums stay enumerated, "must" stays "must" (not
     softened to "should"), no load-bearing clause silently dropped.
   - **(b) Coherence.** Whole-document, cross-file, and whole-corpus
     set-level inspection: every cross-reference resolves, no principle
     is restated-and-drifted across files, no closed set has a member
     stated in one place and missing in another, the changed rule reads
     coherently against the documents it lives among.
   - **(c) Skill-quality review.** Each changed skill file (the rendered
     plugin skills) is reviewed against the skill-design canonical
     guidance — the full canonical sweep for the changed files.

   A check is "run" only when it is dispatched and its output shown
   (checks (a)–(c)). A "verified" claim that asserts more than was
   actually dispatched-and-shown is the over-claimed-verification
   failure shape the lens set watches (`lenses.md`); the battery closes
   it by making each check an artifact the isolated verify context
   produces, not a claim the working context makes.

**Operator approval is not a battery check.** verify runs **isolated
from the operator** (Isolation above), so it cannot run an operator
action. The resulting rule-text diff is approved by the operator at
verify's presentation — the §1(a) menu-selection / release-loop commit
gate — **downstream** of verify's [PASSED]. It is the domain's analogue
of shipping a green build, not a check the isolated verify context runs.

## Account for every check

verify accounts for every check — no check silently absent. Each
planned-vs-actual check, and every standardized lens (applied where it
is in scope, or given a one-line cited reason it is not), either holds —
recorded as a cited-clean line — or yields a divergence from the locked
design or a lens issue. A failed run of any battery check is likewise an
issue.

Any non-failure output a battery check surfaces is also a finding unless
the project has explicitly de-prioritized that output class.
**De-prioritization** requires an artifact: a project config naming the
class, or a tracker entry recording the class + reason.
De-prioritization without an artifact is the silent-substitution shape
(`foundations.md`) the rule rejects.

Record every divergence or issue as a finding (`tracker.md`), entering
the finding track at [PENDING].

## Terminal result

verify ends in one of two results:

- **[PASSED]** — every check accounted for, and no finding short of
  [VERIFIED].
- **[ISSUES FOUND]** — otherwise. This returns the run to
  investigate-design — the single locus for fix resolution. The fix runs
  through the full procedure (investigate-design → implement → verify);
  no in-place shortcut at verify-terminal. See Re-run scope below.

The result is recorded as an evidence-bearing artifact (`foundations.md`):
the result line is paired with a **finding-status ledger** enumerating
every recorded finding's status — including the **disposition suffix** on
each [VERIFIED] entry (`references/tracker.md`, finding-state #3). A
[PASSED] alongside any finding short of [VERIFIED], or any [VERIFIED]
without a cited disposition, is a malformed artifact. Format:

```
Verify result: [PASSED] (isolated)
Finding ledger:
  F1 [VERIFIED — addressed]
  F2 [VERIFIED — non-issue]
  ...
  F34 [VERIFIED — deferred]
```

## Re-run scope

When [ISSUES FOUND] returns the run to investigate-design and the fix
flows through the full procedure (design re-cycled, implement re-run),
verify re-runs as either:

- **Fresh verify pass** — full re-attest of the three checks (planned vs
  actual, lenses, the battery). Default — required when the closing fix
  is not behavior-preserving.
- **Delta verify** — confirm the named finding closed + minimal
  regression. Permitted when the closing fix is **behavior-preserving**.

**Behavior-preserving** (`bindings.md` Behavior-preserving
classification) = a rule-text fix that does **not** change which rules
the corpus encodes nor what any rendered plugin clause prescribes — e.g.,
a pure copy-edit, a basis-only strengthening, a wording tightening that
preserves every "must" and every closed-set member. A fix that
adds/removes/re-strengthens a rule, or that re-renders a clause whose
prescription changes, is **not** behavior-preserving and triggers a
fresh verify pass.

Classification recorded in the tracker on the re-dispatch entry;
un-classified defaults to fresh verify (fail-closed). The delta-verify
dispatch prompt is scoped accordingly: no D1-Dn re-attest, no full lens
re-apply — confirm the finding closed, run the regression. Subagent
honors the scope.
