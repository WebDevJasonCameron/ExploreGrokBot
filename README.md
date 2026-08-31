# ExploreGrokBot

A minimal web chat app for exploring ideas with xAI's **Grok** model. It ships
with a clean Flask backend, a modern single-page chat UI, and an offline mock
mode so you can run it end-to-end without any API key.

## Features

- 💬 Simple, responsive web chat UI
- 🔌 Talks to the xAI Grok API (OpenAI-compatible `/chat/completions`)
- 🧪 Offline **mock mode** when no `XAI_API_KEY` is set — great for local dev/CI
- 🩺 `/api/health` endpoint reporting the active mode and model

## Requirements

- Python 3.12+

## Setup

```bash
python3 -m venv .venv
.venv/bin/pip install -r requirements.txt
```

## Configuration

Copy `.env.example` to `.env` and set your key to enable live Grok responses:

```bash
cp .env.example .env
# edit .env and set XAI_API_KEY=...
```

| Variable       | Default                 | Description                              |
| -------------- | ----------------------- | ---------------------------------------- |
| `XAI_API_KEY`  | _(unset)_               | xAI API key. If empty, runs in mock mode |
| `XAI_MODEL`    | `grok-2-latest`         | Model name                               |
| `XAI_API_BASE` | `https://api.x.ai/v1`   | API base URL                             |
| `PORT`         | `5000`                  | Port for the web server                  |

## Run

```bash
.venv/bin/python app.py
```

Then open http://localhost:5000 and start chatting.

## API

```bash
# Health
curl http://localhost:5000/api/health

# Chat
curl -X POST http://localhost:5000/api/chat \
  -H 'Content-Type: application/json' \
  -d '{"message": "Hello Grok!"}'
```

## Cloud Agent environment

This repo includes `.cursor/environment.json`, which installs dependencies into
a `.venv` and runs the web server on port 5000 in the `web` terminal.
