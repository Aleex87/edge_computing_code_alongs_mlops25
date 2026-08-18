from machine import Pin
from time import sleep

led = Pin(15 , 1)
led_2 = Pin (14 , 1)

led.value(0)
led_2.value(0)
# led.value(1)
# led_2.value(1)

while True:
    secret_num = 6

    number= int(input("insert a number  between 1 and 9"))

    if number == secret_num:
        led_2.value(1)
        led.value(0)
    else:
        led.value(1)
        led_2.value(0)


# while True:
#     led.toggle()
#     sleep(.03)
#     led_2.toggle()
#     sleep(.03)
