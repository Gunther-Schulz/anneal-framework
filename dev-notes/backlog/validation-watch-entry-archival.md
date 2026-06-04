# Validation-watch entry archival — physically retire RESOLVED entries to bound file length

**Status:** OPEN — framework hygiene idea, operator-raised 2026-06-04 ("the V-file has gotten long; do
we have a mechanism to retire items once proven working?"). **Not urgent** (see data below) but real;
filed per no-silent-deferral. Mostly a dev-notes convention + preamble edit, lightly spec-wired.

## The gap
`dev-notes/validation-watch.md` has **logical** retirement but no **physical** retirement:
- **Logical (exists):** the `RESOLVED` status. A `FIX-SHIPPED` entry → `RESOLVED` on the first
  load-bearing instance; once `RESOLVED` it is dormant and Q7 (`post-run-review.md`) skips it.
- **Physical (missing):** `RESOLVED`/`INVALIDATED` entries stay **inline forever**. No `archive/`
  equivalent (the backlog has one — `backlog/archive/`). The file only grows.

## Why it's not urgent yet (but is real)
Status distribution 2026-06-04: **23 WATCHING + 4 FIX-SHIPPED + 1 RESOLVED** (28 entries, 1552 lines).
So ~27 of 28 are *genuinely active* — the current length is real watching, not un-retired cruft; only
1 entry is archival-eligible today. The length is **mostly legitimate**, so this is future-proofing,
not a cleanup backlog.

**Where it bites regardless:** Q7 loads + walks the **whole** file on **every** post-run-review, on
**every** instance (clippy/daneel/anneal-dev — each renders its own `post-run-review.md` Q7 pointing at
the one shared file). So file length is a recurring **context + walk tax** paid on every review across
every instance, scaling with the file — independent of how many entries are still live. Archival caps
that tax at the active set.

## Hard constraint — V-N numbers are stable spec-cited references
`V-5`, `V-9`, `V-21` are cited **by number** inside `development-process.md` (V-21 cadence),
`spec/glossary.md`, and clippy/daneel rendered rules (V-5/V-9 in their `investigate-design.md` +
`SKILL.md`). The number is a permanent reference — **cannot renumber or delete it**, only relocate the
body. (basis: `grep -rhoE 'V-[0-9]+' spec/ development-process.md ../coding-clippy/plugin ../daneel/plugin`
→ V-5, V-9, V-21.)

## Proposed shape (mirror backlog `archive/`)
On `RESOLVED` (or a superseded `INVALIDATED`): move the entry **body** to `dev-notes/validation-watch-archive.md`
(or an `## Archived` tail section), leaving a **one-line numbered stub** in the live file —
`V-N RESOLVED <date>, <commit> — see archive`. Live file = active watches (WATCHING/FIX-SHIPPED) +
stubs; archive = resolved bodies. Citations still resolve (number stays in the live file as a stub).
Touch points: the preamble **Entry lifecycle** (document the archival step); confirm Q7 treats a stub as
skip (already `RESOLVED` = skip, so no logic change); check the `spec/glossary.md` lifecycle description
doesn't need a note (the 4 statuses are unchanged — archival is relocation, not a new status).

Secondary length driver (note, not the primary fix): per-entry **verbosity** (~40-50 ln each:
Decision / Why-uncertain / Production-signal / practice-8 justification / n=1 seeds). Active entries
need their detail; archival is the cleaner lever than compressing live entries.

## Level
Mostly a **dev-notes convention** (the archival act + the preamble documenting it). Lightly spec-wired
(the lifecycle is described in `spec/glossary.md` + consumed by `post-run-review.md` Q7) → a **light
anneal-dev cycle** if any spec/render text changes, else a dev-process-convention add.

## Relates to
- `backlog/README.md` Convention — the `archive/` model this borrows.
- `development-process.md` validation-watch governance + practice 8 (when a V-N is legitimate).
- `spec/glossary.md` (Validation-watch lifecycle definition) + `post-run-review.md` Q7 (the consumer).
- `kernel-consolidation-glossary-hygiene` — sibling corpus-hygiene cluster, but distinct (that is
  glossary/triage homes; this is validation-watch file growth).
