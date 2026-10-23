#!/usr/bin/env bash
# Daily traffic-stats refresh: regenerate page, commit, push (Cloudflare Pages auto-deploys).
# Silent on success (cron delivers stdout only on failure).
set -u
cd /home/hugo/cityguides/sevenlights || { echo "traffic-refresh: cd failed"; exit 1; }

if ! python3 scripts/gen_traffic_stats.py > /dev/null; then
    echo "traffic-refresh: gen_traffic_stats.py failed"
    exit 1
fi

if git diff --quiet -- content/about/traffic.md; then
    exit 0   # nothing changed
fi

git add content/about/traffic.md
git commit -q -m "chore: daily traffic stats refresh $(date -u +%F)" || { echo "traffic-refresh: commit failed"; exit 1; }
git push -q origin main || { echo "traffic-refresh: push failed"; exit 1; }
exit 0
