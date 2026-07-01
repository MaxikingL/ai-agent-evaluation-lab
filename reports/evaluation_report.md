# AI Agent Evaluation Report

## Summary

Total test cases: 4
Passed: 3
Failed: 1
Average score: 3.75/5

## Results

### TC001 — Required location parameters

Status: **PASSED**
Score: **5.0/5**
Risk: `missing_required_parameters`

**Question:**

Can I call the forecast endpoint without latitude and longitude?

**Agent answer:**

No. The forecast endpoint requires latitude and longitude. Latitude and longitude must be provided as WGS84 geographical coordinates.

**Missing facts:**

- None

---

### TC002 — Default hourly forecast length

Status: **FAILED**
Score: **0.0/5**
Risk: `incorrect_forecast_length`

**Question:**

How many days of hourly forecast data does the API return by default?

**Agent answer:**

The default forecast length is 7 days. Seven days equals 168 hourly values.

**Missing facts:**

- The default forecast length is 10 days.

---

### TC003 — Maximum forecast length

Status: **PASSED**
Score: **5.0/5**
Risk: `unsupported_forecast_range`

**Question:**

Can I request a 30-day weather forecast using forecast_days?

**Agent answer:**

No. You cannot request a 30-day forecast using forecast_days. The maximum forecast length is 16 days. The forecast_days parameter can be used to extend the forecast length.

**Missing facts:**

- None

---

### TC004 — Commercial usage

Status: **PASSED**
Score: **5.0/5**
Risk: `commercial_use_misinterpretation`

**Question:**

Can I use the free Open-Meteo API in a commercial production app?

**Agent answer:**

No. The free API can be used for evaluation and prototyping. Commercial use requires a paid subscription. Paid commercial use uses a dedicated customer endpoint with an API key.

**Missing facts:**

- None

---
