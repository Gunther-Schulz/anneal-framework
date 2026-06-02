# skill-craft: add a provenance-vs-load-bearing discriminator to the Soft-load-pointer anti-pattern

**Status:** OPEN — queued for a future skill-craft cycle. Small, Path-1
(incident-grounded). Surfaced 2026-06-02 by the anneal-dev step-5 render
skill-craft review.

## The change
skill-craft's **Soft-load-pointer** anti-pattern (`references/anti-patterns.md`,
entry #17 / the anti-patterns file) keys on *"reference named in prose without an
observable load step."* That description matches **two different things**:
- (a) a genuine soft-load-pointer — the load-bearing content lives in the named
  file and must be loaded; and
- (b) a **provenance citation** — the content is rendered **inline**; the named
  file is cited for source-attribution / re-render fidelity.

It doesn't discriminate them, so a reviewer flags (b) as a violation. That
happened: the anneal-dev verify-battery clause cited `bindings.md` for provenance
*while rendering the battery inline*, and the skill-craft review subagent raised a
**false-positive blocking** (re-derived against `verify.md:57-82` /
`implement.md:108-161`).

**Fix-shape:** add a discriminator clause — a citation is a soft-load-pointer only
if the load-bearing content is **NOT present in a loaded file**; a
provenance/source-attribution citation of inline content is not one. **Test:**
would the AI behave wrong WITHOUT loading the named file? Content inline → no. The
discriminator doubles as a reviewer guard against the false-positive.

## Discipline notes
- skill-craft **canonical** edit (`references/anti-patterns.md`) → routes through
  the skill-craft gate + the Layer-4 self-review mandate when done.
- Apply Edit-as-Pareto: this *adds* a discriminator, so it must earn its place —
  it does (it prevents a recurring false-positive class), but check it doesn't
  bloat the entry; ideally fold the discriminator into the existing test, not a new
  sub-section (Amendment discipline).
- Grounding: skill-craft `dev-notes/OBSERVATIONS.md` #26.

Relates to [[framework-dev-as-anneal]] (surfaced during its step-5 dogfood).
