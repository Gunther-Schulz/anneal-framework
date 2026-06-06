#!/usr/bin/env bash
# Build the sanitized pre-fix tree for the real-codebase A/B (beat-the-books replay engine).
# Exports the codebase at the commit BEFORE the period-aware-settlement fix, strips the
# leak vectors (docs/, .clippy/, .git, loose planning/chat .md — they name the fix), keeps
# code only, and makes N copies for parallel review arms.
#
# Usage: build-tree.sh [REPO] [PREFIX_COMMIT] [N] [BASE]
set -euo pipefail
REPO="${1:-/home/g/dev/Gunther-Schulz/beat-the-books}"
PREFIX_COMMIT="${2:-1f62d57d^}"   # parent of Unit-27 period-aware-settlement fix (the buggy state)
N="${3:-5}"
BASE="${4:-/tmp/bt-eval}"

rm -rf "$BASE"; mkdir -p "$BASE/export"
git -C "$REPO" archive "$PREFIX_COMMIT" | tar -x -C "$BASE/export"

# Keep code + build config only; remove docs/.clippy and all loose root files (chat logs,
# planning .md, data dumps) — those leak the fix / known issues.
cd "$BASE/export"; mkdir -p "$BASE/.keep"
for k in src tests alembic config scripts pyproject.toml setup.cfg uv.lock environment.yml alembic.ini; do
  [ -e "$k" ] && mv "$k" "$BASE/.keep/"
done
cd "$BASE" && rm -rf export && mv .keep export

# Leak check — the fix introduced game_scores / "period-aware settlement"; none should remain.
if grep -rliE 'period-aware|period-keyed|game_scores|unit.?27.*settl' export >/dev/null 2>&1; then
  echo "WARNING: possible fix-leak in export — inspect before dispatching arms"; fi

for i in $(seq 1 "$N"); do rm -rf "$BASE/copy_$i"; cp -r "$BASE/export" "$BASE/copy_$i"; done
echo "Built $N code-only copies: $BASE/copy_1..$N ($(du -sh "$BASE/export" | cut -f1))"
echo "Bug + in-code hint present:"; grep -rn 'def derive_outcome_result' "$BASE/export/src" | head -1
echo "NOTE: dispatch <=5 review subagents per batch (10-at-once rate-limits the server)."
