import machine
import time

SIG_PIN = 15
DEBOUNCE_MS = 50
POLL_MS = 50
USE_IRQ = True

_last_event_ts = 0
_last_event_state = None
_event_pending = False

def _irq_handler(pin):
    global _last_event_ts, _last_event_state, _event_pending
    _last_event_ts = time.ticks_ms()
    _last_event_state = pin.value()
    _event_pending = True

def main():
    global _last_event_ts, _last_event_state, _event_pending
    pin = machine.Pin(SIG_PIN, machine.Pin.IN)
    try:
        if USE_IRQ:
            pin.irq(trigger=machine.Pin.IRQ_RISING | machine.Pin.IRQ_FALLING, handler=_irq_handler)
            irq_enabled = True
        else:
            irq_enabled = False
    except Exception:
        irq_enabled = False
    prev_state = pin.value()
    last_print_ts = time.ticks_ms()
    print("TTP223 test starting on GPIO", SIG_PIN, "irq", irq_enabled, "debounce_ms", DEBOUNCE_MS)
    while True:
        now = time.ticks_ms()
        if irq_enabled:
            if _event_pending:
                if time.ticks_diff(now, _last_event_ts) >= DEBOUNCE_MS:
                    if _last_event_state != prev_state:
                        prev_state = _last_event_state
                        print("touch" if prev_state else "release", "at", now)
                    _event_pending = False
            time.sleep_ms(POLL_MS)
        else:
            cur = pin.value()
            if cur != prev_state:
                if time.ticks_diff(now, last_print_ts) >= DEBOUNCE_MS:
                    prev_state = cur
                    last_print_ts = now
                    print("touch" if cur else "release", "at", now)
            time.sleep_ms(POLL_MS)

main()

