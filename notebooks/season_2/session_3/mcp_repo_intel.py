"""A tiny MCP server exposing repo intelligence: issues and house rules."""
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("repo-intel")

@mcp.tool()
def changelog_policy() -> str:
    """Return this project's house rule for changelog entries."""
    return ("House rule: every behaviour change needs a CHANGELOG.md entry under "
            "'## Unreleased', written as '- <verb> <what> (<ISSUE-ID>)'.")

@mcp.tool()
def lookup_issue(issue_id: str) -> str:
    """Look up an issue by id and return its title and acceptance criteria."""
    issues = {
        "CART-412": {
            "title": "apply_discount accepts out-of-range percentages",
            "criteria": ("Reject pct < 0 or pct > 100 with ValueError. "
                         "cart_total must validate too."),
        }
    }
    i = issues.get(issue_id.upper())
    return (f"{issue_id}: {i['title']}\nAcceptance criteria: {i['criteria']}"
            if i else f"No issue {issue_id}")

if __name__ == "__main__":
    mcp.run()