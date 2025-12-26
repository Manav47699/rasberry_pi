//these libraries only work when you paste the link in platformio.ini file which appers while making a new project with platformio extension.
// you will find these libraries link here -> https://registry.platformio.org/
//yo code esp32 ma halne ani esp32 lai rasberry ma connect garne ani vnc kholera thoung ma python code run garne
#include <ESP32Servo.h>
#include "DHT11.h"

#define DHTPIN 4
#define DHTTYPE DHT11
#define SERVO_PIN 13

DHT11 dht(DHTPIN);
Servo myServo;

// Timer variables for non-blocking delay
unsigned long previousMillis = 0;
const long interval = 2000; // Read sensor every 2000ms (2 seconds)

void setup() {
  Serial.begin(115200);
  myServo.attach(SERVO_PIN);
  myServo.write(0); // Start position (Fan Off)
}

void loop() {
  unsigned long currentMillis = millis();

  // --- TASK 1: Read Sensor (every 2 seconds) ---
  if (currentMillis - previousMillis >= interval) {
    previousMillis = currentMillis;

    float h = dht.readHumidity();
    float t = dht.readTemperature();

    if (!isnan(h) && !isnan(t)) {
      // Send: "24.5,60"
      Serial.print(t);
      Serial.print(",");
      Serial.println(h);
    }
  }

  // --- TASK 2: Listen for Servo Commands (Always running) ---
  if (Serial.available() > 0) {
    String command = Serial.readStringUntil('\n');
    command.trim(); // Clean up whitespace

    if (command == "FAN_ON") {
      myServo.write(180); // Move servo to "On" position
    } 
    else if (command == "FAN_OFF") {
      myServo.write(0);   // Move servo to "Off" position
    }
  }
}
