import csv
import os
from datetime import datetime


def validate_measurement(
    measurement_name,
    expected_value,
    measured_value,
    tolerance_percent,
    unit
):
    tolerance_value = abs(expected_value) * tolerance_percent / 100

    lower_limit = expected_value - tolerance_value
    upper_limit = expected_value + tolerance_value

    if lower_limit <= measured_value <= upper_limit:
        result = "PASS"
    else:
        result = "FAIL"

    measurement_result = {
        "measurement": measurement_name,
        "expected_value": expected_value,
        "measured_value": measured_value,
        "tolerance_percent": tolerance_percent,
        "tolerance_value": tolerance_value,
        "lower_limit": lower_limit,
        "upper_limit": upper_limit,
        "unit": unit,
        "result": result
    }

    return measurement_result


def print_measurement_result(measurement_result):
    print("\n--- Measurement Result ---")

    print(
        f"Measurement: "
        f"{measurement_result['measurement']}"
    )

    print(
        f"Expected: "
        f"{measurement_result['expected_value']:.2f} "
        f"{measurement_result['unit']}"
    )

    print(
        f"Measured: "
        f"{measurement_result['measured_value']:.2f} "
        f"{measurement_result['unit']}"
    )

    print(
        f"Tolerance: "
        f"{measurement_result['tolerance_percent']:.2f} %"
    )

    print(
        f"Allowed Range: "
        f"{measurement_result['lower_limit']:.2f} "
        f"{measurement_result['unit']} - "
        f"{measurement_result['upper_limit']:.2f} "
        f"{measurement_result['unit']}"
    )

    print(
        f"Result: "
        f"{measurement_result['result']}"
    )


def get_float_input(prompt):
    while True:
        try:
            value = float(input(prompt))
            return value

        except ValueError:
            print(
                "Invalid input. Please enter a number."
            )


def get_integer_input(prompt):
    while True:
        try:
            value = int(input(prompt))

            if value > 0:
                return value

            else:
                print(
                    "Please enter a positive integer."
                )

        except ValueError:
            print(
                "Invalid input. Please enter an integer."
            )


def get_non_negative_float_input(prompt):
    while True:
        try:
            value = float(input(prompt))

            if value >= 0:
                return value

            else:
                print(
                    "Please enter zero or a positive number."
                )

        except ValueError:
            print(
                "Invalid input. Please enter a number."
            )


def print_test_summary(test_results):
    total_tests = len(test_results)

    passed_tests = 0
    failed_tests = 0

    for measurement_result in test_results:

        if measurement_result["result"] == "PASS":
            passed_tests += 1

        else:
            failed_tests += 1

    if failed_tests == 0:
        overall_result = "PASS"

    else:
        overall_result = "FAIL"

    print("\n========== TEST SUMMARY ==========")

    print(f"Total Tests: {total_tests}")
    print(f"Passed: {passed_tests}")
    print(f"Failed: {failed_tests}")
    print(f"Overall Result: {overall_result}")


def save_results_to_csv(
    test_results,
    filename
):
    with open(
        filename,
        "w",
        newline=""
    ) as file:

        writer = csv.DictWriter(
            file,
            fieldnames=test_results[0].keys()
        )

        writer.writeheader()
        writer.writerows(test_results)

    full_path = os.path.abspath(filename)

    print(
        f"\nResults saved to: {full_path}"
    )


def main():

    test_results = []

    number_of_tests = get_integer_input(
        "How many measurements do you want to test? "
    )

    for test_number in range(number_of_tests):

        print(
            f"\n--- Test {test_number + 1} ---"
        )

        measurement_name = input(
            "Enter measurement name: "
        )

        expected_value = get_float_input(
            "Enter expected value: "
        )

        measured_value = get_float_input(
            "Enter measured value: "
        )

        tolerance_percent = get_non_negative_float_input(
            "Enter tolerance percentage: "
        )

        unit = input(
            "Enter measurement unit: "
        )

        measurement_result = validate_measurement(
            measurement_name,
            expected_value,
            measured_value,
            tolerance_percent,
            unit
        )

        test_results.append(
            measurement_result
        )

    print(
        "\n========== TEST REPORT =========="
    )

    for measurement_result in test_results:

        print_measurement_result(
            measurement_result
        )

    print_test_summary(
        test_results
    )

    current_time = datetime.now()

    timestamp = current_time.strftime(
        "%Y-%m-%d_%H%M%S"
    )

    filename = (
        f"measurement_results_{timestamp}.csv"
    )

    save_results_to_csv(
        test_results,
        filename
    )


if __name__ == "__main__":
    main()