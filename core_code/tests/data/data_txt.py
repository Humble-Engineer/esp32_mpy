import random
import time

def generate_random_number(file):
    """
    生成并打印一个保留两位小数的随机浮点数。
    随机数的范围在0.9到1.1之间。
    同时将随机数写入到指定的文件中。
    """
    random_number = random.uniform(0.9, 1.1)
    formatted_number = f"{random_number:.2f}"
    print(formatted_number)  # 打印到终端
    file.write(formatted_number + "\n")  # 写入文件

def main():
    """
    主函数。
    在一个无限循环中，每隔一秒生成并打印一个随机数。
    同时将随机数写入到当前目录下的一个txt文件中。
    """
    # 创建一个文件对象，用于写入数据（到单片机里找）
    with open("data.txt", "a") as file:  # 以追加模式打开文件
        while True:
            time.sleep(1)  # 暂停一秒
            generate_random_number(file)  # 调用生成随机数的函数，并传入文件对象

if __name__ == '__main__':
    main()  # 当模块作为主程序运行时，调用主函数