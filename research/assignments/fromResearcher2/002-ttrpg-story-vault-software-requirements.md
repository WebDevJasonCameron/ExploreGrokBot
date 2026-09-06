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
