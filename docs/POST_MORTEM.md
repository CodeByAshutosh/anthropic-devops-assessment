# Incident Post-Mortem: [2025-12-28] - API Latency Spikes

## Executive Summary
[cite_start]On December 28, 2025, the production API experienced significant latency spikes, increasing from 200ms to 3000ms[cite: 103]. [cite_start]Approximately 5% of requests resulted in 504 Gateway Timeouts[cite: 104]. [cite_start]The incident lasted 45 minutes during peak traffic[cite: 105].

## Timeline
- **14:00:** Automated alerts triggered for high response latency.
- **14:10:** Triage identified database connection saturation.
- **14:30:** Applied temporary connection pool increase; latency began to normalize.
- **14:45:** System fully recovered.

## Root Cause Analysis
[cite_start]The root cause was a sudden surge in metadata extraction requests that exhausted the RDS connection pool[cite: 109]. This led to a bottleneck at the database layer, causing the API gateway to timeout while waiting for responses.

## Remediation & Preventive Measures
- [cite_start]**Immediate (High Priority):** Implement an RDS Proxy to manage connection pooling more efficiently and prevent exhaustion during surges[cite: 111].
- [cite_start]**Monitoring Gap:** Add specific Prometheus/Grafana alerts for "Database Connection Utilization > 80%" to catch issues before they impact users[cite: 110].
- [cite_start]**Long-term:** Refine Horizontal Pod Autoscaler (HPA) settings to trigger earlier based on request queuing rather than just CPU usage[cite: 112, 144].