# -*- coding: utf-8 -*-
"""
使用http请求头
"""

# coding utf-8  
import requests  
      
def get_content():  
    header = {  
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36'  
    }  
    html = requests.get("https://www.tuicool.com/",headers=header)
    return html.text  
      
print(get_content())  