# Lessons learned

Append-only. Newest entry at the top. Record only things that should change future research.

## Template

```markdown
### YYYY-MM-DD — <short title>
- Context:
- What happened:
- Lesson:
- Change to process:
```

## Entries

### 2026-08-31 — File research assignments under research/assignments/
- Context: Owner asked that assignment 001 and all following research assignments live in `research/assignments/`.
- What happened: Moved `001-ttrpg-problem-discovery.md` from `research/reports/` to `research/assignments/` and documented the location in README.
- Lesson: Numbered research assignments belong in `research/assignments/`, not `research/reports/`.
- Change to process: Create future assignment write-ups at `research/assignments/NNN-<topic-slug>.md`.

### 2026-08-31 — Problem-discovery assignment 001
- Context: First assigned TTRPG problem-discovery report.
- What happened: Assignment paths were written as `/company/...` and `/research/reports/...`. In this environment those files live under the repository root (`/workspace/company/...`). Several vendor blogs cited unverifiable “surveys.” Some official pricing pages were Cloudflare-blocked.
- Lesson: Treat assignment paths as repository-relative. Do not use product-blog statistics as facts unless a primary source is locatable. Record when a primary page cannot be fetched.
- Change to process: Label vendor claims explicitly. Prefer Sly Flourish, official pricing/help pages, earnings commentary, and practitioner Q&A over tool-comparison blogs.

### 2026-08-31 — Report filename conventions
- Context: Assignment required `001-ttrpg-problem-discovery.md`. README naming convention is `YYYY-MM-DD-<topic-slug>.md`.
- What happened: Followed the assignment filename.
- Lesson: A specific assignment filename overrides the README convention. Note the conflict for the Owner.
- Change to process: If both conventions appear, use the assignment name and record the conflict in the completion summary.
