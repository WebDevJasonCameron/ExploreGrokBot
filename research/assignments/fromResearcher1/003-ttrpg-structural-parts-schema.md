# Research Assignment 003 — TTRPG Structural Parts Schema

**Report ID:** 003  
**Date:** 2026-09-02  
**Analyst:** Opportunity Researcher / Market Research Analyst (Employee 001)  
**Stage:** Book-structure classification schema (worked example)  
**Status:** Complete — awaiting Owner review  
**Path:** `research/assignments/fromResearcher1/003-ttrpg-structural-parts-schema.md`

This report asks how to take a TTRPG book and tag each piece as a designated structural **part**, so story, items, NPCs, rules, mechanics, PC incorporation, and PC sub-parts (class, species, backstory) can be identified independently of table etiquette.

It is **not** an opportunity scorecard, product pitch, software design, or reactivation of any prior TTRPG PDF-ingestion initiative. No copyrighted book prose is reproduced here.

Owner-confirmed corpus: third-party D&D 5e PDFs only, in the Owner's local `TTRPGs/5E` folder. Official books in the sibling `DnD/Sources` folder, Pathfinder, VTT/map zips, art books, and card-image decks were **out of scope** for this pass.

Continuity: Assignment 002 proposed five layers (A social, B procedures, C resolution, D catalogs, E fiction). Assignment 003 **drops Layer A** (meetup, social obligations, table etiquette). In-text procedures (crafting steps, trap design, travel, generators, rest-as-a-heading) remain, because they are book structure.

---

## 1. Executive Summary

**Yes — you can tag a TTRPG book into structural parts.** The unit to tag is a **book-addressable heading** (PDF bookmark, printed TOC entry, or atomic page such as a one-shot interrupt card), not a page, paragraph, or vibe.

**Most important findings**

1. **Fact.** Twenty books in the Owner's `5E` folder were outlined from PDF bookmarks and/or printed TOCs (18-page preview to 524-page campaign). Seventeen had bookmark trees. Two had no bookmarks (a 52-card interrupt deck; an OSE preview). Product types in the sample: 6 adventures, 5 hybrids, 3 procedure-systems, 3 random-table books, 1 player-options book, 1 NPC catalog, 1 bestiary. **Zero** books were a pure magic-item catalog.

2. **Observation.** This library is **adventure- and generator-shaped**, not PHB/DMG-shaped. One book in twenty is a class/species/spell catalog. The 5e resolution engine almost never appears as a heading; it is assumed. Backstory/background never appears as a heading.

3. **Analysis.** Owner's list (story, items, NPCs, rules, mechanics, PC incorporation, class/species/backstory) is a good **ask**, but the books do not store those as one flat list. Story is a nested tree (campaign, then chapter, then site, then keyed room, with maps and handouts as siblings). Item splits into at least four part-kinds. NPC has two incompatible shapes. Mechanics in this corpus is mostly **procedures and generators**, not dice math.

4. **Observation.** Product title is not a part type. A book titled as beginnings is a micro-adventure anthology. Crafting is a faction + rank + quest + recipe operating system, not a downtime sidebar.

5. **Inference.** A usable schema is: **product type** (what the whole book is) times **part kind** (what a heading is) times **nesting** (parent/child) times **facing** (GM / player / fill-in). That is enough to classify pieces without building software.

**Recommended classification method:** walk the bookmark/TOC tree; assign one `kind` tag per heading from the vocabulary in section 6; record parent; do not invent missing PHB parts.

**Do not begin product work.**

**Analyst confidence:** **High** that third-party 5e books can be tagged this way from outlines; **moderate** that the same vocabulary will cover official PHB/DMG/MM or non-5e games without additions; **low** that backstory can be tagged in this corpus at all (it is absent as a heading).

---

## 2. Research Question

If we take popular TTRPG books and categorize each piece so we can identify it by its part in the game — story, items, NPCs, rules, mechanics, expectations for incorporating PCs, and PC sub-parts such as classes, species, and backstories — how would we do that?

Constraints from Owner:

- Structure only; not meetup / social obligations / table etiquette.
- Research markdown plus a classification schema; not software.
- First pass: D&D 5e via the third-party `5E` folder only.
- No copyrighted text in the repository.

---

## 3. Method and Evidence Standards

**Window:** 2026-09-02 (America/Chicago).

**Signals used**

- PDF bookmark trees (17 of 20 books) as the publisher's own part list.
- Printed tables of contents on the first ~20 pages when bookmarks were sparse.
- First-line titles on bookmark-less card pages.
- Page counts from PDF metadata.

**Not used**

- Official WotC books in `TTRPGs/DnD/Sources` (Owner chose the `5E` folder only).
- Free D&D SRD (same Owner constraint for this pass).
- `5E/zip/`, `5E/Zips Unpacked/`, art books, map folios, Tome of Horrors card decks.
- Duplicate `treacheroustraps 2.pdf`.
- Body prose, stat-block numbers, flavor text, maps-as-images.

**Labels**

| Label | Meaning |
| --- | --- |
| **Fact** | Directly present as a heading, bookmark, or file in the named PDF |
| **Observation** | Recurring pattern across independent books in this folder |
| **Analysis** | Structured interpretation for this assignment |
| **Inference** | Reasonable conclusion not stated by the books |
| **Unknown** | Material gap |

**Limitations**

- Bookmark titles are publisher navigation, not a complete ontology. Heuristic tags on working outlines had some misfires; the vocabulary in section 6 is the corrected set.
- PDF page indices can be off printed numbers by cover pages.
- One book in the sample is OSE, not 5e (a preview bound into the folder).
- No table observation; this is document structure.
- Large PDF binaries were not copied into any git workspace. Outlines were extracted locally; only heading labels were retained for analysis.

---

## 4. What a part is (definition)

**Fact (operational).** In this corpus, the smallest reliable structural unit is whatever the publisher already made addressable:

| Unit | When it appears |
| --- | --- |
| PDF bookmark / heading | 17 of 20 books; depth from chapter down to named class feature or keyed room |
| Printed TOC row | Sparse-bookmark books (object-cue tables; travel generators) |
| Atomic page | Interrupt-card deck: one titled card per page, no chapters |
| Fill-in worksheet | Campaign journal: roster, flowchart, blank graph/hex paper |

**Analysis.** Do **not** tag paragraphs, sentences, or art as first-class parts unless they have their own heading. Do **not** treat a page number as a part. Maps and player handouts **are** parts in this corpus: they appear as sibling bookmarks next to rooms, not as unnamed illustrations.

**Inference.** A later official-PHB pass will likely have shallower bookmark trees (chapter/section, not room letters). The schema should not require 400-1300 outline nodes. It should tolerate them.

---

## 5. Product types (tag the book first)

Before tagging headings, tag the **host book**. Product type predicts which part-kinds dominate and which nestings to expect.

| product_type | count in sample | what the outline looks like |
| --- | --- | --- |
| `adventure` | 6 | Campaign/chapter, then keyed sites, then rooms; map and handout siblings; monster/item appendices |
| `hybrid` | 5 | Adventure or generator plus a second spine (PC options, blank journal, monster appendix) |
| `procedure-system` | 3 | How-to (trap design, crafting ranks, harvesting steps) wrapping catalogs |
| `random-tables` | 3 | Instructions plus keyed tables (biome, dungeon level, object-cue, interrupt card) |
| `player-options` | 1 | Class, then subclass, then feature; species; spells; feats |
| `npc-catalog` | 1 | Faction/guild, then named person, then repeated level-band stat blocks |
| `bestiary` | 1 | People-type, then culture/tactics/warband/lair/tribes (plus implied stat blocks) |
| `item-catalog` | 0 | Not observed as a whole book; magic items live in appendices or recipe lists |

**Observation.** Title is not type. The beginnings-titled book is a keyed-site anthology with monster and magic-item appendices. The ultimate-guide crafting book is a faction operating system.

**Analysis.** Owner "break a campaign into story, items, NPCs" is the `adventure` product type. A parts catalog that only looks at PHB-shaped books will miss most of this folder.

---

## 6. Part-kind vocabulary (tag each heading)

Stable set, grounded in observed headings. Add a tag only when a heading does not fit.

### 6.1 Story

| kind | what the heading is | typical children |
| --- | --- | --- |
| `story.plot` | named adventure, chapter, campaign beat | hook, locations, maps, conclusion |
| `story.location` | keyed room, site, biome, settlement locale | sub-rooms, map, monster, trap, loot |
| `story.hook` | adventure hook, quest seed, roleplay cue | sometimes a location or NPC |
| `story.scene` | named beat inside a chapter | rare in this corpus; books title locations, not scenes |
| `story.pacing-note` | optional branch, GM-decision, phase | points at other plot nodes |

**Fact.** Adventure nesting is almost always: `story.plot` (campaign), then `story.plot` (chapter), then `story.location` (site), then `story.location` (room), with `reference.map` and `reference.handout` as **siblings** of rooms, not decorations.

**Observation.** This is the dominant shape of the folder. Assignment 002 Layer E (fiction) and Layer B (procedures of play) are fused here: a keyed room is both fiction and a play procedure.

### 6.2 Lore

`lore.faction` · `lore.history` · `lore.religion` · `lore.myth` · `lore.culture` · `lore.theme` · `lore.settlement`

**Observation.** Gazetteer clusters (government / trade / military / inns) appear as settlement lore, which is Owner "systems" as **fiction**, not as a resolution engine. Bestiary culture/language/roleplaying blocks are lore children of a monster people-type — they are not in a typical SRD monster heading list.

### 6.3 Entities (people and PCs)

| kind | what it is | nesting observed |
| --- | --- | --- |
| `entity.npc` | named person | identity, then optional level-band blocks |
| `entity.monster` | creature or people-type | Horde book: culture + tactics + warband-by-CR + trinkets + lair + tribes |
| `entity.pc-option.class` | class chapter | subclass, then feature |
| `entity.pc-option.subclass` | subclass / path / college / domain | features, spell lists |
| `entity.pc-option.feature` | named class feature | leaf |
| `entity.pc-option.species` | race/species + subrace | traits, then optional racial feats |
| `entity.pc-option.feat` | feat list item | leaf |
| `entity.pc-option.spell` | spell name or spell-list heading | leaf |
| `entity.pc-option.background` | background / backstory chapter | **not observed** |

**Fact — two NPC shapes.** (1) Shopkeeper-in-place: proprietor heading under a shop/location, almost no mechanical children in the outline. (2) Catalog NPC: guild, then person, then five level-band stat-block headings (4 / 8 / 12 / 16 / 20).

**Fact — monster shape.** The horde bestiary treats a people as the parent part. An SRD-like adventure appendix is often just a name heading with an implied stat block.

**Fact — PC parts.** One PHB-shaped book (class, then subclass, then named feature; species; spells; feats). One campaign tacks races/subclasses/chargen on as appendices. One procedure book adds a trapsmith class. **Background/backstory never appears as a heading.**

### 6.4 Objects

| kind | what it is |
| --- | --- |
| `object.item` | mundane ingredient, trinket, object-cue |
| `object.magic-item` | named magic item (usually appendix or recipe output) |
| `object.vehicle` | ship, canoe, registry entry (sometimes with keyed decks) |
| `object.trap` | trap entry, trap level-band, or trap catalog |
| `object.puzzle` | puzzle/riddle module |

**Observation.** Items is not one part. Four shapes:

1. Magic-item appendix (adventures).
2. Recipe catalog keyed to crafting rank.
3. Object-cue / story seed (environment table; good / neutral / bad outcomes) — not a stat block.
4. Trinket table hanging off a people-type or journal.

### 6.5 In-world / play systems

`system.faction` (ranks, principles, standing, quests) · `system.economy` · `system.crafting` · `system.exploration` · `system.downtime`

**Observation.** Crafting in this folder is faction OS + procedure + recipe, not a one-page downtime rule.

### 6.6 Rules (thin)

`rule.resolution` · `rule.combat` · `rule.condition` · `rule.rest` · `rule.advancement`

**Observation.** `rule.resolution` is almost absent as a heading. 5e is assumed. Combat headings in the bestiary are **tactics**, not the d20 engine. Advancement appears as local XP notes or class tables, not a PHB leveling chapter.

**Analysis.** If Owner wants rules and mechanics as separate tags, use `rule.*` for engine/conditions/rest/XP and `procedure.*` / `system.*` for how-to play loops. Mixing them under mechanics will hide that this corpus barely restates the engine.

### 6.7 Procedures (kept; they are structure)

`procedure.session-flow` · `procedure.encounter-setup` · `procedure.generator` · `procedure.chargen` · `procedure.travel` · `procedure.campaign-tracker`

**Fact.** Generators are first-class: travel-encounter books, dungeon-section assemblers, trap randomizers, object-cue instructions, fill-in journals with name tables.

### 6.8 Tables

`table.random` · `table.loot` · `table.encounter` · `table.interrupt-card` · `table.advancement`

**Observation.** Interrupt cards have no PHB analog. Each card is an atomic play part (title + one-shot override), with no chapter wrapper.

### 6.9 Reference

`reference.map` · `reference.stat-block-template` · `reference.index` · `reference.toc` · `reference.front-matter` · `reference.handout` · `reference.worksheet` · `reference.graph-paper`

Use `reference.section` only as a leftover divider; prefer a story or procedure tag when the heading actually starts a beat.

---

## 7. Recurring nesting patterns (how pieces compose)

These are observed trees, not a product data model.

```
adventure
  story.plot                    # campaign / chapter
    story.hook
    procedure.session-flow
    story.location              # site
      story.location            # room
      object.trap?
      entity.monster? | entity.npc?
      table.loot?
    reference.map               # sibling, not child of art
    reference.handout
  appendices: entity.monster* + object.magic-item* + reference.map*

bestiary-people
  entity.monster                # people-type, not one CR
    lore.culture
    rule.combat                 # tactics
    table.encounter             # warband by CR band
    table.loot                  # trinkets
    story.location              # lair
    lore.faction                # named tribes

npc-catalog
  lore.faction                  # alignment guilds
  entity.npc
    reference.stat-block-template x 5 level-bands

player-options
  entity.pc-option.class
    entity.pc-option.subclass
      entity.pc-option.feature
      entity.pc-option.spell?
  entity.pc-option.species then traits then optional feat
  entity.pc-option.spell        # by level
  entity.pc-option.feat

procedure-system (crafting pair)
  system.faction                # association: principles, ranks, quests
  system.crafting
  object.item | object.magic-item   # ingredients / recipes by rank
  system.downtime | system.exploration

generator
  procedure.generator
  story.location | rule.advancement-band
    table.encounter | table.random | object.item (cue)
```

---

## 8. Classification schema (research artifact)

Minimal record for one part. This is a **tagging card**, not an app schema.

```yaml
part:
  source:
    file: string              # filename in the 5E folder
    page: integer             # PDF page index; label as estimate if off printed
    heading: string           # bibliographic short title only
  host:
    product_type: adventure | bestiary | npc-catalog | item-catalog
                  | player-options | procedure-system | random-tables
                  | hybrid | other
  kind: string                # from section 6 vocabulary
  parent: string | null       # parent heading or part id
  facing: gm | player | shared | fill-in
  notes: string               # one line: what this heading IS, not what it says
```

**Tagging procedure (recommended)**

1. Identify `product_type` from the TOC shape (section 5), ignoring the marketing title.
2. Walk bookmarks depth-first. One heading, one `kind`. If two kinds apply (shop + proprietor), prefer the **child** as `entity.npc` and the **parent** as `story.location`.
3. Record `parent` so nesting is recoverable. Do not flatten keyed rooms into a loot list.
4. Tag maps, handouts, and worksheets when they have headings.
5. Do not create `entity.pc-option.background` or `rule.resolution` rows because a PHB should have them. Log a **gap**.
6. Stop at heading level. Do not transcribe body text.

**Worked examples (structure only; no body text)**

| Book (filename) | product_type | distinctive part pattern |
| --- | --- | --- |
| `whisperandvenom5e.pdf` | adventure | Gazetteer + shopkeeper NPCs, then Areas A-E; creature/item/map appendices |
| `exwynshandbooktoheroism.pdf` | player-options | Class, then subclass, then named feature; species; spells; feats |
| `objectsofintrigue.pdf` | random-tables | Biome, then object-cue table, then named seed (reward / diversion / hazard) |
| `ultimatenpcs_skulduggery.pdf` | npc-catalog | Guild, then named NPC, then five level-band blocks |
| `ultimatebestiary_revengeofthehorde_V3.pdf` | bestiary | People-type, then culture/tactics/warband/lair/tribes |
| `ultimateguidetoalchemycraftingandenchanting.pdf` | procedure-system | Association ranks/quests wrapping recipe catalogs |
| `decksofdirtytricks_vol1.pdf` | random-tables | 52 atomic interrupt cards; no chapter tree |
| `recordsoffaith_gmsjournal....pdf` | hybrid | Fill-in campaign tracker: roster, flowchart, generators, graph paper |
| `endlessencounters.pdf` | hybrid | Per-level dungeon sections A-D + charts + sample dungeon + appendices |
| `splintersoffaith20225e.pdf` | adventure | Campaign OS + overland weather/encounter engine + chapter-adventures (largest bookmark tree) |

---

## 9. Gaps vs Owner list

| Owner heading | in this corpus? | note |
| --- | --- | --- |
| story | **strong** | Most of the library *is* `story.plot` + `story.location` |
| items | **strong but split** | Magic-item appendices vs object-cues vs recipes vs trinkets |
| NPCs | **strong but two shapes** | Shopkeeper-in-place vs five-level stat stack |
| rules | **weak as headings** | Engine assumed; local procedures (trap DC families, harvesting, disease) |
| mechanics | **present as procedures** | Crafting steps, trap design, overland weather, dungeon generators |
| PC incorporation | **weak except two books** | Adventures assume existing PCs |
| class | present | One catalog book, plus a trapsmith, plus campaign appendices |
| species | present | Same two books |
| backstory | **missing as a heading** | Closest: family/shop fiction; implied personality inside NPC blocks |

Assignment 002 Layer A (table/social) was dropped as instructed and also barely appears as headings (no safety/principles chapters).

Assignment 002 Layer C (resolution engine) is the loudest **absence**. Third-party 5e books do not restate the d20. A schema trained only on this folder will under-detect rules.

---

## 10. How this sits on Assignment 002

| 002 layer | 003 treatment | in the `5E` folder |
| --- | --- | --- |
| A social / etiquette | **dropped** | almost no headings |
| B procedures of play | **kept as `procedure.*` + generators** | strong |
| C resolution engine | keep tag `rule.*`; expect empty | almost empty |
| D catalogs | `entity.*` / `object.*` / tables | strong, but adventure-appendix and generator-shaped |
| E fiction | `story.*` / `lore.*` | dominant |

**Analysis.** 002's layered map still works as the **comparison** frame across games. 003's kind-tags are the **book-piece** frame inside one game family. Do not collapse them into one list: story is not a sibling of feat.

**Inference.** If the next corpus is official 5e (PHB, DMG, MM), expect Layer C and PC-option tags to fill in, and story.location trees to shrink except in adventures. If the next corpus is Pathfinder (sibling folder), expect more `system.*` operationalized in the rulebooks themselves (002 already flagged PF2e for this).

---

## 11. Unknowns

- Whether official 2014/2024 PHB bookmark trees use the same PC-option nesting (class, then subclass, then feature) or a shallower chapter split.
- Whether a 5.5 / 2024 core book in this library exists at all (none in the `5E` folder; none found earlier in `DnD/Sources` either).
- How to tag **backstory** when it is only implied inside NPC prose, not a heading. Current rule: do not invent a part.
- Whether interrupt cards and object-cues should stay under `table.*` / `object.item` or get a `play.atomic` parent. Deferred; current tags work.
- Whether the second bestiary and warfare NPC book (skipped as same-publisher duplicates of shape) actually introduce new kinds.
- How well heading-tags match **actual tables** (groups skip chapters). Out of scope.

---

## 12. Recommendation

**Classification method to use:** product type times part kind times parent times facing, walking the publisher outline (sections 5-8).

**Do not** flatten Owner's list into seven folders and file every heading into one of them. Story, item, and NPC each have multiple part-kinds and nestings.

**Do not** treat missing PHB chapters as holes to fill with SRD text on this assignment. They are **corpus gaps**.

**Do not begin product work or create another employee** unless Owner asks. A solutions agent is unnecessary for this schema; the research question is answered at the document-structure level.

**Narrow follow-ups (only if Owner wants one)**

1. **Official 5e stress test** — apply the same tagging walk to `TTRPGs/DnD/Sources` (DMG 2014, Monster Manual, Xanathar's, owned adventures). Expected fill: `rule.*` and maybe still no PHB.
2. **Pathfinder folder** — test whether `system.*` becomes first-class in core books, not only in third-party crafting guides.
3. **One adventure tagged end-to-end** — pick a single `adventure` PDF and produce a heading-only tag table (filename, page, kind, parent). Still no body text.

**Analyst confidence:** **High** on the tagging method for this folder; **moderate** on vocabulary completeness beyond third-party 5e.

---

## 13. Sources

Access date **2026-09-02**. Primary evidence is **document structure** of Owner-owned PDFs (bookmarks/TOCs), not quotations.

### Corpus (filenames only)

1. `exwynshandbooktoheroism.pdf`
2. `objectsofintrigue.pdf`
3. `bookofbeginnings.pdf`
4. `elementsofinspiration.pdf`
5. `decksofdirtytricks_vol1.pdf`
6. `endlessencounters.pdf`
7. `whisperandvenom5e.pdf`
8. `tomeofquests5e.pdf`
9. `treacheroustraps.pdf`
10. `ultimateguidetoalchemycraftingandenchanting.pdf`
11. `ultimateguidetoforagingharvestingandnaturaldiscovery.pdf`
12. `splintersoffaith20225e.pdf`
13. `pathofthevanished.pdf`
14. `intotheunknown.pdf`
15. `losttriptych.pdf`
16. `ultimatenpcs_skulduggery.pdf`
17. `ultimatebestiary_revengeofthehorde_V3.pdf`
18. `seakingsmalice5e.pdf`
19. `newold-schoolpreview.pdf` (OSE preview in the same folder)
20. `recordsoffaith_gmsjournalasplintersoffaith2022supplement.pdf`

Folder: `TTRPGs/5E` on the Owner's Mac (iCloud). Skipped per Owner/instruction: `zip/`, `Zips Unpacked/`, art book, map folio, Tome of Horrors card decks, duplicate trap PDF.

### Continuity

21. `research/assignments/fromResearcher1/002-ttrpg-core-components.md` — five-layer map; Layer A dropped here
22. `agents/market-research-analyst/instructions.md`
23. `company/opportunity-criteria.md` (not scored; taxonomy-only)

### Theory already cited in 002 (not re-litigated)

24. Bastarrachea-Magnani, Meritano, León, Analog Game Studies 11.3 (2024) — taxonomies describe documents, not the whole phenomenon of play
25. Aarseth & Grabarczyk, DiGRA game-ontology meta-model — multiple description layers
26. Edwards / Big Model — System as how events unfold; used only as a reminder that procedures exist even when untitled

---

## Appendix A — One-page tagging cheat sheet

**Unit:** heading / bookmark / atomic page.  
**Ignore:** table etiquette, body prose, untitled art.

1. Label the **book**: adventure, catalog, generator, procedure-system, player-options, hybrid.
2. Walk the outline. Tag **what the heading is**:
   - Story tree: plot, then location, then (map, handout)
   - People: npc *or* monster-people (culture/tactics/lair), not both assumed
   - PC: class, then subclass, then feature; species; spell; feat; **background only if headed**
   - Objects: magic-item is not recipe is not object-cue is not trap is not puzzle
   - How-to: procedure.generator / session-flow / chargen / travel / campaign-tracker
   - Engine: rule.* — expect empty in third-party 5e
3. Record **parent**. Maps sit beside rooms.
4. Log gaps. Do not invent a PHB.

**If you only remember one sentence:** third-party 5e books in this library are mostly keyed stories and generators that assume the chassis; tag them that way, and do not look for a Player's Handbook hiding in the adventure folder.
