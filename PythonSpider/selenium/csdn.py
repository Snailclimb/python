# -*- coding: utf-8 -*-
"""
Created on Sat Mar 17 18:30:06 2018

@author: Administrator
"""

from selenium import webdriver
## 创建浏览器对象
browser = webdriver.Firefox()
## 打开小米社区网站
browser.get('https://passport.csdn.net/account/login')
browser.find_element_by_xpath("//*[@id='username']").clear()#清空输入框
browser.find_element_by_xpath("//*[@id='username']").send_keys("1361583339@qq.com")#输入账号
browser.find_element_by_xpath("//*[@id='password']").clear()#清空输入框
browser.find_element_by_xpath("//*[@id='password']").send_keys("ks1996721kr")#输入密码
browser.find_element_by_xpath("/html/body/div[4]/div/div/div[2]/div/div[1]/div/form/input[8]").click()#登录
