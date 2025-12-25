from gpiozero import LED
from time import sleep

led = PwMLED(17)

led.value = 0.5
sleep(2)

while True:
    for bightness in range(0, 100):
        led.value = bightness/100.0
        sleep(0.01)
