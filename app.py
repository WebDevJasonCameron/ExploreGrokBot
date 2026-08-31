"""ExploreGrokBot — a minimal Flask web chat UI backed by the xAI Grok API.

Run with:  python app.py
Then open http://localhost:5000
"""

from __future__ import annotations

import os

from dotenv import load_dotenv
from flask import Flask, jsonify, render_template, request

import grok_client

load_dotenv()

app = Flask(__name__)

SYSTEM_PROMPT = {
    "role": "system",
    "content": (
        "You are ExploreGrokBot, a helpful and witty assistant that helps "
        "people explore ideas. Keep answers concise."
    ),
}


@app.get("/")
def index():
    return render_template("index.html", live=grok_client.is_live())


@app.get("/api/health")
def health():
    return jsonify(
        {
            "status": "ok",
            "mode": "live" if grok_client.is_live() else "mock",
            "model": grok_client.XAI_MODEL if grok_client.is_live() else "mock",
        }
    )


@app.post("/api/chat")
def chat():
    body = request.get_json(silent=True) or {}
    history = body.get("messages")

    if isinstance(history, list) and history:
        messages = [SYSTEM_PROMPT] + [
            {"role": m.get("role", "user"), "content": str(m.get("content", ""))}
            for m in history
        ]
    else:
        message = str(body.get("message", "")).strip()
        if not message:
            return jsonify({"error": "message is required"}), 400
        messages = [SYSTEM_PROMPT, {"role": "user", "content": message}]

    try:
        result = grok_client.chat(messages)
    except grok_client.GrokError as exc:
        return jsonify({"error": str(exc)}), 502

    return jsonify(result)


if __name__ == "__main__":
    port = int(os.environ.get("PORT", "5000"))
    app.run(host="0.0.0.0", port=port, debug=True)
