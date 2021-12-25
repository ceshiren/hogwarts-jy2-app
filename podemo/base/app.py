"""
__author__ = '霍格沃兹测试开发学社'
__desc__ = '更多测试开发技术探讨，请访问：https://ceshiren.com/t/topic/15860'
"""


# 管理 app 相关的操作
# 启动app， 关闭app， 重启app
from appium import webdriver

from podemo.page.main_page import MainPage


class App:

    def start(self):
        # 启动app
        caps = {}
        caps["platformName"] = "Android"
        caps["deviceName"] = "hogwarts"
        # adb logcat ActivityManager:I | grep "cmp" 获取启动页的activity
        # com.tencent.wework/.launch.LaunchSplashActivity
        # 包名/欢迎页的名字
        caps["appPackage"] = "com.tencent.wework"
        caps["appActivity"] = ".launch.LaunchSplashActivity"
        caps["noReset"] = "True"
        # 与server 建立连接
        # 4723 是我们启动的server的端口
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", caps)
        self.driver.implicitly_wait(10)
        return self

    def restart(self):
        pass

    def stop(self):
        self.driver.quit()

    def goto_main(self):
        return MainPage(self.driver)
