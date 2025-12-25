from gpiozero import LED, Button
from signal import pause

led = LED(17)
btn = Button(26)

btn.when_pressed = led.toggle

pause()