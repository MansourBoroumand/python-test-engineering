import pytest

from instrument_automation.instrument_tester import (
    identify_instrument,
    measure_dc_voltage,
    measure_dc_current,
    measure_resistance,
    validate_measurement,
    save_results_to_csv
)


class FakeInstrument:
    def __init__(
        self,
        idn_response=None,
        voltage_response=None,
        current_response=None,
        resistance_response=None
    ):
        self.idn_response = idn_response
        self.voltage_response = voltage_response
        self.current_response = current_response
        self.resistance_response = resistance_response
        self.last_query = None

    def query(self, command):
        self.last_query = command

        if command == "*IDN?":
            return self.idn_response

        if command == "MEAS:VOLT:DC?":
            return self.voltage_response

        if command == "MEAS:CURR:DC?":
            return self.current_response

        if command == "MEAS:RES?":
            return self.resistance_response

        return ""


@pytest.mark.parametrize(
    "measured_value, expected_value, tolerance_percent, expected_result",
    [
        (5.0, 5.0, 2.0, "PASS"),
        (5.012, 5.0, 2.0, "PASS"),
        (4.9, 5.0, 2.0, "PASS"),
        (5.1, 5.0, 2.0, "PASS"),
        (4.89, 5.0, 2.0, "FAIL"),
        (5.11, 5.0, 2.0, "FAIL"),
    ]
)
def test_validate_measurement(
    measured_value,
    expected_value,
    tolerance_percent,
    expected_result
):
    result = validate_measurement(
        "DC Voltage",
        measured_value,
        expected_value,
        tolerance_percent,
        "V"
    )

    assert result["result"] == expected_result


def test_identify_instrument():
    fake_instrument = FakeInstrument(
        idn_response="SIMULATED,DMM,001,1.0\n"
    )

    result = identify_instrument(
        fake_instrument
    )

    assert result == "SIMULATED,DMM,001,1.0"
    assert fake_instrument.last_query == "*IDN?"


def test_measure_dc_voltage():
    fake_instrument = FakeInstrument(
        voltage_response="5.012\n"
    )

    result = measure_dc_voltage(
        fake_instrument
    )

    assert result == pytest.approx(5.012)
    assert fake_instrument.last_query == "MEAS:VOLT:DC?"


def test_measure_dc_voltage_invalid_response():
    fake_instrument = FakeInstrument(
        voltage_response="ERROR\n"
    )

    with pytest.raises(ValueError):
        measure_dc_voltage(
            fake_instrument
        )

def test_save_results_to_csv(tmp_path, monkeypatch):
    validation_results = [
        {
            "measurement": "DC Voltage",
            "measured_value": 5.012,
            "expected_value": 5.0,
            "tolerance_percent": 2.0,
            "lower_limit": 4.9,
            "upper_limit": 5.1,
            "unit": "V",
            "result": "PASS"
        }
    ]

    instrument_id = "SIMULATED,DMM,001,1.0"

    monkeypatch.chdir(tmp_path)

    save_results_to_csv(
        instrument_id,
        validation_results
    )

    csv_files = list(
        tmp_path.glob("instrument_results_*.csv")
    )

    assert len(csv_files) == 1

    csv_content = csv_files[0].read_text(
        encoding="utf-8"
    )

    assert "instrument_id" in csv_content
    assert "SIMULATED,DMM,001,1.0" in csv_content
    assert "measurement" in csv_content
    assert "DC Voltage" in csv_content
    assert "5.012" in csv_content
    assert "V" in csv_content
    assert "PASS" in csv_content

def test_measure_dc_current():
    fake_instrument = FakeInstrument(
        current_response="0.102\n"
    )

    result = measure_dc_current(
        fake_instrument
    )

    assert result == pytest.approx(0.102)
    assert fake_instrument.last_query == "MEAS:CURR:DC?"


def test_measure_resistance():
    fake_instrument = FakeInstrument(
        resistance_response="998.5\n"
    )

    result = measure_resistance(
        fake_instrument
    )

    assert result == pytest.approx(998.5)
    assert fake_instrument.last_query == "MEAS:RES?"