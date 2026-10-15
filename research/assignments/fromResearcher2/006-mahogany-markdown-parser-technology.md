# 006 — Mahogany Markdown Parser Technology

- **Researcher:** Researcher 2 (Market Research Analyst)
- **Owner:** Jason Cameron
- **Date:** 2026-10-15
- **Status:** Complete — awaiting Owner review
- **Filing path:** `research/assignments/fromResearcher2/006-mahogany-markdown-parser-technology.md`
- **Related issue:** 0.1.6.5 — Implement Markdown → Field Parsing
- **Leading candidate:** `remark-parse` + `remark-gfm` + unified / mdast
- No changes to mahogany repo.

> **Evidence labels.** **[Verified Fact]** = observed in an executed test on 2026-10-15, or stated in a primary spec/official docs fetched that day. **[Assumption]** = not directly tested here. **[Recommendation]** = this researcher's advice; *not* an approved decision. **[Open]** = choice for Owner/Architect. This report does **not** redefine the Field model or implement the production reader.

> **Executed vs proposed.** Sections marked **EXECUTED** report real outputs from `/workspace/poc-006`. Sections marked **PROPOSED** are illustrative only.

---

## 1. Executive summary

1. **[Recommendation]** Proceed with **`unified` + `remark-parse` + `remark-gfm` (+ `remark-frontmatter` for YAML)** as the Phase 0 Markdown reader. Keep a thin **parser adapter** that maps mdast → Mahogany domain model and never leaks mdast types into Fields. Component Definitions are not required to parse.

2. **[Verified Fact — EXECUTED]** The irregular table row `| Lothar | Fighter | Veteran |` under a 2-column header: **`Veteran` survives in the remark-gfm mdast** as a third `tableCell`. The body `tableRow.position` offsets cover the full authored line, so `source.slice(start.offset, end.offset)` recovers `| Lothar | Fighter | Veteran |`. **markdown-it drops `Veteran`** from its token stream (HTML-faithful). **`@lezer/markdown` keeps `Veteran`** as a `TableCell` with exact `from`/`to` ranges.

3. **[Verified Fact — EXECUTED]** GFM HTML *renders* by padding missing cells and ignoring excess cells (GFM 0.29-gfm §4.10). remark-gfm's **AST does not pad** missing cells (`| A |` → 1 cell) and **does keep** excess cells. Successful parse ≠ semantic or byte-level preservation of table *shape*; preservation of excess content requires either the AST's extra cells or the row source slice.

4. **[Verified Fact — EXECUTED]** Every node in the tested mdast trees carried `position.start/end` with `line`, `column`, and `offset`. Offsets are **JavaScript string indices (UTF-16 code units)**, not UTF-8 bytes. A known caveat: for text spanning blockquote continuations, `source.slice(offsetSpan)` can include `> ` prefixes that are absent from `node.value` (documented upstream behavior).

5. **[Verified Fact — EXECUTED]** Required constructs parse: ATX/setext headings, nested tight/loose lists, GFM task lists (`listItem.checked`), nested blockquotes, fenced + indented code, aligned tables. Structural smoke over CommonMark 0.31.2 focus sections: **212/212 pass**. GFM tables, tasks, strikethrough, escaped pipes: all smoke-pass.

6. **[Recommendation]** Source-preservation strategy for Phase 0 (read-only): retain the original file string; attach mdast positions; for Table Fields and any irregular rows, prefer **row (or table) source slices** over reconstructing from cells alone. Do not serialize through `remark-stringify` for writes (out of Phase 0 scope, but established in assignment 005).

7. **Alternatives:** (a) **micromark events + `mdast-util-from-markdown` directly** — same stack, slightly lower-level; no meaningful advantage over remark for Mahogany. (b) **`@lezer/markdown`** — better concrete syntax / editor ranges; weaker semantic document model; good *complement* if CodeMirror 6 is the editor, not a replacement for the domain adapter. (c) **markdown-it** — weaker for source-preserving tables (drops excess cells; line-level `map` only).

8. **Risks deserving early automated tests:** excess/missing table cells; omitted vs empty cells; escaped `|` and pipes in `inlineCode`; position-slice invariants; CRLF; BOM; entity/escape decoding vs raw slice; flat heading sequence; ESM-only packaging in Electron/Vite/Vitest.

---

## 2. Candidate library evaluation

### 2.1 Stack under test (installed 2026-10-15 in `/workspace/poc-006`)

| Package | Installed version | `package.json` type | npm `time.modified` (approx.) |
|---|---|---|---|
| `unified` | 11.0.5 | module (ESM) | 2024-06-19 |
| `remark-parse` | 11.0.0 | module | 2023-11-20 |
| `remark-gfm` | 4.0.1 | module | 2025-02-10 |
| `remark-frontmatter` | 5.0.0 | module | 2023-11-20 |
| `micromark` | 4.0.3 | module | 2026-09-26 |
| `micromark-extension-gfm` | 3.0.0 | module | 2023-06-26 |
| `mdast-util-from-markdown` | 2.1.0 | module | 2026-10-03 |
| `mdast-util-gfm` | 3.1.0 | module | 2025-02-10 |
| `@types/mdast` | 4.0.4 | (types) | 2026-10-04 |
| `markdown-it` (comparison) | 15.0.2 | commonjs | 2026-09-12 |
| `@lezer/markdown` (comparison) | 1.8.0 | module | 2026-10-07 |

### 2.2 Compatibility with CommonMark 0.31.2 + GFM 0.29-gfm

**[Verified Fact — Spec]** GFM is a strict CommonMark supersets adding tables, task list items, strikethrough, extended autolinks, and disallowed raw HTML (tagfilter). Sources: <https://spec.commonmark.org/0.31.2/>, <https://github.github.com/gfm/> (accessed 2026-10-15).

**[Verified Fact — Docs]** micromark README claims **100% CommonMark** and **100% GFM** via `micromark-extension-gfm`. remark-parse builds on micromark + `mdast-util-from-markdown`; remark-gfm wires GFM extensions.

**[Verified Fact — EXECUTED]** Local smoke tests (`compatibility.ts`, `spec-sample.ts`):

| Feature | Result |
|---|---|
| ATX headings (levels 1–3 tested) | Pass — `heading.depth` set; positions present |
| Setext H1 (`===`) / H2 (`---`) | Pass |
| Nested lists (3 levels) | Pass — `list` inside `listItem` |
| Tight vs loose (`spread`) | Pass — ordered list with blank line → `spread: true` |
| Task lists `- [ ]` / `- [x]` | Pass — `listItem.checked` false/true |
| Nested blockquotes | Pass |
| Fenced code + info string (`statblock`) | Pass — `code.lang === "statblock"` |
| Indented code | Pass — `code.lang === null` |
| Tables with alignment `|:--|:-:|--:|` | Pass — `align: ["left","center","right"]` |
| CommonMark structural sample (headings, code, quotes, lists, thematic breaks, paragraphs) | **212/212 pass** (structure presence vs spec HTML tags; not full HTML equality) |
| GFM table / task / strikethrough / escaped-pipe examples | All smoke PASS |
| Header/delimiter cell-count mismatch | Correctly **not** a table (paragraph) — matches GFM ex. 203 |

**Significant limitations [Verified / Assumption]:**

- **Delimiter row** is not a child node; alignment is on `table.align` only. Table `position` *span* still covers the delimiter line in source. **[Verified Fact — EXECUTED]**
- **Missing body cells are not padded in mdast**; excess cells are **kept**. Differs from GFM HTML. **[Verified Fact — EXECUTED]**
- **Front matter** requires `remark-frontmatter` (not part of remark-gfm). **[Verified Fact — EXECUTED]**
- **Wikilinks / Obsidian callouts** are not first-class nodes without extra plugins; they appear as text / blockquote. **[Verified Fact — EXECUTED]**
- **Link reference definitions** become `definition` nodes (not rendered content). **[Verified Fact — EXECUTED]**
- Full CommonMark HTML-equality suite was **not** run end-to-end in this PoC (only structural sample). Treat “100% compliant” as **[Assumption]** backed by micromark’s published claims + our sample, not as a Mahogany CI result yet.

### 2.3 TypeScript / Electron / Vite fit

- Stack is **ESM-only**. Vite already expects ESM; Electron main/renderer and Vitest need `"type": "module"` or explicit `.mjs` / Vite SSR config. **[Assumption]** Mahogany’s Vite setup can consume remark without a CJS shim (standard in 2026 Electron+Vite apps).
- Types: `@types/mdast` provides the document model; remark packages ship JSDoc types consumed by TypeScript 5+/7.
- Pure JS — runs in main, renderer, or worker; no native addon (unlike tree-sitter).

### 2.4 Adapter boundary (no Field redefinition)

**[Recommendation]** Pipeline: `string → remark parse (mdast Root) → MahoganyMarkdownAdapter → domain document/Fields`. The adapter:

1. Walks mdast (e.g. `unist-util-visit`).
2. Emits Mahogany structures using the **already-approved** Field types (not redefined here).
3. Stores **source offsets** (and optionally row/table raw slices) on adapted nodes for later splice-writes.
4. Never imports mdast types into Field definitions or Component Definitions.

Component Definitions remain schema for *authored Mahogany components*, not a prerequisite to *read* arbitrary Markdown.

---

## 3. Irregular table findings

### 3.1 Spec baseline **[Verified Fact — Spec]**

GFM 0.29-gfm §4.10 (accessed 2026-10-15):

- Header and delimiter cell counts must match, or there is no table.
- Leading/trailing pipes optional; cell content trimmed.
- Body rows with **fewer** cells: empty cells are inserted **in HTML**.
- Body rows with **greater** cells: **excess is ignored** in HTML.
- Pipes in cells must be escaped (`\|`), including inside other inline spans.

### 3.2 Critical example — EXECUTED

Source:

```markdown
| Name | Class |
| --- | --- |
| Lothar | Fighter | Veteran |
```

**remark-gfm mdast (EXECUTED):**

| Observation | Result |
|---|---|
| Body row cell count | **3** |
| Cell texts | `Lothar`, `Fighter`, **`Veteran`** |
| `Veteran` in AST? | **Yes** |
| Body row `position` | `offset` 31–61 |
| `SOURCE.slice(31, 61)` | `"| Lothar | Fighter | Veteran |"` — **full authored row recovered** |
| Header cells | 2 (`Name`, `Class`) |
| `align` | `[null, null]` |

**markdown-it 15.0.2 (EXECUTED):** tokens for the body row include inline contents `Lothar`, `Fighter` only — **`Veteran` absent**. `map` is line-level (`[2,3]` for the row); no character offsets on cells.

**@lezer/markdown 1.8.0 + GFM (EXECUTED):** `TableRow [31,61]` contains three `TableCell` nodes including `Veteran` at `[52,59]`. Concrete ranges over the source string.

### 3.3 Omitted vs explicitly empty — EXECUTED

| Source body row | mdast cell count | Cell texts | Notes |
|---|---|---|---|
| `\| A \|` | 1 | `["A"]` | **Not padded** to header width |
| `\| A \| \|` | 2 | `["A", ""]` | Empty cell present with position |
| `\| A \|  \|` | 2 | `["A", ""]` | Whitespace-only → empty text; distinguishable from omit only via cell count / source slice |
| `\| A \| B \| C \|` | 3 | `["A","B","C"]` | Excess **kept** (unlike GFM HTML / markdown-it) |

**[Verified Fact]** Omitted cells vs empty cells **can** be distinguished in mdast by **whether the padded cell node exists**. Relying only on “empty string” is insufficient for omitted cells (node absent). Source slice of the row remains the ground truth for fidelity.

### 3.4 Outer pipes — EXECUTED

Without leading/trailing pipes (`Lothar | Fighter | Veteran`), remark-gfm still builds a table; excess `Veteran` still present; row slice recovers the full line.

### 3.5 Escaped pipes and inline Markdown — EXECUTED

| Construct | Result |
|---|---|
| `f\|oo` in header | Text node value `f|oo` (unescape); row slice retains `\|` |
| `` b `\|` az `` | `inlineCode` with value `|` |
| `**x**` | `strong` |
| `[lnk](u)` | `link` |
| `a *b* c` | text + `emphasis` + text |

### 3.6 Implications for Table Fields **[Recommendation]**

1. Treat **row source slices** (via `tableRow.position`) as the fidelity channel for irregular rows.
2. When mapping to a fixed-column Table Field: pad missing cells in the **adapter** (not expected from mdast); decide explicitly whether excess cells become overflow metadata, a warning, or additional columns — **[Open]**.
3. Do not assume markdown-it and remark agree on excess cells — they do not (**EXECUTED**).

### 3.7 Minimal reproducible TypeScript example (EXECUTED)

Saved at `/workspace/poc-006/mre-irregular-table.ts`. Run: `npx tsx mre-irregular-table.ts`.

```typescript
/**
 * Minimal reproducible example — irregular GFM table excess cell.
 * Run: npx tsx mre-irregular-table.ts
 * Verified 2026-10-15 with remark-parse@11.0.0 + remark-gfm@4.0.1
 */
import { unified } from 'unified';
import remarkParse from 'remark-parse';
import remarkGfm from 'remark-gfm';
import type { Root, Table, TableRow } from 'mdast';

const SOURCE = `| Name | Class |
| --- | --- |
| Lothar | Fighter | Veteran |
`;

const tree = unified().use(remarkParse).use(remarkGfm).parse(SOURCE) as Root;
const table = tree.children.find((n) => n.type === 'table') as Table;
const body = table.children[1] as TableRow;

console.log('body cell count:', body.children.length); // → 3
console.log(
  'cell texts:',
  body.children.map((c) =>
    c.children.map((n: any) => (n.type === 'text' ? n.value : '')).join('')
  )
); // → ['Lothar', 'Fighter', 'Veteran']

const { start, end } = body.position!;
console.log('row source slice:', JSON.stringify(SOURCE.slice(start.offset!, end.offset!)));
// → "| Lothar | Fighter | Veteran |"
```

**EXECUTED output:**

```
body cell count: 3
cell texts: [ 'Lothar', 'Fighter', 'Veteran' ]
row source slice: "| Lothar | Fighter | Veteran |"
```

---

## 4. Source preservation strategy

### 4.1 What positions provide — EXECUTED

- On tested trees (headings, lists, tasks, blockquotes, code, tables, yaml front matter, html, definitions): **all nodes had** `position.{start,end}.{line,column,offset}`.
- `offset` is a **0-based index into the JavaScript string** passed to `parse` (UTF-16 code units). Astral characters (e.g. `🎯`) count as 2 units in `.length` / offsets — standard JS behavior. **[Verified Fact — EXECUTED]** for `Café 🎯` heading slice round-trip.
- **CRLF:** `\r\n` counts as 2 offset units; parse still succeeds. **[Verified Fact — EXECUTED]**
- **BOM (`U+FEFF`):** heading text was `BomTitle` (BOM not in text value); heading `position.start.offset` was `0` (BOM at index 0). **[Verified Fact — EXECUTED]** Adapter should strip/ignore BOM before parse or adjust offsets — **[Recommendation]**.

### 4.2 Raw slicing

**[Recommendation]** Keep `originalSource: string` beside the tree. For any node with offsets, `originalSource.slice(start.offset, end.offset)` recovers that span. Use this for:

- Irregular table rows / full tables
- Fenced code blocks (already have `value`, but slice preserves fence style)
- Unknown / extension-like text (wikilinks, callouts)
- Future splice-writes (assignment 005)

### 4.3 What is normalized or discarded in the AST (not in the file)

| Input | In mdast | Raw file |
|---|---|---|
| List marker `-` vs `*` | Not stored | Preserved in file; lost if re-serialized |
| ATX vs setext | Only `heading.depth` | Style only in source / inferable from slice |
| Table padding / delimiter text | Not as nodes; `align` only | In source; table position covers delimiter |
| `&amp;` | Decoded to `&` in `text` | Slice keeps `&amp;` |
| `\*` escape | Becomes `*` in `text` | Slice keeps `\*` |
| `[[Wiki Link]]` | Plain `text` | Unchanged in file |
| `> [!note] Title` | `blockquote` + paragraph text starting `[!note]…` | Unchanged |
| Raw HTML | `html` node with string value | Unchanged |
| Link reference defs | `definition` nodes | Unchanged |
| Front matter without plugin | Parsed as thematic break / setext / paragraphs **[Assumption]** without `remark-frontmatter` | — |
| Front matter with `remark-frontmatter` | `yaml` node, raw value string | Unchanged |
| Excess table cells | **Kept** in remark-gfm AST | Unchanged |
| Missing table cells | **Not padded** in AST | Unchanged |

**[Verified Fact — EXECUTED]** Entity decode, escape unescape, wikilink-as-text, callout-as-blockquote, html node, yaml node, excess-cell keep, missing-cell non-pad.

### 4.4 Known position caveat **[Verified Fact — Docs + EXECUTED]**

For `> *a*\n> b`, a text node’s `value` can be `"\nb"` while `source.slice(start,end)` is `"\n> b"` (includes blockquote marker). Confirmed EXECUTED. **Do not assume `slice.length === node.value.length`.** Prefer slice for byte-faithful preservation; use `value` for semantic text.

### 4.5 Phase 0 read-only policy **[Recommendation]**

1. Parse with remark + GFM + frontmatter.
2. Adapter builds domain model from mdast **and** retains offsets / selective slices.
3. Never claim “lossless” solely because parse succeeded.
4. Defer writes to the splice strategy (005); do not round-trip through `remark-stringify` for persistence.

---

## 5. Relevant alternatives

### 5.1 micromark + `mdast-util-from-markdown` directly

Same underlying tokenizer and AST as remark-parse. **Advantage:** slightly more control over extension wiring. **Disadvantage:** more boilerplate; remark already is the thin unified plugin over this stack. **[Recommendation]** No meaningful advantage for Mahogany Phase 0 — stay on remark.

### 5.2 `@lezer/markdown` (CodeMirror 6)

**EXECUTED:** keeps excess `Veteran` cell; exact `from`/`to` on delimiters and cells; GFM via `parser.configure([GFM])`.  
**Advantage:** concrete syntax tree ideal for editor highlighting/folding; ranges include pipe delimiters as nodes.  
**Disadvantage:** not a semantic mdast; weaker typed document model for Field mapping; repo relocated (haverbeke.berlin) though npm still publishes.  
**[Recommendation]** Use as **editor companion** if CM6 is chosen; do **not** replace remark for the domain adapter. Add fixture tests that block boundaries agree.

### 5.3 markdown-it

**EXECUTED:** drops excess table cells; `map` is `[startLine, endLine]` for blocks; no inline character offsets. Mature, fast, CJS-friendly.  
**[Recommendation]** Suitable for HTML preview only — **not** for source-preserving Table Fields.

### 5.4 Custom parser

**[Recommendation]** Do **not** build a custom Markdown parser. Established libraries satisfy CommonMark/GFM + positions. Custom work belongs in the **adapter** and splice layer.

---

## 6. PoC code and test results

### 6.1 Location

All PoC under `/workspace/poc-006` (not the mahogany repo):

| File | Role |
|---|---|
| `irregular-table.ts` | Excess/missing/empty cells; pipes; markdown-it + Lezer compare |
| `mre-irregular-table.ts` | Minimal reproducible excess-cell example |
| `compatibility.ts` | Headings, lists, tasks, quotes, code, tables, FM, HTML, unicode/CRLF/BOM |
| `offset-caveat.ts` | Blockquote position vs value |
| `spec-sample.ts` | CommonMark JSON structural sample + GFM smoke |
| `versions.json` | Exact installed versions |
| `package.json` / `node_modules` | Locked installs from 2026-10-15 |

### 6.2 EXECUTED results (summary)

| Test | Result |
|---|---|
| `Veteran` in remark mdast | **Present** (3 cells) |
| Row slice recovers full line | **Yes** |
| markdown-it keeps `Veteran` | **No** |
| Lezer keeps `Veteran` | **Yes** |
| Omitted vs empty cells | Distinguishable by cell node presence |
| Escaped `\|` / code pipe / emphasis / link in cells | Correct mdast nodes |
| Positions on all nodes (tested cases) | Yes |
| CM focus-section structural sample | 212/212 |
| GFM table/task/strike smokes | Pass |
| Front matter via `remark-frontmatter` | `yaml` node |
| Headings flat siblings | Yes (no section nodes) |
| Blockquote ⊃ list + table | Yes |
| Offset ≠ value length (blockquote) | Confirmed |

### 6.3 PROPOSED (not executed here)

- Full CommonMark HTML-equality suite against cmark output.
- Property-based tests (fast-check) over random GFM tables.
- Electron main-process integration harness.
- Dual-parser boundary agreement suite (remark vs Lezer) beyond the one critical table.

---

## 7. Recommended approach with risks and limitations

### 7.1 Recommended approach **[Recommendation]**

1. **Parser:** `unified().use(remarkParse).use(remarkGfm).use(remarkFrontmatter, ['yaml'])`.
2. **Adapter:** map mdast → approved Field/document model; isolate third-party types; attach `position` + selective raw slices (especially `table` / `tableRow`).
3. **Tables:** build Table Fields from cells **and** retain row source text; adapter pads missing cells if the domain requires fixed arity; define excess-cell policy **[Open]**.
4. **Unknown syntax:** leave as text/html/blockquote; preserve via source slices.
5. **Testing (early):** fixture corpus including the Lothar/Veteran case; omitted vs empty; escaped pipes; nested list+table in blockquote; CRLF; BOM; position-slice invariants (`slice` round-trips for chosen node types); spec JSON subset in CI.
6. **Do not** implement production reader in this assignment; do not redefine Fields; do not touch mahogany repo.

### 7.2 Risks and limitations

| Risk | Why it matters | Mitigation |
|---|---|---|
| Excess cells kept in AST but dropped by HTML/markdown-it | Dual-parser or preview disagreement | Single semantic parser; document behavior; tests |
| Missing cells not padded in AST | Fixed-column Fields need adapter padding | Explicit pad in adapter; test |
| Position span ≠ `value` (blockquotes) | Naïve splice corrupts markers | Slice carefully; test caveat |
| ESM-only | Electron/Vitest misconfig | Verify imports in app scaffold early |
| remark core packages churn slowly; micromark still active | Supply-chain / upgrade discipline | Pin versions; periodic `npm outdated` |
| BOM / CRLF | Offset surprises | Normalize or document; fixtures |
| Assuming parse ⇒ lossless | Silent data loss on later stringify | Read-only Phase 0; splice later |
| Section hierarchy not in AST | Recursive docs need derived view | Derive in adapter; don’t persist as truth (005) |

### 7.3 One-line recommendation

**Use remark-parse + remark-gfm (+ remark-frontmatter) with a source-offset-preserving adapter; recover irregular table rows via `tableRow` source slices because `Veteran`-class excess cells survive in mdast (unlike markdown-it / GFM HTML).**

---

## 8. Sources and package versions investigated

*Accessed 2026-10-15 unless noted.*

### Specs and primary docs

1. CommonMark 0.31.2 — <https://spec.commonmark.org/0.31.2/> and `spec.json`
2. GFM 0.29-gfm — <https://github.github.com/gfm/> (tables §4.10; task lists §5.3)
3. micromark README (100% CommonMark / GFM claims) — <https://github.com/micromark/micromark>
4. remark-gfm — <https://github.com/remarkjs/remark-gfm>
5. mdast — <https://github.com/syntax-tree/mdast>
6. mdast-util-from-markdown issue #48 (position vs value in blockquotes) — <https://github.com/syntax-tree/mdast-util-from-markdown/issues/48>
7. Assignment 005 — `/workspace/005-mahogany-markdown-structured-document-architecture.md` (architecture context; not re-deciding dialect)

### npm packages (installed versions in §2.1)

Exact tree recorded in `/workspace/poc-006/versions.json` and `npm ls` from 2026-10-15.

### Unverified / out of scope

- Full HTML-equality CommonMark suite in Mahogany CI
- Obsidian-specific callout plugin parse trees
- Production Electron packaging matrix
- Whether Mahogany’s approved eight Field types already include a Table Field shape sufficient for excess-cell metadata (**[Open]** — do not redefine here)

---

*End of Assignment 006 — Mahogany Markdown Parser Technology*
