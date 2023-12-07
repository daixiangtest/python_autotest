import json
import time
from selenium import webdriver

"""
获取浏览器的控住台日志，判断接口的日志状态
"""
# driver配置
options = {'performance': 'ALL'}
chrome_options = webdriver.ChromeOptions()
chrome_options.set_capability('goog:loggingPrefs', options)
driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.baidu.com/")
while True:

    # 将日志信息保存在list中
    logs = driver.get_log('performance')
    for log in logs:
        res = json.loads(log["message"])
        a = res['message']['method']
        if a != "Network.responseReceived":  # 不是接口的日志
            continue
        b = res['message']['params']['response']['status']
        print(b)
        if b != 200:
            print("接口报错")
    time.sleep(3)
    driver.execute_cdp_cmd('Page.reload', {'ignoreCache': True})  # 强制刷新
