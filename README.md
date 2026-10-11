# GRC102 Security Governance Laboratory

## Student Information

**Name:** Chioma Ameh

**Student ID:** C11/26/CGRCE/17567

**Programme:** ICDFA Trainee – GRC Engineering

**Environment:** Kali Linux (kernel 6.16.8) VirtualBox VM on Windows 11; Docker 28.5.2; Compose 2.40.3.
Isolated lab, synthetic data only, no external targets.

## What this repository contains
| Part | Files |
|---|---|
| 1 Simulated environment | `docker-compose.yml`, `database_init/init.sql`, `vulnerability_scanner.py`, `vulnerability_report_*.json`, `patch_management.py`, `governance_tracker.py`, `initialize_governance.py`, `governance_data.json` |
| 2 Failure analysis | `simulate_attack.py`, `attack_log.json`, `analyze_governance_failures.py`, `governance_failure_report_*.json`, `equifax_comparison.md` |
| 3 Controls | `implement_governance_controls.py`, `governance_controls_report.md`, `patch_status.json`, `governance_oversight.md`, `monitoring/` |
| 4 Metrics | `governance_metrics.py`, `executive_dashboard.html`, `board_report.md`, `metrics_visualizations/`, `governance_metrics_framework.md`, `dashboard_user_guide.md` |
| Evidence | `screenshots/` (labelled figures), `evidence/attempt1_first_run/` (first attempt), `evidence/pre_remediation/` (results before the real fixes) |

The scripts are the instructor's official scripts. Documented changes only: `docker tag` for the Struts image, one address change and one added argument in the scanner, the same address change in the attack script, and a labelled supplementary remediation. See Appendix A of the PDF report.

## Results
| Check | Official controls only | After supplementary real remediation |
|---|---|---|
| Scanner | Critical 1, High 1, Medium 1 | Critical 0, High 0, Medium 1 |
| Attack simulation | Vulnerable | Not vulnerable |

The remaining Medium finding is a limitation of the official segmentation check; segmentation was proven manually.

## Order of execution
1. Part 1: create the files, `docker-compose up -d`, `./vulnerability_scanner.py`, `./patch_management.py --list`, `./initialize_governance.py`.
2. Part 2: `./simulate_attack.py`, `./analyze_governance_failures.py`, create `equifax_comparison.md`.
3. Part 3: `./implement_governance_controls.py --all`, `--verify`, create `governance_controls_report.md`, then the supplementary real remediation.
4. Part 4: `./governance_metrics.py`, create the framework and user guide.

## Limitations
Simulation with synthetic data; the attack only returns a header; monitoring is designed but not operating; the official dashboard uses random and hard-coded values, so measured results are reported separately in the PDF.

