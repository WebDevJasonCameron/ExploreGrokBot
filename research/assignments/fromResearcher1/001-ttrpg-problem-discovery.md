# Research Report 001 — TTRPG Problem Discovery

**Report ID:** 001  
**Date:** 2026-08-31  
**Analyst:** Market Research Analyst (Employee 001)  
**Stage:** Stage 1 — Initial Screening / Problem Discovery  
**Status:** Complete — awaiting Owner review  
**Path:** `research/assignments/001-ttrpg-problem-discovery.md`  

This report identifies recurring problems. It does **not** score business opportunities, recommend building a product, or recommend investment.

---

## Executive Summary

Tabletop role-playing game (TTRPG) players and game masters repeatedly report five clusters of friction:

1. Game-master session preparation consumes a large amount of unpaid time and is repeatedly linked to burnout.
2. Forming and keeping a reliable play group is treated by experienced GMs as the hardest part of the hobby; many campaigns end without a satisfying conclusion.
3. Campaign knowledge (NPCs, lore, loot, session history) is stored in ad-hoc notes, wikis, and general-purpose tools that many tables abandon or underuse.
4. Digital play commonly requires several paid platforms at once; purchased books, characters, and maps do not travel cleanly between them.
5. Players often cannot operate their own characters and rules during play, which slows sessions and transfers lookup work to the GM.

These are **problems**, not product ideas.

Spending in adjacent categories is real: Hasbro reports that D&D Beyond has more than 30 million registered accounts; Foundry VTT sells a $50 license; Roll20 and D&D Beyond sell subscriptions; StartPlaying states that the average paid game costs $15–20 per session; TTRPG Insider reports StartPlaying has paid out more than $50 million to GMs. That is evidence that people already spend money on play, digital content, and access to a table. It is **not** evidence that a new product would be bought.

Several of these problems may already be adequately solved for a large share of tables (paper play, published adventures, Lazy-DM methods, Owlbear Rodeo, Kanka, Pathbuilder, D&D Beyond character tools). The strongest remaining questions are how painful the unsolved remainder is, whether customers will switch, and whether the remaining pain is social rather than software-shaped.

---

## Research Question

What recurring problems do tabletop RPG players and game masters experience that might later be worth investigating as opportunities for a small software or digital-product company?

The investigation started from problems, not from product ideas.

---

## Method and Evidence Standards

Sources reviewed include:

- Independent GM surveys and essays (Sly Flourish).
- Official product pricing and help pages (Foundry VTT, D&D Beyond, StartPlaying, LegendKeeper).
- Industry reporting (Hasbro earnings commentary, TTRPG Insider).
- Practitioner Q&A (RPG Stack Exchange, D&D Beyond forums, Demiplane forums).
- Tool comparison and review writing (used cautiously; several sites sell competing tools).

Claims are labeled:

| Label | Meaning |
| --- | --- |
| **Fact** | Supported by a named primary or official source. |
| **Observation** | Repeated pattern across independent sources. |
| **Inference** | Reasonable conclusion from the evidence, not directly proven. |
| **Speculation** | Possible, but weakly supported. |
| **Vendor claim** | Comes from a company or product blog that benefits if the problem looks large. Treat as unverified until independently confirmed. |

Vendor blogs (StoryRoll, ScriptoriumGM, StormScape, Quill, Kazkar, and similar) were used only as pointers to products or as examples of marketing narratives. Their survey statistics were **not** treated as verified facts.

Research was not limited to Dungeons & Dragons. D&D dominates public discussion and digital spending, so it appears more often in the evidence. Pathfinder 2e appears as a second major digital-tool ecosystem.

---

## Brief Market Context

These facts describe the environment in which the problems occur. They are not opportunity scores.

- **Fact.** Hasbro Q2 2026 earnings commentary stated that D&D Beyond has more than 30 million registered accounts and “reaches more than three in four hobby role-playing gamers each year.” Registered accounts are not the same as active paying customers. ([stockanalysis.com/stocks/has/transcripts/675981-q2-2026/](https://stockanalysis.com/stocks/has/transcripts/675981-q2-2026/))
- **Fact.** Hasbro acquired D&D Beyond from Fandom in 2022 for $146.3 million. ([fool.com/investing/2022/04/17/hasbro-doubles-down-on-dungeons-and-dragons/](https://www.fool.com/investing/2022/04/17/hasbro-doubles-down-on-dungeons-and-dragons/))
- **Fact.** D&D Beyond Hero and Master subscriptions are sold at $2.99 and $5.99 per month (lower if billed annually). ([dndbeyond.com/en/subscribe](https://www.dndbeyond.com/en/subscribe))
- **Fact.** Foundry VTT individual licenses are $50 one-time; only the host needs a license. ([foundryvtt.com/purchase/](https://foundryvtt.com/purchase/), [foundryvtt.com/article/faq/](https://foundryvtt.com/article/faq/))
- **Fact.** StartPlaying’s help center states the average game price is $15–20 per session, with players charged each session of a campaign. ([StartPlaying help](https://intercom.help/startplaying/en/articles/8959627-how-much-does-it-cost-to-play-on-startplaying))
- **Fact / reported interview.** TTRPG Insider (Dec 2025), citing StartPlaying CEO Devon Chulick and a Many Sided Media interview, reported ~5,000 GMs, ~80,000 players, and more than $50 million paid out to GMs since inception; platform fee rose from 10% to 15% in January 2025. These figures were not independently audited in this research. ([ttrpginsider.news](https://www.ttrpginsider.news/p/pay-to-play-the-business-of-the-professional-dungeon-master))

**Inference.** People already pay for digital rules, character tools, virtual tabletops, maps, campaign wikis, and access to a GM. The category is not “hobbyists who never spend money.”

---

## Problem 1 — Session preparation consumes a large amount of unpaid GM time

### Who experiences the problem

Primarily **game masters / dungeon masters**, especially those running weekly or biweekly home games from homebrew or heavily customized published adventures. Players experience the downstream effect when the GM is exhausted, late, or cancels.

### What they are trying to accomplish

Prepare enough material for the next session: scenes, NPCs, encounters, maps, loot, and continuity with prior play — without turning hobby time into a second job.

### Evidence that the problem exists

- **Fact.** Sly Flourish Twitter poll (April 2020, 3,663 responses) asked how long DMs prep for a roughly four-hour D&D game: 10% about 30 minutes or less; 33% about an hour; 28% about two hours; 29% about three hours or more. ([slyflourish.com/how_long_to_prep.html](https://slyflourish.com/how_long_to_prep.html))
- **Fact.** An earlier Sly Flourish prep-habits survey (804 DMs) reported that among 198 weekly 4e DMs, 69% spent less than three hours and 8% spent more than six. ([slyflourish.com/dm_survey_results.html](https://slyflourish.com/dm_survey_results.html))
- **Observation.** Advice literature treating multi-hour prep as a burnout risk is abundant and long-lived (Lazy DM books and articles; published-adventure use; “prep less” frameworks). The persistence of that advice is itself evidence that over-prep remains common.
- **Vendor claim, not used as fact.** Product blogs describe 6–8 hour prep weeks. Those anecdotes may be real for some GMs but are marketing-adjacent and not survey-grade.

**Inference.** A large minority of GMs spend roughly as much time prepping as playing. A larger group spends 1–2 hours per session. Prep is a recurring weekly cost, not a one-time setup cost.

### How people currently solve it

- Published adventures and starter sets instead of homebrew.
- “Lazy GM” / next-session-only prep (Sly Flourish *Return of the Lazy Dungeon Master* and related books).
- Improvisation and random tables.
- Digital encounter builders (D&D Beyond, Kobold Fight Club / Kobold Plus Fight Club).
- VTT modules that pre-place maps, tokens, and walls (Roll20 marketplace adventures; Foundry adventure imports).
- General-purpose AI chat tools for NPC names, boxed text, and stat sketches.
- Paying someone else to GM (StartPlaying).

### Relevant existing products or alternatives

| Approach | Examples | Notes |
| --- | --- | --- |
| Method books | *Return of the Lazy Dungeon Master*, other GM advice books | Paid; teaches process, not software |
| Official digital prep | D&D Beyond encounter builder, official adventures | D&D-specific |
| VTT-ready modules | Roll20 / Foundry published adventures | Reduce map and token prep |
| Campaign / prep apps | World Anvil, LegendKeeper, Kanka, Notion templates, many newer AI prep tools | Overlapping with Problem 3 |
| Marketplace GMs | StartPlaying | Transfers prep labor to a paid GM |

### Evidence of dissatisfaction or inefficiency

- **Observation.** A recurring complaint is that GMs prep material players never encounter. Sly Flourish explicitly warns about diminishing returns after a full day of prep. ([slyflourish.com/how_long_to_prep.html](https://slyflourish.com/how_long_to_prep.html))
- **Observation.** VTT “nice” prep (dynamic lighting, walls, playlists, handouts) is repeatedly described as a time sink that is optional for play quality.
- **Inference.** The existence of an entire advice industry around *reducing* prep implies many GMs believe they are spending too much time, not too little.

### Counter-evidence (possible adequate solutions)

- Nearly half of the 2020 Sly Flourish poll (43%) already preps in about an hour or less. For that group the problem may be solved.
- Published adventures and theater-of-the-mind play remove much of the work.
- Many GMs enjoy prep and would not pay to shorten it.
- General-purpose AI already drafts NPCs, names, and encounters. **Speculation:** this may further shrink demand for dedicated prep software.

### Do people appear to spend money in this category?

**Yes, in adjacent forms.** People buy GM advice books, published adventures, VTT-ready modules, map packs, and paid GM seats. That is spending to reduce or replace prep labor. It is weaker evidence that they will pay for another prep *app*, because free methods and AI already exist.

### Important unknowns

- What share of high-prep GMs consider the time a problem versus a hobby they like.
- How much prep is system-specific (5e encounter math vs. PbtA improvisation vs. Pathfinder 2e encounter building).
- Whether AI chat tools have already absorbed the “generate content faster” demand.
- How often prep burden, versus scheduling, is the actual cause of a GM quitting.

### Initial confidence

**High** that unpaid GM prep is a recurring, measurable time cost.  
**Moderate** that it is painful enough, after existing methods, to remain an unsolved problem.  
**Low** that the remaining pain is a distinct software gap rather than a discipline / taste problem.

---

## Problem 2 — Forming and keeping a reliable play group

### Who experiences the problem

**Players** who cannot find a table or a GM.  
**GMs** who cannot fill seats, cannot keep attendance, or watch campaigns dissolve.  
Both groups when a campaign ends because life, not the story, intervened.

### What they are trying to accomplish

Play regularly with a compatible group, finish stories, and avoid the social and logistical work of constantly re-forming a table.

### Evidence that the problem exists

- **Fact.** Sly Flourish YouTube poll (25 August 2022, 2,600 respondents): how often do you reach a satisfying conclusion to your D&D campaign? Almost never 26%; rarely 21%; sometimes 31%; often 14%; almost always 7%. About half rarely or almost never finish satisfyingly. ([slyflourish.com/lack_of_satisfying_conclusions.html](https://slyflourish.com/lack_of_satisfying_conclusions.html))
- **Fact.** In follow-up discussion, Sly Flourish reported scheduling as “by far the number one reason,” followed by shiny-new-game syndrome, player churn, DM burnout, playstyle conflict, lack of interest, lack of campaign clarity, and TPKs. ([same article](https://slyflourish.com/lack_of_satisfying_conclusions.html))
- **Fact.** The same article states: “Finding and maintaining a D&D group is the hardest part of D&D.” Recommended workarounds include on-call players, fixed weekly slots, shorter campaigns, online play, and reminder emails.
- **Observation.** Dedicated LFG venues exist at large scale: Reddit `r/lfg`, Roll20 LFG, Discord servers, local game stores, StartPlaying. Persistent large LFG channels are evidence that matching is an ongoing problem, not a solved one.
- **Observation.** A large body of table advice (quorum rules, West Marches, “schedule the next session before you leave”) exists because cancellation and drift are common.
- **Vendor claim, not used as fact.** StoryRoll and similar sites cite an unverified “23% of scheduled sessions cancelled” figure attributed to an r/DnD survey. This research did not locate a primary source for that number.

### How people currently solve it

- Fixed weekly time so the game becomes a ritual.
- Quorum rules (play if 3 of 5 can attend).
- On-call / substitute players.
- Online play to widen the player pool.
- West Marches or episodic formats that tolerate rotating attendance.
- Discord polls, When2Meet, LettuceMeet, Doodle, Google Calendar.
- Purpose-built schedulers (Roll4Availability, Tabletop Time, and similar).
- Reddit / Discord / Roll20 LFG posts.
- Paid tables on StartPlaying (and competitors).
- Adventurers League / store organized play (more drop-in, less campaign continuity).

### Relevant existing products or alternatives

| Product / channel | Role | Commercial model |
| --- | --- | --- |
| StartPlaying | Paid GM marketplace + scheduling/payments | Per-session fees; 15% platform cut (reported) |
| Roll20 LFG | Find tables on a VTT | Free + VTT subscriptions |
| Reddit `r/lfg`, Discord | Free matching | Free; high noise, flakes, occasional scams (anecdotal) |
| When2Meet / Doodle / LettuceMeet | Generic availability polling | Free / freemium |
| Roll4Availability, Tabletop Time | TTRPG-specific scheduling | Product blogs; pricing not independently verified here |
| Game stores / Adventurers League | In-person organized play | Store traffic; usually free to play |

### Evidence of dissatisfaction or inefficiency

- **Observation.** Free LFG is repeatedly described as noisy: many “player looking for GM” posts, fewer GMs offering games, flaky applicants, and the need to re-post.
- **Observation.** Generic schedulers still leave a second conversation (“do we have enough people?”) after the poll closes. Purpose-built tools exist specifically to close that gap, which is evidence the generic tools are incomplete for this use.
- **Fact.** Players already pay $15–20 per session on average on StartPlaying to get a committed table and a GM. That is revealed-preference evidence that *access to a reliable game* is worth money for at least tens of thousands of people. ([StartPlaying help](https://intercom.help/startplaying/en/articles/8959627-how-much-does-it-cost-to-play-on-startplaying); [TTRPG Insider](https://www.ttrpginsider.news/p/pay-to-play-the-business-of-the-professional-dungeon-master))

### Counter-evidence (possible adequate solutions)

- StartPlaying already commercializes “I cannot find a reliable table.” For players willing to pay, the matching problem may be largely solved.
- Sly Flourish’s own advice is mostly social policy (fixed night, quorum, on-call list), not software. **Inference:** a large part of this problem may not be software-shaped.
- Many long-running groups exist without special tools.
- Paid tables introduce a different dissatisfaction (platform fees, variable GM quality, less “game with friends”).

### Do people appear to spend money in this category?

**Yes.** StartPlaying’s reported payout volume and public per-session prices are the strongest willingness-to-pay signal found in this assignment. People also pay for VTT subscriptions partly because online play makes attendance easier.

### Important unknowns

- How many people with the problem will pay versus insist the hobby must be free among friends.
- How much of campaign failure is scheduling versus burnout, boredom, or social conflict.
- Whether StartPlaying already captures most of the paying segment.
- Geographic / time-zone structure of unmatched demand.
- Safety, trust, and moderation costs of any matching marketplace (legal/reputation risk).

### Initial confidence

**High** that group formation and attendance are recurring, severe problems and a leading cause of dead campaigns.  
**High** that some people already pay to solve the “no table” version.  
**Moderate-to-low** that a *new* small-company software product is what the remaining friend-group scheduling problem needs.

---

## Problem 3 — Campaign knowledge is hard to capture, find, and share

### Who experiences the problem

**GMs** who must remember NPCs, factions, locations, plot threads, and what happened last session.  
**Players** who forget prior sessions, cannot find lore they are allowed to know, and lose character-journal details.  
Worse in long campaigns, West Marches games, and groups that meet infrequently.

### What they are trying to accomplish

Keep a usable record of the shared fiction and logistics (who is who, what was promised, what loot exists, what the players know) and retrieve the right fact in seconds during play.

### Evidence that the problem exists

- **Observation.** Dedicated campaign-wiki products have existed for years and still compete with Google Docs, Notion, Obsidian, OneNote, and paper binders. The category’s age plus continued new entrants is evidence the job is real and not considered finished.
- **Observation.** Independent comparison writing consistently describes the same split: World Anvil is powerful and hard; Kanka is cheaper and plainer; LegendKeeper is map-forward and paid; Notion/Obsidian are flexible but require the user to invent a system; Google Docs is easy and becomes messy. ([scriptoriumgm.com comparison](https://www.scriptoriumgm.com/blog/2025-11-13-gm-campaign-management-tools-comparison); [legendkeeper.com/best-world-anvil-alternatives/](https://www.legendkeeper.com/best-world-anvil-alternatives/); [kazkar.ai/blog/build-campaign-wiki](https://kazkar.ai/blog/build-campaign-wiki))
- **Observation.** Advice articles exist specifically about building a wiki “that actually gets used,” which implies many wikis are built and then abandoned.
- **Fact.** Sly Flourish lists “players forgetting what happened” as a reason to have attendees recap the prior session, and lists lack of campaign clarity among reasons campaigns fail to conclude. ([slyflourish.com/lack_of_satisfying_conclusions.html](https://slyflourish.com/lack_of_satisfying_conclusions.html))
- **Observation.** A newer cluster of tools (session recorders / “archivist” products) tries to auto-build wikis from recordings. That is a workaround for the cost of writing notes after a three-hour session.

**Inference.** The core job is not “write more lore.” It is “retrieve the right fact at the table without breaking play,” plus “give players a spoiler-safe view.” General note apps do the first poorly during live play; dedicated wikis often cost more setup than a weekly GM will maintain.

### How people currently solve it

- Paper notebooks and a DM screen.
- Shared Google Docs / Drive folders.
- Discord pins, search, and a `#recap` channel.
- Notion databases and paid/community Notion templates (e.g. Lorekeeper-style templates sold as one-time digital products).
- Obsidian vaults with community TTRPG plugins.
- Spreadsheets for NPCs, loot, and faction standing.
- World Anvil, Kanka, LegendKeeper, Campfire, and similar.
- Player-written recaps (often one designated scribe).
- Voice recordings and, more recently, AI transcription tools.

### Relevant existing products or alternatives

| Product | Model (as of this research) | Common praise / complaint pattern |
| --- | --- | --- |
| World Anvil | Free tier with limits/ads; Master about $7/mo or $4.50/mo annual; Grandmaster about $12/mo (secondary sources citing [worldanvil.com/pricing](https://www.worldanvil.com/pricing); official page was Cloudflare-blocked during this research) | Deep features; steep learning curve; “feels like work” |
| LegendKeeper | **Fact:** $9/mo or $90/year; 14-day trial; guests free ([legendkeeper.com/pricing](https://www.legendkeeper.com/pricing/)) | Faster/cleaner; no long-term free tier for creators |
| Kanka | Generous free tier; paid extras | Practical; less polished sharing |
| Notion / Obsidian | Free or already-paid productivity tools | Flexible; setup time; sharing/spoilers awkward |
| Google Docs / Sheets | Free | Zero learning curve; poor structure at campaign scale |
| Session-capture tools | Various subscriptions (~$10/mo range in vendor blogs) | Promise to automate notes; quality and privacy unverified here |

### Evidence of dissatisfaction or inefficiency

- **Observation.** Repeated independent complaints that World Anvil is cluttered, slow in play, and overkill for published-module tables.
- **Observation.** Notion-from-scratch setup is repeatedly estimated in how-to articles at many hours, and “most people don’t finish” is a recurring claim in template-seller copy. Treat the hour estimates as **vendor-adjacent**, but the existence of a template market is **fact-like evidence** that setup cost is a felt problem.
- **Observation.** Mid-session lookup (“that tavern from session 12”) is the failure mode people describe, not the absence of a place to type.

### Counter-evidence (possible adequate solutions)

- Kanka, Obsidian, and Google Docs are free enough that a motivated GM can solve this today.
- For published adventures, the book *is* the wiki.
- Some GMs prefer paper at the table and do not want another SaaS login.
- A large share of games are short enough that a single Google Doc is adequate.
- **Inference.** This may be a “tool discipline” problem more than a missing-product problem.

### Do people appear to spend money in this category?

**Yes.** World Anvil, LegendKeeper, Campfire, Notion templates, and newer AI note tools are paid. World Anvil has offered lifetime memberships at high one-time prices, which implies at least a core of committed paying worldbuilders. The *size* of that paying segment versus free-workaround users is unknown.

### Important unknowns

- Percentage of GMs who maintain a wiki for a whole campaign versus abandoning it.
- Whether players actually open player-facing wikis.
- How much of paid World Anvil/LegendKeeper use is RPG campaigns versus novelists and hobby worldbuilders.
- Privacy comfort with session recording / AI transcription.
- Switching costs after a campaign is already stored in one tool.

### Initial confidence

**High** that campaign information management is a recurring job with many workarounds.  
**Moderate** that current tools leave a meaningful gap (too heavy or too unstructured).  
**Low-to-moderate** that customers will pay *and switch* after already using Docs/Notion/Discord.

---

## Problem 4 — Digital play is split across tools; content and characters do not travel

### Who experiences the problem

**Online groups** (and hybrid groups) that use a character tool, a VTT, voice chat, and notes at the same time.  
**Players** who build a character in one system and play it in another.  
**GMs** who buy an adventure where the maps live on one platform and the rules/characters live on another.

This appears in both D&D (D&D Beyond + Roll20/Foundry + Discord) and Pathfinder 2e (Pathbuilder or Demiplane + Foundry + Discord).

### What they are trying to accomplish

Play with digital character automation, maps, dice, and voice — without re-entering the same character, buying the same book twice, or spending an evening on hosting and module configuration.

### Evidence that the problem exists

- **Fact.** RPG Stack Exchange question “Online D&D Module Purchase: Roll20, D&D Beyond or Both” (2020; still a canonical statement of the tradeoff) documents that the two stores do not share owned books; a common pattern is D&D Beyond for characters/planning and Roll20 for maps, with manual transfer. The accepted answer states the author would likely buy a module on *both* sites to get maps/tokens on Roll20 and planning tools on Beyond. ([rpg.stackexchange.com/questions/167291](https://rpg.stackexchange.com/questions/167291/online-dd-module-purchase-roll20-dd-beyond-or-both))
- **Fact.** D&D Beyond forum thread: users play on Roll20 but keep characters on Beyond; official reply is that purchases do not overlap; community workaround is the Beyond20 browser extension. ([dndbeyond.com forums](https://www.dndbeyond.com/forums/d-d-beyond-general/bugs-support/192725-is-it-possible-to-buy-content-on-dnd-beyond-but))
- **Fact.** Community importers exist because official interoperability does not: DDB-Importer (Foundry ← D&D Beyond), Beyond20 (Beyond → Roll20 dice), Pathmuncher (Pathbuilder → Foundry PF2e). Several advanced import features sit behind Patreon. ([foundryvtt.com/packages/ddb-importer](https://foundryvtt.com/packages/ddb-importer); [foundryvtt.com/packages/pathmuncher/](https://foundryvtt.com/packages/pathmuncher/))
- **Fact.** Foundry is a $50 one-time license with no official hosted service; official FAQ points users to third-party hosting partners. ([foundryvtt.com/article/faq/](https://foundryvtt.com/article/faq/)) A market of Foundry hosts (The Forge and others) exists specifically to remove port-forwarding and always-on server work.
- **Observation.** Independent VTT comparisons repeat the same tradeoff: Roll20 is easier and subscription-gated; Foundry is more powerful and harder; Owlbear Rodeo is simpler and thinner; D&D Beyond Maps/Sigil is convenient if the group is already in that ecosystem.
- **Fact.** Demiplane forum threads document Pathfinder groups rejecting official Nexus/Demiplane character tools in favor of Pathbuilder because browsing, performance, and new-player usability were worse; Pathbuilder then still requires an importer to reach Foundry. ([forums.demiplane.com](https://forums.demiplane.com/t/why-my-players-have-decided-to-not-use-demiplane-in-our-next-campaign/4663))

**Observation.** The workaround pattern matches the company’s opportunity-criteria examples: multiple tools for one task, browser extensions, paid importers, and third-party hosting.

### How people currently solve it

- Accept a two- or three-app stack (Beyond + VTT + Discord).
- Browser extensions and Foundry modules to sync characters.
- Buy content twice when maps-on-VTT matter.
- Choose one ecosystem and live with its gaps (Beyond-only, Foundry-only, theater of the mind).
- Use a thin VTT (Owlbear Rodeo) plus external character sheets.
- Pay The Forge (or similar) so the GM does not self-host Foundry.
- Play in person with paper or a shared Beyond campaign and a physical map.

### Relevant existing products or alternatives

| Layer | Examples | Pricing signal |
| --- | --- | --- |
| Character / rules | D&D Beyond, Demiplane, Pathbuilder 2e, 5e.tools (free/fan), Hero Lab | Subscriptions, book purchases, app unlocks |
| VTT | Roll20, Foundry, Fantasy Grounds, Owlbear Rodeo, Alchemy, D&D Beyond Maps/Sigil | Free–subscription or $50 license |
| Voice | Discord, Zoom, built-in VTT audio | Usually free Discord |
| Hosting | The Forge, other Foundry hosts | Monthly hosting on top of the Foundry license |
| Glue | Beyond20, DDB-Importer, Pathmuncher | Free + Patreon |

### Evidence of dissatisfaction or inefficiency

- **Observation.** “Do I buy this book on Beyond, Roll20, or both?” is a standing consumer question, not a one-off.
- **Observation.** Foundry’s learning curve and hosting friction are the most repeated complaints in reviews; they are also the reason a hosting industry exists.
- **Observation.** Roll20’s free tier is usable, but features people associate with a “real” VTT (historically dynamic lighting, storage, API) sit behind Plus/Pro. Help-center feature breakdown documents paid tiers (Plus and Pro; Pro listed at $10.99/mo or $109.99/yr in Roll20 help content retrieved in this research). ([help.roll20.net](https://help.roll20.net/hc/en-us/articles/360037774633-Feature-Breakdown))
- **Inference.** Community importers persist because official platforms benefit from lock-in; the workaround is popular and legally/ToS-fragile.

### Counter-evidence (possible adequate solutions)

- Many groups are satisfied inside one ecosystem.
- Owlbear Rodeo (and similar lightweight VTTs) already exist for groups that found Roll20/Foundry too much.
- Foundry + DDB-Importer is “good enough” for technically comfortable GMs.
- D&D Beyond Maps / Sigil is Hasbro’s attempt to collapse the stack for 5e. If it improves, the gap narrows.
- **Legal/ToS risk:** unofficial importers may be restricted. A business that depends on scraping or cookie-based import would inherit that risk.

### Do people appear to spend money in this category?

**Yes — this is the strongest digital-spending category found.** D&D Beyond was acquired for $146.3 million; it sells subscriptions and digital books. Roll20 sells subscriptions and marketplace modules. Foundry sells licenses. Foundry hosts sell monthly plans. Glue-tool authors earn Patreon income. Players and GMs already pay, sometimes twice for the same adventure.

### Important unknowns

- How many groups still run a multi-tool stack versus a single platform in 2026, after D&D Beyond Maps/Sigil.
- How much of the spend is “tax of lock-in” versus perceived value.
- Switching costs (libraries of purchased books) and whether they prevent new entrants.
- Licensing feasibility for a small company (WotC, Paizo, and VTT platform rules).
- Whether improving first-party VTTs will close the gap before a new product could matter.

### Initial confidence

**High** that fragmentation and lock-in are real, recurring, and already monetized.  
**High** that incumbents are strong and licensing is a hard constraint.  
**Moderate** that a small company could legally and practically improve the “glue” layer without becoming a ToS-dependent importer.

---

## Problem 5 — Players struggle to operate characters and rules during play

### Who experiences the problem

**Players**, especially new and returning players, and anyone playing a spell-heavy or feat-heavy class.  
**GMs**, who become the table’s lookup service.  
Present in D&D 5e and, from forum evidence, Pathfinder 2e (more options, more lookup).

### What they are trying to accomplish

On their turn, know what they can do, roll the correct numbers, and apply the correct rule — without rereading a book or scrolling a dense sheet while others wait.

### Evidence that the problem exists

- **Observation.** Character-sheet complexity is a standing onboarding complaint. Simplified fan sheets exist specifically because new players are told to ignore sections of the official sheet. ([gamerant.com on a simplified 5e sheet](https://gamerant.com/dungeons-and-dragons-simple-character-sheet-new-player-friendly/))
- **Observation.** GMs publish guidance for “when players forget their abilities,” “when players don’t read the rules,” and mid-combat PHB lookups. The recommended workaround is often index cards with *final* modifiers, not formulas. That is a manual information-design fix.
- **Observation.** Learn-to-play GMs still ask for “new player packets” because official materials are either too long or too class-specific. ([r/DMToolkit discussion](https://reddit.synth.download/r/DMToolkit/comments/1um2cdo/new_player_pack_assistance/))
- **Fact.** Pathfinder players on Demiplane’s own forum described the official digital builder as too slow and too hard for new players compared with Pathbuilder; the group chose not to use the official tool for the next campaign. ([forums.demiplane.com](https://forums.demiplane.com/t/why-my-players-have-decided-to-not-use-demiplane-in-our-next-campaign/4663))
- **Observation.** Combat-tracker apps (Improved Initiative, D&D Beyond combat tracker, Encounter+, Game Master 5 / Fight Club 5, VTT combat UI) exist because live-state tracking (initiative, HP, conditions, concentration) is error-prone on paper and split across player sheets.

**Inference.** The player-facing problem is cognitive load and information design. The GM-facing problem is that player confusion becomes GM labor and slower combat.

### How people currently solve it

- D&D Beyond (or Pathbuilder / Demiplane) so the sheet calculates bonuses.
- Pre-generated characters for session one.
- Index cards and one-page cheat sheets.
- GM or another player coaching on turns.
- Choosing simpler systems (OTT, Mausritter, Dungeon World, etc.) or theater of the mind.
- VTT automation (especially Foundry + system modules) so clicking a feature rolls the right dice.
- Phone apps for spell lists and initiative.

### Relevant existing products or alternatives

| Product | Job | Notes |
| --- | --- | --- |
| D&D Beyond character builder / app | Official 5e sheet + rules lookup | Widely used; content gated by purchases/sharing |
| Pathbuilder 2e | PF2e character builder | Often preferred to official tools |
| Demiplane / Pathfinder Nexus | Official PF digital books + sheet | Complaints about UX and speed |
| Foundry system sheets | In-play automation | High setup; strong once configured |
| Improved Initiative, Encounter+, etc. | Combat state | Another window in the stack |
| Fan simplified sheets / 5e.tools | Lower friction / free rules | Licensing and completeness vary |

### Evidence of dissatisfaction or inefficiency

- **Observation.** Even with D&D Beyond, GMs still report players who do not know their features. A calculated sheet does not equal an operable sheet.
- **Observation.** Official digital tools can still lose to a hobby app (Pathbuilder) on usability. That is evidence that “an official app exists” does not mean the problem is solved.
- **Observation.** Combat slowing down while someone searches a spell text is one of the most common table-feel complaints in GM advice writing.

### Counter-evidence (possible adequate solutions)

- D&D Beyond is, for many 5e tables, a satisfactory character solution. Hasbro’s “3 of 4 hobby RPG gamers reached” claim, even if survey-biased, shows very wide distribution.
- Foundry automation is considered excellent for PF2e by a large share of that community; some groups treat Foundry as the default way to *make the system playable*.
- Simpler TTRPG systems exist; players who hate rules complexity can switch games.
- **Speculation.** General-purpose AI at the table (“what can I do this turn?”) may become a default lookup layer and commoditize dedicated helpers.

### Do people appear to spend money in this category?

**Yes.** D&D Beyond subscriptions and book unlocks, Pathbuilder paid unlocks, Hero Lab, phone apps, and VTT licenses are all character/rules-operation spend. Content *sharing* (D&D Beyond Master Tier) exists because players need books they did not buy in order to build legal characters.

### Important unknowns

- How much of the remaining pain is “new player’s first five sessions” versus a lifelong problem.
- Whether tables that still struggle are ones that refused digital tools, or ones that use them and still stall.
- Difference in severity between 5e, PF2e, and rules-light games.
- Whether players would pay for a helper, or expect the GM / publisher to provide it free.

### Initial confidence

**High** that rules/character operability is a recurring table problem, especially for new players and crunchy systems.  
**Moderate** that D&D 5e is already well served digitally.  
**Moderate** that PF2e and mixed-system / homebrew tables still feel a gap.  
**Low** that this is underserved enough to be a Stage 2 opportunity without more segmentation.

---

## Problems Noticed but Not Selected as Top Five

These appeared in sources but were weaker, narrower, or less clearly unsolved:

| Problem | Why not in the top five |
| --- | --- |
| Battle-map and token production | Real time sink and real spend (Inkarnate, Dungeon Alchemist, DungeonDraft, Patreon map creators, Dwarven Forge). Also many adequate paid tools already. Overlaps Problem 1. |
| Homebrew / third-party content legality after OGL-era distrust | Important historically; more of a publisher/platform risk than a weekly user workflow. |
| Audio/video quality for online play | Mostly solved by Discord; complaints are generic remote-work issues. |
| Inventory and loot tracking | Common annoyance; less evidence of severity or spend than the five above. |
| Encounter balance math | Real, but heavily covered by Kobold Fight Club, Beyond, and published adventures. |

---

## Cross-Cutting Counter-Evidence

Before treating any of the five as a company opportunity, the following arguments apply to **all** of them:

1. **The hobby already has a lot of software.** D&D Beyond, Roll20, Foundry, Pathbuilder, World Anvil, Kanka, Owlbear Rodeo, StartPlaying, and dozens of smaller apps exist. Absence of a tool is not the pattern. Fragmentation and misfit are the pattern.
2. **Complaints are not willingness to pay.** Most public complaints come from hobbyists who expect core play to be free among friends.
3. **Social problems masquerade as software problems.** Scheduling, flakes, and “nobody wants to GM” may not yield to another app.
4. **Incumbents can add the missing feature.** Hasbro, Roll20, Foundry, and Paizo/Demiplane can absorb many adjacent features.
5. **AI commoditization risk is high** for generation tasks (NPCs, recaps, prep text, “what can I do this turn?”). It is lower for workflow, hosting, licensed content libraries, and trusted marketplaces.
6. **D&D-centric evidence may overstate the general TTRPG case.** Rules-light and indie-game tables often have milder versions of Problems 1, 4, and 5.

---

## Unknowns That Limited This Research

- No first-party customer interviews (outside authority).
- No paid market reports, app-store scrape, or search-volume tools (would require accounts or spend).
- Reddit and some pricing pages were blocked or Cloudflare-gated from this environment; some community-size figures could not be confirmed from primary JSON/API.
- No reliable split of in-person versus online play in 2026.
- No reliable count of *active* (not registered) D&D Beyond users or paying subscribers.
- Owner Fit was not scored. Owner context documents TTRPG interest and prior TTRPG software exploration; per company rules, interest is not evidence of an opportunity.
- Geographic market preference is undocumented.

---

## Analyst Recommendation

This is a recommendation for **additional research only**. It is not a recommendation to build, validate experimentally, or invest.

### Research next: Problem 2 (reliable groups) and Problem 3 (campaign knowledge)

**Problem 2 — Forming and keeping a reliable play group**

Why this deserves deeper research:

- Independent survey evidence that campaigns often fail to finish, with scheduling named as the top cause.
- Experienced-GM testimony that group formation/maintenance is the hardest part of the hobby.
- The clearest *revealed* willingness to pay found in this assignment (StartPlaying per-session prices and reported payouts).
- Reachable communities already exist (LFG subreddits, Discord, StartPlaying, game stores).

What deeper research should answer:

- How much of the remaining pain is “I will pay for a seat” (possibly already served) versus “I want my friend group to stop collapsing” (possibly not software).
- StartPlaying satisfaction, retention, and gaps (quality, price, safety, non-D&D systems, in-person).
- Whether friend-group scheduling tools have any paying users or only free usage.
- Support, trust-and-safety, and marketplace operating burden — these are likely high.

**Problem 3 — Campaign knowledge capture and retrieval**

Why this deserves deeper research:

- Matches the company’s screening examples unusually well: spreadsheets, Docs, Notion schemas, Discord pins, abandoned wikis, and multiple paid products with the same complaints.
- Affects both GMs (source of truth) and players (recaps, spoiler-safe lore).
- Existing paid products appear either too heavy (World Anvil) or too generic (Docs/Notion), which is a possible gap — **or** evidence that the job will not support another product. That uncertainty is worth collapsing.
- More likely than Problem 2 to be a small-team software problem rather than a marketplace/moderation business.

What deeper research should answer:

- Actual retention: do buyers of World Anvil / LegendKeeper / Notion templates still use them at session 12?
- What query do GMs fail mid-session, in their own words.
- How many campaigns are long enough for a wiki to matter.
- Whether session-recording tools are being adopted or rejected on privacy grounds.

### Why not the other three for the next research slice

- **Problem 1 (prep time)** is well documented but may be adequately addressed by methods, published adventures, and general-purpose AI. Further research is optional after 2 and 3, not first.
- **Problem 4 (stack fragmentation)** has strong spending evidence and should be *monitored*, but licensing, ToS, and incumbent advantage make it a poor next research target until the Owner wants a legal/competitive deep dive rather than a customer-problem deep dive.
- **Problem 5 (character/rules operability)** looks partly solved for mainstream 5e. It becomes interesting again only if research focuses on a specific underserved segment (PF2e new players, in-person play, rules-light onboarding, homebrew).

---

## Overall Analyst Confidence

**Moderate-to-high** that these five problems recur and are not invented from a product idea.  
**Moderate** that the evidence mix (surveys + workarounds + paid products) is good enough for Stage 1.  
**Low** that this report, by itself, identifies a business opportunity. That is by design.

---

## Source List

Primary / official or close-to-primary:

1. https://slyflourish.com/how_long_to_prep.html  
2. https://slyflourish.com/dm_survey_results.html  
3. https://slyflourish.com/lack_of_satisfying_conclusions.html  
4. https://slyflourish.com/facebook_surveys.html  
5. https://www.dndbeyond.com/en/subscribe  
6. https://foundryvtt.com/purchase/  
7. https://foundryvtt.com/article/faq/  
8. https://www.legendkeeper.com/pricing/  
9. https://intercom.help/startplaying/en/articles/8959627-how-much-does-it-cost-to-play-on-startplaying  
10. https://rpg.stackexchange.com/questions/167291/online-dd-module-purchase-roll20-dd-beyond-or-both  
11. https://www.dndbeyond.com/forums/d-d-beyond-general/bugs-support/192725-is-it-possible-to-buy-content-on-dnd-beyond-but  
12. https://foundryvtt.com/packages/ddb-importer  
13. https://foundryvtt.com/packages/pathmuncher/  
14. https://forums.demiplane.com/t/why-my-players-have-decided-to-not-use-demiplane-in-our-next-campaign/4663  
15. https://stockanalysis.com/stocks/has/transcripts/675981-q2-2026/  
16. https://help.roll20.net/hc/en-us/articles/360037774633-Feature-Breakdown  

Industry / secondary:

17. https://www.ttrpginsider.news/p/pay-to-play-the-business-of-the-professional-dungeon-master  
18. https://www.fool.com/investing/2022/04/17/hasbro-doubles-down-on-dungeons-and-dragons/  
19. https://www.enworld.org/threads/hasbro-financial-call-3-out-of-4-d-d-players-using-beyond-with-30-million-registered-accounts.720073/  
20. https://www.worldanvil.com/pricing  
21. https://www.legendkeeper.com/best-world-anvil-alternatives/  
22. https://gamerant.com/dungeons-and-dragons-simple-character-sheet-new-player-friendly/  

Used as pointers only (vendor or tool-seller content):

23. Various World Anvil / LegendKeeper / Notion / VTT comparison blogs  
24. StartPlaying, StoryRoll, ScriptoriumGM, StormScape, Quill, and similar product blogs  

---

## Appendix — Mapping to Assignment Requirements

Each of the five problem sections includes: who; what they are trying to accomplish; evidence; current solutions; existing products; dissatisfaction/inefficiency; spending signal; unknowns; initial confidence.

This report does not include an opportunity scorecard and does not recommend product development.
