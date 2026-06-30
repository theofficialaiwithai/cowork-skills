#!/usr/bin/env python3
"""
generate-audit-report.py
AI Security Specialist — HumanFirst AI

Generates a formatted markdown audit report from completed checkpoint data.
Run after all 7 checkpoints are complete.

Usage:
    python scripts/generate-audit-report.py

The script prompts for checkpoint results interactively, then writes the
report to /outputs/security-audit-report-[appname]-[date].md
"""

import os
import json
from datetime import datetime

# ── Output directory ──────────────────────────────────────────────────────────
OUTPUT_DIR = os.path.join(os.path.dirname(__file__), "..", "outputs")
os.makedirs(OUTPUT_DIR, exist_ok=True)

# ── Status emoji helpers ──────────────────────────────────────────────────────
STATUS_EMOJI = {
    "pass": "✅ Pass",
    "needs work": "⚠️ Needs Work",
    "fail": "❌ Fail",
}

OVERALL_EMOJI = {
    "cleared": "🔒 Cleared for Launch",
    "conditional": "⚠️ Conditional — Review Open Items",
    "not cleared": "🚫 Not Cleared — Resolve High Priority Items First",
}

CHECKPOINTS = [
    {
        "number": 1,
        "name": "Authentication & Access",
        "checked": "Clerk config, MFA, session timeouts, RBAC",
    },
    {
        "number": 2,
        "name": "Database Security",
        "checked": "RLS, env vars, credentials, connection safety",
    },
    {
        "number": 3,
        "name": "API Security",
        "checked": "Rate limiting, input validation, error handling, HTTPS",
    },
    {
        "number": 4,
        "name": "AI-Specific Security",
        "checked": "Prompt injection, system prompt leakage, output validation, audit logs, PII in API calls",
    },
    {
        "number": 5,
        "name": "Infrastructure",
        "checked": "Dependencies, error monitoring, serverless timeouts, secrets in URLs, env var scoping",
    },
    {
        "number": 6,
        "name": "IP Protection",
        "checked": "GitHub repo privacy, TOS, trademark search, system prompt confidentiality, AI data policies",
    },
    {
        "number": 7,
        "name": "Go-Live Hardening",
        "checked": "Production env vars, CORS, console.log audit, auth end-to-end test, agentic workflow test",
    },
]


def prompt(label, default=None):
    """Simple input prompt with optional default."""
    if default:
        val = input(f"{label} [{default}]: ").strip()
        return val if val else default
    val = input(f"{label}: ").strip()
    return val


def collect_checkpoint(cp):
    """Collect status, issues, actions, and remaining items for one checkpoint."""
    print(f"\n── Checkpoint {cp['number']}: {cp['name']} ──")
    print(f"   Checked: {cp['checked']}")

    status_raw = ""
    while status_raw not in ("pass", "needs work", "fail"):
        status_raw = input("   Status (pass / needs work / fail): ").strip().lower()

    issues_raw = input("   Issues found (comma-separated, or 'none'): ").strip()
    issues = [] if issues_raw.lower() == "none" else [i.strip() for i in issues_raw.split(",")]

    actions_raw = input("   Actions taken (comma-separated, or 'none'): ").strip()
    actions = [] if actions_raw.lower() == "none" else [a.strip() for a in actions_raw.split(",")]

    remaining_raw = input("   Remaining items (comma-separated, or 'none'): ").strip()
    remaining = [] if remaining_raw.lower() == "none" else [r.strip() for r in remaining_raw.split(",")]

    return {
        "number": cp["number"],
        "name": cp["name"],
        "checked": cp["checked"],
        "status": status_raw,
        "issues": issues,
        "actions": actions,
        "remaining": remaining,
    }


def determine_overall_status(results):
    """Determine overall launch clearance from checkpoint results."""
    statuses = [r["status"] for r in results]
    has_remaining = any(r["remaining"] for r in results)

    if "fail" in statuses:
        return "not cleared"
    if "needs work" in statuses or has_remaining:
        return "conditional"
    return "cleared"


def build_report(app_name, stack, user_name, results, overall):
    """Build the full markdown report string."""
    date_str = datetime.now().strftime("%B %d, %Y")
    lines = []

    # ── Header ────────────────────────────────────────────────────────────────
    lines += [
        "# Security Audit Report",
        f"**App:** {app_name}",
        f"**Stack:** {stack}",
        f"**Audit Date:** {date_str}",
        "**Auditor:** AI Security Specialist (HumanFirst AI)",
        "",
        "---",
        "",
        "## Audit Summary",
        "",
        "| Checkpoint | Status | Items Fixed | Remaining |",
        "|---|---|---|---|",
    ]

    for r in results:
        fixed = len(r["actions"]) if r["actions"] else 0
        remaining = len(r["remaining"]) if r["remaining"] else 0
        lines.append(
            f"| {r['number']}. {r['name']} "
            f"| {STATUS_EMOJI[r['status']]} "
            f"| {fixed} "
            f"| {remaining} |"
        )

    lines += [
        "",
        f"**Overall Status:** {OVERALL_EMOJI[overall]}",
        "",
        "---",
        "",
        "## Checkpoint Details",
        "",
    ]

    # ── Per-checkpoint detail ─────────────────────────────────────────────────
    for r in results:
        lines += [
            f"### {r['number']}. {r['name']}",
            f"**Status:** {STATUS_EMOJI[r['status']]}",
            f"**What was checked:** {r['checked']}",
            "",
            "**Issues found:**",
        ]
        if r["issues"]:
            lines += [f"- {i}" for i in r["issues"]]
        else:
            lines.append("- None")

        lines += ["", "**Actions taken:**"]
        if r["actions"]:
            lines += [f"- {a}" for a in r["actions"]]
        else:
            lines.append("- None")

        lines += ["", "**Remaining items:**"]
        if r["remaining"]:
            lines += [f"- {rem}" for rem in r["remaining"]]
        else:
            lines.append("- None")

        lines += ["", "---", ""]

    # ── Open items table ──────────────────────────────────────────────────────
    open_items = [
        (r["name"], rem)
        for r in results
        for rem in r["remaining"]
    ]

    lines += [
        "## Open Items (carry forward)",
        "Items not resolved during this audit. Address before next launch or major release.",
        "",
    ]

    if open_items:
        lines += [
            "| # | Checkpoint | Item | Priority |",
            "|---|---|---|---|",
        ]
        for idx, (cp_name, item) in enumerate(open_items, 1):
            lines.append(f"| {idx} | {cp_name} | {item} | — |")
    else:
        lines.append("No open items. All checkpoints resolved. ✅")

    # ── Sign-off ──────────────────────────────────────────────────────────────
    lines += [
        "",
        "---",
        "",
        "## Sign-off",
        "- [ ] All High priority items resolved",
        "- [ ] All checkpoints reviewed",
        "- [ ] App cleared for launch",
        "",
        f"**Cleared by:** {user_name}",
        f"**Date:** {date_str}",
        "",
        "---",
        "*Generated by AI Security Specialist — HumanFirst AI*",
        "*aiwithai.ai*",
    ]

    return "\n".join(lines)


def main():
    print("\n🔒 AI Security Specialist — Audit Report Generator")
    print("=" * 52)
    print("Enter your audit results for each checkpoint.\n")

    app_name = prompt("App name")
    stack = prompt("Stack (e.g. Next.js, Vercel, Clerk, Neon, Claude API)")
    user_name = prompt("Your name", default="Adamma Ihemeson")

    results = []
    for cp in CHECKPOINTS:
        result = collect_checkpoint(cp)
        results.append(result)

    overall = determine_overall_status(results)
    report = build_report(app_name, stack, user_name, results, overall)

    # ── Write output ──────────────────────────────────────────────────────────
    safe_name = app_name.lower().replace(" ", "-")
    date_slug = datetime.now().strftime("%Y-%m-%d")
    filename = f"security-audit-report-{safe_name}-{date_slug}.md"
    output_path = os.path.join(OUTPUT_DIR, filename)

    with open(output_path, "w") as f:
        f.write(report)

    print(f"\n✅ Report saved to: {output_path}")
    print(f"   Overall status: {OVERALL_EMOJI[overall]}")


if __name__ == "__main__":
    main()
