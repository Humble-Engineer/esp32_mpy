这是ESP32微控制器使用MicroPython作为编程语言的一套外设驱动程序。

根目录文件夹： 
refer_code/ #主要存放一些网上的参考示例程序。

工程文件夹:
core_code/ #用vscode打开，其中子文件需要最终同步到esp32设备。

core_code/main.py(boot.py) #上电自启程序

core_code/modules/ #主要存放各个功能模块以供主程序调用。 
core_code/stores/ #主要存放各个版本PCB板的主程序（引脚分配上有区别）。 
core_code/tests/ #主要存放还在测试中的程序。 
