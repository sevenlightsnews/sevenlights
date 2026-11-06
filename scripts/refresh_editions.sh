#!/usr/bin/env bash
# Regenerate the daily editions archive, commit and push only when something
# changed (same pattern as refresh_source_feeds.sh / refresh_traffic_stats.sh).
# Run after a story push; silent no-op otherwise.
set -euo pipefail
cd "$(dirname "$0")/.."

python3 scripts/gen_editions.py

if git diff --quiet -- content/editions && [ -z "$(git ls-files --others --exclude-standard -- content/editions)" ]; then
  echo "editions unchanged — nothing to commit"
  exit 0
fi

git add content/editions
git commit -m "chore: refresh daily editions archive ($(date +%F))"
git push origin main
echo "editions pushed"
