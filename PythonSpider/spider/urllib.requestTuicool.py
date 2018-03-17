# -*- coding: utf-8 -*-
"""
不带Http请求头的访问方法
"""

import urllib.request
print("第一种方法：")
response1=urllib.request.urlopen('https://www.tuicool.com/')
html=response1.read().decode('utf-8')
print("输出状态码：")
print(response1.getcode())