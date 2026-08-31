"""Client for the xAI Grok chat API with an offline mock fallback.

When ``XAI_API_KEY`` is set the client talks to the real xAI Grok API
(OpenAI-compatible ``/chat/completions`` endpoint). When no key is present it
returns a deterministic offline mock reply so the app can run end-to-end in
development and CI without any secret.
"""

from __future__ import annotations

import os
from typing import List, Dict

import requests

XAI_API_BASE = os.environ.get("XAI_API_BASE", "https://api.x.ai/v1")
XAI_MODEL = os.environ.get("XAI_MODEL", "grok-2-latest")
REQUEST_TIMEOUT_SECONDS = float(os.environ.get("XAI_TIMEOUT", "30"))


class GrokError(RuntimeError):
    """Raised when the upstream Grok API returns an error."""


def is_live() -> bool:
    """Return True when a real API key is configured."""
    return bool(os.environ.get("XAI_API_KEY", "").strip())


def _mock_reply(messages: List[Dict[str, str]]) -> str:
    last_user = next(
        (m["content"] for m in reversed(messages) if m.get("role") == "user"),
        "",
    )
    return (
        "[offline mock] ExploreGrokBot received: "
        f"\u201c{last_user}\u201d. "
        "Set the XAI_API_KEY secret to get real Grok responses."
    )


def chat(messages: List[Dict[str, str]]) -> Dict[str, object]:
    """Return a reply for the given chat messages.

    ``messages`` is a list of ``{"role": ..., "content": ...}`` dicts. The
    return value is ``{"reply": str, "mode": "live" | "mock", "model": str}``.
    """
    if not is_live():
        return {"reply": _mock_reply(messages), "mode": "mock", "model": "mock"}

    headers = {
        "Authorization": f"Bearer {os.environ['XAI_API_KEY'].strip()}",
        "Content-Type": "application/json",
    }
    payload = {"model": XAI_MODEL, "messages": messages, "stream": False}

    try:
        resp = requests.post(
            f"{XAI_API_BASE}/chat/completions",
            headers=headers,
            json=payload,
            timeout=REQUEST_TIMEOUT_SECONDS,
        )
    except requests.RequestException as exc:  # network / timeout
        raise GrokError(f"Failed to reach xAI API: {exc}") from exc

    if resp.status_code != 200:
        raise GrokError(f"xAI API returned {resp.status_code}: {resp.text[:500]}")

    data = resp.json()
    try:
        reply = data["choices"][0]["message"]["content"]
    except (KeyError, IndexError, TypeError) as exc:
        raise GrokError(f"Unexpected xAI API response shape: {data}") from exc

    return {"reply": reply, "mode": "live", "model": XAI_MODEL}
