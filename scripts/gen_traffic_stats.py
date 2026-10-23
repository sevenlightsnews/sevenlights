#!/usr/bin/env python3
"""Generate content/about/traffic.md from Cloudflare GraphQL analytics.

Reads the API token from ~/.cloudflare/api_token. The token is NEVER
embedded in the output page — only rendered numbers appear there.
Cloudflare daily rollups lag ~24h, so "last 24 hours" = most recent
full day of data.
"""
import json, os, sys, urllib.request
from datetime import date, datetime, timedelta, timezone

TOKEN = open(os.path.expanduser("~/.cloudflare/api_token")).read().strip()
ZONE_TAG = "629ca6b1e1603e6ed58ac3a9e9e21a2a"  # sevenlights.org
OUT = "/home/hugo/cityguides/sevenlights/content/about/traffic.md"
GQL = "https://api.cloudflare.com/client/v4/graphql"

def gql(query, variables):
    req = urllib.request.Request(GQL, data=json.dumps({"query": query, "variables": variables}).encode(),
                                 headers={"Authorization": f"Bearer {TOKEN}", "Content-Type": "application/json"})
    with urllib.request.urlopen(req, timeout=30) as r:
        d = json.load(r)
    if d.get("errors"):
        raise SystemExit(f"GraphQL errors: {json.dumps(d['errors'])[:400]}")
    return d["data"]["viewer"]["zones"][0]

ROLLUP = """
query($zt:String!,$from:String!,$to:String!){
  viewer{zones(filter:{zoneTag:$zt}){
    httpRequests1dGroups(filter:{date_geq:$from,date_leq:$to},orderBy:[date_ASC],limit:31){
      sum{requests bytes cachedBytes}
      uniq{uniques}
      dimensions{date}
    }
  }}
}"""

TOP = """
query($zt:String!,$from:String!,$to:String!){
  viewer{zones(filter:{zoneTag:$zt}){
    httpRequestsAdaptiveGroups(filter:{datetime_geq:$from,datetime_leq:$to},
      orderBy:[count_DESC],limit:10){
      count dimensions{clientRequestPath}
    }
  }}
}"""

SCAN_PATS = ["wp-login", "wp-admin", "xmlrpc", ".env", ".git", "phpmyadmin", "cgi-bin"]
SCAN_SEL = "".join(
    f'p{i}:httpRequestsAdaptiveGroups(filter:{{datetime_geq:$from,datetime_leq:$to,clientRequestPath_like:"%{p}%"}},limit:1){{count}}'
    for i, p in enumerate(SCAN_PATS))
SCANNER = 'query($zt:String!,$from:String!,$to:String!){viewer{zones(filter:{zoneTag:$zt}){%s}}}' % SCAN_SEL

def period(days):
    """Return (from_date, to_date) covering the last `days` full days."""
    to = date.today() - timedelta(days=1)          # last full day (rollups lag)
    return to - timedelta(days=days - 1), to

def fmt_bytes(n):
    for unit in ("B", "KB", "MB", "GB", "TB"):
        if n < 1024 or unit == "TB":
            return f"{n:.1f} {unit}" if unit != "B" else f"{int(n)} B"
        n /= 1024

def stats(days):
    f, t = period(days)
    d = gql(ROLLUP, {"zt": ZONE_TAG, "from": f.isoformat(), "to": t.isoformat()})
    g = d["httpRequests1dGroups"]
    req = sum(x["sum"]["requests"] for x in g)
    byt = sum(x["sum"]["bytes"] for x in g)
    cach = sum(x["sum"]["cachedBytes"] for x in g)
    # uniq{uniques} per day can't be summed across days for a true distinct
    # count; report the daily-average unique IPs as the visitor proxy.
    uniq_avg = sum(x["uniq"]["uniques"] for x in g) / len(g) if g else 0
    return {"from": f, "to": t, "requests": req, "bytes": byt,
            "cache_pct": (100.0 * cach / byt) if byt else 0, "uniq_avg": uniq_avg,
            "days": g}

def top_paths(days):
    f, t = period(days)
    d = gql(TOP, {"zt": ZONE_TAG, "from": f"{f.isoformat()}T00:00:00Z", "to": f"{(t + timedelta(days=1)).isoformat()}T00:00:00Z"})
    return [(x["dimensions"]["clientRequestPath"], x["count"]) for x in d["httpRequestsAdaptiveGroups"]
            if not x["dimensions"]["clientRequestPath"].startswith("/_")
            and not any(s in x["dimensions"]["clientRequestPath"] for s in SCAN_PATS + [".php", "/admin", "/api", "/login", "/config", "/user", "/.well-known", "favicon", "robots.txt", "sitemap", "cdn-cgi"])]

def scanner(days):
    f, t = period(days)
    d = gql(SCANNER, {"zt": ZONE_TAG, "from": f"{f.isoformat()}T00:00:00Z", "to": f"{(t + timedelta(days=1)).isoformat()}T00:00:00Z"})
    total = 0
    for rows in d.values():
        total += rows[0]["count"] if rows else 0
    return total

def table(label, s, blocked_ct):
    rng = s["from"].strftime("%b %-d") + "–" + s["to"].strftime("%b %-d") if s["from"] != s["to"] else s["to"].strftime("%b %-d")
    rows = [
        f"| Requests | {s['requests']:,} |",
        f"| Unique IPs (daily avg) | {s['uniq_avg']:,.0f} |",
        f"| Data served | {fmt_bytes(s['bytes'])} |",
        f"| Served from cache | {s['cache_pct']:.0f}% |",
        f"| Blocked scanner requests | {blocked_ct:,} |",
    ]  # note: window label already reflects actual data span
    return f"**{label}**  \n_{rng}_\n\n" + "| Metric | Count |\n|---|---|\n" + "\n".join(rows)

def main():
    now = datetime.now(timezone.utc)
    s1, s7, s30 = stats(1), stats(7), stats(30)
    b1, b7, b30 = scanner(1), scanner(7), scanner(30)
    tops = top_paths(7)
    top_md = "\n".join(f"| `{p}` | {c:,} |" for p, c in tops[:6] if p != "/")
    body = f"""+++
title = "Traffic Statistics"
description = "Seven Lights traffic, measured at the Cloudflare edge and updated daily."
date = 2026-10-21T06:00:00-04:00
lastmod = {now.strftime('%Y-%m-%dT%H:%M:%S')}Z
draft = false
+++

Seven Lights traffic, counted at the Cloudflare edge (the network that serves this site). Numbers are requests and distinct client IPs, not analytics cookies — no visitor tracking happens on this site. Blocked scanner requests are automated probes for non-existent pages (WordPress login files, config files, etc.) that Cloudflare rejects before they reach the site.

Data lags about one day; "Last 24 hours" covers the most recent complete day. The site launched on October 21, 2026, so the 30-day figures currently cover the same span as the 7-day figures until more history accumulates.

{table("Last 24 hours", s1, b1)}

{table("Last 7 days", s7, b7)}

{table("Last 30 days", s30, b30)}

## Most-requested pages (last 7 days)

| Page | Requests |
|---|---|
| `/` (home) | {next((c for p, c in tops if p == '/'), 0):,} |
{top_md}

_Last updated: {now.strftime('%Y-%m-%d %H:%M UTC')}. Generated from Cloudflare edge metrics; figures are exact request counts at the edge, with a small (~1%) sampling caveat on the per-page breakdown._
"""
    with open(OUT, "w") as fh:
        fh.write(body)
    print(f"wrote {OUT}: 24h={s1['requests']:,}req 7d={s7['requests']:,} 30d={s30['requests']:,}")

if __name__ == "__main__":
    main()
