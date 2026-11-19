+++
title = "Malicious Releases of Microsoft's Agent Framework Poisoned With Credential Stealer"
date = 2026-11-19T03:45:00-05:00
lastmod = 2026-11-19T03:45:00-05:00
draft = false
slug = "microsoft-agent-framework-releases-poisoned"
summary = "Attackers published two booby-trapped versions of Microsoft's agent-framework Python package on PyPI, stealing cloud and CI/CD credentials from anyone who installed them."
description = "Versions 1.26.1 and 1.26.2 ran at every Python start, harvesting Azure, Azure DevOps and GitHub Actions secrets; researchers independently analysed the malware."
author = "Seven Lights"
categories = ["Technology"]
tags = ["supply chain attack", "pypi", "microsoft", "malware", "azure"]
image = "/images/stories/microsoft-agent-framework-releases-poisoned.webp"
image_alt = "Editorial illustration, plain shipping crates on a conveyor belt in a warehouse at night, one crate cracked open with dark tendrils spilling out, cool industrial lighting, metaphor for compromised software supply chain, no text or letters, 3:2"
refs = 3
+++

![Editorial illustration, plain shipping crates on a conveyor belt in a warehouse at night, one crate cracked open with dark tendrils spilling out, cool industrial lighting, metaphor for compromised software supply chain, no text or letters, 3:2](/images/stories/microsoft-agent-framework-releases-poisoned.webp)

Hackers published two malicious versions of Microsoft's Agent Framework Python package on the Python Package Repository on November 17, in a supply-chain attack that could have exposed cloud and continuous-integration credentials belonging to everyone who installed them.

The affected package, agent-framework, is Microsoft's supported library for building artificial-intelligence agents and multi-agent applications, and draws roughly 190,000 downloads a month. The malicious releases, versions 1.26.1 and 1.26.2, appeared about 33 minutes apart. Both were later quarantined on PyPI, where version 1.26.0 remains the latest clean release.

A maintainer for the framework confirmed in a GitHub discussion that the compromised releases had been removed and that an investigation was underway. Microsoft acknowledged the incident.

The malicious distributions kept the legitimate framework components intact, so applications continued to work normally. Hidden alongside them, however, was code that exploited a Python startup mechanism to execute automatically in any affected environment — running whenever the interpreter started, even if the application never imported the compromised package.

Researchers at OX Security, Wiz, Endor Labs and SafeDep, who analysed the malware independently, reported that it harvested secrets stored in environment variables and configuration files, along with credentials belonging to other running processes. It also attempted to obtain Azure managed identity tokens and Azure DevOps authentication tokens, either of which can grant access to cloud resources without a password. The second malicious release extended the theft to GitHub Actions, the continuous-integration service used by countless software teams.

SecurityWeek noted that the method used to publish the malicious packages had not been disclosed; attackers typically obtain such access by stealing a maintainer's publishing credentials or by inserting a collaborator account.

Security firms advised organisations to audit any environment that installed either version since Tuesday, rotate Azure, Azure DevOps and GitHub credentials, and treat 1.26.0 as the last trustworthy release. Researchers said the incident was the latest in a string of attacks on open-source package repositories, where a single poisoned release can reach hundreds of thousands of machines within days.

Microsoft's investigation continues. No count of affected installations has been published.

## Sources
- [SecurityWeek](https://www.securityweek.com/microsoft-agent-framework-releases-poisoned-with-credential-stealer/)
- [BleepingComputer](https://www.bleepingcomputer.com/news/security/microsofts-agent-framework-pypi-package-compromised-to-steal-credentials/)
- [The Register](https://www.theregister.com/security/2026/11/18/microsofts-official-python-agent-framework-hijacked-to-distribute-malware/5310858)
