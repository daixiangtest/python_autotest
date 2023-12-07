import time

from selenium.webdriver.chrome.service import Service

from hamster_test.web.selenium.page.create_project import CreateProject
from selenium import webdriver
from selenium.webdriver.common.by import By

s = Service(
    r"C:\Users\HUAWEI\Desktop\work_space\BaiduSyncdisk\auto_test\hamster_test\web\web_driver\chrome\119.0.6045\chromedriver.exe")
driver = webdriver.Chrome(service=s)  # 指定chromedriver的路径
cp = CreateProject(driver)
cp.geturl("https://computeshare-frontend.hamster.newtouch.com/dashboard/Script")
driver.maximize_window()

# cp.send_keys(10, By.ID, "form_item_telephoneNumber", "18326447662")
# cp.click(10, By.XPATH, '//*[@id="rc-tabs-0-panel-1"]/form/div[2]/div/div/div/div/div/button')
# cp.click(10, By.XPATH, '//*[@id="app"]/div/div/div/div/div[3]/div/label/span')
# time.sleep(5)
# cp.click(10, By.XPATH, '//*[@id="app"]/div/div/div/div/div[3]/button')
# cp.click(10, By.XPATH, '//*[@id="app"]/div/div[1]/ul/li[2]/span/a')
#
# time.sleep(3)
# el = driver.find_element(By.XPATH, '//*[@id="app"]/div/div[2]/div[2]/div[1]/span/div/span/input')
# el.send_keys(r"C:\Users\HUAWEI\Desktop\2.zip")
# cp.send_keys(10, By.XPATH, '//*[@id="app"]/div/div[2]/div[2]/div[1]/span/div/span/input',
#              r"C:\Users\HUAWEI\Desktop\2.zip")
# el = cp.find_elements(10, By.XPATH, '//*[@id="app"]/div/div[2]/div[2]/div[1]/span/div/span/input')[0]
# el.send_keys(r"C:\Users\HUAWEI\Desktop\2.zip")
cp.input_file(10, By.XPATH, '//*[@id="app"]/div/div[2]/div[2]/div[1]/div[1]/span/div/span/input',
              r"C:\Users\HUAWEI\Desktop\test01.py")
time.sleep(10)
