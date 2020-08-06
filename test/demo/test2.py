import os
import time
from selenium import webdriver
driver = webdriver.Firefox()
driver.get("file:///F:/Pycharm/test/selenium2html/checkbox.html")
inputs = driver.find_elements_by_tag_name("input")
for input in inputs:
    if input.get_attribute('type')=="checkbox":
        input.click()
time.sleep(2)
print("定位一组元素完成")
driver.quit()


