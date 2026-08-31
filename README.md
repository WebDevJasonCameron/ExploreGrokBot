# ExploreGrokBot

File-based operating environment for exploring markets and logging opportunities. Company intent lives in `company/`. Agent behavior lives in `agents/`. Research output lands in `research/`. Choices are recorded in `decisions/`.

## Layout

```
ExploreGrokBot/
├── README.md
├── company/
│   ├── mission.md
│   ├── opportunity-criteria.md
│   └── owner-context.md
├── agents/
│   └── market-research-analyst/
│       ├── role.md
│       ├── instructions.md
│       └── lessons-learned.md
├── research/
│   ├── assignments/
│   ├── reports/
│   └── opportunities/
└── decisions/
    └── decision-log.md
```

## How to use

1. Keep `company/mission.md`, `company/opportunity-criteria.md`, and `company/owner-context.md` current. Agents may use only documented Owner Fit facts; undocumented items are unknown.
2. Point an agent at `agents/market-research-analyst/` and have it follow `instructions.md`.
3. File research assignments (problem discovery and similar investigations) under `research/assignments/`.
4. File other finished write-ups under `research/reports/` when they are not numbered assignments.
5. File scored opportunities under `research/opportunities/`.
6. Record go / no-go / defer choices in `decisions/decision-log.md`.
7. Capture reusable mistakes and wins in `agents/market-research-analyst/lessons-learned.md`.

## Naming

- Assignments: `NNN-<topic-slug>.md` (example: `001-ttrpg-problem-discovery.md`)
- Reports: `YYYY-MM-DD-<topic-slug>.md`
- Opportunities: `YYYY-MM-DD-<opportunity-slug>.md`
