# GRC102 Practical Lab 8
# Security Governance Simulation, Analysis, Control Implementation and Executive Reporting

**Student Name:** Chioma Ameh  
**Student ID:** C11/26/CGRCE/17567  
**Course:** GRC102 - Information Security Governance  
**Program:** ICDFA Cohort 11 - GRC Engineering (CGRCE)

---

# Executive Summary

This repository contains the complete implementation, analysis, remediation activities, governance artifacts, metrics, and supporting evidence for GRC102 Practical Lab 8.

The project reproduces governance weaknesses similar to those that contributed to the 2017 Equifax breach using a controlled Docker-based environment. The exercise demonstrates how inadequate governance, poor patch management, ineffective monitoring, and weak oversight can lead to significant organizational risk.

The assessment involved:

- Building a simulated vulnerable environment
- Conducting vulnerability assessments
- Identifying governance control failures
- Implementing corrective governance controls
- Verifying remediation effectiveness
- Generating executive-level security metrics and reports

The repository contains all scripts, reports, screenshots, dashboards, governance documentation, and supporting evidence required for assessment.

---

# Learning Objectives Achieved

✅ Build a simulated security governance environment

✅ Identify and analyse governance failures

✅ Compare governance weaknesses to the Equifax breach

✅ Implement governance controls

✅ Validate the effectiveness of remediation efforts

✅ Develop security governance metrics

✅ Produce executive dashboards and board-level reporting

✅ Demonstrate governance oversight and accountability

---

# Project Architecture

The simulation environment consists of four primary components:

## Vulnerable Web Application

Apache Struts 2 web application intentionally configured with the S2-045 vulnerability used during the Equifax breach.

## Database Server

MySQL database configured with insecure credentials and governance weaknesses for assessment purposes.

## Monitoring Server

Security monitoring platform used to collect events, detect activity and provide operational visibility.

## Governance Platform

Governance tracking solution used to evaluate security controls, monitor remediation activities and generate governance metrics.

---

# Repository Structure

```text
grc102-lab8-security-governance/
│
├── README.md
├── docs/
├── scripts/
├── config/
├── database_init/
├── monitoring/
├── reports/
├── metrics_visualizations/
├── evidence/
└── repository_evidence_map.md
```

---

# Assessment Part 1
# Simulated Security Governance Environment

## Objective

Create and evaluate a vulnerable environment that demonstrates governance weaknesses.

## Activities Performed

### Environment Setup

- Docker installation and configuration
- Docker Compose deployment
- MySQL database initialization
- Creation of governance services
- Configuration of monitoring environment

### Vulnerability Discovery

The vulnerability scanner identified several security concerns:

| Finding | Severity |
|----------|----------|
| Apache Struts S2-045 (CVE-2017-5638) | Critical |
| Default MySQL Credentials | High |
| Flat Network Architecture | Medium |

### Governance Weaknesses Identified

- Lack of effective patch management
- Weak authentication practices
- Insufficient monitoring controls
- Poor network segregation
- Inadequate security governance oversight

---

## Evidence Location

```text
evidence/part1_environment_setup/
```

Supporting screenshots include:

```text
fig1_kali_vm.png
fig2_docker_installation.png
fig3_docker_compose_fix.png
fig4_db_initialization.png
fig5_container_startup.png
fig6_vulnerability_scan.png
fig7_governance_tracker.png
fig8_dashboard.png
```

---

# Assessment Part 2
# Governance Failure Analysis

## Objective

Identify governance failures and compare them to the factors that contributed to the Equifax breach.

---

## Governance Failure 1
### Patch Management Failure

The vulnerable Apache Struts component remained unpatched despite publicly available updates.

**Impact**

- Increased exposure to exploitation
- Critical organizational risk
- Failure of asset governance

---

## Governance Failure 2
### Vulnerability Management Failure

Known vulnerabilities were not effectively identified, tracked or remediated.

**Impact**

- Persistent security weaknesses
- Increased attack surface

---

## Governance Failure 3
### Monitoring and Detection Failure

Security monitoring capabilities were insufficient to reliably identify suspicious activity.

**Impact**

- Delayed incident awareness
- Increased breach impact

---

## Governance Failure 4
### Security Architecture Failure

Systems operated within a flat network environment with limited segmentation.

**Impact**

- Greater potential lateral movement
- Expanded compromise scope

---

## Governance Failure 5
### Authentication and Access Control Failure

Weak credential practices exposed critical systems.

**Impact**

- Elevated unauthorized access risk

---

## Governance Failure 6
### Governance Oversight Failure

Security accountability and executive oversight mechanisms were insufficient.

**Impact**

- Delayed remediation
- Weak governance culture

---

## Equifax Comparison

The simulation demonstrates governance failures closely aligned with those publicly identified following the Equifax breach:

| Equifax Failure | Lab Simulation |
|---------------|---------------|
| Unpatched Apache Struts | Vulnerable Struts Deployment |
| Weak oversight | Governance tracking deficiencies |
| Monitoring gaps | Detection weaknesses |
| Delayed remediation | Vulnerability persistence |
| Poor accountability | Governance ownership weaknesses |

---

## Evidence Location

```text
evidence/part2_governance_failures/
```

---

# Assessment Part 3
# Governance Control Implementation

## Objective

Implement governance controls and verify their effectiveness.

---

## Control 1
### Patch Governance

Implemented actions:

- Software inventory review
- Upgrade planning
- Remediation workflows
- Patch verification procedures

---

## Control 2
### Database Hardening

Implemented actions:

- Removed insecure credentials
- Improved authentication controls
- Strengthened database access governance

---

## Control 3
### Network Segmentation

Implemented actions:

- Backend network creation
- Service separation
- Reduced attack pathways

---

## Control 4
### Security Monitoring

Implemented actions:

- Monitoring automation
- Event logging improvements
- Governance oversight controls

---

## Control 5
### Accountability and Governance

Implemented actions:

- Governance ownership assignments
- Reporting mechanisms
- Executive oversight processes

---

## Verification Results

| Metric | Before | After |
|----------|---------|---------|
| Critical Findings | 1 | 0 |
| High Findings | 1 | 0 |
| Medium Findings | 1 | 1 |
| Attack Success | Successful | Blocked |

The results demonstrate a measurable reduction in organizational security risk.

---

## Evidence Location

```text
evidence/part3_control_implementation/
```

---

# Assessment Part 4
# Governance Metrics and Reporting

## Objective

Develop governance metrics and provide executive-level reporting.

---

## Governance Metrics

The following key metrics were developed:

### Patch Compliance Rate

Measures the percentage of systems operating with approved patch levels.

---

### Vulnerability Remediation Rate

Measures the speed and effectiveness of vulnerability remediation.

---

### Security Incident Count

Tracks recorded security events and incident trends.

---

### Monitoring Coverage

Evaluates visibility across systems and services.

---

### Policy Compliance

Measures adherence to established governance requirements.

---

# Executive Dashboard

The governance dashboard provides leadership visibility into:

- Vulnerability status
- Patch compliance
- Incident monitoring
- Governance performance
- Compliance trends

---

# Board 
