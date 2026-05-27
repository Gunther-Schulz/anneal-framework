# <Instance> Specification

<Instance> is the Anneal framework instantiated for <domain>.
The framework's method — phases, tracker, status-state machine,
basis rule, evidence-bearing-artifact rule — is specified in the
`anneal-framework` repo (`spec/`). That spec is domain-general;
this document set binds it to <domain>.

This `spec/` folder carries the slots the framework leaves to
the instance. Per `anneal-framework/instantiation-guide.md` §2
the slot set is **closed**: an instance fills declared slots,
does not invent new ones.

**Required:**

- `bindings.md` — domain bindings
- `persistence.md` — run-artifact persistence mechanism
- `lens-set.md` — the standardized lens set

**Optional** (delete the file if your instance does not declare
the slot):

- `presentation.md` — instance presentation
- `extensions.md` — lifecycle extensions
- `lens-supplement.md` — lens-supplement mechanism declaration

Refer to `anneal-framework/instantiation-guide.md` for each
slot's definition and shape constraints; this folder's files
are the instance-side filling-in.
