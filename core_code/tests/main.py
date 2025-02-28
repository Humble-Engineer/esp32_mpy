from machine import Pin,ADC,I2C
import time
import ssd1306

def adc_get_result_average(times):
    
    temp_val = 0
    
    for i in range(0,times):
        temp_val += adc.read()
        
    return temp_val / times
    
if __name__ == '__main__':
    
    adcdata = 0
    adc = ADC(Pin(1))         # 引脚1跟底板的电位器相连接
    adc.atten(ADC.ATTN_11DB)  # 11dB 衰减（扩大电压输入范围至3.3v）
    adc.width(ADC.WIDTH_12BIT)  #4095
    
    i2c = I2C(0, scl=Pin(10), sda=Pin(9))
    oled_width = 128
    oled_height = 64
    oled = ssd1306.SSD1306_I2C(oled_width, oled_height, i2c)
    
    while True:

        # 读取ADC值
        adcdata = adc_get_result_average(5)
        # 读取ADC值
        umber = float(adcdata * (3.3 / 4096))
        # 保留四位有效数字并打印
        
        data_str = f"{umber:.4f}"
        print(data_str)
        
        oled.fill(0)
        oled.text("ADC:" + data_str, 27, 30)      
        oled.show()
        
        time.sleep(0.2)
        
        break




