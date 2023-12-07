"""
一、ADB简介
1、什么是adb
ADB 全称为 Android Debug Bridge，起到调试桥的作用，是一个客户端-服务器端程序。其中客户端是用来操作的电脑，服务端是 Android 设备。

ADB 也是 Android SDK 中的一个工具，可以直接操作管理 Android 模拟器或者真实的 Android 设备。

2、为什么要用adb
运行设备的 shell(命令行)
管理模拟器或设备的端口映射
计算机和设备之间上传/下载文件
可以对设备的应用进行卸载安装等
在 App 遇到 ANR/Crash 等 bug 时，可以通过 ADB 来抓取日志

二，ADB安装
1，下载adb工具
ADB和Fastboot for Windows：
https://dl.google.com/android/repository/platform-tools-latest-windows.zip

ADB和Fastboot for Mac：
https://dl.google.com/android/repository/platform-tools-latest-darwin.zip

ADB和Fastboot for Linux：
https://dl.google.com/android/repository/platform-tools-latest-linux.zip

2.安装
复制 adb文件路径添加环境变量

3.链接
1. 将手机连接PC，打开手机设置，进入“关于手机”，连击“型号”菜单，会提示：您已进入开发者模式

2. 返回设置中，进入“开发者选项”菜单

3. 打开“开发者选项”，然后向下翻，打开 “USB调试”

   Tips：这个时候一般情况下PC就在安装驱动了，稍后就会弹出秘钥，如果迟迟没有弹出，可以尝试开关开发者选项或者USB调试开关

4. 手机端弹出秘钥，选择允许，点击确定

"""
# adb shell input tap x坐标 y坐标  根据坐标定位点击
# adb shell input text “字符串”  输入文本信息
# adb version ：显示 adb 版本
# adb help：帮助信息，查看adb所支持的所有命令
# adb devices：查看当前连接的设备，已连接的设备会显示出来
# adb get-serialno：也可以查看设备号
# adb root：获取Android管理员（root用户）的权限
# adb shell：登录设备 shell，该命令将登录设备的shell（内核），登录shell后，可以使用 cd，ls，rm 等Linux命令
# adb -d：如果同时连了usb，又开了模拟器，连接当前唯一通过usb连接的安卓设备
#
# adb -e shell：指定当前连接此电脑的唯一的一个模拟器
#
# adb -s <设备号> shell：当电脑插多台手机或模拟器时，指定一个设备号进行连接
# exit：退出
# adb kill-server：杀死当前adb服务，如果连不上设备时，杀掉重启。（没事不要用它）
# adb start-server：杀掉后重启
# 5037：adb默认端口，如果该端口被占用，可以指定一个端口号，如下命令↓
#
# adb -p 6666 start-server：任意指定一个 adb shell 的端口
# adb shell pm list packages：列出当前设备/手机，所有的包名
# adb shell logcat -c：清理现有日志
# adb shell logcat -v time ：输出日志，信息输出在控制台
# adb shell logcat -v time > <存放路径\log.txt>：输出日志并保存在本地文件
# Ctrl+C：终止日志抓取
# adb shell logcat -v time *:E > <存放路径\log.txt>：打印级别为Error的信息
# 日志的等级：
# -v：Verbse（明细）
# -d：Debug（调试）
# -i：Info（信息）
# -w：Warn（警告）
# -e：Error（错误）
# -f：Fatal（严重错误）
# 抓取日志的步骤先输入命令启动日志，然后操作 App，复现 bug，再 ctrl+c 停止日志，分析本地保存的文件。
# ：日志是记录手机系统在运行app时有什么异常的事件
# EXCEPTION
# 也可以把更详细得Anr日志拉取出来：adb shell pull /data/anr/traces.txt <存放路径>
# adb shell getprop ro.product.model：获取设备型号
# adb shell screencap -p /sdcard/mms.png：屏幕截图
# adb pull /sdcard/mms.png <存放的路径>：将截图导出到本地
