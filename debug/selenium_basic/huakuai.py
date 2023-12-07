import time
import requests
import re
import cv2
from selenium import webdriver
from selenium.webdriver.common.by import By

dr = webdriver.Firefox()
dr.get("https://i.qq.com/")
dr.implicitly_wait(5)
dr.switch_to.frame(dr.find_element(By.XPATH, '//*[@id="login_frame"]'))  # iframe页面中的元素定位是需要先切换至该页面框架中
"""
# dr.switch_to.frame()  #切换至某页面框
# dr.switch_to.parent_frame()  #切换至主页面框
# dr.switch_to.default_content()  #切换至上一级的页面框
（）括号中可以输入元素的对象，下标，或者元素的属性值
"""
dr.find_element(By.XPATH, '//*[@id="switcher_plogin"]').click()  # 点击账户登录
dr.find_element(By.XPATH, '//*[@id="u"]').send_keys("983643937@qq.com")  # 输入用户名
dr.find_element(By.XPATH, '//*[@id="p"]').send_keys("Dx3826729")  # 输入密码
time.sleep(1)
dr.find_element(By.XPATH, '//*[@id="login_button"]').click()  # 点击登录按钮

dr.switch_to.frame(dr.find_element(By.XPATH, '//*[@id="tcaptcha_iframe_dy"]'))

url = None
url2 = None
while True:
    try:
        ele_big = dr.find_element(By.XPATH, '//*[@id="slideBg"]')
        ele_min = dr.find_element(By.XPATH, '//*[@id="tcOperation"]/div[7]')
        ele_min.screenshot("dada.png")  # 对所选元素进行截图
        b = ele_big.get_attribute('style')  # 获取该元素中styles标签的值
        print(b)
        a = ele_min.get_attribute("style")

        print(a)
        time.sleep(1)
        if (b and a) is None:
            print("为空")
            time.sleep(3)
            continue
        else:
            time.sleep(3)
            print(b)
            url_style = re.findall(r'"(.*)"', b)  # 对返回值的字符串截取出url地址
            url_style2 = re.findall(r'"(.*)"', a)
            """
            通过正则表达式提取字符串中的文本值
            # a = "ab1234fe"
            # b = re.findall(r'a(.*)e', a)  
            # print(b)=['b1234f']
            """
            url = url_style[0]
            url2 = url_style2[0]
            # print(url)
            # print(url2)

            break
    except Exception as e:
        time.sleep(3)
        print("获取url地址失败")
        continue
time.sleep(300)
print(url)
print(url2)
con = requests.get(url).content
f = open(r'C:\Users\HUAWEI\Desktop\work_space\BaiduSyncdisk\auto_test\debug\selenium_basic/bj.jpg', mode='wb')
f.write(con)
f.close()

con2 = requests.get(url2).content
f = open(r'C:\Users\HUAWEI\Desktop\work_space\BaiduSyncdisk\auto_test\debug\selenium_basic/hk.jpg', mode='wb')
f.write(con2)
f.close()
"""
# 读取背景图片的RGB码
bj_rgb = cv2.imread(r'./bj.jpg')
# 灰度处理
bj_gray = cv2.cvtColor(bj_rgb, cv2.COLOR_BGR2GRAY)
# 读取滑块的rgb
hk_rgb = cv2.imread(r'./hk.jpg', 0)
# 匹配滑块在背景图的位置
res = cv2.matchTemplate(bj_rgb, hk_rgb, cv2.TM_CCOEFF)
# 获取位置
lo = cv2.minMaxLoc(res)
print(lo)
"""

dr.close()
