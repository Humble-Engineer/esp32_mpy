# blink.py（MicroPython版本）
import sys

# 添加模块搜索路径（根据实际文件位置调整）
sys.path.append('/modules')  # 假设模块存放在设备的根目录/modules下

try:
    from modules.led import LED  # 直接导入模块（MicroPython会自动搜索sys.path）
except ImportError:
    print("Class LED not found!")
    
def main():
    led = LED(2)  # 根据硬件调整引脚号
    while True:
        led.blink(0.2)

if __name__ == '__main__':
    main()