import pytest

from measurement_validator import validate_measurement


@pytest.mark.parametrize(
    "measurement_name, expected_value, measured_value, tolerance_percent, unit, expected_result",
    [
        ("Voltage", 5.0, 4.95, 2.0, "V", "PASS"),
        ("Voltage", 5.0, 4.80, 2.0, "V", "FAIL"),

        ("Current", 2.0, 1.99, 1.0, "A", "PASS"),
        ("Current", 2.0, 1.90, 1.0, "A", "FAIL"),

        ("Resistance", 1000.0, 1010.0, 2.0, "Ohm", "PASS"),
        ("Resistance", 1000.0, 1030.0, 2.0, "Ohm", "FAIL"),
    ]
)
def test_measurement_results(
    measurement_name,
    expected_value,
    measured_value,
    tolerance_percent,
    unit,
    expected_result
):
    result = validate_measurement(
        measurement_name,
        expected_value,
        measured_value,
        tolerance_percent,
        unit
    )

    assert result["result"] == expected_result


@pytest.mark.parametrize(
    "measured_value, expected_result",
    [
        (4.89, "FAIL"),
        (4.90, "PASS"),
        (5.10, "PASS"),
        (5.11, "FAIL"),
    ]
)
def test_voltage_boundaries(
    measured_value,
    expected_result
):
    result = validate_measurement(
        "Voltage",
        5.0,
        measured_value,
        2.0,
        "V"
    )

    assert result["result"] == expected_result


def test_zero_tolerance_pass():
    result = validate_measurement(
        "Voltage",
        5.0,
        5.0,
        0.0,
        "V"
    )

    assert result["result"] == "PASS"


def test_voltage_calculation():
    result = validate_measurement(
        "Voltage",
        5.0,
        4.95,
        2.0,
        "V"
    )

    assert result["tolerance_value"] == pytest.approx(0.1)
    assert result["lower_limit"] == pytest.approx(4.9)
    assert result["upper_limit"] == pytest.approx(5.1)