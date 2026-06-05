# vendor/ — provenance

Copied verbatim from Anthropic's `skill-creator` (the `anthropics/skills` repo),
used as the execution/aggregation runner. Not anneal-authored.

| File | Source (in `anthropics/skills`) |
|---|---|
| `aggregate_benchmark.py` | `skills/skill-creator/scripts/aggregate_benchmark.py` |
| `schemas.md` | `skills/skill-creator/references/schemas.md` |

Local clone: `~/dev/reference/skills` (shallow). Re-vendor by re-copying from
there. We reuse the aggregation + the `grading.json` / `timing.json` /
`benchmark.json` schemas as-is; everything else under `eval/` is anneal-authored.
