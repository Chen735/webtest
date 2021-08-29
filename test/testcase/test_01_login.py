import unittest
import sys
import ddt
from test.page.LoginPage import LoginPage

from test.testcase.case_modle import *
from test.common.BrowserDriver import *
sys.path.append('../')


@ddt.ddt
class LoginCase(model):
    # @ddt.data(["445275113@qq.com", "321d43", "Account and password not match!"],
    #           ["445275113", "32143", "Email format is incorrect"],
    #           ["445275113@qq.com", '123456', None])
    @ddt.data(["445275113@qq.com", '123456', None])

    @ddt.unpack
    def test_login(self, email, password, error_toast):
        self.driver.get('https://linkr.bio/login')
        # self.driver.get('https://linkr.bio/login')
        # email, password, error_toast = data   数据解析有问题
        self.login = LoginPage(self.driver)
        self.login.input_email_text(email)
        self.login.input_pwd_text(password)
        self.login.click_login_btn()
        if error_toast is not None:
            self.assertTrue(self.login.get_error_text(error_toast))
