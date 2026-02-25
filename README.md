# 🤖 Ollama Chatbot

A simple local AI chatbot built with **Streamlit** and **Ollama**, running the **LLaMA 3** model entirely on your machine — no API keys, no internet required.

---

## Features

- Chat with LLaMA 3 locally via Ollama
- Maintains full conversation history for context-aware replies
- Clean, minimal UI powered by Streamlit

---

## Prerequisites

- Python 3.8+
- [Ollama](https://ollama.com) installed and running on your machine
- LLaMA 3 model pulled via Ollama

---

## Setup

**1. Install Ollama**

Download and install Ollama from [https://ollama.com](https://ollama.com), then pull the LLaMA 3 model:

```bash
ollama pull llama3
```

**2. Clone or download this project**

```bash
git clone <your-repo-url>
cd <your-repo-folder>
```

**3. Install Python dependencies**

```bash
pip install -r requirements.txt
```

**4. Run the app**

```bash
streamlit run app.py
```

The app will open in your browser at `http://localhost:8501`.

---

## How It Works

- `st.session_state.messages` stores the full conversation history so the model has context for each reply.
- Each message is tagged with a role — either `user` or `assistant`.
- `ollama.chat()` sends the entire conversation history to LLaMA 3 and returns a response.

---

## Project Structure

```
├── app.py            # Main chatbot application
├── requirements.txt  # Python dependencies
└── README.md         # This file
```

---

## Troubleshooting

- **Ollama not running:** Make sure the Ollama desktop app is open or run `ollama serve` in your terminal before starting the chatbot.
- **Model not found:** Run `ollama pull llama3` to download the model first.
- **Slow responses:** LLaMA 3 runs locally — response speed depends on your hardware.
