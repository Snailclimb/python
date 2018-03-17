# -*- coding: utf-8 -*-
"""
Created on Tue Mar 13 12:53:20 2018

@author: Administrator
"""

# 爬取网易云音乐的爬虫
# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import urllib.request
import urllib

#获取网页
def gethtml(url, headers={}):
    req = urllib.request.Request(url, headers=headers)
    response = urllib.request.urlopen(req)
    content = response.read().decode('utf-8')
    response.close()
    return content

#解析音乐列表网页
def parsehtmlMusicList(html):
    soup = BeautifulSoup(html, 'lxml')
    list_pic = soup.select('ul#m-pl-container li div img')
    list_nameUrl = soup.select('ul#m-pl-container li div a.msk')
    list_num = soup.select('div.bottom span.nb')
    list_author = soup.select('ul#m-pl-container li p a')
    n = 0
    length = len(list_pic)
    while n < length:
        print('歌单图片：'+list_pic[n]['src']+'\n\n')
        print('歌单名称：'+list_nameUrl[n]['title']+'\n\n歌单地址：'+list_nameUrl[n]['href']+'\n\n')
        print('歌单播放量：'+list_num[n].text+'\n\n')
        print('歌单作者：'+list_author[n]['title']+'\n\n作者主页：'+list_author[n]['href']+'\n\n\n')
        n += 1


url = 'http://music.163.com/discover/playlist'
url = gethtml(url, headers={
    'User-Agent': 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)',
    'Host': 'music.163.com'
})
parsehtmlMusicList(url) 