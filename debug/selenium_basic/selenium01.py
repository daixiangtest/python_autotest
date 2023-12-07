import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from webdriver_manager.chrome import ChromeDriverManager
browser = webdriver.Chrome(options=ChromeDriverManager().install())
"""
自动获取浏览器版本并更新webdriver
"""
browser.refresh()

browser.get('http://www.baidu.com')
time.sleep(30)



# 关闭浏览器
browser.close()
