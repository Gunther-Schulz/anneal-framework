# Instance template

This directory is the **starter scaffold** for a new
Anneal-framework instance. To begin a new instance:

1. Copy this entire directory into your new instance repo as the
   seed.
2. Rename placeholders throughout: `<Instance>` (the prose
   name — e.g., "Clippy"), `<plugin-skill-name>` (filesystem
   namespace — e.g., "clippy"), `<domain>` (e.g., "software
   engineering"), `<skill-dir>` (the rendered skill directory
   path).
3. Follow `anneal-framework/instantiation-guide.md` for the
   spec-writing and verification procedure.

## What the template carries

The template surfaces every slot the framework recognises as a
separate file in `spec/`, making the closed slot set visible at
bootstrap time rather than as prose you have to remember.

**Required slots** (must be filled before the instance is
usable):

- `spec/bindings.md` — bindings table answering domain-general
  framework terms with your domain's values.
- `spec/persistence.md` — your run-artifact persistence
  mechanism (where the tracker, standardized-pass artifacts, and
  implementation decompositions live; how a run is resumed).
- `spec/lens-set.md` — the domain's standardized lens set: the
  recurring blind-spots an expert watches for.

**Optional slots** (each placeholder file starts with
"OPTIONAL — delete this file if your instance does not declare
this slot"):

- `spec/presentation.md` — instance branding, menu wording,
  visual flourish.
- `spec/extensions.md` — lifecycle extensions (declared
  behaviors at framework-defined cycle events).
- `spec/lens-supplement.md` — the lens-supplement mechanism
  declaration (where projects supply additional lenses, how
  they are loaded).

## After instantiation

The template's one-file-per-slot structure is for
discoverability. Once your instance stabilizes you may
consolidate (e.g., put presentation as a section inside
bindings.md), as clippy and daneel did — the framework requires
the slot content, not the file structure. Closed-slot discipline
applies regardless of file layout: every render-consumed kind is
declared explicitly, none silently.

## What is NOT included

- The `plugin/skills/` render — generated from spec via
  skill-craft after the spec settles
  (`anneal-framework/instantiation-guide.md` §6).
- Repo-housekeeping (plugin.json, .claude-plugin/, etc.) — those
  are repo-local per the instantiation guide.
