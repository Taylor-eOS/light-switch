from machine import Pin, PWM
import time

servo_pin = 14
pwm = PWM(Pin(servo_pin))
pwm.freq(50)

def set_angle(pulse_us):
    period_us = 20000
    duty = int(pulse_us * 65535 // period_us)
    pwm.duty_u16(duty)

set_angle(1790);
time.sleep(2)
set_angle(1660);

