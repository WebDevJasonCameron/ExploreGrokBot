# 004 — Mahogany Architecture Risk Assessment

**Researcher:** Researcher 2  
**Owner:** Jason Cameron  
**Product:** Mahogany — local-first desktop TTRPG / story management app  
**Repo (grounding only; no PRs/pushes performed):** https://github.com/WebDevJasonCameron/mahogany  
**Date:** 2026-09-10 (America/New_York)  
**Status:** Complete — awaiting Owner review  
**Filed by:** Researcher 2  
**Filing path:** `research/assignments/fromResearcher2/004-mahogany-architecture-risk-assessment.md`  
**Note:** No PRs to `mahogany` repo.  
**Assignment goal:** Technical architecture risk assessment — failure modes as the app grows. Identify concrete risks, severity, when each becomes relevant, and practical mitigations. Do **not** redesign Mahogany merely because another stack is fashionable.

**Evidence labels used throughout:**  
- **Verified Fact** — confirmed in official docs, primary public sources, or inspected public repo files.  
- **Observation** — pattern visible across multiple independent sources / public product behavior without claiming universality.  
- **Inference** — reasoned conclusion from facts; may be wrong.  
- **Speculation** — hypothesis needing Owner validation.

**Tone:** Market Research Analyst / technical advisor — evidence-first. Electron is acceptable if risks are managed. Tauri appears only as a comparison tradeoff, not a redesign mandate.

---

## 1. Executive summary

Mahogany’s proposed architecture — **Markdown + YAML frontmatter as authoritative user data**, **SQLite as a disposable derived index**, **Electron main owning FS/DB**, **React renderer via narrow IPC** — is a proven local-first pattern used (with variations) by Obsidian, Logseq, Joplin, Foam, and VS Code’s folder-as-workspace model. **[Observation]** The hard problems are not “which UI framework,” but **filesystem truthfulness**: watchers, atomic/durable writes, concurrent/external edits, stable identity across renames, schema evolution, and keeping a cache honest without ever treating it as source of truth.

**Current scaffold (2026-09 public `main`):** Electron Forge + Vite, Electron **44.3.0**, React **19**, TypeScript, Vitest, `yaml` dependency; `src/main.ts` creates a `BrowserWindow` with preload path and opens DevTools; `src/preload.ts` is effectively empty; early domain models + Markdown serializer for `ComponentDefinition` exist under `src/domain/components/` and `src/infrastructure/markdown/`. README is `# mahogany`. **[Verified Fact]** — public GitHub tree / `package.json` / source files. This is an **early prototype**: many production risks are *latent* (not yet coded), so severity should be read as “when this surface ships,” not “broken today.”

**Bottom line for Owner:** Stay on Electron if desired. The architecture is sound **if** Mahogany treats Markdown files as the contract, builds a ruthless write/watch/reconcile loop in main, uses UUID (or equivalent) stable IDs in frontmatter for references, versions schemas from day one, and never lets the renderer touch FS/SQLite. Highest early risks: **Electron security defaults not yet locked in BrowserWindow**, **no atomic write path yet**, **identity/path coupling when references appear**, and **YAML/Markdown round-trip fidelity** once humans edit files outside the app.

**Analyst confidence:** **High** on Electron security baseline, atomic-write/watcher failure modes, and peer-app conflict patterns (public literature). **Moderate** on exact Mahogany schema/reference model (partially implemented; Owner intent stated). **Low** on production packaging/updater specifics (not yet configured beyond Forge makers/fuses).

---

## 2. Architecture assumptions

Assumptions below are the assessment baseline. Where they diverge from Owner intent, risks shift.

| # | Assumption | Label | Source |
| --- | --- | --- | --- |
| A1 | User library = ordinary folder of Markdown (and attachments); human-readable and editable outside Mahogany | Observation / Owner intent | Assignment brief; peer vault apps |
| A2 | YAML frontmatter + Markdown body serialize structured “components”; `yaml` package already used in serializer | Verified Fact | `serializeComponentDefinition.ts` |
| A3 | Frontmatter already includes nested `mahogany: { type, version }`, plus `id`, `name`, `directory`, `fields` | Verified Fact | same serializer |
| A4 | SQLite (when added) is **rebuildable cache/index only** — never sole copy of user data | Owner intent | Assignment brief |
| A5 | Renderer must not access filesystem or SQLite directly; main (+ preload bridge) owns privileged I/O | Owner intent | Assignment brief |
| A6 | Electron Forge + Vite multi-process layout (main / preload / renderer) remains the shell | Verified Fact | `forge.config.ts`, Vite configs |
| A7 | External editors, OS file managers, and optional folder sync tools (iCloud/Syncthing/Git) may touch the same files | Observation | Peer-app public discussions |
| A8 | Cross-platform desktop (at least macOS / Windows / Linux) is in scope eventually | Inference | Forge makers include Squirrel, ZIP, Deb, Rpm |
| A9 | Multi-device realtime collaboration is **not** MVP (local-first single primary editor) | Speculation / recommended | Peer conflict tax is high |

---

## 3. Grounding in current scaffold (2026-09)

| Area | Observed state | Risk implication | Label |
| --- | --- | --- | --- |
| Shell | Electron Forge + Vite; Electron 44.3.0; React 19; Vitest present | Good packaging/test footing; native modules later will need rebuild discipline | Verified Fact |
| `BrowserWindow` | `webPreferences: { preload }` only — no explicit `contextIsolation` / `sandbox` / `nodeIntegration` | Modern Electron defaults are safer than older eras, but **explicit secure baseline should be set** before loading untrusted Markdown/HTML | Verified Fact / Inference |
| Preload | Comment-only stub — no `contextBridge` API | Correct empty state for now; **must not** later expose raw `ipcRenderer` or `fs` | Verified Fact |
| DevTools | Always opened in `createWindow` | Fine for prototype; must be gated for packaged builds | Verified Fact |
| Domain | Component definition models, validation, normalization, factories | Early schema discipline is a **positive** signal | Verified Fact |
| Markdown out | Serialize-only path with `mahogany.version: 1`; no deserializer/round-trip tests visible in tree summary | Round-trip / external-edit fidelity still open | Observation |
| Persistence | No watcher, atomic writer, library root, or SQLite yet | Prototype concerns ≠ production bugs — design before growth | Observation |
| Packaging | ASAR on; FusesPlugin enables ASAR integrity + OnlyLoadAppFromAsar; RunAsNode false | Strong packaging hygiene already started | Verified Fact |
| Docs | README empty | Onboarding/contract docs missing (process risk, not runtime) | Verified Fact |

---

## 4. Risk register

Severity: **High** = data loss, security RCE/path escape, or trust-breaking corruption; **Med** = serious UX/reliability debt or recoverable inconsistency; **Low** = cost/perf/polish. “When relevant” = lifecycle stage.

| ID | Risk | Severity | When relevant | Practical mitigation | Label |
| --- | --- | --- | --- | --- | --- |
| R01 | Renderer XSS → privileged FS if IPC/preload too broad or isolation weakened | **High** | Prototype → MVP (as soon as Markdown/HTML/plugins render) | Explicit `contextIsolation: true`, `nodeIntegration: false`, `sandbox: true`; minimal `contextBridge` API; validate paths in **main**; never expose generic invoke; CSP; no `dangerouslySetInnerHTML` without sanitizer | Verified Fact (Electron guidance) |
| R02 | In-place writes → torn/empty files on crash | **High** | MVP (first real save path) | Same-dir temp write → `fsync`/`fdatasync` → `rename` → directory `fsync` where durable; treat rename alone as atomicity ≠ durability | Verified Fact (POSIX durability literature) |
| R03 | File watchers miss external atomic saves (inode replace) | **High** | MVP (external editor / sync) | Watch **parent directories**, not single-file inodes; debounce/coalesce; `awaitWriteFinish` / atomic options if using chokidar; re-read+validate; re-attach on watcher errors | Verified Fact / Observation |
| R04 | Concurrent app + external edit last-write-wins without user noticing | **High** | MVP+ | mtime/hash compare before save; dirty buffer vs disk conflict UI; optional conflict copies (Obsidian-style naming); never silently discard either side without policy | Observation |
| R05 | Path-based references break on rename/move | **High** | MVP once cross-links exist | Stable `id` in frontmatter (already present on definitions); store references by **id**, display path/name; app-mediated rename updates indexes; detect broken refs | Inference / Observation (Obsidian path-link pain; ID plugins) |
| R06 | YAML round-trip mutates user files (dates→Date, key order, booleans, multiline) | **Med→High** | MVP | Quoting rules; schema validation (Zod-class); prefer deterministic stringify options; preserve unknown keys; golden round-trip tests; avoid rewriting files that only “look dirty” | Verified Fact / Observation |
| R07 | Schema / frontmatter evolution without migration story | **Med→High** | MVP → Post-MVP | Keep `mahogany.version`; read adapters per version; migrate-on-read or explicit upgrade tool; never require SQLite for migration | Inference (scaffold already has version field) |
| R08 | SQLite cache diverges from Markdown truth | **High** | When SQLite lands | Content-hash / mtime watermark; incremental invalidate on watch; “Rebuild index” always works; treat DB wipe as safe; never write authoritative fields only to SQLite | Owner intent + Inference |
| R09 | Native module ABI mismatch (`better-sqlite3` etc.) breaks builds | **Med** | When SQLite lands | Electron rebuild via Forge `rebuildConfig`; unpack natives from ASAR; CI matrix per platform; pin Electron/native versions together | Verified Fact |
| R10 | Cross-platform path / case / Unicode normalization bugs | **Med** | MVP multi-OS | Store vault-relative POSIX-style paths in data; resolve via `path` in main only; case-insensitive collision checks on Windows/macOS; NFC normalize names | Observation |
| R11 | Large libraries: watcher storm, cold index, FTS lag | **Med** | Post-MVP (thousands+ files / big attachments) | Ignore globs; batch index; incremental FTS; virtualized UI; attachment size caps; don’t full-rescan on every event | Observation / Inference |
| R12 | Attachments (maps, PDFs, audio) orphaned or bloated sync | **Med** | MVP light / Post-MVP heavy | Sidecar folder convention; hash-named blobs optional; refs by id; exclude from naive sync; quarantine missing assets | Observation |
| R13 | Packaging / code signing / auto-update supply chain | **Med→High** | Distribution | Keep fuses; sign+notarize; signed update feeds; force signing in CI; never ship always-on DevTools | Verified Fact / Observation |
| R14 | Folder sync tools (iCloud/Syncthing) create conflict duplicates | **Med** | Anytime users sync vault folder | Document “one writer”; ignore app cache dirs; conflict file detection; eventual first-party sync is separate product | Observation (Obsidian/Logseq public issues) |
| R15 | Plugin/extensibility without sandbox → RCE | **High** | Post-MVP | Delay plugins; if added: no Node in plugin renderer; capability tokens; signed packages; separate process later | Inference |
| R16 | Insufficient automated tests around FS edge cases | **Med** | Prototype → MVP | Vitest for pure domain/YAML; temp-dir integration tests for atomic write/watch/reconcile; fixture libraries of hostile Markdown | Inference |
| R17 | Electron memory/bundle size vs Tauri | **Low** | Post-MVP polish | Accept Electron cost for Chromium consistency / JS ecosystem; revisit Tauri only if size/memory becomes a measured user problem | Observation |

---

## 5. Output buckets (required)

### 5.1 Prototype concerns

*Things to get right while the app is still a scaffold — cheap now, expensive after habits form.*

1. **Lock Electron security explicitly in `BrowserWindow`**  
   Do not rely on “defaults are fine forever.” Set and document: `contextIsolation: true`, `nodeIntegration: false`, `sandbox: true`, `webSecurity: true`. Gate `openDevTools()` behind `!app.isPackaged` or an env flag. **[Verified Fact]** — current `main.ts` only sets `preload`; DevTools always open.

2. **Design the preload contract before the first FS call**  
   Empty preload is good. When adding APIs, expose *named* operations (`library.open`, `component.save`, `index.search`) — never `invoke(channel, ...)` passthrough or path-arbitrary `readFile`. Validate that every path is inside the chosen library root (realpath + prefix check). **[Verified Fact]** — Electron security guides.

3. **Preserve and expand the `mahogany.version` / `type` envelope**  
   Serializer already writes `mahogany: { type: "component-definition", version: 1 }`. Treat this as the migration spine for all future file kinds. **[Verified Fact]**

4. **Decide identity policy before cross-references**  
   `id` already exists on definitions. Codify: IDs are stable UUIDs (or ULID); filenames are display convenience; references use IDs. Document what happens if a user deletes `id` in an external editor. **[Inference]**

5. **Round-trip tests before “save” ships**  
   Implement deserialize + serialize golden tests (key order, Unicode, nested fields, unexpected keys). Prefer preserving unknown frontmatter keys so external tooling does not fight Mahogany. **[Observation]** — YAML date/boolean traps are well-documented with gray-matter/js-yaml ecosystems; Mahogany uses `yaml` package — same class of issues.

6. **Keep domain pure and FS at the edge**  
   Current split (`domain/` vs `infrastructure/markdown/`) is healthy. Do not let React components import Node `fs`. **[Observation]**

7. **Ignore list / library root conventions early**  
   Even a prototype should define `.mahogany/` (or similar) for disposable cache and ensure watchers ignore it — prevents feedback loops later. **[Inference]**

### 5.2 MVP concerns

*Must be correct for a trustworthy single-user local library.*

1. **Atomic + (appropriately) durable saves**  
   Pattern: write temp in same directory → sync file → rename over target → sync directory when durability matters (campaign notes users care about). Same-filesystem rename only. **[Verified Fact]**

2. **Directory-based watching + reconcile loop**  
   External editors (VS Code, Obsidian, Vim variants) often save via temp+rename, replacing inodes. File-level watches go silent; directory watches survive. Debounce, then hash/mtime reconcile into memory + SQLite. Re-subscribe on errors. Joplin’s public Chokidar throttle issues show even mature apps miss rapid external edits without careful queueing. **[Verified Fact / Observation]**

3. **Conflict detection for dirty buffers**  
   If disk changed since load, block blind overwrite; offer reload / overwrite / save-as-conflict-copy. Peer pattern: Obsidian Sync conflict copies with device+timestamp naming. **[Observation]**

4. **Stable IDs + broken-reference UX**  
   Index `id → path`. On missing target, show broken-ref state; do not invent files silently unless product explicitly wants wiki-style create-on-click. Obsidian’s default path/wikilink model is known to confuse workflows that expect frontmatter IDs. **[Observation]**

5. **Schema validation on read**  
   Invalid YAML or failed schema → quarantine file in UI (open as raw text), do not crash the library, do not delete. Soft-fail with actionable errors. **[Inference]**

6. **SQLite as cache with mandatory rebuild**  
   When introduced: store only derived rows (titles, ids, links, FTS). Startup: verify schema version + watermark; if mismatch, rebuild. Expose “Rebuild index” in UI. Native rebuild via Forge. Unpack natives. **[Verified Fact / Owner intent]**

7. **Path normalization**  
   Persist vault-relative paths with `/`; resolve on the OS in main. Detect case-only collisions. **[Observation]**

8. **Minimal backup story**  
   Even MVP: optional timestamped copy-on-write into `.mahogany/backups/` before destructive migrations; document that Git/Time Machine remain first-class. Logseq’s `bak` folder is a peer precedent. **[Observation]**

9. **Testing matrix**  
   Unit: YAML/domain. Integration: temp vault fixtures (atomic save, external rewrite, rename, broken YAML). Do not wait for E2E Electron for core FS invariants. **[Inference]**

10. **Security review of Markdown rendering**  
    Preview must sanitize HTML; disable `file://` navigation to outside vault; treat library content as untrusted input. **[Verified Fact]** — XSS→RCE chain is the classic Electron failure mode.

### 5.3 Post-MVP concerns

*Real, but should not block first trustworthy library.*

1. **Full-text search at scale** — SQLite FTS5 or similar; incremental updates; ranking; non-blocking UI.  
2. **Large attachment pipelines** — thumbnails, dedupe, media metadata, size budgets.  
3. **Multi-device sync product** — app-aware sync beats blind folder sync; conflict CRDT/OT is a product, not a weekend. **[Observation]**  
4. **Plugin / script extensibility** — capability security model; separate from core.  
5. **Auto-update + signing operations** — notarization, update signature verification, staged rollouts. Forge makers exist; update channel not evidenced in scaffold. **[Observation]**  
6. **Performance profiling on 10k–100k note libraries** — watcher batching, lazy parse, worker threads for index.  
7. **Mobile / second shell** — out of scope unless Owner expands; Electron does not automatically give mobile.  
8. **Import/export fidelity** from Notion/World Anvil/etc. — export ≠ native model (**Observation** from prior ExploreGrokBot work).

### 5.4 Problems we should deliberately ignore for now

*Acknowledged so they do not hijack the roadmap.*

| Ignore (for now) | Why |
| --- | --- |
| Rewriting in Tauri/Rust “for modernity” | Electron is acceptable; Tauri trades bundle size/memory for WebView variance and Rust IPC surface. Revisit only on measured pain. |
| Realtime multiplayer editing of the same Markdown file | Conflict tax dominates; local-first single primary writer first. |
| Perfect byte-identical round-trip of every exotic YAML 1.1 quirk on day one | Enforce a documented subset; preserve unknowns; expand tests over time. |
| Custom CRDT / OT sync protocol | Folder + Git is enough for early users. |
| Full Obsidian plugin marketplace compatibility | Different product; huge security surface. |
| Matching Obsidian Live Preview polish | Editor quality is product depth, not architecture risk for data integrity. |
| Micro-optimizing Chromium RAM before feature-complete library I/O | Premature. |
| End-to-end encrypted cloud sync | Separate product decision. |
| Notion-like relational DB as primary store | Contradicts Markdown-authoritative thesis. |

---

## 6. Deep dives on investigated surfaces

### 6.1 Filesystem watching

**Failure modes:** missed events after atomic replace; duplicate burst events; Windows/network FS needing polling; handle invalidation when vault root moves; feedback loops watching the app’s own cache writes. **[Verified Fact / Observation]**

**Mitigations:** directory watch; ignore globs (`.git`, `.mahogany`, `node_modules`, OS junk); debounce 50–200ms+; coalesce by path; always re-stat/hash; periodic full reconcile as safety net; self-write generation tokens to ignore echo events.

**Peers:** Community tooling around Obsidian vaults explicitly watches parent directories for temp+rename saves; Joplin fixed external-edit races around Chokidar throttling. **[Observation]**

### 6.2 Atomic writes & crash recovery

**Atomicity** (readers see old or new file) ≠ **durability** (survives power loss). Rename gives atomicity on same filesystem; `fsync` of file + directory gives durability. **[Verified Fact]**

**MVP policy recommendation:** always atomic rename for note saves; add directory fsync for “commit points” (explicit save, autosave flush, pre-quit). Accept that extreme power-loss durability has perf cost on HDDs.

**Recovery:** on startup, scan for `*.tmp` / `*.mahogany-tmp` leftovers; never delete the only good file; rebuild SQLite freely.

### 6.3 Concurrent edits & external editors

Three writers: Mahogany UI, external editor, sync agent. Public Obsidian/Logseq discussions show Syncthing/iCloud conflicts, duplicate notes, and “app unaware of sync.” **[Observation]**

**Mitigations:** single active library lock file (advisory); document sync exclusions for cache; conflict copies; reduce write frequency to disk if a future sync feature exists (Joplin-like “commit to md” cadence discussed by Logseq users).

### 6.4 Renames, moves, stable identifiers, broken references

Obsidian primarily resolves **path/filename** wikilinks; frontmatter `id` is not a first-class resolver without plugins — a cautionary tale. **[Observation]**

Mahogany should:  
- Require `id` on authoritative entities.  
- Index links by id.  
- Offer path-based display strings that do not affect identity.  
- On rename via app: update path index only.  
- On external rename: detect via watch (unlink+add or rename events), rematch by scanning frontmatter `id` (not by path memory alone).

### 6.5 Schema migrations & YAML/frontmatter evolution

Scaffold version field is the right start. **[Verified Fact]** Plan:

1. Version N readers understand N and N−k.  
2. Migrations are pure functions over frontmatter(+body).  
3. Batch migrate with backup.  
4. Unknown fields preserved.  
5. Strict mode optional for CI fixtures; lenient mode for user libraries.

YAML traps: unquoted dates becoming dates; `yes`/`no` booleans; duplicate keys; very large nested structures in frontmatter (prefer body or sidecar for huge blobs). **[Verified Fact / Observation]**

### 6.6 Markdown parsing / round-tripping

Components-as-Markdown means Mahogany owns a **dialect**. Risks: drifting serializers reformatting users’ prose; frontmatter delimiter collisions in content; Windows CRLF.

**Mitigations:** separate “structured fields” (frontmatter) from “narrative body”; never pretty-print body unless user asks; normalize newlines intentionally; fuzz tests with hostile fixtures.

### 6.7 SQLite synchronization & index rebuilding

**Rule:** Markdown wins. SQLite is a projection.

Protocol sketch:  
1. Watch event → enqueue path.  
2. Parse → validate → upsert derived rows / delete if removed.  
3. If parse fails → mark `index_error`, keep last good derived row optional policy.  
4. Global rebuild: wipe derived tables, walk vault, ignore cache dirs.

FTS: store plain-text extraction, not raw HTML. Attachments: metadata only in DB unless thumbnails cached under `.mahogany/`.

Native module risk is operational (CI), not conceptual. **[Verified Fact]**

### 6.8 Backups

Layers: (1) user Git/Time Machine, (2) pre-migration snapshots, (3) optional in-app version history (Post-MVP). Do not invent a pseudo-database backup that ignores Markdown.

### 6.9 Large libraries & FTS

Watchers and UI virtualization dominate before raw Markdown parse cost. Ignore non-library trees. Consider sharding FTS later — not now.

### 6.10 Attachments

Convention: `attachments/<id>-<slug>.ext` or parallel folder per entity. Store hashes for integrity. Missing file = soft error. Beware iCloud placeholder files (0-byte stubs) on macOS — detect and wait. **[Speculation / Observation]**

### 6.11 Cross-platform paths

Never persist `C:\\...` inside content. Symlinks: decide allowlist policy (follow within vault only). APFS/Windows case folding: prevent two IDs mapping via case collision on filenames.

### 6.12 Electron IPC design

Channel allowlists in preload; structured clone–safe payloads; size limits; no sending DB handles; request IDs for cancel; push events `library:changed` with coarse invalidation rather than dumping whole vault over IPC.

### 6.13 Electron security

Baseline from current public guidance: isolation + sandbox + no node in renderer + tiny bridge + CSP + path containment + disable navigation. Fuses already harden packaged app (ASAR integrity, OnlyLoadAppFromAsar, RunAsNode off). **[Verified Fact]** — `forge.config.ts`.

### 6.14 Packaging / updating

Forge makers present; signing/update feed not configured in inspected files. Distribution risk arrives at first external users: unsigned macOS/Windows friction, compromised update servers. Mitigate with signed artifacts and pinned update HTTPS + signature verify.

### 6.15 Testing

Vitest already in repo — good. Expand toward FS contract tests. Electron Spectron-class E2E is optional; prioritize deterministic Node tests of main-side libraries.

### 6.16 Future plugins

Ignore until core FS trust is boring. If needed: host plugins like VS Code extensions with explicit API, not `eval` of vault scripts with Node rights.

---

## 7. Comparisons to peer local-first / filesystem-backed apps

| Peer | Relevant lesson for Mahogany | Label |
| --- | --- | --- |
| **Obsidian** | Vault = folder; Electron desktop; metadata cache; path-centric links; Sync conflict copies; external sync tools cause duplicates | Verified Fact / Observation |
| **Logseq** | Graph folder + `bak`; Syncthing conflict spam when always-on remote sync races the app | Observation |
| **Joplin** | External editor watcher subtlety (Chokidar throttle); MD export sync model differs from live vault | Observation |
| **Foam / VS Code** | IDE file model: editor buffer vs disk; rely on VS Code FS APIs; good mental model for dirty buffers | Observation |
| **Notion export** | Export is not a native working format — reinforces Mahogany’s Markdown-as-source advantage if fidelity is kept high | Observation |
| **Tauri (comparison only)** | Smaller bundles, capability FS permissions by default; costs Rust skills + WebView variance. Not a mandate to rewrite. | Observation |

**Inference:** Mahogany should copy **Obsidian’s local folder trust** and **VS Code’s buffer/disk honesty**, while learning from **Obsidian ID/path confusion** and **Logseq/Syncthing conflict** reports — without cloning closed-source internals.

---

## 8. Open questions for Owner

1. Is the library root a single “vault” folder chosen by the user (Obsidian-style), or an app-managed documents directory?  
2. Are filenames user-meaningful, or may they be ID-based with titles only in frontmatter?  
3. Will MVP support intentional external editing (VS Code) as a first-class workflow, or “supported but best-effort”?  
4. Which link syntax is canonical — Mahogany IDs, wikilinks, standard Markdown links, or all three?  
5. Attachments: embed in vault vs content-addressed blob store under `.mahogany/`?  
6. Is Git the blessed backup, or is in-app history required for MVP?  
7. Target platforms for first paid/public users (macOS-only vs Win+Mac)?  
8. Timeline for SQLite — before or after multi-file library UX feels solid?  
9. Will component definitions and component **instances** share one file format family with different `mahogany.type` values?  
10. Any plan for encrypted libraries at rest (OS secret store vs vault password)?

---

## 9. Recommended sequencing (advisory, not a redesign)

1. Secure BrowserWindow + preload API shape (even if APIs are stubs).  
2. Library open/watch/reconcile + atomic save without SQLite.  
3. Deserialize + schema version adapters + round-trip tests.  
4. ID-based references + broken-ref UI.  
5. Add disposable SQLite index + rebuild.  
6. FTS, attachments polish, packaging/signing.  
7. Sync/plugins only after the above is boring.

---

## 10. Citations

1. Electron security / contextIsolation / sandbox / preload discipline — e.g. public guides summarizing Electron `webPreferences` baselines (DeepStrike Electron pentest notes; ContextBridge security writeups; Electron IPC guides).  
2. Chokidar README — `atomic`, `awaitWriteFinish`, polling options: https://github.com/paulmillr/chokidar  
3. File watching + atomic replacement (directory watch vs inode): https://www.thenodebook.com/file-system/watching-atomic-writes  
4. Crash consistency / fsync + rename + directory fsync: POSIX durability articles (e.g. 0xKiire crash-consistency; Calvin Loncaric durable create).  
5. Obsidian Sync troubleshooting / conflict copy naming: https://obsidian.md/help/sync/troubleshoot  
6. Obsidian sync conflict analysis (third-party): https://synch.run/blog/obsidian-sync-conflicts/  
7. Logseq + Syncthing conflict discussion: https://github.com/logseq/logseq/discussions/7944  
8. Joplin external editor watcher / Chokidar throttle: https://github.com/laurent22/joplin/issues/14957  
9. gray-matter / Zod frontmatter validation & YAML date traps: gray-matter repo; zod-matter; practitioner guides on quoted dates.  
10. better-sqlite3 + Electron rebuild / ASAR unpack: WiseLibs issues; Electron native module docs; Forge auto-unpack-natives.  
11. Electron Forge fuses / packager ASAR: https://www.electronforge.io (config & auto-unpack-natives).  
12. Tauri vs Electron tradeoffs (size/memory/capabilities): public 2025 comparison posts (DoltHub, OpenReplay, Hopp) — comparison only.  
13. Obsidian internal links / rename behavior (path-centric): Obsidian help “Internal links”.  
14. Mahogany public repo inspection (2026-09): https://github.com/WebDevJasonCameron/mahogany — `package.json`, `src/main.ts`, `src/preload.ts`, `forge.config.ts`, `serializeComponentDefinition.ts`, domain/test tree.

---

## 11. Confidence, blockers, and handoff notes

**Confidence:** High on FS/Electron risk catalog; Moderate on Mahogany-specific schema roadmap; Low on unbuilt sync/plugin surfaces.

**Blockers / unknowns:** Owner answers to §8 (especially identity, external-edit support level, and SQLite timing) would refine severity ordering. No runtime testing of Mahogany was performed (read-only remote inspection only). No proprietary binaries reverse-engineered.

**Constraints honored:** No PRs, pushes, or modifications to the mahogany GitHub repository. Assessment distinguishes **current scaffold** vs **intended architecture**.

---

*End of Assignment 004 — Mahogany Architecture Risk Assessment*
