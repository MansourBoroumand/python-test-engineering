# Serial Device Tester

A Python-based serial communication test tool for validating command/response behavior of an embedded device over UART.

## Project Overview

This project demonstrates automated serial communication testing between a Python test application and an Arduino Uno used as the Device Under Test (DUT).

The Python application:

- Detects available serial ports
- Opens and configures a serial connection
- Sends test commands to the DUT
- Reads DUT responses
- Detects communication timeouts
- Validates actual responses against expected responses
- Reports PASS / FAIL results
- Separates communication failures from functional failures
- Generates a final test summary

## Hardware

- Arduino Uno
- USB cable
- Windows PC

## Software

- Python
- PySerial
- pytest
- Arduino IDE

## Communication Parameters

- Interface: Serial / UART
- Baud rate: 115200
- Port: COM3
- Line termination: New Line

## Supported Commands

| Command | Expected Response |
|---|---|
| GET_STATUS | STATUS:OK |
| GET_VERSION | VERSION:1.0 |
| Hi | Hallo |

## Project Structure

```text
serial_device_tester/
├── serial_device_tester.py
├── README.md
├── arduino_serial_dut/
│   └── arduino_serial_dut.ino
└── tests/
    └── test_serial_device_tester.py