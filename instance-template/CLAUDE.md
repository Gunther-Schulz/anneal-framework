## The skill content is rendered, not authored

<Instance> is an *instance* of the Anneal framework. The skill
files — `<skill-dir>/SKILL.md`, `phases/`, and `references/` —
are **rendered** from the framework spec (the `anneal-framework`
repo, `spec/`) and from this instance's `spec/` folder. They are
not authored here, and are never where a behavior change
originates.

A change to how <Instance> behaves goes to the framework spec or
the instance spec first: committed there, then re-rendered into
these files and verified in a separate context — the procedure
is `development-process.md` in the `anneal-framework` repo.
Hand-editing a skill file as if it were source breaks
re-derivability: the spec and the instance drift, and the change
cannot be reproduced for another instance.

This rule covers the skill *content*. The plugin's packaging —
this file, the READMEs, `plugin.json`, and the like — is
repo-local, maintained in the instance repo directly.

---

<!--
Extend below this section with the instance's own plugin-
housekeeping rules — description sync, version discipline,
component inventory — and any instance-specific behaviors.
-->
