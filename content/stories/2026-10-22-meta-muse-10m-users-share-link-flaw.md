+++
title = "Meta Says Its Muse AI App Has Over 10 Million Users as It Pauses Share-Link Feature"
date = 2026-10-22T06:18:00-04:00
lastmod = 2026-10-22T09:21:00-04:00
draft = false
slug = "meta-muse-10m-users-share-link-flaw"
summary = "Meta said during its Q3 earnings call that its Muse AI app has over 10 million users, with shopping a top activity; it has paused the app's conversation share-link feature after researchers enumerated thousands of discoverable links."
description = "Meta says its Muse AI app has passed 10 million users, with shopping a top activity, per its Q3 earnings call, as it pauses a conversation share-link feature after security firm Claroc enumerated 6,800 publicly discoverable links via passive DNS searches."
author = "Seven Lights"
categories = ["AI"]
tags = ["meta", "ai-apps", "privacy", "security", "techcrunch", "q3-earnings"]
image = "https://techcrunch.com/wp-content/uploads/2026/09/meta-muse-finger-on-app-GettyImages-2293791808.jpg?w=1024"
image_alt = "A close-up of a human finger pressing the Muse app icon inside a folder containing Meta apps on a smartphone screen"
+++

![A close-up of a human finger pressing the Muse app icon inside a folder containing Meta apps on a smartphone screen](https://techcrunch.com/wp-content/uploads/2026/09/meta-muse-finger-on-app-GettyImages-2293791808.jpg?w=1024)

*Image: TechCrunch.*

Update (Oct. 22, 2026): In a further report on the same story, TechCrunch said Meta told investors on its Q3 earnings call that the AI app now has over 10 million users and that users are adopting Muse for shopping and personal productivity.

Meta said its Muse AI app now has more than 10 million users and that users are adopting it for shopping and personal productivity, the company said during its Q3 earnings call, TechCrunch reported.

The disclosure came as Meta paused the feature that lets users create share links for Muse conversations, after researchers at security firm Claroc enumerated 6,800 such links using passive DNS searches and, after opening a few hundred, found information that was not intended to be publicly available, Ars Technica reported. Wired, carrying the Ars Technica report, said all Muse share links use the domain cf.metaaiusercontent.com with the conversation title placed in the subdomain rather than the URL path, which public DNS records make searchable; Claroc called the pages “GhostShares.”

Examples the researchers said they found included a candidate’s notes preparing for a confidential executive-search call with a frontier AI lab, a marketing company’s internal revenue review marked for its CEO, a small-business owner’s loan application, and a to-do list containing a bank fraud alert with a partial account number, according to Ars Technica. Claroc co-founder and CTO Asaf Aprozper said he reported the findings through Meta’s bug bounty program on Oct. 8, Ars reported; Meta said it had “paused this functionality while we review this report and consider changes to how these links can be discovered.”

The share-link episode follows a zero-day vulnerability found three weeks after Muse’s launch by macOS security expert Patrick Wardle, which Ars Technica reported would have let other apps on the same device take control of a user’s Muse account.

## Sources

- [TechCrunch](https://techcrunch.com/2026/10/21/meta-says-muse-has-over-10m-users-with-shopping-a-top-activity/)
- [Wired](https://www.wired.com/story/a-design-flaw-in-share-links-exposes-users-personal-conversations-with-meta-muse/)
- [Ars Technica](https://arstechnica.com/security/2026/10/meta-muse-exposes-users-personal-and-business-secrets-when-they-share-conversations/)
