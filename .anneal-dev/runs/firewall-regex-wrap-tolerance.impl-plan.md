# firewall-regex-wrap-tolerance — impl plan

**1 dispatch unit** (multi-file, sequential). Disjointness basis: sole unit — runs in place under the
Integrity check. Touched containers: this repo only.

## Unit 1 — the regex fix + the render-debt note (D1, D2)
- **Dependencies:** first (sole unit). **Parallelism:** sequential.
- **Files:** `instantiation-guide.md` (D1), `dev-notes/backlog/instance-reinstantiation.md` (D2).
- **D1 — `instantiation-guide.md:189`:** replace `rg '(core|modules)\.md[^\n]{0,4}§' <instance>` with
  `rg -U '(core|modules)\.md[^A-Za-z0-9]{0,12}§' <instance>` and add a brief inline clause that the check is
  **wrap-tolerant** — multiline `-U`; the gap is non-alphanumeric (whitespace / newline / backtick / punctuation,
  up to 12 chars), so a §-cite split across a line wrap is caught while prose between `.md` and `§` is not a false
  positive (words break the gap) — matching the basis-rule wrap-tolerant idiom (`glossary.md` Completeness claim /
  `core.md` §3.2). Keep the surrounding sentence (187-191) coherent (Integrate-don't-insert; ~1 added clause).
- **D2 — `dev-notes/backlog/instance-reinstantiation.md` render-debt queue (the section at `:24+`):** add a
  source-delta entry noting the firewall-regex SOURCE FIX (instantiation-guide.md:189 → wrap-tolerant
  `rg -U ...[^A-Za-z0-9]{0,12}§`) so the batch re-render propagates the wrap-tolerant regex into every instance's
  rendered firewall check (clippy/daneel render-verify). Match the queue's existing source-delta entry format;
  note it as the discharge of the already-filed `firewall-regex-wrap-tolerance` tail (the item is referenced at ~:294).
- **Briefing:** load anneal-dev foundations/tracker/implement; **invoke skill-craft via the Skill tool BEFORE
  editing `instantiation-guide.md`** (pre-edit gate fires on it — SPEC_SOURCE). Write-time self-check (Lossy-render —
  the regex renders verbatim into instances, confirm it's a literal command not a paraphrase; Missed-dependents —
  the only in-repo home is instantiation-guide.md:189, the render-debt covers instances; Undefined-shorthand;
  Over-claimed) + change-set-vs-scope. Do NOT commit.
