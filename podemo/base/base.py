"""
__author__ = '霍格沃兹测试开发学社'
__desc__ = '更多测试开发技术探讨，请访问：https://ceshiren.com/t/topic/15860'
"""
# 1、优化__init__()方法， 将driver放到基类中
# 2、在基类中添加一些公共的方法：find, swipe_find, find_click
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.webdriver import WebDriver
from selenium.common.exceptions import NoSuchElementException


class BasePage:

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def find(self, by, locator):
        return self.driver.find_element(by, locator)

    def find_click(self, by, locator):
        """
        查找到元素并点击
        :param by:
        :param locator:
        :return:
        """
        self.find(by, locator).click()

    def find_sendkeys(self, by, locator, text):
        """
        找到元素之后输入
        :param by:
        :param locator:
        :param text:
        :return:
        """
        self.find(by, locator).send_keys(text)

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




