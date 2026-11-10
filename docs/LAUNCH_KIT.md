# CreativeCode Engine — Community launch kit (Phase 2)

**Prepared:** 2026-11-10 · **Release:** v0.2.0 · **Status:** GitHub feedback issue and first DEV Community article published; Reddit and other community posts remain unposted.

## Public links

- Repository: https://github.com/faysalishere/creativecode-engine
- Live interactive design study: https://faysalishere.github.io/creativecode-engine/
- Full portfolio concept pilot: https://faysalishere.github.io/creativecode-engine/demo/portfolio/
- Official release: https://github.com/faysalishere/creativecode-engine/releases/tag/v0.2.0
- Community feedback: https://github.com/faysalishere/creativecode-engine/issues/1
- Published DEV article: https://dev.to/faysalishere/i-built-an-open-source-toolkit-to-fix-repetitive-ai-generated-ui-designs-5ej5

## Positioning and truth-in-marketing

**For:** independent developers, people learning AI-assisted coding, UI designers who want meaningful layout alternatives.

**One sentence:** CreativeCode Engine is an open-source, offline Python design-direction toolkit and prompt workflow that helps users challenge repetitive UI concepts before writing code.

**What works today:** three *curated* concept architectures for portfolio/directory/product briefs; declared-structure originality heuristics; an evidence-gated reviewer packet; design prompts; a static interactive concept demo; English/Bangla in the portfolio pilot.

**What it is NOT:** a trained AI model, autonomous coding agent, screenshot-based originality detector, production website generator, or a hosted API. The GitHub Pages **demo exists** but does not run the Python CLI in the browser.

Use the actual v0.2.0 release URL; do not imply third-party adoption, star counts, performance metrics or real-user validation.

## Channel A — DEV Community technical article (ready to edit and post)

Suggested tags: python, opensource, webdev, discuss. Follow DEV's current guidelines and keep the discussion technical.

### Title: I built an offline toolkit to challenge repetitive AI-generated UI ideas

When I ask an AI coding assistant for a new UI, I often get a familiar composition: a large headline, a few equal cards, rounded buttons and a different gradient. The code may work, but a color change is not a new design direction.

I built **CreativeCode Engine**, a small open-source toolkit for deciding *what to design* before asking an assistant to implement it.

### What it currently does

1. Generates three **curated structural starting points** for portfolio, directory or product briefs. These are rule-based configurations, not an LLM inventing new designs.
2. Compares declared composition/navigation/content dimensions to flag superficial alternatives. It does not inspect screenshots.
3. Builds a design-critic packet with evidence gates, so untested behavior is explicitly marked as unverified.
4. Includes prompts and a bilingual interactive portfolio concept demo.

### Try it locally

Python 3.10+ is sufficient; no pip packages or API key are needed for the core CLI:

~~~bash
git clone https://github.com/faysalishere/creativecode-engine.git
cd creativecode-engine
python3 -m creativecode concepts --brief examples/portfolio_brief.json --out concepts.json
python3 -m creativecode originality --concepts concepts.json --out originality.json
python3 -m creativecode critique --brief examples/portfolio_brief.json --concepts concepts.json --out critic.json
~~~

There's also a browser-based design study you can explore without installing anything:

https://faysalishere.github.io/creativecode-engine/

### The question I'm testing

Can a repeatable workflow make AI-assisted design exploration less generic **without pretending that a heuristic can judge aesthetics**? My current approach separates concept generation from adversarial review, then asks a person to approve the direction.

**Limitations:** current concept patterns are curated, similarity is based on declared fields, and there's no built-in generative model or autonomous website builder. This is an early developer toolkit, not a finished end-to-end product.

I'd value technical feedback on the structural originality heuristic, CLI ergonomics and which concept comparisons would help in a real workflow.

**Source:** https://github.com/faysalishere/creativecode-engine

**Focused feedback issue:** https://github.com/faysalishere/creativecode-engine/issues/1

## Channel B — Reddit r/SideProject (adapt to live rules before posting)

**Title:** Built an offline toolkit for exploring different UI structures before AI coding — looking for feedback

**Body:**

I've been experimenting with a small open-source toolkit called CreativeCode Engine. The problem I'm trying to address is AI-generated UI concepts that look different only because the colors changed.

It has a Python 3.10+ offline CLI for three curated concept starting structures, declared-structure similarity checks and an evidence-gated review packet. There is also a free static interactive portfolio study: https://faysalishere.github.io/creativecode-engine/

It's early: no built-in LLM, no automatic website builder and no screenshot originality judging. Source: https://github.com/faysalishere/creativecode-engine

If you use AI to build interfaces, what is the bigger obstacle: repetitive layouts, missing design rationale, or weak review/testing? I'm especially interested in false positives in the originality checks.

**Posting policy:** Share once only if current subreddit rules allow project promotion; disclose that you built it, and participate genuinely in replies. No upvote requests, duplicate blasts or bot submissions.

## Channel C — Reddit r/opensource (conditional)

Read https://www.reddit.com/r/opensource/about/rules before posting. If permitted, choose the appropriate self-promotion flair and focus on the MIT license, dependency-free architecture and specific contribution requests. Do not copy the same Reddit post unchanged across communities.

**Title:** CreativeCode Engine: MIT-licensed design-direction toolkit (Python, no API key)

**Body:** I released a small MIT-licensed Python toolkit to explore multiple UI structures before implementing AI-assisted code. The CLI uses curated concept structures and transparent heuristics; it is not a generative model. There's a public demo and documented reviewer packet. I'd appreciate feedback on the originality rules and potential contributor-friendly tests. Repo: https://github.com/faysalishere/creativecode-engine | Demo: https://faysalishere.github.io/creativecode-engine/

## Hacker News / Show HN — hold for now

Official guidelines: https://news.ycombinator.com/showhn.html. Show HN expects non-trivial work that people can try, not a marketing landing page or quickly assembled demo. Re-evaluate after external developer testing improves the CLI and a real use case demonstrates value. Do not post a premature Show HN or ask for upvotes.

## Optional short personal social post

I built CreativeCode Engine, an open-source experiment in better AI-assisted UI decisions. Instead of presenting three color swaps as three concepts, it explores structural alternatives and makes missing evidence explicit. Offline Python CLI + interactive browser demo. Repo: https://github.com/faysalishere/creativecode-engine · Demo: https://faysalishere.github.io/creativecode-engine/ . Feedback welcome.

Only post through an account that represents the creator/project. Do not post CreativeCode content to an unrelated connected music/brand channel.

## Launch procedure

1. Open both live demo URLs and verify functionality in a fresh browser.
2. Publish the DEV article **once** from a DEV account owned by the creator; no DEV account is connected to this workflow.
3. Share an adapted Reddit feedback post **only after** reading the current community rules; avoid cross-posting everywhere at once.
4. Respond to comments and genuine bug reports. Keep criticism visible.
5. Record public post URLs and dates here after posting, rather than treating drafts as published.
6. Compare genuine 7-day and 30-day metrics (GitHub traffic unique visitors/clones if available, referral URLs, stars, forks, new issues, actual users reporting successful CLI runs). Never invent numbers.

### Tracking ledger

| Channel | Publication status | Post URL | Date | Feedback/actions |
|---|---|---|---|---|
| GitHub public feedback issue | Published | https://github.com/faysalishere/creativecode-engine/issues/1 | 2026-11-10 | Pending |
| DEV Community | Published; formatting review recommended | https://dev.to/faysalishere/i-built-an-open-source-toolkit-to-fix-repetitive-ai-generated-ui-designs-5ej5 | 2026-11-10 | Article public (HTTP 200); headings and command formatting need improvement |
| Reddit r/SideProject | Draft ready, not posted | — | — | — |
| Reddit r/opensource | Conditional draft, not posted | — | — | — |
| Hacker News | Deferred | — | — | — |

### Baseline

Capture GitHub Insights → Traffic and repository statistics on the day of first external post. This repository's public star/fork numbers and traffic can change; no numeric baseline is claimed in this document.

## Maintenance

Keep outreach accurate when the product changes. Do not impersonate independent reviewers, buy engagement, ask for upvotes or claim a live CLI hosted on GitHub Pages.