import time

from selenium import webdriver

dr = webdriver.Chrome()
file_path = "file:///F:/Pycharm/test/selenium2html/alert.html#"
dr.get(file_path)
# 点击链接弹出alert
dr.find_element_by_id("tooltip").click()
time.sleep(3)
alert = dr.switch_to.alert
#接受警告信息
#点击确认
alert.accept()
time.sleep(3)
text = dr.switch_to.alert.text
print(text)
dr.quit()

