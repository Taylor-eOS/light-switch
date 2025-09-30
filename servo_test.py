from machine import Pin, PWM
import time

servo_pin = 14
pwm = PWM(Pin(servo_pin))
pwm.freq(50)

def set_angle_us(pulse_us):
    period_us = 20000
    duty = int(pulse_us * 65535 // period_us)
    pwm.duty_u16(duty)

#one end
set_angle_us(500)
time.sleep(1)

set_angle_us(1000)
time.sleep(1)

set_angle_us(1500)
time.sleep(1)

set_angle_us(2000)
time.sleep(1)

#other end
set_angle_us(2500)
time.sleep(1)
