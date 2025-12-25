from gpiozero import MotionSensor, LED
from signal import pause

pir = MotionSensor(26)

led = LED(17)

def motion_detected():
    print("alaram!!!!!")
    led.on()

def motion_stopped():
    print("area is clear :::))")
    led.off()

print ("system aramed")
pir.when_motion = motion_detected
pir.when_no_motion = motion_stopped

pause()