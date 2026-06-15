# instance-template doesn't scaffold the mechanism slots

**Status:** ✅ DONE 2026-06-07 (anneal-dev run `f0-render-conventions`, verify [PASSED] + operator
soundness SOUND; release `<pending-this-commit>`). The slot-as-file-vs-section "fork" was already
settled in the live corpus (template README:53-59 — file-per-slot in template, instances may
consolidate); the real gap (missing `isolation.md` scaffold + README enumeration omission + the
guide's internally-contradictory file-vs-section framing) is closed by D2 (`instance-template/spec/
isolation.md`), D3 (README "Required slots" + isolation), D5 (guide §2 reconciliation clause).
Archivable.

_Original finding (2026-06-01, Cycle a):_

`instantiation-guide.md` §2 claims the template "scaffolds a placeholder file
for every slot the framework recognises." But `instance-template/spec/` carries
only the bindings TABLE + `lens-set.md` — it does NOT scaffold placeholder
sections for the **mechanism slots**: run-artifact persistence (pre-existing)
and now isolation (declared in Cycle a). Clippy carries both as prose sections
in its `bindings.md`, but the template never pre-scaffolds them.

**Design question to settle first:** slot-as-file vs slot-as-section. Clippy
keeps mechanism slots as sections inside `bindings.md`; the guide's wording says
"placeholder *file* per slot." Resolve the model, then scaffold the template to
match (persistence + isolation placeholders) so the guide's claim holds.

Bounded (affects 2-3 slots), low-urgency. Relates to
[[contract1-depollution-cluster]].
