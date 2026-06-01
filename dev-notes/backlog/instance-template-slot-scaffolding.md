# instance-template doesn't scaffold the mechanism slots

**Status:** OPEN finding, surfaced by Cycle a (2026-06-01) while declaring the
isolation slot. Pre-existing; not caused by the de-pollution.

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
