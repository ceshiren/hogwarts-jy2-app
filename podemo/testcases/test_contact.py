"""
__author__ = '霍格沃兹测试开发学社'
__desc__ = '更多测试开发技术探讨，请访问：https://ceshiren.com/t/topic/15860'
"""
from podemo.base.app import App


class TestContact:

    def setup(self):
        self.app = App()
        self.main = self.app.start().goto_main()

    def teardown(self):
        pass

    def test_addcontact(self):
        name = "hgwarts1"
        phonenum = '13401111112'
        result = self.main.goto_addresslist().click_addmember().\
            click_addmember_menual().editmember(name,phonenum).get_result()

        assert  result == "添加成功"
