# 测试显示，只有中间那个靠谱

from machine import Pin
import time

Pin_M = Pin(32, Pin.IN, Pin.PULL_UP)

while True:
    
    # 读取数字量输入状态
    input_state = Pin_M.value()
    # 打印当前状态
    print("Input State:", input_state)
    # 延时0.1秒（可根据需要调整）
    time.sleep(0.5)