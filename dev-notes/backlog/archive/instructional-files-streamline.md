# Streamline / rename / reorder the instructional-file set

**Status:** [PARKED] — operator-raised 2026-06-03, parked for AFTER `corpus-flows-redesign`
lands. Idea, not yet a design. A clarity/structure pass over the framework's
instructional files now that the routing redesign has settled their roles.

## The prompt
After the corpus-flows-redesign re-anchored the instructional files into a clean
role-map, the operator asked whether the SET can be further streamlined — renamed
or reordered — for newcomer clarity. The current role-map (post-redesign):

| File | Role |
|---|---|
| `spec/` (core/modules/glossary/README) | the method, domain-agnostic — the render SOURCE |
| `foundation.md` | the 3 architectural contracts (upstream) |
| `development-process.md` | governance: routing + release machinery + the 12 practices (canonical routing home, D8) |
| `instantiation-guide.md` | the derivation procedure (the one path not in the channel) |
| `instance-template/` | the new-instance scaffold |
| `CLAUDE.md` | auto-load session orientation |
| `post-run-review.md` | empirical-validation procedure (rendered per instance) |
| `hooks/` | the enforcement floor |

## Candidate questions (for the actual pass — not yet decided)
- Naming: are the filenames the clearest possible for a newcomer (e.g., does
  `development-process.md` read as "governance/routing+release" or could it be
  named for that role)? Is `foundation.md` vs `spec/` ordering legible?
- Reorder/group: would a top-level index (or README section) ordering the files
  by the layering (contracts → method/source → governance → derivation →
  enforcement) help a newcomer more than the current flat root?
- Streamline: any genuine consolidation (NOT just rename) — e.g., is the
  foundation↔spec/README architecture split load-bearing or mergeable? (Apply
  Edit-as-Pareto + Additive-reflex — default to leaving alone unless a real
  consolidation earns its place.)
- The newcomer's path: does a first-time cloner land on a clear ordered entry
  (README → ?) — the D11 bootstrapping anchor is the start; is the rest legible?

## Caveat
This is a clarity/structure pass, NOT a routing change (that's corpus-flows-redesign,
which must land first). Resist rename-churn for its own sake — renames ripple
through cross-references (a practice-4 dependent audit each). Bias toward the
minimal change that improves newcomer legibility.

## Relates to
- `corpus-flows-redesign.md` — settled the file ROLES this pass would re-label/reorder; must land first.
- `framework-spec-cleanup.md` — the spec re-derivation effort (sibling structural-clarity work).
- Method-kernel-adjacent if it touches `spec/*` filenames/structure → anneal-dev + kernel-independent verify.
