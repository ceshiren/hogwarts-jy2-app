"""
__author__ = '霍格沃兹测试开发学社'
__desc__ = '更多测试开发技术探讨，请访问：https://ceshiren.com/t/topic/15860'
"""
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.webdriver import WebDriver

from podemo.base.base import BasePage


class EditMemberPage(BasePage):

    def editmember(self,name,phonenum):
        # input name
        # input phonenum
        # click save
        self.find_sendkeys(MobileBy.XPATH,
                                 '//*[contains(@text,"姓名")]/../*[@text="必填"]',
                           name)

        self.find_sendkeys(MobileBy.XPATH,
                                 '//*[contains(@text,"手机")]/..//*[@text="必填"]',
                           phonenum)
        self.find_click(MobileBy.XPATH, "//*[@text='保存']")

        from podemo.page.addmember_page import AddMemberPage

        return AddMemberPage(self.driver)