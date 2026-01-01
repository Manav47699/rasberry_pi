from flask import Flask, render_template
import paho.mqtt.client as mqtt
from picamzero import Camera
from datetime import datetime
import os

# -------- CONFIG --------
BROKER = "localhost"
TOPIC = "home/pir"

app = Flask(__name__)
cam = Camera()

# Absolute path to project capture folder
HOME_DIR = os.environ['HOME']
CAPTURE_DIR = os.path.join(HOME_DIR, "thief-detection", "static", "captures")
os.makedirs(CAPTURE_DIR, exist_ok=True)  # ensure folder exists

images = []  # newest image first

# -------- MQTT CALLBACK --------
def on_message(client, userdata, msg):
    if msg.payload.decode() == "MOTION":
        now = datetime.now()
        timestamp = now.strftime("%Y-%m-%d_%H-%M-%S")
        filename = f"intruder_{timestamp}.jpg"
        filepath = os.path.join(CAPTURE_DIR, filename)

        try:
            cam.start_preview()
            cam.annotate(now.strftime("%Y-%m-%d %H:%M:%S"))  # timestamp overlay
            cam.take_photo(filepath)
            cam.stop_preview()
            images.insert(0, filename)
            print(f"Captured with timestamp: {filename}")
        except Exception as e:
            print(f"Camera error: {e}")

# -------- MQTT SETUP --------
mqtt_client = mqtt.Client()
mqtt_client.on_message = on_message
mqtt_client.connect(BROKER, 1883, 60)
mqtt_client.subscribe(TOPIC)
mqtt_client.loop_start()

# -------- FLASK ROUTE --------
@app.route("/")
def home():
    return render_template("index.html", images=images)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

