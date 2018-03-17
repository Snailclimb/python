# -*- coding: utf-8 -*-
"""
不实用http请求头，一些网站可能无法爬取
"""

# coding utf-8  
import requests  
      
def get_content():  
    html = requests.get("https://www.tuicool.com/")  
    return html.text  
      
print(get_content())  