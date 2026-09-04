# 001 — Obsidian Product Architecture

**Assignment:** `research/assignments/fromResearcher2/001-obsidian-product-architecture.md`  
**Analyst style:** ExploreGrokBot Market Research Analyst  
**Owner:** Jason Cameron  
**Draft date:** 2026-09-04 (America/Chicago)  
**Status:** Complete — awaiting Owner review
**Filed by:** Researcher 2
**Source policy:** Public third-party preferred; official company site largely avoided

**Label legend used throughout:**  
- **[Verified Fact]** — corroborated by reputable third-party or primary public sources cited below  
- **[Observation]** — pattern visible in public discussions / product behavior without formal proof of internals  
- **[Inference]** — reasoned reverse inference from public info; not confirmed by source code of the closed core  
- **[Speculation]** — plausible but weakly evidenced; treat as hypothesis  

---

## Executive Summary

Obsidian is a **proprietary, local-first personal knowledge base** that stores notes as plain Markdown files in a user-owned folder (“vault”). **[Verified Fact]** It was co-founded by **Shida Li** and **Erica Xu** (University of Waterloo alumni; previously built the outliner **Dynalist**), with a public beta around **30 March 2020** and v1.0.0 on **13 October 2022**. **[Verified Fact]** Desktop builds use **Electron** (JS/HTML/CSS); mobile uses a **Capacitor**-wrapped WebView of largely the same codebase. **[Observation / Inference]** The UI is widely reported as **framework-light** (no React/Angular-style SPA framework), with the editor built on **CodeMirror 6**. Extensibility was a day-one design goal: core features ship as toggleable plugins, and a large community plugin ecosystem sits on a published TypeScript API. The company is commonly described as **Dynalist Inc.**, small and **bootstrapped / user-supported** (no VC), with **Steph Ango** joining as CEO in **February 2023**.

For a **solo programmer** building a **scaled-down home version**, the realistic path is **not** cloning Obsidian’s full product. An MVP of “folder of Markdown + wiki links + backlinks + simple search + optional local graph” is **highly feasible** in months using Tauri/Electron + CodeMirror 6, or even lighter stacks (VS Code/Foam, Logseq fork, static wiki). The hard parts that make Obsidian hard to match are: polished Live Preview, vault-scale metadata cache performance, a trusted plugin sandbox/API, cross-platform mobile parity, and a self-sustaining community marketplace—not the basic Markdown vault idea.

**Analyst confidence:** **Moderate–High** on founding story, local-first model, Electron/Capacitor/CodeMirror stack, and solo MVP feasibility; **Moderate** on fine-grained internal architecture (closed source); **Low** on viral revenue/ARR figures circulating in secondary blogs.

---

## Research Question

How was Obsidian likely made (architecture/stack/design choices), who made it, how might a solo developer create a scaled-down personal/home version, how might a ground-up rewrite look given today’s usage patterns, and what should further research cover—while assessing solo feasibility without pitching a business unless evidence supports it?

**Source policy followed:** Prefer Wikipedia, tech press, Indie/community interviews, HN/Reddit, GitHub of open alternatives, blogs. Prefer **not** to use obsidian.md as primary; where a fact appears mainly there, it is flagged. No binary reverse-engineering, license cracking, or private/admin access.

---

## Findings

### 1. How was Obsidian likely made? (Architecture, stack, design choices)

#### 1.1 Product architecture (high-level reverse inference)

| Layer | Likely design | Label | Basis |
| --- | --- | --- | --- |
| Data model | Vault = ordinary filesystem folder of `.md` (+ attachments); config in `.obsidian/` | Verified Fact / Observation | Wikipedia; product teardowns; help-doc mirrors |
| Local-first | App is a thick client; cloud Sync/Publish optional, not required | Verified Fact | Wikipedia; Fast Company; Ness Labs |
| Indexing | In-memory **Metadata Cache** for links, tags, headings, frontmatter; powers graph, backlinks, search | Observation / Inference | DeepWiki of public help/API docs; architecture maps |
| Editor | **CodeMirror 6** with Live Preview decorations; earlier CM5 “legacy editor” on desktop | Verified Fact / Observation | HN comments from plugin authors; community plugin docs |
| Desktop shell | **Electron** (Chromium + Node) | Verified Fact | Wikipedia languages; widespread HN/press |
| Mobile shell | **Capacitor** (Ionic) wrapping shared web UI | Observation | Multiple independent teardowns / architecture guides citing credits |
| Plugins | Core plugins + community plugins via TypeScript API (`App`, `Vault`, `Workspace`, `MetadataCache`) | Verified Fact | Public `obsidianmd/obsidian-api` types/docs |
| Graph / Canvas | Force-directed graph of note links; Canvas as spatial board (JSON canvas format later open-documented by CEO-related writing) | Verified Fact / Observation | Wikipedia; Steph Ango project list (JSON Canvas) |
| Sync / Publish | Paid optional services; Sync described as E2E encrypted | Observation | Press/teardowns; exact protocol details not independently audited here |

**Design thesis (founder-stated):** Obsidian as an **“IDE for thought”**—like a code IDE opening a local folder of plain text, with extensibility inspired by VS Code, motivated by dissatisfaction with MediaWiki/TiddlyWiki and other note apps. **[Verified Fact]** — Erica Xu interview (Ness Labs).

**Inferred architectural choices that matter:**

1. **Files over database for the default path** — maximizes portability and trust; pushes complexity into indexing, watchers, and conflict handling when syncing. **[Inference]**
2. **Plugin-first modularity** — most “native” features as core plugins so the same extension surface can be dogfooded. **[Verified Fact]** — Ness Labs.
3. **Web stack everywhere** — one JS/TS UI codebase across desktop Electron and mobile Capacitor reduces team size at cost of native feel and some resource use. **[Inference]** supported by teardowns.
4. **Avoid heavy UI frameworks** — repeatedly claimed on HN and in product teardowns: custom DOM-oriented UI without React/Vue/Angular, which may explain better-than-typical Electron performance. **[Observation]** — not proven from source; consistent across independent commenters.
5. **No product analytics by philosophy** — CEO states they do not track users, so public “user count” figures are estimates. **[Verified Fact]** — The Verge / Decoder interview with Steph Ango.

#### 1.2 Likely technology stack (summary)

**[Observation / Inference — assembled from third-party sources]**

- **Languages:** JavaScript / TypeScript, HTML, CSS (Wikipedia: Written in JavaScript, HTML, CSS)
- **Desktop runtime:** Electron
- **Mobile runtime:** Capacitor (WebView)
- **Editor:** CodeMirror 6 (+ Lezer parsing ecosystem)
- **Markdown / rendering helpers (commonly cited):** markdown-it / remark-family tooling, Prism (code), Mermaid, KaTeX/MathJax — treat library list as **Observation** from teardowns, not audited dependency manifests
- **FS / watchers:** Node `fs` on desktop; platform file APIs on mobile; watcher libraries often inferred (e.g. chokidar-class behavior) **[Inference]**
- **Plugin distribution:** Community plugins as JS bundles; API types published on GitHub (`obsidianmd/obsidian-api`); core app remains closed/proprietary

#### 1.3 What we are *not* claiming

- Exact internal module boundaries, Electron process security model details, Sync wire protocol, or search index implementation are **not** reverse-engineered here. Architecture maps on the open web are useful but secondary; treat fine detail as **Inference** unless corroborated by official public API docs or founder statements.

---

### 2. Who made it? (Team vs individual, company, founding story)

| Claim | Label | Source basis |
| --- | --- | --- |
| Co-founders: **Shida Li**, **Erica Xu** | Verified Fact | Wikipedia; Ness Labs interview |
| Met / collaborated since University of Waterloo; ~10 years of joint projects before Obsidian | Verified Fact | Wikipedia; Ness Labs |
| Prior product: **Dynalist** (outliner; started ~2015 as “Omniflow”) | Verified Fact | Dynalist forum “About the makers”; Ness Labs |
| Obsidian conceived as itch for personal knowledge base; quarantine 2020 catalyzed build | Verified Fact | Ness Labs; Wikipedia |
| First beta **2020-03-30**; v1.0.0 **2022-10-13** | Verified Fact | Wikipedia |
| Legal/developer entity often cited: **Dynalist Inc.** | Verified Fact | Wikipedia; ToS archives naming Dynalist Inc. |
| Originally tiny team (founders + cats); community absorbs support load | Verified Fact | Ness Labs |
| **Steph Ango** (kepano) joined as **CEO Feb 2023**; community contributor / Minimal theme; ex-Lumi | Verified Fact | Wikipedia; The Verge; Ango personal site |
| Bootstrapped / no VC / “user-supported” | Verified Fact (widely reported) | Fast Company; Medium teardown; Ango writing titles; Verge interview framing |
| Team size ~7 FTE (Ango, Verge era); intent to stay ~10–12 | Observation | Verge transcript summary; secondary recaps of Ango posts — exact headcount changes over time |
| ~1M users (2023 estimate from download heuristics) | Observation | Fast Company (“Obsidian estimates… one million users”) |
| Exact ARR / valuation figures ($25M ARR, $350M valuation, etc.) | Speculation / Weak evidence | Secondary newsletters/aggregators; **not** treated as verified here |
| HQ / presence Toronto area | Observation | LinkedIn-style summaries; not independently verified in this draft |

**Founding narrative (compressed):** Two long-time collaborators who already ran Dynalist used COVID quarantine to build the note app Erica had wanted for years—local plain text, links as first-class, IDE-like extensibility. They launched into a pandemic-era PKM boom, grew Discord/forum communities early, kept the core free, and monetized Sync/Publish/Catalyst/commercial licenses. Ango later formalized “file over app” / independence messaging as CEO of a still-small team.

---

### 3. Alternative ways a solo programmer might create a scaled-down home version

**Goal for “home version”:** Personal vault of Markdown with wiki-links, backlinks, search, and maybe a simple graph—**not** a competitor to Obsidian’s plugin marketplace or mobile parity.

#### 3.1 Path A — Don’t build an app (fastest)

| Approach | What you get | Effort | Notes |
| --- | --- | --- | --- |
| Plain Markdown folder + VS Code / Neovim | Editing, git, search | Days | Add Foam or markdown-wiki extensions for links |
| **Foam** (VS Code) | Wikilinks, graph-ish navigation on Markdown folder | Days–weeks | MIT; “shallow graph” vs Obsidian **[Observation]** |
| **Org-roam** (Emacs) | Mature personal wiki graph on Org files | Weeks if new to Emacs | Strong for Emacs users |
| Static site generators (Quartz, Digitals garden tools) | Publishable linked Markdown | Weeks | Different UX (publish-first) |
| Use Obsidian / Logseq as-is | Full product | Zero build | Often the rational choice for personal use |

#### 3.2 Path B — Fork or lean on open products

| Project | License / status | Fit for solo home use |
| --- | --- | --- |
| **Logseq** | AGPL; file-based + evolving DB/SQLite line | Closest OSS PKM; outliner-first; architecture in flux **[Observation]** |
| **SiYuan**, **TriliumNext**, **Joplin** | AGPL/MIT variants | Strong local PKMs; different data models (not always plain MD folder) |
| **Dendron** | Effectively maintenance-mode | Hierarchy insight useful; poor bet as living base **[Observation]** |
| Open Tauri MD editors (e.g. Inkdown-like, Markora, LMD patterns) | Varies | Good **reference architectures** for solo stacks |

#### 3.3 Path C — Build an MVP yourself (concrete stacks)

**Recommended MVP scope (solo, personal):**

1. Open a folder of `.md` files  
2. Edit with CodeMirror 6 (source + basic preview)  
3. Parse `[[wikilinks]]` and Markdown links → backlink index  
4. Full-text search (ripgrep subprocess, Tantivy/SQLite FTS, or simple in-memory)  
5. Local graph (force-directed; Canvas2D or a small viz lib)  
6. Optional: YAML frontmatter tags; daily notes convention  
7. **Out of MVP:** plugin marketplace, Live Preview parity, mobile, E2E sync, Canvas whiteboard, Bases/Dataview-class queries  

**Stack options:**

| Stack | Pros | Cons | Solo fit |
| --- | --- | --- | --- |
| **Tauri 2 + Rust + React/Svelte + CodeMirror 6** | Small binary, native FS, modern default for 2026 desktop | Rust learning curve; mobile later | **Best default for new desktop-only home app** |
| **Electron + TypeScript + CodeMirror 6** | Closest to Obsidian’s shape; huge JS ecosystem | Heavier RAM; packaging pain | Fine if already fluent in Electron |
| **Native Swift/Kotlin + shared MD core** | Best OS integration | Two+ codebases; slower for one person | Only if one OS matters |
| **Browser-only (OPFS / File System Access API)** | Zero install | Fragile permissions; weak mobile | Prototype only |
| **CLI + TUI (e.g. NeonVim + custom indexer)** | Extremely lean | Limited non-dev UX | Excellent for personal use |

