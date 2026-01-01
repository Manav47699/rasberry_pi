import paho.mqtt.client as mqtt
from flask import Flask, jsonify, render_template
import sqlite3
import datetime

# --- CONFIGURATION ---
BROKER = "localhost"
TOPIC_TEMP = "home/temperature"
TOPIC_HUM  = "home/humidity"
TOPIC_LED  = "home/led"  # New Topic for Control

# --- GLOBAL VARS ---
current_data = {
    "temperature": 0.0,
    "humidity": 0.0,
    "last_updated": "Waiting..."
}

# --- DATABASE SETUP ---
def init_db():
    conn = sqlite3.connect('iot_data.db', check_same_thread=False)
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS readings 
                 (timestamp DATETIME, temperature REAL, humidity REAL)''')
    conn.commit()
    conn.close()

def save_to_db(temp, hum):
    conn = sqlite3.connect('iot_data.db', check_same_thread=False)
    c = conn.cursor()
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    c.execute("INSERT INTO readings (timestamp, temperature, humidity) VALUES (?, ?, ?)", 
              (timestamp, temp, hum))
    conn.commit()
    conn.close()
    print(f"Saved: {temp}C, {hum}%")

# --- MQTT LISTENER ---
def on_message(client, userdata, msg):
    payload = msg.payload.decode()
    topic = msg.topic
    
    if topic == TOPIC_TEMP:
        current_data["temperature"] = payload
    elif topic == TOPIC_HUM:
        current_data["humidity"] = payload
        save_to_db(current_data["temperature"], current_data["humidity"])
        
    current_data["last_updated"] = datetime.datetime.now().strftime("%H:%M:%S")

# --- START MQTT ---
client = mqtt.Client()
client.on_message = on_message
client.connect(BROKER, 1883, 60)
client.subscribe([(TOPIC_TEMP, 0), (TOPIC_HUM, 0)])
client.loop_start()

# --- FLASK APP ---
app = Flask(__name__)

init_db() # Ensure DB exists

# 1. THE HOMEPAGE (Serves the HTML file)
@app.route('/')
def home():
    return render_template('index.html')

# 2. DATA API (Used by JavaScript to update numbers)
@app.route('/api/data')
def get_data():
    return jsonify(current_data)

# 3. LED CONTROL API (Used by JavaScript Buttons)
@app.route('/api/led/<action>')
def control_led(action):
    # Publish to MQTT
    client.publish(TOPIC_LED, action)
    print(f"User clicked: {action}")
    return jsonify({"status": "success", "command": action})

# 4. HISTORY API
@app.route('/history')
def get_history():
    conn = sqlite3.connect('iot_data.db')
    c = conn.cursor()
    c.execute("SELECT * FROM readings ORDER BY rowid DESC LIMIT 10")
    data = c.fetchall()
    conn.close()
    return jsonify(data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5100)
