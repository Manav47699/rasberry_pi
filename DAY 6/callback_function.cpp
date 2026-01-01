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