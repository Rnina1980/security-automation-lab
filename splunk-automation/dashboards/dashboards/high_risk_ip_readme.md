📌 High-Risk IP Dashboard (Explanation)

This dashboard focuses on identifying suspicious or malicious IP addresses based on failed authentication activity. It is part of my Security Automation Lab and demonstrates my ability to analyze, correlate, and visualize authentication threat indicators using Splunk.

🔍 What This Dashboard Shows
1. Failed Login Attempts by Source IP (Bar Chart)

This panel displays:

All IPs extracted from detection output

Total failed attempts per IP

Sorted from highest to lowest

Purpose:
Helps quickly identify brute-force attempts or suspicious hosts generating repeated failures.

2. IP Threat Ranking Table

This table provides:

Each IP seen in the logs

Total number of failed login attempts

Ranked by severity

Purpose:
Allows SOC analysts or ISSOs to manually triage the most concerning IPs.

3. Top Offending IP (Single Value Panel)

Highlights:

The single highest-risk IP

Based on number of failed login attempts

Purpose:
Acts as a high-level indicator for rapid decision-making and threat prioritization.

🧠 Why This Dashboard Matters

This dashboard mirrors real SOC workflows:

Quick visualization of authentication threats

Easy identification of brute force indicators

Supports escalation, firewall blocks, or SOAR automation

Demonstrates Splunk search, parsing, and dashboarding skills

🚀 STEP 3 — Commit

After adding both files, commit with:

“Added High-Risk IP Dashboard + README”
