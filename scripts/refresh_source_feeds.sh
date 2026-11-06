#!/usr/bin/env bash
# Regenerate the source-feeds transparency page from the live feed pool,
# commit, push (Cloudflare Pages auto-deploys). Silent when unchanged.
set -u
cd /home/hugo/cityguides/sevenlights || { echo "source-feeds-refresh: cd failed"; exit 1; }

if ! python3 scripts/gen_source_feeds.py > /dev/null; then
    echo "source-feeds-refresh: gen_source_feeds.py failed"
    exit 1
fi

if git diff --quiet -- content/about/source-feeds.md; then
    exit 0   # nothing changed
fi

git add content/about/source-feeds.md
git commit -q -m "chore: refresh source-feeds page $(date -u +%F)" || { echo "source-feeds-refresh: commit failed"; exit 1; }
git push -q origin main || { echo "source-feeds-refresh: push failed"; exit 1; }
exit 0
