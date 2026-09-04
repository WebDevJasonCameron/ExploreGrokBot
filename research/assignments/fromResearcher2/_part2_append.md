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
