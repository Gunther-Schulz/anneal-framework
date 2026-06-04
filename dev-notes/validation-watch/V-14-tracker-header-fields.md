## V-14. Emergent tracker-header fields — codify or leave instance-free?

**Status: WATCHING.**

**Decision (`modules.md` §3.1).** The 2026-05-26 light tracker
formalization requires `Status` and `Phase` as instance-defined
closed enums (plus run identifier, mode, task summary as the
core header fields). It does **not** formalize emergent fields
observed in practice — specifically `Protocol` (Clippy version
stamp, observed in Unit 16's tracker) and `Cycles complete`
(count + per-cycle summary, also Unit 16). The framework's
header schema currently names only the core required fields;
emergent fields are instance-free.

**Why uncertain.** These fields appeared organically in the
most recent run and look useful but are n=1 at this shape.
The formalization-vs-instance-freedom trade-off is unsettled:

- *Codify (broader header schema):* cross-instance consistency,
  audit-trail predictability, easier retroactive audits.
- *Leave instance-free:* preserves evolution; instances carry
  different metadata as their domains demand.

The codify-path risks freezing emergent shape from n=1; the
instance-free path risks drift that future retroactive audits
will struggle with.

**Production signal to watch.** Tracker review across future
runs:

- Whether `Protocol` and `Cycles complete` recur in subsequent
  Clippy runs
- Whether daneel or campaign-craft trackers develop their own
  emergent-field set (different from Clippy's)
- Whether new emergent fields appear that warrant inclusion
- Whether the absence of formalization causes AI confusion or
  drift about what to put in the header

**Closing criterion (WATCHING → RESOLVED via codify).** One run
where the emergent fields appear with content that semantically
matches the prior emergence (Protocol version stamp; Cycles
complete count) — codify at instance-level
(`references/tracker.md` extension) or framework-level
(`modules.md` §3.1 extension) per scope. One cross-instance
recurrence is equivalent positive evidence.

**Alternative closure (WATCHING → INVALIDATED).** One run shows
the emergent field set drifted (different fields, different
semantics) from the prior emergence — accept instance freedom as
design intent; document as observation, no codification.

**Operator-pull codification (2026-05-28).** `Implementation
model` added to clippy's `references/tracker.md` ahead of V-14's
emergence-trigger — operator-empirical motivation (Sonnet vs
Opus impl quality comparison), not cross-instance recurrence.
The methodology already produces comparable artifacts
(verify-terminal Status, loopback count, verify cycles to
PASSED); stamping the impl model closes the comparison loop.
Codified at instance-level per V-14's preferred path. V-14
remains WATCHING for the original Protocol + Cycles-complete
question; this codification is recorded as observation.

---

