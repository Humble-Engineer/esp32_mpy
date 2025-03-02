from machine import Pin
import time

switch = Pin(32, Pin.IN, Pin.PULL_UP)
last_trigger = 0  # 新增防抖时间戳

def handle_interrupt(pin):
    global last_trigger
    now = time.ticks_ms()
    
    # 200ms防抖判断
    if time.ticks_diff(now, last_trigger) > 200:
        last_trigger = now
        t = time.localtime()
        print(f"[{t[3]:02}:{t[4]:02}:{t[5]:02}] 有效触发")

switch.irq(trigger=Pin.IRQ_RISING, handler=handle_interrupt)

print("GPIO32 防抖监控已启动")
try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    print("监控已停止")