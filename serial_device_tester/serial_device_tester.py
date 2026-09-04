import serial
import serial.tools.list_ports
import time

def list_serial_ports():
    ports = serial.tools.list_ports.comports()

    if not ports:
        print("No serial ports found.")
        return

    print("Available serial ports:")

    for port in ports:
        print(f"{port.device} - {port.description}")

def open_serial_port(port_name, baud_rate):
    try:
        ser = serial.Serial(
            port=port_name,
            baudrate=baud_rate,
            timeout=1
        )

        time.sleep(2)

        print("Serial port opened successfully.")
        return ser

    except serial.SerialException as error:
        print(f"Failed to open serial port: {error}")
        return None


def send_command(connection, command):
    message = command + "\n"

    connection.write(
        message.encode()
    )

    print(f"Command sent: {command}")

def read_response(connection):
    response = connection.readline()

    decoded_response = response.decode().strip()

    print(f"Response received: {decoded_response}")

    return decoded_response

def validate_response(
    actual_response,
    expected_response
):
    if actual_response == expected_response:
        result = "PASS"
    else:
        result = "FAIL"

    print(f"Expected response: {expected_response}")
    print(f"Actual response:   {actual_response}")
    print(f"Test result:       {result}")

    return result


if __name__ == "__main__":
    list_serial_ports()

    connection = open_serial_port(
        "COM3",
        115200
    )

    if connection is not None:
        try:
            print("Ready for communication.")

            send_command(
                connection,
                "GET_STATUS"
            )

            response = read_response(
                connection
            )

            validate_response(
                response,
                "STATUS:OK"
            )

        finally:
            connection.close()
            print("Serial port closed.")