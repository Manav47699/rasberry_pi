from gpiozero import LED
from signal import pause

red = LED(17)

print ("Blinking running in background")
red.blink(on_time =0.5, off_time = 0.5)

pause()