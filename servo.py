from machine import Pin, PWM
import time
import neopixel

servo_pin = 14
led_pin = 16
pir_pin = 12
on_value = 1792
off_value = 1688
pwm = PWM(Pin(servo_pin))
pwm.freq(50)
np = neopixel.NeoPixel(Pin(led_pin), 1)
pir = Pin(pir_pin, Pin.IN)
previous_state = 0

def blink_status():
    np[0] = (0, 40, 0)
    np.write()
    time.sleep(0.08)
    np[0] = (0, 0, 0)
    np.write()
    time.sleep(0.12)

def set_angle(pulse_us):
    period_us = 20000
    duty = int(pulse_us * 65535 // period_us)
    pwm.duty_u16(duty)
    blink_status()

print("Motion-activated switch ready")
set_angle(off_value)

while True:
    current = pir.value()
    if current == 1 and previous_state == 0:
        print("New motion detected at", time.ticks_ms())
        set_angle(off_value)
        time.sleep(0.1)
        set_angle(on_value)
        time.sleep(1.8)
        set_angle(off_value)
        previous_state = 1
    if current == 0:
        previous_state = 0
    time.sleep_ms(20)

