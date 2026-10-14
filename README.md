# GRC102 Practical Lab 8 - Security Governance Simulation (Equifax-modelled)

**Student:** Chioma Ameh | 
**ID:** C11/26/CGRCE/17567 | 
**Programme:** ICDFA Trainee - GRC Engineering
**Environment:** Kali Linux (kernel 6.16.8) VirtualBox VM on Windows 11; Docker 28.5.2; Compose 2.40.3. Isolated lab, synthetic data only, no external targets. Submitted late (after 11 Oct 2026, 4:07 PM WAT).

## Repository layout
| Path | Content |
|---|---|
| `docker-compose.yml`, `database_init/init.sql` | Environment (Part 1, Task 1), as given in the instructor's instructions |
| `scripts/` | The instructor's official scripts (scanner, patch manager, tracker, initialiser, attack simulation, analysis, controls, metrics) with the documented changes below |
| `reports/` | Outputs: scan reports `vulnerability_report_*.json`, `attack_log.json`, `governance_failure_report_*.json`, `equifax_comparison.md`, `governance_controls_report.md`, `governance_oversight.md`, `governance_data.json`, `patch_status.json`, `board_report.md`, `governance_metrics_framework.md`, `dashboard_user_guide.md`, PDF report |
| `executive_dashboard.html`, `dashboards/`, `metrics_visualizations/` | Dashboard and charts (Part 4) |
| `monitoring/` | Files created by the official controls script |
| `evidence/` | Labelled screenshots by Part, `attempt1_first_run/` (my first attempt), `pre_remediation/` (results before the real fixes, plus two scans marked INVALID because the containers were stopped), `EVIDENCE.md` |
| `docs/figure_register.md` | Figure register for the PDF report |

To re-run, copy `scripts/*.py` next to `docker-compose.yml` (the scripts use relative paths).

## Documented changes to the official instructions
1. `docker tag vulhub/struts2:2.3.30 vulhub/struts2:s2-045` - Docker Hub no longer serves the `s2-045` tag; the compose file is unchanged.
2. `vulnerability_scanner.py` and `simulate_attack.py`: `web_server` replaced by `127.0.0.1` (the name only resolves inside Docker); `errors="replace"` added in the segmentation check.
3. A clearly labelled supplementary real remediation (MySQL password change, internal `backend_network`, Struts upgrade to 2.3.34-showcase), because the official control script only simulates controls.

## Results
| Check | Official controls only | After supplementary remediation |
|---|---|---|
| Scanner | Critical 1, High 1, Medium 1 (`vulnerability_report_20261011_012507/015357/015841/022005.json`) | Critical 0, High 0, Medium 1 (`..._073429`, `..._154310`, `..._154558`) |
| Attack simulation | Vulnerable | Not vulnerable |

`vulnerability_report_20261011_011816.json` is the scan as written, before the scanner fix (Struts and segmentation Unknown).
The remaining Medium finding is a limitation of the official segmentation check; segmentation was proven manually (database on its own internal network; web-to-database access fails).

## Limitations
Simulation with synthetic data; the attack only returns a header; monitoring is designed but not operating; the official dashboard uses random and hard-coded values, so measured results are reported separately in the PDF (Part 4).

## AI-assistance declaration
An AI assistant (Claude) was used for guidance, troubleshooting and drafting. I ran all commands and produced all screenshots myself.

Note: `evidence/official_as_written/` holds the official scanner and attack script exactly as written, before my documented fixes.
