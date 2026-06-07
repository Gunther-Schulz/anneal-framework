# f0-render-conventions — cycle 1 standardized-pass

Lenses in scope this cycle = those the cycle's investigation touched (template scaffolding, the
template README enumeration, the guide's "every slot" claim, the glossary binding-table interface).

- **Missed-dependents** — FINDING (F3/F4): the "scaffolds a placeholder file for every slot" claim
  has dependents beyond the file set — the template README's slot enumeration (`instance-template/
  README.md:33-49`) and guide §2's slot set (`instantiation-guide.md:102-140`). D2 (add the file)
  without D3 (fix the README enumeration) would leave a dependent stale. Both are tracked; the
  enumeration of the claim's dependents is owed in D3's basis at [VERIFIED] (cycle 2).
- **Fragmentation** — CLEAN: the isolation slot's *rule* lives once (`core.md` §4.2.3, pointed to by
  guide §2:102-108); `isolation.md` is a placeholder *scaffold* pointing at that rule (persistence.md
  style), not a second statement of it. basis: located read `instance-template/spec/persistence.md`
  (header → `core.md` §6 + `instantiation-guide.md` §2, no rule-restatement).
- **Undefined-shorthand** — FINDING (F6): the binding-table left-column terms {located read, taken
  whole/true-unit/visible-close, executable verification} are used in instance binding tables but
  have no glossary headword. basis: `grep '\*\*[^*]*<term>' spec/glossary.md` → 0. Routed to D4
  (discriminator pass, cycle 2).
- **Bloat** — CLEAN (this cycle adds no rule-text yet; D2/D3/D4 bodies not drafted). Re-attest at
  the cycle that drafts isolation.md content + headwords. basis: D2/D3/D4 all [PENDING], no prose
  committed this cycle.
- **Unenforced-rule** — NOTE (in scope via F4): the "file for every slot" claim is enforced by
  file-presence (`instantiation-guide.md:404-408` — "file-presence is producer-independent
  re-checkable"), so the fix is to make the artifact exist (D2), not to add enforcement prose. Clean
  given D2. basis: located read `instantiation-guide.md:400-408`.
- **Leakage** — CLEAN (deferred to drafting): `isolation.md` must be domain-general placeholder (like
  persistence.md), no language/tool concretion; re-attest when D2's body is drafted (cycle 2). basis:
  `instance-template/spec/persistence.md` is domain-general placeholder (no concretion).
- **Lossy-render / Over-claimed-verification** — out of scope this cycle: no plugin-clause render
  decision and no "verified/faithful" completeness claim committed this cycle (findings carry
  located-read/search bases, not render-fidelity claims).
