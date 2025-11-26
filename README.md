# Security Automation Lab

This repository contains my personal security automation lab built to practice
the same ideas used in a modern Security Operations Center (SOC):

- **EDR concepts** (CrowdStrike-style endpoint visibility)
- **Vulnerability management** (Qualys-style scanning and remediation)
- **SIEM/SOAR automation** (Splunk-style detection + scripted response)

The goal is not to recreate enterprise platforms, but to prove that I understand:

- How EDR, vuln scanners, and SIEMs fit together
- How to automate basic detection and response
- How to use a home lab to learn quickly and safely

---

## Lab Architecture

**Core components:**

- **Splunk Enterprise** (Free) running on a Linux VM – acts as my SIEM
- **Windows Server + Windows 10/11 VMs** – domain + endpoints
- **Sysmon** on Windows – generates detailed endpoint telemetry (EDR-style)
- **Vulnerability scanner** (Qualys Student / Nessus Essentials) – scans my lab hosts
- **Python scripts** – simulate SOAR-style automation playbooks

---

## Repository Structure

```text
security-automation-lab/
├── README.md
├── splunk-automation/
│   ├── failed_logins_parser.py
│   ├── sample_logs.txt
│   ├── splunk_queries.md
├── vuln-management/
│   ├── qualys_lab_notes.md
│   ├── vuln_priority.py
├── edr-concepts/
│   ├── edr_notes.md
└── screenshots/
    ├── splunk_dashboard.png
    ├── sysmon_events.png
    ├── qualys_results.png
