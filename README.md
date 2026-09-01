<div align="center">

<img src="assets/sambanova_logo.png" alt="SambaNova" width="300">

# Deep Agents from Scratch

### A Hands-On Webinar Series

**Data Science Dojo** x **SambaNova**

[![Python 3.11+](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/downloads/)
[![LangGraph](https://img.shields.io/badge/LangGraph-0.6+-green.svg)](https://github.com/langchain-ai/langgraph)
[![SambaNova](https://img.shields.io/badge/SambaNova-MiniMax--M2.7-purple.svg)](https://cloud.sambanova.ai/)

Build production-ready AI agents from the ground up using LangGraph and SambaNova Cloud.

</div>

---

## About This Series

**Deep Agents from Scratch** is a 6-session webinar series by Data Science Dojo and SambaNova that teaches you to build sophisticated AI agents step by step — from a simple ReAct loop to a full agent system with memory, tools, evaluation, and more.

| Session | Topic | Notebook | Recording | Date |
|---------|-------|----------|-----------|------|
| 1 | The Rise of the Deep Agent | [`session_1/0_create_agent.ipynb`](notebooks/session_1/0_create_agent.ipynb) | [Watch](https://www.youtube.com/watch?v=H_h9kmKAcJc) | Mar 4, 2026 |
| 2 | Agent Architecture Deep Dive | [`session_2/1_build_first_agent.ipynb`](notebooks/session_2/1_build_first_agent.ipynb) | [Watch](https://www.youtube.com/watch?v=ZxOkyYz95s4) | Mar 25, 2026 |
| 3 | Memory & Context Management | [`session_3/1_context_engineering.ipynb`](notebooks/session_3/1_context_engineering.ipynb) | [Watch](https://www.youtube.com/watch?v=MF8Qf0VmzIE) | Apr 15, 2026 |
| 4 | Agent Skills & MCP | [`session_4/1_agent_skills.ipynb`](notebooks/session_4/1_agent_skills.ipynb) | [Watch](https://www.youtube.com/watch?v=vYFX7JhOJgw) | May 13, 2026 |
| 5 | Multi-Agent Workflows | [`session_5/1_multi_agent_workflows.ipynb`](notebooks/session_5/1_multi_agent_workflows.ipynb) | [Watch](https://www.youtube.com/watch?v=VN0OEC3jNrs) | June 10, 2026 |
| 6 | Evaluation & Production | [`session_6/1_evaluation_production.ipynb`](notebooks/session_6/1_evaluation_production.ipynb) | TBD | July 1, 2026 |

---

## Season 2 — Coding Agents That Improve

*Build, evaluate, and self-improve coding agents on SambaNova.* A second 6-part series, presented by
**Varun Krishna** and **Kwasi Ankomah**, on the architecture behind every modern coding agent: a
frontier model **plans**, and a fast SambaNova model **executes** the dozens of edits and test runs
— then how to make the whole thing measurably better from its own traces.

| Session | Topic | Notebook | Recording | Date |
|---------|-------|----------|-----------|------|
| 1 | The Coding-Agent Harness | TBD | TBD | TBD |
| 2 | Scaling the Executors | [`season_2/session_2/1_scaling_executors.ipynb`](notebooks/season_2/session_2/1_scaling_executors.ipynb) | TBD | Sep 2, 2026 |
| 3 | Giving the Agent an Environment | TBD | TBD | TBD |
| 4 | Evaluating Coding Agents | TBD | TBD | TBD |
| 5 | Improving Your Agent From Its Traces | TBD | TBD | TBD |
| 6 | Closing the Loop in Production + Capstone | TBD | TBD | TBD |

### Session 2 — Scaling the Executors

Almost everything written about coding agents assumes **one developer, one agent, one laptop**. The
moment you run N candidates for one task, or a team's worth of agents at once, you are operating a
multi-tenant, inference-bound system. This notebook measures that shift end to end:

1. **The latency budget** — where an agent's wall-clock actually goes (TTFT, tok/s, turns).
2. **Concurrency** — fan out to N executors and see wall-clock track `max`, not `sum`.
3. **Best-of-N** — N candidate patches, with the **pytest suite** as the selector, and `pass@k`.
4. **The economics** — the real cost model, priced from the live model registry.

Everything runs against SambaNova Cloud on a free-tier key, and **every number is measured at run
time** — nothing is hard-coded. Expect the figures to differ from the committed outputs; `pass@1`
is a distribution, not a constant.

Only `SAMBANOVA_API_KEY` is required for this notebook.

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
    │
    ├── session_1/          # Season 1 — The Rise of the Deep Agent
    ├── session_2/          # Season 1 — Agent Architecture Deep Dive
    ├── session_3/          # Season 1 — Memory & Context Management
    ├── session_4/          # Season 1 — Agent Skills & MCP
    ├── session_5/          # Season 1 — Multi-Agent Workflows
    ├── session_6/          # Season 1 — Evaluation & Production
    │
    └── season_2/           # Season 2 — Coding Agents That Improve
        └── session_2/      # Scaling the Executors
            └── 1_scaling_executors.ipynb
```

---

## License

This project is provided for educational purposes as part of the Data Science Dojo x SambaNova webinar series.
