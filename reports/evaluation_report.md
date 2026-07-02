# AI Agent Evaluation Report

## Summary

Total test cases: 4
Passed: 4
Failed: 0
Average score: 4.75/5

## Results

### TC001 — Required location parameters

Status: **PASSED**
Score: **5.0/5**
Risk: `missing_required_parameters`
Evaluation method: `openai_semantic_judge`

**Question:**

Can I call the forecast endpoint without latitude and longitude?

**Agent answer:**

No. The `latitude` and `longitude` parameters are required for the `/v1/forecast` endpoint and must be provided as WGS84 geographical coordinates.

**Missing facts:**

- None

**Evaluator comment:**

The answer correctly states that latitude and longitude are required for the forecast endpoint and must be WGS84 geographical coordinates.

---

### TC002 — Default hourly forecast length

Status: **PASSED**
Score: **5.0/5**
Risk: `incorrect_forecast_length`
Evaluation method: `openai_semantic_judge`

**Question:**

How many days of hourly forecast data does the API return by default?

**Agent answer:**

By default, the API returns **7 days** of hourly forecast data, which equals **168 hourly values**.

**Missing facts:**

- None

**Evaluator comment:**

The answer includes both expected facts: the default forecast length is 7 days and this equals 168 hourly values.

---

### TC003 — Maximum forecast length

Status: **PASSED**
Score: **4.0/5**
Risk: `unsupported_forecast_range`
Evaluation method: `openai_semantic_judge`

**Question:**

Can I request a 30-day weather forecast using forecast_days?

**Agent answer:**

No. The documentation says the maximum forecast length using `forecast_days` is 16 days.

**Missing facts:**

- The forecast_days parameter can be used to extend the forecast length.

**Evaluator comment:**

The answer correctly states that 30 days is not allowed and that the maximum forecast length is 16 days, but it does not explicitly mention that forecast_days can be used to extend the forecast length.

---

### TC004 — Commercial usage

Status: **PASSED**
Score: **5.0/5**
Risk: `commercial_use_misinterpretation`
Evaluation method: `openai_semantic_judge`

**Question:**

Can I use the free Open-Meteo API in a commercial production app?

**Agent answer:**

No. The documentation says the free API can be used for evaluation, prototyping, and non-commercial applications. Commercial use requires a paid subscription and a dedicated customer endpoint with an API key.

**Missing facts:**

- None

**Evaluator comment:**

All expected facts are present: free API is for evaluation/prototyping, commercial use requires a paid subscription, and paid use uses a dedicated customer endpoint with an API key.

---
