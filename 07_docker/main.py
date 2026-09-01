from wifi import connect_wifi
from machine import Pin 
from time import sleep

sleep(.5)

status_led = Pin(15, Pin.OUT)
connect_wifi(1)

if connect_wifi():
    status_led.value(1)


print(connect_wifi())


