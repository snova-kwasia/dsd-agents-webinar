<div align="center">

<img src="assets/sambanova_logo.png" alt="SambaNova" width="300">

# Deep Agents from Scratch

### A Hands-On Webinar Series

**Data Science Dojo** x **SambaNova**

[![Python 3.11+](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/downloads/)
[![LangGraph](https://img.shields.io/badge/LangGraph-0.6+-green.svg)](https://github.com/langchain-ai/langgraph)
[![SambaNova](https://img.shields.io/badge/SambaNova-MiniMax--M2.5-purple.svg)](https://cloud.sambanova.ai/)

Build production-ready AI agents from the ground up using LangGraph and SambaNova Cloud.

</div>

---

## About This Series

**Deep Agents from Scratch** is a 6-session webinar series by Data Science Dojo and SambaNova that teaches you to build sophisticated AI agents step by step — from a simple ReAct loop to a full agent system with memory, tools, evaluation, and more.

| Session | Topic | Notebook | Recording | Date |
|---------|-------|----------|-----------|------|
| 1 | The Rise of the Deep Agent | `session_1/0_create_agent.ipynb` | [Watch](https://youtube.com/) | Jan 15, 2025 |
| 2 | Agent Architecture Deep Dive | `session_2/1_build_first_agent.ipynb` | [Watch](https://youtube.com/) | Jan 22, 2025 |
| 3 | Memory & Context Management | Coming soon | TBA | Jan 29, 2025 |
| 4 | Tools & Agent Skills | Coming soon | TBA | Feb 5, 2025 |
| 5 | Multi-Agent Systems | Coming soon | TBA | Feb 12, 2025 |
| 6 | Evaluation & Production | Coming soon | TBA | Feb 19, 2025 |

---

## Quick Start

### Prerequisites

- Python 3.11 or higher
- [uv](https://docs.astral.sh/uv/getting-started/installation/) (recommended package manager)
- A [SambaNova Cloud](https://cloud.sambanova.ai/) API key (free tier available)
- A [Tavily](https://tavily.com/) API key (free tier available)

### Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/snova-kwasia/dsd-agents-webinar.git
   cd dsd-deep-agents
   ```

2. **Install dependencies**
   ```bash
   uv sync
   ```

3. **Configure API keys**
   ```bash
   cp .env.example .env
   ```
   Open `.env` and fill in your API keys:
   ```
   SAMBANOVA_API_KEY=your_sambanova_api_key_here
   TAVILY_API_KEY=your_tavily_api_key_here
   ```

4. **Launch JupyterLab**
   ```bash
   uv run jupyter lab notebooks/
   ```

---

## Getting API Keys

### SambaNova Cloud

1. Go to [cloud.sambanova.ai](https://cloud.sambanova.ai/)
2. Sign up for a free account
3. Navigate to **API Keys** and create a new key
4. Copy the key into your `.env` file

### Tavily (Web Search)

1. Go to [tavily.com](https://tavily.com/)
2. Sign up for a free account
3. Copy your API key into your `.env` file

### Langfuse (Observability — Optional)

Langfuse lets you trace and inspect every LLM call and tool invocation. You can use [Langfuse Cloud](https://cloud.langfuse.com) or [self-host with Docker](https://langfuse.com/docs/deployment/self-host).

To self-host Langfuse locally:
```bash
# Clone and start Langfuse
git clone https://github.com/langfuse/langfuse.git
cd langfuse
docker compose up -d
```

### LangSmith (Observability — Optional)

[LangSmith](https://docs.smith.langchain.com/) is another observability option from the LangChain ecosystem. It provides tracing, debugging, and evaluation for your LLM applications.

To use LangSmith:
1. Go to [LangSmith](https://smith.langchain.com/)
2. Sign up for a free account
3. Create an API key
4. Copy the key into your `.env` file

---

## Project Structure

```
dsd-deep-agents/
├── README.md               # This file
├── pyproject.toml          # Python dependencies (uv)
├── .env.example            # API key template
├── assets/
│   └── sambanova_logo.png  # SambaNova branding
└── notebooks/
    ├── utils.py            # Display utilities for Rich formatting
    ├── session_1/          # The Rise of the Deep Agent
    │   └── 0_create_agent.ipynb
    ├── session_2/          # Coming soon
    ├── session_3/          # Coming soon
    ├── session_4/          # Coming soon
    ├── session_5/          # Coming soon
    └── session_6/          # Coming soon
```

---

## License

This project is provided for educational purposes as part of the Data Science Dojo x SambaNova webinar series.
