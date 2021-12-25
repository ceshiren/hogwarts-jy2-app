"""
__author__ = '霍格沃兹测试开发学社'
__desc__ = '更多测试开发技术探讨，请访问：https://ceshiren.com/t/topic/15860'
"""
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.webdriver import WebDriver
from selenium.common.exceptions import NoSuchElementException

from podemo.base.base import BasePage
from podemo.page.addmember_page import AddMemberPage


class AddressListPage(BasePage):

    def click_addmember(self):
        # click 添加成员
        self.swipe_find("添加成员").click()
        return AddMemberPage(self.driver)