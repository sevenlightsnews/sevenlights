+++
title = "Backdoored Claude Code Extension Circulated on Cursor's Marketplace for 11 Hours"
date = 2026-10-31T16:30:00-04:00
lastmod = 2026-10-31T16:30:00-04:00
draft = false
slug = "cursor-marketplace-backdoored-claude-extension"
summary = "Cursor confirmed that tampered versions of Anthropic's Claude Code extension were distributed through its marketplace for about 11 hours on Oct. 29, exposing thousands of developers to software that installs a persistent SSH backdoor."
description = "Cursor confirmed that tampered versions of Anthropic's Claude Code extension were distributed through its marketplace for about 11 hours on Oct. 29, exposing thousands of developers to software that installs a persistent SSH backdoor."
author = "Seven Lights"
categories = ["Technology"]
tags = ["Cursor", "Anthropic", "security", "malware", "SSH backdoor", "developers"]
image = "/images/stories/cursor-marketplace-backdoored-claude-extension.webp"
image_alt = "A dim developer workspace at night, three monitors showing lines of source code in a dark editor, a red warning dialog blurred on one screen, a mechanical keyboard and coffee mug on the desk, no readable text or faces."
refs = 4
+++

![A dim developer workspace at night, three monitors showing lines of source code in a dark editor, a red warning dialog blurred on one screen, a mechanical keyboard and coffee mug on the desk, no readable text or faces.](/images/stories/cursor-marketplace-backdoored-claude-extension.webp)

Cursor confirmed that malicious versions of Anthropic's Claude Code extension were available through its VS Code extension marketplace for roughly eleven hours on October 29, exposing as many as 5,000 developers to software designed to install a persistent SSH backdoor on their machines.

The affected packages, published under the identifier Anthropic.claude-code at versions 2.1.312 and 2.1.313, were live between about 2:27 a.m. and 1:35 p.m. Pacific time, Cursor said in a security notice. The tampered extension targeted Windows and macOS systems.

Researchers at the security firms Phorion and OpenSourceMalware found that the attackers inserted a malicious JavaScript loader at the beginning of the extension's extension.js file, leaving the legitimate code otherwise unchanged. Once run, the payload attempted to plant an SSH backdoor for lasting remote access, reporting to a hidden endpoint on port 8099 and adding an entry named svc-telemetry to the system's authorized keys.

Cursor advised teams to inspect authorized keys for that entry, review extension installation records, endpoint alerts and network logs, and isolate hosts where evidence shows the payload executed. Removing the extension alone is not sufficient, the company warned, because separate scripts can remain; it published platform-specific cleanup guidance and urged rotation of credentials and sessions from a trusted system.

Anthropic has said the compromised packages were not published by it. The Register reported the company distanced itself from the compromise, and the extension's official versions remained unaltered.

The episode struck at a central assumption of modern software work: that extension marketplaces operated by major tools vendors are a controlled channel. Cursor, an artificial-intelligence code editor built from Microsoft's open-source Visual Studio Code, said the incident was contained to the eleven-hour window and that it had removed the packages. Security firms urged organizations that use the editor to audit developer machines from the Oct. 29 window regardless of whether tampered versions appeared to install.

## Sources

- [Cyber Security News](https://cybersecuritynews.com/malicious-claude-code-extension-with-cursor/)
- [BleepingComputer](https://www.bleepingcomputer.com/news/security/malicious-claude-code-extension-on-cursor-planted-ssh-backdoors/)
- [Ars Technica](https://arstechnica.com/security/2026/10/anthropic-vs-code-extension-on-cursor-backdoored-for-nearly-12-hours/)
- [The Register](https://www.theregister.com/cyber-crime/2026/10/30/anthropic-that-claude-code-extension-compromise-couldnt-be-us/5306682)
