import time

from selenium import webdriver

path = './drivers/'  # 这是获取相对路径的方法
chrome_driver_path = path + 'chromedriver.exe'
from selenium.webdriver.common.by import By

list = []
driver = webdriver.Chrome(chrome_driver_path)
driver.get('https://linkr.bio/login')
driver.find_element_by_id('email').send_keys('445275113@qq.com')
driver.find_element_by_id('pwd').send_keys('123456')
driver.find_element_by_class_name('btn-purple').click()
time.sleep(1)
driver.find_element_by_xpath('//*[@id="linksTab"]/div/div[1]/div[1]/button').click()
eles = driver.find_elements_by_xpath('//*[@class="inputs col"]/input')
eles[0]
eles[0].get_attribute()
eles[0].send_keys('123')
eles[1].send_keys('456')
eles[2].is_displayed()
# hot = driver.find_elements(By.ID, 'hotsearch-content-wrapper')
# hot_ul = driver.find_elements(By.XPATH, '//*[@id="hotsearch-content-wrapper"]/li')
# time.sleep(1)
# hot_ul[0].click()
# # driver.quit()
