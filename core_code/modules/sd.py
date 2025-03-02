import machine
import os
import uos
import time

def init_sd_card():
    """
    初始化SD卡（SPI模式）
    引脚配置基于常见ESP32开发板：
    - ESP32-WROOM: SCK=14, MOSI=13, MISO=12 (需要根据实际型号调整)
    - ESP32-S3:    SCK=36, MOSI=35, MISO=37
    """
    try:
        # 初始化SD卡（直接通过SDCard类配置）
        sd = machine.SDCard(
            slot=1,          # SPI模式使用slot=1
            sck=14,         # SCK引脚
            mosi=26,        # MOSI引脚
            miso=27,        # MISO引脚
            cs=13,          # 片选引脚
            freq=400_000    # 初始频率设为400kHz确保稳定性
        )
        
        # 挂载文件系统
        os.mount(sd, '/sd')
        print('[成功] TF卡已挂载至 /sd 目录')
        return sd
    except Exception as e:
        print(f'[错误] 初始化失败: {e}')
        return None

# 初始化SD卡（最多重试3次）
for retry in range(3):
    sd = init_sd_card()
    if sd:
        break
    print(f'第 {retry+1} 次重试...')
    time.sleep(1)
else:
    raise RuntimeError("SD卡初始化失败，请检查硬件连接")

# 显示存储信息
sd_info = sd.info()
print(f"\nTF卡信息:")
print(f"类型: {'SDHC' if sd_info[0]==2 else 'SDSC'}")
print(f"容量: {sd_info[1] // (1024*1024)} MB")
print(f"块大小: {sd_info[2]} 字节")

# 增强版文件列表函数
def list_files(path='/sd', indent=0):
    """带错误处理的递归文件列表"""
    try:
        for item in os.listdir(path):
            full_path = f"{path}/{item}" if path != '/' else f"/{item}"
            try:
                stat = os.stat(full_path)
                prefix = '├─' if indent == 0 else '└─'
                
                # 显示条目信息
                print(' ' * indent + f"{prefix} {item}", end='')
                if stat[0] & 0x4000:  # 判断目录
                    print('/')
                    list_files(full_path, indent + 4)
                else:
                    # 显示文件大小和修改时间
                    size = stat[6]
                    mtime = time.localtime(stat[8])
                    print(f" ({size} bytes, 修改于 {mtime[0]}-{mtime[1]:02d}-{mtime[2]:02d} {mtime[3]:02d}:{mtime[4]:02d})")
            except OSError as e:
                print(f"\n[警告] 无法读取 {full_path}: {e}")
    except OSError as e:
        print(f"\n[错误] 访问 {path} 失败: {e}")

print("\n文件系统结构：")
list_files()

# 示例文件操作（可选）
def test_file_operations():
    """测试文件读写功能"""
    test_file = '/sd/test.txt'
    
    # 写入文件
    with open(test_file, 'w') as f:
        f.write('MicroPython SD卡测试\n')
    
    # 读取文件
    with open(test_file, 'r') as f:
        content = f.read()
        print(f"\n文件内容：\n{content}")
    
    # 删除测试文件
    os.remove(test_file)

# 执行测试（取消注释以下行进行测试）
# test_file_operations()