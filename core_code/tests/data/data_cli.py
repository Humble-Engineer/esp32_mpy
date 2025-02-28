import random
import time

def generate_random_number():
    """
    生成并打印一个保留两位小数的随机浮点数。
    随机数的范围在0.9到1.1之间。
    """
    random_number = random.uniform(0.9, 1.1)
    print(f"{random_number:.2f}")

def main():
    """
    主函数。
    在一个无限循环中，每隔一秒生成并打印一个随机数。
    """
    while True:
        time.sleep(1)  # 暂停一秒
        generate_random_number()  # 调用生成随机数的函数

if __name__ == '__main__':
    main()  # 当模块作为主程序运行时，调用主函数