import time
from selenium import webdriver

from hamster_test.comms.yaml_utils import get_picture

browser = webdriver.Chrome()
browser.get('https://develop.hamster.newtouch.com/projects')
# value = browser.execute_script('return localStorage.getItem("wwwPassLogout");')
# 将token的值放入浏览器缓存中
browser.execute_script(
    'localStorage.setItem("token","6vaHUC1Pv9kYrDDWmJ/jOnl05RMX+eaooM1/JGd2ZkXOjI5pQUIA1sxe2qaNIfpO")')
# 刷新以token登录
browser.refresh()
for i in range(20):
    get_picture(browser, fr'输入{i}失败')
    time.sleep(2)
# 获取缓存中的token值
value = browser.execute_script("return localStorage.getItem('token')")
print(value)
time.sleep(300)
