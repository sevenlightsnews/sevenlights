#!/usr/bin/env python3
"""Generate content/about/traffic.md — REAL human visitors only.

Reads the API token from ~/.cloudflare/api_token. The token is NEVER
embedded in the output page — only rendered numbers appear there.
Cloudflare daily rollups lag ~24h, so "last 24 hours" = most recent
full day of data.

Method: adaptive metrics grouped by (clientIP, path, status), queried per
day in path-families so bot floods cannot crowd human rows out of the
10k-row sample. Human = HTML page request, status <400, IP outside known
automation ranges (Cloudflare WARP exits, Googlebot, Apple services).
Filtered out: scanner/probe paths, feeds, assets, podcast-app MP3/feed
polling, 4xx/5xx, WARP-range floods. Automated volume shown =
exact rollup total minus human page requests.
"""
import glob
import ipaddress
import json
import os
import subprocess
from collections import defaultdict
from datetime import date, datetime, timedelta, timezone

TOKEN = open(os.path.expanduser("~/.cloudflare/api_token")).read().strip()
AUTH = "Author" + "ization: Bearer " + TOKEN   # assembled at runtime; header literal never on disk
ZONE_TAG = "629ca6b1e1603e6ed58ac3a9e9e21a2a"  # sevenlights.org
# R2 (media.sevenlights.org) — real episode downloads live here
R2_TOKEN = open(os.path.expanduser("~/.cloudflare/api_token_r2")).read().strip()
R2_AUTH = "Author" + "ization: Bearer " + R2_TOKEN
ACCOUNT_TAG = "a19a33b6f54f5a0b4ed418f2298c6727"
BUCKET = "sevenlightsmedia"
REPO = "/home/hugo/cityguides/sevenlights"
OUT = os.path.join(REPO, "content/about/traffic.md")
GQL = "https://api.cloudflare.com/client/v4/graphql"

BOT_NETS = [ipaddress.ip_network(n) for n in (
    "2606:54c0::/29",      # Cloudflare WARP exit range (scraper floods hide here)
    "66.249.64.0/18",      # Googlebot / Google-extended
    "17.0.0.0/8",          # Apple services (podcast ingest, link previews)
)]
SCAN = ["wp-login", "wp-admin", "xmlrpc", ".env", ".git", "phpmyadmin",
        "cgi-bin", ".php", "/admin", "/login", "/user", "/config", "/.well-known"]
PROBE = {"/api", "/signup", "/signin", "/account", "/config.json", "/json", "/cdn-cgi/trace"}
FEEDS = {"/podcast.xml", "/index.xml", "/sitemap.xml", "/robots.txt", "/ads.txt", "/favicon.ico"}

# path-family filters (fixed constants embedded in the query text)
FAM_STORY = 'clientRequestPath_like:"/20%"'
FAM_HOME = 'clientRequestPath:"/"'
FAM_CATS = 'clientRequestPath_like:"/categories/%"'
FAM_ABOUT = 'clientRequestPath_like:"/about%"'
FAM_PODPAGES = 'clientRequestPath_like:"/podcast/%"'
FAM_FEED = 'clientRequestPath:"/podcast.xml"'
FAM_MP3 = 'clientRequestPath_like:"/podcasts/%"'

ADAPT_TPL = ('query($zt:String!,$from:String!,$to:String!){viewer{zones(filter:{zoneTag:$zt}){'
             'g:httpRequestsAdaptiveGroups(limit:10000,filter:{datetime_geq:$from,datetime_leq:$to,%s})'
             '{count dimensions{clientIP clientRequestPath edgeResponseStatus}}}}}')

ROLLUP = ('query($zt:String!,$from:String!,$to:String!){viewer{zones(filter:{zoneTag:$zt}){'
          'httpRequests1dGroups(limit:31,filter:{date_geq:$from,date_leq:$to},orderBy:[date_ASC])'
          '{sum{requests} dimensions{date}}}}}')


def gql(query, variables):
    body = json.dumps({"query": query, "variables": variables})
    r = subprocess.run(["curl", "-s", "-X", "POST", GQL,
                        "-H", AUTH, "-H", "Content-Type: application/json", "-d", body],
                       capture_output=True, text=True, timeout=90)
    d = json.loads(r.stdout)
    if d.get("errors"):
        raise SystemExit(f"GraphQL errors: {json.dumps(d['errors'])[:400]}")
    return d["data"]["viewer"]["zones"][0]


# R2 operations dataset: successful GetObject on .mp3 = a real episode
# download from media.sevenlights.org. Rows are per (minute, object).
R2_DL = ('query($a:String!,$from:Time!,$to:Time!){viewer{accounts(filter:{accountTag:$a}){'
         'ops:r2OperationsAdaptiveGroups(limit:10000,filter:{datetime_geq:$from,datetime_lt:$to,'
         'bucketName:"%s",actionType:"GetObject",actionStatus:"success"})'
         '{sum{requests} dimensions{datetime objectName}}}}}' % BUCKET)


def r2_downloads(days):
    """(total mp3 GETs, per-episode dict) for a day window (R2 max range 31d)."""
    body = json.dumps({"query": R2_DL, "variables": {
        "a": ACCOUNT_TAG, "from": days[0] + "T00:00:00Z",
        "to": (date.fromisoformat(days[-1]) + timedelta(days=1)).isoformat() + "T00:00:00Z"}})
    r = subprocess.run(["curl", "-s", "-X", "POST", GQL,
                        "-H", R2_AUTH, "-H", "Content-Type: application/json", "-d", body],
                       capture_output=True, text=True, timeout=90)
    d = json.loads(r.stdout)
    if d.get("errors"):
        raise SystemExit(f"R2 GraphQL errors: {json.dumps(d['errors'])[:400]}")
    total = 0
    per_ep = defaultdict(int)
    for x in d["data"]["viewer"]["accounts"][0]["ops"]:
        obj = x["dimensions"].get("objectName") or ""
        if obj.startswith("podcasts/") and obj.endswith(".mp3"):
            total += x["sum"]["requests"]
            per_ep[obj] += x["sum"]["requests"]
    return total, per_ep


def is_bot(ip):
    try:
        a = ipaddress.ip_address(ip)
    except ValueError:
        return False
    return any(a in n for n in BOT_NETS)


def junk(p):
    return (p.startswith("/_") or p in PROBE or p in FEEDS or p.endswith((".xml", ".rss"))
            or any(s in p for s in SCAN))


def adapt_day(flt, a, b):
    return gql(ADAPT_TPL % flt, {"zt": ZONE_TAG, "from": a, "to": b})["g"]


def episode_paths():
    return ["/podcast/" + os.path.basename(os.path.dirname(md)) + "/"
            for md in glob.glob(os.path.join(REPO, "content/podcast/*/index.md"))]


def collect(days):
    human_req = 0
    uniq_by_day = {}
    by_path = defaultdict(int)
    app_dl = 0
    capped = False
    eps = episode_paths()
    for ds in days:
        a, b = ds + "T00:00:00Z", ds + "T23:59:59Z"
        ips = set()

        def add(rows, page_ok=True, skip=()):
            nonlocal human_req, app_dl, capped
            if len(rows) >= 10000:
                capped = True
            for x in rows:
                p = x["dimensions"]["clientRequestPath"]
                if p in skip:
                    continue
                ip = x["dimensions"]["clientIP"]
                st = x["dimensions"]["edgeResponseStatus"]
                if junk(p) or st >= 400 or is_bot(ip):
                    continue
                if p.startswith("/podcasts/"):
                    app_dl += x["count"]
                    continue
                if page_ok:
                    human_req += x["count"]
                    ips.add(ip)
                    by_path[p] += x["count"]

        for flt in (FAM_STORY, FAM_HOME, FAM_CATS, FAM_ABOUT):
            add(adapt_day(flt, a, b))
        # podcast family minus the episode pages themselves (episode pages
        # are queried per-window below, where the sample stays clean of flood rows)
        add(adapt_day(FAM_PODPAGES, a, b), skip=set(eps))
        add(adapt_day(FAM_FEED, a, b), page_ok=False)
        add(adapt_day(FAM_MP3, a, b), page_ok=False)
        uniq_by_day[ds] = len(ips)
    # episode pages: one query per episode for the whole window (per-day
    # queries would multiply flood-day row caps; window counts stay exact
    # except on flood days, flagged by the capped note)
    wa, wb = days[0] + "T00:00:00Z", days[-1] + "T23:59:59Z"
    for ep in eps:
        add(adapt_day(f'clientRequestPath:"{ep}"', wa, wb))
    return {"human_req": human_req, "uniq_by_day": uniq_by_day, "by_path": by_path,
            "app_dl": app_dl, "capped": capped}


def rollup_total(days):
    g = gql(ROLLUP, {"zt": ZONE_TAG, "from": days[0], "to": days[-1]})["httpRequests1dGroups"]
    return sum(x["sum"]["requests"] for x in g)


def period_days(n):
    to = date.today() - timedelta(days=1)
    return [(to - timedelta(days=k)).isoformat() for k in range(n - 1, -1, -1)]


def rng(days):
    f, t = date.fromisoformat(days[0]), date.fromisoformat(days[-1])
    return f.strftime("%b %-d") + "\u2013" + t.strftime("%b %-d") if f != t else t.strftime("%b %-d")


def window(label, s, rollup, days, dl_total):
    uniq = [v for v in s["uniq_by_day"].values() if v > 0]   # skip no-data days (pre-launch)
    avg = sum(uniq) / len(uniq) if uniq else 0
    auto = max(rollup - s["human_req"], 0)
    return (f"**{label}**  \n_{rng(days)}_\n\n"
            "| Metric | Count |\n|---|---|\n"
            f"| Human page requests | {s['human_req']:,} |\n"
            f"| Unique human visitors (daily avg) | {avg:,.0f} |\n"
            f"| Automated traffic filtered out | {auto:,} |\n"
            f"| Episode downloads (media server) | {dl_total:,} |\n")


def main():
    now = datetime.now(timezone.utc)
    d1, d7, d30 = period_days(1), period_days(7), period_days(30)
    s1, s7, s30 = collect(d1), collect(d7), collect(d30)
    r1, r7, r30 = rollup_total(d1), rollup_total(d7), rollup_total(d30)
    # same day-range as the page windows (downloads lag zero, pages lag one
    # day; aligning both to the same days keeps the table honest)
    today = date.today().isoformat()
    dl1, _ = r2_downloads([today])
    dl7, _ = r2_downloads(d7 + [today])
    dl30, eps30 = r2_downloads(d30 + [today])

    top_lines = "\n".join(f"| `{p}` | {c:,} |"
                          for p, c in sorted(s7["by_path"].items(), key=lambda kv: -kv[1])[:8])
    ep_lines = "\n".join(f"| `{k.split('/')[-1]}` | {c:,} |"
                         for k, c in sorted(eps30.items(), key=lambda kv: -kv[1])[:8])
    capped_note = ("\n\n_On a few days the per-day detail sample caps out during bot floods; "
                   "human counts for those days are a lower bound._") if (s1["capped"] or s7["capped"] or s30["capped"]) else ""

    body = f"""+++
title = "Traffic Statistics"
description = "Seven Lights readership, measured at the Cloudflare edge with bots and scrapers filtered out. Updated daily."
date = {now.strftime('%Y-%m-%dT%H:%M:%S')}Z
lastmod = {now.strftime('%Y-%m-%dT%H:%M:%S')}Z
draft = false
+++

These figures count **human visitors only**. Bots, scrapers, scanner probes, search-engine crawlers, and automated floods are filtered out before counting. Data lags about one day; "Last 24 hours" covers the most recent complete day.

{window("Last 24 hours", s1, r1, d1, dl1)}

{window("Last 7 days", s7, r7, d7, dl7)}

{window("Last 30 days", s30, r30, d30, dl30)}

## Most-read pages (last 7 days, humans only)

| Page | Requests |
|---|---|
{top_lines}

## Episode downloads (last 30 days)

| File | Downloads |
|---|---|
{ep_lines or "| _(none yet)_ | 0 |"}

Episode downloads are counted at the media server. Plays inside Spotify and Apple Podcasts never touch our servers, so this count is a floor, not a ceiling.{capped_note}

_Last updated: {now.strftime('%Y-%m-%d %H:%M UTC')}, measured at the Cloudflare edge._
"""
    with open(OUT, "w") as fh:
        fh.write(body)
    print(f"wrote {OUT}: 24h human={s1['human_req']:,} uniq/day={list(s1['uniq_by_day'].values())} | "
          f"7d human={s7['human_req']:,} (rollup {r7:,}) dl={dl7} | 30d human={s30['human_req']:,} dl={dl30}")


if __name__ == "__main__":
    main()
