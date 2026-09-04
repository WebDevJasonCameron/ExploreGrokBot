# Research Assignment 002 — Core Components of Popular TTRPGs

**Report ID:** 002  
**Date:** 2026-09-01  
**Analyst:** Opportunity Researcher / Market Research Analyst (Employee 001)  
**Stage:** Structural taxonomy / component inventory  
**Status:** Complete — awaiting Owner review  
**Revision:** 2026-09-01c — additional free academic/designer citations for Owner review  
**Path:** `research/assignments/002-ttrpg-core-components.md`

This report asks whether popular tabletop RPGs can be dissected into shared components and how those components might be organized. It is **not** an opportunity scorecard, product pitch, or reactivation of any prior TTRPG software initiative.

Owner-confirmed corpus: D&D 5e (free SRD), Pathfinder 2e (Archives of Nethys), Call of Cthulhu 7e (free Quick-Start), Blades in the Dark (free SRD), Fate Core (free SRD), Cairn (CC-BY-SA SRD).  
Constraint: free public sources only; no paid sites, no outreach.

---

## 1. Executive Summary

**Yes — with caveats.** Popular TTRPGs can be broken into recurring components. The Owner’s hypothesized list (Game Mechanics, Story, Lore, Objects, Systems, Characters, Groups and relations) is a **workable first cut of fictional and rules *content***, but it mixes unlike layers and misses several components that every surveyed game actually documents.

**Most important findings**

1. **Fact.** Free rule documents already *categorize* play. The current D&D legal SRD is **5.2.1** (2024 rules): Playing the Game, Character Creation, Classes, Character Origins (species + backgrounds), Feats, Equipment, Spells, Rules Glossary, Gameplay Toolbox, Magic Items, Monsters, Animals. SRD **5.1** (2014) still listed races, pantheons, and planes; 5.2 **removed** Fantasy-Historical Pantheons and The Planes of Existence as “not rules-bearing,” renaming races to species. Pathfinder 2e’s Archives of Nethys split Player Core vs GM Core and further into ancestries, classes, skills, feats, equipment, spells, encounter/exploration/downtime modes, world-building (nations, settlements, planes), factions-adjacent subsystems, and treasure. Fate, Blades, and Cairn SRDs do the same with different labels. ([D&D Beyond SRD hub](https://www.dndbeyond.com/srd); [SRD 5.2.1 PDF](https://media.dndbeyond.com/compendium-images/srd/5.2/SRD_CC_v5.2.1.pdf); [SRD 5.1 TOC](https://dnd-srd-sphinx.readthedocs.io/en/latest/index.html); [Archives of Nethys Rules](https://2e.aonprd.com/Rules.aspx); [Fate SRD](https://fate-srd.com/); [Blades basics](https://bladesinthedark.com/basics/); [Cairn SRD](https://cairnrpg.com/first-edition/cairn-srd/))

2. **Observation.** Across the corpus, four *kinds* of thing keep appearing, not one flat list:
   - **Table / social procedure** (who speaks, GM vs player authority, principles, session shape)
   - **Resolution engine** (dice, fortune/karma/drama, position/effect, saves, clocks)
   - **Catalogs of game objects** (characters, items, creatures, spells/moves, conditions)
   - **Shared fiction** (situation, setting/lore, in-world institutions, relationships)

3. **Analysis.** The Owner’s categories mostly live in catalogs + shared fiction. They under-specify **how conflict is resolved**, **how time is sliced** (rounds, scores, downtime), and **the social contract**. Academic and Forge-era theory insist those layers exist even when a book does not title them. ([GNS / Big Model summaries](https://en.wikipedia.org/wiki/GNS_theory); [Analog Game Studies 2024 ontology essay](https://analoggamestudies.org/2024/10/a-tri-heuristic-ontological-approximation-of-tabletop-rpgs/))

4. **Observation.** Some components are **near-universal** (characters, a GM-like role, uncertainty resolution, fictional situation, consequences, objects/gear). Others are **system-family specific** (class/level, Sanity, Stress/Heat, Aspects/Fate points, inventory-as-HP, crew-as-character).

5. **Inference.** A useful organization is **layered**, not a single tree: (A) social play, (B) procedures of play, (C) resolution math, (D) entity catalogs, (E) fictional world. Owner categories map cleanly onto D and E once A–C are added.

**Is this area worth further investigation?**  
Yes, as **taxonomy work**. A follow-up could stress-test the map against 2–3 more systems or against how actual books vs actual tables diverge. It should not automatically become a software schema.

**Analyst confidence:** **Moderate-to-high** that the layers and near-universals are real; **moderate** that any one nesting (including the synthesized tree below) is *the* correct tree. Multiple valid organizations exist.

---

## 2. Research Question

Can the most popular TTRPGs be dissected and categorized into common core components, and how might those components be further organized — including subsets under headings such as mechanics, story, lore, objects, systems, characters, and groups/relations?

The investigation started from **documents and existing theory**, not from a product idea.

---

## 3. Method and Evidence Standards

**Window:** Sources accessed 2026-09-01; game texts spanning current free SRDs (D&D SRD 5.2.1 and 5.1; PF2e Nethys; Fate; Blades; Cairn 1e; CoC 7e Quick-Start).

**Signals used**

- Official or publisher-authorized free SRDs / quickstarts (primary for “what the game claims its parts are”)
- Archives of Nethys (Paizo-authorized PF2e reference)
- Open academic essays (Analog Game Studies; DiGRA)
- Secondary summaries of GNS / Big Model (Wikipedia, with Forge essays linked)

**Not used:** paid rulebooks, D&D Beyond subscription content, DriveThru storefronts, contacting publishers, pirated PDFs.

**Labels**

| Label | Meaning |
| --- | --- |
| **Fact** | Directly present in a named free document or official page |
| **Observation** | Recurring pattern across independent documents |
| **Analysis** | Structured interpretation for this assignment |
| **Inference** | Reasonable conclusion not stated by sources |
| **Unknown** | Material gap |

**Limitations**

- SRDs omit some setting IP and some GM advice that full books contain (especially D&D and CoC).
- CoC is represented by the **free Quick-Start**, not the Keeper Rulebook.
- Blades SRD **excludes** Duskwall setting IP; mechanics vs lore split is legally explicit. ([Blades licensing](https://bladesinthedark.com/node/33))
- No table observation / ethnography; this is document structure, not “how groups actually play.”
- Academic ontology papers often argue TTRPGs **resist** a single fixed definition; a catalog is a tool, not a complete ontology. ([Bastarrachea-Magnani et al. 2024](https://analoggamestudies.org/2024/10/a-tri-heuristic-ontological-approximation-of-tabletop-rpgs/))

---

## 4. Existing Frameworks (do not reinvent blindly)

### 4.1 GNS / Big Model (designer theory)

**Fact (secondary).** GNS theory (Ron Edwards, late 1990s–2000s, The Forge) groups *player creative agenda* as Gamism, Narrativism, Simulationism. The later **Big Model** nests: Social Contract → Exploration (shared imagined space) → Techniques → Ephemera, with Creative Agenda as a “skewer.” Exploration is described with five elements: **Character, Setting, Situation, System, Color**. ([Wikipedia: GNS theory](https://en.wikipedia.org/wiki/GNS_theory); Edwards essays linked there, e.g. [System Does Matter](https://en.wikipedia.org/wiki/GNS_theory#External_links))

**Analysis.** This is a theory of *why people play and how layers depend*, not a content taxonomy of spells and swords. It is still useful because it names layers the Owner list omits: **social contract**, **shared imagined space**, **system as “how events unfold.”**

**Counterevidence / criticism (Fact as reported).** Gleichman and others argue GNS confuses components of play with exclusive goals; Vincent Baker later called the model obsolete for fitting play into boxes. Use as a **partial map**, not gospel. ([Wikipedia criticism section](https://en.wikipedia.org/wiki/GNS_theory#Criticism))

### 4.2 Analog Game Studies: tri-heuristic ontology (2024)

**Fact.** Bastarrachea-Magnani, Meritano, and León argue RPGs are fluid and that feature-lists and taxonomies are insufficient as a *definition*. They propose heuristics: what RPGs are not; sufficient elements in play (including simulation/simulacrum, diegesis, interactive storytelling, self-regulation); and a “meta” crossing narrative, cognition, and social experience. ([Analog Game Studies 11.3](https://analoggamestudies.org/2024/10/a-tri-heuristic-ontological-approximation-of-tabletop-rpgs/))

**Analysis.** Academic caution: a component catalog can describe **documents and common practices** without claiming to *be* the phenomenon of play. This report follows that caution.

### 4.3 DiGRA game ontology meta-model (Aarseth & Grabarczyk)

**Fact.** Aarseth and Grabarczyk propose a four-layer mechanism model for comparing game ontologies (physical, structural, etc.) rather than one true list. ([DiGRA PDF](https://dl.digra.org/index.php/dl/article/download/973/973/970))

**Analysis.** Supports organizing TTRPGs as **multiple description layers**, which matches the SRD evidence below.

### 4.4 MDA (Hunicke, LeBlanc, Zubek 2004)

**Observation (via later TTRPG theses).** MDA splits Mechanics → Dynamics → Aesthetics. Useful reminder that a “mechanic” (dice) is not the same as the felt experience (fear, mastery). Owner “Game Mechanics” should not swallow Story’s emotional pacing. (Framework originally for digital games; applied to TRPGs in open theses such as SAE/CREO work citing MDA.)

### 4.5 Documentation structure as implicit taxonomy

**Observation.** The most empirical “component list” is **how publishers already chapter their free texts**. That is treated as primary evidence in §5.

---

## 5. Corpus Maps

### 5.1 D&D 5e — SRD 5.2.1 (current) and 5.1 (2014)

**Fact.** Two free legal SRDs exist. **SRD 5.2.1** (CC-BY-4.0; 2024 rules) top-level: Playing the Game (rhythm of play; d20 tests; actions; social interaction; exploration; combat; damage/healing); Character Creation; Classes; Character Origins (backgrounds + **species**); Feats; Equipment (incl. weapon masteries); Spells; Rules Glossary (actions, conditions, hazards, initiative, rest); Gameplay Toolbox (travel, curses/contagions, environment, fear/mental stress, poison, traps, combat encounters); Magic Items; Monsters; Animals. **SRD 5.1** additionally had Races (incl. Half-Elf/Half-Orc), Inspiration, Diseases/Madness appendices, **Fantasy-Historical Pantheons**, and **The Planes of Existence**. Wizards’ 5.1↔5.2 table states pantheons and planes were removed as not rules-bearing. The free D&D Beyond Basic Rules 2024 HTML adds explicit DM chapters (“What Does a DM Do?”, session prep) that the SRD PDF folds into Toolbox/Monsters; Wizards note Basic Rules is **not** the SRD. ([D&D Beyond SRD hub](https://www.dndbeyond.com/srd); [SRD 5.2.1 PDF](https://media.dndbeyond.com/compendium-images/srd/5.2/SRD_CC_v5.2.1.pdf); [SRD 5.1 TOC](https://dnd-srd-sphinx.readthedocs.io/en/latest/index.html); [Basic Rules 2024](https://www.dndbeyond.com/sources/dnd/br-2024))

**Mapping to Owner headings (Analysis)**

| Owner heading | SRD 5.2.1 clusters |
| --- | --- |
| Characters | Species, classes, backgrounds, alignment, languages, ability scores, feats |
| Game Mechanics | D20 tests, advantage, actions/bonus/reactions, combat, spellcasting, conditions, heroic inspiration, weapon masteries |
| Objects | Equipment, magic items, crafting potions/scrolls |
| Lore | **Almost none in 5.2** (language names, creature types, class fiction). Pantheons/planes were 5.1-only |
| Systems (in-world) | Travel/hazards/rests/attitudes; **no** faction, settlement, kingdom, or downtime-activity subsystem |
| Story | Rhythm of Play + three pillars (social/exploration/combat); Toolbox encounter tools; little plotted-adventure structure |
| Groups / relations | Party + NPC attitudes (Friendly/Indifferent/Hostile) + Influence action; hirelings; no first-class faction system |

**Missing vs full D&D books (Inference from SRD omissions):** setting gazetteers, most subclasses, downtime optional rules, adventure structure. **Analysis:** 5.2 is a **generic-fantasy rules chassis**. That is evidence that “lore” is optional in a *legal* component list even for the hobby’s most popular game — unlike PF2e, where Golarion is in Player Core.

### 5.2 Pathfinder 2e — Archives of Nethys (free)

**Fact.** Player Core chapters: Introduction (what is an RPG, basics, character creation, Golarion/religion); Ancestries & Backgrounds; Classes; Skills; Feats; Equipment; Spells; Playing the Game (checks, HP, actions, movement, **Encounter / Exploration / Downtime modes**); Conditions. GM Core: Running the Game; Building Games (campaign/adventure/encounter design, environment, hazards, building creatures/items/**worlds**); Age of Lost Omens (history, nations, settlements, planes); Subsystems (influence, research, chases, infiltration, **reputation**, leadership, hexploration, vehicles); Treasure. Additional books add gods, NPC relationships/connection subsystem, kingdoms, warfare, cults. ([Nethys Rules index](https://2e.aonprd.com/Rules.aspx))

**Observation.** PF2e is the **richest explicit taxonomy** in the corpus. It separately names:
- Character building blocks (ancestry, heritage, background, class, archetype, skill, feat)
- **Modes of play** (encounter / exploration / downtime)
- **World-building objects** (nations, settlements, planes, gods)
- **Social/institutional subsystems** (reputation, influence, leadership, kingdoms)
- GM-facing design procedures (how to build adventures, creatures, items)

**Analysis.** Owner “Systems” (governments, religions) appear here as **in-world institutions with optional subsystems**, distinct from dice mechanics. Owner “Groups and relations” appear as factions, reputation, connection/NPC relationship rules — first-class in later books, not only flavor.

### 5.3 Call of Cthulhu 7e — free Quick-Start (Chaosium)

**Fact.** Chaosium’s free Quick-Start presents: Investigator vs Keeper roles; investigator sheet clusters (identity/occupation, characteristics STR/CON/SIZ/DEX/APP/INT/POW/EDU, Luck, Sanity, Magic points, skills, combat stats, backstory/traits, gear); **game system** (skill rolls, difficulty, bonus/penalty dice, pushed rolls, opposed rolls, Luck); Sanity and temporary insanity; Combat (DEX order, fighting, damage); a full scenario (*The Haunting*) with locations, NPCs, handouts, Mythos tome/spell, SAN costs. Full investigator-creation and Keeper corpus live in paid books; Quick-Start uses pregens. ([Chaosium free PDF](https://www.chaosium.com/content/FreePDFs/CoC/CHA23131%20Call%20of%20Cthulhu%207th%20Edition%20Quick-Start%20Rules.pdf))

**Observation.** CoC makes **SAN / Mythos knowledge / occupation** first-class character components. Story is delivered as a **Keeper-owned plotted scenario** (locations, clues, antagonist abilities) more than as player-authored story engine.

**Analysis.** “Lore” here is both setting (Mythos) **and** a mechanical resource (Cthulhu Mythos skill, SAN loss). That blurs Owner Lore vs Mechanics — a useful stress test.

### 5.4 Blades in the Dark — free Forged in the Dark SRD

**Fact.** SRD covers: the game’s premise (crew of scoundrels); Players / Characters / **Crew** / GM roles; session as TV-episode with **score then downtime**; core rolls (action, resistance, fortune, downtime); 12 actions in 3 attributes (Insight, Prowess, Resolve); stress, trauma, armor; progress clocks including faction clocks; crew Tier, heat, entanglements, vice. Setting of Duskwall is **explicitly not in the SRD**. ([Basics](https://bladesinthedark.com/basics/); [Core System](https://bladesinthedark.com/core-system); [Actions & Attributes](https://bladesinthedark.com/actions-attributes); [Licensing](https://bladesinthedark.com/node/33))

**Observation.** **Crew is a character-like entity.** **Factions** have clocks and Tier. **Time** is procedural (free play → score → downtime). **Position/effect** and clocks are resolution/situation tools, not “lore.”

**Analysis.** Owner “Groups and relations” is **load-bearing mechanics** here, not a subset of color. Story is “play to find out,” not a pre-written plot chapter.

### 5.5 Fate Core — free SRD

**Fact.** Fate SRD presents Fate as setting-agnostic drama about proactive characters. Core pieces (from Fate Core documentation): characters built from **aspects, skills, stunts**; **fate points**; **four actions** (overcome, create an advantage, attack, defend); **stress and consequences**; **the ladder**; **game creation** (setting issues, faces/places) rather than a default world. Toolkit SRDs add adversaries, horror, space, accessibility. ([Fate SRD home](https://fate-srd.com/); [Fate Core basics](https://fate-srd.com/fate-core/basics))

**Observation.** Fate **collapses** “lore” into aspects on characters, scenes, and settings. “Objects” are usually aspects or extras, not a 40-page equipment chapter. “Story” is structural (issues, compels, consequences) more than plotted adventures.

### 5.6 Cairn — CC-BY-SA SRD

**Fact.** Cairn SRD TOC: Overview and **principles** (Warden + players); Character creation (name, background, traits, STR/DEX/WIL, HP, **inventory slots**, gear tables); Rules (saves, healing, deprivation, armor, reactions, morale, hirelings, wealth); Magic (spellbooks, relics); Combat; Bestiary / creating monsters; 100 spells. Fiction-first; classless; Warden as neutral arbiter. ([Cairn SRD](https://cairnrpg.com/first-edition/cairn-srd/))

**Observation.** **Principles of play** are first-class components (information, danger telegraphing, treasure-as-lure). Inventory is a mechanical constraint (full inventory → 0 HP). Story is **emergent** (random tables, not plots). Lore is minimal in the SRD; implied by bestiary and Wood framing.

---

## 6. Synthesized Component Taxonomy

**Analysis.** A practical organization uses **five layers**. Owner categories sit mostly in layers 4–5. Subsets below are illustrative, not exhaustive.

```text
Layer A. Table & social procedure
Layer B. Procedures of play (time, conversation, GM/player moves)
Layer C. Resolution engine (how uncertainty becomes fiction)
Layer D. Entity catalogs (who/what can be in play)
Layer E. Shared fiction / world (what it means)
```

### Layer A — Table & social procedure

**Near-universal.** Someone facilitates; others play characters; group agrees (implicitly or not) on tone and authority.

Subsets:

- Roles: GM / Keeper / Warden / Fate GM; players; sometimes rotating
- Social contract: safety, session length, who can say what about the world
- Creative agenda / principles: Cairn principles; PbtA “play to find out”; Blades “players are co-authors”
- Record-keeping: character sheets, clocks, maps, notes

Owner list: **not named**. GNS “Social Contract” covers this.

### Layer B — Procedures of play

**Near-universal as a *need*; highly variable as *form*.**

Subsets:

- Conversation loop: player declares → facilitator frames → resolve → narrate
- **Time units:** rounds/turns (D&D, PF2, Cairn, CoC combat); scores + downtime (Blades); scenes (Fate)
- **Modes:** PF2e encounter / exploration / downtime is the clearest named split; Blades free-play / score / downtime is analogous
- Adventure/situation structure: plotted scenarios (CoC *Haunting*); fronts/clocks (Blades/PbtA family); nodes/clues (investigative); random generation (Cairn)
- Prep vs improvisation norms

Owner “Story” (plots, pacing, highs/lows) lives **here as procedure** *and* in Layer E as events. Distinguishing those two is important.

### Layer C — Resolution engine

**Near-universal that *some* uncertainty resolver exists.**

Subsets:

- Randomizers: d20 (D&D/PF2), d20-under (Cairn), percentile (CoC), d6 pools (Blades), 4dF (Fate)
- Success spectrum: pass/fail; degrees (CoC regular/hard/extreme); position & effect (Blades); success-at-cost
- Resources spent to alter outcomes: inspiration, hero points, fate points, stress, luck, bonus/penalty dice, pushed rolls
- Initiative / turn order
- Damage, harm, conditions, clocks as “progress of trouble”
- Fortune vs karma vs drama (Tweet/Edwards resolution types)

Owner “Game Mechanics” is mostly this layer **plus** some Layer D rules (how a sword works). Splitting **engine** from **catalog** reduces mush.

### Layer D — Entity catalogs (game objects)

**Near-universal catalogs; contents differ.**

| Catalog | Typical subsets | Corpus notes |
| --- | --- | --- |
| **Player characters** | Identity; capabilities; resources; look/voice | D&D/PF2: ancestry/race, class, background, level. CoC: occupation, characteristics, SAN. Fate: aspects/skills/stunts. Cairn: 3 abilities + gear-defined role. Blades: playbook + actions + vice |
| **Non-player characters / creatures** | Stats, wants, tactics | All; PF2 and D&D huge bestiaries; Cairn “creating monsters” template; Fate adversaries toolkit |
| **Collective entities** | Party, crew, hirelings, detachments, kingdoms | Blades **crew**; Cairn hirelings/detachments; PF2 kingdoms/troops |
| **Items / objects** | Mundane gear, vehicles, magic/relics, treasure | Heavy in D&D/PF2/Cairn; light in Fate (extras/aspects) |
| **Powers / moves / spells** | Spells, feats, stunts, actions | Named differently; same job: permitted fictional operations with rules |
| **Conditions / statuses** | Exhaustion, harm, stress, heat, aspects on a scene | PF2 conditions appendix; Blades heat/stress; Fate scene aspects |
| **Places as mechanics** | Hazards, clocks on a location, claims | PF2 hazards; Blades claims/turf; CoC location keyed rooms |

### Layer E — Shared fiction / world

**Near-universal that play is *about* a fictional situation.** Thickness of published lore varies from Fate (bring your own) to PF2 Golarion / CoC Mythos.

Subsets matching Owner examples:

- **Situation / story-now:** what is at stake this session (GNS “Situation”)
- **Lore / setting / color:** history, cosmology, myths, tone, prejudices, genre expectations
- **In-world systems:** governments, religions, economies, laws, calendars, magic-as-institution
- **Geography / cosmology:** settlements, nations, planes, the Wood (Cairn), Duskwall (Blades book, not SRD)
- **Groups & relations:** factions, kinship, reputation, debts, clocks on relationships
- **Themes:** cosmic horror (CoC), criminal rise-and-fall (Blades), emergent exploration (Cairn), heroic adventure (D&D/PF2), dramatic competence (Fate)

---

## 7. Testing the Owner’s Hypothesis

| Owner category | Verdict | How to nest |
| --- | --- | --- |
| **Game Mechanics** | **Real, but too broad** if it includes both dice *and* “finances.” Split into **C. Resolution engine** vs **D. Resources/items** vs **E. in-world economy** | Subsets of C: dice, initiative, actions, degrees of success. Subsets of D: currency, inventory. Subsets of E: prices, jobs |
| **Story** | **Real as two things:** (1) procedures that produce pacing (B) and (2) fictional events/themes (E). Pre-written plot is common (CoC) but not universal (Blades, Cairn, Fate) | Plots, scenes, clocks, fronts, clues, “highs/lows” as **pacing tools**, not a single object type |
| **Lore** | **Real.** Myths, prejudices, genre expectations, cosmology. Sometimes mechanical (CoC Mythos skill) | Setting bible vs diegetic knowledge vs mechanical “lore skill” |
| **Objects** | **Real catalog.** Gear, relics, documents, vehicles | Mundane vs magical; slot/bulk; tags |
| **Systems** | **Ambiguous word.** In-world institutions (E) ≠ game system/engine (C). PF2 uses both senses | Recommend renaming in-world one to **Institutions** or **Diegetic systems** |
| **Characters** | **Real and central.** PCs, NPCs, creatures; sometimes crews | Identity, capabilities, resources, relationships, progression |
| **Groups and relations** | **Real; first-class in Blades/PF2, implied elsewhere** | Factions, party, crew, reputation, bonds, hirelings |

**What the hypothesis missed (Observation across corpus)**

1. Table/social layer and facilitation role  
2. Modes of play / session economy (downtime, scores, exploration)  
3. Resolution engine as distinct from “content”  
4. Principles/agendas of play (Cairn, PbtA/Blades)  
5. Progression/advancement as its own subsystem (XP, advances, scars, SAN, crew Tier)  
6. Information tools: maps, handouts, clocks, GM-facing secrets vs player-facing knowledge  

---

## 8. Universal vs System-Specific (comparison)

| Component | D&D 5e SRD | PF2e | CoC QS | Blades SRD | Fate | Cairn |
| --- | --- | --- | --- | --- | --- | --- |
| Facilitator role | Y | Y | Y (Keeper) | Y | Y | Y (Warden) |
| PCs with recorded stats | Y | Y | Y | Y | Y | Y |
| Uncertainty resolution | d20+mod | d20+mod | % skills | d6 pool | 4dF | d20-under |
| Fictional situation | Y | Y | Y (plotted) | Y (play to find out) | Y | Y (emergent) |
| Items/gear catalog | Heavy | Heavy | Light | Load/light | Minimal | Heavy (slots) |
| Class / playbook | Class | Class | Occupation | Playbook + Crew type | No class | Classless |
| Levels | Y | Y | Skill ticks | Advances / Tier | Skill pyramid / milestones | Scars / gear / in-world |
| Explicit modes (combat vs other) | Combat vs adventuring | Encounter/Explore/Downtime | Combat vs investigation | Score / downtime | Scenes | Combat vs free exploration |
| Sanity / horror meter | Optional madness | Afflictions | **SAN core** | Stress/trauma (adjacent) | Consequences | WIL / deprivation |
| Factions as mechanics | Weak in SRD | Reputation, nations | Scenario NPCs | **Core** | Faces & places | Reactions/morale |
| Published setting in free text | Thin (planes/gods) | **Golarion heavy** | Mythos assumed | **Excluded from SRD** | None default | Light Wood |
| Principles chapter | Sparse | GM advice books | Keeper advice in QS | Explicit co-authorship | Game creation | **First-class** |

Y = present in the free text consulted.

---

## 9. How Components Might Be Further Organized

Three organizations are **all valid**; they answer different questions.

### 9.1 Layered (recommended default)

A social → B procedures → C engine → D catalogs → E fiction.  
Best for **comparing games** and for later data models, because it does not force “story” to be a sibling of “sword.”

### 9.2 Book-shaped (how publishers already write)

Character creation → playing the game → equipment/magic → GM running → world/bestiary/treasure.  
Best for **navigation**. PF2e Nethys is the exemplar.

### 9.3 Play-shaped (what happens at the table, in order)

Sit down (A) → establish situation (E/B) → declare actions (B) → resolve (C) → update entities (D) → update fiction and relationships (E) → downtime/prep (B).  
Best for **session design** and for Owner “story pacing” questions.

**Story subsets** (Owner ask), placed:

- Premise / campaign frame → E + A  
- Scenario/front/score → B  
- Scene beats, highs/lows, clocks → B (pacing tools) acting on E  
- Character arcs → D (PC) × E (events)  
- Theme → E, sometimes enforced by C (SAN, stress, fate compels)

**Lore subsets:** cosmology; history; cultures; myths; prejudices/norms; genre tropes; secret truths (Mythos); player-facing vs GM-only.

**In-world systems subsets:** polity, law, religion, economy, military, magic-as-institution, information networks. PF2e subsystems operationalize several of these.

---

## 10. Unknowns

- How well this document taxonomy matches **actual tables** (many groups ignore chapters).
- Non-Anglophone popular games (e.g. Japanese TRPGs) — out of corpus.
- Full CoC Keeper Rulebook and full D&D/PF2 adventure-design chapters (paid).
- Whether a **single** data schema can hold both Cairn’s 12-page engine and PF2e’s encyclopedia without becoming PF2e-shaped.
- Owner’s intended use of this map (thinking tool vs later software). **Not assumed.**

---

## 11. Recommendation

**This assignment’s conclusion:** popular TTRPGs *can* be dissected into common components; the Owner’s headings are a good draft of **catalogs and fiction**; they should be wrapped in **social, procedural, and resolution** layers and should split the overloaded word “system.”

**Do not begin product work.**

**Narrow follow-up (if wanted):** `003-ttrpg-component-map-worked-examples` — take **one adventure/session** from two different families (e.g. CoC *The Haunting* vs a Blades score vs a Cairn crawl) and tag each beat with Layer A–E to see whether the map survives contact with play transcripts or published examples of play (Cairn includes one; Fate and Blades SRDs discuss session shape). Still taxonomy, still free sources.

**Analyst confidence:** **Moderate-to-high** on the layered claim; **moderate** on the exact subset lists.

---

## 12. Sources

Access date **2026-09-01** unless noted.

### Primary / free game texts

1. https://www.dndbeyond.com/srd — D&D SRD hub (5.1 and 5.2.1; CC-BY-4.0)  
2. https://media.dndbeyond.com/compendium-images/srd/5.2/SRD_CC_v5.2.1.pdf — SRD 5.2.1 PDF  
3. https://dnd-srd-sphinx.readthedocs.io/en/latest/index.html — SRD 5.1 table of contents reconstruction  
4. https://www.dndbeyond.com/sources/dnd/br-2024 — Basic Rules 2024 (free HTML; not the SRD)  
5. https://2e.aonprd.com/Rules.aspx — Pathfinder 2e Archives of Nethys rules index  
6. https://www.chaosium.com/content/FreePDFs/CoC/CHA23131%20Call%20of%20Cthulhu%207th%20Edition%20Quick-Start%20Rules.pdf — CoC 7e Quick-Start (free)  
7. https://bladesinthedark.com/basics/ — Blades SRD overview  
8. https://bladesinthedark.com/core-system — Blades core rolls and session cycle  
9. https://bladesinthedark.com/actions-attributes — Actions and attributes  
10. https://bladesinthedark.com/node/33 — SRD vs setting IP  
11. https://fate-srd.com/ — Fate SRD hub  
12. https://fate-srd.com/fate-core/basics — Fate Core basics  
13. https://cairnrpg.com/first-edition/cairn-srd/ — Cairn 1e SRD (CC-BY-SA 4.0)

### Academic / theory (free)

14. https://analoggamestudies.org/2024/10/a-tri-heuristic-ontological-approximation-of-tabletop-rpgs/ — Bastarrachea-Magnani, Meritano, León, Analog Game Studies 11.3 (2024)  
15. https://www.cristoleon.com/project/a-tri-heuristic-ontological-approximation-of-tabletop-rpgs/ — Same paper, project page  
16. https://dl.digra.org/index.php/dl/article/download/973/973/970 — Aarseth & Grabarczyk, DiGRA ontological meta-model  
17. https://en.wikipedia.org/wiki/GNS_theory — GNS summary + links to Edwards Forge essays  
18. https://rpgmuseum.fandom.com/wiki/Big_Model — Big Model nested boxes (secondary)  
19. https://creo.sae.edu.au/cgi/viewcontent.cgi?article=1024&context=postgraduate — Open thesis applying MDA to TRPGs (secondary use of MDA)

### Additional free theory, adventure-structure, and data-model sources (for later review)

These did not change the five-layer conclusion. They are listed because the assignment asked for academic and designer sources the Owner can open later.

20. http://www.indie-rpgs.com/articles/1/ — Edwards, “GNS and Other Matters of Role-playing Theory”  
21. http://www.indie-rpgs.com/_articles/system_does_matter.html — Edwards, “System Does Matter”  
22. http://indie-rpgs.com/_articles/glossary.html — Edwards, “The Provisional Glossary” (Big Model component list; Lumpley Principle)  
23. https://www.darkshire.net/jhkim/rpg/theory/threefold/ — Threefold Model (GDS) FAQ  
24. https://dl.digra.org/index.php/dl/article/view/136 — Zagal et al., Game Ontology Project (DiGRA 2005)  
25. https://arxiv.org/html/2007.06108v2 — Guzdial et al., “Tabletop Roleplaying Games as Procedural Content Generators” (FDG 2020)  
26. https://thealexandrian.net/wordpress/1118/roleplaying-games/three-clue-rule — Justin Alexander, Three Clue Rule  
27. https://thealexandrian.net/wordpress/7949/roleplaying-games/node-based-scenario-design-part-1-the-plotted-approach — Node-based scenario design  
28. https://slyflourish.com/eight_steps_2023.html — Mike Shea, Eight Steps of Lazy DM prep  
29. https://www.dungeonworldsrd.com/gamemastering/fronts/ — Dungeon World Fronts (PbtA GM prep objects)  
30. https://www.roleplayingtips.com/5-room-dungeons/ — Johnn Four, 5-Room Dungeon  
31. https://pelgranepress.com/2020/10/16/see-page-xx-how-to-design-for-gumshoe/ — Laws, GUMSHOE investigation structure  
32. https://foundryvtt.com/article/system-data-models/ — Foundry VTT document types (implemented Actor/Item ontology)  
33. https://paizo.com/blog/orc-license-the-final-version-is-here — ORC license (legal split: mechanics vs reserved setting/IP)  
34. https://lumpley.games/2019/12/30/powered-by-the-apocalypse-part-1/ — Vincent Baker, PbtA concentric design  
35. http://apocalypse-world.com/ — Apocalypse World free playbooks / MC sheets

### Company documents

36. `agents/market-research-analyst/instructions.md`  
37. `company/opportunity-criteria.md` (not scored; assignment was taxonomy-only)

---

## Appendix A — Suggested one-page cheat sheet

**If you only remember one organization:**

1. **People at a table** (roles, principles, safety)  
2. **How a session runs** (scenes, modes, scores, downtime, prep)  
3. **How you roll / decide** (engine + resources)  
4. **Sheets and lists** (characters, stuff, monsters, powers, conditions)  
5. **The imagined world** (situation, lore, institutions, relationships)

Owner labels map to 4 and 5, with “mechanics” covering 3 plus some of 4, and “story” covering 2 plus some of 5.

