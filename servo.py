from machine import Pin, PWM
import time
import neopixel

servo_pin = 14
led_pin = 16

pwm = PWM(Pin(servo_pin))
pwm.freq(50)

np = neopixel.NeoPixel(Pin(led_pin), 1)

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

set_angle(1688)
time.sleep(0.1)
set_angle(1792)
time.sleep(1.8)
set_angle(1688)
