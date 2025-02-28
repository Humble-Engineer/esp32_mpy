from machine import Pin  # type: ignore
from time import sleep

class LED:
    def __init__(self, pin):
        self.pin = Pin(pin, Pin.OUT)
    
    def blink(self, time):
        self.pin.value(1)
        sleep(time)
        self.pin.value(0)
        sleep(time)

if __name__ == "__main__":
    
    # 将led作为LED类的实例化对象，引脚为2号
    led = LED(2)

    # 调用LED类中的blink方法，时间间隔为1秒
    while 1:
        led.blink(2)
