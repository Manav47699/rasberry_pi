import paho.mqtt.client as mqtt
from flask import Flask, jsonify
import sqlite3  # <--- NEW: Import Database Library
import datetime

# --- CONFIGURATION ---
BROKER = "localhost"
TOPIC_TEMP = "home/temperature"
TOPIC_HUM  = "home/humidity"

# --- GLOBAL RAM VARS (The Whiteboard) ---
current_data = {
    "temperature": 0.0,
    "humidity": 0.0,
    "last_updated": "Waiting..."
}

# --- DATABASE FUNCTIONS (The Logbook) --- 
def init_db():
    # 1. Open (or create) the notebook file
    conn = sqlite3.connect('iot_data.db', check_same_thread=False)
    c = conn.cursor()
    # 2. Create a table with 3 columns: Time, Temp, Humidity
    c.execute('''CREATE TABLE IF NOT EXISTS readings 
                 (timestamp DATETIME, temperature REAL, humidity REAL)''')
    conn.commit()
    conn.close()

def save_to_db(temp, hum):
    # 1. Open the notebook
    conn = sqlite3.connect('iot_data.db', check_same_thread=False)
    c = conn.cursor()
    # 2. Get current time
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    # 3. Write a new line
    c.execute("INSERT INTO readings (timestamp, temperature, humidity) VALUES (?, ?, ?)", 
              (timestamp, temp, hum))
    conn.commit()
    conn.close()
    print(f"Saved to DB: {timestamp} -> {temp}C, {hum}%")

# --- MQTT LISTENER ---
def on_message(client, userdata, msg):
    payload = msg.payload.decode()
    topic = msg.topic
    
    if topic == TOPIC_TEMP:
        current_data["temperature"] = payload
    elif topic == TOPIC_HUM:
        current_data["humidity"] = payload
        # <--- NEW LOGIC: Only save when we receive Humidity 
        # (Assuming humidity comes slightly after temp, so we have both)
        save_to_db(current_data["temperature"], current_data["humidity"])
        
    current_data["last_updated"] = datetime.datetime.now().strftime("%H:%M:%S")

# --- MAIN SETUP ---
# 1. Create the Database Table immediately
init_db() 

# 2. Start MQTT
client = mqtt.Client()
client.on_message = on_message
client.connect(BROKER, 1883, 60)
client.subscribe([(TOPIC_TEMP, 0), (TOPIC_HUM, 0)])
client.loop_start()

# --- FLASK SERVER ---
app = Flask(__name__)

@app.route('/')
def home():
    return "<h1>Go to <a href='/history'>/history</a> to see the logbook!</h1>"

@app.route('/api/data')
def get_data():
    return jsonify(current_data)

# <--- NEW ROUTE: View History
@app.route('/history')
def get_history():
    conn = sqlite3.connect('iot_data.db')
    c = conn.cursor()
    # Get the last 10 readings, newest first
    c.execute("SELECT * FROM readings ORDER BY rowid DESC LIMIT 10")
    data = c.fetchall()
    conn.close()
    return jsonify(data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5100)
