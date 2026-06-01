from machine import Pin, PWM
import time

pwm = PWM(Pin(14), freq=50)

def us(x):
    pwm.duty_ns(x * 1000)

us(700)
time.sleep(5)

us(2300)
time.sleep(5)

us(1500)
