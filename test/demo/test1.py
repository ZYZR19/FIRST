import time

from selenium import webdriver
driver = webdriver.Firefox()
driver.get("http://www.baidu.com")
# print("浏览器最大化")
# driver.maximize_window()
# print ("设置浏览器宽480、高800显示")
# driver.set_window_size(480,800)
# time.sleep(3)
# print("操作浏览器的前进后退")
# first_url = "http://www.baidu.com"
# print("访问第一个页面")
# driver.get(first_url)
# time.sleep(2)
# print("访问第二个页面")
# second_url = "http://news.baidu.com"
# driver.get(second_url)
# time.sleep(2)
# #返回到百度首页
# print("返回到第一个页面")
# driver.back()
# time.sleep(1)
# #前进到第二个页面
# print("前进到第二个页面")
# driver.forward()
# time.sleep(2)
# driver.quit




#控制滚动条
driver.find_element_by_id("kw").send_keys("好累")
driver.find_element_by_id("su").click()
time.sleep(2)
print("将页面拖到底部")
js = "var q = document.documentElement.scrollTop=10000"
driver.execute_script(js)
time.sleep(5)
print("拖到顶部")
js = "var q = document.documentElement.scrollTop=0"
driver.execute_script(js)
time.sleep(3)
driver.quit()