+++
title = "OpenAI rates new GPT-6 Cyber model 'critical' after finding hundreds of software flaws"
date = 2026-11-07T03:30:00-05:00
lastmod = 2026-11-07T03:30:00-05:00
draft = false
slug = "openai-gpt6-cyber-model"
summary = "OpenAI said Thursday its security-specialized GPT-6 Cyber model found 81 Firefox flaws and built 948 working Linux kernel exploits in testing, leading it to rate the system 'critical' and restrict access."
description = "The company reported 304 critical issues to maintainers and limited the model to approved defenders while new monitoring ties its use to customer permissions."
author = "Seven Lights"
categories = ["Technology"]
tags = ["artificial intelligence", "cybersecurity", "openai", "software vulnerabilities", "linux"]
image = "/images/stories/openai-gpt6-cyber-model.webp"
image_alt = "Security operations center wall of terminal screens showing scrolling code, empty chairs, blue monitor glow in a dark room, no faces visible"
refs = 3
+++

![Security operations center wall of terminal screens showing scrolling code, empty chairs, blue monitor glow in a dark room, no faces visible](/images/stories/openai-gpt6-cyber-model.webp)

OpenAI said Thursday that its new GPT-6 Cyber model, built to hunt software vulnerabilities, identified 81 previously unknown high-severity flaws in the Firefox browser and constructed 948 working privilege-escalation exploits against the Linux kernel in internal testing. Mozilla is rolling out patches for the Firefox defects.

In the kernel exercise, the model identified 2,308 potential flaws, reproduced 1,724 of them and produced 948 exploits that gained elevated privileges, up from 166 for the prior GPT-5.6 Sol system. OpenAI reported 304 critical issues to maintainers, all of which have been fixed, the company said.

On ExploitGym, a benchmark of vulnerability exploitation tasks, GPT-6 Cyber scored 48.5 percent against 32.1 percent for GPT-5.6 Cyber. The result moved the model to a "critical" rating for cybersecurity under OpenAI's Preparedness Framework, up from "high."

The company said alignment testing improved. Given a decoy service outside authorized boundaries, the model avoided exploiting it in 99.93 percent of unprompted trials, compared with 94.49 percent for the previous system; with safety prompts, violations fell to zero. Access is limited to approved customers under a program OpenAI calls Daybreak Red, with a Daybreak Blue tier planned for defenders. The company added monitoring that matches the model's actions to each customer's permissions.

SecurityWeek reported the rating and access controls. BleepingComputer reported the Firefox and Linux results.

Defenders and vendors have "a limited window to use frontier models to secure software," OpenAI said in its announcement. Rob T. Lee of the industrial-control security firm Dragos, which tested the model, told Mashable that the concern is the falling skill floor: an attacker once needed years of exploit-development experience, and systems like this compress that training. OpenAI said it built specific safeguards against attacks on industrial control systems.

The model's release follows a year in which frontier labs have raced to productize vulnerability research while regulators press for capability disclosures. OpenAI said it will expand Daybreak access as its monitoring matures.

## Sources

- [SecurityWeek](https://www.securityweek.com/openai-says-new-gpt-6-cyber-model-hunts-flaws-without-crossing-the-line/)
- [BleepingComputer](https://www.bleepingcomputer.com/news/security/openais-new-gpt-6-cyber-ai-finds-81-firefox-flaws-948-linux-bugs/)
- [Mashable](https://mashable.com/tech/openai-gpt-6-cyber)
