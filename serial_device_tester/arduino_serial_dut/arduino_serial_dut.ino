String command;

void setup() {
    Serial.begin(115200);
}

void loop() {
    if (Serial.available() > 0) {
        command = Serial.readStringUntil('\n');
        command.trim();

        if (command == "GET_STATUS") {
            Serial.println("STATUS:OK");
        }
        else if (command == "GET_VERSION") {
            Serial.println("VERSION:1.0");
        }
        else if (command == "Hi") {
            Serial.println("Hallo");
        }
    }
}