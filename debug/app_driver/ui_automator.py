import time

from uiautomator import Device

"""
Windows搭建uiautomator2和weditor环境
前提条件：adb安装完成并且配置号环境,手机连接了电脑adb调试通过
1,pip install uiautomator2
2 python -m uiautomator2 init #init就是所有USB连接电脑的手机上都安装uiautomator2
3 pip install -U weditor==0.6.4  安装weditor  
4 python -m weditor   运行weditor
启动后会在浏览器中打开终端服务
5.输入adb devices 查看设备ID进行连接
"""

# 获取Device对象
driver = Device()
# 通过页面中的decription属性获取元素对象进行点击
driver(description="设置").click()
# 通过页面的坐标来进行点击
driver.click(420, 1845)
#
# print(11)
# # driver(resourceId="com.huawei.hisuite:id/open_pc_side_hisuite_tip").click()
# time.sleep(3)
# driver(resourceId="android:id/content").click()
# driver.click(0.18, 0.489)
# driver.click(380, 1230)
