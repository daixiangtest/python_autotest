import time

from selenium import webdriver

from hamster_test.comms.yaml_utils import get_ini_data

# options = webdriver.ChromeOptions()
# options.add_experimental_option('detach', True) # 不自动关闭浏览
# driver = webdriver.Chrome(options=options)    # Chrome浏览器


option = webdriver.ChromeOptions()
option.add_argument("--user-data-dir=" + r"C:\Users\HUAWEI\AppData\Local\Google\Chrome\User Data")  # 添加获取到的配置文件路径
option.add_experimental_option('detach', True)  # 浏览器不会自动关闭
# option.add_argument("--remote-debugging-port=9222")  # this
driver = webdriver.Chrome(options=option)  # 打开配置插件的chrome浏览器
a = driver.window_handles
driver.maximize_window()  # 浏览器窗口最大化
driver.get("https://develop.hamster.newtouch.com/projects")
value = driver.execute_script('return localStorage.getItem("token")')
print(value)
time.sleep(30)
