from selenium.webdriver import Chrome
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
driver = Chrome(
    service=Service(r'D:\software\PyCharmLib\chromedriver.exe'),
    options=chrome_options)
# 注意：把chromedriver文件放到了当前文件夹里面，可以这样调用
# driver = Chrome('./chromedriver.exe', options=chrome_options)

driver.get('https://blog.csdn.net/HRG520JN/article/details/125936986')
http_str = input('输入任意地址，无则回车')
if http_str:
    http_str = http_str
else:
    http_str = 'https://blog.csdn.net/HRG520JN/article/details/125781184'
driver.get(http_str)

http_str2 = input('输入任意内容地址，无则回车查看selenium全面讲解文章')
if http_str2:
    http_str2 = http_str2
else:
    http_str2 = 'https://blog.csdn.net/HRG520JN/article/details/125781184'
driver.get(http_str2)


