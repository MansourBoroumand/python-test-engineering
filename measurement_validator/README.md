# Measurement Validator

A Python-based measurement validation tool designed to simulate a basic test engineering workflow.

The program compares measured values against expected values using a defined tolerance and automatically determines whether each measurement passes or fails.

## Features

- Measurement validation based on expected value and tolerance
- Automatic lower and upper limit calculation
- PASS / FAIL evaluation
- Support for different measurement types and units
- User input validation
- Measurement result reporting
- Timestamped CSV result logging
- Automated testing with pytest
- Boundary value testing
- Parameterized test cases
- Handling of negative expected values

## Validation Logic

The acceptable measurement range is calculated using:

```text
Tolerance Value = |Expected Value| × Tolerance (%) / 100

Lower Limit = Expected Value - Tolerance Value

Upper Limit = Expected Value + Tolerance Value
```

The measured value passes when:

```text
Lower Limit <= Measured Value <= Upper Limit
```

Otherwise, the result is:

```text
FAIL
```

## Example

For a voltage measurement:

```text
Expected value: 5.0 V
Measured value: 5.05 V
Tolerance: 2 %
```

The calculated limits are:

```text
Lower limit: 4.9 V
Upper limit: 5.1 V
```

Since:

```text
4.9 <= 5.05 <= 5.1
```

the result is:

```text
PASS
```

## Project Structure

```text
measurement_validator/
├── measurement_validator.py
├── README.md
└── tests/
    └── test_measurement_validator.py
```

## Automated Tests

The project includes pytest tests covering:

- Measurements within tolerance
- Measurements outside tolerance
- Lower boundary
- Upper boundary
- Zero tolerance
- Voltage measurements
- Current measurements
- Resistance measurements
- Tolerance calculations
- Negative expected values

Parameterized tests are used to evaluate multiple test cases efficiently.

Run the complete test suite from the repository root:

```bash
python -m pytest
```

## Technologies

- Python
- pytest
- CSV
- Git
- GitHub

## Purpose

This project demonstrates fundamental concepts used in test engineering, including:

- Measurement validation
- Tolerance analysis
- Boundary value analysis
- Automated PASS / FAIL decisions
- Test result logging
- Unit testing
- Regression testing

It serves as a foundation for more advanced test automation projects involving real devices and laboratory instruments.