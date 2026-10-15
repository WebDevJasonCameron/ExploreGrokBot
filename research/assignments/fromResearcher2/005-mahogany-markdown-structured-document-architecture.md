# 005 — Mahogany Markdown & Structured Document Architecture

- **Researcher:** Researcher 2 (Market Research Analyst)
- **Owner:** Jason Cameron
- **Date:** 2026-10-12
- **Status:** Complete — awaiting Owner review
- **Filing path:** `research/assignments/fromResearcher2/005-mahogany-markdown-structured-document-architecture.md`
- **Roadmap support:** primary 0.1.6.1–0.1.6.4; secondary 0.1.6.5–0.1.6.6
- **Guiding principle:** Read Before Write
- No changes to mahogany repo.

> **Evidence labels.** **[Spec/Doc Fact]** = stated in a primary spec or official documentation. **[Common Practice]** = observed in widely used tools or communities. **[Recommendation]** = this researcher's advice. It is *not* an approved decision. **[Open Architectural Decision]** = a choice for the Owner/Architect. This report does **not** design Mahogany's Field model, Table model, or final architecture.

---

## 1. Executive summary

1. **[Spec/Doc Fact]** CommonMark 0.31.2 defines a strict, unambiguous core. GFM 0.29-gfm is a strict superset that adds exactly five extensions: tables, task list items, strikethrough, extended autolinks, and disallowed raw HTML (tagfilter). Front matter, footnotes, wikilinks, callouts, definition lists, math, and directives are **not** part of either spec.
2. **[Recommendation]** The portable baseline to read is **CommonMark + GFM + YAML front matter**. Footnotes are a low-risk "recognize and preserve" addition. Wikilinks, Obsidian callouts, math, and directives should be *recognized and preserved verbatim* when they appear, and not authored by Mahogany unless needed.
3. **[Common Practice]** Real TTRPG Markdown (Obsidian vaults, Homebrewery, GM Binder, Fantasy Statblocks) leans heavily on headings, bold "Label:" lines, bullet lists, GFM tables, blockquote callouts, and fenced code blocks that carry YAML (`statblock`). Much of what looks like structure, such as stat blocks rendered from code fences or Homebrewery `{{ }}` blocks, is renderer convention that Markdown itself does not encode.
4. **[Spec/Doc Fact]** Markdown headings are **flat siblings** in every major AST (mdast, markdown-it tokens, CommonMark AST). Any section hierarchy is *derived*, and the derivation is ambiguous when levels skip, repeat, or appear inside containers.
5. **[Spec/Doc Fact]** GFM tables are inline-only grids. They have one header row, a delimiter row with alignment, no multiline cells, no colspan or rowspan, and no captions. Missing cells are filled with empty cells and excess cells are ignored. The header row decides the column count. Everything TTRPG-semantic (dice ranges, progression levels, row labels) is **inference**.
6. **[Inference]** For TypeScript/Electron, **unified/remark (micromark + mdast + remark-gfm + remark-frontmatter)** is the strongest fit for the parse/read path. It is 100% CommonMark/GFM compliant per its docs, has positions on every node, ships typed ASTs (`@types/mdast`), and supports extensions. markdown-it is fast and mature, but its token stream is a weaker document model.
7. **[Spec/Doc Fact]** `remark-stringify` regenerates Markdown from the AST. It is **not lossless**: list markers, emphasis markers, escapes, table padding, and heading styles get normalized.
8. **[Recommendation]** Use the round-trip strategy "parse for understanding, splice for writing". Edits should replace only the source span of the changed node (using `position.start/end.offset`) and leave all other bytes untouched. Unknown nodes are kept as raw slices. Front matter edits go through the `yaml` package's `Document` API, which preserves comments and ordering.
9. **[Recommendation]** The adapter boundary (`parser AST → Mahogany adapter → Mahogany model`) is sound and should keep mdast types from leaking. The adapter should still keep a *reference* (source offsets) back to the originating span so that writes can be minimal.
10. **Key risks:** flat key/value assumptions, unstable node identity across re-parses, repeated or skipped headings, table semantics inferred wrongly, parser/serializer disagreement, and front matter edge cases (duplicate keys, YAML 1.1 vs 1.2 booleans, `---` inside the body).

---

## 2. Dialect comparison

### 2.1 Core specs

| Feature | CommonMark 0.31.2 | GFM 0.29-gfm | Notes |
|---|---|---|---|
| ATX / setext headings | Yes | Yes | Setext only allows levels 1–2 **[Spec/Doc Fact]** |
| Paragraphs, blockquotes, lists, code (indented/fenced), thematic breaks | Yes | Yes | |
| Raw HTML blocks (7 kinds) and inline HTML | Yes | Yes, with tagfilter | |
| Link reference definitions | Yes | Yes | Not rendered; they affect link resolution |
| Backslash escapes, entity refs | Yes | Yes | Any ASCII punctuation can be escaped |
| Tables | No | **Yes** (extension) | |
| Task list items `- [ ]` / `- [x]` | No | **Yes** | Only as the first content of a list item |
| Strikethrough `~~` | No | **Yes** | One or two tildes |
| Extended autolinks (`www.`, bare URLs) | No | **Yes** | |
| Disallowed raw HTML | No | **Yes** | Filters `title, textarea, style, xmp, iframe, noembed, noframes, script, plaintext` by replacing `<` with `&lt;` at render time |
| Footnotes | No | Not in spec; GitHub renders them | remark-gfm supports them |
| Front matter | No | No | De facto YAML between `---` lines (Jekyll/Hugo/Obsidian) |

**[Spec/Doc Fact] Unknown syntax:** CommonMark has no "unknown syntax" error state. Every input is valid Markdown. Anything unrecognized becomes literal text, a paragraph, or HTML. So `[[Wiki Link]]` parses as the text `[[Wiki Link]]` (possibly a shortcut reference attempt), `> [!note]` parses as a blockquote whose paragraph begins with `[!note]`, and `$x$` stays text. **[Inference]** This is good for "Read Before Write". Nothing is lost at parse time, but the *meaning* is lost unless an extension recognizes it.

**[Spec/Doc Fact] Raw HTML:** CommonMark passes HTML through. GFM's tagfilter is a *render-time* safety measure, not a parse-time one. **[Recommendation]** In Electron, never render raw HTML unsanitized. Use rehype-sanitize or DOMPurify and keep `contextIsolation`. HTML should be preserved in files but treated as opaque.

### 2.2 Common extensions (non-standard)

| Extension | Syntax | Where | Portability | Suggested stance **[Recommendation]** |
|---|---|---|---|---|
| YAML front matter | `---\n…\n---` at the start of the file | Jekyll, Hugo, Obsidian, Astro | Very high (by convention) | **Support** (already authoritative in Mahogany) |
| Footnotes | `[^1]` / `[^1]: text` | GitHub, Pandoc, Obsidian, PHP Markdown Extra | High | Read and preserve |
| Wikilinks | `[[Page]]`, `[[Page\|alias]]`, `[[Page#Heading]]` | Obsidian, Foam, Logseq, MediaWiki | Medium (unreadable on GitHub) | Recognize and preserve; Owner decides whether to author them |
| Callouts | `> [!note] Title` (Obsidian); `> [!NOTE]` (GitHub alerts, 5 types) | Obsidian, GitHub | Medium; degrades to a blockquote | Recognize as a blockquote subtype and preserve |
| Definition lists | `Term\n: definition` | Pandoc, PHP Markdown Extra | Low | Preserve as text; don't author |
| Math | `$…$`, `$$…$$` | Pandoc, Obsidian, GitHub | Medium | Preserve; low TTRPG value |
| Directives | `:name[…]{…}`, `::name`, `:::name` (generic directives proposal) | remark-directive, MyST/Docusaurus admonitions | Low | Avoid authoring; preserve |
| Homebrewery `{{ }}` blocks / `\page` | `{{monster,frame … }}` | Homebrewery, GM Binder | Very low | Preserve as opaque text |

**[Spec/Doc Fact]** GitHub alerts officially support `NOTE, TIP, IMPORTANT, WARNING, CAUTION`. Obsidian supports these and more (`abstract, info, todo, success, question, failure, danger, bug, example, quote`), plus folding with `[!note]-`/`+`.

**Plain-editor usefulness [Inference]:** CommonMark + GFM + front matter reads cleanly in any text editor and renders on GitHub. Wikilinks and callouts still read acceptably as plain text. Directives and Homebrewery blocks read poorly.

**Baseline recommendation [Recommendation]:** *Read* CommonMark 0.31.2 + GFM (tables, task lists, strikethrough, autolinks) + YAML front matter + footnotes. *Recognize-and-preserve* wikilinks, Obsidian/GitHub callouts, and math. Treat everything else as opaque text that is preserved byte-for-byte. Mahogany should *write* only baseline constructs unless the Owner approves more. No custom syntax.

---

## 3. TTRPG Markdown findings

### 3.1 Observed patterns [Common Practice]

| Content | Typical Markdown pattern | Covered by GFM? |
|---|---|---|
| Character / NPC | Front matter (`type: npc`, `race`, `faction`, `tags`), H1 name, H2 sections (Appearance, Personality, Secrets), bold-label lines `**Alignment:** CN` | Yes; "labels" are inference |
| Location | H1 + description, H2 "Points of interest" with nested lists, links to NPCs | Yes (wikilinks are extension) |
| Item | Front matter or label lines (rarity, attunement), description paragraph | Yes |
| Stat block | (a) Obsidian Fantasy Statblocks: a ```` ```statblock ```` fence containing YAML; (b) Homebrewery `{{monster,frame` with `___` and `>` blockquote lines plus an ability-score table; (c) plain bold labels + 6-column ability table | Fence and table yes; *meaning* is renderer-defined |
| Spells | H3 per spell, italic school/level line, label lines (Casting Time, Range), paragraph | Yes |
| Classes / progression | A "Level \| Proficiency Bonus \| Features \| …" table | Yes (table) |
| Roll / random tables | `\| d6 \| Result \|`, `\| d100 \| … \|` with `01–05` ranges | Yes; ranges are text |
| Encounter tables | Range + creature + count (`1d4+1 goblins`) | Yes; dice expressions are text |
| Equipment | Name \| Cost \| Weight \| Properties | Yes |
| Timelines | Ordered or bulleted lists with dates, or headings per era, or tables | Yes |
| GM notes / secrets | Callouts `> [!secret]`, `%% comments %%` (Obsidian), HTML comments, separate files | Callouts and `%%` are extensions; HTML comments are standard |
| Links | Wikilinks in Obsidian, relative `.md` links elsewhere | Relative links yes |
| Queries | Dataview `dataview` fences, inline `key:: value` fields | No (plugin-specific) |

### 3.2 Import implications [Inference]
- Plugin data lives *inside* standard containers. Fenced code with an info string (`statblock`, `dataview`, `dice`) is standard syntax. Its contents are opaque to a GFM parser but often contain YAML. **[Recommendation]** Preserve fences verbatim. Optionally expose "fenced block with language X" for future adapters.
- Bold-label lines (`**HP:** 45`) are *the* most common informal key/value pattern, but they are paragraphs with strong emphasis, not fields. Deriving fields from them is heuristic.
- Obsidian Dataview inline fields (`Key:: Value`) are a third key/value convention, alongside front matter and bold labels.
- Homebrewery/GM Binder content is effectively its own dialect (V3 `{{ }}`, `\page`, `\column`, CSS). Expect lossy *interpretation* but lossless *preservation*.

---

## 4. Parser comparison

| Parser | Compliance | AST | Tables / tasks | HTML | Extensibility | TS | Positions | Round-trip | Maturity (approx., verify before decision) |
|---|---|---|---|---|---|---|---|---|---|
| **micromark** + **mdast-util-from-markdown** (unified/remark core) | 100% CommonMark; GFM via `micromark-extension-gfm` **[Doc Fact]** | mdast (typed tree, documented spec) | Via remark-gfm: `table`, `tableRow`, `tableCell`, `align[]`; `listItem.checked` | `html` nodes (raw string) | Syntax extensions (micromark) + from/to-markdown utils; complex to write | Full (`@types/mdast`, written in JS with JSDoc types) | `position.start/end {line,column,offset}` on every node | `mdast-util-to-markdown` / `remark-stringify` normalizes | Active (verified 2026-10-12): micromark 4.0.3 published 2026-09-26; remark repo pushed 2026-09-27; remark 15.0.1 / remark-stringify 11.0.0 last published 2023-09 (stable core, little churn); remark-gfm 4.0.1 (2025-02); ESM-only |
| **remark-frontmatter** | — | `yaml`/`toml` nodes, raw value | — | — | — | Yes | Yes | Value preserved as string | Active |
| **markdown-it** | CommonMark (tracks spec, near-full) | Flat token stream with nesting; `map` = [startLine,endLine] for blocks only | Tables built in; tasks via plugin | `html_block`/`html_inline` | Large plugin ecosystem (footnote, container, deflist, front-matter) | `@types/markdown-it` (community) | Line-level only for blocks; no inline offsets | Renderer is HTML-focused; no official Markdown serializer | Mature; v15.0.2 published 2026-09-11 (verified) |
| **marked** | Targets CommonMark/GFM; README claims "all markdown features from the supported flavors" (no exact compliance % verified) | Lexer tokens with `raw` | Built in | Yes | Extensions API | Bundled TS | `raw` text but no offsets | Can concat `raw`; weak structure | Very active; v18.1.1 published 2026-10-12 (verified) |
| **commonmark.js** | Reference implementation | CommonMark AST | No GFM | Yes | Minimal | Community types | `sourcepos` | No | Reference impl.; npm `commonmark` 0.31.2 last published 2024-09 (verified) |
| **@lezer/markdown** (CodeMirror 6) | CommonMark + GFM extensions | Lossless-ish concrete syntax tree with node ranges over the source | GFM extension | Yes | Parser extensions | Native TS | Exact `from/to` offsets for all nodes incl. markers | Source is retained; tree is a view over text, ideal for editors | Active; v1.8.0 published 2026-10-07. **Note (verified):** the GitHub repo is archived and has moved to https://code.haverbeke.berlin/lezer/markdown |
| **tree-sitter-markdown** (`tree-sitter-grammars/tree-sitter-markdown`) | Split block/inline grammars; README says it targets CommonMark but is not recommended where correctness matters (verified) | CST | GFM pipe tables | Yes | Grammar forks | Bindings | Byte ranges | Incremental, lossless CST | Active; native/WASM build needed in Electron |
| **Pandoc** (external) | Own dialects, can read CommonMark/GFM | Pandoc AST with sections | Rich tables | Yes | Lua filters | No (Haskell binary) | Optional sourcepos | Normalizes heavily | Very mature; not embeddable in a TS app |

**[Inference] Fit for `Markdown → parser AST → Mahogany adapter → Mahogany model`:**
- **remark/mdast** is the best *read* model. It has a documented, typed tree, complete offsets, first-class GFM table/task nodes, front matter nodes, and many utilities (`unist-util-visit`, `mdast-util-heading-range`, `mdast-util-toc`). It runs in Electron main, renderer, or a worker, and is pure JS. The ESM-only packaging needs a modern Vite/Electron config (already standard).
- **@lezer/markdown** is the natural complement *if* the editor is CodeMirror 6. It keeps exact ranges, which helps with editor folding and highlighting. It is not a semantic document model.
- **markdown-it** is fine for rendering previews but weak as a source of truth for writes, because it lacks inline offsets.
- **[Recommendation]** One parser should be canonical for semantics, to avoid parser disagreement. If a second one is used for the editor, test fixtures should check that both agree on block boundaries.

---

## 5. AST findings

**[Spec/Doc Fact] mdast essentials:** `root` contains block content. Block nodes are `paragraph`, `heading{depth 1–6}`, `thematicBreak`, `blockquote`, `list{ordered,start,spread}`, `listItem{spread,checked}`, `code{lang,meta,value}`, `html`, `definition`, `footnoteDefinition`, `table{align}`, `tableRow`, `tableCell`, `yaml`. Inline (phrasing) nodes are `text`, `emphasis`, `strong`, `delete`, `inlineCode`, `break`, `link`, `image`, `linkReference`, `imageReference`, `footnoteReference`, `html`. Every node may carry `position`.
- **Lists:** `spread` encodes loose vs tight lists (blank lines between items). That is a formatting fact that affects rendering (`<p>` wrapping). Nested lists are `list` inside `listItem`, which gives real recursion.
- **Blockquotes** contain arbitrary blocks, including headings, lists, and tables. Callouts are therefore blockquotes with a first-line marker.
- **Code** keeps `lang` and `meta` (the info string) and the raw `value`, which is good for preserving plugin fences.
- **Positions** are 1-based line/column plus 0-based `offset`. Nodes created by transforms have no position.
- Not in the AST: marker choices (`*` vs `-`), ATX closing hashes, setext vs ATX (inferable only from source), table padding, escape choices, and the exact whitespace.

### 5.1 Sequential headings vs derived section hierarchy (dedicated)

- **[Spec/Doc Fact]** CommonMark/mdast represent headings as **siblings** of the content that "belongs" to them. No spec defines sections.
- **[Spec/Doc Fact]** `mdast-util-heading-range` finds a heading by text/test and returns the nodes up to the next heading of the **same or lower depth** (the conventional rule). `mdast-util-toc` builds a nested list from heading depths. `remark-sectionize` (community) wraps headings and their following content into `section` nodes. Pandoc's `--section-divs` / `Ext_section_divs` and its `makeSections` do the same, nesting by level.
- **[Spec/Doc Fact]** The HTML5 "outline algorithm" (sectioning-element nesting) was **replaced in the HTML spec on 2022-07-01 by one based purely on heading levels** (whatwg/html PR #7829), largely because browsers and assistive tech never implemented the old one. That is a cautionary precedent: derived outlines are a tool convention, not a document fact.
- **[Common Practice]** Obsidian's Outline pane and CodeMirror 6 heading folding (`foldService` over the Lezer tree) both derive "the range until the next heading of ≤ depth". On a skip (H1 → H3), the H3 nests under the H1. Headings inside blockquotes or lists are generally *not* sections.
- **[Inference] Ambiguities Mahogany must decide:** heading-level skips; content before the first heading (a preamble); duplicate heading text at the same level (non-unique anchors, which GitHub disambiguates with `-1`, `-2` slugs); headings inside containers; thematic breaks used as section separators; and setext vs ATX parity.
- **[Recommendation]** Store headings as the AST gives them (sequential). Compute section hierarchy as a **derived, recomputable view** with a documented rule ("until next heading of depth ≤ n, top-level only"). Never persist the derived tree as truth.

---

## 6. Table findings

**[Spec/Doc Fact] GFM table rules (spec §4.10):**
- A header row is followed by a delimiter row (`---`, `:--`, `--:`, `:-:`). The **header and delimiter cell counts must match**, or there is no table.
- Leading and trailing pipes are optional. Cell content is trimmed.
- Body rows with **fewer cells get empty cells; extra cells are ignored** (dropped from the AST, so a naïve re-serialize *loses data*).
- A table ends at a blank line or at the start of another block.
- Cells hold **inline content only**: no lists, no block code, no multiple paragraphs. Line breaks need `<br>` (HTML).
- A literal pipe must be escaped as `\|`, **including inside code spans** (the table splits rows before inline parsing). This is a long-standing interoperability gotcha.
- There is no colspan/rowspan, caption, header column, or multi-row header. Exactly one header row is required (it may be empty-looking but must exist).
- Duplicate header texts are allowed. Headers are not keys.
- **[Doc Fact]** `mdast-util-gfm-table` serializes with aligned padding by default (`tablePipeAlign`, `tableCellPadding` options), so hand-formatted compact tables get reformatted.

**TTRPG patterns [Common Practice] vs what's encoded:**

| Pattern | Example | Encoded by Markdown | Inferred by readers |
|---|---|---|---|
| Die roll table | `\| d6 \| Result \|` rows `1`…`6` | Strings in cells | That col 1 is a die face; d6 from header |
| Range table | `01–05`, `96–00` | Strings (en dash vs hyphen varies) | Numeric ranges, `00` = 100, coverage/gaps |
| Progression | `Level \| Prof. Bonus \| Features \| Slots…` | Strings; alignment | Level is a row key; ordinal semantics |
| Equipment | `Name \| Cost \| Weight` | Strings | Units (gp, lb), currency |
| Stats | `STR \| DEX \| …` with `16 (+3)` | One row of strings | Score + modifier pairs |
| Row-label first column | `\| **Armor Class** \| 15 \|` | Strong emphasis in a cell | Transposed key/value table |
| Header-less key/value | Empty header row hack `\| \| \|` | Empty header cells | That header is meaningless |

**[Recommendation]** Read tables as (alignment[], header cells, rows of inline cells) plus source span, and nothing more at parse time. Treat roll-range, progression, and key/value interpretations as *optional, explicit, user-confirmed interpretations* layered on top. Never silently convert. Preserve ragged rows (extra cells) by keeping raw source when the counts differ. This report deliberately does not propose a Table model (0.1.6.4 is an Open Architectural Decision).

---

## 7. Round-trip findings

**Levels [Inference / terminology]:**
1. **Byte-level:** the identical file. Achievable only for unchanged regions (splicing).
2. **Formatting-level:** the same rendering *and* same markers/whitespace; differences are only where edited.
3. **Structural:** the same AST (mdast deep-equal minus positions). `remark-stringify` generally achieves this.
4. **Semantic:** the same meaning to Mahogany's model; the weakest guarantee.

**[Spec/Doc Fact] Normalization causes under AST → Markdown (remark-stringify defaults/options):** bullet marker (`bullet: '*'` default, verified; `-` common), `listItemIndent` (default `'one'`), ordered marker `.` vs `)`, `listItemIndent`, emphasis `*` vs `_` (`emphasis`, `strong` options), setext → ATX (`setext: false`), closing ATX hashes, fence char/length (`fence`, `fences`), indented code → fenced, thematic break style (`rule`), escaping (`unsafe` patterns add backslashes that weren't there), reference-style links (definitions are kept but may move; `[x][]` vs `[x]` forms), hard breaks (two trailing spaces vs `\`), blank-line counts collapse, table padding re-aligned, entities decoded (`&copy;` → `©`), trailing newline normalized, and front matter re-dumped if passed through a YAML stringifier (comments, quoting, and key order lost).

**Techniques:**
- **Source-span splicing [Recommendation]:** parse, locate the target node's `position.start.offset..end.offset`, generate *only* the replacement text, and splice into the original string. Untouched bytes survive. Re-parse afterwards to verify (Read Before Write *and* Read After Write).
- **Minimal edit granularity:** replace the smallest node (a cell, a list item, a paragraph) rather than a whole section.
- **CST vs AST:** Lezer and tree-sitter trees cover every byte (markers included), so they support exact edits. mdast drops markers but has offsets, which is enough for splicing.
- **Raw slices for unknown nodes:** for HTML, unrecognized fences, wikilink/callout text, and Homebrewery blocks, keep `source.slice(start,end)` and emit it verbatim.
- **Front matter:** use the **`yaml` (eemeli) `Document` API** (`parseDocument`, `doc.setIn`, `String(doc)`), which keeps comments, key order, and scalar styles. Avoid `js-yaml` load/dump for writes. The `yaml` package (v2.9.1, published 2026-09-11, verified) supports YAML 1.1 and 1.2 and preserves comments and blank lines per its README. Watch YAML 1.1 vs 1.2 (`yes`/`no`/`on` booleans, `010` octal) and duplicate keys.
- **Golden fixtures:** a corpus of foreign Markdown (Obsidian, GitHub, Homebrewery exports) with assertions that parse → no-op write is byte-identical.

---

## 8. Risks and edge cases

| Risk | Why it matters |
|---|---|
| Flat key/value assumption | TTRPG data is nested (stat blocks, attacks with sub-fields, tables in sections). A flat map loses structure or forces lossy flattening (0.1.6.2/0.1.6.3). |
| Node identity | mdast nodes have no IDs. Positions shift on every edit, and heading text can repeat. Without a stable anchor, edits can hit the wrong node. |
| Repeated headings | Two `## Attacks` headings break text-keyed lookup and slug anchors. |
| Heading skips / preamble | Derived hierarchy becomes ambiguous; different tools nest differently. |
| Deep nesting | Lists in blockquotes in list items; indentation rules (§5.2 list item width) make hand edits and serializer output differ. |
| Malformed Markdown | There's no error state, so a table whose delimiter count mismatches silently becomes a paragraph. The user sees "my table vanished". |
| Raw HTML | XSS in Electron if rendered; opaque to the model; `<br>` in cells. |
| Unknown extensions | Wikilinks, callouts, Dataview, and `%%` comments parse as plain text. Naïve re-serialization may escape `[[` to `\[\[` and corrupt them for Obsidian. |
| Normalization | Whole-file stringify rewrites user formatting, which leads to noisy git diffs, Obsidian users' distrust, and sync conflicts. |
| Positions | Offsets are in UTF-16 code units in JS strings; BOM, CRLF, and tab expansion (columns) can misalign splices. |
| Partial edits | External edits (another editor or sync) between read and write invalidate offsets. A content hash/mtime check is needed before splicing. |
| Parser/serializer disagreement | Output from stringify can parse to a different tree (edge cases with escapes, lists after paragraphs). Requires a re-parse check. |
| Parser disagreement across tools | Editor (Lezer) vs model (micromark) may see different block boundaries. |
| Extensibility | micromark extensions are low-level and hard to write. Committing to custom syntax creates long-term maintenance. |
| Front matter edge cases | Missing closing `---`, `---` thematic break at top, TOML `+++`, empty front matter, duplicate keys, non-object YAML, tabs, comments, multi-document YAML. |
| Extra table cells | Dropped by the parser, so data loss on rewrite. |

---

## 9. Recommendations (mapped to roadmap; not decisions)

- **0.1.6.1 Supported Markdown scope:** Declare tiers. Tier A (read and write): CommonMark 0.31.2 + GFM + YAML front matter. Tier B (read and preserve; author later only if approved): footnotes, wikilinks, callouts (GitHub/Obsidian), math. Tier C (opaque, preserve bytes): everything else (HTML, directives, Homebrewery blocks, plugin fences). Avoid custom syntax.
- **0.1.6.2 Field model:** Let fields be anchored to sources (front matter keys, heading sections, tables, fenced blocks) with a source span rather than a free-floating flat map. Distinguish *encoded* (front matter values) from *inferred* (bold labels) fields.
- **0.1.6.3 Recursive/container fields:** Mirror real Markdown recursion (sections → lists → nested lists; blockquote containers). Treat section hierarchy as a derived view with a documented rule.
- **0.1.6.4 Table semantics:** Read the GFM grid faithfully, including alignment and raw rows. Layer optional interpretations (roll, range, progression, key/value) that the user confirms. Keep ragged/extra cells preserved.
- **0.1.6.5 MD → Field parsing:** Use unified + remark-parse + remark-gfm + remark-frontmatter as a spike candidate. Keep the adapter as the only module that imports mdast types. Build a foreign-Markdown fixture corpus first.
- **0.1.6.6 Field → MD / round-trip:** Use span splicing + `yaml` Document API, with re-parse verification and a stale-file check before write. Use remark-stringify only for *newly created* content, with options fixed to the house style (e.g. `bullet: '-'`, `emphasis: '_'`, fenced code).

---

## 10. Open architect questions

1. Which tiers of syntax does Mahogany *author*, versus merely preserve? (Wikilinks especially.)
2. What is the canonical rule for derived sections (skips, preamble, headings in containers)?
3. How is node identity anchored across edits: heading slug + ordinal, front matter `id`, block IDs (`^block-id`, Obsidian style), or span + hash?
4. Are bold "Label: value" lines ever promoted to fields automatically, or only with user confirmation?
5. Which table interpretations ship first (roll/range, progression, key/value), and how are they declared (front matter hint vs UI)?
6. What's the acceptable round-trip guarantee for untouched regions? (Byte-level is recommended.)
7. Is a CodeMirror 6/Lezer editor planned? If so, how is agreement with the micromark model tested?
8. What is the policy for raw HTML rendering in Electron (sanitize, or show as source)?
9. What is the YAML policy: 1.2 core schema, duplicate key handling, comment preservation?
10. How does the app behave when a file changes on disk between read and write?

---

## 11. Sources

- CommonMark Spec 0.31.2 — https://spec.commonmark.org/0.31.2/ (accessed 2026-10-12)
- GitHub Flavored Markdown Spec — https://github.github.com/gfm/ (tables §4.10, task lists §5.3, strikethrough §6.5, autolinks §6.9, disallowed raw HTML §6.11) (accessed 2026-10-12)
- GitHub Docs, alerts and footnotes — https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax (accessed 2026-10-12)
- mdast specification — https://github.com/syntax-tree/mdast (accessed 2026-10-12)
- unist (positions) — https://github.com/syntax-tree/unist (accessed 2026-10-12)
- micromark — https://github.com/micromark/micromark (accessed 2026-10-12)
- remark — https://github.com/remarkjs/remark ; remark-gfm — https://github.com/remarkjs/remark-gfm ; remark-frontmatter — https://github.com/remarkjs/remark-frontmatter ; remark-stringify — https://github.com/remarkjs/remark/tree/main/packages/remark-stringify (accessed 2026-10-12)
- mdast-util-to-markdown (options) — https://github.com/syntax-tree/mdast-util-to-markdown (accessed 2026-10-12)
- mdast-util-gfm-table — https://github.com/syntax-tree/mdast-util-gfm-table (accessed 2026-10-12)
- mdast-util-heading-range — https://github.com/syntax-tree/mdast-util-heading-range ; mdast-util-toc — https://github.com/syntax-tree/mdast-util-toc (accessed 2026-10-12)
- remark-sectionize — https://github.com/jake-low/remark-sectionize (accessed 2026-10-12)
- remark-directive / generic directives proposal — https://github.com/remarkjs/remark-directive ; https://talk.commonmark.org/t/generic-directives-plugins-syntax/444 (accessed 2026-10-12)
- markdown-it — https://github.com/markdown-it/markdown-it (accessed 2026-10-12)
- marked — https://github.com/markedjs/marked (accessed 2026-10-12)
- commonmark.js — https://github.com/commonmark/commonmark.js (accessed 2026-10-12)
- @lezer/markdown — https://github.com/lezer-parser/markdown ; CodeMirror folding — https://codemirror.net/docs/ref/#language.foldService (accessed 2026-10-12)
- tree-sitter-markdown — https://github.com/tree-sitter-grammars/tree-sitter-markdown (accessed 2026-10-12)
- Pandoc manual (sections, extensions) — https://pandoc.org/MANUAL.html (accessed 2026-10-12)
- HTML outline algorithm removal — https://github.com/whatwg/html/pull/7829 (accessed 2026-10-12)
- yaml (eemeli) Document API — https://eemeli.org/yaml/ (accessed 2026-10-12)
- Obsidian Help: callouts, internal links, properties — https://help.obsidian.md/ (accessed 2026-10-12)
- Obsidian Fantasy Statblocks — https://github.com/javalent/fantasy-statblocks (accessed 2026-10-12)
- Dataview — https://blacksmithgu.github.io/obsidian-dataview/ (accessed 2026-10-12)
- Homebrewery — https://github.com/naturalcrit/homebrewery ; GM Binder — https://www.gmbinder.com/ (accessed 2026-10-12)
- Mahogany (read-only reference) — https://github.com/WebDevJasonCameron/mahogany (accessed 2026-10-12)

> **Verification note (2026-10-12):** All URLs above returned HTTP 200 on 2026-10-12. Verified against primary sources: the GFM spec's five extensions and section numbers; the table rules (header/delimiter count must match, missing cells padded, excess cells ignored, pipes must be escaped even inside code spans (spec example), block elements not allowed); the task-list marker rules; GitHub's five alert types; micromark's 100% CommonMark/GFM claim; mdast `spread`/`checked`; mdast-util-to-markdown defaults; mdast-util-gfm-table `tablePipeAlign`/`tableCellPadding` defaults (true); remark-gfm footnote support; the HTML outline PR; and npm release dates. **Not individually verified** (they remain working knowledge): Obsidian callout type list and fold syntax; Homebrewery/GM Binder syntax details; Dataview inline-field syntax; markdown-it `map` granularity; Pandoc section details; the remark-sectionize and mdast-util-heading-range behavior summaries; GitHub slug de-duplication; the CommonMark 0.31.2 HTML block count (the GFM spec text confirms seven kinds).

---

*End of Assignment 005 — Mahogany Markdown & Structured Document Architecture*
