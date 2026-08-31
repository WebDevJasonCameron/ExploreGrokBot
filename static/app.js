const chat = document.getElementById("chat");
const form = document.getElementById("composer");
const input = document.getElementById("input");
const sendBtn = document.getElementById("send");

const history = [];

function addMessage(role, text, opts = {}) {
  const msg = document.createElement("div");
  msg.className = `msg ${role === "user" ? "user" : "bot"}`;
  const bubble = document.createElement("div");
  bubble.className = "bubble" + (opts.typing ? " typing" : "");
  bubble.textContent = text;
  msg.appendChild(bubble);
  chat.appendChild(msg);
  chat.scrollTop = chat.scrollHeight;
  return bubble;
}

form.addEventListener("submit", async (e) => {
  e.preventDefault();
  const text = input.value.trim();
  if (!text) return;

  addMessage("user", text);
  history.push({ role: "user", content: text });
  input.value = "";
  input.focus();
  sendBtn.disabled = true;

  const typing = addMessage("bot", "ExploreGrokBot is thinking…", { typing: true });

  try {
    const res = await fetch("/api/chat", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ messages: history }),
    });
    const data = await res.json();
    if (!res.ok) throw new Error(data.error || `HTTP ${res.status}`);

    typing.classList.remove("typing");
    typing.textContent = data.reply;
    history.push({ role: "assistant", content: data.reply });
  } catch (err) {
    typing.classList.remove("typing");
    typing.textContent = `⚠️ ${err.message}`;
  } finally {
    sendBtn.disabled = false;
  }
});
