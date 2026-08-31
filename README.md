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
│   ├── reports/
│   └── opportunities/
└── decisions/
    └── decision-log.md
```

## How to use

1. Keep `company/mission.md`, `company/opportunity-criteria.md`, and `company/owner-context.md` current. Agents may use only documented Owner Fit facts; undocumented items are unknown.
2. Point an agent at `agents/market-research-analyst/` and have it follow `instructions.md`.
3. File finished write-ups under `research/reports/`.
4. File scored opportunities under `research/opportunities/`.
5. Record go / no-go / defer choices in `decisions/decision-log.md`.
6. Capture reusable mistakes and wins in `agents/market-research-analyst/lessons-learned.md`.

## Naming

- Reports: `YYYY-MM-DD-<topic-slug>.md`
- Opportunities: `YYYY-MM-DD-<opportunity-slug>.md`
