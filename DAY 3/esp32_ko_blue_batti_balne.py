# battibalne esp32 ko
import serial
import time

try:
    ser = serial.Serial('/dev/ttyUSB0', 115200, timeout= 1.0)
    time.sleep(3)
    ser.reset_input_buffer()

    while True:
        cmd = input ("enter command:")

        if cmd == "q":
            break

        ser.write((cmd + '\n').encode('utf-8'))
        time.sleep(0.01)


        while ser.in_waiting > 0:
            response = ser.readline().decode('utf-8').rstrip()
            print(f"esp32 sent is : {response}")


except KeyboardInterrupt:
    print("exiting")

except serial.SerialException as e:
    print(e)

finally:
    if 'ser' in locals() and ser.is_open:
        ser.close()