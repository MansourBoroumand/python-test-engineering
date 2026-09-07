# Python Test Engineering Portfolio

A collection of practical Python projects focused on **test engineering, measurement validation, device communication, and instrument automation**.

The repository demonstrates a progressive test automation workflow, starting with software-based measurement validation, continuing with serial communication to a real device, and extending to automated laboratory instrument control using PyVISA and SCPI.

## Projects

### 1. Measurement Validator

A Python tool for validating measured values against expected values and defined tolerances.

**Key features:**

- Automatic tolerance calculation
- Lower and upper limit calculation
- PASS / FAIL evaluation
- Support for different measurement types and units
- Boundary value testing
- CSV result logging
- Automated tests with pytest

Project folder:

```text
measurement_validator/
```

---

### 2. Serial Device Tester

A Python-based automated communication and testing project using an **Arduino Uno as a Device Under Test (DUT)**.

Python communicates with the Arduino through a serial interface and validates command/response behavior.

**Key features:**

- Serial communication using PySerial
- Arduino Uno as a real DUT
- Command/response testing
- Communication timeout handling
- PASS / FAIL evaluation
- Fake serial interface for unit testing
- Automated tests with pytest

Example commands:

```text
GET_STATUS  → STATUS:OK
GET_VERSION → VERSION:1.0
Hi          → Hallo
```

Project folder:

```text
serial_device_tester/
```

---

### 3. Instrument Automation

An automated instrument testing project using **PyVISA, SCPI, and a simulated digital multimeter (DMM)**.

The project demonstrates the basic architecture used to communicate with programmable laboratory instruments.

**Key features:**

- Instrument communication using PyVISA
- SCPI command/query handling
- Simulated DMM using PyVISA-sim
- Instrument identification
- DC voltage measurement
- DC current measurement
- Resistance measurement
- Automatic tolerance validation
- CSV test reports
- Automated tests with pytest

Example SCPI commands:

```text
*IDN?
MEAS:VOLT:DC?
MEAS:CURR:DC?
MEAS:RES?
```

Project folder:

```text
instrument_automation/
```

## Repository Structure

```text
python-test-engineering/
│
├── measurement_validator/
│   ├── measurement_validator.py
│   ├── README.md
│   └── tests/
│
├── serial_device_tester/
│   ├── serial_device_tester.py
│   ├── README.md
│   ├── arduino_serial_dut/
│   └── tests/
│
├── instrument_automation/
│   ├── instrument_tester.py
│   ├── simulated_dmm.yaml
│   ├── README.md
│   └── tests/
│
├── .gitignore
└── README.md
```

## Technologies and Tools

- Python
- pytest
- PySerial
- PyVISA
- PyVISA-py
- PyVISA-sim
- SCPI
- Arduino
- UART / Serial Communication
- CSV
- Git
- GitHub

## Testing

The repository contains automated pytest test suites for all three projects.

Run all tests from the repository root:

```bash
python -m pytest
```

The test suite covers areas such as:

- Measurement validation
- Boundary conditions
- Tolerance calculations
- Command/response validation
- Communication timeout behavior
- Instrument responses
- Invalid measurement responses
- CSV result generation

## Test Engineering Concepts Demonstrated

The projects demonstrate practical concepts commonly used in test and validation engineering:

- Measurement validation
- Tolerance analysis
- Boundary value analysis
- Automated PASS / FAIL decisions
- Device Under Test (DUT) communication
- Command/response testing
- Serial communication
- Instrument control
- SCPI commands
- Test result logging
- Unit testing
- Regression testing
- Hardware-independent testing using simulated and fake devices

## Development Direction

The repository is designed as a growing test engineering portfolio.

Future development may include communication with real laboratory instruments, oscilloscope automation, additional SCPI-based measurements, hardware testing, and more advanced automated test sequences.















