# Comparison of Simulated Environment to Equifax Data Breach

## Overview

This report compares governance failures identified during the security governance simulation with failures that contributed to the Equifax breach.

---

## Similar Failures

### Patch Management Failure

Equifax failed to remediate a known Apache Struts vulnerability (CVE-2017-5638).

Simulation Finding:

- Vulnerability remained unpatched.
- Patch-management process was ineffective.

---

### Weak Security Monitoring

Equifax attackers remained undetected for an extended period.

Simulation Finding:

- Monitoring controls were absent.
- Security events lacked visibility.

---

### Lack of Network Segmentation

Weak segmentation increased attacker movement opportunities.

Simulation Finding:

- Web application maintained unnecessary access to database services.
- Network architecture lacked isolation.

---

### Governance Oversight Weaknesses

Equifax governance processes failed to ensure remediation completion.

Simulation Finding:

- Missing governance control ownership.
- Inadequate management oversight.

---

## Lessons Learned

1. Effective patch management is critical.
2. Continuous monitoring improves detection.
3. Network segmentation reduces attack impact.
4. Governance oversight improves accountability.
5. Metrics should drive management action.

---

## Conclusion

The simulation demonstrates how governance failures can contribute to security incidents and highlights the importance of proactive governance controls.
