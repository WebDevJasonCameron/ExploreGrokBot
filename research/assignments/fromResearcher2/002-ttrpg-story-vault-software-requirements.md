# 002 — TTRPG & Story Vault Software Requirements

**Assignment:** `research/assignments/fromResearcher2/002-ttrpg-story-vault-software-requirements.md`  
**Analyst style:** ExploreGrokBot Market Research Analyst (adapted for requirements brief)  
**Owner / Researcher:** Jason Cameron / Researcher 2  
**Draft date:** 2026-09-05 (America/Chicago)  
**Status:** Complete — awaiting Owner review
**Filed by:** Researcher 2
**Source policy:** Public third-party / OSS docs preferred; not a business pitch

**Label legend used throughout:**  
- **[Verified Fact]** — corroborated by public docs / reputable third-party sources cited below  
- **[Observation]** — pattern visible in OSS products / community practice without formal proof of internals  
- **[Inference]** — reasoned conclusion from public info; suitable for engineering planning but not gospel  
- **[Speculation]** — plausible hypothesis; treat as experiment target

**Reuse from assignment 001 (compressed):** Obsidian-class apps are local Markdown vaults + metadata cache + CodeMirror 6 editor + Electron/Capacitor shell; solo home MVP of vault + wikilinks + backlinks + search is feasible; marketplace/mobile/Live Preview are hard. This brief narrows that class into an **opinionated TTRPG/story world manager**, not a general PKM clone.

---

## Executive Summary

Build a **local-first, opinionated TTRPG & story/world manager**: plain Markdown files on disk, wikilinks/relations, full-text search, and graph-ish or entity-structured navigation—shaped for **lived campaign/story worlds** (Character, Location, Faction, Session, Plot beat), not for “second brain” kitchen-sink PKM.

**Owner purposes (in order):** (1) learn this class of software by implementing it; (2) eventually own a faster/stable file/thought manager for TTRPGs + fiction writing with notes staying on the user’s computer; (3) stay narrow via opinionated conventions so the product does not dissolve into general PKM.

**MVP hard requirement:** open a vault and **read, search, manage, and relate thousands of Markdown files** with correct link maintenance under renames and external edits.

**Recommended learning/build default:** **Rust-primary** — Tauri 2 core (FS, indexer, search, graph) + web UI (Svelte or Solid) + CodeMirror 6; SQLite FTS5 for metadata+search (Tantivy optional upgrade). **[Verified Fact]** Tauri 2 uses a Rust core process + OS WebView; **[Verified Fact]** SQLite FTS5 and Tantivy are production-grade embedded search options. **Alternate path:** Java-primary (JavaFX/Compose Desktop or Spring Boot local server + web UI + Lucene/SQLite + WatchService)—stronger fit if Owner wants to leverage Spring/Java muscle memory, weaker default for snappy native packaging and memory discipline. **[Inference]**

**Analyst confidence:** **High** on capability map, non-goals, and that solo part-time MVP is learnable; **Moderate** on exact effort bands and which search backend wins at 50k notes; **Low** on UI “feel” parity with mature PKM tools without sustained polish work.

---

## Research Question

What software must be specified and learned to build—from scratch—a local-first, opinionated TTRPG/story vault manager inspired by Obsidian-class construction (files, links, search, graph-ish nav), including concrete functional/non-functional requirements, architecture, two stack blueprints (Rust OR Java), a learning curriculum, MVP cut line, and further research/roles—without evaluating whether cloning Obsidian is a good business idea?

---

## Findings

### A. Capability map (Obsidian-like construction → this MVP)

Break the class into subsystems. Tags: **MVP** = required for Owner MVP; **Later** = valuable after MVP; **OOS** = out of scope for an opinionated TTRPG-story tool (do not build).

| Subsystem | What it does | Tag | Notes |
| --- | --- | --- | --- |
| Vault FS layer | Open folder as vault; read/write UTF-8 `.md` (+ attachments); preserve bytes for git | **MVP** | Source of truth = files |
| File tree / browser | Hierarchical navigation, create/rename/move/delete | **MVP** | Folder conventions encode entity types |
| Markdown editor | Open/edit note; save atomically | **MVP** | Source mode first; Live Preview later |
| Wikilinks | Parse `[[Note]]` / `[[Note\|alias]]` / optional `#heading` | **MVP** | Prefer parser over naive regex long-term |
| Backlinks / outgoing links | Show notes that link here; resolve unresolved links | **MVP** | Core of “relating” |
| Rename/refactor | Rename file → rewrite inbound links across vault | **MVP** | Hard problem; must be correct |
| Metadata cache | Paths, titles, frontmatter, tags, headings, link edges | **MVP** | Powers UI without re-scanning all files |
| Full-text search | Query body + title; ranked results | **MVP** | Target thousands → tens of thousands |
| File watcher | Detect external edits; incremental reindex | **MVP** | Correctness > cleverness |
| Tags + YAML frontmatter | Parse, index, filter | **MVP** | Frontmatter carries entity schema |
| Entity conventions | Character/Location/Faction/Session/PlotBeat schemas + folders | **MVP** | Opinionation vs freeform PKM |
| Relationship views | Structured “related entities” panels; basic graph optional | **MVP** (structured first) | Force graph can be Later if structured links ship |
| Graph visualization | Force-directed whole-vault graph | **Later** | Useful; not the only relationship UX |
| Frontmatter query | Filter `type: character AND faction: X` | **Later** (thin MVP filter OK) | Dataview-like is Later |
| Templates / new-entity wizards | Create note from schema template | **Later** (MVP: seed templates on disk) | |
| Continuity checks | Dead links, missing required fields, status contradictions | **Later** | Differentiator for TTRPG |
| Campaign hierarchy UI | Campaign → Adventure → Session navigation | **MVP** (folders + frontmatter) | UI chrome can deepen Later |
| Attachments / images | Store and link binaries | **Later** (MVP: leave files alone) | Don’t mangle |
| Canvas / spatial boards | Freeform boards | **OOS** | |
| Plugin marketplace / API | Third-party extensions | **OOS** | |
| Cloud Sync SaaS | Hosted sync product | **OOS** | Git/Syncthing later, not product |
| Mobile parity | iOS/Android apps | **OOS** | |
| Real-time collab | Notion-like multiplayer | **OOS** | |
| General PKM kitchen sink | Daily notes OS, flashcards, task GTD, etc. | **OOS** | Narrow domain |
| Publish / static site | Public garden | **OOS** for MVP | |
| CRDT sync | Multi-device merge without git | **Later / research** | Curriculum item only |

**Inference:** The learning value sits in **indexer + watcher + link refactor + search + editor integration**. UI chrome without those subsystems teaches the wrong lessons. **[Inference]**

---

### B. Software requirements

#### B.1 Functional requirements (engineers)

**FR-VAULT**
1. User can open an existing directory as a vault and create a new vault with seed folder layout + schema templates.
2. App stores only ephemeral/cache state outside the vault (e.g. `.storyvault/` or app data dir); **never** requires a proprietary note DB as source of truth.
3. Ignore patterns (`.gitignore`-style) exclude `node_modules`, large binaries, and cache dirs from indexing.

**FR-TREE**
4. File tree shows vault folders/files; supports create folder, create `.md`, rename, move, delete with confirm for destructive ops.
5. Opening a note loads content into the editor; dirty state and save (explicit + optional autosave) are visible.

**FR-EDIT**
6. Edit Markdown as plain text (source mode) with syntax highlighting.
7. Saves write UTF-8; use atomic write pattern (temp + rename) to reduce crash truncation. **[Inference — industry practice]**
8. App does not rewrite files the user did not edit (git-friendly: no mass reformatting, no forced EOL changes, preserve unknown frontmatter keys).

**FR-LINKS**
9. Recognize wikilinks: `[[Target]]`, `[[Target|alias]]`, optional `[[Target#heading]]`.
10. Clicking a resolved link opens the target; unresolved links are visually distinct and creatable.
11. Backlinks panel lists notes linking to the current note (path + optional context snippet).
12. Outgoing links panel lists targets from current note.
13. **Rename/refactor:** renaming or moving a note updates inbound wikilinks across the vault in one transaction (or staged preview + apply). Path-based and title-based resolution rules must be documented and tested.

**FR-SEARCH**
14. Full-text search over note titles and bodies for vaults of **≥1,000** notes; design for **10,000** with graceful behavior toward **50,000**.
15. Results show path, title, snippet, and score/rank; open result on activate.
16. Search remains usable while background indexing runs (stale-while-revalidate OK if labeled).

**FR-META**
17. Parse YAML frontmatter; index declared fields used by schemas.
18. Index `#tags` (inline and/or frontmatter `tags:`).
19. Filter/browse by `type` (entity type) and common fields (e.g. `status`, `campaign`).

**FR-REL**
20. MVP relationship view: for an entity, show typed relations from frontmatter (e.g. `location`, `faction`, `appears_in`) **and** wikilink neighbors.
21. Optional MVP graph: nodes = notes (or entities only), edges = wikilinks; filter by type. If schedule slips, structured panels ship before pretty graph.

**FR-DOMAIN**
22. Seed conventions (folders + frontmatter schemas) for at least: `character`, `location`, `faction`, `session`, `plot_beat`, plus `campaign`/`adventure` containers.
23. New-note flow can pick an entity type and apply the matching template (MVP may be “copy template file”).

**FR-WATCH**
24. External create/modify/delete of `.md` files updates cache/search/links without full restart.
25. Debounce rapid events; recover via hash/mtime check if watcher drops events (esp. network FS / WSL). **[Verified Fact — notify docs warn NFS/WSL limitations]**

#### B.2 Non-functional requirements

| ID | Requirement | Target / note |
| --- | --- | --- |
| NFR-LOCAL | Local-only by default; no account; no telemetry required | Privacy default |
| NFR-OFFLINE | Fully usable offline | Absolute |
| NFR-PRIVACY | Notes never uploaded by the app | Absolute for MVP |
| NFR-UTF8 | UTF-8 round-trip; don’t corrupt non-ASCII names/bodies | Absolute |
| NFR-GIT | Don’t mangle files; cache/index files gitignoreable | Absolute |
| NFR-CRASH | Crash during save must not silently empty a note; index corrupt → rebuildable | Absolute |
| NFR-PERF-1K | Cold open + interactive UI ≤ 2s on modern laptop SSD; search first keystroke results ≤ 100ms after warm index | Stretch-OK if measured |
| NFR-PERF-10K | Warm search ≤ 200ms typical queries; incremental reindex single file ≤ 50ms median | Design goal |
| NFR-PERF-50K | App remains usable: background index, no UI freeze > 100ms on main thread; full reindex may take minutes but is cancellable/progressed | Stress goal |
| NFR-WATCH | External edit reflected in UI ≤ 1s after debounce under local disk | Design goal |
| NFR-MEM | Steady RSS target: prefer < 500MB at 10k average notes (Rust path); document Java path expectations separately | Soft |

Performance numbers are **engineering targets for learning measurement**, not contractual SLAs. **[Inference]**

#### B.3 Explicit non-goals

- Plugin marketplace / third-party plugin API  
- Sync SaaS, accounts, E2EE cloud product  
- Mobile app parity  
- Notion-like realtime collaboration  
- General PKM feature sprawl (daily-note OS, spaced repetition, CLIPBOARD managers, etc.)  
- Re-implementing Obsidian Live Preview polish in MVP  
- Shipping copyrighted TTRPG rulebook text  

---

### C. Architecture (from-scratch)

```
┌─────────────────────────────────────────────────────────────┐
│ UI shell (web or native toolkit)                            │
│  file tree │ editor (CM6) │ search │ backlinks │ entity pane │
└───────────────────────────┬─────────────────────────────────┘
                            │ IPC / local HTTP / bindings
┌───────────────────────────▼─────────────────────────────────┐
│ Application services                                        │
│  vault session │ commands (open/save/rename) │ query API    │
└───────┬─────────────┬───────────────┬───────────────┬───────┘
        │             │               │               │
┌───────▼──────┐ ┌────▼─────┐ ┌───────▼──────┐ ┌──────▼───────┐
│ FS vault I/O │ │ Indexer  │ │ Search engine│ │ Link graph   │
│ atomic write │ │ parse MD │ │ FTS index    │ │ adj lists    │
│ watcher      │ │ frontmatter│ │ snippets    │ │ resolve      │
└───────┬──────┘ └────┬─────┘ └───────┬──────┘ └──────┬───────┘
        │             │               │               │
        └─────────────┴───────┬───────┴───────────────┘
                              │
                    ┌─────────▼─────────┐
                    │ Metadata cache DB │
                    │ (SQLite recommended) │
                    └─────────┬─────────┘
                              │
                    ┌─────────▼─────────┐
                    │ User vault on disk│
                    │ *.md + folders    │
                    └───────────────────┘
```

**Layer responsibilities**

1. **FS vault** — sole source of truth; list/read/write/watch; attachment passthrough.  
2. **Indexer / metadata cache** — parse frontmatter, tags, headings, wikilinks; content hash; upsert into SQLite; expose note docs to UI.  
3. **Search engine** — FTS over title/body (and optionally typed fields); ranking (BM25-class). SQLite FTS5 provides `bm25`/`rank`. **[Verified Fact]**  
4. **Link graph** — directed edges note→target; unresolved set; reverse index for backlinks; refactor planner.  
5. **Editor shell** — CodeMirror 6 (or Java alternative) with wikilink decoration + autocomplete fed by cache.  
6. **UI** — navigation + panels; keep heavy work off UI thread via async commands.  
7. **Optional query** — SQL/DSL over frontmatter columns (`type`, `campaign_id`, …).

**Design rules:** Core never trusts the WebView with raw FS authority beyond mediated commands (Tauri model). **[Verified Fact — Tauri process model]** Cache is disposable: delete DB → full reindex restores behavior.

---

### D. Two concrete stack blueprints

#### D.1 Rust-primary path (recommended default)

**Stack sketch**
- **Shell:** Tauri 2 (Rust core + OS WebView) **[Verified Fact]**  
- **UI:** Svelte or Solid + TypeScript  
- **Editor:** CodeMirror 6 + `@lezer/markdown` / custom wikilink inline parser (study SilverBullet / community CM6 wikilink patterns) **[Observation]**  
- **Parse:** `pulldown-cmark` (has wikilink options in recent versions) or dedicated MD+frontmatter pipeline; `serde_yaml` / `gray_matter`-style split for frontmatter **[Observation — see also sakuin-md-style indexers]**  
- **DB/search:** `rusqlite` + **FTS5** first; optional **Tantivy** if FTS5 ranking/scale proves insufficient **[Verified Fact — Tantivy Lucene-like Rust library]**  
- **Watcher:** `notify` + `notify-debouncer-full` **[Verified Fact]**  
- **IPC:** Tauri commands for request/response; events for index progress **[Verified Fact]**

**Implement in order (learning milestones)**
1. Vault open + recursive `.md` listing + read/write + atomic save  
2. SQLite schema: files, links, tags, FTS table; full scan indexer  
3. Search UI wired to FTS  
4. Wikilink extract + backlinks panel  
5. Watcher → incremental reindex  
6. Rename/refactor transaction  
7. CM6 editor + link autocomplete  
8. Entity schemas + folder seed + relationship panel  
9. Perf pass at 1k/10k fixtures; then basic graph or typed query

**Libraries / docs to study**
- https://v2.tauri.app/concept/process-model/  
- https://v2.tauri.app/develop/calling-rust/  
- https://sqlite.org/fts5.html  
- https://docs.rs/tantivy/latest/tantivy/  
- https://docs.rs/notify/latest/notify/  
- https://codemirror.net/docs/ (CM6)  
- OSS study: Foam, Logseq (file mode), SiYuan/Trilium (DB-centric contrasts), SilverBullet parser patterns

**Hard problems**
- Wikilink resolution rules (unique title vs path vs ambiguous)  
- Rename races with watcher (app-originated writes vs external)  
- Partial/corrupt YAML frontmatter  
- Windows path case / Unicode normalization  
- Keeping UI non-blocking during initial index  

**Effort band (competent solo, part-time ~10–15 h/wk)** — **[Speculation / planning estimate]**
- Vertical slice (open/edit/search 1k): **6–10 weeks**  
- MVP (links, refactor, watcher, schemas, 10k-ready): **4–7 months**  
- Polish + graph + continuity checks: **+2–4 months**

#### D.2 Java-primary path (Owner Java/Spring strengths)

**Stack sketch (pick one UI strategy)**
- **A — Desktop UI:** JavaFX **or** Compose Multiplatform desktop; embed editor (less ideal than CM6) or host WebView for CM6  
- **B — Local server:** Spring Boot on localhost + web UI (Svelte/CM6) in system browser or WebView — familiar to Spring devs; packaging/UX more “dev tool” than “app”  
- **Search:** Apache Lucene (proven) **and/or** SQLite FTS via JDBC  
- **Watcher:** `java.nio.file.WatchService` (know platform quirks)  
- **Parse:** commonmark-java / flexmark + SnakeYAML  

**Precedents:** JavaFX + Lucene desktop search apps exist (e.g. FXDesktopSearch patterns). **[Observation]**

**Implement in order**
1. Vault service + file I/O + WatchService  
2. Lucene or SQLite index + search API  
3. Link extraction + graph model in memory/SQLite  
4. UI shell (JavaFX tree+webview **or** Spring+web)  
5. Refactor rename  
6. Schemas / entity panels  
7. Packaging (jpackage / native image research)

**Tradeoffs vs Rust**
| Dimension | Rust/Tauri | Java path |
| --- | --- | --- |
| Owner familiarity | Steeper if new to Rust | Faster ramp **[Inference]** |
| Memory / snappy feel | Generally stronger default **[Inference]** | Higher baseline RAM; GC pauses possible |
| Packaging | Tauri installers mature | jpackage workable; more moving parts |
| Search ecosystem | FTS5/Tantivy excellent | Lucene is the reference FTS library **[Verified Fact]** |
| Editor quality | CM6 in WebView natural | Need WebView or accept weaker native editor |
| Learning goal fit | Teaches systems/perf deeply | Teaches domain+architecture with familiar tools |

**Effort band (solo part-time)** — **[Speculation]**
- If Spring+web chosen: vertical slice **5–8 weeks**; MVP **4–6 months**  
- If pure JavaFX+Lucene without web editor: similar calendar time, more UI friction risk  

**Recommendation:** Use **Rust-primary** unless Owner explicitly wants Java to maximize weeks-of-coding vs weeks-of-language-learning. A hybrid (“Java indexer prototype → Rust rewrite”) is valid but doubles work—avoid unless intentional. **[Inference]**

---

### E. What you must understand (learning curriculum)

Ordered for build order:

1. **Vault as git-friendly directory** — source of truth, ignore rules, atomic saves  
2. **Frontmatter vs body** — YAML parse failures; schema validation vs permissive read  
3. **Markdown AST vs regex wikilinks** — regex ships fast, lies on edge cases (code blocks, nested brackets); AST/lezer/pulldown long-term  
4. **Link resolution policy** — path, filename stem, unique display title; ambiguity UX  
5. **Metadata cache design** — what is derived vs stored; invalidation by hash/mtime  
6. **Incremental indexing** — per-file upsert; directory deletes; rename detection  
7. **File watchers & races** — debounce, self-write echoes, lost events, polling fallback (NFS/WSL) **[Verified Fact — notify limitations]**  
8. **Graph data structures** — adjacency lists, reverse edges, connected components for “orphan” reports  
9. **FTS ranking** — tokenization, BM25/`rank`, phrases, prefixes (FTS5/Lucene/Tantivy)  
10. **Refactor as search-replace with parse awareness** — don’t rewrite inside fenced code  
11. **Editor embedding** — CM6 extensions, autocomplete sources from index  
12. **IPC & thread safety** — UI thread vs indexer pool (Tauri async commands / Java executors)  
13. **Frontmatter schemas for domains** — typed entities without becoming a database app  
14. **CRDT-less sync later** — why git/Syncthing conflict on plain text; what would be required for true multi-device merge (curriculum only)  
15. **Performance measurement** — fixtures at 1k/10k/50k; flamegraphs; avoid premature Tantivy/Lucene complexity  

---

### F. Opinionated TTRPG/story product requirements (narrowing PKM)

Domain opinionation **changes requirements** relative to general PKM:

| General PKM | This product |
| --- | --- |
| Any folder taxonomy | **Forced seed layout** + allowed entity `type` values |
| Freeform links only | **Typed relations** in frontmatter *plus* wikilinks |
| Daily notes as hub | **Session / chapter** as time hub |
| Tags as primary structure | Tags secondary; **entities & campaign hierarchy** primary |
| Infinite plugin workflows | **Few workflows:** prep → play → recap → continuity update |

**Proposed vault layout (concrete)**

```text
CampaignName/
  _templates/
  campaigns/
  adventures/
  sessions/          # or chapters/ for pure fiction
  characters/        # PCs + NPCs (frontmatter.role)
  locations/
  factions/
  plot/              # plot_beat, arcs, mysteries
  items/             # optional early
  rules-homebrew/    # user content only; no copyrighted books
  assets/            # images maps; ignored by FTS body or lightly indexed
```

**Proposed frontmatter schemas (MVP fields)**

```yaml
# character
type: character
name: Mira the Fence
role: npc            # pc | npc | creature
status: alive        # alive | dead | unknown | retired
location: "[[Dock Ward]]"
faction: "[[Ashen Ring]]"
campaign: "[[Crown of Cinders]]"
tags: [npc, criminal]
updated: 2026-09-05

# location
type: location
name: Dock Ward
region: "[[Westport]]"
campaign: "[[Crown of Cinders]]"

# faction
type: faction
name: Ashen Ring
goals: ...
status: active

# session (TTRPG) / chapter (fiction)
type: session
number: 12
date: 2026-09-01
adventure: "[[Heist at Low Tide]]"
summary: ...
characters: ["[[Mira the Fence]]", "[[PC: Rowan]]"]
locations: ["[[Dock Ward]]"]
plot_beats: ["[[Beat: Ledger stolen]]"]
cliffhanger: ...

# plot_beat
type: plot_beat
status: open         # open | resolved | abandoned
arc: "[[Arc: Crown]]"
```

**Structural-parts thinking (non-copyrighted):** Treat a lived world as interlocking parts—**story/plot**, **people (PCs/NPCs)**, **places**, **factions/orgs**, **items**, **session/chapter logs**, **optional rules/homebrew**—without ingesting proprietary rulebooks. Continuity features (Later) flag: dead character still `status: alive`, session links to missing entities, open plot beats never referenced again. **[Inference — common GM practice; see OSS vault templates / GM blogs]**

**Product rules that keep focus**
- Creating a note **asks for entity type** (default templates).  
- Search facets default to entity types + current campaign.  
- Relationship panel prioritizes typed fields over raw graph spaghetti.  
- “Library/rules reference” is user homebrew only in-scope; SRD/legal text handling is a **legal research follow-up**, not MVP software.

---

### G. MVP cut line + milestone plan

#### MVP definition (ship / dogfood bar)

A desktop app that can:
1. Open a vault with seed TTRPG/story layout  
2. Browse tree; create/open/edit/save Markdown  
3. Parse wikilinks; show backlinks/outgoing  
4. Rename note and rewrite inbound links correctly  
5. Full-text search across **thousands** of notes (tested at ≥1k, designed for 10k)  
6. Index tags + frontmatter `type` and filter by type  
7. Show structured relations for entities  
8. Pick up external file changes via watcher  
9. Remain local-only, UTF-8 safe, git-friendly, rebuildable index  

**Not in MVP:** plugin API, sync product, mobile, Live Preview polish, full Dataview language, pretty global graph (optional if cheap), continuity linter.

#### Milestones (4–6)

| # | Milestone | Exit criteria |
| --- | --- | --- |
| M1 | **Vault + editor slice** | Open vault, tree, CM6/source edit, atomic save, 100-note fixture |
| M2 | **Index + search** | Full scan to SQLite FTS; search UI; 1k-note fixture bench |
| M3 | **Links** | Extract links; backlinks; unresolved; click navigation |
| M4 | **Watcher + refactor** | External edits reindex; rename updates links; race tests |
| M5 | **Opinionated domain** | Schemas, templates, type filter, relationship panel, campaign seed |
| M6 | **Scale & harden** | 10k fixture; crash/rebuild drills; git round-trip test; basic perf notes |

Optional **M5b:** minimal graph view filtered to `type` nodes.

---

### H. Recommended next research / team roles

**Do not create agents now—recommendations only.**

| Follow-on research | Why |
| --- | --- |
| **003 — Wikilink resolution & refactor correctness matrix** | Ambiguity rules are the silent MVP killer |
| **004 — Search backend bakeoff** | FTS5 vs Tantivy vs Lucene on 10k/50k synthetic TTRPG vaults |
| **005 — Watcher reliability matrix** | macOS/Windows/Linux/WSL; editor self-write loops |
| **006 — CM6 wikilink UX patterns** | Autocomplete, dead links, heading deep links |
| **007 — TTRPG domain schema v0** | Field dictionary + continuity rules with Domain specialist |
| **008 — Legal/content boundaries** | What user content is safe; no scraped copyrighted books |

**Future build-team roles (suggested)**
- **Owner / Researcher 2** — requirements, prioritization (this track)  
- **Builder** — implements stack milestones, benches  
- **TTRPG Domain** — schemas, workflows (prep/recap), sample vaults  
- **QA** — fixture generators, rename/watcher fuzz, git cleanliness checks  
- Optional later: **Designer** (information architecture), **Tech writer** (user conventions doc)

---

## Evidence (links)

| Topic | URL | Use |
| --- | --- | --- |
| Tauri 2 process model | https://v2.tauri.app/concept/process-model/ | Core vs WebView architecture **[Verified Fact]** |
| Tauri IPC / commands | https://v2.tauri.app/develop/calling-rust/ | Command/event patterns **[Verified Fact]** |
| SQLite FTS5 | https://sqlite.org/fts5.html | Embedded FTS + bm25/rank **[Verified Fact]** |
| Tantivy | https://docs.rs/tantivy/latest/tantivy/ | Rust Lucene-class search **[Verified Fact]** |
| notify crate | https://docs.rs/notify/latest/notify/ | Cross-platform watching; NFS/WSL caveats **[Verified Fact]** |
| CodeMirror 6 | https://codemirror.net/docs/ | Editor shell **[Verified Fact]** |
| Foam | https://github.com/foambubble/foam | Markdown vault + links in VS Code **[Observation]** |
| Logseq | https://github.com/logseq/logseq | Local MD/outliner; file vs DB evolution **[Observation]** |
| SiYuan / Trilium(Next) | project sites/GitHub | DB-centric local PKM contrast **[Observation]** |
| Joplin | https://github.com/laurent22/joplin | MD + SQLite management contrast **[Observation]** |
| FXDesktopSearch | https://github.com/mirkosertic/FXDesktopSearch | JavaFX + Lucene + WatchService precedent **[Observation]** |
| Apache Lucene | https://lucene.apache.org/ | Java FTS reference **[Verified Fact]** |
| GM vault practice | Gnome Stew Obsidian campaign article; public vault templates (e.g. stoicrogue/dnd-campaign-template) | Folder/entity conventions **[Observation]** — do not copy copyrighted adventure text |

Assignment 001 file (reuse): `/workspace/001-obsidian-product-architecture.md` (Electron, CM6, local vault, metadata cache, solo MVP feasibility).

---

## Existing Solutions / Alternatives (study targets, not buy list)

| Project | Why study | What not to copy blindly |
| --- | --- | --- |
| Foam | Minimal MD+wikilink graph on files | VS Code-bound; shallow product UX |
| Logseq | Backlinks, graph, local files; block model | Outliner ontology ≠ session/entity model; license/architecture shifts |
| SiYuan / Trilium | Block DB performance, relations | Not plain-file-first; harder git story |
| Joplin | Sync/E2EE lessons | Notebook model; not graph-native |
| SilverBullet | CM6 markdown extension patterns | Different product goals |
| Obsidian (behavior only) | UX reference for links/search | Closed core; don’t reverse binaries; not primary source per policy |
| World Anvil / Notion TTRPG guides | Domain IA inspiration | SaaS/collab non-goals; paywalls avoided |

---

## Opportunity Assessment → **Build-learning fit**

This is **not** a market entry recommendation. Fit for Owner goals:

| Goal | Fit | Why |
| --- | --- | --- |
| Learn how this class of app works | **Strong** | Forces indexer, watchers, FTS, link graph, editor integration |
| Eventually reinvent faster/stable local manager for TTRPG+stories | **Moderate–Strong** | Narrow domain reduces feature infinity; perf still hard at 50k |
| Keep notes on own computer | **Strong** | Files-first architecture |
| Avoid boiling ocean of general PKM | **Strong if non-goals held** | Opinionated schemas are the control surface |

**Wrong learning path:** theming a web UI for months without a real indexer. **Right path:** ugly UI + correct cache/search/refactor. **[Inference]**

---

## Risks / Counter-Evidence (engineering)

1. **Rename/refactor correctness** — subtle bugs destroy trust in a notes app. Mitigate with golden-file tests.  
2. **Watcher unreliability** on some FS setups — need hash reconciliation. **[Verified Fact — notify NFS/WSL notes]**  
3. **Scope creep toward Obsidian** — every “small” PKM feature delays domain value. Enforce non-goals.  
4. **Editor polish time sink** — Live Preview / WYSIWYG can consume the project; source-first MVP. (001 finding)  
5. **Rust learning tax** — may slow calendar progress vs Java; still recommended for systems learning.  
6. **50k-note perf** — unproven until measured; FTS5 may suffice far longer than expected **or** need Tantivy/Lucene. **[Speculation]**  
7. **Schema rigidity** — too strict frontmatter frustrates writers; too loose recreates PKM chaos. Version schemas.  
8. **Legal** — never ship copyrighted monster/spell text; user-owned content only.

---

## Unknowns

- Exact wikilink resolution rules Owner prefers (title vs path primacy)  
- Whether fiction-mode (chapters) and TTRPG-mode (sessions) share one schema family or fork  
- Attachment/search policy for maps/PDFs  
- Single-campaign vs multi-campaign vault as default  
- How much graph UX matters vs typed relationship panels for Owner dogfooding  
- Long-term sync: git-only vs future CRDT research  

---

## Recommended Next Research

1. Researcher/Builder spike: **1k MD fixture generator** + FTS5 search prototype (language of chosen stack).  
2. Domain brief: finalize **schema v0** + sample “Crown of Cinders” fake campaign vault.  
3. Wikilink **ambiguity decision record**.  
4. Bakeoff doc: FTS5 vs Tantivy (Rust) or Lucene vs SQLite (Java) on shared fixtures.  
5. QA: rename/watcher property tests design.

---

## Analyst Confidence

| Area | Confidence |
| --- | --- |
| Capability map & non-goals | **High** |
| Functional requirements completeness for MVP | **High** |
| Architecture layering | **High** |
| Rust/Tauri + FTS5/CM6 suitability | **High** (docs-backed) |
| Java path viability | **Moderate–High** |
| Effort bands | **Low–Moderate** (solo variance) |
| TTRPG schema specifics | **Moderate** (needs Domain dogfood) |
| 50k perf winner | **Low** until benches |

**Overall brief confidence:** **Moderate–High** — sufficient to start M1 without waiting on more product research; remaining unknowns are decision records and measurement, not conceptual blockers.

---

## Appendix — Requirement ID quick index

`FR-VAULT` `FR-TREE` `FR-EDIT` `FR-LINKS` `FR-SEARCH` `FR-META` `FR-REL` `FR-DOMAIN` `FR-WATCH`  
`NFR-LOCAL` `NFR-OFFLINE` `NFR-PRIVACY` `NFR-UTF8` `NFR-GIT` `NFR-CRASH` `NFR-PERF-*` `NFR-WATCH` `NFR-MEM`
