import time
import unittest
import sys
import ddt
from test.page.LinkPage import LinkPage
from test.testcase.case_modle import *

# from test.testcase.test_01_login import *   会重复将login test 再次添加，出现bug
sys.path.append('../')


@ddt.ddt()
class LinkCase(model):

    @ddt.data(["google", "", " Invalid Url. "])
    @ddt.unpack
    def test_add_link(self, link_title, link_url, error_toast):
        self.link = LinkPage(self.driver)
        # self.link.icon_click()
        #  点击link图标按钮
        self.link.links_click()
        #  点击+ADD NEW LINK按钮
        self.link.add_new_link_click()
        # self.assertTrue(self.link.link_all_input_exist())
        time.sleep(1)
        self.link.link_input_title(link_title)
        self.link.link_input_url(link_url)
        self.link.add_link_click()
        if error_toast is not None:
            self.assertTrue(self.link.get_error_text(error_toast))
        # self.link.input_url('baidu.com')
