#!/usr/bin/env python3
"""Generate content/about/source-feeds.md from the live RSS_FEEDS pool in
~/.hermes/scripts/news_digest_core.py. Transparency page: lists every feed the
daily pipeline scans. Run via scripts/refresh_source_feeds.sh (same pattern as
gen_traffic_stats.py / refresh_traffic_stats.sh)."""
import datetime
import importlib.util
import sys
from urllib.parse import urlparse

CORE = "/home/hugo/.hermes/scripts/news_digest_core.py"
OUT = "/home/hugo/cityguides/sevenlights/content/about/source-feeds.md"

# Pipeline category key -> (site section label, order)
SECTIONS = [
    ("global", "World"),
    ("us", "US"),
    ("politics", "Politics"),
    ("business", "Business"),
    ("tech", "Technology"),
    ("ai", "Artificial Intelligence"),
    ("sports", "Sports"),
    ("pop_culture", "Entertainment"),
    ("health", "Health"),
]

def main():
    spec = importlib.util.spec_from_file_location("ndc", CORE)
    ndc = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(ndc)
    feeds = ndc.RSS_FEEDS

    now = datetime.datetime.now(datetime.timezone.utc)
    stamp = now.strftime("%Y-%m-%dT%H:%M:%SZ")

    total = 0
    domains = set()
    lines = []
    lines.append("+++")
    lines.append('title = "Source Feeds"')
    lines.append('description = "The complete list of public RSS feeds this site reads each day to find stories."')
    lines.append(f"date = {stamp}")
    lines.append(f"lastmod = {stamp}")
    lines.append("draft = false")
    lines.append("+++")
    lines.append("")
    lines.append(
        "Seven Lights finds its stories by reading the public RSS feeds of the news "
        "organizations listed on this page. Nothing else is scanned: no social media, "
        "no press releases, no anonymous sites. The list below is generated directly "
        "from the live configuration the publishing software uses, so it always shows "
        "exactly what the site reads."
    )
    lines.append("")
    lines.append("Three points a reader should know:")
    lines.append("")
    lines.append(
        "- Appearing on this list is not an endorsement. The feeds are read for facts, "
        "and every published summary links back to the original articles so a reader "
        "can check the reporting behind each claim."
    )
    lines.append(
        "- A feed is only where a story starts. A story is published here only when at "
        "least three separate articles from at least three different media companies "
        "report it, as stated on the [About page](/about/). One outlet's story, however "
        "well written, does not run."
    )
    lines.append(
        "- The list changes over time. Feeds are added when they carry reliable, "
        "accessible reporting, and removed when they stop updating or block automated "
        "reading. Removed candidates are tested before they are ever added."
    )
    lines.append("")

    for key, label in SECTIONS:
        entries = feeds.get(key, [])
        seen = set()
        rows = []
        for url, name, _cat in entries:
            u = url.strip()
            if u in seen:
                continue
            seen.add(u)
            rows.append((name, u))
            domains.add(urlparse(u).netloc.lower().removeprefix("www."))
        total += len(rows)
        lines.append(f"## {label} ({len(rows)} feeds)")
        lines.append("")
        for name, u in sorted(rows, key=lambda r: r[0].lower()):
            lines.append(f"- **{name}** — {u}")
        lines.append("")

    lines.append(
        f"*{total} feeds from {len(domains)} distinct publishers across "
        f"{len(SECTIONS)} sections. This page is regenerated from the live feed "
        f"configuration; it was last generated on {now.strftime('%B %-d, %Y')}.*"
    )
    lines.append("")

    with open(OUT, "w") as f:
        f.write("\n".join(lines))
    print(f"wrote {OUT}: {total} feeds, {len(domains)} publishers")

if __name__ == "__main__":
    main()
