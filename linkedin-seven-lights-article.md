# Seven Lights: A News Site Written by an AI That Runs on My Own Hardware

Every morning at 3:00 a.m. Eastern, while I'm asleep, a pipeline on my home server reads 174 public RSS feeds from news organizations around the world, groups the articles that cover the same event, and publishes a short factual summary of each story that at least three different media companies are reporting.

It's called Seven Lights (sevenlights.org), an independent news site with no advertising, no sponsored posts, no affiliate links, no paid placement, and no paywall. It has been running on that schedule since 2026, and every story on it was written by a local, open-weight AI model running on hardware I own.

**What it is**

Seven Lights publishes one kind of thing: a plain, factual summary of the stories that multiple established newsrooms are already reporting, with links to that reporting. Seven categories: Global, US, Politics, Business, Technology, Sports, Entertainment. No opinion, no analysis, no commentary. The editorial rule is simple. If three separate articles from three different media companies are reporting a story with enough concrete detail, it qualifies. Two outlets owned by the same company count as one source. If a story doesn't meet the bar, it doesn't ship. Some days that means fewer stories. The bar never moves to manufacture volume.

Every story links to the original articles, every claim is attributed to the organization that reported it, and the complete list of feeds the software reads is published on the site itself. Transparency is the whole point. A reader can compare every summary against the underlying reporting.

**How I do it**

I don't write the news. I built and maintain the system that does:

- A deterministic pipeline fetches the feed pool, drops stale items, clusters articles covering the same event, deduplicates coverage from the same media family, and ranks by how widely a story is being covered, not by any preference for a topic or a side.
- An AI agent reads the day's brief and the full text of the clustered articles and writes each summary in a straight newspaper voice. Who, what, when, where, why. 300 to 450 words, synthesizing the shared facts once.
- A hard lint gate runs before anything can be published: minimum three source links from three distinct outlets, word-count bounds, category rules, image rules, banned cliches. If the lint fails, nothing ships.
- Illustrations for every story are generated in-house from the reported facts. The site never republishes photographs taken by newsrooms.
- The site builds with Hugo, deploys through GitHub and Cloudflare Pages, and publishes itself. A daily podcast edition is produced the same way.

**The tech behind it**

The interesting part, for me, is what's *not* in the stack. There is no commercial AI API anywhere in the pipeline. The writing, editing, and orchestration run on open-weight models served by llama.cpp on a Dell T7910 server in my home office: 48 cores, 128 GB of RAM, and a 32 GB GPU. The same box generates the story images through ComfyUI, which runs on an RTX 5060 Ti. The models are open weights, quantized to fit the hardware, and everything (fetching, clustering, drafting, linting, building, deploying) happens on machines I control, on a schedule I control.

No per-token API bills. No third party reading the pipeline's data. No vendor deciding what the model can say. The whole newsroom costs electricity and a Cloudflare Pages plan.

**Why no monetization**

This is deliberate. Ad-supported news sites have an incentive structure that shapes what gets published. Outrage sells, and pageviews shape coverage. Seven Lights has no incentive at all except the reputational one: if the summaries are wrong or the sourcing is thin, that's on me. Running on local open-weight models closes the loop. The site isn't monetizing my readers' data, and it isn't feeding anyone else's either.

It's a small demonstration of what I think a lot of publishing will look like. Deterministic plumbing does the mechanical work, an open-weight model does the language work, and a human owns the standards, the guardrails, and the editorial rules that the machine is not allowed to relax.

The site is live at sevenlights.org. The About page and the published source-feed list explain the standards in full. Happy to talk to anyone building similar pipelines; I've learned a lot about what breaks at 3 a.m.

#AI #OpenSource #Publishing #LocalLLM #News #Automation #SideProject
