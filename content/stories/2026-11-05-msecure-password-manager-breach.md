+++
title = "Password manager mSecure orders resets without explaining the breach"
date = 2026-11-05T03:50:00-05:00
lastmod = 2026-11-05T03:50:00-05:00
draft = false
slug = "msecure-password-manager-breach"
summary = "mSeven Software told current and former mSecure customers to change passwords, reset two-factor authentication and remove passkeys after 'suspicious activity', reportedly an encrypted customer database theft. The company has not said what was taken."
description = "Security outlets reported a hacker stole an encrypted customer database. mSecure's November 3 notice gave no account of what happened, when, or whether data was accessed."
author = "Seven Lights"
categories = ["Technology"]
tags = ["cybersecurity", "password manager", "msecure", "data breach"]
image = "/images/stories/msecure-password-manager-breach.webp"
image_alt = "Close-up of a steel padlock hasp on a dark server cabinet door, shallow depth of field, single work light, no text or labels visible"
refs = 3
+++

![Close-up of a steel padlock hasp on a dark server cabinet door, shallow depth of field, single work light, no text or labels visible](/images/stories/msecure-password-manager-breach.webp)

mSeven Software warned current and former customers of its mSecure password manager on November 3 to change passwords, reset two-factor authentication and remove passkeys, after what the company described as suspicious activity involving the application. Security outlets reported that a hacker stole an encrypted customer database.

"mSeven Software recently learned of suspicious activity associated with the mSecure password management application," the company's security notification said. The notice, shared with BleepingComputer, advised customers to change the master passwords on their vaults, re-enrol in two-factor authentication and delete stored passkeys.

The company gave no account of what happened, when the activity was detected, or whether customer data had been accessed. BleepingComputer reported that a hacker reportedly stole an encrypted customer database. The Register, which said it saw the November 3 email, reported that customers were left wondering what had been compromised, and that mSeven, a US-based developer, had opened an investigation after finding something amiss.

The silence matters more for a password manager than for an ordinary application. A vault holds the keys to the accounts it protects, and a theft of vault credentials cannot be undone by patching a server. mSeven's own security documentation says mSecure uses AES-256 encryption and a zero-knowledge architecture, with data encrypted on users' devices before transmission, and that the company cannot access customers' decrypted vault contents. Customers who reuse passwords across services face exposure well beyond mSecure itself, and the advice to remove passkeys, which cannot be intercepted in the way a one-time code can, signals concern about account takeover rather than mere spam.

Practitioners have long advised users of any password manager to keep unique passwords per account, maintain an offline copy of the vault, and treat unexplained reset demands from a provider as a reason for immediate action.

mSecure said its investigation continues. Until the company discloses the scope of the activity, customers cannot judge whether the stolen database, if confirmed, contained vault contents or account metadata alone.

## Sources

- [BleepingComputer](https://www.bleepingcomputer.com/news/security/msecure-password-manager-hack-prompts-password-reset-warnings/)
- [The Register](https://www.theregister.com/security/2026/11/03/password-manager-msecure-tells-users-to-change-passwords-wont-say-why/5307296)
- [TechRadar](https://www.techradar.com/pro/security/top-password-manager-msecure-tells-users-to-change-passwords-immediately)
