"""
__author__ = '霍格沃兹测试开发学社'
__desc__ = '更多测试开发技术探讨，请访问：https://ceshiren.com/t/topic/15860'
"""
# pip install appium-python-client
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.common.exceptions import NoSuchElementException


class TestContact:
    def setup(self):
        # 初始化，打开app
        # 定义 了json
        # Desire 配置：http://appium.io/docs/en/writing-running-appium/caps/
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

    def teardown(self):
        # 关闭app
        self.driver.quit()

    def swipe_find(self,text, num=3):
        """
        滑动查找
        num: 查找次数
        :return:
        """
        for i in range(num):
            try:
                return self.driver.find_element(MobileBy.XPATH, f"//*[@text='{text}']")
            except:
                # 找不到元素，滑动页面
                size = self.driver.get_window_size()
                width = size.get("width")
                height = size.get("height")
                start_x = width / 2
                start_y = height * 0.8
                end_x = start_x
                end_y = height * 0.3
                duration = 2000
                self.driver.swipe(start_x, start_y, end_x, end_y, duration)
            if i == num - 1:
                raise NoSuchElementException(f"找了 {num} 次，未找到")

    def test_addcontact(self):
        name = "hgwarts1"
        phonenum = '13401111112'
        # 点击【通讯录】
        self.driver.find_element(MobileBy.XPATH,
                                 "//*[@text='通讯录']").click()
        # 直接找添加成员，会报错，
        # find_element 只能找到你看到的页面上展示的元素，没有展示出来的，找不到
        # self.driver.find_element(MobileBy.XPATH, "//*[@text='添加成员']").click()
        self.swipe_find("添加成员").click()
        self.driver.find_element(MobileBy.XPATH, "//*[@text='手动输入添加']").click()
        self.driver.find_element(MobileBy.XPATH, '//*[contains(@text,"姓名")]/../*[@text="必填"]').send_keys(name)
        self.driver.find_element(MobileBy.XPATH, '//*[contains(@text,"手机")]/..//*[@text="必填"]').send_keys(phonenum)
        self.driver.find_element(MobileBy.XPATH, "//*[@text='保存']").click()
        # 判断 断言
        # while True:
        #     if "添加成功" in self.driver.page_source:
        #         print(self.driver.page_source)
        #         break
        result = self.driver.find_element(MobileBy.XPATH, "//*[@class='android.widget.Toast']").get_attribute("text")
        assert  result == "添加成功"
