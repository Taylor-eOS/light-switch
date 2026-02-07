from machine import Pin, PWM
import time
import neopixel

servo_pin = 14
led_pin = 16
pir_pin = 12
on_value = 1792
off_value = 1688
timeout_seconds = 15.0
pwm = PWM(Pin(servo_pin))
pwm.freq(50)
np = neopixel.NeoPixel(Pin(led_pin), 1)
pir = Pin(pir_pin, Pin.IN)
previous_state = 0
last_motion_time = 0
is_on = False

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

def turn_on():
    global is_on
    if not is_on:
        set_angle(off_value)
        time.sleep(0.1)
        set_angle(on_value)
        is_on = True
        print("Light ON")

def turn_off():
    global is_on
    if is_on:
        set_angle(off_value)
        is_on = False
        print("Light OFF")

print("Motion presence light ready")
turn_off()
while True:
    current = pir.value()
    now = time.ticks_ms()
    if current == 1:
        last_motion_time = now
        turn_on()
    if current == 0 and previous_state == 1:
        print("Sensor went low at", now)
    previous_state = current
    if is_on and current == 0:
        elapsed = time.ticks_diff(now, last_motion_time) / 1000.0
        if elapsed > timeout_seconds:
            turn_off()
    time.sleep_ms(50)

