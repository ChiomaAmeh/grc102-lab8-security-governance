#!/usr/bin/env python3
import json, datetime, os
PATCH_DB = "patch_status.json"
def init_patch_db():
    if not os.path.exists(PATCH_DB):
        data = {
            "patches": [
                {
                    "id": "STRUTS-2017-5638",
                    "cve": "CVE-2017-5638",
                    "component": "Apache Struts 2.3.30",
                    "severity": "Critical",
                    "discovered": "2017-03-07",
                    "patch_available": "2017-03-07",
                    "status": "Not Applied",
                    "days_overdue": 3500,
                    "governance_failure": "Equifax failed to patch for 143 days"
                },
                {
                    "id": "MYSQL-CRED-001",
                    "component": "MySQL 5.7.44",
                    "severity": "High",
                    "status": "Not Applied"
                }
            ]
        }
        with open(PATCH_DB, "w") as f:
            json.dump(data, f, indent=2)

def apply_patches():
    print("=== Patch Management System ===")
    with open(PATCH_DB, "r") as f:
        data = json.load(f)
    for patch in data["patches"]:
        if patch["id"] == "STRUTS-2017-5638":
            patch["status"] = "Applied"
            patch["applied_date"] = datetime.datetime.now().isoformat()
    with open(PATCH_DB, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Patch status saved to {PATCH_DB}")

if __name__ == "__main__":
    init_patch_db()
    apply_patches()
    with open(PATCH_DB) as f:
        print(f.read())
