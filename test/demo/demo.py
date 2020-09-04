# coding = utf-8
import sys

from selenium import webdriver
# 要使用selenium的webdriver里的函数 首先把包导进来
import time

# browser = webdriver.Firefox()#操控的浏览器是哪个
# time.sleep(3)
# browser.get("http://www.baidu.com")
# time.sleep(3)
# browser.find_element_by_id("kw").send_keys("你在干啥啊")
# #一个控件有若干属性id 、name、（也可以用其它方式定位），百度输入框的id 叫kw ，我要在输入框里输入 selenium
# time.sleep(3)
# browser.find_element_by_id("su").click()
# #搜索的按钮叫su 需要点一下就是click
# browser.quit()
# 退出并关闭窗口的每一个相关的驱动程序
# browser.close() 关闭当前窗口
# close方法关闭当前的浏览器窗口
# quit方法不仅关闭窗口，还会彻底的退出webdriver，释放与driver server之间 的连接。
# 所以简单来说quit是更加彻底的close，quit会更好的释放资源

#########百度输入框的定位方式##########
# id  name   classname tagname xpath cssselector linktest particallinktest
# 鼠标点击与键盘输入
driver = webdriver.Firefox()
driver.get("http://47.92.29.3:8080/musicplay/login.html")
time.sleep(2)
driver.find_element_by_css_selector("#user").send_keys("张雨蓉")
time.sleep(2)
driver.find_element_by_css_selector("#password").send_keys("1234")
time.sleep(2)
#此处不用click操作百度一下 用submit
driver.find_element_by_css_selector("#submit").click()
# data = driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[7]/div[2]/span[1]")
# data2=data.text
# print(data2)
# print("hello")
# #打印title 和url
# print (driver.title)
# print(driver.current_url)
# #智能等待 在5s中智能等待
#driver.implicitly_wait(3)
time.sleep(3)
driver.quit()

