# Research Assignment 006 — TTRPG Definition vs Instantiation Across Systems

**Report ID:** 006  
**Date:** 2026-09-10  
**Analyst:** Opportunity Researcher / Market Research Analyst (Employee 001)  
**Stage:** Cross-system definition vs instance inventory  
**Status:** Complete — awaiting Owner review  
**Path:** `research/assignments/fromResearcher1/006-ttrpg-definition-vs-instantiation.md`

This report asks how free-source TTRPG systems represent **reusable definitions** (a class, a creature type, a spell name, a threat kind) versus **instantiated objects** (this campaign, this filled sheet, this encounter’s HP, this clock with ticks). It is a cross-system inventory of the same question Assignment 005 asked of gazetteers and adventures: what can be pointed at from more than one story, and what is only this run of play?

It is **not** an opportunity scorecard, product pitch, software design, data schema, or reactivation of any prior TTRPG PDF-ingestion initiative. No copyrighted book prose is reproduced here. No Mahogany schema is proposed. Vocabulary stays as system-independent as the corpus allows; when a system’s own word is load-bearing (playbook, Role, SAN, claim), that word is kept.

Continuity: Assignment 002 split catalogs (Layer D) from procedures of play (Layer B) and shared fiction (Layer E). Assignment 003 tagged book headings and found story trees nested under adventures, with people and items often as children of rooms. Assignment 004 recorded named beings as cards plus nine heading-backed edges, and allowed a hireling gallery with **zero** edges. Assignment 005 preferred **Person `appears_in` Campaign** and **Adventure `uses_asset` Person** over exclusive ownership. This assignment does not walk a new PDF folder. It asks the next question of free rule texts: **when a system prints a thing, is it printing a definition, an instance, or both?**

**Core finding (Inference, grounded below).** Instantiation is **reference plus overlay**, not exclusive ownership. A Fighter class, a goblin type, or a MotW Monster kind is a Layer D catalog entry. A filled sheet, a room’s occupant, or a mystery countdown is Layer B context sitting on that entry. The same pattern 005 already named: `appears_in` / `uses_asset`. Systems disagree which side they treat as primary.

**Do not begin product work.**

---

## 1. Executive Summary

**Yes — free-source TTRPG systems already split reusable definitions from instantiated play objects.** They disagree which side is the book’s spine. Catalog-heavy games print types first and treat filled sheets as loads on those types. Instance-heavy games print unique sheets, situations, and threats first and treat catalogs as thin or optional. Quick-starts often skip the catalog and ship pre-instantiated people and one scenario.

**Most important findings**

1. **Analysis (continuity 005).** Layer D catalogs (classes, creature types, spells, item names, condition types, threat kinds) are reusable definitions. Layer B context (campaign, adventure, encounter, session, score, mystery, clock) is where those definitions get **referenced and overlaid** with current meters, applied conditions, and ticks. Instantiation is not exclusive ownership. Person `appears_in` Campaign; Adventure `uses_asset` Person still holds when the “person” is a filled sheet pointing at a class, occupation, playbook, or Role.

2. **Observation.** Nearly every concept in the inventory is **both** a definition and an instance *somewhere* in the nine-system corpus. Systems disagree which side is primary. D&D SRD 5.2.1, Pathfinder 2e Archives of Nethys, and Old-School Essentials are **catalog-heavy**. Fate Core, Apocalypse World / Monster of the Week, and Blades in the Dark are **instance-heavy**. Call of Cthulhu 7e Quick-Start and Cyberpunk RED Easy Mode (and, on the free text, Savage Worlds Test Drive) are **pre-instantiated**: named sheets plus one scenario, with the full catalog living in unpaid books.

3. **Observation.** The strongest shared pattern is **template → sheet instance with mutable meters**. A class / playbook / Role / occupation / ancestry bundle is the definition. The filled character is the instance. HP, stress, SAN, heat, Luck, Humanity, bennies, and fate points are overlays on that instance. The template does not own the current number.

4. **Observation.** Creatures split four ways, not one. OSR (OSE, and Cairn’s short bestiary notes) prints **HD + Number Appearing** (or a one-line fiction + a few numbers). PF2 and D&D print **rich stat blocks** that are already almost-instances of a type. Cairn often prints **short fiction plus a creating-monsters recipe**. Apocalypse World and Monster of the Week print **threat kinds** (warlord / grotesque / monster / minion) whose job is impulse and countdown, not a reusable combat catalog.

5. **Inference.** **Component-candidates** are the publisher catalogs and reusable sheets: creature types, species/ancestry, class/playbook/Role/occupation, ability defs, spell/power defs, item defs, condition types, reusable locations/factions, claim slot types, threat kinds, deities/lore catalogs. **Non-Components** are ephemeral runtime, rules procedures, edges treated as if they were entities, and adventure ownership of beings. Investigate later; do not implement.

**Analyst confidence:** **High** that the definition / instance split is real across the nine free texts; **moderate** on crew / spell-as-item / threat-kind boundaries (those three sit on the line); **low** on unpaid full-book depth for Savage Worlds and Cyberpunk RED (this pass used Test Drive and Easy Mode only).

---

## 2. Research Question

If we look only at free-source texts from nine popular TTRPG families, how does each system represent **reusable definitions** versus **instantiated objects** — campaigns, adventures, encounters, characters, worlds — and which concepts behave as definitions, instances, both, or probably not a Component?

Constraints from Owner:

- Research markdown only. No software schema. No Mahogany design. No Rust, YAML, database, or UI.
- Free sources only.
- Label **Fact / Observation / Analysis / Inference / Unknown**.
- Continuity with Assignments 002–005, including Layer D vs Layer B and `appears_in` / `uses_asset`.
- Filed under `fromResearcher1`.
- Do not invent beyond this brief.

---

## 3. Method and Sources

**Window:** Sources accessed 2026-09-10.

**Signals used**

- Continuity documents: Assignments 002, 003, 004, 005 (layers; heading nest; nine edges; independent vs play-context).
- Free SRDs and publisher-authorized free texts already in the 002 corpus, plus the additional free texts named for this pass.

**Systems (Owner-confirmed free corpus for this pass)**

| System | Free text used |
| --- | --- |
| D&D 5e | SRD 5.2.1 |
| Pathfinder 2e | Archives of Nethys |
| Call of Cthulhu 7e | Quick-Start |
| Cyberpunk RED | Easy Mode (plus publisher Easy Mode / Single Shot pages for what the free booklet contains) |
| Savage Worlds | Test Drive |
| Blades in the Dark | Forged in the Dark SRD |
| Fate Core | Fate SRD |
| Apocalypse World + Monster of the Week | AW 2e threats preview; MotW free playbooks and mystery/arc sheet |
| Cairn + Old-School Essentials | Cairn 1e SRD; OSE SRD / online rules reference |

**Not used**

- Paid core books (full CoC Keeper Rulebook, full Cyberpunk RED, full Savage Worlds Adventure Edition, full MotW hardcover, full AW book).
- Body prose from paid adventures.
- A new PDF-folder walk.
- Software, vault, or storage design.
- Invented ownership graphs or schemas.

**Labels**

| Label | Meaning |
| --- | --- |
| **Fact** | Directly present in a named free page, SRD, or prior assignment heading record |
| **Observation** | Recurring pattern across independent products or texts |
| **Analysis** | Structured interpretation for this assignment |
| **Inference** | Reasonable conclusion not stated by the sources |
| **Unknown** | Material gap |

**Limitations**

- Quick-starts and Test Drive / Easy Mode **pre-instantiate** and omit most of the unpaid catalog. Claims about SW and CPR full-book depth are **Unknown** except where publisher pages describe what the free booklet includes.
- Blades SRD excludes Duskwall setting IP (already flagged in 002 and 005).
- MotW free files are playbooks, reference sheets, and a mystery worksheet — not the full Keeper chapter.
- AW evidence here is the free threats preview (types, impulses, map, clocks), not the complete 2e book.
- No table ethnography: this is document structure, not how a given group actually copies a goblin.

---

## 4. System Snapshots

One short subsection each. The question is always: **what does this free text treat as a reusable definition, and what does it treat as an already-filled instance?**

### 4.1 D&D SRD 5.2.1 — catalog first, sheet as load

**Fact.** SRD 5.2.1 chapters are Playing the Game; Character Creation; Classes; Character Origins (species + backgrounds); Feats; Equipment; Spells; Rules Glossary; Gameplay Toolbox; Magic Items; Monsters; Animals. ([D&D Beyond SRD hub](https://www.dndbeyond.com/srd); [SRD 5.2.1 PDF](https://media.dndbeyond.com/compendium-images/srd/5.2/SRD_CC_v5.2.1.pdf); Assignment 002 §5.1)

**Analysis.** The legal free text is a **definition catalog**. A class (Fighter), a species, a named spell, a condition in the glossary, and a monster type are reusable. The filled character — current HP, spell slots remaining, which species×class bundle this person is — is an instance that `uses_asset` those definitions. The SRD does not print a campaign object that owns the Fighter class.

**Observation.** Many people can be Fighters. The class is not unique to one PC. That is the opposite of a PbtA playbook table-norm (one Chosen at the table).

### 4.2 Pathfinder 2e (Archives of Nethys) — richest catalog, ancestry × class

**Fact.** Player Core / GM Core on Nethys split ancestries and backgrounds, classes, skills, feats, equipment, spells, Playing the Game (Encounter / Exploration / Downtime), conditions, world-building (nations, settlements, planes), subsystems, treasure, and creature-building. ([Nethys Rules index](https://2e.aonprd.com/Rules.aspx); Assignment 002 §5.2)

**Fact.** NPC gallery blocks are written as humans; ancestry is applied as an **adjustment** (change trait, add language/senses/speed). Important NPCs are pointed at full creature-creation rules. ([NPC Ancestry Adjustments](https://2e.aonprd.com/Rules.aspx?ID=1401); [Ancestry Adjustments](https://2e.aonprd.com/Rules.aspx?ID=3369))

**Analysis.** PF2 is catalog-heavy **and** combinatorial: ancestry × heritage × background × class is the definition bundle; the creature/NPC block is a rich, almost-instantiated print of a type. Encounter mode is Layer B wrapping those blocks. The type remains reusable.

### 4.3 Call of Cthulhu 7e Quick-Start — pre-instantiated investigators + one scenario

**Fact.** The free Quick-Start presents Investigator vs Keeper; sheet clusters (identity/occupation, characteristics, Luck, Sanity, magic points, skills, combat, backstory/traits, gear); resolution; SAN; combat; and a full scenario (*The Haunting*) with locations, NPCs, handouts, a Mythos tome/spell, and SAN costs. Full investigator-creation lives in paid books; the Quick-Start uses pregens. ([Chaosium free PDF](https://www.chaosium.com/content/FreePDFs/CoC/CHA23131%20Call%20of%20Cthulhu%207th%20Edition%20Quick-Start%20Rules.pdf); Assignment 002 §5.3)

**Analysis.** Occupation is a **definition-like slot** (skill package, Credit Rating band) but the free text mostly ships **instances**: named pregens and one plotted scenario. SAN and Luck are mutable meters on the instance. *The Haunting* `uses_asset` locations and NPCs; it does not publish a reusable occupation catalog the way the SRD publishes classes.

### 4.4 Cyberpunk RED Easy Mode — Roles as taste, five named Edgerunners, one mission

**Fact.** Publisher copy: 48-page Free RPG Day / free PDF introduction; Night City geography; skill-check and combat rules; a scaled-down Lifepath; five pregens (Forty the Rockerboy, Mover the Solo, Torch the Tech, Redtail the Medtech, 24/7 the Media) each with a **simplified Role Ability**; introductory mission *Getting Paid*. ([R. Talsorian Free RPG Day 2022](https://rtalsoriangames.com/2022/06/25/free-rpg-day-2022/); [Talsorian store Easy Mode](https://talsorianstore.com/products/cyberpunk-red-easy-mode))

**Fact (adjacent free packet, not Easy Mode body).** The free Single Shot Pack states Role is “akin to a class,” lists ten STATS including spendable **Luck**, current vs max **HP** and **Humanity** (Humanity tied to Empathy and lowered by cyberware), and ships one pregen per Role. ([Single Shot Pack PDF](https://rtalsoriangames.com/wp-content/uploads/2021/02/RTG-CPRed-SingleShotPackv1.1.pdf))

**Analysis.** Easy Mode is **pre-instantiated**. Role is a reusable definition in the unpaid core (Unknown here beyond publisher description). The free booklet’s primary objects are five named people plus one mission. Humanity and Luck are meters on the instance.

**Unknown.** Full Role catalog, full Lifepath, and Night City gazetteer depth in the unpaid core book.

### 4.5 Savage Worlds Test Drive — archetypes, bennies, one Deadlands tale

**Fact.** Official Test Drive is a free PDF with pregenerated **archetype** characters, Power Cards, combat rules, and *Blood on the Range* (Deadlands: the Weird West). Full Adventure Edition is a separate paid book. ([PEG: Start Here](https://peginc.com/new-to-savage-worlds-start-here/); [PEG: Test Drive announcement](https://peginc.com/take-savage-worlds-deadlands-out-for-a-free-test-drive/); [DriveThru listing](https://www.drivethrurpg.com/en/product/339651/savage-worlds-adventure-edition-test-drive))

**Fact (older free Test Drive text, 2015 PDF still posted).** Wild Cards roll a Wild Die; each player starts a session with three **Bennies** (reroll trait tests, remove Shaken, Soak); Bennies do not save between sessions. ([2015 Test Drive PDF](https://www.peginc.com/wp-content/uploads/2015/07/Test_Drive_2015.pdf))

**Analysis.** On the free text, Savage Worlds looks **instance-first**: named archetypes and one adventure, plus a session-scoped luck token. Edges, Hindrances, and Powers are definition-shaped on the sheet and on Power Cards, but this pass did not open the unpaid SWADE catalog.

**Unknown.** How complete the unpaid core’s Edge / Power / creature catalogs are relative to D&D/PF2. Confidence on SW is **low** by design of the free window.

### 4.6 Blades in the Dark (FitD SRD) — playbook + crew as sheets; heat, clocks, claims as state

**Fact.** A playbook is the sheet for a character type: special abilities and XP triggers, not an “immutable essence.” Creation also chooses heritage, background, action dots, friend/rival, vice, and **load** per operation. ([Character Creation](https://bladesinthedark.com/character-creation))

**Fact.** Crew is created beside characters: crew type, lair, upgrades, claim map, Tier, hold, coin, reputation. Claims are seized; holding grants listed benefits until lost. ([The Crew](https://bladesinthedark.com/crew); [Faction Game](https://bladesinthedark.com/faction-game); Assignment 005 §5.2, §5.9)

**Fact.** After a score the crew takes **heat**; at 9 heat a wanted level lands and heat clears with rollover. Downtime can Reduce Heat. Stress is personal; filling the stress track causes **trauma**. ([Heat](https://bladesinthedark.com/heat); [Downtime](https://bladesinthedark.com/downtime-activities); Assignment 002 §5.4)

**Analysis.** Playbook and crew **type** are definitions. The filled playbook, the filled crew sheet, current heat, held claims, clocks with ticks, and friend/rival marks are instances / overlays. 005 already split claim **type** from **held** state. Session shape (score → downtime) is Layer B, not a catalog object.

### 4.7 Fate Core SRD — aspects live on instances; issues are campaign-facing

**Fact.** Fate is setting-agnostic. Characters are aspects, skills, stunts, fate points, four actions, stress and consequences, the ladder. Game creation writes setting issues and faces/places rather than a default world. ([Fate SRD home](https://fate-srd.com/); [Basics](https://fate-srd.com/fate-core/basics); Assignment 002 §5.5)

**Fact.** An aspect is a phrase attached to *whatever it describes* (character, scene, location, game). Fate points are a pool; players reset toward refresh; the GM budgets points per scene. ([Aspects & Fate Points](https://fate-srd.com/fate-core/aspects-fate-points))

**Fact.** Current and impending issues are aspects for the whole game; they can later attach to a location or organization and can change or resolve. ([Setting’s Big Issues](https://fate-srd.com/fate-core/settings-big-issues); Assignment 005 §5.8)

**Observation.** Fate **collapses** catalog into phrases on instances. A feat-like stunt is a definition-shaped exception. A **boost** is a fleeting extra (succeed-with-style leftover) — more instance than catalog. There is no Monster Manual-shaped creature type list in Core.

**Analysis.** Fate is instance-heavy. The reusable pieces are procedures (actions, ladder, stress boxes) and the *habit* of writing aspects — not a publisher bestiary.

### 4.8 Apocalypse World threats preview + MotW free playbooks / mystery sheet — unique sheets, threat kinds

**Fact.** AW 2e threats preview lists threat **types** with subtypes and impulses: Warlords (slaver, hive queen, prophet, dictator, collector, alpha wolf); Grotesques; Brutes; Afflictions (disease, condition, custom, delusion, sacrifice, barrier); Landscapes; plus essential-threat recipes (where the PCs are → landscape; gangs → brutes; local populations → affliction) and countdown clocks. ([AW 2e Threats Preview PDF](http://apocalypse-world.com/AW2ndEdThreatsPreview.pdf))

**Fact.** MotW free downloads include consolidated hunter playbooks and a mystery/arc preparation sheet with Concept, Hook, Countdown (Day → Shadows → Sunset → Dusk → Nightfall → Midnight), and Threat lines (Name, Type: Monster /, Motivation, Powers, Weaknesses, Attacks, Armour, Harm Capacity). ([Evil Hat MotW page](https://evilhat.com/monster-of-the-week/); [Mystery/Arc sheet](https://evilhat.com/wp-content/uploads/2022/01/Monster-of-the-Week-Revised-Mystery-Worksheet.pdf))

**Fact.** A MotW playbook (example: Action Scientist) is a unique filled-in-progress sheet: ratings, moves, gear picks, Luck boxes, Harm, History with the other hunters. Luck is marked to change a roll to 12 or avoid all harm; spending Luck also fires a playbook-specific complication. ([Consolidated playbooks 2025](https://evilhat.com/wp-content/uploads/2023/01/Monster-of-the-Week-Hunter-Playbooks-Consolidated-2025.pdf))

**Analysis.** PbtA here is **instance-heavy**. The playbook is a one-table unique role more than a many-of-class catalog. The reusable definition is the **threat kind** (monster / minion / phenomenon; warlord / landscape), not a goblin HD line. The mystery sheet is a Layer B instance: this countdown, these named threats.

### 4.9 Cairn SRD + OSE SRD — classless gear-role vs demihuman-as-class; spell-as-item vs Vancian; HD+NA

**Fact.** Cairn is classless: role is equipment and experience, not a class. Spellbooks contain a single spell, take one inventory slot, cannot be transcribed or created in the SRD procedure, and are recovered from tombs and manors. Anyone casts by holding the book in both hands; casting adds Fatigue to inventory. The SRD includes a creating-monsters section and a 100-spell list. ([Cairn SRD](https://cairnrpg.com/first-edition/cairn-srd/); Assignment 002 §5.6)

**Fact.** OSE prints **demihuman classes**: Dwarf, Elf, Halfling are classes with their own HD, level caps, and (for Elf) spell tables — not an ancestry multiplied by Fighter/Wizard. ([OSE SRD: Dwarf](https://oldschoolessentials.necroticgnome.com/srd/index.php/Dwarf); [Elf](https://oldschoolessentials.necroticgnome.com/srd/index.php/Elf); [Halfling](https://oldschoolessentials.necroticgnome.com/srd/index.php/Halfling))

**Fact.** OSE monsters list **Number Appearing (NA)** as two values (dungeon wandering vs lair/wilderness), scaled by HD and locale. ([OSE SRD: Game Statistics (Monsters)](https://oldschoolessentials.necroticgnome.com/srd/index.php/Game_Statistics_(Monsters)))

**Analysis.** Both are catalog-shaped, but the catalogs disagree. OSE: class (including demihuman-as-class) and monster type (HD+NA) are definitions; a keyed room’s 2d4 goblins are instances. Cairn: the spell **definition** lives on an **item instance** (this book in this slot); the bestiary is short fiction plus a recipe more than a PF2 block.

---

## 5. Concept Classification Table

**Observation.** “Both” is the common cell. The interesting disagreement is which side the book treats as primary.

| Concept | Classification | Primary-side note |
| --- | --- | --- |
| Characters | **Both** | Template/playbook/Role vs filled sheet + meters |
| NPCs | **Both** | Gallery/pregen vs this adventure’s named person |
| Creatures | **Both** | Type (HD+NA / rich block / threat kind) vs this encounter’s bodies |
| Species / ancestry | **Definition** (OSE: fused into class) | PF2/D&D catalog; OSE demihuman-as-class |
| Classes / archetypes / playbooks / Roles / occupations | **Both** | Many-of-class (D&D/PF2) vs unique playbook (PbtA) vs occupation package (CoC) vs Role (CPR) |
| Abilities | **Both** | Feat/stunt/move/Role Ability def vs this sheet’s picks |
| Spells / powers | **Both** | Vancian named list vs Cairn spell-as-item vs SW Power Cards |
| Items | **Both** | Gear catalog vs this inventory / this loadout |
| Locations | **Both** | Gazetteer site vs this scene’s staging |
| Factions | **Both** | Org as object vs this crew’s status number |
| Quests / scores / mysteries / scenarios | **Instantiated** (defs are thin templates) | 5-room / mystery sheet / score cycle are procedures; *The Haunting* / *Getting Paid* / *Blood on the Range* are instances |
| Events | **Instantiated** (mostly) | Festival scene, compel event; rarely a reusable catalog |
| Conditions / effects | **Both** | Condition type vs applied stack on a body |
| Encounters | **Instantiated** (default) | OSE NA can generate them from a type; not a publisher catalog of “Encounter #14” as a Component |
| Timelines / clocks | **Both** | Clock as procedure vs this clock with ticks |
| Rules | **Probably not a Component** | Procedures of play (Layer B/C), not a reusable in-world object |
| Resources / meters | **Instantiated** (type is a def) | HP/stress/SAN/heat/Luck/Humanity **values** are overlays |
| Tags / traits | **Definition-ish; probably not objects** | Labels on defs; do not mint as entities |
| Relationships | **Instantiated** (edges, not entities) | 004: heading-backed edges; Blades friend/rival marks; Fate aspects |
| Clocks (extra) | **Both** | See timelines |
| Stress / trauma | **Both** | Stress is a meter; trauma is a lasting mutation on the instance |
| Heat | **Instantiated** | Crew-level overlay; 005 already called it campaign state |
| Aspects / boosts | **Both / boosts instantiated** | Aspects can persist; boosts are ephemeral |
| Fronts / threats | **Both** | Kind is a def; this front/threat is instance |
| Claims | **Both** | Slot type vs held claim |
| Humanity | **Instantiated** (meter) | CPR Easy Mode / Single Shot; current vs max |
| SAN | **Instantiated** (meter) | CoC QS; current Sanity on the investigator |
| Bennies / Fate points / Luck | **Instantiated** | Session or scene pools; MotW Luck boxes on the playbook |

---

## 6. Per-Concept Writeups

Each writeup stays brief. Examples are bibliographic or SRD-structural, not quoted adventure prose.

### 6.1 Characters

**Fact.** Every free text in the corpus has a filled or fillable PC record: D&D/PF2 creation chapters; CoC/CPR/SW pregens; Blades playbook; Fate character; MotW hunter playbook; Cairn 3-ability + inventory; OSE class + HP.

**Analysis.** The **definition** is the bundle the book lets you reuse (class + species; playbook; Role; occupation). The **instance** is this named person with current meters. Pregens (`reference.pregen` in 004) are instances that still `appears_in` a scenario.

**Divergence.** D&D/PF2 expect many instances per class definition. PbtA expects one instance of a given playbook at the table. CoC QS / CPR Easy Mode / SW Test Drive skip straight to instances.

### 6.2 NPCs

**Fact (004).** Named beings may open a card (`entity.npc`) with nine edges or **zero** (Fortune Hunters).

**Fact.** Fate lists faces beside issues. Blades playbooks list friend/rival names to mark. CoC QS and the three quick-starts embed named NPCs in one scenario.

**Inference.** An NPC **type** (PF2 gallery “guard,” OSE Veteran) is a definition. A named shopkeeper is an instance that may be reusable (005 Greyhawk folk) or local (keyed-room occupant). Adventure does not own them (`uses_asset`).

### 6.3 Creatures

**Observation.** Four print styles:

| Style | Systems | Definition vs instance |
| --- | --- | --- |
| HD + Number Appearing | OSE (OSR) | Type is the def; NA rolls instances |
| Rich stat block | D&D SRD monsters; PF2 creatures | Block is a heavy def that is already playable as an instance |
| Short fiction + recipe | Cairn bestiary / creating monsters | Kind + a few numbers; Warden instantiates |
| Threat kind | AW preview; MotW mystery sheet | Impulse/motivation def; this monster is the instance |

**Analysis.** Unique named monsters (005: Halaster) behave like **Person**. Alphabetized types behave like 004’s Tome of Horrors cards with no lair edge.

### 6.4 Species / ancestry

**Fact.** D&D 5.2.1: species under Character Origins, combinable with class. PF2: ancestry + heritage, combinable with class; NPC ancestry is an adjustment on a human block. OSE: Dwarf/Elf/Halfling **are** classes.

**Contradiction (see §8).** OSE demihuman-as-class vs PF2 ancestry × class is the same fictional person split two incompatible ways.

### 6.5 Classes / archetypes / playbooks / Roles / occupations

**Fact.** D&D/PF2: many characters share a class. Blades: playbook is focus, not unique essence — but it is still *this table’s* Cutter. MotW/AW: playbooks are unique-at-table in normal use. CoC: occupation is a skill/Credit package, not a level track. CPR: Role + Role Ability; Easy Mode ships five named Roles as people.

**Analysis.** All five words do the **PC-option** job (002 Layer D; 003 `entity.pc-option`). They disagree on cardinality (many vs one) and on whether fiction (occupation, Role) is also a combat class.

### 6.6 Abilities

**Fact.** D&D feats; PF2 feats; Fate stunts; Blades special abilities; MotW moves; CPR Role Ability; SW Edges (sheet-shaped on Test Drive).

**Inference.** The named ability is a definition. The checkbox on this sheet is the instance. Do not store “has Iron Will” as a separate world entity; it is a `uses_asset` from the character instance to the ability def.

### 6.7 Spells / powers

**Fact.** D&D/PF2/OSE: named spell lists; prepared/known slots are instance state (Vancian-family). Cairn: the spell **is** a slot-filling spellbook item. SW Test Drive: Power Cards as playable power instances. CoC QS: a tome/spell inside *The Haunting*, not a PHB-sized list.

**Contradiction (see §8).** Cairn spell-as-item vs Vancian named catalog.

### 6.8 Items

**Observation (002–003).** Heavy catalogs in D&D/PF2/Cairn/OSE; Blades **load** (declare later); Fate extras/aspects; CoC QS light gear on pregens.

**Analysis.** Item **type** (longsword, infirmary claim slot, spellbook) is a definition. This carried object, this loadout, this attunement is instance overlay. 004 `wields` attaches instance to person without the adventure owning the type.

### 6.9 Locations

**Fact (005).** Gazetteers print settlements and sites as independents. Adventures `uses_asset` them. AW treats **landscape** as a threat type. CoC QS / CPR / SW free texts key locations inside one scenario.

**Inference.** Reusable site = definition-ish independent object. “Room 12 of this dungeon crawl” may be only an instance with no second appearance (005 counter-pattern).

### 6.10 Factions

**Fact.** Blades: factions have status (−3..+3) and claim maps. PF2: reputation / nations. D&D SRD: weak. 005: Greyhawk/Waterdeep/Absalom factions as gazetteer objects.

**Analysis.** The organization is a reusable definition/object. This crew’s status is instance state (005 §10). Do not freeze status as gazetteer truth.

### 6.11 Quests / scores / mysteries / scenarios

**Fact.** Blades session = score then downtime. MotW mystery sheet = this mystery’s hook and countdown. CoC *The Haunting*, CPR *Getting Paid*, SW *Blood on the Range* are single scenario instances. 005: adventure cards, 5-room sequences, Alexandrian nodes.

**Inference.** The **procedure** (score cycle, mystery countdown, 5-room beats) is Layer B, not a Component-candidate object. A published scenario is play-context that `uses_asset` people and places. Default: **instantiated**, not a catalog of reusable “Quest types” unless a book actually prints those types.

### 6.12 Events

**Observation.** 004 festival `story.scene`; Fate event-based compels; Lazy DM disposable scenes (005). Events are almost always this-session.

**Inference.** Probably not a Component. An event type catalog is **Unknown** in this free corpus.

### 6.13 Conditions / effects

**Fact.** D&D Rules Glossary and PF2 Conditions are named catalogs. Fate consequences are aspect-shaped and sit on the person. Blades harm / trauma; MotW harm + unstable; SW Shaken / wounds.

**Analysis.** Condition **type** (Frightened, Shaken) is a Component-candidate. The applied stack and its duration are instance overlay.

### 6.14 Encounters

**Fact.** PF2 names Encounter mode. OSE NA generates how many of a type appear. D&D Toolbox includes combat-encounter tools. 003 keyed rooms fuse site + encounter.

**Inference.** An encounter is Layer B context (`staged_in` site, `uses_asset` creature type). Do not default “encounters-as-catalog” to Component-candidate. A published encounter-in-a-box is still play-context.

### 6.15 Timelines / clocks

**Fact.** Blades progress clocks (including faction clocks). AW countdown clocks on threats. MotW mystery countdown (Day → Midnight). 002 Layer B; 005 front/clock as context.

**Analysis.** The **clock procedure** is reusable. **This** clock with current ticks is instance state (`advances` a faction, deity, or issue — 005).

### 6.16 Rules

**Analysis.** Rules are Layer B/C procedures (how to roll, how a score runs). They are not in-world reusable objects. **Probably not a Component.** Recording “the grappling procedure” as if it were a Person or Site would repeat 002’s warning not to mash engine into catalog.

### 6.17 Resources / meters

**Observation.** Mutable numbers on instances are the strongest shared overlay: D&D/PF2/OSE/Cairn HP (Cairn: Hit Protection); CoC SAN, Luck, magic points; Blades stress, heat, coin, rep; Fate stress boxes and fate points; MotW Luck and Harm; CPR HP, Humanity, Luck; SW Bennies and wounds.

**Inference.** The **meter type** (there is HP; there is SAN) is a tiny definition. The **value** is instance. Do not Component-ize “47 HP” as an object.

### 6.18 Tags / traits

**Fact.** PF2 creature/NPC **traits**; MotW gear tags; D&D creature types; Blades item italics / load boxes.

**Inference.** Tags classify definitions. Treat as labels, not entities. **Probably not a Component.**

### 6.19 Relationships

**Fact (004).** Nine heading-backed edges; no minted `knows` / `allied_with` / backstory web. Fortune Hunters: zero edges legal.

**Fact.** Blades: mark one friend and one rival on a playbook list. Fate: aspects can *be* relationships (*I Owe Old Finn Everything*). MotW: History picks with each other hunter.

**Analysis.** Relationships are **edges** (004/005), sometimes **aspects** (Fate), not first-class Components. Status values are context overlays.

### 6.20 Extras (clocks, stress/trauma, heat, aspects/boosts, fronts/threats, claims, humanity, SAN, bennies/FP/luck)

**Clocks / fronts / threats.** Kind = definition; filled front/threat + ticks = instance. Do not merge front with faction (005 §12).

**Stress / trauma.** Stress is a refillable meter. Trauma is a **permanent mutation** on the character instance (Blades). Cairn **scars** are a related mutation pattern.

**Heat.** Crew-level instance state after scores (Blades). 005: campaign state, not an independent object.

**Aspects / boosts.** Aspects can be character-, situation-, or game-scoped definitions-in-play. Boosts are ephemeral extras — **not** Component-candidates.

**Claims.** Type vs holding (005 §5.9). Slot types are Component-candidates; held ticks/ownership are instance.

**Humanity / SAN.** Horror/cyber meters on the person instance (CPR free packets; CoC QS). The existence of the meter is a system definition; the number is overlay.

**Bennies / fate points / Luck.** Session or sheet pools that alter rolls (SW; Fate; CoC Luck; CPR Luck; MotW Luck). Instantiated, usually ephemeral across sessions (explicitly for SW Bennies in the 2015 Test Drive).

---

## 7. Divergence Patterns

**Observation.** The nine texts disagree in recurring ways. These are patterns, not a schema.

1. **Runtime meters.** Almost every system overlays mutable numbers on a sheet instance (HP / stress / SAN / heat / Luck / Humanity / bennies / FP). The catalog does not store the current value.

2. **Condition stacks.** Catalog-heavy games print a condition **type** list (D&D glossary; PF2 conditions) and then stack instances on bodies. Fate writes the condition as an aspect/consequence phrase instead of a shared type name.

3. **Inventory / load.** D&D/PF2/OSE: listed gear instances pointing at item defs. Cairn: slots **are** HP-adjacent constraint; spellbooks occupy slots. Blades: load band chosen per score; items declared in play. Fate: usually aspects/extras, not a 40-page list.

4. **Progression.** D&D/PF2/OSE: level on the class instance. Blades: playbook advances + crew Tier. Fate: skill pyramid / milestones. Cairn: scars, gear, in-world change. CoC QS: skill ticks in the full game (**Unknown** depth here); SAN can fall. Progression is overlay on the instance, not a new definition.

5. **Unique individuals.** PbtA playbooks and MotW History make uniqueness a table rule. D&D/PF2 make uniqueness optional (named NPCs vs 12 bandits). 005 unique monster vs type still holds.

6. **Temporal politics.** Clocks, heat, wanted levels, MotW countdowns, AW threats, Fate issues that resolve — time lives on **context and state**, not on the class definition (005 §11).

7. **Situation overlays.** Scene aspects, position/effect, encounter mode, score vs downtime, exploration vs combat. Layer B wraps Layer D. The situation is not a second copy of the goblin type.

8. **Permanent mutations.** Trauma (Blades), scars (Cairn), consequences that persist (Fate), SAN loss (CoC), Humanity loss (CPR). These change the **instance** without minting a new class definition.

9. **Document nesting vs world reuse.** 003/005: bookmark parent is publishing containment. A spell under a class chapter, an NPC under a room, or a Role Ability under a pregen is not ownership. Association (`uses_asset`, `appears_in`, 004 edges) is what reuse requires.

---

## 8. Contradictions

The corpus disagrees with itself. That is evidence, not a defect to smooth over.

| # | Contradiction | Definition-side | Instance-side | Why it matters |
| --- | --- | --- | --- | --- |
| 1 | **PbtA unique playbook vs D&D many-of-class** | Fighter is a reusable type | The Chosen is *this table’s* Chosen | Cardinality of the PC-option |
| 2 | **Fate aspect vs PF2 feat** | Feat is a named catalog row | Aspect is a unique phrase on an instance | Same “capability/color” job; incompatible grain |
| 3 | **Blades crew vs informal D&D party** | Crew type + sheet + claims | Party is usually not a catalog object in the SRD | Collective as Component-candidate vs not |
| 4 | **OSR HD+NA vs PF2 creature** | Type + how many appear | Rich block is already a fightable instance | How heavy a creature definition is |
| 5 | **Cairn spell-as-item vs Vancian** | Named spell in a list, prepared on the caster | Spell lives in a slot-filling book anyone can hold | Whether a spell is a power def or an item instance |
| 6 | **CoC occupation vs class** | Occupation packages skills / Credit | Class levels combat identity | PC-option is not one ontology |
| 7 | **MotW/AW threat vs monster block** | Threat kind + impulse + countdown | D&D/PF2 combat catalog | Adversary as situation engine vs type-in-bestiary |
| 8 | **Fate boost vs condition** | Condition type persists as a named rule | Boost is one-and-done extra | Ephemeral vs catalogued effect |
| 9 | **OSE demihuman-as-class vs PF2 ancestry × class** | Elf **is** the class | Elf **times** Wizard | Species and class are fused or factored |
| 10 | **CPR Role vs Blades playbook** | Role + Role Ability (class-like, many Rockerboys exist in the setting) | Playbook as table focus (and PbtA uniqueness elsewhere) | Same slang family; different cardinality and fiction |

**Analysis.** Do not pick a winner. A later investigation can record **which side a given system treats as primary**. Forcing one Component shape to absorb all ten rows would hide the disagreement.

---

## 9. Relationship + Context Table

**Analysis.** Keep 004’s in-world edges and 005’s play-context verbs. Instantiation adds **overlay** (meters, ticks, applied conditions) without new ownership.

### 9.1 Verbs (continuity 004–005)

| rel | typical from → to | definition vs instance note |
| --- | --- | --- |
| `appears_in` | Person, faction, item, crew, deity → campaign / adventure / session / scene | Instance is present in that slice; definition is not owned |
| `uses_asset` | Adventure, encounter, score, mystery, 5-room → any independent / definition | Context **casts** a def or a reusable instance |
| `inhabitant_of` / `contains` | Person → site; site → person/item | Geographic or nest-to-edge; not adventure-owns |
| `member_of` | Person → faction / crew / church | Lasting if the org is reusable |
| `wields` | Person → item | Instance holding; item type remains reusable |
| `quest_giver_for` / `leads_to` | Person → adventure/score; clue → node | Often play-scoped (005 §10) |
| `enemy_of` / `status` | Person/faction → person/faction | Edge vs numeric overlay (Blades −3..+3) |
| `controls_claim` | Crew / faction → claim slot | Holding is state; slot type is def |
| `has_issue` | Campaign / location / org → Fate issue | Campaign-facing object, not a scene |

**Rejected (still).** Campaign `owns` Person. Adventure `owns` Creature type. Class `owns` this Fighter’s current HP.

### 9.2 Contexts where overlays live

| Context | What is instantiated here | What stays a definition |
| --- | --- | --- |
| **World** | This table’s map-scale facts; AW landscape threat | Gazetteer objects; deity/lore catalogs |
| **Campaign** | Issues, crew sheet, heat, wanted, SAN trend, campaign front | Classes, ancestries, creature types |
| **Adventure** / scenario | *The Haunting*, *Getting Paid*, Greyhawk card, MotW mystery | Sites and people the scenario `uses_asset` |
| **Encounter** / scene / score | Rosters, scene aspects, load, position | Creature types, item types |
| **Character sheet** | Meters, picks, trauma/scars, friend marks | Playbook/class/Role/occupation text |

**Preferred pair (unchanged from 005, now also for defs).**

- Character-instance `appears_in` Campaign  
- Adventure `uses_asset` Character-instance  
- Character-instance `uses_asset` Class / Playbook / Role / Occupation / Creature-type / Spell-def  

---

## 10. Component Investigation

**Do not implement.** This section only marks what a later pass should **investigate** as possible Components versus what should stay context, overlay, or non-object.

### 10.1 Component-candidates (publisher catalogs / reusable sheets)

Investigate these as reusable definitions:

- Creature **types** (D&D/PF2/OSE catalogs; Cairn recipe-kinds)
- Species / ancestry (and the OSE fused demihuman-class as a *different* shape of the same ask)
- Class / playbook / Role / occupation (PC-option family; cardinality differs)
- Ability definitions (feats, stunts, moves, Role Abilities, Edges)
- Spell / power definitions (Vancian lists; SW powers; CoC spells when catalogued)
- Item definitions (including Cairn spellbook-as-item as a boundary case)
- Condition **types**
- Reusable locations and factions (005 independents)
- Claim **slot types** (Blades)
- Threat **kinds** (AW / MotW)
- Deities / lore catalogs (004/005)

### 10.2 Instances / context (reference + overlay)

These are how play sits on the candidates:

- PC / NPC **instances** (filled sheets, pregens, named people)
- Campaign / adventure / session / scene
- Clocks **with ticks**; MotW countdown position
- Applied conditions; consequence phrases in play
- Meter **values** (HP, stress, SAN, heat, Luck, Humanity, bennies, FP)
- Status **values** (Blades faction status; wanted level)
- Relationship **edges** (004 nine; friend/rival marks)

### 10.3 Not Components

- Rules procedures (how to roll, how a score runs, how to compel)
- Pure tags-as-objects (traits used as if they were People)
- Ephemeral boosts (Fate)
- Default encounters-as-catalog (the fight ends; the type remains)
- Informal parties (D&D SRD party is not a crew sheet)
- Backstory blobs (still absent as headings in 003/004; CoC QS has a backstory cluster on the sheet — treat as instance color, not a catalog)
- Adventure **owns** beings (rejected in 005; still rejected)

### 10.4 Open design risks (investigate, do not implement)

Seven questions a later Owner pass would have to answer before any Component work. They are risks because the corpus contradicts itself.

1. **Crew / party.** Is Blades crew a Component-candidate while a D&D party is not? One type or two? (005 open question, still open.)
2. **Spell-as-item.** If Cairn’s spell is an item instance, does a Vancian *fireball* become an item when written on a scroll and a power when prepared? Boundary is **moderate** confidence.
3. **Threat kind vs creature type.** Can one candidate hold both a goblin HD line and an AW warlord impulse without flattening one of them?
4. **Playbook uniqueness.** If class is a many-instance definition, what constraint records “only one Spell-Slinger at this table”?
5. **Occupation vs class vs Role.** Three PC-option shapes. One candidate with flags, or three candidates?
6. **Meter types.** Is “has SAN” a tiny Component, or only a field on the character instance?
7. **Keyed-room occupant.** 005 Unknown remains: when is a being only that room’s instance (no extra edges) versus a reusable Person?

---

## 11. Open Questions

- **Unknown.** Full unpaid Cyberpunk RED core: how Role, Humanity, Lifepath, and Night City catalogs are factored versus Easy Mode’s five named people.
- **Unknown.** Full unpaid SWADE: Edge / Hindrance / Power / creature catalog depth versus Test Drive archetypes and Power Cards.
- **Unknown.** Full MotW / AW books: how often threat kinds are reused as a *catalog* versus written fresh per mystery.
- **Unknown.** Whether tables treat OSE NA as “the definition includes how many you meet” or as a generator that produces instances (document is both).
- **Unknown.** CoC full investigator-creation: how many occupations are printed as a reusable list versus Quick-Start pregens.
- **Unknown (005, still).** Crew vs party as one object type; occupancy-only dungeon names; official 5e Sources bookmark trees.
- **Out of scope.** Software, storage, UI, Mahogany, or any named internal design.

**Narrow follow-ups (only if Owner wants one)**

1. One **worked sheet pair**: a D&D SRD Fighter definition beside a MotW playbook instance, tagged definition vs overlay only.
2. Stress-test spell-as-item: Cairn spellbook vs D&D SRD spell + scroll, bibliographic structure only.
3. If Owner opens paid SWADE or CPR core later: rerun §4.4–4.5 with the unpaid-window gap closed.

**Analyst confidence:** **High** on the split; **moderate** on crew / spell-as-item / threat-kind boundaries; **low** on unpaid full-book depth for SW and CPR.

---

## 12. Sources

Access date **2026-09-10**. No copyrighted adventure prose is quoted.

### Continuity (prior assignments)

1. `research/assignments/fromResearcher1/002-ttrpg-core-components.md` — Layers A–E; catalog vs procedure; corpus maps  
2. `research/assignments/fromResearcher1/003-ttrpg-structural-parts-schema.md` — heading nest; catalogs vs story tree  
3. `research/assignments/fromResearcher1/004-gygax-structural-parts-and-character-relations.md` — nine edges; Fortune Hunters zero edges  
4. `research/assignments/fromResearcher1/005-ttrpg-reusable-domain-objects-and-relationships.md` — independent vs play-context; `appears_in` / `uses_asset`  

### D&D SRD 5.2.1

5. https://www.dndbeyond.com/srd  
6. https://media.dndbeyond.com/compendium-images/srd/5.2/SRD_CC_v5.2.1.pdf  

### Pathfinder 2e (Archives of Nethys)

7. https://2e.aonprd.com/Rules.aspx  
8. https://2e.aonprd.com/Rules.aspx?ID=1401  
9. https://2e.aonprd.com/Rules.aspx?ID=3369  

### Call of Cthulhu 7e Quick-Start

10. https://www.chaosium.com/content/FreePDFs/CoC/CHA23131%20Call%20of%20Cthulhu%207th%20Edition%20Quick-Start%20Rules.pdf  

### Cyberpunk RED Easy Mode (free)

11. https://rtalsoriangames.com/2022/06/25/free-rpg-day-2022/  
12. https://talsorianstore.com/products/cyberpunk-red-easy-mode  
13. https://www.drivethrurpg.com/en/product/409912/cyberpunk-red-easy-mode  
14. https://rtalsoriangames.com/wp-content/uploads/2021/02/RTG-CPRed-SingleShotPackv1.1.pdf — adjacent free packet (Role / Luck / Humanity sheet language)  

### Savage Worlds Test Drive (free)

15. https://peginc.com/new-to-savage-worlds-start-here/  
16. https://peginc.com/take-savage-worlds-deadlands-out-for-a-free-test-drive/  
17. https://www.drivethrurpg.com/en/product/339651/savage-worlds-adventure-edition-test-drive  
18. https://www.peginc.com/wp-content/uploads/2015/07/Test_Drive_2015.pdf — older posted Test Drive (Bennies / Wild Die)  

### Blades in the Dark (FitD SRD)

19. https://bladesinthedark.com/basics/  
20. https://bladesinthedark.com/character-creation  
21. https://bladesinthedark.com/crew  
22. https://bladesinthedark.com/faction-game  
23. https://bladesinthedark.com/heat  
24. https://bladesinthedark.com/downtime-activities  
25. https://bladesinthedark.com/licensing  

### Fate Core SRD

26. https://fate-srd.com/  
27. https://fate-srd.com/fate-core/basics  
28. https://fate-srd.com/fate-core/aspects-fate-points  
29. https://fate-srd.com/fate-core/settings-big-issues  
30. https://fate-srd.com/fate-core/faces-places  

### Apocalypse World + Monster of the Week (free)

31. http://apocalypse-world.com/AW2ndEdThreatsPreview.pdf  
32. http://apocalypse-world.com/  
33. https://evilhat.com/monster-of-the-week/  
34. https://evilhat.com/wp-content/uploads/2022/01/Monster-of-the-Week-Revised-Mystery-Worksheet.pdf  
35. https://evilhat.com/wp-content/uploads/2023/01/Monster-of-the-Week-Hunter-Playbooks-Consolidated-2025.pdf  

### Cairn SRD + OSE SRD

36. https://cairnrpg.com/first-edition/cairn-srd/  
37. https://oldschoolessentials.necroticgnome.com/srd/index.php/Main_Page  
38. https://oldschoolessentials.necroticgnome.com/rules/  
39. https://oldschoolessentials.necroticgnome.com/srd/index.php/Dwarf  
40. https://oldschoolessentials.necroticgnome.com/srd/index.php/Elf  
41. https://oldschoolessentials.necroticgnome.com/srd/index.php/Halfling  
42. https://oldschoolessentials.necroticgnome.com/srd/index.php/Game_Statistics_(Monsters)  

### Company documents (not scored)

43. `agents/market-research-analyst/instructions.md`

---

## Appendix A — Shortlists

### Top 5 patterns

1. Instantiation is **reference + overlay**, not exclusive ownership (continuity 005 `appears_in` / `uses_asset`).
2. **Template → sheet** with mutable meters (HP / stress / SAN / heat / Luck / Humanity).
3. Systems choose a **primary side**: catalog-heavy (D&D / PF2 / OSE) vs instance-heavy (Fate / PbtA / Blades) vs pre-instantiated quick-starts (CoC QS / CPR Easy Mode / SW Test Drive).
4. Creatures are not one print job: **HD+NA** vs **rich block** vs **short fiction** vs **threat kind**.
5. Permanent mutations (trauma, scars, SAN/Humanity loss) change the **instance**, not the definition.

### Top 5 contradictions

1. PbtA unique playbook vs D&D many-of-class.
2. Fate aspect vs PF2 feat.
3. Cairn spell-as-item vs Vancian named spell.
4. OSE demihuman-as-class vs PF2 ancestry × class.
5. MotW/AW threat vs D&D/PF2 monster block.

### Component-candidate shortlist

Creature types; species/ancestry; class/playbook/Role/occupation; ability defs; spell/power defs; item defs; condition types; reusable locations/factions; claim slot types; threat kinds; deities/lore catalogs.

### Non-Component shortlist

Rules procedures; tags-as-objects; ephemeral boosts; encounters-as-default-catalog; informal parties; backstory blobs; adventure-owns-beings.

**If you only remember one sentence:** Layer D prints the reusable definition; Layer B context **references** it and **overlays** meters, ticks, and applied conditions — the campaign still does not own the Fighter, the goblin type, or the person.
