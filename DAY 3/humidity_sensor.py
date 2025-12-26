# temp and humidity sensor ko code
import serial
import time
import datetime

ser = serial.Serial('/dev/ttyUSB0', 115200, timeout=1.0)

time.sleep(3)
ser.reset_input_buffer()

print("Logging DHT11 Data...")

try:
    while True:
        if ser.in_waiting > 0:
            try:
                line = ser.readline().decode('utf-8').rstrip()

                if line == "ERROR":
                    print("Sensor Error on ESP32")
                    continue

                # Parse the CSV data
                if "," in line:
                    temp, hum = line.split(",")
                    timestamp = datetime.datetime.now().strftime("%H:%M:%S")

                    print(f"[{timestamp}] Temp: {temp}C | Humidity: {hum}%")

                    # (Optional) You could save this to a file or database here

            except ValueError:
                print("Data packet corrupted")

except KeyboardInterrupt:
    print("Stop logging")
    ser.close()
