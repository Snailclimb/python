# -*- coding: utf-8 -*-
"""
Created on Sat Mar 17 17:06:02 2018

@author: Administrator
"""

## 引入WebDriver的包
from selenium import webdriver
from bs4 import BeautifulSoup
## 创建浏览器对象
browser = webdriver.Firefox()
## 打开小米社区网站
browser.get('https://account.xiaomi.com/pass/serviceLogin?callback=http%3A%2F%2Fbbs.xiaomi.cn%2Flogin%2Fcallback%3Ffollowup%3Dhttp%253A%252F%252Fbbs.xiaomi.cn%252F%26sign%3DM2E4MTg3MzE3MGJmZGFiMTc0MTE5NmNjZTAyYWNmMDZhNTEwOTU2NQ%2C%2C&sid=new_bbs_xiaomi_cn&_locale=zh_CN')
browser.find_element_by_xpath("//*[@id='username']").clear()#清空输入框
browser.find_element_by_xpath("//*[@id='username']").send_keys("18163138155")#输入账号
browser.find_element_by_xpath("//*[@id='pwd']").clear()#清空输入框
browser.find_element_by_xpath("//*[@id='pwd']").send_keys("ks1996721kr")#输入密码
browser.find_element_by_xpath("//*[@id='login-button']").click()#登录
base_url="http://bbs.xiaomi.cn/d-{page}"
for i in range(1,6):
    url=base_url.format(page=i)
    browser.get(url)
    bs4=BeautifulSoup(browser.page_source,'lxml')
    titles=bs4.find_all('div', {'class':'title'})
    for title in titles:
        title_content=title.get_text().strip('\n')
        print(title_content)
