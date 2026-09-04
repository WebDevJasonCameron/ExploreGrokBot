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

**Hard parts (where solos fail if they chase Obsidian parity):**

1. **Live Preview** quality on CM6 (decorations, embeds, callouts) — months  
2. **Correct link/rename refactor** across thousands of notes — easy to get subtly wrong  
3. **File watcher races** + external edits (Dropbox/iCloud/git) — reliability work  
4. **Plugin security & API stability** — product surface, not a weekend feature  
5. **Mobile + sync** — often larger than the desktop MVP combined  
6. **Performance at 10k–100k notes** — needs real indexing strategy  

**Feasibility verdict:** A **personal scaled-down desktop MVP is feasible for a competent solo in ~1–3 months part-time** (Path C) or **days–weeks** (Path A/B). Matching Obsidian’s ecosystem and polish is **not** a solo weekend project and is usually unnecessary for home use.

---

### 4. Ways it could be better if rewritten today

Framed as engineering/product hypotheses given **how people use Obsidian now** (large local vaults, heavy plugins, Dataview-like queries, multi-device, AI sidekicks, Canvas/Bases-style structured views)—not as a claim that Obsidian should rewrite.

| Area | 2020-era choice | 2026 rewrite hypothesis | Label |
| --- | --- | --- | --- |
| Desktop shell | Electron | **Tauri 2** or native WebView shells for smaller footprint | Inference |
| UI framework | Custom DOM / no React | Still defendable; or **Solid/Svelte** for smaller reactive UI without React weight | Speculation |
| Editor | CM6 (current) | Keep **CodeMirror 6** or evaluate **ProseMirror/TipTap** only if WYSIWYG > source fidelity | Inference |
| Indexing | In-memory metadata cache | Hybrid: **SQLite/FTS5 or Tantivy** for search + incremental link graph; keep files as source of truth | Inference |
| Plugin model | Same-process JS plugins | Process-isolated plugins (WASM or separate process) for security; capability permissions | Inference |
| Query layer | Community Dataview / newer Bases | First-class **local query engine** over frontmatter + links (without leaving Markdown) | Observation of user demand |
| Sync | Proprietary optional Sync | Bring-your-own: **Git**, **Syncthing**, CRDT file sync; optional hosted E2E | Inference |
| AI | Cautious / ecosystem | Local RAG over vault with explicit consent; never cloud-default | Observation (CEO messaging on community > AI hype) |
| Collaboration | Secondary to personal PKM | Realtime collab fights local-first; keep as export/publish, not core | Inference |
| Mobile | Capacitor parity push | Either embrace shared WebView or split “capture client” vs full vault app—founders already learned users reject weak companions **[Verified Fact]** Ness Labs | — |

**Skeptical note:** A rewrite does not automatically win. Obsidian’s moat is less “Electron” and more **trust + files + plugins + community + habit**. A cleaner stack that breaks plugin compatibility or Markdown fidelity would lose power users.

---

### 5. What else should we explore that this assignment didn’t cover?

See also **Recommended Next Research**. High-value gaps:

1. Competitive economics of Sync vs Syncthing/iCloud/git workflows  
2. Plugin security incident history and threat model  
3. Large-vault performance benchmarks (Obsidian vs Logseq DB vs Foam)  
4. Accessibility and non-Markdown-user onboarding (known criticism)  
5. Enterprise/commercial license adoption (mostly opaque)  
6. Relationship and roadmap overlap with Dynalist today  
7. Formal comparison of JSON Canvas vs tldraw-like boards  
8. AI-plugin ecosystem norms vs core product philosophy  

---

## Evidence (sources with links)

### Primary / high-value third-party

1. Wikipedia — *Obsidian (software)*: https://en.wikipedia.org/wiki/Obsidian_(software)  
2. Ness Labs — Erica Xu interview: https://nesslabs.com/obsidian-featured-tool  
3. Dynalist Forum — *About the makers* (Xu/Li Dynalist origin): https://talk.dynalist.io/t/about-the-makers/98  
4. Fast Company — cult/obsession piece; user/community estimates, no VC: https://www.fastcompany.com/90960653/why-people-are-obsessed-with-obsidian-the-indie-darling-of-notetaking-apps  
5. The Verge / Decoder — Steph Ango interview: https://www.theverge.com/decoder-podcast-with-nilay-patel/760522/obsidian-ceo-steph-ango-kepano-productivity-software-notes-app  
6. Steph Ango — Obsidian / related writing hub: https://stephango.com/obsidian  
7. Hacker News — Electron / no-framework discussions: https://news.ycombinator.com/item?id=36616563 ; https://news.ycombinator.com/item?id=45618782 ; CM6: https://news.ycombinator.com/item?id=31669303 ; Canvas/API: https://news.ycombinator.com/item?id=34068512  
8. Medium / Bootcamp — product teardown (stack claims: Electron, Capacitor, CM6, no React): https://medium.com/design-bootcamp/obsidian-app-in-depth-product-teardown-6d685930a367  
9. GitHub — `obsidianmd/obsidian-api` (public plugin API types): https://github.com/obsidianmd/obsidian-api  
10. Community plugin docs (CM6 editor extensions): https://marcusolsson.github.io/obsidian-plugin-docs/editor/extensions  

### Architecture / help mirrors (use cautiously; not primary)

11. Architecture map (secondary synthesis): https://ggprompts.com/architecture/obsidian/index.html  
12. DeepWiki mirrors of help/API (derivative of public docs): e.g. https://deepwiki.com/obsidianmd/obsidian-help  

### Alternatives / OSS landscape

13. Open-source Obsidian alternatives roundup: https://storyflow.so/blog/best-open-source-obsidian-alternatives-2026  
14. Logseq vs Obsidian (DB split context): https://instantowl.com/blog/obsidian-vs-logseq  
15. Example Tauri+CM6 editor patterns: https://github.com/kelvink96/markora ; Inkdown docs patterns: https://mintlify.wiki/inkdown/inkdown/introduction  

### Weak / secondary (revenue claims — do not treat as verified)

16. Newsletter/aggregator pieces citing ~$25M ARR / valuations — e.g. https://readthesignal.co/p/obsidian-25m-arr-8-people-1-cat-no — **Speculation until primary confirmation**

### Official site limitation note

Pricing, manifesto wording, exact Sync cryptography whitepapers, and some credits lists are most complete on **obsidian.md**. Per assignment constraints, those were **not** used as primary sources here; Wikipedia/press/API GitHub were preferred. If a filing needs exact current prices or manifesto text, fetch official pages in a follow-up and label the source limitation explicitly.

---

## Existing Solutions / Competitors / Alternatives

| Product | Model | Solo-build relevance |
| --- | --- | --- |
| **Obsidian** | Proprietary; free core; paid Sync/Publish | Reference UX; closed core |
| **Logseq** | OSS AGPL; outline-first; file + DB tracks | Best “study the code” peer |
| **Foam** | VS Code + Markdown conventions | Minimal path to linked notes |
| **Dendron** | VS Code hierarchical notes | Conceptually useful; project cold |
| **Org-roam** | Emacs | Max power / max niche |
| **Joplin** | OSS; notebook + MD/ENEX heritage | Sync story stronger; different UX |
| **SiYuan / TriliumNext** | OSS local PKMs | More DB/block structured |
| **Notion / Roam / Reflect** | Cloud-first | Opposite of local-first tradeoff |
| **Plain MD + git + ripgrep** | DIY | Often enough for home |
| **Tauri MD editors** | Emerging OSS | Blueprint for rewrite stacks |

**Pattern:** The category split is **plain-files + indexer app** vs **database/block graph**. Obsidian’s bet is firmly the former; Logseq’s recent DB line shows the tension when sync/performance/collaboration pressures rise.

---

## Opportunity Assessment (solo scaled-down feasibility)

**Not a startup pitch.** Assessment for Owner Jason’s “home product” question:

| Criterion | Assessment |
| --- | --- |
| Problem novelty | **Low** — “local Markdown wiki” is well-served |
| Technical feasibility (MVP) | **High** for desktop personal tool |
| Time to useful personal vault app | **Weeks–few months** part-time |
| Time to Obsidian-like ecosystem | **Years / team** — poor solo ROI |
| Differentiator for a home build | Personal workflow fit, privacy, learning, extreme minimalism, or niche (e.g. research lab notes) |
| When *not* to build | If goal is daily notes productivity—**use Obsidian or Logseq** |
| When building still makes sense | Learning exercise; need features Obsidian won’t do; air-gapped constraints; embedding into another system |

**Bottom line:** Solo scaled-down **personal/home** product = **feasible and concrete**. Solo scaled-down **market challenger** = **evidence does not support** as a default recommendation; the incumbents’ moat is community + plugins + trust, not secret algorithms.

---

## Risks and Counter-Evidence

1. **Closed source** → all stack tables beyond Electron/JS/CM6/API are partly inferred; teardowns can be wrong.  
2. **User counts / ARR** → company avoids analytics; press estimates and newsletter ARR claims conflict or lack methodology.  
3. **“No React” performance narrative** → plausible and repeated, but could be overstated relative to careful Electron engineering generally.  
4. **Capacitor/mobile details** → strongly attested in secondary tech writeups; not re-verified from official credits in this pass.  
5. **Building your own** risks abandoning it; opportunity cost vs configuring Obsidian is high.  
6. **Logseq DB split** shows pure Markdown sync/scale pain is real—counter-argument to “files forever, never index in SQLite.”  
7. **Plugin ecosystem as moat** cuts both ways: security surface and beginner overwhelm (documented criticisms in Wikipedia reception).

---

## Unknowns

- Exact Sync protocol, conflict resolution, and encryption audit status  
- Current FTE headcount and revenue mix (Sync vs Publish vs Catalyst vs commercial)  
- How much of Dynalist engineering carried into Obsidian  
- Internal test strategy for vault corruption / watcher edge cases  
- Whether a future first-party query/DB layer will dilute “just Markdown files”  
- Long-term plugin API stability guarantees  
- Real distribution of vault sizes and plugin counts among active users  

---

## Recommended Next Research

1. **Read Ango essays** “File over app” and “100% user-supported” end-to-end; extract principles vs marketing.  
2. **Comparative bench:** 1k / 10k / 50k note vaults — Obsidian vs Logseq (file) vs Logseq (DB) vs Foam cold start & search latency.  
3. **Security brief:** community plugin supply chain (review of past malicious plugins if any).  
4. **Sync alternatives playbook:** iCloud vs Syncthing vs git-annex vs paid Sync — failure modes.  
5. **Solo MVP spike (optional):** 2-week Tauri+CM6+wikilink index prototype to validate personal fit before larger investment.  
6. **Dynalist continuity:** Is Dynalist still actively developed; any shared infra?  
7. **Bases / Dataview trajectory:** Are users moving from community query plugins to core structured views?  
8. If needed for filing accuracy: **one limited official-site pass** for current pricing/manifesto, clearly labeled.

---

## Analyst Confidence

**Overall: Moderate–High**

| Topic | Confidence | Why |
| --- | --- | --- |
| Founders, Dynalist lineage, 2020 origin | **High** | Wikipedia + Ness Labs + Dynalist forum |
| Local Markdown vault + plugins + graph | **High** | Ubiquitous corroboration |
| Electron desktop + CM6 editor | **High** | Wikipedia + HN + plugin docs |
| Capacitor mobile + no React UI | **Moderate** | Multiple secondary sources; not source-audited |
| Metadata cache / process model details | **Moderate** | API surface + secondary architecture maps |
| Bootstrapped / small team / Ango CEO | **High** | Press + Verge + Ango site |
| Revenue/ARR specifics | **Low** | Secondary estimates only |
| Solo MVP feasibility | **High** | Many working OSS precedents + clear MVP cut line |
| “Rewrite today” recommendations | **Moderate** | Engineering judgment, not empirical bakeoff |

---

## Appendix A — Claim register (Owner’s “known facts” check)

| Prior claim to verify | Result |
| --- | --- |
| Founders Shida Li & Erica Xu | **Confirmed** |
| Small team | **Confirmed** (started as 2; still small FTE) |
| Electron app | **Confirmed** |
| Local Markdown files | **Confirmed** |
| Plugin ecosystem | **Confirmed** |
| Graph view | **Confirmed** |
| Started ~2020 | **Confirmed** (beta 2020-03-30) |
| Related to Dynalist | **Confirmed** |

---

## Appendix B — Suggested solo MVP checklist

- [ ] Folder picker + recursive `.md` list  
- [ ] CM6 editor tab  
- [ ] Wikilink parse → adjacency list  
- [ ] Backlinks panel for active note  
- [ ] Search (start with ripgrep or SQLite FTS5)  
- [ ] Simple graph for ≤2k nodes  
- [ ] Manual refresh + basic file watch  
- [ ] Git-friendly: no rewrite of unrelated files; UTF-8; preserve user formatting  
- [ ] Explicit non-goals doc (no plugins, no sync, no mobile)

---

*End of assignment. Path: `research/assignments/fromResearcher2/001-obsidian-product-architecture.md`.*
