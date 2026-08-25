import time
from machine import PWM, Pin

time.sleep(0.1)

MAX_U16 = 2**16

led_ref = Pin(14, Pin.OUT)
led_ref.value(1)

led_pwm = PWM(Pin(15))
led_pwm.freq(1000)

while True:
    for i in range(101):
        led_pwm.duty_u16(int(MAX_U16 * i / 100))
        time.sleep(0.02)

    for i in range(99, -1, -1):
        led_pwm.duty_u16(int(MAX_U16 * i / 100))
        time.sleep(0.02)
