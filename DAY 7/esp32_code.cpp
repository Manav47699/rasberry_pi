#include <WiFi.h>
#include <PubSubClient.h>

#define PIR_PIN 4

const char* ssid = "arcs";  #your hotspot
const char* password = "88888888";     #pass
const char* mqtt_server = "10.36.16.213"; 

WiFiClient espClient;
PubSubClient client(espClient);

void setup_wifi() {
  WiFi.begin(ssid, password);
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
  }
}

void setup() {
  Serial.begin(115200);
  pinMode(PIR_PIN, INPUT);

  setup_wifi();
  client.setServer(mqtt_server, 1883);
}

void loop() {
  if (!client.connected()) {
    client.connect("ESP32_PIR");
  }
  client.loop();

  if (digitalRead(PIR_PIN) == HIGH) {
    Serial.println("Motion detected!");
    client.publish("home/pir", "MOTION");
    delay(5000);  // avoid spamming
  }
}
