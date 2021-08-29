from selenium.webdriver.common.by import By
from test.common.Seleniums import BasePage
import sys

sys.path.append('../')


class LoginPage(BasePage):
    """
    在这里写定位器，通过元素属性定位元素对象
    """
    email_input = (By.ID, 'email')  # email输入框
    pwd_input = (By.ID, 'pwd')  # 密码输入框
    login_btn = (By.CLASS_NAME, 'btn-purple')  # 定位登录按钮
    error_toast = (By.CLASS_NAME, 'error_text')  # 定位错误提示

    def input_email_text(self, text):
        self.send_key(self.email_input, text)

    def input_pwd_text(self, text):
        self.send_key(self.pwd_input, text)

    def click_login_btn(self):
        self.click(self.login_btn)

    #  比较登录时出现的错误提示码
    def get_error_text(self, text):
        if text == self.get_text(self.error_toast):
            return True
        else:
            return False

