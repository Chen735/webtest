from selenium.webdriver.common.by import By
from test.common.Seleniums import BasePage
import sys

sys.path.append('../')


class LinkPage(BasePage):
    """
    在这里写定位器，通过元素属性定位元素对象
    """
    # add_link_btn = (By.CLASS_NAME, 'd-inline-block add-links-btn flex-grow-1')  # 添加link按钮
    add_new_link_btn = (By.XPATH, '//*[@id="linksTab"]/div/div[1]/div[1]/button')  # 添加link按钮
    # link_all_input = (By.CLASS_NAME, 'inputs col')  # 获取link整个输入框
    #  add link 输入框模板
    add_link = (By.XPATH, '//*[@class="inputs col"]/input')

    title_input = (By.ID, 'root-title-input')
    icon = (By.ID, 'icons-tab')
    links = (By.ID, 'links-tab')
    error_toast = (By.XPATH, '//*[@class="mt-4 error-link"]/div')
    add_link_btn = (By.XPATH, '//*[@id="linksTab"]/div/div[1]/div[2]/div/div[3]/div[2]/button')

    def links_click(self):
        self.click(self.links)

    def icon_click(self):
        self.click(self.icon)

    #  点击add link按钮
    def add_new_link_click(self):
        self.click(self.add_new_link_btn)

    def add_link_click(self):
        self.click(self.add_link_btn)

    # # 判断点击add link按钮后是否出现add link模板
    # def link_all_input_exist(self):
    #     temp = self.find_element(self.link_all_input)
    #     if temp is not None:
    #         return True
    #     else:
    #         return False

    # def input_title(self, text):
    #     # self.send_key(self.title_input, text)
    #     title_ele = self.find_elements(self.add_link)
    #     self.send_key(title_ele[0], text)

    def link_input_title(self, text):
        #  使用find elements方法时，前面必须加*号，不然就会报错
        #  selenium.common.exceptions.InvalidArgumentException: Message: invalid argument: 'using' must be a string
        elems = self.find_elements(*self.add_link)
        print(elems[0].get_attribute('placeholder'))
        # temp = elems[0]
        self.send_keys(elems[0], text)

    def link_input_url(self, text):
        elems = self.find_elements(*self.add_link)
        self.send_keys(elems[1], text)

    #  比较登录时出现的错误提示码
    def get_error_text(self, text):
        if text == self.get_text(self.error_toast):
            return True
        else:
            return False
