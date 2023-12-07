import time, yaml
from configparser import ConfigParser
from hamster_test.comms.constants import PICTURE_DIR, CFI, DATA_YAML
import allure
from selenium import webdriver

"""读取yaml文件数据"""


def get_yaml_data(file):  # 读取yaml文件数据
    try:
        with open(file, mode='r', encoding='utf-8') as fr:
            cases = yaml.safe_load(fr)
            return cases
    except Exception as e:
        print("yaml文件读取失败", e)


# 保存截图
def get_picture(browser, name):
    try:
        # 获取时间戳用来命名截图
        sys_time = time.strftime("%Y%m%d%H%M%S")
        timestamp = int(time.time())
        # 截图名称：时间+截图名字描述+后缀
        png_name = sys_time + name + ".png"
        # 截图存放位置
        png_file = PICTURE_DIR + '\\' + png_name
        page_source_path = PICTURE_DIR + '\\' + sys_time + name + '.html'
        # 获取截图（这才是灵魂）
        browser.save_screenshot(png_file)
        with open(page_source_path, "w", encoding="u8") as f:
            f.write(browser.page_source)
        time.sleep(1)
        allure.attach.file(png_file, name='image', attachment_type=allure.attachment_type.PNG)
        allure.attach.file(page_source_path, name="page_source", attachment_type=allure.attachment_type.HTML)
    except Exception as e:
        print('截图失败', e)


# 读取conf中的config.ini文件
def get_ini_data(section, option):
    try:
        cp = ConfigParser()  # 创建 解析器对象
        cp.read(CFI, encoding="utf-8")  # 加载ini文件
        return cp.get(section, option)  # 通过 标头和选项获取对应的值
    except Exception as e:
        print("从ini文件中读取数据失败", e)


if __name__ == '__main__':
    option = webdriver.ChromeOptions()
    option.add_experimental_option("detach", True)
    driver = webdriver.Chrome(options=option)
    dr = webdriver.Chrome()
    driver.get('https://www.baidu.com')
    time.sleep(3)
    get_picture(dr, 'cc')
