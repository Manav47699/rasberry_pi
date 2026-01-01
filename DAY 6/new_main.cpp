#include <Arduino.h>
#include <WiFi.h>
#include <PubSubClient.h>
#include <DHT11.h>

// --- CONFIGURATION ---
const char* ssid = "pi-wifi";
const char* password = "analog1010";
const char* mqtt_server = "10.64.31.33"; // YOUR PI IP ADDRESS

#define DHTPIN 4
#define DHTTYPE DHT11
#define LED_PIN 2  // The pin we want to control

// --- OBJECTS ---
WiFiClient espClient;
PubSubClient client(espClient);
DHT11 dht(DHTPIN);

// --- VARIABLES ---
unsigned long previousMillis = 0;
const long interval = 2000; 

// ==========================================
//  1. THE CALLBACK (The Listener)
//  This runs AUTOMATICALLY when a message arrives
// ==========================================
void callback(char* topic, byte* payload, unsigned int length) {
  String message = "";
  for (int i = 0; i < length; i++) {
    message += (char)payload[i];
  }

  Serial.print("Message arrived [");
  Serial.print(topic);
  Serial.print("]: ");
  Serial.println(message);

  // Control Logic
  if (String(topic) == "home/led") {
    if (message == "ON") {
      digitalWrite(LED_PIN, HIGH);
      Serial.println("Action: Light ON");
    } 
    else if (message == "OFF") {
      digitalWrite(LED_PIN, LOW);
      Serial.println("Action: Light OFF");
    }
  }
}

void setup_wifi() {
  delay(10);
  Serial.println();
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
    String clientId = "ESP32-FullStack-" + String(random(0xffff), HEX);
    
    if (client.connect(clientId.c_str())) {
      Serial.println("connected");
      // *** IMPORTANT: Subscribe to the topic here ***
      client.subscribe("home/led"); 
    } else {
      Serial.print("failed, rc=");
      Serial.print(client.state());
      delay(5000);
    }
  }
}

void setup() {
  Serial.begin(115200);
  pinMode(LED_PIN, OUTPUT); // Configure LED pin
  
  setup_wifi();
  client.setServer(mqtt_server, 1883);
  client.setCallback(callback); // Register the listener function
}

void loop() {
  if (!client.connected()) {
    reconnect();
  }
  client.loop(); // Checks for incoming messages

  // --- SENSOR LOGIC (Same as Phase 1) ---
  unsigned long currentMillis = millis();
  if (currentMillis - previousMillis >= interval) {
    previousMillis = currentMillis;

    float h = dht.readHumidity();
    float t = dht.readTemperature();

    if (!isnan(h) && !isnan(t)) {
      char tempStr[8];
      char humStr[8];
      dtostrf(t, 1, 2, tempStr);
      dtostrf(h, 1, 2, humStr);

      client.publish("home/temperature", tempStr);
      client.publish("home/humidity", humStr);
    }
  }
}