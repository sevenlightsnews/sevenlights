+++
title = "Microsoft Previews Windows Server 2028 With Security Defaults That Break Compatibility"
date = 2026-11-19T03:45:00-05:00
lastmod = 2026-11-19T03:45:00-05:00
draft = false
slug = "windows-server-2028-security-first-preview"
summary = "Microsoft opened a public preview of Windows Server 2028 with hardened security settings switched on by default, a break with the backward compatibility that long defined the platform."
description = "The preview turns on SMB signing, modern TLS with post-quantum key exchange and Kerberos over NTLM; older clients and applications may fail until administrators re-enable legacy options."
author = "Seven Lights"
categories = ["Technology"]
tags = ["windows server", "microsoft", "security", "ignite", "it administration"]
image = "/images/stories/windows-server-2028-security-first-preview.webp"
image_alt = "Rows of rack-mounted servers in a modern data center aisle, green status lights in long horizontal lines, glass panels reflecting overhead lighting, clean symmetrical composition, photojournalism, no readable text, 3:2"
refs = 3
+++

![Rows of rack-mounted servers in a modern data center aisle, green status lights in long horizontal lines, glass panels reflecting overhead lighting, clean symmetrical composition, photojournalism, no readable text, 3:2](/images/stories/windows-server-2028-security-first-preview.webp)

Microsoft has opened a public preview of Windows Server 2028, announced this week at its Ignite conference. For the first time the flagship server operating system arrives with its security protections switched on by default — a decision that will break older clients and applications until administrators intervene.

The preview, the successor to Windows Server 2025, applies a hardened security baseline from first boot. Microsoft enables Server Core, the minimal installation option without a graphical shell, as the default configuration. The baseline enforces Kerberos authentication over the older NTLM protocol, requires signing and encryption of Server Message Block file-sharing traffic, turns on the host firewall, and restricts Transport Layer Security to modern cipher suites, including hybrid post-quantum key exchange based on the ML-KEM standard. Remote Desktop connections require network-level authentication, and the platform is designed to be managed through Microsoft's Intune administration tools.

The Register's report on the preview put the change bluntly in its headline: the server "won't be compatible by default." Ars Technica, which reviewed the announcement, described the release as a bet on a "security-first" approach for enterprise data centers.

The defaults reflect a decade of pressure on Microsoft over the exploitability of legacy protocols. NTLM and unsigned SMB have featured prominently in some of the largest intrusions of recent years, including attacks that spread laterally through corporate networks. Microsoft has moved the same direction in stages on Windows client editions; the server line has lagged because enterprises depend on ageing applications and industrial equipment.

Administrators will be able to re-enable legacy features individually, restoring compatibility at the cost of the protections. BleepingComputer noted that the preview is intended to give organisations time to test their workloads before the general release, planned for 2028.

The preview is available to enrol through Microsoft's insider programme for IT professionals. Microsoft did not say how many enterprise customers had already tested the baseline.

## Sources
- [BleepingComputer](https://www.bleepingcomputer.com/news/microsoft/microsoft-announces-windows-server-2028-with-hardened-security/)
- [The Register](https://www.theregister.com/os-platforms/2026/11/18/windows-server-2028-wont-be-compatible-by-default/5310766)
- [Ars Technica](https://arstechnica.com/gadgets/2026/11/windows-server-2028-public-preview-bets-on-a-security-first-approach/)
