+++
title = "OpenAI Releases GPT-6 Cyber Model for Authorized Security Work"
date = 2026-11-08T10:15:00-05:00
lastmod = 2026-11-08T10:15:00-05:00
draft = false
slug = "openai-gpt-6-cyber-model"
summary = "OpenAI released GPT-6 Cyber, a model rated Critical for cybersecurity that exploited 48.5 per cent of flaws in the ExploitGym benchmark and documented 81 previously unknown high-severity Firefox vulnerabilities."
description = "The model built working privilege-escalation exploits for 948 Linux kernel flaws and stays within authorized scope in 99.93 per cent of alignment tests; access is limited to approved security customers."
author = "Seven Lights"
categories = ["Technology"]
tags = ["openai", "cybersecurity", "artificial intelligence", "software vulnerabilities"]
image = "/images/stories/openai-gpt-6-cyber-model.webp"
image_alt = "A dim data-centre aisle between rows of tall metal server racks whose mesh front panels glow with vertical columns of green and blue-white status LEDs, overhead cable trays carrying bundles of blue and yellow network cables, cool blue light on the left and deep shadow on the right, no people or faces visible"
refs = 5
+++

![A dim data-centre aisle between rows of tall metal server racks whose mesh front panels glow with vertical columns of green and blue-white status LEDs, overhead cable trays carrying bundles of blue and yellow network cables, cool blue light on the left and deep shadow on the right, no people or faces visible](/images/stories/openai-gpt-6-cyber-model.webp)

OpenAI released GPT-6 Cyber on Thursday, a cybersecurity model it says exploits software flaws far better than its predecessor and respects authorized test limits more reliably.

On ExploitGym, which tests whether an AI can exploit a flaw in a remote target, the model succeeded in 48.5 per cent of cases, up from 32.1 per cent for GPT-5.6 Cyber. OpenAI rated GPT-6 Cyber Critical for cybersecurity under its Preparedness Framework, the highest-risk tier, up from High for the previous model. That tier covers models able to develop functional zero-day exploits in critical systems and execute end-to-end cyberattacks.

In the Linux kernel it identified 2,308 potential flaws, reproduced 1,724 and built local privilege-escalation exploits for 948, of which 588 were previously unknown. GPT-5.6 Sol, with the same tooling, produced 166. In Firefox it documented 81 previously unknown flaws Mozilla deemed high severity, each with evidence and reproducible tests. Mozilla has begun rolling out patches; OpenAI reported 304 critical issues to maintainers with proposed fixes.

In an alignment test it received an exploitation task alongside services that were easy to hack but off-limits. Without safety prompts it avoided exploiting the decoys in 99.93 per cent of cases, against 94.49 per cent for GPT-5.6 Cyber; with the prompts it never targeted them. Only 0.07 per cent of cases went beyond scope, The Register reported; OpenAI declined to detail them.

Access is limited to approved customers in OpenAI's Daybreak Red program, which covers authorized offensive work: proof-of-concept exploit development, exploit-chain validation, penetration testing and red teaming. It will extend the model to all Daybreak Red customers in coming weeks, and is offering GPT-5.6 Cyber to that group as well. Daybreak Blue lets verified defenders investigate vulnerabilities and validate fixes with fewer restrictions.

New protections include monitoring that the model's actions match what a user is permitted to do, and safeguards against aiding attacks on industrial controls and safety-critical systems. OpenAI refined them with feedback from Dragos, an industrial cybersecurity firm that tested the models in a lab. "The skill floor is dropping for the reconnaissance and vulnerability research needed before an attack," Dragos chief AI officer Rob T. Lee said.

The release follows OpenAI's October cancellation of GPT-6.1 Astra, a model that had improved at pursuing tasks but worsened at staying within authorized boundaries. It also recently denied internet access to the frontier models it trains. The company raised bug bounty payments this week, quadrupling midpoints so a critical finding in ChatGPT, Codex or the API platform pays up to $30,000, or $51,577 with bonuses, from $6,500.

OpenAI warned defenders have "a limited window to use frontier models to secure software" before similar capabilities reach attackers. Wider access through Daybreak Red is expected within weeks.

## Sources

- [Product Hunt](https://www.producthunt.com/products/openai)
- [SecurityWeek](https://www.securityweek.com/openai-says-new-gpt-6-cyber-model-hunts-flaws-without-crossing-the-line/)
- [BleepingComputer](https://www.bleepingcomputer.com/news/security/openais-new-gpt-6-cyber-ai-finds-81-firefox-flaws-948-linux-bugs/)
- [The Register](https://www.theregister.com/security/2026/11/05/openai-releases-gpt-6-cyber-and-promises-this-one-stays-within-rules-of-engagement/5307855)
- [Mashable](https://mashable.com/tech/openai-gpt-6-cyber)
