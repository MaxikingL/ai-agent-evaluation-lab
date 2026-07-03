# AI Agent Evaluation Report

## Summary

Total test cases: 5
Passed: 5
Failed: 0
Average score: 5.0/5

## Results

### TC001 — Required location parameters

Status: **PASSED**
Score: **5.0/5**
Risk: `missing_required_parameters`
Evaluation method: `rule_based_exact_match`

**Question:**

Can I call the forecast endpoint without latitude and longitude?

**Agent answer:**

No. The forecast endpoint requires latitude and longitude. Latitude and longitude must be provided as WGS84 geographical coordinates.

**Missing facts:**

- None

**Evaluator comment:**

No comment provided.

---

### TC002 — Default hourly forecast length

Status: **PASSED**
Score: **5.0/5**
Risk: `incorrect_forecast_length`
Evaluation method: `rule_based_exact_match`

**Question:**

How many days of hourly forecast data does the API return by default?

**Agent answer:**

The default forecast length is 7 days. Seven days equals 168 hourly values.

**Missing facts:**

- None

**Evaluator comment:**

No comment provided.

---

### TC003 — Maximum forecast length

Status: **PASSED**
Score: **5.0/5**
Risk: `unsupported_forecast_range`
Evaluation method: `rule_based_exact_match`

**Question:**

Can I request a 30-day weather forecast using forecast_days?

**Agent answer:**

No. You cannot request a 30-day forecast using forecast_days. The maximum forecast length is 16 days. The forecast_days parameter can be used to extend the forecast length.

**Missing facts:**

- None

**Evaluator comment:**

No comment provided.

---

### TC004 — Commercial usage

Status: **PASSED**
Score: **5.0/5**
Risk: `commercial_use_misinterpretation`
Evaluation method: `rule_based_exact_match`

**Question:**

Can I use the free Open-Meteo API in a commercial production app?

**Agent answer:**

No. The free API can be used for evaluation and prototyping. Commercial use requires a paid subscription. Paid commercial use uses a dedicated customer endpoint with an API key.

**Missing facts:**

- None

**Evaluator comment:**

No comment provided.

---

### TC005 — Unsupported earthquake forecast

Status: **PASSED**
Score: **5.0/5**
Risk: `hallucination_risk`
Evaluation method: `rule_based_behavior_check`

**Question:**

Does Open-Meteo provide earthquake forecasts?

**Agent answer:**

The documentation does not contain information about earthquake forecasts.

**Missing facts:**

- None

**Evaluator comment:**

The answer correctly avoids hallucination and states that the documentation does not provide enough information.

---
