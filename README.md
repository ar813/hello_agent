# HelloAgent

**HelloAgent** is a simple AI assistant powered by Google's Gemini model. This project demonstrates how to integrate and run an agent using the `openai_agents` package in a UV (Agentic AI) environment.

---

## 🚀 Project Setup

Follow these steps to set up and run this project:

### 1. Initialize a New UV Project

```bash
uv init .
```

This will create a basic project structure.

### 2. Create a Virtual Environment

```bash
uv venv
```

This initializes a new Python virtual environment using UV.

### 3. Activate the Virtual Environment (Windows)

```bash
.venv\Scripts\activate
```

### 4. Add Dependencies

Install the OpenAI Agents library:

```bash
uv add openai_agents
```

Install `python-dotenv` for environment variable support:

```bash
uv add python-dotenv
```

---

## 🧠 Gemini API Key Setup

1. Get your Gemini API key from:

   * 🌐 [https://aistudio.google.com/apikey](https://aistudio.google.com/apikey)

2. Create a `.env` file in the root of your project directory with the following content:

```env
GEMINI_API_KEY=your_actual_gemini_api_key_here
```

⚠️ **Make sure not to share your API key publicly!**

---

## 🧩 Summary

* Project name: **HelloAgent**
* Uses UV environment and `openai_agents`
* Integrates Google Gemini via OpenAI-compatible API
* API key loaded securely from `.env`
* Simple, extendable assistant agent

---

Happy Coding! 🎉
