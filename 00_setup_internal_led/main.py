from machine import Pin
from time import sleep

sleep(1) # 1 mean 1 second

led_interal = Pin("LED", 1)

while True:
    led_interal.toggle()
    sleep(.5)
    
