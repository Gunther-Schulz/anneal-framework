# commit-msg hook treats development-process.md / instantiation-guide.md / post-run-review.md as method-kernel SOURCE (broader than the spec's kernel definition)

**Status:** [DESIGN] — genuine hook-vs-spec inconsistency surfaced in run
`release-machinery-batch` (F6); resolving it is a methodology decision (is
`development-process.md` method-kernel?), not a mechanical fix.

## What
The `commit-msg` hook's `KERNEL_SOURCE_PATTERN` (`hooks/commit-msg:61-64`) treats
`development-process.md`, `instantiation-guide.md`, and `post-run-review.md` as
method-kernel **SOURCE** — a commit touching one of these is gated as a
method-kernel edit and the discharge must carry the **Foundation-invariant check**
line. That set is **broader** than the spec's own method-kernel definition.

`development-process.md:24-44` defines the method-kernel as `spec/*` +
`foundation.md` + `anneal-dev/spec/*` only — "anything else is corpus-evolution".
By that definition `development-process.md`, `instantiation-guide.md`, and
`post-run-review.md` are corpus-evolution, NOT method-kernel — so the hook
requires the Foundation-invariant check on commits the spec does not classify as
method-kernel edits.

## The decision (why this is [DESIGN], not a fix)
A genuine hook-vs-spec inconsistency with two candidate resolutions, and which is
correct is a methodology judgment:
- **The hook over-broadens** — narrow `KERNEL_SOURCE_PATTERN` to the spec's kernel
  set (`spec/*` + `foundation.md` + `anneal-dev/spec/*`), dropping the three
  process docs.
- **The spec is too narrow** — `development-process.md` (and siblings) genuinely
  are method-kernel and the definition at `:24-44` should widen to include them.

The crux: is `development-process.md` method-kernel? That is the methodology
question to settle before either edit.

## Relates to
- `commit-msg-hook-packaging-overmatch` — sibling hook-vs-spec inconsistency
  (RULE_CORPUS_PATTERN over-matching packaging); its fix shipped in run
  `release-machinery-batch`. Same shape: the hook's pattern disagrees with a
  spec-level classification.
- `hooks/commit-msg:61-64` (`KERNEL_SOURCE_PATTERN`) — the pattern to change.
- `development-process.md:24-44` — the method-kernel definition the pattern is
  measured against.
- Surfaced by run `release-machinery-batch` (F6 [VERIFIED — surfaced]; tracker in
  `.anneal-dev/runs/`).
