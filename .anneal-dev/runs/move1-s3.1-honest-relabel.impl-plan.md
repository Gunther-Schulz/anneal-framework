# Impl plan — move1-s3.1-honest-relabel

5 source-edit units (the RENDER-follow set is NOT an impl unit — D7 queues it to the render-debt batch). Each unit invokes skill-craft before editing (rule-corpus). Run-level: Unit 1 first (locks the canonical §3.1 wording), Units 2-5 parallel-eligible after.

**Disjointness basis:** the D1 enumeration partitions by file; Units 2-5 touch pairwise-disjoint file sets (development-process.md / glossary.md+instantiation-guide.md+foundation.md+spec-README.md / anneal-dev-spec / V-25). Search-established by the D1 scope enumeration (F1). Units 2-5 each render Unit 1's locked framing into their site — they READ Unit 1's result but edit disjoint files, so concurrent dispatch is safe once Unit 1 is locked.

- **Unit 1** [first] — `spec/core.md` §3.1 (L111-151): the keystone amend per D2 — producer-independence bind test (L141-142 property), name binding terminus vs self-recorded surfacer, recast "the guarantee comes from the checker, not the artifact". Honors D2, D4 (keep "un-fakeable" as gradient term), D5 (sharpen INV-3 independence). Carry F-B's fence (operator-surfaces ≠ operator-detection-as-enforcement) into the wording.
- **Unit 2** [parallel after Unit 1] — `development-process.md` practices 10/11 (L391/L468) + step-4 (L571-573): reconcile "the X IS the un-fakeable artifact — presence is the check" → weak-artifact/presence-checkable + name the binding party, per D6(b).
- **Unit 3** [parallel after Unit 1] — `development-process.md` practice-12 (L533/539): affirm git-log/marker leg binds (external terminus), audit-content leg surfaces, per D6(c). (Same file as Unit 2 → sequence Unit 3 after Unit 2, OR merge Units 2+3 into one development-process.md unit — merge recommended, same file.)
- **Unit 4** [parallel after Unit 1] — `glossary.md` Evidence-bearing-artifact-rule term (L56-59) + minor-align: `instantiation-guide.md`:394, `foundation.md`:25-26, `spec/README.md`:124 per D6(d).
- **Unit 5** [parallel after Unit 1] — `anneal-dev/spec/` restatements (lens-set L134/144, lens-supplement:27, README:7) + `dev-notes/validation-watch/V-25` alignment per D6.

**Note:** Units 2+3 share `development-process.md` → merge into one unit (sequential within the file). Effective units: 1 (core.md) → then {2+3 merged (dev-process), 4 (glossary+minor), 5 (anneal-dev-spec+V-25)} in parallel (3 disjoint-file units).
