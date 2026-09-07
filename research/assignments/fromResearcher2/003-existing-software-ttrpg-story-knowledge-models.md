# 003 — Existing Software Models for TTRPG and Story Knowledge

**Researcher:** Researcher 2  
**Owner:** Jason Cameron  
**Product code name (evaluation lens only):** Mahogany  
**Date:** 2026-09-06 (America/Chicago)  
**Status:** Complete — awaiting Owner review  
**Filed by:** Researcher 2  
**Filing path:** `research/assignments/fromResearcher2/003-existing-software-ttrpg-story-knowledge-models.md`  
**Central question:** How do existing applications answer *“What belongs to the creator’s world, and what merely uses or references it?”* — ownership/containment vs association/context, and reuse without duplication.

**Evidence labels used throughout:**  
- **Verified Fact** — confirmed in official docs, product UI copy, or primary source text.  
- **Observation** — pattern visible across multiple independent sources without claiming universality.  
- **Inference** — reasoned conclusion from facts; may be wrong.  
- **Speculation** — hypothesis needing further validation.  
- **Anecdotal** — individual complaint/praise; not treated as widespread unless corroborated.

**Constraints honored:** No Mahogany schema, architecture, folder structure, Rust structs, DB tables, YAML formats, APIs, or Svelte components. No implementation recommendations. Implications only in §17.

---

## 1. Executive summary

Across TTRPG worldbuilding, general knowledge tools adapted for TTRPGs, and author/story planners, products answer the containment-vs-association question in a small number of recurring ways:

1. **Hard project/campaign containers** (Kanka, Scrivener, Fantasia Archive projects): everything *belongs to* one container; reuse across containers means copy/import and risk of divergence.  
2. **World-as-canon + campaign-as-consumer** (World Anvil): setting articles live in a world; campaigns/manuscripts *live in* the world and *link* to articles rather than owning them.  
3. **Account/library ownership + multi-project membership** (Campfire): elements can belong to a user’s library and be *added* to multiple projects — closer to association-for-reuse than containment-for-reuse.  
4. **Document/graph without strong ownership semantics** (Obsidian, LegendKeeper wiki pages): notes/pages are first-class; “belongs to campaign” is almost always a *user convention* (folders, tags, properties, plugins).  
5. **Database relations** (Notion): entities are rows; campaigns/stories relate to characters/locations via relation properties — association-first, with high schema/setup cost.  
6. **Narrative-context specialists** (Aeon Timeline; partially Plottr/World Anvil session reports): treat *appearance in an event/scene/session* as a first-class relationship distinct from the canonical entity record.

**Verified Fact / Observation:** No mainstream product cleanly solves *canonical object identity* + *story/campaign-specific state* + *cross-campaign reuse without duplication* at once. Users repeatedly invent conventions (one-write rule, master bible + copies, tags-as-campaigns, story-specific character variants).

**Local-first / portable-data lens (evaluation only):** Obsidian and Fantasia Archive score highest on post-app access; Scrivener is local but proprietary-project-bound; LegendKeeper/Kanka/World Anvil/Campfire/Notion are cloud-primary with export of varying fidelity. Export ≠ portable working source in most cloud products (**Observation**).

---

## 2. Products investigated and why selected

| Product | Category | Why selected |
|--------|----------|--------------|
| **World Anvil** | TTRPG / worldbuilding + campaign + novel | Market leader for structured wiki + campaign manager; explicit world↔campaign split |
| **LegendKeeper** | TTRPG / worldbuilding | Wiki-first GM tool; boards for visual relationships; offline sync claims |
| **Kanka** | TTRPG / worldbuilding | Entity-module campaign model; public docs on nesting, connections, no cross-campaign sync |
| **Campfire** | Author/story + worldbuilding | Element Library + project linking; dual story/world modules |
| **Fantasia Archive** | Offline worldbuilding | Hierarchy + typed two-way relations; local/offline philosophy |
| **Obsidian** | General knowledge → TTRPG | Community TTRPG vaults/plugins; file-ownership extreme; friction rich |
| **Notion** | General knowledge → TTRPG | Relation/rollup entity graphs; template marketplace for campaigns |
| **Scrivener** | Author/story | Binder hierarchy; series-bible practice; sealed projects |
| **Aeon Timeline** | Author/story (entity+time) | Characters/locations as items related to events — narrative context |
| **Plottr** | Author/story | Series bible; characters/places across books; scene linking |

**Also sampled (lighter):** Obsidian community plugins (RPG Manager, TTRPG Campaign Manager, Storyteller Suite, nested/multi-vault tools); World Anvil Academy “one-write rule”; Loreteller category guidance; Trustpilot/RPGnet/forum threads for friction; Realm Works only as historical note (legacy, not deeply investigated).

**Sources preference:** Official docs and product pages for “how the product models info”; Reddit/forums/GitHub/community for friction. Paywalled/admin-only systems avoided.

---

## 3. Fundamental concepts per product

### 3.1 Quick comparison table

| Product | First-class objects | Soft / user-defined objects | Primary container | Primary association mechanism |
|---------|---------------------|-----------------------------|-------------------|-------------------------------|
| World Anvil | Articles (typed templates), maps, timelines, campaigns, manuscripts | Categories, tags, custom fields (limited) | **World** | @mentions, template relationship fields |
| LegendKeeper | Wiki pages/elements, maps, boards | Tags, properties, templates, folders | **Project** | [[links]] / @mentions, board arrows |
| Kanka | Module entities (Character, Location, Org, Quest, …) | Tags, properties, property kits, custom categories (premium) | **Campaign** (= world/universe) | Mentions, connections (mirrored), parent nesting |
| Campfire | Elements (characters, locations, chapters, …) with panels | Templates, nested folders, tags | **Project** (+ Element Library) | Links / @ smart links, relationship webs |
| Fantasia Archive | Typed documents (Characters, Locations, Events, Chapters, …) | Nested docs as categories, tags | **Project** | Typed two-way relation fields |
| Obsidian | Notes (files) | Frontmatter, tags, folders, Bases/Dataview, plugins | **Vault** (filesystem) | Wikilinks, embeds, metadata |
| Notion | Database pages / blocks | Properties, relations, rollups, templates | **Workspace / page tree** | Relation properties, mentions |
| Scrivener | Binder documents/folders | Labels, keywords, custom metadata, templates | **Project (.scriv)** | Document links, keywords (weak) |
| Aeon Timeline | Events, narrative items, characters, locations, arcs | Custom item types, properties | **Timeline file** | Relationships to events |
| Plottr | Books, scenes, characters, places, notes, tags | Custom attributes, templates | **Project / Series** | Scene tags/links; family trees |

### 3.2 Product notes (evidence-tagged)

**World Anvil** — **Verified Fact:** Articles are the core of the setting; campaigns and manuscripts “live” in a world and connect to articles/maps/timelines ([Beginner tutorials](https://www.worldanvil.com/learn/beginner-tutorials/get-started-articles)). Templates define typed relationship slots (e.g., character parents, org leader) ([Article templates](https://www.worldanvil.com/learn/article-guides/article-templates) — content corroborated via search/KB summaries). Campaign Manager can create NPCs that become world character articles, or link existing ones ([Campaign Manager guide](https://www.worldanvil.com/learn/rpg/campaign-manager)).

**LegendKeeper** — **Verified Fact:** Writing-focused wiki with auto-linking, tags & properties, templates; Boards place page cards and arrows for relationship charts ([Boards announcement](https://www.legendkeeper.com/boards-announcement/)). Team has stated Boards are not a substitute for a future dedicated relationship-graph system (**Verified Fact** from [LK Weekly](https://www.legendkeeper.com/lk-weekly-surprise-feature-announcement-for-those-who-color-outside-the-lines/)).

**Kanka** — **Verified Fact:** “A campaign, also known as a world or a universe, is the way data is stored in Kanka. Everything belongs to a campaign” ([Campaign settings docs](https://docs.kanka.io/en/latest/features/campaigns/campaign-settings.html)). Mentions via `@`; connections (formerly relations) with mirroring; nesting via parent for most types except Characters/Items ([References blog](https://blog.kanka.io/2021/07/26/how-to-use-references-kanka/), [Nested entries](https://docs.kanka.io/en/latest/features/nested.html), [Connections](https://docs.kanka.io/en/latest/features/connections.html)). **Verified Fact:** No sync across campaigns ([KB](https://kanka.io/kb)).

**Campfire** — **Verified Fact:** Projects contain elements; Element Library holds elements across projects; “Add to Project” shares elements into another project ([FAQ](https://campfirewriting.com/faq); Library tutorial/video descriptions). Editors creating elements choose whether ownership is their account or the project owner’s library. Project linking for series/same-world projects ([Project linking tutorial](https://campfirewriting.com/learn/project-linking-tutorial)).

**Fantasia Archive** — **Verified Fact / Observation (secondary review):** Offline hierarchical document DB; hard-coded top-level document types; documents nest infinitely; typed two-way relationships (e.g., friend links update both sides); project export/import ([CartographyAssets feature list](https://cartographyassets.com/assets/10089/fantasia-archive/); [Koen Martens review](https://koenmartens.nl/20210425-world-building-with-fantasia-archive.html)).

**Obsidian** — **Verified Fact:** Notes are Markdown files; links are associations; structure is user-defined. Community plugins invent campaign/entity models (e.g., [RPG Manager](https://github.com/carlonicora/obsidian-rpg-manager) assets reusable across campaigns via relationships; [TTRPG Campaign Manager](https://community.obsidian.md/plugins/ttrpg-campaign-manager)).

**Notion** — **Verified Fact:** Databases + Relation/Rollup properties form an object graph ([community analyses](https://www.resumelens.org/blog/notion/notion-relations-and-rollups); TTRPG templates such as [RPG Campaign template](https://www.notion.com/templates/rpg-campaign)). Mentions create backlinks; many GMs add explicit Relations for session notes ↔ NPCs ([DMCG worldbuilding](https://www.dmcgdesign.com/blog/worldbuilding-in-notion)).

**Scrivener** — **Verified Fact:** Projects are self-contained; no native live-shared document across projects ([Literature & Latte forums](https://forum.literatureandlatte.com/t/sharing-a-document-between-projects/145434)). Series-bible pattern: one project or master research project + copy/bookmark ([Writer Unboxed](https://writerunboxed.com/2021/08/13/scrivener-scenario-creating-a-series-bible/); [Copy between projects](https://www.literatureandlatte.com/blog/how-to-copy-items-between-scrivener-projects)).

**Aeon Timeline** — **Verified Fact:** Sync maps Scrivener docs to events; characters/locations sync from folders; *relationships* (who appears in which event) sync as keywords or custom metadata ([Aeon Scrivener sync](https://www.aeontimeline.com/guides/sync-with-scrivener)).

**Plottr** — **Verified Fact:** Characters/places/notes live at project/series level and can be filtered by book and linked to scenes; Series View for continuity; Family Tree for visual relationships not tied to a single book ([Plottr series bible](https://plottr.com/series-bible-software/); [Series View docs](https://docs.plottr.com/article/65-timeline-series-view)).

---

## 4. Containment vs association approaches

Central distinction operationalized:

- **Containment:** A has exclusive or primary ownership of B (B “belongs to” A; deleting/moving A affects B’s home).  
- **Association:** A references B; B may exist independently and appear in many contexts.

### 4.1 Containment-dominant

| Approach | Products | Consequence |
|----------|----------|-------------|
| Campaign owns all entities | **Kanka** | Reuse across campaigns = copy → duplicates. Official advice: one campaign + tags/roles (**Verified Fact**, [KB](https://kanka.io/kb)). |
| Project owns binder tree | **Scrivener** | Cross-book character is either duplicated or kept only in a master project. |
| Project owns documents | **Fantasia Archive**, **LegendKeeper** (project scope) | Export/import or copy to move worlds; identity is project-scoped. |
| Folder/parent nesting | **Kanka** (same-type parent), **Fantasia Archive**, **Campfire** folders, **Obsidian** folders | Good for geography (“city in kingdom”); fails for multi-parent membership (**Observation**). |

### 4.2 Association-dominant

| Approach | Products | Consequence |
|----------|----------|-------------|
| Mentions / wiki links | WA, LK, Kanka, Campfire, Obsidian | Cheap association; often no typed semantics; discovery via backlinks/search varies. |
| Typed template fields | World Anvil, Fantasia Archive | Stronger semantics + often bidirectional; limited extensibility (WA community request for custom relationship slots — [suggestion](https://www.worldanvil.com/community/voting/suggestion/47977b49-63a8-44d4-a113-ae7ceb5c35a1/view)). |
| Connections / relations | Kanka connections, Notion relations, Campfire relationship webs | User-defined labels; optional mirroring; attributes on edges vary. |
| Visual boards / trees | LK Boards, Plottr Family Tree, Kanka connection map (premium) | Association as diagram; may not be queryable as data (**Inference** for LK Boards). |
| Library multi-membership | **Campfire** Add to Project | Element can appear in multiple projects without being “owned by” only one story (**Verified Fact** via FAQ/Library behavior). |
| World articles ↔ campaigns | **World Anvil** | Campaign *uses* world articles (primer, NPC link); articles are not children of the campaign (**Verified Fact**). |

### 4.3 Hybrid patterns (most common in practice)

**Observation:** Successful setups usually combine:

1. A **hard outer container** (world, vault, campaign, series project) for permissions, search scope, and billing.  
2. **Association inside** that container for characters↔locations↔factions.  
3. **Hierarchy only where ontology is tree-shaped** (geography, org charts), not for “appears in.”

**World Anvil’s split** is the clearest published answer to the central question: *the world owns canon articles; the campaign references them.* Kanka collapses “world” and “campaign” into one container, then uses tags/permissions to fake multi-campaign association.

---

## 5. Cross-campaign / cross-story reuse

| Product | Native reuse without duplication? | Typical workaround | Duplication/update problem |
|---------|-----------------------------------|--------------------|----------------------------|
| World Anvil | Within one world: yes (link). Across worlds: limited | One world, multiple campaigns; or copy articles | Multi-world forks diverge (**Inference**) |
| Kanka | **No** sync across campaigns (**Verified Fact**) | Single campaign + tags/roles; bulk copy | Copies create new IDs; re-import duplicates ([Import docs](https://docs.kanka.io/en/latest/features/campaigns/import.html)) |
| LegendKeeper | Within project: links. Across projects: export/import | Partial MD export → Obsidian | Partial export loses maps/boards/properties ([Changelog 0.16.1](https://www.legendkeeper.com/changelog/legendkeeper-0-16-1-0/)) |
| Campfire | **Yes** — Library Add to Project / linked projects | Library as shared pool | Ownership/subscription tied to library owner (**Verified Fact**, FAQ); nested timeline elements may require whole-project share (**Observation** from Library video) |
| Fantasia Archive | Within project: relations. Across: export/import project | One big project | Project switching clunky; DB not user-file-native (**Observation**, Martens) |
| Obsidian | Yes if single vault + links | Multi-vault plugins, Folder Bridge, nested vaults | File can’t live in two folders; story-specific variants proliferate ([Forum Apr 2026](https://forum.obsidian.md/t/linking-or-redirecting-to-a-base-note-from-multiple-directories/113158)) |
| Notion | Relations across DBs in one workspace | Duplicate workspace/template for new campaign | Relation performance; schema drift (**Observation**) |
| Scrivener | No live share | Series bible project; Copy to Project; bookmarks | Stale copies; path-fragile links (**Verified Fact**, forums) |
| Aeon Timeline | Characters shared across events in one timeline | Sync with Scrivener folders | Two-app sync complexity |
| Plottr | Characters/places at series level | Filter by book | Series View doesn’t auto-populate from book timelines (**Verified Fact**, docs limitations) |

**Pattern (Observation):** Products that equate *campaign* with *data universe* (Kanka) force either mega-campaigns or duplication. Products that separate *canon world* from *play/story instance* (World Anvil; Campfire library; Plottr series) handle reuse better — but still struggle with *instance-specific state* (see §7).

---

## 6. Relationship modeling

| Dimension | Strong examples | Weak / absent examples |
|-----------|-----------------|------------------------|
| **Typed vs generic** | WA templates; FA field types; Aeon relationship types; Kanka connection labels | Obsidian bare `[[links]]`; LK board arrows (visual) |
| **Direction + inverses** | FA two-way auto; Kanka mirrored connections with different labels per side; WA relationship panels | Notion optional bidirectional (costly if overused); Scrivener keywords |
| **User-definable types** | Kanka free-text connections; Notion relations; Campfire webs; Plottr family tree editor | WA: custom article relationship slots requested, not fully general (**Verified Fact**, community suggestion) |
| **Edge attributes** | Character relationship detail panels (WA); Notion relation is mostly identity + rollups | Many systems: label only, no “since year X” on the edge without a third object |
| **Context/time-dependent** | Aeon (character↔event); session reports linking interacted characters (WA); Plottr scene↔character | Most wikis store “lives in City” as eternal fact on the character |

**Inference:** Systems optimize for *stable world facts* (born in, member of) more than *time-bounded or story-bounded* relations. Time-bounded relations are often smuggled into prose, session notes, or timeline events.

---

## 7. Canonical object vs narrative-context handling *(critical)*

### 7.1 Definitions used here

- **Canonical object:** The durable identity and facts of an entity in the creator’s world (who Mira is).  
- **Narrative context / appearance state:** How that entity appears in a specific story, campaign, session, or scene (Mira in Session 12 is wounded and allied with the PCs; Mira in Book 2 is a child).

### 7.2 How products handle the split

| Product | Canonical model | Narrative-context model | Gap |
|---------|-----------------|-------------------------|-----|
| World Anvil | Character/location articles in world | Session reports; scrapbooks; campaign NPC instances linked to articles; plot trees | Easy to overwrite canon with play state; no first-class “appearance record” (**Inference**) |
| Kanka | Entity pages | Journals, quests, calendars, posts on entities; mentions in session-like notes | Mentions not in “Related elements” list (**Verified Fact**, connections docs) — weak appearance discovery |
| LegendKeeper | Wiki pages | Boards, session pages (user convention), player visibility | No dedicated appearance object (**Observation**) |
| Campfire | Character/location elements | Chapters/manuscript; timeline; links panels | Element is shared; story-specific deltas unclear without duplicate elements (**Inference**) |
| Fantasia Archive | Documents + relations | Events as documents linked to characters | Stronger than most for “who was at event” (Martens example) |
| Obsidian | Character note | Session notes with wikilinks; optional MOCs; plugins with session logs | Users invent “Story!Character” variants; graph duplicates from transclusion (**Anecdotal→pattern** on forums) |
| Notion | Character DB row | Session/Notes DB with relations/mentions | Works if discipline maintained; high maintenance (**Observation**) |
| Scrivener | Character sheet in Research | Scene docs in Draft; keywords | No structured “appears in”; search/binder browsing |
| Aeon Timeline | Character/location items | **Events with relationships** | Best explicit separation among surveyed tools (**Verified Fact** sync model) |
| Plottr | Series-level character/place | Scene cards tagged with characters/places | Good for fiction outlining; less for mutable RPG live state |

### 7.3 Community “solutions” (not product features)

1. **One-write rule** — World Anvil Academy: one canonical article; everything else links, never copies ([WA Academy](https://academy.worldanvil.com/blog/dnd-campaign-wiki-lore-management)). **Verified Fact** as published guidance; **Observation** that discipline fails under time pressure.  
2. **Promote from session → wiki** — Write ephemeral notes; only promote stable facts to canon (**Inference** / common GM advice pattern).  
3. **Variant notes** — Separate files per story version of a character (Obsidian fanfic forum thread). Solves narrative context by *abandoning single identity*.  
4. **Tags as campaign membership** — Kanka/Obsidian: `campaign:A` tag on entity. Association, but doesn’t store per-campaign state.  
5. **Plugin assets** — Obsidian RPG Manager v4: assets not part of a single campaign; add relationship to reuse (**Verified Fact**, GitHub README).

**Conclusion for §7:** Existing apps mostly store **one mutable canon blob**. Narrative context is secondary (notes, events, tags). The hardest unsolved case is: *same identity, different simultaneous contexts* (two active campaigns; AU vs canon; PC vs world-article view) without duplication or silent overwrite.

---

## 8. Hierarchy approaches

| Where hierarchy works | Products | Why |
|----------------------|----------|-----|
| Geography drill-down | Kanka locations, FA nesting, Campfire location folders, WA categories | Real-world mereology is tree-ish |
| Org charts / family trees | WA org charts & family trees; Plottr family tree; FA relations | Directed trees/DAGs with clear roots |
| Manuscript structure | Scrivener binder; Campfire chapters; Aeon narrative hierarchy | Writing order is hierarchical |
| Wiki taxonomy | WA categories; LK directories | Navigation IA |

| Where hierarchy fails | Why | What users do instead |
|----------------------|-----|------------------------|
| Character “belongs under” one faction | Characters have multiple affiliations | Tags, connections, links |
| Campaign contains characters exclusively | Same NPC in West Marches + one-shot | Association or mega-container |
| Story version inside folder taxonomy | Obsidian: one file, one path | Transclusion, aliases, duplicate notes |
| Cross-cutting themes | “All curses,” “all rivers” | Tags, Dataview/Bases, Notion views |

**Kanka Verified Fact:** Characters and Items cannot have parent entities ([References blog](https://blog.kanka.io/2021/07/26/how-to-use-references-kanka/)) — product explicitly refuses hierarchy for those types.

**Loreteller guidance (Observation):** Categories = identity (“what is this”); tags = connections (“what else is this tied to”) ([Loreteller WA categories](https://loreteller.com/learn/world-anvil-categories/)).

---

## 9. Search and discovery

Questions users actually ask (from docs, templates, forums):

1. Where has this character appeared?  
2. What is in this location / who is here now?  
3. What is unused / orphaned?  
4. What did we do last session?

| Product | Appearance / backlink discovery | Structural search | Unused/orphan support |
|---------|--------------------------------|-------------------|------------------------|
| World Anvil | Mentions, template reverse fields, search | Category browse, maps | TODO list for unwritten links; limited orphan analytics (**Observation**) |
| Kanka | Connections + Related elements; mentions **excluded** from Related (**Verified Fact**) | Filters, nested lists, tags, bookmarks | Filters for empty fields (`!!`) |
| LegendKeeper | Full-text search; auto-links; boards | Tags/properties, directory | Unknown / weak publicly documented |
| Campfire | Links panels bidirectional when present | Library search, module filters | Library unassigned after project delete (**FAQ**) |
| Fantasia Archive | Relation-aware search (review claim) | Hierarchy + property query | Not documented deeply |
| Obsidian | Backlinks, graph, Omnisearch, Dataview/Bases | Folders, tags, properties | Community scripts; orphan plugins |
| Notion | Linked views, relations, rollups | Database filters | Manual; performance limits discovery UX |
| Scrivener | Project search | Binder, collections, keywords | Manual |
| Aeon Timeline | Filter by entity on timeline | Item lists | Gaps visible on timeline |
| Plottr | Filter characters/places/notes by book/tag | Series/book views | Manual |

**Gap (Observation):** “Where appeared in sessions?” is poorly first-class except where session notes systematically relation-link entities (Notion discipline; Aeon events; some WA session report fields). Kanka’s exclusion of mentions from Related elements is a concrete product gap for appearance tracking.

---

## 10. User organizational burden

| Burden type | High in | Notes |
|-------------|---------|-------|
| Upfront schema/templates | Notion, World Anvil (prompt-heavy templates), Campfire panels | WA can feel “chiding” for incomplete worlds (**Anecdotal**, [RPGnet](https://forum.rpg.net/index.php?threads/worldanvil-thoughts-now-that-it-has-been-out-for-a-while.902656/)) |
| Plugin/stack assembly | Obsidian | Power + decision fatigue; vault restructures costly |
| Category/taxonomy maintenance | WA, LK, Obsidian folders | Restructuring articles/categories is recurring friction (**Observation**) |
| Permission/tag gymnastics | Kanka multi-group-in-one-campaign | Official workaround for no cross-campaign sync |
| Relation hygiene | Notion | Bidirectional clutter; relation dropdown slow at scale ([performance writeups](https://wisechecker.com/notion-relation-search-performance-large-databases/)) |
| Dual-tool sync | Scrivener + Aeon | Setup and conflict management |
| Template marketplace dependence | Notion TTRPG templates | “Build from scratch” estimated 8–15 hours (**Anecdotal/marketing**, [Minva](https://minvarpg.com/blogs/ttrpg/notion-dnd-campaign-planner)) |

**Obsidian/Notion specifically:** Both shift modeling work onto the user. Obsidian’s cost is *convention + plugins*; Notion’s cost is *database schema + performance*. Neither encodes TTRPG containment semantics by default.

---

## 11. Data ownership and portability

| Product | Storage model | Export | Portable working source? | Git-friendly? |
|---------|---------------|--------|--------------------------|---------------|
| Obsidian | Local MD vault | N/A (files *are* source) | **Yes** | **Yes** |
| Fantasia Archive | Local project DB + export dir | Export/import project (JSON bundle per reviews) | Partial | Limited |
| Scrivener | Local `.scriv` package | Compile; copy; not open wiki | Local yes; open interchange weak | Poor |
| LegendKeeper | Cloud + offline cache | LK format (complete-ish), HTML, partial MD/JSON ([changelog](https://www.legendkeeper.com/changelog/legendkeeper-0-16-1-0/)) | MD export partial | Partial after MD export |
| Kanka | Cloud (self-host free tier possible) | JSON (re-importable) or Markdown (not re-importable) daily ([export docs](https://docs.kanka.io/en/latest/features/campaigns/export.html)) | JSON is backup/migration, not daily editing format | No |
| World Anvil | Cloud | World/article export (HTML/CSV/JSON tooling; guild tiers) | Export ≠ editable portable wiki; lock-in complaints (**Anecdotal widespread pattern** on Trustpilot/community votes) | No |
| Campfire | Cloud | Element/project export (HTML etc. mentioned in import guides) | Cloud-primary | No |
| Notion | Cloud | Markdown/CSV/HTML export | Relations/views degrade | No |
| Aeon Timeline | Local file | CSV; share read-only | Local yes | Limited |
| Plottr | Local/cloud options (product-dependent) | Word/Scrivener export | Outline-centric | Limited |

**Local-first lens:** Obsidian is the reference for “post-app access.” Cloud wikis offer collaboration and structured templates but treat export as *escape hatch*, not *source of truth* (**Observation**). Kanka’s open source + export is stronger than WA on transparency; self-host is explicitly not production-supported (**Verified Fact**, [self-hosting docs](https://docs.kanka.io/en/latest/self-hosting.html)).

---

## 12. Major user-reported friction

Distinguished carefully:

### Widespread patterns (multiple independent channels)

1. **Cloud lock-in / export fidelity** — WA Trustpilot and community votes on usable export; LK partial MD export acknowledges missing maps/boards/properties; Notion export loses relational UX.  
2. **Cross-campaign reuse** — Kanka official “we don’t sync”; users pushed into mega-campaigns.  
3. **Organizational overwhelm** — WA template depth; Notion schema complexity/performance; Obsidian “how should I structure my vault?” endless threads.  
4. **Canon vs session drift** — Duplicated NPC info across session notes and wiki; one-write rule exists because the failure mode is common.  
5. **Hierarchy vs multi-belonging** — Obsidian forum: cannot place one note in two folders for story vs character organization.

### Anecdotal (treat as signals, not prevalence)

- WA free-tier article limits “holding work hostage” (Trustpilot).  
- WA reliability/lost notes during sessions (Trustpilot).  
- WA “too much worldbuilding, not enough for running a game” (RPGnet).  
- Fantasia Archive early bugs/Electron hunger (2021 review; may be dated).  
- Scrivener users wanting live cross-project character sheets (forums; feature not present).

---

## 13. Comparative product philosophy analysis

| Philosophy | Exemplars | Strengths for TTRPG+story | Weaknesses |
|------------|-----------|---------------------------|------------|
| **Document / wiki-centric** | LegendKeeper, WA articles, Obsidian | Fast writing; gradual structure; human-readable | Weak typed reuse; relationships ad hoc |
| **Hierarchy-centric** | Scrivener binder, FA tree, folder vaults | Excellent for geography & manuscripts | Multi-parent & cross-cutting fail |
| **Entity / module-centric** | Kanka, WA templates, Campfire modules | Consistent object types; RPG-shaped | Rigid modules; campaign-as-universe lock |
| **Graph / relation-centric** | Notion relations, Kanka connections, Obsidian links | Flexible association; discovery via links | Cognitive + performance cost; edge attributes thin |
| **Database-centric** | Notion, Kanka properties, Campfire attributes | Queryable facts; views | Schema burden; migration pain |
| **User-defined-centric** | Obsidian, Notion | Fits any ontology | No shared defaults; reinventing the wheel |
| **Narrative-timeline-centric** | Aeon, Plottr, WA timelines | Appearance-in-time natural | Weaker as full world encyclopedia |

**Inference:** TTRPG+story needs *at least* entity identity, association, and narrative appearance. Most products pick two and fake the third with prose or process.

---

## 14. Patterns that appear successful

1. **Separate canon container from play/story container** (WA world vs campaign; Plottr series vs book; Campfire library vs project).  
2. **One-write / single source of truth** for entity facts, with links outward.  
3. **Association for people; hierarchy for places** (Kanka: no character parents; location parents OK).  
4. **Events/scenes as the place to hang appearance** (Aeon relationships; session note relations in Notion).  
5. **Tags for cross-cutting membership** when hierarchy can’t express it.  
6. **Mirrored/inverse relationships** to avoid double maintenance (FA, Kanka mirrors, WA panels).  
7. **Local files as source of truth** when portability matters (Obsidian).  
8. **Library-style multi-project membership** for reuse without fork (Campfire).

---

## 15. Patterns that appear problematic

1. **Equating campaign with entire data universe** without sync (Kanka) → duplication or permission spaghetti.  
2. **Copy/import as “reuse”** → silent divergence (Scrivener, Kanka import duplicates).  
3. **Overloading the canonical record with live play state** → lost history / wrong “current” facts.  
4. **Hierarchy as general organization** for multi-belonging entities.  
5. **Visual-only relationships** (boards) that aren’t searchable as structured data.  
6. **Export as afterthought** — partial exports, HTML soup, JSON only useful inside same app.  
7. **Unbounded Notion relation graphs** — performance and schema opacity.  
8. **Prompt-maximal templates** that inflate empty fields and intimidate users who need “good enough for tonight’s game.”

---

## 16. Problems existing products do not solve well

1. **Same entity, multiple concurrent narrative contexts** with divergent state, without duplication.  
2. **Reuse across campaigns/worlds with update propagation** (true shared instances).  
3. **First-class appearance history** (“every session/scene this NPC entered”) as queryable structure.  
4. **Time-varying relationships** as data (alliances by era) without timeline gymnastics.  
5. **Portable structured source** that remains fully editable outside the vendor app *and* preserves relations/maps.  
6. **Low-burden defaults** that still encode containment vs association clearly for TTRPG newcomers.  
7. **Orphan/unused detection** across large worlds as a standard feature.  
8. **Player-facing vs creator-facing views of the same object** without maintaining two records (partially solved by permissions/secrets, not by context layers).

---

## 17. Implications worth considering during Mahogany domain modeling

*(Implications only — not schema or architecture.)*

1. **Treat “belongs to” and “appears in / references” as different questions** — products that collapse them pay later in duplication or mega-containers.  
2. **Expect users to run multiple stories/campaigns against one creative world** — evaluate any model against that load case.  
3. **Canonical identity vs contextual state is a primary design tension** — session play mutates “current truth”; novels need variant truths; both are normal.  
4. **Hierarchy is a specialized tool, not a universal organizer** — especially weak for characters and cross-cutting sets.  
5. **Reuse mechanisms should clarify whether instances are shared or forked** — Campfire-style membership vs Kanka-style copy.  
6. **Discovery of appearances matters as much as editing entities** — mention/backlink gaps (e.g., Kanka Related excluding mentions) frustrate GMs.  
7. **Portability lens:** if local-first matters, structured associations must survive outside the app — partial MD exports show how easy it is to lose the graph.  
8. **Organizational burden is a product decision** — entity modules reduce blank-page fear but create ontology fights; blank documents defer cost to the user.  
9. **Visual relationship tools delight but don’t replace typed, queryable associations** (LegendKeeper’s own caveat).  
10. **Permissions/secrets are related but not identical to narrative context** — hiding a field ≠ recording a story-specific state.

---

## 18. Open questions requiring product/design decisions

1. Is the primary user mental model a **World**, a **Campaign/Story**, or a **Library of entities**?  
2. When an entity is reused, is the default **shared instance** or **fork**?  
3. Should narrative appearance be a **first-class object**, a **relationship to session/scene**, or only **prose + links**?  
4. How much **typed ontology** is opinionated vs user-defined?  
5. Are time-varying facts stored on the entity, on relationships, or on timeline events?  
6. What must remain usable if the user opens the data in another tool tomorrow?  
7. How should **player-visible**, **GM-secret**, and **author-private** layers interact with canon vs context?  
8. Where does hierarchy get first-class support (places? orgs?) and where is it discouraged?  
9. What orphan/appearance questions must search answer on day one?  
10. How explicit should inverse relationships be, and who maintains them?

---

## 19. Citations / links

### Official / primary
- World Anvil: [Home](https://www.worldanvil.com/), [Get started articles](https://www.worldanvil.com/learn/beginner-tutorials/get-started-articles), [GM workflow](https://www.worldanvil.com/learn/workflows/gm-workflow), [Campaign Manager](https://www.worldanvil.com/learn/rpg/campaign-manager), [Article templates](https://www.worldanvil.com/learn/article-guides/article-templates), [FAQ](https://www.worldanvil.com/faq), [Custom relationships suggestion](https://www.worldanvil.com/community/voting/suggestion/47977b49-63a8-44d4-a113-ae7ceb5c35a1/view), [Export suggestion](https://www.worldanvil.com/community/voting/suggestion/20e8c78e-c171-4280-8556-356052d48a35/view), [Academy one-write](https://academy.worldanvil.com/blog/dnd-campaign-wiki-lore-management)  
- LegendKeeper: [Home](https://www.legendkeeper.com/), [Boards](https://www.legendkeeper.com/boards-announcement/), [FAQ](https://www.legendkeeper.com/faq/), [Export changelog](https://www.legendkeeper.com/changelog/legendkeeper-0-16-1-0/), [Import guide](https://www.legendkeeper.com/import-world-legendkeeper/)  
- Kanka: [KB](https://kanka.io/kb), [Nested](https://docs.kanka.io/en/latest/features/nested.html), [Connections](https://docs.kanka.io/en/latest/features/connections.html), [Export](https://docs.kanka.io/en/latest/features/campaigns/export.html), [Import](https://docs.kanka.io/en/latest/features/campaigns/import.html), [References blog](https://blog.kanka.io/2021/07/26/how-to-use-references-kanka/), [Self-hosting](https://docs.kanka.io/en/latest/self-hosting.html)  
- Campfire: [FAQ](https://campfirewriting.com/faq), [Project linking](https://campfirewriting.com/learn/project-linking-tutorial), [Library tutorial](https://www.campfirewriting.com/learn/library-tutorial)  
- Fantasia Archive: [CartographyAssets listing](https://cartographyassets.com/assets/10089/fantasia-archive/), [Martens review](https://koenmartens.nl/20210425-world-building-with-fantasia-archive.html)  
- Obsidian: [RPG Manager](https://github.com/carlonicora/obsidian-rpg-manager), [Forum multi-directory](https://forum.obsidian.md/t/linking-or-redirecting-to-a-base-note-from-multiple-directories/113158), [TTRPG Campaign Manager plugin](https://community.obsidian.md/plugins/ttrpg-campaign-manager)  
- Notion: [RPG template](https://www.notion.com/templates/rpg-campaign), [DMCG worldbuilding](https://www.dmcgdesign.com/blog/worldbuilding-in-notion)  
- Scrivener: [Share across projects forum](https://forum.literatureandlatte.com/t/sharing-a-document-between-projects/145434), [Copy between projects](https://www.literatureandlatte.com/blog/how-to-copy-items-between-scrivener-projects), [Series bible](https://writerunboxed.com/2021/08/13/scrivener-scenario-creating-a-series-bible/)  
- Aeon Timeline: [Sync with Scrivener](https://www.aeontimeline.com/guides/sync-with-scrivener), [Sync settings](https://help.timeline.app/article/217-sync-settings)  
- Plottr: [Series bible](https://plottr.com/series-bible-software/), [Series View](https://docs.plottr.com/article/65-timeline-series-view)

### Community / friction
- [Loreteller WA categories](https://loreteller.com/learn/world-anvil-categories/)  
- [WA Trustpilot](https://www.trustpilot.com/review/worldanvil.com)  
- [RPGnet WA thread](https://forum.rpg.net/index.php?threads/worldanvil-thoughts-now-that-it-has-been-out-for-a-while.902656/)  
- Notion relation performance commentary: [WiseChecker](https://wisechecker.com/notion-relation-search-performance-large-databases/), [ResumeLens relations](https://www.resumelens.org/blog/notion/notion-relations-and-rollups)

---

## 20. Concise comparison: What products do | Problem solved | Tradeoff introduced

| Product | What it does | Problem solved | Tradeoff introduced |
|---------|--------------|----------------|---------------------|
| **World Anvil** | World-owned articles; campaigns/manuscripts reference them; typed templates | Canon setting shared by multiple campaigns/stories | Cloud gravity; template weight; custom relations limited; export not a working wiki |
| **LegendKeeper** | Flexible wiki pages + folders + boards | Fast GM lore writing with light structure | Relationships partly visual; MD export partial; ontology is DIY |
| **Kanka** | Campaign-as-universe of typed entities + connections + nesting | Coherent RPG entity model in one place | No cross-campaign sync; reuse = copy or mega-campaign; mentions ≠ related discovery |
| **Campfire** | Library-owned elements addable to many projects; links/webs | True multi-story reuse of the same element | Cloud; ownership/subscription tied to library owner; story-specific state ambiguous |
| **Fantasia Archive** | Offline typed docs, deep hierarchy, two-way relations | Local structured world graph | Smaller ecosystem; project/file UX clunky; less campaign-runtime tooling |
| **Obsidian** | Files + links + user metadata/plugins | Total ownership & portability; any model imaginable | User bears all modeling; multi-context & multi-folder membership painful |
| **Notion** | Databases + relations/rollups | Queryable association graph & dashboards | Schema/performance burden; cloud; weak offline/portable source |
| **Scrivener** | Hierarchical writing project with research sheets | Manuscript-centric organization | Sealed projects; cross-book live reuse missing |
| **Aeon Timeline** | Events + entity relationships over time | Narrative appearance vs entity list | Not a full world wiki; sync complexity with writing apps |
| **Plottr** | Series-level characters/places linked to scenes | Series bible continuity for fiction | Not built for live TTRPG state; Series View not auto-merged from books |

---

### Bottom line on the central question

**What belongs to the creator’s world** is variously: a World (WA), a Campaign-universe (Kanka), a Project (LK/FA/Scrivener/Plottr), a Vault (Obsidian), or a Library of elements (Campfire).  

**What merely uses or references it** is usually: campaigns, sessions, scenes, boards, mentions, and tags — except where products force containment to do the job of association (copying entities into each campaign), which reliably creates duplication and update problems.

No surveyed product fully separates **owned canon**, **associative structure**, and **narrative-context state** while remaining portable. That triad is the recurring market gap visible from evidence above.

---

*End of assignment 003. No Mahogany schema or implementation content included.*
