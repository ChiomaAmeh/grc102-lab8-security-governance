#!/usr/bin/env python3
import json, datetime, os
print("=== Security Governance Tracker - Equifax Case Mapping ===")
governance = {
    "framework": "ISO 27001 / NIST CSF",
    "controls_failed": [
        {"control": "A.12.6.1 Management of technical vulnerabilities", "failure": "No patching after 143 days", "impact": "RCE S2-045"},
        {"control": "A.9.4.3 Password management", "failure": "Default MySQL creds root:password", "impact": "Data breach"},
        {"control": "A.13.1.3 Segregation in networks", "failure": "Flat network web->DB", "impact": "Lateral movement"},
        {"control": "A.12.4.1 Event logging", "failure": "No monitoring for 76 days", "impact": "Delayed detection"}
    ],
    "equifax_fine": "$700M",
    "lessons": "Governance > Technology. Patch existed but process failed."
}
fname = f"governance_report_{datetime.datetime.now().strftime('%Y%m%d')}.json"
with open(fname, "w") as f:
    json.dump(governance, f, indent=2)
print(json.dumps(governance, indent=2))
print(f"\nSaved to {fname}")
os.makedirs("monitoring", exist_ok=True)
with open("monitoring/README.md", "w") as f:
    f.write("# Monitoring - Equifax failed to detect for 76 days\n")
print("Monitoring folder created")
