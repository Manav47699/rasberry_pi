from gpiozero import LED
from time import sleep

red = LED(17)

print ("light on")
red.on()
sleep(2)

print ("led off")

red.off()