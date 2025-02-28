from machine import Pin,ADC
import time

"""
 * @brief       ADC取平均值
 * @param       times：次数
 * @retval      返回：ADC平均值
"""
def adc_get_result_average(times):
    
    temp_val = 0
    
    for i in range(0,times):
        temp_val += adc.read()
        
    return temp_val / times
    
"""
 * @brief       程序入口
 * @param       无
 * @retval      无
"""
if __name__ == '__main__':
    
    adcdata = 0

    adc = ADC(Pin(1))         # 引脚1跟底板的电位器相连接
    adc.atten(ADC.ATTN_11DB)  # 11dB 衰减（扩大电压输入范围至3.3v）
    adc.width(ADC.WIDTH_12BIT)  #4095
    
    while True:

        # 读取ADC值
        adcdata = adc_get_result_average(5)
        # 读取ADC值
        umber = float(adcdata * (3.3 / 4096))
        # 保留四位有效数字并打印
        print(f"{umber:.4f}")
        time.sleep_ms(100)



