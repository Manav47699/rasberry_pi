#include <Arduino.h>
#include <PubSubClient.h>
#include <WiFi.h>
#include <DHT11.h>


// --- CONFIGURATION ---
const char* ssid = "pi-wifi";
const char* password = "analog1010";
const char* mqtt_server = "10.64.31.33"; // YOUR PI IP ADDRESS

#define DHTPIN 4
#define DHTTYPE DHT11

// --- OBJECTS ---
WiFiClient espClient;
PubSubClient client(espClient);
DHT11 dht(DHTPIN);

// --- VARIABLES ---
unsigned long previousMillis = 0;
const long interval = 2000; // Send data every 2 seconds

void setup_wifi() {
  delay(10);
  Serial.print("Connecting to ");
  Serial.println(ssid);
  WiFi.begin(ssid, password);
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }
  Serial.println("\nWiFi connected");
}

void reconnect() {
  while (!client.connected()) {
    Serial.print("Attempting MQTT connection...");
    // Random ID to prevent conflicts
    String clientId = "ESP32-Sender-" + String(random(0xffff), HEX);
    
    if (client.connect(clientId.c_str())) {
      Serial.println("connected");
    } else {
      Serial.print("failed, rc=");
      Serial.print(client.state());
      delay(5000);
    }
  }
}

void setup() {
  Serial.begin(115200);
  setup_wifi();
  client.setServer(mqtt_server, 1883);
}

void loop() {
  if (!client.connected()) {
    reconnect();
  }
  client.loop();

  // Non-blocking timer
  unsigned long currentMillis = millis();
  if (currentMillis - previousMillis >= interval) {
    previousMillis = currentMillis;

    // 1. Read Sensor
    float h = dht.readHumidity();
    float t = dht.readTemperature();

    // 2. Check for errors
    if (isnan(h) || isnan(t)) {
      Serial.println("Failed to read from DHT sensor!");
      return;
    }
    // 3. Convert numbers to text (String)
    char tempStr[8];
    char humStr[8];
    dtostrf(t, 1, 2, tempStr); // 12.345 -> "12.35"
    dtostrf(h, 1, 2, humStr);

    // 4. Publish to Broker
    client.publish("home/temperature", tempStr);
    client.publish("home/humidity", humStr);

    Serial.print("Sent -> Temp: ");
    Serial.print(tempStr);
    Serial.print(" | Hum: ");
    Serial.println(humStr);
  }
}
