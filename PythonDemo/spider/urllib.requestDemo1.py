# -*- coding: utf-8 -*-
"""
Created on Mon Mar 12 17:25:58 2018

@author: Snaliclimb
@description: urllib.request的三种使用
"""
import urllib.request,http.cookiejar
print("第一种方法：")
response1=urllib.request.urlopen('http://www.baidu.com')
html=response1.read()
print("输出状态码：")
print(response1.getcode())
print("输出文本长度：")
print(len(html))

print("第二种方法：")
request = urllib.request.Request('http://www.baidu.com')
request.add_header("user-agent","Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:60.0) Gecko/20100101")
response1=urllib.request.urlopen(request)
html=response1.read()
print("输出状态码：")
print(response1.getcode())
print("输出文本长度：")
print(len(html))

print("第三种方法：")
cj = http.cookiejar.CookieJar()
opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))
urllib.request.install_opener(opener)
response3 = urllib.request.urlopen('http://www.baidu.com')
print(response3.getcode())
print(cj)
print(response3.read())