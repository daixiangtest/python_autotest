import time
from selenium import webdriver
from selenium.webdriver.common.by import By

"""
浏览器加载配置文件启动
about:support  
"""
# 老版本的加载配置使用的是profile方法，该方法已经不适用与新版本浏览器新版本使用与option方法
# profileDir = r'C:\Users\HUAWEI\AppData\Roaming\Mozilla\Firefox\Profiles\1v6kjv0t.default-release'
# profile = webdriver.FirefoxProfile(profile_directory=profileDir)
#
# driver = webdriver.Firefox()
# driver.get("https://blog.csdn.net/weijiaxin2010")


profile_dir = r'C:\Users\HUAWEI\AppData\Roaming\Mozilla\Firefox\Profiles\1v6kjv0t.default-release'  # 本地浏览器配置文件的路径
profile = webdriver.FirefoxOptions()  # 声明一个option的对象
profile.add_argument(profile_dir)  # 使用对象添加配置文件路劲
dr = webdriver.Firefox(options=profile)  # 将配置好的对象传入浏览对象中启动时进行加载
dr.maximize_window()
dr.get('https://github.com/daixiang11')
time.sleep(10)
dr.quit()

# # coding=utf-8
# from selenium import webdriver
# from selenium.common.exceptions import TimeoutException
# from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver import ActionChains
# import time
#
#
# # 页面交互
# def pageInteraction():
#     driver = webdriver.Firefox()
#     driver.get('http://www.baidu.com')
#
#     # 隐示等待，为了等待充分加载好网址
#     driver.implicitly_wait(5)
#     write = driver.find_element_by_id("kw")
#     write.send_keys("Selenium")
#     # 点击
#     driver.find_element_by_id('su').click()
#     try:
#         # 显示等待，其中5的解释：5秒内每隔0.5毫秒扫描1次页面变化，直到指定的元素
#         wait = WebDriverWait(driver, 5)
#         wait.until(lambda driver: driver.find_element_by_id("content_left"))
#         # 打印源代码
#         print(driver.page_source)
#
#     except  TimeoutException:
#         print("查询元素超时")
#     finally:
#         time.sleep(3)
#         driver.close()
#
#
# # 页面元素拖拽
# def element_dragging():
#     global driver
#     try:
#         driver = webdriver.Firefox()
#         url = "http://www.runoob.com/try/try.php?filename=jqueryui-api-droppable"
#         driver.get(url)
#         driver.implicitly_wait(5)
#         # 切换到元素所在的frame
#         driver.switch_to.frame("iframeResult")
#         # 起点
#         start = driver.find_element_by_id("draggable")
#         # 终点
#         end = driver.find_element_by_id("droppable")
#
#         actions = ActionChains(driver)
#         actions.drag_and_drop(start, end)
#         # 执行
#         actions.perform()
#     except Exception:
#         print("exception")
#     finally:
#         driver.close()
#
#
# # 页面切换
# def pageSwitching():
#     driver = webdriver.Firefox()
#     driver.get('http://www.baidu.com')
#     # 获取当前百度界面的窗口句柄
#     BD_windows = driver.current_window_handle
#     # 打印
#     print(BD_windows)
#     # 隐示等待，为了等待充分加载好网址
#     driver.implicitly_wait(5)
#
#     write = driver.find_element_by_id("kw")
#     write.send_keys("CSDN")
#     # 点击
#     driver.find_element_by_id('su').click()
#     try:
#         # 打开一个网页
#         driver.find_element_by_link_text(u'CSDN-专业IT技术社区').click()
#         # 隐示等待，为了等待充分加载好网址
#         driver.implicitly_wait(5)
#         # 打印所有的窗口
#         print(driver.window_handles)
#         # 隐示等待，为了等待充分加载好网址
#         driver.implicitly_wait(5)
#         # 窗口切换到第二个网页
#         driver.switch_to_window(driver.window_handles[1])
#         # 点击第二个网页的"写博客"按钮
#         driver.find_element_by_link_text(u'写博客').click()
#         time.sleep(5)
#
#     except Exception:
#         print("exception")
#
#     finally:
#         driver.quit()
#
#     if __name__ == '__main__':
#         pageInteraction()
#         # pageSwitching()
#         # elementDragging()
