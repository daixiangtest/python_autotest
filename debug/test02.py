from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from hamster_test.web.selenium.page import CreateProject

# 打印浏览器的端口号
# print('debugger_address:', dr.caps['goog:chromeOptions']['debuggerAddress'])

chrome_options = Options()
chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:27362")
driver = webdriver.Chrome(options=chrome_options)

cp = CreateProject(driver)
cp.window(0)
a = cp.text(10, By.XPATH, '//*[@class="tip"]')
print(a)
