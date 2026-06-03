# Complete the glossary as the binding-table interface (the technical binding terms)

**Status:** OPEN — spun off 2026-06-03 from the `cite-glossary-not-section-numbers` run
(D6 [AUTO-ACCEPTED]). The §-number citation convention (FB-3) is settled + the §-cited
method-concept gaps closed (3 headwords added); THIS item is the caveat's separable
"real work" — making the glossary cover the binding-table left column too.

## The gap (enumerated, not yet closed)

The instance binding table (`<instance>/spec/bindings.md`, `| Framework term | domain
value |`) is the OTHER instance-facing interface — its left column names framework terms
an instance binds. Several have framework-specific meaning an instance author would
otherwise read `core.md §3.2` to obtain, but are NOT glossary headwords (confirmed by run
subagent `aa8a9e95d7b3601e9` + spot-checks):

- **a located read of the source** (not a headword; in `Basis` prose only)
- **a construct taken whole** / true-unit / visible-close (no headword)
- **exhaustive search of an element's dependents** / "search" (no headword; `Completeness
  claim` says basis "is a mechanical search" but `search` is undefined)
- **the domain's executable verification** (no headword; in `Basis` prose glossary:52)
- **an element of the work product** (no headword; "element" only in prose)
- (the work product's **containers** — anneal-dev binding; check)

Self-evident binding terms (`the task`, `the problem space`, `existing work`) likely do
NOT need headwords — they carry no hidden framework semantics. The discriminator to apply:
**a framework term needs a glossary headword iff an instance referencing it would otherwise
read the framework spec to learn its precise meaning** (avoids both a leaky firewall and
Additive-reflex bloat).

## Why separate (not folded into the FB-3 run)

The §-number rule + its §-cited-concept gaps fully unblock every instance re-render
(binding-table terms are prose, not §-cites — re-rendering anneal-dev does not require
them). This is an interface-completeness improvement, not a re-render blocker. Folding it
would have bloated the keystone-unblock run (run F9/D6 reasoning).

## Done when
The binding-table left-column terms that pass the discriminator have glossary headwords;
an instance can resolve every framework term it binds through the glossary (no spec read).

## Relates to
- `cite-glossary-not-section-numbers.md` (this run's source finding; its caveat = this item).
- `planner-instance-exploration.md` finding 4 + the slot-collapse fork (FB-3's sibling).
- The settled FB-3 convention: `instantiation-guide.md` §3 "Referencing the framework" +
  `spec/README.md` glossary-as-interface bullet (this item extends that interface to the
  binding table).
