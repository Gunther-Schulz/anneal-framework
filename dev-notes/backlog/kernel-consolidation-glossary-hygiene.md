# Kernel consolidation + glossary hygiene (coherence-audit follow-up)

**Status:** OPEN — a batched **consolidation cluster** surfaced by the 2026-06-04 coherence-audit
(handoff `ac39b6ab6d5d929cd`). Framework-spec edits → route through **anneal-dev + kernel-independent
verify** (the audit was the floor; these are the edits). F3-theme (fragmentation → consolidate) + the
`core.md` bloat known-debt. Resolvable as one themed cycle, or two tightly-coupled (glossary-vocab +
core/modules consolidation). NOT inline-fixable.

## Findings (from the audit; file:line cited)

### A. Practice-1 triage restated in 3 homes — and the copies drift (L1-a, notable)
The render-gap / spec-gap / adherence-gap triage is canonical at `development-process.md:94-122` (full
machinery: enumerate-three-forms + cited per-form failure) but **restated, not cross-referenced**, at
`modules.md:456-471` (§4.5) and `glossary.md:441-452` — and the copies have drifted to a compressed
paraphrase that lags the canonical wording. **Fix:** one canonical home + cross-ref; the copies index,
don't restate.

### B. Three corpus-evolution terms misfiled in the methodology glossary (L8-a / L9-a, notable)
`glossary.md:359-388` — **Production signal**, **Watch-entry lifecycle states**, **Load-bearing
instance** — are dev-process / validation-watch vocabulary (they cite a `dev-notes/` file as canonical
source; used by **zero** `core.md`/`modules.md` sections), violating the glossary's own declared scope
(`glossary.md:3-7`: terms "every spec section uses"). **Fix:** relocate to a dev-process /
validation-watch glossary home.

### C. "edit cycle" — load-bearing but unglossed; collides with framework "Cycle" (L3-a, notable)
`glossary.md:144` glosses "Cycle" (the investigate-design loop); `development-process.md:177-181`
defines "**edit cycle**" (one scope of change) — load-bearing for the practice-12 audit trigger
(`:486-499`) and practice-5 re-grounding — with **no glossary entry** (a practice-10 self-violation).
**Fix:** gloss "edit cycle" + disambiguate from "Cycle". **Couples to B** — if a dev-process glossary
is created for B, "edit cycle" lands there.

### D. core.md bloat — §4 = 52% of the file; two measured movable points (Bloat lens — NO rewrite)
`core.md` = 976 ln; §4 (phase specs) = ~510 ln / **52%**. Operator's call = **measure-then-cut, no
blind rewrite**. The two concrete movable points:
- **§4.1.4 convergence mechanics (~40 ln, `:408-429`) duplicate `modules.md §3.4` (`:312-390`)** — core
  could state the *requirement* + cross-ref the line-form / predicate mechanics to modules; today both
  carry the full mechanics.
- **glossary entries restate core bodies** instead of indexing them (`glossary.md` Integrity-check /
  Spawn-fallback / Self-check `:208-235` ↔ `core.md §4.2.3 :531-555`; glossary Status-tag `:306-319` ↔
  `core.md §5.2`). Glossary should index; core authors.

## Observation (not actioned)
- **L9-c:** per-entry foundation-grounding is implicit — only `core.md:26-28` cites `foundation.md`;
  sound at the corpus level, traceable-not-recorded. **Keep-as-is** (per-entry foundation citations =
  heavy ceremony, low value at this maturity); flag against future scope-creep.

## Relates to
- coherence-audit handoff `ac39b6ab6d5d929cd` (2026-06-04); cadence baseline reset from `ac1856832b8712fda`.
- `verified-integrity-consolidation` — a *separate* consolidation ([VERIFIED]-integrity family), NOT this.
- `verify-vs-original-requirements`, `impl-green-on-commit` — the audit's other (F1) confirmations, their own items.
