import csv
from datetime import datetime

import pyvisa


def connect_to_instrument():
    resource_manager = pyvisa.ResourceManager(
        "instrument_automation/simulated_dmm.yaml@sim"
    )

    resources = resource_manager.list_resources()

    print("Available VISA resources:")
    print(resources)

    instrument = resource_manager.open_resource(
        "ASRL1::INSTR"
    )

    return instrument


def identify_instrument(instrument):
    response = instrument.query(
        "*IDN?"
    )

    return response.strip()


def measure_dc_voltage(instrument):
    response = instrument.query(
        "MEAS:VOLT:DC?"
    )

    try:
        measured_voltage = float(
            response.strip()
        )

        return measured_voltage

    except ValueError:
        raise ValueError(
            "Invalid voltage response from instrument."
        )


def measure_dc_current(instrument):
    response = instrument.query(
        "MEAS:CURR:DC?"
    )

    try:
        measured_current = float(
            response.strip()
        )

        return measured_current

    except ValueError:
        raise ValueError(
            "Invalid current response from instrument."
        )


def measure_resistance(instrument):
    response = instrument.query(
        "MEAS:RES?"
    )

    try:
        measured_resistance = float(
            response.strip()
        )

        return measured_resistance

    except ValueError:
        raise ValueError(
            "Invalid resistance response from instrument."
        )


def validate_measurement(
    measurement_name,
    measured_value,
    expected_value,
    tolerance_percent,
    unit
):
    tolerance_value = (
        abs(expected_value)
        * tolerance_percent
        / 100
    )

    lower_limit = (
        expected_value
        - tolerance_value
    )

    upper_limit = (
        expected_value
        + tolerance_value
    )

    if lower_limit <= measured_value <= upper_limit:
        result = "PASS"
    else:
        result = "FAIL"

    return {
        "measurement": measurement_name,
        "measured_value": measured_value,
        "expected_value": expected_value,
        "tolerance_percent": tolerance_percent,
        "lower_limit": lower_limit,
        "upper_limit": upper_limit,
        "unit": unit,
        "result": result
    }


def save_results_to_csv(
    instrument_id,
    validation_results
):
    timestamp = datetime.now().strftime(
        "%Y-%m-%d_%H%M%S"
    )

    filename = (
        f"instrument_results_{timestamp}.csv"
    )

    fieldnames = [
        "instrument_id",
        "measurement",
        "measured_value",
        "expected_value",
        "tolerance_percent",
        "lower_limit",
        "upper_limit",
        "unit",
        "result"
    ]

    with open(
        filename,
        "w",
        newline="",
        encoding="utf-8"
    ) as csv_file:

        writer = csv.DictWriter(
            csv_file,
            fieldnames=fieldnames
        )

        writer.writeheader()

        for validation_result in validation_results:
            row = {
                "instrument_id": instrument_id,
                "measurement":
                    validation_result["measurement"],
                "measured_value":
                    validation_result["measured_value"],
                "expected_value":
                    validation_result["expected_value"],
                "tolerance_percent":
                    validation_result["tolerance_percent"],
                "lower_limit":
                    validation_result["lower_limit"],
                "upper_limit":
                    validation_result["upper_limit"],
                "unit":
                    validation_result["unit"],
                "result":
                    validation_result["result"]
            }

            writer.writerow(row)

    print(
        f"Results saved to: {filename}"
    )


def print_result(validation_result):
    print(
        f"\nMeasurement: "
        f"{validation_result['measurement']}"
    )

    print(
        f"Measured value: "
        f"{validation_result['measured_value']} "
        f"{validation_result['unit']}"
    )

    print(
        f"Expected value: "
        f"{validation_result['expected_value']} "
        f"{validation_result['unit']}"
    )

    print(
        f"Tolerance: "
        f"{validation_result['tolerance_percent']} %"
    )

    print(
        f"Lower limit: "
        f"{validation_result['lower_limit']} "
        f"{validation_result['unit']}"
    )

    print(
        f"Upper limit: "
        f"{validation_result['upper_limit']} "
        f"{validation_result['unit']}"
    )

    print(
        f"Test result: "
        f"{validation_result['result']}"
    )


def print_summary(validation_results):
    total_tests = len(validation_results)

    passed_tests = sum(
        result["result"] == "PASS"
        for result in validation_results
    )

    failed_tests = sum(
        result["result"] == "FAIL"
        for result in validation_results
    )

    if failed_tests == 0:
        overall_result = "PASS"
    else:
        overall_result = "FAIL"

    print("\n===== TEST SUMMARY =====")
    print(f"Total tests: {total_tests}")
    print(f"Passed: {passed_tests}")
    print(f"Failed: {failed_tests}")
    print(f"Overall result: {overall_result}")


if __name__ == "__main__":
    instrument = connect_to_instrument()

    try:
        idn = identify_instrument(
            instrument
        )

        print(
            f"Instrument identification: {idn}"
        )

        measured_voltage = measure_dc_voltage(
            instrument
        )

        measured_current = measure_dc_current(
            instrument
        )

        measured_resistance = measure_resistance(
            instrument
        )

        voltage_result = validate_measurement(
            "DC Voltage",
            measured_voltage,
            5.0,
            2.0,
            "V"
        )

        current_result = validate_measurement(
            "DC Current",
            measured_current,
            0.100,
            5.0,
            "A"
        )

        resistance_result = validate_measurement(
            "Resistance",
            measured_resistance,
            1000.0,
            2.0,
            "Ohm"
        )

        validation_results = [
            voltage_result,
            current_result,
            resistance_result
        ]

        for result in validation_results:
            print_result(
                result
            )

        print_summary(
            validation_results
        )

        save_results_to_csv(
            idn,
            validation_results
        )

    except ValueError as error:
        print(
            f"Measurement error: {error}"
        )

        print(
            "Test result: INSTRUMENT ERROR"
        )

    finally:
        instrument.close()

        print(
            "\nInstrument connection closed."
        )