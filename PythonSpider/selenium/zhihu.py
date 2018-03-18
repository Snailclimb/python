# -*- coding: utf-8 -*-
"""
Created on Sat Mar 17 18:30:06 2018

@author: Administrator
"""

from selenium import webdriver
## 创建浏览器对象
browser = webdriver.Firefox()
## 打开小米社区网站
browser.get('https://www.zhihu.com/signin?next=%2F')
browser.find_element_by_xpath("/html/body/div[1]/div/main/div/div/div/div[2]/div[1]/form/div[1]/div[2]/div[1]/input").clear()#清空输入框
browser.find_element_by_xpath("/html/body/div[1]/div/main/div/div/div/div[2]/div[1]/form/div[1]/div[2]/div[1]/input").send_keys("18163138155")#输入账号
browser.find_element_by_xpath("/html/body/div[1]/div/main/div/div/div/div[2]/div[1]/form/div[2]/div/div[1]/input").clear()#清空输入框
browser.find_element_by_xpath("/html/body/div[1]/div/main/div/div/div/div[2]/div[1]/form/div[2]/div/div[1]/input").send_keys("ks1996721kr")#输入密码
browser.find_element_by_xpath("/html/body/div[1]/div/main/div/div/div/div[2]/div[1]/form/button").click()#登录
