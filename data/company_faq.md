# Open-Meteo Forecast API — Simplified Documentation

## Overview

Open-Meteo provides a weather forecast API that returns weather data for a given geographical location. The API can be used for prototyping, evaluation and non-commercial applications without an API key.

## Forecast Endpoint

The main forecast endpoint is `/v1/forecast`.
The endpoint accepts geographical coordinates and a list of requested weather variables. It returns weather forecast data in JSON format.

## Required Parameters

The `latitude` and `longitude` parameters are required.
They must be provided as WGS84 geographical coordinates.

Example:

`latitude=52.52&longitude=13.41`

## Hourly Forecast

The API can return hourly weather forecast data.
By default, the forecast covers 7 days. This equals 168 hourly values.
To request specific hourly variables, the `hourly` parameter should be used.

Example:

`hourly=temperature_2m,precipitation_probability`

## Forecast Length

The default forecast length is 7 days.
The forecast can be extended by using the `forecast_days` parameter.
The maximum forecast length is 16 days.
Example:

`forecast_days=16`

## Weather Models

By default, Open-Meteo automatically selects the best suitable weather model for the requested location.
Users can manually select one or more weather models using the `models` parameter.
The default value for `models` is `auto`.

## Units and Time Format

The default temperature unit is Celsius.
The default wind speed unit is kilometers per hour.
The default precipitation unit is millimeters.
Dates use ISO 8601 format, for example `2026-07-01`.

## Usage Limits and Commercial Use

The free API can be used for evaluation and prototyping.
The free API is rate-limited and does not include an uptime guarantee.
Commercial use requires a paid subscription and a dedicated customer endpoint with an API key.