#include <WiFi.h>

/* WiFi Credentials */
const char* ssid = "department";
const char* password = "00000000";

/* PIR Sensor Pin */
#define PIR_PIN 4

void setup() {
  Serial.begin(115200);
  pinMode(PIR_PIN, INPUT);

  /* Connect to WiFi */
  Serial.print("Connecting to WiFi");
  WiFi.begin(ssid, password);

  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }

  Serial.println("\nWiFi Connected!");
  Serial.print("ESP32 IP Address: ");
  Serial.println(WiFi.localIP());
}

void loop() {
  int motion = digitalRead(PIR_PIN);

  if (motion == HIGH) {
    Serial.println("🚨 Motion Detected!");
    delay(2000);   // prevent repeated triggers
  } else {
    Serial.println("No motion");
  }

  delay(1000);
}