import time
from machine import PWM, Pin

time.sleep(0.1)

MAX_U16 = 2**16 - 1

led_ref = Pin(14, Pin.OUT)
led_ref.value(1)

led_pwm = PWM(Pin(15))
led_pwm.freq(1000)

button = Pin(11, Pin.IN, Pin.PULL_UP)

buzzer = PWM(Pin(7))


while True:

    if button.value() == 0:
        print("Button is pressed")

        # Rising alarm
        for freq in [500, 700, 900, 1100, 1300]:
            buzzer.freq(freq)
            buzzer.duty_u16(30000)
            time.sleep(0.15)

        # Turn buzzer off
        buzzer.duty_u16(0)

        # LED fade in
        for i in range(101):
            led_pwm.duty_u16(int(MAX_U16 * i / 100))
            time.sleep(0.02)

        # LED fade out
        for i in range(99, -1, -1):
            led_pwm.duty_u16(int(MAX_U16 * i / 100))
            time.sleep(0.02)

        # Wait until button is released
        while button.value() == 0:
            time.sleep(0.01)

    time.sleep(0.01)
    