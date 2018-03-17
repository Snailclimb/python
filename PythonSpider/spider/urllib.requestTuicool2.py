# -*- coding: utf-8 -*-
"""
带http请求头的访问方法
"""
import urllib.request
print("第二种方法：")
request = urllib.request.Request('https://www.tuicool.com/')
request.add_header("user-agent","Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:60.0) Gecko/20100101")
response1=urllib.request.urlopen(request)
html=response1.read().decode('utf-8')
print("输出状态码：")
print(response1.getcode())
print("输出文本长度：")
print(len(html))
print(html)
