# Anneal Framework — Foundation-Invariants Register

Companion to the Anneal-framework spec; not part of it. The register holds
anneal's load-bearing kernel invariants — the rules the method rests on —
each paired with a genuine **external anchor**: an author, work, and
concept from *outside* the anneal kernel that independently warrants the
invariant. The anchor is the entry's whole justification. `ls` is the
index: `INV-<n>-<slug>.md` is one invariant; `archive/` holds retired ones.

The register exists because anneal never self-certifies its own foundation.
An invariant warranted only by appeal to another part of anneal is
warranted in a circle. Pairing each load-bearing invariant with an
independent, external source is how the kernel earns the claim that its
foundation is sound — grounded somewhere anneal does not control.

## Membership rule (anchor-gated)

An invariant earns a slot **iff** it is both:

1. a **live kernel invariant** — a rule the kernel actually holds today
   (located in the kernel, not a candidate sharpening); AND
2. carries a **genuine external anchor** — a concept from outside the
   anneal kernel that warrants it.

An invariant anchorable only to anneal itself is **EXCLUDED** — it stays an
ordinary kernel rule and does not enter the register. This exclusion IS the
anti-bloat gate: the register is not a catalogue of every kernel rule, only
the load-bearing ones that an external source independently grounds. The
anchor requirement is what keeps the register small and the entries earned.

## The per-kernel-edit artifact

When a method-kernel edit touches a registered invariant, it produces a
**per-touched-invariant holds/violates-against-anchor ledger** — one line
per touched invariant, recording whether the edited kernel still holds
against that invariant's external anchor or violates it.

This ledger is a **focusing input** for the operator's soundness pass — it
names which invariants the edit touched and which anchors to satisfy, so
the operator's review is aimed. It is explicitly **NOT a soundness
verdict.** The operator originates the verdict; the artifact focuses it,
never pre-empts it. (Wired into the method-kernel-edit discipline at
`development-process.md` §2 and the release-loop step-4 discharge; the AI
produces the artifact, the operator judges soundness.)

## Anti-false-comfort residual

**Register-clean ≠ sound.**

The register catches breaks against invariants that are **already written
down**. It cannot catch novel unsoundness — a way the edit is wrong that no
registered invariant names. That residual is the operator's, always: the
machinery **shrinks and focuses** the operator's soundness pass, it never
removes it. (Gödel: a system does not certify its own consistency from
inside.) Dogfood plus an outside check — never dogfood alone.

A green per-edit ledger means "no break against the invariants we know to
write down," not "sound." Read it that way.

## Protection — the Invariant-change-ratified marker

Modifying or deleting a registered invariant file requires an
`Invariant-change-ratified: <operator-approval-ref>` line in the commit
message (checked by `hooks/commit-msg`; marker shape parallels the
established `Coherence-audit-handoff:` marker).

Honestly, this is an **audit-trail + deliberate-friction** mechanism — not
an unbypassable gate. The marker is visible, ratification-claiming, and
logged in git history, making invariant-weakening a deliberate, recorded,
operator-claiming act rather than a silent edit. It is NOT binding on its
own: `--no-verify` bypasses it, and a local hook cannot verify an operator
actually approved (that would be operator-detection, a malformed
enforcement form per `foundations.md`). The real binding is AI-discipline
plus the operator's review catching a bogus ratification claim. Adding a
*new* invariant file is exempt — extending the register does not weaken the
foundation.

## Term definitions

Defined here (a dev-notes companion defines its own terms in its README,
per the validation-watch precedent) — NOT in `spec/glossary.md`, which
would leak a dev-process concept into the domain-general spec.

- **Foundation invariant** — a load-bearing kernel rule the anneal method
  rests on, which the kernel holds today AND which a genuine external anchor
  independently warrants. The pairing with an external source is what makes
  it a *foundation* invariant rather than an ordinary kernel rule.

- **Foundation-invariants register** — this companion folder: one
  `INV-<n>-<slug>.md` per foundation invariant, this README, and `archive/`
  for retired entries. The set of invariants whose external anchors warrant
  the kernel's foundation.

- **Anchor-gated** — the membership rule: an invariant enters the register
  iff it is a live kernel invariant AND carries a genuine external anchor.
  An invariant anchorable only to anneal itself is excluded. The gate is
  the register's anti-bloat mechanism.

- **Per-edit holds/violates artifact** — the per-touched-invariant ledger a
  method-kernel edit produces, recording each touched invariant as
  holds-or-violates against its external anchor. A focusing input for the
  operator's soundness pass; not a soundness verdict.

- **Invariant-change-ratified marker** — the `Invariant-change-ratified:`
  commit-message line required when a commit modifies or deletes a
  registered invariant file. An audit-trail + deliberate-friction
  mechanism (visible, logged, ratification-claiming), not an unbypassable
  gate.

## Considered and excluded

Two candidate seeds were considered and **excluded** — documenting the
membership gate working:

- an **"exclusion-obligation"** rule, and
- a general **"falsifiability-gate"** acceptance gate.

Both are candidate *sharpenings*, not invariants the kernel holds today.
Research finding [5]
(`dev-notes/research/process-literature-deep-research-2026-06-03.raw.json`)
frames the latter as an "importable acceptance gate sharper than
re-checkability" — i.e. adoptable, not held. Their live form is already
carried by INV-5 (exclusion via a named, runnable falsifier); the
standalone candidate gates remain backlog material, not register entries.
