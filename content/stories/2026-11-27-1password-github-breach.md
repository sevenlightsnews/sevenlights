+++
title = "1Password Discloses Breach of Customer Data and Source Code"
date = 2026-11-27T03:00:00-05:00
lastmod = 2026-11-27T03:00:00-05:00
draft = false
slug = "1password-github-breach"
summary = "The password manager 1Password said Wednesday that a hacker used a compromised employee GitHub account to steal customer records and private source code, though customer vaults were not touched."
description = "The attacker injected malicious code into backend services and took account metadata, authentication parameters and invitation tokens. The company says vault contents and encryption keys were not compromised."
author = "Seven Lights"
categories = ["Technology"]
tags = ["1password", "data breach", "github", "cybersecurity", "source code"]
image = "/images/stories/1password-github-breach.webp"
image_alt = "Dark data-center corridor with rows of server racks, scattered green and amber indicator lights, an open padlock hanging from a cable tray in the foreground, cool blue light, long shadows, ominous quiet mood, editorial photojournalism, no people, no readable text, 3:2"
refs = 3
+++

![Dark data-center corridor with rows of server racks, scattered green and amber indicator lights, an open padlock hanging from a cable tray in the foreground, cool blue light, long shadows, ominous quiet mood, editorial photojournalism, no people, no readable text, 3:2](/images/stories/1password-github-breach.webp)

1Password disclosed on Wednesday that a hacker stole customer information and proprietary source code by way of a compromised employee GitHub account, and said the intrusion did not reach the encrypted vaults its customers pay it to protect.

The company opened an investigation on November 19 after detecting indications that an employee's corporate GitHub account had been compromised. The attacker used the account to reach private source code repositories and to inject malicious code into backend services that downloaded customer account records, 1Password said in a security incident disclosure.

The stolen records include customer names and email addresses, account and user identifiers, timestamps showing when accounts were created and last signed into, public cryptographic keys, parameters of the Secure Remote Password authentication protocol, invitation, provisioning and recovery tokens, and other non-secret account metadata. The authentication parameters cannot be used directly to sign in, the company said; brute-forcing account passwords would require the associated Secret Keys, which 1Password does not store.

"At no time were customer vault contents accessed by, or available to, the attacker," 1Password said. A company representative added that there is no evidence that encrypted vaults were downloaded or accessed. Client applications, browser extensions and account recovery keys were not affected.

The stolen tokens, embedded in emails that guide users through account invitations or recovery, cannot grant access on their own, because completing either process also requires single sign-on authentication or a verification code sent to the registered email address. A small number of people whose provisioning or recovery was under way during the intrusion have been notified individually. The company found no evidence of account takeovers, but strengthened the verification codes from six numeric digits to ten alphanumeric characters as a precaution against brute-force attacks.

1Password said it disabled the compromised GitHub account, revoked a stolen token, rotated or replaced potentially exposed infrastructure credentials, and restored clean versions of the affected services. The intruder also reached the company's continuous integration and continuous delivery infrastructure, which houses credentials that keep its products running. 1Password has not detailed the extent of that access, how the GitHub account permitted it, or how many customers were affected.

Customers need take no action, the company said, but were advised to watch for phishing attacks that exploit news of the incident. Independent cybersecurity experts are assisting the investigation, which continues.

The episode recalls the first stage of LastPass's 2022 breach, in which an attacker compromised that company's development environment and stole source code; information from that intrusion helped enable a second attack that exposed customer vault backups. Britain's information regulator fined LastPass 1.2 million pounds last December.

## Sources

- [SecurityWeek](https://www.securityweek.com/1password-breach-exposes-customer-data-internal-source-code/)
- [BleepingComputer](https://www.bleepingcomputer.com/news/security/1password-customer-data-stolen-after-employee-github-account-breach/)
- [The Register](https://www.theregister.com/security/2026/11/26/hackers-help-themselves-to-1passwords-source-code-and-customer-data/5312317)
