from machine import Pin
from time import sleep_ms

led = Pin(2, Pin.OUT)

while 1:
    
    led.on()
    sleep_ms(200)
    led.off()
    sleep_ms(200)


