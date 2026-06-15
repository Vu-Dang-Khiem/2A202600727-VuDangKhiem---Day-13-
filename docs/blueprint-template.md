# Day 13 Observability Lab Report

> **Instruction**: Fill in all sections below. This report is designed to be parsed by an automated grading assistant. Ensure all tags (e.g., `[GROUP_NAME]`) are preserved.

## 1. Team Metadata
- [GROUP_NAME]: 2A202600727
- [REPO_URL]: https://github.com/Vu-Dang-Khiem/2A202600727-VuDangKhiem---Day-13-
- [MEMBERS]:
  - Member A: Vũ Đăng Khiêm | Role: Logging & PII
  - Member B: Vũ Đăng Khiêm | Role: Tracing & Enrichment
  - Member C: Vũ Đăng Khiêm | Role: SLO & Alerts
  - Member D: Vũ Đăng Khiêm | Role: Load Test & Dashboard
  - Member E: Vũ Đăng Khiêm | Role: Demo & Report

---

## 2. Group Performance (Auto-Verified)
- [VALIDATE_LOGS_FINAL_SCORE]: 100/100
- [TOTAL_TRACES_COUNT]: 108
- [PII_LEAKS_FOUND]: 0

---

## 3. Technical Evidence (Group)

### 3.1 Logging & Tracing
- [EVIDENCE_CORRELATION_ID_SCREENSHOT]: docs/dashboard_1_latency.png
- [EVIDENCE_PII_REDACTION_SCREENSHOT]: docs/dashboard_2_traffic.png
- [EVIDENCE_TRACE_WATERFALL_SCREENSHOT]: docs/dashboard_3_error_rate.png
- [TRACE_WATERFALL_EXPLANATION]: The `run` span captures the full agent pipeline — RAG retrieval + LLM generation. During the `rag_slow` incident, latency spiked from ~150ms to ~2650ms, visible as a long span in the waterfall. This pinpointed the retrieval step as the bottleneck.

### 3.2 Dashboard & SLOs
- [DASHBOARD_6_PANELS_SCREENSHOT]: docs/dashboard_1_latency.png
- [SLO_TABLE]:
| SLI | Target | Window | Current Value |
|---|---:|---|---:|
| Latency P95 | < 3000ms | 28d | 150ms |
| Error Rate | < 2% | 28d | 0% |
| Cost Budget | < $2.5/day | 1d | $0.00 |

### 3.3 Alerts & Runbook
- [ALERT_RULES_SCREENSHOT]: docs/dashboard_4_cost.png
- [SAMPLE_RUNBOOK_LINK]: docs/alerts.md#1-high-latency-p95

---

## 4. Incident Response (Group)
- [SCENARIO_NAME]: rag_slow
- [SYMPTOMS_OBSERVED]: Latency spiked from ~150ms to ~2650ms per request. All requests during the incident window showed P95 latency exceeding the 3000ms SLO threshold.
- [ROOT_CAUSE_PROVED_BY]: Trace IDs req-caba5d18, req-05b0328c, req-9e65704d all show latency=2650ms logged in data/logs.jsonl. The `rag_slow` incident flag injected a sleep in the RAG retrieval step.
- [FIX_ACTION]: Disabled incident via POST /incidents/rag_slow/disable. Latency immediately returned to ~150ms.
- [PREVENTIVE_MEASURE]: Alert `high_latency_p95` in config/alert_rules.yaml triggers at P95 > 5000ms for 30 minutes, notifying team-oncall to investigate RAG pipeline health.

---

## 5. Individual Contributions & Evidence

### Vũ Đăng Khiêm
- [TASKS_COMPLETED]: Implemented Correlation ID middleware (app/middleware.py), PII scrubbing with regex patterns for email/phone/CCCD/credit card/passport/address (app/pii.py), structured logging pipeline with PII processor (app/logging_config.py), log enrichment with user context (app/main.py), Langfuse tracing with @observe decorator (app/tracing.py, app/agent.py), SLO configuration (config/slo.yaml), alert rules (config/alert_rules.yaml), 6-panel Langfuse dashboard, load testing and incident injection.
- [EVIDENCE_LINK]: https://github.com/Vu-Dang-Khiem/2A202600727-VuDangKhiem---Day-13-

### [MEMBER_B_NAME]
- [TASKS_COMPLETED]: N/A
- [EVIDENCE_LINK]: N/A

### [MEMBER_C_NAME]
- [TASKS_COMPLETED]: N/A
- [EVIDENCE_LINK]: N/A

### [MEMBER_D_NAME]
- [TASKS_COMPLETED]: N/A
- [EVIDENCE_LINK]: N/A

### [MEMBER_E_NAME]
- [TASKS_COMPLETED]: N/A
- [EVIDENCE_LINK]: N/A

---

## 6. Bonus Items (Optional)
- [BONUS_COST_OPTIMIZATION]: N/A
- [BONUS_AUDIT_LOGS]: N/A
- [BONUS_CUSTOM_METRIC]: N/A
