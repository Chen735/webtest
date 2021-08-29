#!/usr/bin/env python
# -*- coding:utf-8 -*-
import unittest
from test.common.BrowserDriver import BrowserDriver
from selenium import webdriver

path = './drivers/'  # 这是获取相对路径的方法
chrome_driver_path = path + 'chromedriver.exe'


class model(unittest.TestCase):
    dr = webdriver.Chrome(chrome_driver_path)

    # @classmethod
    # def setUpClass(cls,driver = dr):
    #     cls.driver = BrowserDriver(driver)
    #     cls.driver = cls.driver.openbrowser(cls.driver)

    def setUp(self, driver=dr):
        self.driver = driver

    def teardown(self):
        self.driver.quit()

    # @classmethod
    # def tearDownClass(cls):
    #     cls.driver.quit()
