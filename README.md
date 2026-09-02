# Measurement Validator

A Python-based measurement validation tool designed to simulate a basic engineering test workflow.

The program compares measured values against expected values and determines whether each measurement passes or fails based on a user-defined tolerance.

The project demonstrates fundamental concepts used in test engineering, including measurement validation, tolerance checking, input validation, automated result evaluation, test reporting, and CSV data logging.

## Features

- Supports different types of measurements such as voltage, current, and resistance
- Accepts expected and measured values from the user
- Calculates upper and lower tolerance limits automatically
- Determines PASS or FAIL for each measurement
- Validates numeric user inputs
- Supports multiple measurements in a single test session
- Generates a summary of passed and failed tests
- Automatically saves test results to a CSV file
- Adds date and time to the generated CSV filename
- Displays the full path of the saved report
- Uses a modular function-based program structure

## Example

For an expected voltage of:

```text
5.00 V
```

with a tolerance of:

```text
2 %
```

the acceptable range is:

```text
4.90 V - 5.10 V
```

If the measured value is:

```text
4.93 V
```

the result will be:

```text
PASS
```

If the measured value is outside the allowed range, the result will be:

```text
FAIL
```

## Example Test Report

```text
========== TEST REPORT ==========

--- Measurement Result ---
Measurement: Voltage
Expected: 5.00 V
Measured: 4.90 V
Tolerance: 2.00 %
Allowed Range: 4.90 V - 5.10 V
Result: PASS

--- Measurement Result ---
Measurement: Current
Expected: 2.00 A
Measured: 1.90 A
Tolerance: 1.00 %
Allowed Range: 1.98 A - 2.02 A
Result: FAIL

========== TEST SUMMARY ==========
Total Tests: 2
Passed: 1
Failed: 1
Overall Result: FAIL
```

## CSV Report

After completing the measurements, the program automatically saves the results in a CSV file.

The filename contains the date and time of the test execution:

```text
measurement_results_2026-09-02_104910.csv
```

The CSV report contains information such as:

- Measurement type
- Expected value
- Measured value
- Tolerance percentage
- Calculated tolerance value
- Lower limit
- Upper limit
- Measurement unit
- PASS/FAIL result

Generated measurement reports are excluded from Git tracking using `.gitignore`.

## Project Structure

```text
python-test-engineering/
│
├── measurement_validator.py
├── temperature_validator.py
├── README.md
└── .gitignore
```

The main program for this project is:

```text
measurement_validator.py
```

## Main Functions

### `validate_measurement()`

Calculates the tolerance limits and determines whether a measurement passes or fails.

### `get_float_input()`

Accepts and validates floating-point numerical input from the user.

### `get_integer_input()`

Ensures that the number of requested tests is a positive integer.

### `get_non_negative_float_input()`

Ensures that values such as tolerance percentages are not negative.

### `print_measurement_result()`

Displays the detailed result of an individual measurement.

### `print_test_summary()`

Calculates and displays the total number of passed and failed measurements and determines the overall test result.

### `save_results_to_csv()`

Stores all measurement results in a timestamped CSV report.

### `main()`

Controls the overall program workflow, including user input, measurement validation, reporting, and CSV file generation.

## Requirements

- Python 3.x

The project currently uses only Python standard library modules:

```python
import csv
import os
from datetime import datetime
```

Therefore, no additional third-party packages are required.

## How to Run

Clone the repository or download the project files.

Open a terminal in the project directory and run:

```bash
python measurement_validator.py
```

The program will ask for:

1. Number of measurements
2. Measurement name
3. Expected value
4. Measured value
5. Tolerance percentage
6. Measurement unit

After all measurements are entered, the program displays the complete test report and saves the results to a CSV file.

## Purpose of the Project

This project was created as part of a practical Python learning path focused on Test Engineering and test automation.

It demonstrates how Python can be used to implement a simple measurement evaluation workflow similar to those used in electronics testing and validation.

Future improvements may include:

- Automated testing with `pytest`
- Additional test cases and boundary-condition testing
- JSON report generation
- Instrument communication
- Automated measurement acquisition
- Serial communication using PySerial
- Test equipment control using PyVISA

## License

This project is intended for educational and portfolio purposes.
