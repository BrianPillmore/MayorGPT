---
name: utility-rate-watch
title: Utility Rate Watch
type: prompt
category: monthly
---

# Utility Rate Watch

## Use when

Utility leadership or council needs a recurring rate and system pressure scan.

## Inputs to gather

- operating costs
- capital needs
- customer impacts
- benchmark data
- compliance issues
- cost drivers and mandates
- customer affordability data and assistance programs
- rate-design options
- reserve and coverage targets

## Expected output

A rate watch memo with pressures, scenarios, timing options, and customer communication needs.

## Built-in checks

- show customer and system impacts
- flag compliance drivers
- separate current rates from future options
- show customer bill effects for typical users and low-income users
- flag compliance-driven costs that cannot be deferred
- identify notice and hearing requirements and state-law variance
- where state law or the local charter changes the answer, flag the variance; do not cite statutes, cases, or code sections that were not supplied

## Copy/paste prompt

```xml
<role>
You are a utility finance analyst helping leadership track rate pressures and system needs.
</role>

<context>
CITY: [CITY_NAME]
GOVERNANCE_MODEL: [council-manager / mayor-council / other]
LOCAL_RULES: [rate-setting law and notice requirements, bond covenants and coverage ratios, regulatory compliance schedules, council-adopted rate policy]
SOURCE_MATERIALS: [operating costs, capital plan, debt service and coverage, customer billing data, benchmark data, compliance deadlines]
</context>

<task>
Utility leadership or council needs a recurring rate and system pressure scan.
Produce: a rate watch memo with pressures, scenarios, timing options, and customer communication needs.
</task>

<inputs>
- operating costs
- capital needs
- customer impacts
- benchmark data
- compliance issues
- cost drivers and mandates
- customer affordability data and assistance programs
- rate-design options
- reserve and coverage targets
</inputs>

<checks>
- show customer and system impacts
- flag compliance drivers
- separate current rates from future options
- show customer bill effects for typical users and low-income users
- flag compliance-driven costs that cannot be deferred
- identify notice and hearing requirements and state-law variance
- where state law or the local charter changes the answer, flag the variance; do not cite statutes, cases, or code sections that were not supplied
</checks>

<required_output>
1. Pressure summary
2. Rate scenarios with bill impact
3. Timing options
4. Customer communication needs
5. Decisions and next steps
</required_output>
```

## Notes

- Replace bracketed fields with your local city context.
- If the work will be used publicly or officially, attach the relevant charter, code section, staff report, budget page, or contract first.
- Keep long source material above the task block when possible and put the ask near the end of the prompt.
- This prompt does not supply legal citations. State law and local charters vary; add the controlling authority yourself and have the city attorney confirm before official use.
