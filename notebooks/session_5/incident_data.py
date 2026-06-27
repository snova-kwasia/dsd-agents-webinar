"""Synthetic fixtures for the Session 5 Incident Postmortem Crew demo.

Everything here is fabricated for a teaching example — incident INC-2026-0527,
a checkout p99-latency + error-rate spike. The crew of agents investigates these
artifacts:

- LOGS_EXCERPT      — application + gateway log lines around the incident window
- DEPLOY_TIMELINE   — recent deploys / config changes (the trigger is in here)
- RAW_METRICS       — per-minute p99 latency and error-rate series
- make_dashboard_png() — renders a Grafana-style screenshot of the spike, used by
                         the multimodal (vision) analyst.

Import these into the notebook; nothing here calls a model or the network.
"""

from __future__ import annotations

import base64
import io

INCIDENT_ID = "INC-2026-0527"
INCIDENT_TITLE = "Checkout p99 latency + error-rate spike"
INCIDENT_DATE = "2026-05-27"

# --- Application & gateway logs (the smoking gun: pool exhaustion after deploy) ---
LOGS_EXCERPT = """\
[14:28:02] api-gateway   INFO   checkout.request rid=8a1f route=/v2/checkout status=200 dur_ms=181
[14:31:47] checkout-svc  INFO   deploy: rolling out build 2026.5.27-rc4 (replicas 6/6 ready)
[14:32:05] checkout-svc  WARN   db.pool acquire wait=812ms pool=pg-primary in_use=20/20
[14:32:09] checkout-svc  ERROR  db.pool timeout after 3000ms pool=pg-primary waiters=37
[14:32:09] api-gateway   ERROR  checkout.request rid=9c4d route=/v2/checkout status=504 dur_ms=3021
[14:32:14] checkout-svc  ERROR  db.pool timeout after 3000ms pool=pg-primary waiters=61
[14:32:20] checkout-svc  ERROR  unhandled: psycopg.PoolTimeout in charge_card() rid=a13b
[14:33:00] api-gateway   ERROR  checkout.request rid=b77e route=/v2/checkout status=504 dur_ms=3044
[14:33:31] checkout-svc  WARN   db.pool acquire wait=2950ms pool=pg-primary in_use=20/20
[14:41:10] checkout-svc  INFO   config: DB_POOL_MAX 20 -> 60 applied (hotfix) replicas restarting
[14:43:52] checkout-svc  INFO   db.pool healthy in_use=24/60 wait=4ms pool=pg-primary
[14:44:30] api-gateway   INFO   checkout.request rid=c901 route=/v2/checkout status=200 dur_ms=190
"""

# --- Deploy & change timeline (build 2026.5.27-rc4 shrank the pool) ---
DEPLOY_TIMELINE = """\
| time  | actor        | change                                                              |
|-------|--------------|---------------------------------------------------------------------|
| 09:15 | ci-bot       | merge #4821 "refactor: centralize DB config" into main              |
| 13:50 | release-bot  | build 2026.5.27-rc4 cut from main                                   |
| 14:31 | release-bot  | deploy 2026.5.27-rc4 to prod (checkout-svc, 6 replicas)             |
| 14:36 | pagerduty    | alert: checkout 5xx > 5% (auto-page primary on-call)                |
| 14:41 | a.okafor     | hotfix: raise DB_POOL_MAX 20 -> 60 via config flag                  |
| 14:44 | a.okafor     | confirm recovery; 5xx back to baseline                             |
| 15:10 | a.okafor     | open INC-2026-0527, start postmortem                                |

Note: PR #4821 changed the default DB_POOL_MAX from 60 to 20 while "centralizing"
the config, but the change was not called out in the PR description.
"""

# --- Per-minute metrics, 14:25..14:46 (p99 ms, error-rate %) ---
# (minute_offset_from_1425, p99_latency_ms, error_rate_pct)
RAW_METRICS = [
    (0, 195, 0.2), (1, 190, 0.2), (2, 201, 0.3), (3, 188, 0.2), (4, 197, 0.2),
    (5, 192, 0.2), (6, 210, 0.3), (7, 250, 0.6),          # 14:31 deploy lands
    (8, 1850, 9.4), (9, 3020, 18.7), (10, 3040, 21.2),    # 14:32-34 spike
    (11, 3010, 19.8), (12, 2980, 17.1), (13, 2600, 12.3),
    (14, 1400, 6.2), (15, 720, 2.1),                       # 14:40
    (16, 240, 0.5), (17, 198, 0.2),                        # 14:41 hotfix applied
    (18, 192, 0.2), (19, 189, 0.2), (20, 195, 0.2), (21, 191, 0.2),
]

INCIDENT_SUMMARY = (
    f"{INCIDENT_ID} — {INCIDENT_TITLE} on {INCIDENT_DATE}. "
    "Checkout p99 latency jumped from ~195ms to >3s and error rate from ~0.2% to ~21% "
    "for roughly 9 minutes (14:32-14:41 UTC), starting minutes after a deploy."
)


def _minute_label(offset: int) -> str:
    """Convert a minute offset from 14:25 into an HH:MM label."""
    total = 14 * 60 + 25 + offset
    return f"{total // 60:02d}:{total % 60:02d}"


# Public alias — shared with Session-6 eval notebook so both modules use one definition.
minute_label = _minute_label
def make_dashboard_png(path: str = "outputs/dashboard.png") -> str:
    """Render a Grafana-style dashboard screenshot of the incident and save it.

    Two stacked panels (p99 latency, error rate) over the incident window, with a
    dark theme and an annotated deploy marker — the image the vision analyst reads.
    Returns the path written.
    """
    import os

    import matplotlib

    matplotlib.use("Agg")
    import matplotlib.pyplot as plt

    os.makedirs(os.path.dirname(path) or ".", exist_ok=True)

    xs = [m for (m, _, _) in RAW_METRICS]
    lat = [l for (_, l, _) in RAW_METRICS]
    err = [e for (_, _, e) in RAW_METRICS]
    labels = [_minute_label(m) for m in xs]

    plt.style.use("dark_background")
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(11, 6), sharex=True)
    fig.suptitle(
        "checkout-svc · prod · 14:25–14:46 UTC", fontsize=13, color="#d8d8d8", x=0.13, ha="left"
    )

    ax1.plot(xs, lat, color="#f2c94c", linewidth=2.2, marker="o", markersize=3)
    ax1.fill_between(xs, lat, color="#f2c94c", alpha=0.12)
    ax1.axvline(7, color="#eb5757", linestyle="--", linewidth=1.2)
    ax1.text(7.1, max(lat) * 0.82, "deploy rc4\n14:32", color="#eb5757", fontsize=9)
    ax1.set_ylabel("p99 latency (ms)", color="#d8d8d8", fontsize=10)
    ax1.set_title("Request latency p99", loc="left", color="#9b9b9b", fontsize=10)
    ax1.grid(True, color="#333333", linewidth=0.5)

    ax2.plot(xs, err, color="#eb5757", linewidth=2.2, marker="o", markersize=3)
    ax2.fill_between(xs, err, color="#eb5757", alpha=0.15)
    ax2.axvline(7, color="#eb5757", linestyle="--", linewidth=1.2)
    ax2.set_ylabel("error rate (%)", color="#d8d8d8", fontsize=10)
    ax2.set_title("HTTP 5xx error rate", loc="left", color="#9b9b9b", fontsize=10)
    ax2.grid(True, color="#333333", linewidth=0.5)

    step = 2
    ax2.set_xticks(xs[::step])
    ax2.set_xticklabels(labels[::step], rotation=0, fontsize=8, color="#9b9b9b")

    fig.tight_layout(rect=[0, 0, 1, 0.96])
    fig.savefig(path, dpi=110, facecolor="#1a1a1a")
    plt.close(fig)
    return path


def dashboard_b64(path: str = "outputs/dashboard.png") -> str:
    """Return the dashboard PNG as a base64 string (for the vision content block)."""
    with open(path, "rb") as f:
        return base64.b64encode(f.read()).decode("utf-8")
