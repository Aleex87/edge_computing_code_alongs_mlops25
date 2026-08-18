from machine import Pin
from time import sleep

sleep(1) # 1 mean 1 second

led_interal = Pin("LED", 1)

led_interal.value(1)

sleep(2)

led_interal.value(0)

    