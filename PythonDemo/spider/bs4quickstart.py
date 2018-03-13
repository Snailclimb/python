# -*- coding: utf-8 -*-
"""
Created on Mon Mar 12 20:17:37 2018

@author: Administrator
@description： BeautifulSoup快速开始案例
"""
html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""
from bs4 import BeautifulSoup
import re
soup = BeautifulSoup(html_doc,"lxml")
print("从文档中找到所有<a>标签的链接:")
for link in soup.find_all('a'):
    print(link.get('href'))
print("正则表达式匹配：")
link_node=soup.find('a',href=re.compile(r"illi"))
print("标签名：",link_node.name)
print("链接属性：",link_node.get('href'))
print("标签文字：",link_node.text)
print("根据class获取相应段落文字：")
p_node=soup.find('p' ,"story")
print(p_node.get_text())
print(soup.title)#<title>The Dormouse's story</title>
print(soup.title.name)#title
print(soup.title.parent.name)#head
print(soup.title.string)#The Dormouse's story
print(soup.title.text)#The Dormouse's story
#print(soup.get_text())#从文档中获取所有文字内容: