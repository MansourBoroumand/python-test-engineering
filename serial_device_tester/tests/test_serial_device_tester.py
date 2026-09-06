import pytest

from serial_device_tester.serial_device_tester import (
    validate_response,
    read_response,
    send_command
)

class FakeSerialConnection:
    def __init__(self, response=b""):
        self.response = response
        self.written_data = None

    def readline(self):
        return self.response

    def write(self, data):
        self.written_data = data

@pytest.mark.parametrize(
    "actual_response, expected_response, expected_result",
    [
        ("STATUS:OK", "STATUS:OK", "PASS"),
        ("STATUS:ERROR", "STATUS:OK", "FAIL"),
        ("VERSION:1.0", "VERSION:1.0", "PASS"),
        ("VERSION:2.0", "VERSION:1.0", "FAIL"),
        ("PONG", "PONG", "PASS"),
        ("Hallo", "Hallo", "PASS"),
        ("Hello", "Hallo", "FAIL"),
    ]
)
def test_validate_response(
    actual_response,
    expected_response,
    expected_result
):
    result = validate_response(
        actual_response,
        expected_response
    )

    assert result == expected_result

def test_read_response_with_data():
    fake_connection = FakeSerialConnection(
        b"STATUS:OK\r\n"
    )

    result = read_response(
        fake_connection
    )

    assert result == "STATUS:OK"


def test_read_response_timeout():
    fake_connection = FakeSerialConnection(
        b""
    )

    result = read_response(
        fake_connection
    )

    assert result is None

def test_send_command():
    fake_connection = FakeSerialConnection()

    send_command(
        fake_connection,
        "GET_STATUS"
    )

    assert fake_connection.written_data == b"GET_STATUS\n"