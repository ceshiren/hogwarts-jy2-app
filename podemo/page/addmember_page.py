"""
__author__ = '霍格沃兹测试开发学社'
__desc__ = '更多测试开发技术探讨，请访问：https://ceshiren.com/t/topic/15860'
"""
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.webdriver import WebDriver

from podemo.base.base import BasePage


class AddMemberPage(BasePage):


    def click_addmember_menual(self):
        #click 手动输入添加
        self.find_click(MobileBy.XPATH, "//*[@text='手动输入添加']")
        from podemo.page.editmember_page import EditMemberPage

        return EditMemberPage(self.driver)

    def get_result(self):
        result = self.find(MobileBy.XPATH, "//*[@class='android.widget.Toast']").get_attribute("text")
        return result