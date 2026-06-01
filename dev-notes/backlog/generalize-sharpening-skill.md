# Generalize the sharpening skill — extract a PBS-decoupled standalone (sibling to coherence-audit)

**Status:** open item — cross-repo tooling extraction, low-priority / parked.
Surfaced 2026-06-01 during the `framework-dev-as-anneal` decision-design
session, which ran `pbs:decision-design-sharpening` and had to substitute
anneal's own anchors (foundation contracts / practice 9 / validation-watch)
for the skill's PBS-internal apparatus. Relates to `framework-dev-as-anneal.md`.

**Gap.** The sharpening discipline family — `sharpen`,
`decision-design-sharpening`, `pre-implementation-sharpening` — lives **only**
inside `pbs-bureau/plugin/skills/`. There is **no standalone generalized
version** (confirmed 2026-06-01: full repo scan + code search + installed-plugin
scan). Two coupling facts:
- `sharpen` is generic *in spirit* (its "Spirit" section is domain-general and
  self-applicable) but is still namespaced under `pbs` and carries ~4 residual
  PBS references (`DISCIPLINES.md`, `profiles/`, G/D gates).
- `decision-design-sharpening` is the **most** PBS-coupled of the three — its
  entire Round-1 termination checklist is built on PBS `profiles/` + G/D gates
  + a PBS `GLOSSARY`, none of which map onto a non-PBS corpus.

**Precedent.** Other PBS corpus-disciplines were already extracted into
standalone generalized repos+marketplaces: `coherence-audit`
("lens-driven set-level scan for rule corpora"), `architecture-audit`,
`bildhauer`, `skill-craft`. The sharpening family is the conspicuous
non-extracted member. `coherence-audit` is the clean template: a corpus-level
discipline pulled out and used framework-side (anneal practice 12 dispatches it).

**Why it's framework-dev work (the relation).** A generalized sharpening skill
is a tool the framework-dev process *uses*, not a PBS deliverable. Under
`framework-dev-as-anneal.md` Option A, decision-design-sharpening maps onto
anneal's investigate-design/decide phase; a PBS-decoupled version is the clean
tool that anneal-ified process wants (exactly as `coherence-audit` is the clean
tool practice 12 dispatches). So this item de-risks the A effort's tooling.

**Scope / next action (deferred, not designed).** Extract a PBS-decoupled
sharpening skill into a standalone repo + marketplace, on the `coherence-audit`
model. Open design question to resolve when it's picked up: generalize the
**whole family** (sharpen spine + decision-design + pre-implementation layers)
or just the `sharpen` spine, leaving the phase-specific layers to instances.
Lower priority than the A decision itself — capture now so it isn't lost; design
later.
