# Instrument Automation with PyVISA

This project demonstrates automated communication and measurement validation with a simulated digital multimeter (DMM) using Python and PyVISA.

The goal is to simulate a realistic test engineering workflow before connecting to real laboratory equipment.

## Features

- Instrument communication using PyVISA
- Simulated DMM using PyVISA-sim
- Instrument identification with SCPI `*IDN?`
- DC voltage measurement
- DC current measurement
- Resistance measurement
- Automatic tolerance validation
- PASS / FAIL evaluation
- CSV result logging
- Pytest-based unit tests
- Fake instrument testing without hardware

## Supported SCPI Commands

The simulated instrument currently supports:

```text
*IDN?
MEAS:VOLT:DC?
MEAS:CURR:DC?
MEAS:RES?