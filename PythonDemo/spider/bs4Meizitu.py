# -*- coding: utf-8 -*-
"""
Created on Mon Mar 12 22:20:22 2018

@author: Administrator
@description： BeautifulSoup抓取美女图片
"""

import requests
from bs4 import BeautifulSoup
import os,re
#导入所需要的模块
class mzitu():
    def all_url(self, url):
        html = self.request(url)##
        all_a = BeautifulSoup(html.text, 'lxml').find('div', class_='all').find_all('a', href=re.compile('[0~9]'))
        for a in all_a:
            title = a.get_text()
            print('------开始保存：', title) 
            path = str(title).replace("?", '_') ##替换掉带有的？
            self.mkdir(path) ##调用mkdir函数创建文件夹！这儿path代表的是标题title
            href = a['href']
            self.html(href) 

    def html(self, href):   ##获得图片的页面地址并保存图片
        html = self.request(href)
        max_span = BeautifulSoup(html.text, 'lxml').find('div', class_='pagenavi').find_all('span')[-2].get_text()
        #这个上面有提到
        for page in range(1, int(max_span) + 1):
            page_url = href + '/' + str(page)
            self.img(page_url) ##调用img函数

    def img(self, page_url): ##处理图片页面地址获得图片的实际地址
        img_html = self.request(page_url)
        img_url = BeautifulSoup(img_html.text, 'lxml').find('div', class_='main-image').find('img')['src']
        self.save(img_url)

    def save(self, img_url): ##保存图片
        name = img_url[-9:-4]
        img = self.request(img_url)
        f = open(name + '.jpg', 'ab')
        f.write(img.content)
        f.close()

    def mkdir(self, path): ##创建文件夹
        path = path.strip()
        isExists = os.path.exists(os.path.join("E:\mzitu2", path))
        if not isExists:
            print('建了一个名字叫做', path, '的文件夹！')
            os.makedirs(os.path.join("E:\mzitu2", path))
            os.chdir(os.path.join("E:\mzitu2", path)) ##切换到目录
            return True
        else:
            print( path, '文件夹已经存在了！')
            return False

    def request(self, url): ##这个函数获取网页的response 然后返回
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.110 Safari/537.36',
            'referer': "http://www.mzitu.com/100260/2" #伪造一个访问来源    
                     }
        content = requests.get(url, headers=headers)
        return content
#设置启动函数
def main():
    Mzitu = mzitu() ##实例化
    Mzitu.all_url('http://www.mzitu.com/all') ##给函数all_url传入参数  

main()