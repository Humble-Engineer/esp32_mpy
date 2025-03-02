import machine
import os
import sdcard
from machine import SPI, Pin

class TF_Card:
    def __init__(self):
        # 配置SPI引脚（根据用户指定参数）
        self.spi = SPI(
            1,  # 使用SPI1（VSPI）
            baudrate=8000000,  # 初始频率8MHz
            sck=Pin(14),       # SCK引脚
            mosi=Pin(26),      # MOSI引脚
            miso=Pin(27),      # MISO引脚
            polarity=0,
            phase=0
        )
        
        # 初始化SD卡
        self.cs = Pin(13, Pin.OUT)  # 片选引脚
        self.sd = sdcard.SDCard(self.spi, self.cs)
        
        # 挂载文件系统
        try:
            os.mount(self.sd, '/sd')
            print("SD卡挂载成功")
            # 添加SD卡路径到系统（可选）
            sys.path.append('/sd')
        except OSError as e:
            print("挂载失败:", e)

    def list_files(self, path="/sd"):
        """列出SD卡文件"""
        return os.listdir(path)

    def read_file(self, filename):
        """读取文件内容"""
        with open('/sd/' + filename, 'r') as f:
            return f.read()

    def write_file(self, filename, content):
        """写入文件"""
        with open('/sd/' + filename, 'w') as f:
            f.write(content)

# 使用示例
if __name__ == "__main__":
    # 初始化TF卡
    tf = TF_Card()
    
    # 测试写入和读取
    tf.write_file("test.txt", "Hello ESP32 SD Card!")
    print("文件内容：", tf.read_file("test.txt"))
    
    # 列出根目录文件
    print("SD卡文件列表：", tf.list_files())