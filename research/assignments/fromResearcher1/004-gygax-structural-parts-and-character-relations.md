# Research Assignment 004 — Gygax Folder Parts Schema and Character Relations

**Report ID:** 004  
**Date:** 2026-09-02  
**Analyst:** Opportunity Researcher / Market Research Analyst (Employee 001)  
**Stage:** Book-structure classification + character-relation recording  
**Status:** Complete — awaiting Owner review  
**Path:** `research/assignments/004-gygax-structural-parts-and-character-relations.md`

This report asks whether the Assignment 003 heading-walk still classifies the Owner's whole `TTRPGs/DnD/Gygax` folder, and how named beings should be recorded as relations without minting a social network.

It is **not** an opportunity scorecard, product pitch, software design, or reactivation of any prior TTRPG PDF-ingestion initiative. No copyrighted book prose is reproduced here.

Owner-confirmed corpus: the Owner's whole folder `TTRPGs/DnD/Gygax` on `Jasons-Mac.local`, including CoC Geneva Lake and `gordtherogue.pdf`. Sibling folders were **out of scope** for this pass. The folder's D&D world is Greyhawk / Lost Lands / Gygaxian fiction, not 5e rules.

Continuity: Assignment 003 vocabulary and tagging procedure. Layer A etiquette remains dropped. In-text procedures remain, because they are book structure. Tag `system_family` per book.

---

## 1. Executive Summary

**Yes — the 003 walk still works.** This folder is **not** a 5e library. It is mostly Swords & Wizardry and Old-School Essentials keyed adventures, plus Castles & Crusades gazetteer/horror, d20 Gygax Fantasy Worlds, two Call of Cthulhu books, three Tome of Horrors, one deity catalog, one novel, and one 5e magazine.

**Most important findings**

1. **Fact.** Thirty-two PDFs were attempted. Twenty-four were heading-level (22 bookmark trees + 2 publisher/public TOCs: Canting Crew and Living Fantasy). Eight are scans or image-heavy with no outline, including Necropolis. Tome of Horrors Complete was capped at 800 nodes / 688 pages.

2. **Observation.** The 003 keyed-dungeon nest repeats. A new whole-book product type appears: **deity-catalog**. New part-kinds appear: `entity.deity`, `lore.pantheon`, `reference.pregen`, `system.law`, `system.warfare`. `entity.pc-option.background` is now observed (Eye of Itral PC templates). Species and personal backstory are still absent as headings.

3. **Observation.** Call of Cthulhu in this folder is parts + Keeper + sanity + pregens + handouts, **not** room letters. Tome of Horrors is a flat A–Z, **not** the 003 Horde culture/lair skeleton.

4. **Analysis.** Record characters as a **card plus heading-backed edges**, not as a social network. Nine relations are enough for this folder: `inhabitant_of`, `owner_of`, `quest_giver_for`, `enemy_of`, `member_of`, `worships`, `rules`, `wields`, `appears_in`. A hireling gallery can have **zero** edges. Do not mint `allied_with`, `knows`, or backstory.

5. **Inference.** The best recording method is one card per named being, plus edges only from nest, fused title (office + residence), or an explicit phrase *Working for X*.

**Do not begin product work.**

**Analyst confidence:** **High** on the 003 walk for this folder; **high** on the nine-edge card for this folder; **moderate** that the same nine edges cover books beyond it; **low** on the eight bookmark-less books.

---

## 2. Research Question

If we take the Owner's whole `TTRPGs/DnD/Gygax` folder and walk each book the way Assignment 003 walked `TTRPGs/5E`, does the same heading unit and kind vocabulary still classify the pieces — and how should named beings be recorded so story, items, NPCs, rules, mechanics, PC incorporation, and PC sub-parts stay identifiable without inventing a relationship graph?

Constraints from Owner:

- Structure only; Layer A etiquette stays dropped; in-text procedures stay.
- Research markdown plus classification cards; not software.
- Whole Gygax folder on `Jasons-Mac.local`; sibling folders out of scope.
- No copyrighted text in the repository.
- Extra ask: a character-relation card, not a social network.

---

## 3. Method and Evidence Standards

**Window:** 2026-09-02 (America/Chicago).

**Signals used**

- PDF bookmark trees (22 of 32 books) as the publisher's own part list.
- Publisher/public tables of contents for Canting Crew and Living Fantasy (2 of 32).
- Filename / product identity for the 8 books with no outline.

**Not used**

- Body prose.
- Official WotC books.
- The `5E` folder (Assignment 003 corpus).
- Pathfinder.
- PDF binaries in git.

**Bookmark-less set (filename / product only)**

- `garygygaxsnecropolisd20.pdf`
- `gl2thedreadfromgenevalake2coc.pdf`
- `gordtherogue.pdf`
- `heartofstbathusose.pdf`
- `lakeofdustosr.pdf`
- `playersguidetothenorthlandsose.pdf`
- `spearsintheiceose.pdf`
- `undercavernsofgaxmoorcandc.pdf`

**Labels**

| Label | Meaning |
| --- | --- |
| **Fact** | Directly present as a heading, bookmark, or file in the named PDF |
| **Observation** | Recurring pattern across independent books in this folder |
| **Analysis** | Structured interpretation for this assignment |
| **Inference** | Reasonable conclusion not stated by the books |
| **Unknown** | Material gap |

**Limitations**

- Eight books have no heading tree; product type and `system_family` for those rest on filename / product only.
- Tome of Horrors Complete outline was capped at 800 nodes / 688 pages.
- Bookmark titles are publisher navigation, not a complete ontology.
- No table observation; this is document structure.
- Large PDF binaries were not copied into any git workspace.

---

## 4. What a part is (definition)

**Fact (operational).** The smallest reliable structural unit is still whatever the publisher already made addressable, as in Assignment 003:

| Unit | When it appears in this folder |
| --- | --- |
| PDF bookmark / heading | 22 of 32 books |
| Publisher / public TOC | 2 of 32 (Canting Crew; Living Fantasy) |
| Filename / product only | 8 of 32 (scans or image-heavy; no outline; includes Necropolis) |

**Analysis.** Do **not** tag paragraphs, sentences, or art as first-class parts unless they have their own heading. Maps remain sibling parts of rooms where the outline prints them that way.

**Observation.** Twenty-four books can be walked at heading level. The other eight cannot be walked by this method.

---

## 5. Product types (tag the book first)

Before tagging headings, tag the **host book**. Product type predicts which part-kinds dominate and which nestings to expect.

| product_type | count in sample (32) | what the outline looks like |
| --- | --- | --- |
| `adventure` | 20 (6 without tree) | Keyed sites and rooms in S&W / OSE; CoC investigation parts instead of room letters |
| `bestiary` | 3 | Tome of Horrors: flat A–Z letter buckets, not a culture/lair people-type |
| `setting-gazetteer` | 2 | C&C city / region; fused residence + office titles |
| `hybrid` | 2 | Counted; outline shape not further specified in this pass |
| `npc-catalog` | 1 | Flat named-person siblings (Fortune Hunters: no guild parent) |
| `deity-catalog` | 1 | **New product type.** Pantheon, then church, then god leaf |
| `procedure-system` | 1 | Counted; in-text procedures kept as in 003 |
| `player-options` | 1 | Counted; PC-option headings appear in this folder |
| `fiction` | 1 | Novel (`gordtherogue.pdf`); heading method does not tag prose |

**Observation.** The folder name is not a product type. Twenty of thirty-two books are adventures; six of those twenty have no tree.

**Analysis.** Owner "break a campaign into story, items, NPCs" still maps to `adventure`, but this folder also needs `setting-gazetteer`, `deity-catalog`, and `fiction` as whole-book tags. A parts catalog trained only on the 003 `5E` folder will miss those three.

---

## 6. System family (tag the book second)

**Observation.** Folder name is not system. Tag `system_family` on the book.

| system_family | count in sample (32) | note |
| --- | --- | --- |
| `sw` | 11 | Swords & Wizardry |
| `ose` | 5 | Old-School Essentials |
| `osr` | 3 | Other OSR |
| `cc` | 3 | Castles & Crusades |
| `d20` | 3 | Gygax Fantasy Worlds and related d20 |
| `coc` | 2 | Call of Cthulhu (Geneva Lake set) |
| `5e` | 1 | One magazine; assumes 5e |
| `adnd1e` | 1 | |
| `fiction` | 1 | `gordtherogue.pdf` |
| `other` | 2 | Cat's Cradle; Deities of the Lost Lands |

**Fact.** This folder is not a 5e corpus. One book in thirty-two is tagged `5e`.

---

## 7. Part-kind vocabulary (tag each heading)

### 7.1 Reused 003 kinds

Stable set from Assignment 003, still grounded here:

- Story: `story.plot` · `story.location` · `story.hook` · `story.scene` · `story.pacing-note`
- Lore: `lore.faction` · `lore.history` · `lore.religion` · `lore.culture` · `lore.settlement` · `lore.myth` · `lore.theme`
- Entities: `entity.npc` · `entity.monster` · `entity.pc-option.*`
- Objects: `object.item` · `object.magic-item` · `object.vehicle` · `object.trap`
- Procedures: `procedure.session-flow` · `procedure.travel` · `procedure.encounter-setup` · `procedure.chargen`
- Tables and reference: as in Assignment 003

**Fact.** S&W / OSE reuse plot, then site, then room, with maps as siblings.

**Observation.** `story.scene` is used here (festival events). In Assignment 003 it was idle.

### 7.2 New tags (add only when a heading does not fit)

| kind or product | what it is in this folder |
| --- | --- |
| `entity.deity` | named god leaf under church / pantheon |
| `lore.pantheon` | pantheon parent over churches and gods |
| `entity.pc-option.background` | PC templates (Eye of Itral), **not** an NPC's personal past |
| `reference.pregen` | prepared investigator / PC sheet as a heading |
| `system.law` | in-world law as a headed system |
| `system.warfare` | in-world warfare as a headed system |
| product `deity-catalog` | whole book whose spine is pantheon → church → god |

**Fact.** CoC sanity headings are `rule.condition`. Raslam frights are `table.random`.

**Fact.** Species and personal backstory are still absent as headings.

---

## 8. Recurring nesting patterns (how pieces compose)

These are observed trees, not a product data model.

```
keyed-dungeon                         # S&W / OSE (003 nest repeats)
  story.plot                          # adventure / chapter
    story.location                    # site
      story.location                  # room
      entity.monster? | entity.npc?
    reference.map                     # sibling of rooms, not child of art

ose-festival-village
  story.plot
    story.scene                       # festival events (used here; idle in 003)
    story.location

cc-city-gazetteer                     # fused residence + office titles
  lore.settlement
    entity.npc                        # person heading IS the place / office

sw-noir                               # Working for Named Person
  story.hook                          # Working for X / Name's Offer / Meeting with Name
  entity.pc-option.background         # PC templates, not NPC past
  object.magic-item                   # MacGuffin

coc-investigation                    # not room letters
  procedure.session-flow              # parts + Keeper
    rule.condition                    # sanity
    reference.pregen
    reference.handout

deity-catalog
  lore.pantheon
    lore.religion                     # church
      entity.deity                    # god leaf

toh-letter-bucket                     # flat A-Z; not 003 Horde culture/lair
  entity.monster                      # letter bucket; catalog names only

fortune-hunters                       # flat NPC siblings; no guild parent
  entity.npc                          # hireling gallery: card with zero edges
```

---

## 9. Engine restatement by system_family

| system_family | engine as a heading |
| --- | --- |
| `sw` / `ose` / `osr` | almost never restated |
| `cc` | optional-rules appendix |
| `d20` | prestige class / spell as a section |
| `coc` | sanity is a heading (`rule.condition`) |
| `5e` | magazine assumes 5e |
| `adnd1e` | none |
| `fiction` | n/a |

**Observation.** The 003 engine absence repeats, except Call of Cthulhu.

**Analysis.** If Owner wants rules and mechanics as separate tags, keep `rule.*` for engine / conditions and `procedure.*` / `system.*` for how-to loops. Mixing them under mechanics will hide that this folder barely restates an engine outside CoC.

---

## 10. Gaps vs Owner list

| Owner heading | in this corpus? | note |
| --- | --- | --- |
| story | **strong** | Keyed plot/site/room; festival `story.scene`; gazetteer settlement |
| items | **split** | Magic-item / MacGuffin / trap / mundane object still separate kinds |
| NPCs | **more shapes** | Shop/quarters inhabitant; fused person-is-place; flat hireling gallery; pregen; deity |
| rules | **weak** except CoC sanity, thief skills, Zagyg optional | Engine still assumed in S&W / OSE / OSR |
| mechanics | **present as procedures** | Session-flow, travel, encounter-setup, chargen |
| PC incorporation | **stronger than 003** | Backgrounds (PC templates), pregens, prestige classes |
| class | **only** in the Gygax Fantasy Worlds d20 patch | |
| species | **missing** as a heading | |
| backstory | **missing** as a heading | Do not mint it from NPC prose |

**Analysis.** Do not collapse character relations into `entity.npc`. The relation is the **edge**.

---

## 11. Character relations (Owner extra ask)

Character kinds that may open a card:

`entity.npc` · `entity.deity` · `entity.monster` · `lore.faction` · `reference.pregen` · `entity.pc-option.background`

### 11.1 Nine relations (what the outline shows)

| rel | what the outline shows | examples in this folder |
| --- | --- | --- |
| `inhabitant_of` | person under shop / quarters / farm / room | Raslam staff; Yule Cat brewer; Yggsburgh residences |
| `owner_of` | place heading **is** the person site | named camps, keeps, shops |
| `quest_giver_for` | *Working for Name* / *Name's Offer* / *Meeting with Name* | Eye of Itral; Mithral wizard meeting |
| `enemy_of` | named antagonist heading | |
| `member_of` | nested under faction / church / household | |
| `worships` | temple / shrine / god; item under a saint | |
| `rules` | office fused into residence / palace title | |
| `wields` | named item attached to person / cult / MacGuffin | |
| `appears_in` | named figure as a moving plot heading across sites | |

Do **not** add `allied_with`, `parent_of`, `owes`, `knows`, `romance`, or backstory.

### 11.2 Nest-to-edge

| outline nest | edge to record | via | do not record |
| --- | --- | --- | --- |
| shop / quarters / farm / room | `inhabitant_of` | nest | |
| fused residence + office title | `rules` (person **is** the place) | fused-title | a separate flat NPC list row |
| patron block (*Working for X* / offer / meeting) | `quest_giver_for` | explicit-parent-phrase | `allied_with` / `knows` |
| named camp / keep / shop as the person site | `owner_of` | nest | |
| pantheon → church → god | `worships` / `member_of` | nest | |
| monster appendix | none for location | — | location unless a lair heading exists |
| pregen | `appears_in` | nest | `inhabitant_of` a lodge |
| hireling gallery (flat siblings, no guild parent) | **zero edges** | — | a fabricated guild or ally |

### 11.3 Edge strength by book

| strength | books |
| --- | --- |
| **Strong** | Eye of Itral; Raslam; Yggsburgh; Mithral Rattlesnakes; One Last Thing; Yule Cat; Spring Rites; Seanche's Lament; Deities vol.1; Orcus 34th |
| **Medium** | Cat's Cradle; Fortune Hunters (zero edges); GL1; Tower (Dramatis Personae only); later Okkori |
| **None** | Lost Crypt; 1975; Tome of Horrors (catalog names); Gord; the bookmark-less set |

**Analysis.** Yggsburgh shows why flat NPC lists fail: the person **is** the place. Fortune Hunters shows why a graph would sit empty: the hireling gallery is cards with no edges.

**Inference.** Best method: one card per named being; edges only from nest, fused title, or *Working for X*. Empty edge lists are allowed. Lonely catalog names get a card with no edges.

---

## 12. Classification cards (research artifacts)

Two tagging cards sit together. Neither is an app schema.

### 12.1 Part record (003-style: product_type × kind × parent × facing)

```yaml
part:
  source:
    file: string              # filename in the Gygax folder
    page: integer             # PDF page index; label as estimate if off printed
    heading: string           # bibliographic short title only
  host:
    product_type: adventure | bestiary | setting-gazetteer | hybrid
                  | npc-catalog | deity-catalog | procedure-system
                  | player-options | fiction | other
    system_family: sw | ose | osr | cc | d20 | coc | 5e
                   | adnd1e | fiction | other
  kind: string                # section 7 vocabulary
  parent: string | null       # parent heading or part id
  facing: gm | player | shared | fill-in
  notes: string               # one line: what this heading IS, not what it says
```

### 12.2 Character-relation card

```yaml
character:
  source: file, page, heading
  kind: entity.npc | entity.deity | entity.monster | lore.faction | reference.pregen | entity.pc-option.background
  edges:
    - rel: inhabitant_of | owner_of | quest_giver_for | enemy_of | member_of | worships | rules | wields | appears_in
      target_heading: string
      target_kind: story.plot | story.location | object.magic-item | lore.faction | lore.pantheon | story.scene
      via: nest | fused-title | explicit-parent-phrase
```

**Tagging procedure (recommended)**

1. Label the book: `product_type` from the TOC shape (section 5), then `system_family` (section 6). Ignore the folder name.
2. Walk the outline. One heading, one `kind`. Reuse 003 kinds; add a new tag only when the heading does not fit.
3. Record `parent` so nesting is recoverable. Maps sit beside rooms.
4. If a heading names a being, open a **character** card (`entity.npc`, `entity.deity`, `entity.monster`, `lore.faction`, `reference.pregen`, or `entity.pc-option.background`).
5. Add an edge only from nest, fused title, or an explicit parent phrase (*Working for X* / *Name's Offer* / *Meeting with Name*). Multiple edges are allowed.
6. A lonely catalog name gets a card with **no** edges. A hireling gallery may be all lonely cards.
7. Do not mint backstory. Do not mint `allied_with`, `parent_of`, `owes`, `knows`, or romance.
8. Stop at heading level. Do not transcribe body text.

---

## 13. Worked examples (structure only; no body text)

| Book (filename) | distinctive part + relation pattern |
| --- | --- |
| `eyeofitralsw` | S&W noir: *Working for Name* hooks, PC-option backgrounds, MacGuffin; strong edges (`quest_giver_for`, `wields`) |
| `candccastlezagygyggsburgh` | C&C city gazetteer; fused residence + office titles; person **is** the place (`rules`, `inhabitant_of`, `owner_of`) |
| `bewaretheyulecatose` | OSE festival-village; `story.scene` in use; brewer as `inhabitant_of` |
| `raslamasylumcc` | C&C horror; staff under shop/quarters/farm/room; frights as `table.random`; strong edges |
| `fortunehunterssw` | Flat NPC siblings; no guild parent; hireling gallery; **zero** edges |
| `deitiesofthelostlands_vol1` | Deity-catalog: pantheon, then church, then god leaf; `worships` / `member_of` |
| `gl1thedreadfromgenevalakecoc` | CoC investigation: parts + Keeper + sanity + pregens + handouts; medium edges |
| `tomeofhorrorscompletesw` | Flat A–Z letter buckets; catalog names; no location edge unless a lair exists; outline capped at 800 nodes / 688 pages |
| `gordtherogue` | Fiction / novel; heading method does not tag prose; no edges |
| `to1talesfromokkorimg20` | Later Okkori; medium edges |

---

## 14. How this sits on Assignment 002 / 003

| 002 layer | 003 treatment | in the `Gygax` folder |
| --- | --- | --- |
| A social / etiquette | **dropped** | still empty |
| B procedures of play | **kept** as `procedure.*` | present (session-flow, travel, encounter-setup, chargen) |
| C resolution engine | keep tag `rule.*`; expect empty | empty except CoC sanity |
| D catalogs | `entity.*` / `object.*` / tables | plus deities, hirelings, pregens |
| E fiction | `story.*` / `lore.*` | plus gazetteer, pantheon, festival; novel untaggable |

**Analysis.** 003 kind-tags remain the book-piece frame. Character relations are **not** a sixth layer and are **not** a new `entity.npc` subtype. The relation is the edge on the character card.

**Inference.** Mixed-system folders need `system_family` on the book. The 003 walk does not require a 5e chassis.

---

## 15. Unknowns

- The eight bookmark-less books (scans / image-heavy, including Necropolis).
- How GL2 compares to GL1 (`gl2thedreadfromgenevalake2coc.pdf` has no outline).
- Whether Northlands (`playersguidetothenorthlandsose.pdf`) would show species if it had headings.
- Gord as a novel versus a later prose pass — out of heading method.
- How well heading-tags match **actual tables** (groups skip chapters). Out of scope.

---

## 16. Recommendation

**Keep the 003 walk.** The unit is still the heading. Add `system_family` on mixed folders.

**Record characters as cards plus heading-backed edges.** Empty edge lists are allowed. Do not flatten names into one folder. Do not mint a social network.

**Do not begin product work or create another employee** unless Owner asks. The research question is answered at the document-structure level.

**Narrow follow-ups (only if Owner wants one)**

1. **Official 5e Sources** — same heading-walk on the sibling official folder (out of scope here).
2. **One adventure tagged as an edge table** — Eye of Itral or Yggsburgh; filename, page, kind, parent, then character cards with only heading-backed edges. Still no body text.
3. **OCR of scans** — a different method; not an extension of this walk.

**Analyst confidence:** **High** on the walk; **high** on the nine-edge card for this folder; **moderate** beyond it; **low** on the eight bookmark-less books.

---

## 17. Sources

Access date **2026-09-02**. Primary evidence is **document structure** of Owner-owned PDFs (bookmarks / publisher-public TOCs / filename), not quotations.

### Corpus

Owner's whole folder `TTRPGs/DnD/Gygax` on `Jasons-Mac.local` (32 PDFs attempted; 24 heading-level). Sibling folders out of scope.

Bookmark-less filenames:

1. `garygygaxsnecropolisd20.pdf`
2. `gl2thedreadfromgenevalake2coc.pdf`
3. `gordtherogue.pdf`
4. `heartofstbathusose.pdf`
5. `lakeofdustosr.pdf`
6. `playersguidetothenorthlandsose.pdf`
7. `spearsintheiceose.pdf`
8. `undercavernsofgaxmoorcandc.pdf`

Worked-example filenames named in this report:

9. `eyeofitralsw`
10. `candccastlezagygyggsburgh`
11. `bewaretheyulecatose`
12. `raslamasylumcc`
13. `fortunehunterssw`
14. `deitiesofthelostlands_vol1`
15. `gl1thedreadfromgenevalakecoc`
16. `tomeofhorrorscompletesw`
17. `to1talesfromokkorimg20`

Publisher/public TOC (no bookmark tree): Canting Crew; Living Fantasy.

Books named for edge strength or product identity, without a separate filename in this report: Eye of Itral; Raslam; Yggsburgh; Mithral Rattlesnakes; One Last Thing; Yule Cat; Spring Rites; Seanche's Lament; Deities vol.1; Orcus 34th; Cat's Cradle; Fortune Hunters; GL1; Tower (Dramatis Personae only); later Okkori; Lost Crypt; 1975; Tome of Horrors (three books); Necropolis; Gygax Fantasy Worlds; CoC Geneva Lake.

### Continuity

18. `research/assignments/003-ttrpg-structural-parts-schema.md` — vocabulary and tagging procedure
19. `research/assignments/002-ttrpg-core-components.md` — five-layer map; Layer A remains dropped
20. `agents/market-research-analyst/instructions.md`

---

## Appendix A — One-page tagging cheat sheet

**Unit:** heading / bookmark / publisher-public TOC row.  
**Ignore:** table etiquette, body prose, untitled art, sibling folders.

1. Label the **book**: `product_type` + `system_family`. Folder name is not system.
2. Walk the outline. Tag **kinds**:
   - Story tree: plot, then location, then (map as sibling); `story.scene` when festival events are headed
   - CoC: parts + Keeper + sanity (`rule.condition`) + pregens + handouts — not room letters
   - ToH: flat A–Z letter bucket — not Horde culture/lair
   - Deity-catalog: pantheon, then church, then god leaf
   - Gazetteer: fused residence + office title (person **is** the place)
   - New kinds only when needed: `entity.deity`, `lore.pantheon`, `entity.pc-option.background`, `reference.pregen`, `system.law`, `system.warfare`
3. If a heading **names a being**, open a character card.
4. Nine relations only: `inhabitant_of`, `owner_of`, `quest_giver_for`, `enemy_of`, `member_of`, `worships`, `rules`, `wields`, `appears_in`.
5. Edge only from nest, fused title, or *Working for X*. Maps sit beside rooms. Pregens `appears_in`; they do not inhabit a lodge. Hireling gallery may have zero edges.
6. Log gaps. Do not mint species, backstory, `allied_with`, or `knows`.

**If you only remember one sentence:** tag the book like 003, then record each named being as a card whose only ties are the ones the outline already printed.
