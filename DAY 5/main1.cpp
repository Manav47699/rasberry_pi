#include <ESP8266WiFi.h>
#include <PubSubClient.h>

//lib_deps = knolleary/PubSubClient@^2.8

const char* WIFI_SSID = "Realme";
const char* WIFI_PASS = "lalit123";

const char* MQTT_BROKER = "10.233.206.247";  // Raspberry Pi IP
const int   MQTT_PORT   = 1883;

const char* TOPIC = "home/esp8266";

WiFiClient espClient;
PubSubClient client(espClient);

void connectWiFi() {
  WiFi.mode(WIFI_STA);
  WiFi.begin(WIFI_SSID, WIFI_PASS);
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
  }
}

void connectMQTT() {
  while (!client.connected()) {
    String clientId = "ESP8266-" + String(ESP.getChipId());
    if (client.connect(clientId.c_str())) {
      // connected
    } else {
      delay(2000);
    }
  }
}

void setup() {
  Serial.begin(115200);
  connectWiFi();

  client.setServer(MQTT_BROKER, MQTT_PORT);
  connectMQTT();
}

void loop() {
  if (!client.connected()) connectMQTT();
  client.loop();

  String msg = "Hello from ESP8266!";
  client.publish(TOPIC, msg.c_str());

  delay(2000);
}

