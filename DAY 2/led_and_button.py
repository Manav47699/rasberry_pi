from gpiozero import Button, LED
from time import sleep

btn = Button(26)

led = LED(17)

while True:
    if btn.is_pressed:
        print ("button is pressed")
        led.on()
    else:
        print ("button is released")
        
        

    


