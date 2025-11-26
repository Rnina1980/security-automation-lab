#!/usr/bin/env python3

"""
failed_logins_parser.py

Simple lab script to simulate a SOAR-style detection.

Reads a log file with failed login events and identifies
users or IPs with too many failures in a short period.

In a real environment, this logic could be tied to a Splunk
alert or SOAR playbook to:
- create an incident
- disable an account
- block an IP
"""

from collections import defaultdict

LOG_FILE = "sample_logs.txt"
THRESHOLD = 5  # failed attempts before we flag

def parse_log_line(line):
    """
    Expected sample format:

    TIMESTAMP | USERNAME | IP | STATUS

    Example:
    2025-11-22T10:01:15 | rafael | 10.0.0.15 | FAILED
    """
    parts = [p.strip() for p in line.split("|")]
    if len(parts) != 4:
        return None

    timestamp, user, ip, status = parts
    return {
        "timestamp": timestamp,
        "user": user,
        "ip": ip,
        "status": status.upper()
    }

def main():
    failed_by_user = defaultdict(int)
    failed_by_ip = defaultdict(int)

    with open(LOG_FILE, "r") as f:
        for line in f:
            parsed = parse_log_line(line)
            if not parsed:
                continue

            if parsed["status"] == "FAILED":
                failed_by_user[parsed["user"]] += 1
                failed_by_ip[parsed["ip"]] += 1

    print("=== High-Risk Users (too many failed logins) ===")
    for user, count in failed_by_user.items():
        if count >= THRESHOLD:
            print(f"- {user}: {count} failed attempts")

    print("\n=== High-Risk IPs ===")
    for ip, count in failed_by_ip.items():
        if count >= THRESHOLD:
            print(f"- {ip}: {count} failed attempts")

if __name__ == "__main__":
    main()
