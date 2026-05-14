"""Minimal stdio MCP server for the Session 4 demo.

Exposes two business-relevant tools so the agent has something concrete to call
through the MCP protocol. Run via:

    python mcp_demo_server.py        # stdio (the notebook launches it this way)
"""

from datetime import date

from mcp.server.fastmcp import FastMCP

mcp = FastMCP("session4-demo")


@mcp.tool()
def get_team_oncall(date_iso: str | None = None) -> dict:
    """Return who's on call for a given date (YYYY-MM-DD). Defaults to today.

    Returns the primary and secondary on-call engineers plus their pager handles.
    """
    rota = {
        "2026-05-12": {"primary": "Asha P.", "secondary": "Marco L.", "pager": "+1-415-555-0142"},
        "2026-05-13": {"primary": "Jordan W.", "secondary": "Priya S.", "pager": "+1-415-555-0143"},
        "2026-05-14": {"primary": "Mei C.", "secondary": "Tomás R.", "pager": "+1-415-555-0144"},
    }
    d = date_iso or date.today().isoformat()
    return {"date": d, **rota.get(d, {"primary": "TBD", "secondary": "TBD", "pager": "-"})}


@mcp.tool()
def get_company_metrics(quarter: str = "Q1-2026") -> dict:
    """Return high-level company metrics for a given quarter.

    Returns ARR, customer count, NPS, and uptime SLA for the requested quarter.
    """
    snapshots = {
        "Q4-2025": {"arr_usd": 18_200_000, "customers": 412, "nps": 47, "uptime_pct": 99.91},
        "Q1-2026": {"arr_usd": 21_700_000, "customers": 468, "nps": 51, "uptime_pct": 99.94},
    }
    return {"quarter": quarter, **snapshots.get(quarter, {"error": "unknown quarter"})}


if __name__ == "__main__":
    mcp.run(transport="stdio")
