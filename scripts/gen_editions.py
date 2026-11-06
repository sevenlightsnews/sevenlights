#!/usr/bin/env python3
"""Generate the daily editions archive for sevenlights.org.

Scans content/stories/*.md (filename date prefix YYYY-MM-DD-) and ensures a
page bundle exists at content/editions/<date>/index.md for every publication
day. Idempotent: existing edition pages are left untouched.

content/editions/ is generated output — never hand-edit edition pages
(same rule as content/about/traffic.md and content/about/source-feeds.md).
Rendering lives in layouts/editions/single.html; this script only fixes the
day's existence, title, and date.
"""
import glob
import os
import re
import sys
from datetime import datetime

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
STORIES = os.path.join(REPO, "content", "stories")
EDITIONS = os.path.join(REPO, "content", "editions")

DATE_RE = re.compile(r"^(\d{4}-\d{2}-\d{2})-")


def main() -> int:
    dates = set()
    for path in glob.glob(os.path.join(STORIES, "*.md")):
        m = DATE_RE.match(os.path.basename(path))
        if m:
            dates.add(m.group(1))

    created = 0
    for d in sorted(dates):
        day = datetime.strptime(d, "%Y-%m-%d")
        title = f"Edition of {day.strftime('%B')} {day.day}, {day.year}"
        ed_dir = os.path.join(EDITIONS, d)
        ed_file = os.path.join(ed_dir, "index.md")
        if os.path.exists(ed_file):
            continue
        os.makedirs(ed_dir, exist_ok=True)
        # 06:00 ET = the pipeline's publish time; keeps the edition sorted
        # with its day regardless of individual story timestamps.
        # ET: DST runs Mar-Nov (approx); editions only need stable ordering.
        offset = "-04:00" if 3 <= day.month <= 11 else "-05:00"
        with open(ed_file, "w") as f:
            f.write(
                "+++\n"
                f'title = "{title}"\n'
                f"date = {d}T06:00:00{offset}\n"
                "+++\n"
            )
        created += 1
        print(f"created {os.path.relpath(ed_file, REPO)}")

    print(f"editions: {len(dates)} days, {created} new")
    return 0


if __name__ == "__main__":
    sys.exit(main())
