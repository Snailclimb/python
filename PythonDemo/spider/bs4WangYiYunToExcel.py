# -*- coding: utf-8 -*-
"""
Created on Tue Mar 13 15:11:32 2018

@author: Administrator
"""

from bs4 import BeautifulSoup
import urllib.request
import urllib
import xlwt 

#获取网页
def gethtml(url, headers={}):
    req = urllib.request.Request(url, headers=headers)
    response = urllib.request.urlopen(req)
    content = response.read().decode('utf-8')
    response.close()
    return content
def set_style(name, height, bold = False):  
    style = xlwt.XFStyle()   #初始化样式  
      
    font = xlwt.Font()       #为样式创建字体  
    font.name = name  
    font.bold = bold  
    font.color_index = 4  
    font.height = height  
      
    style.font = font  
    return style  

#解析音乐列表网页
def parsehtmlMusicList(html):
    soup = BeautifulSoup(html, 'lxml')
    list_pic = soup.select('ul#m-pl-container li div img')
    list_nameUrl = soup.select('ul#m-pl-container li div a.msk')
    list_num = soup.select('div.bottom span.nb')
    list_author = soup.select('ul#m-pl-container li p a')
    n = 0
    length = len(list_pic)
    #创建工作簿  
    workbook = xlwt.Workbook(encoding='utf-8')    
    #创建sheet  
    data_sheet = workbook.add_sheet('demo')    
    row0 = [u'歌单介绍', u'歌曲链接地址', u'歌曲播放次数', u'歌单作者']   
    data_sheet.col(0).width = 9999#设置单元格宽度
    data_sheet.col(1).width = 9999#设置单元格宽度
    data_sheet.col(2).width = 4444#设置单元格宽度
    data_sheet.col(3).width = 3333#设置单元格宽度
    data_sheet.col(4).width = 3333#设置单元格宽度
    #生成第一行和第二行  
    for i in range(len(row0)):  
        data_sheet.write(0, i, row0[i], set_style('Times New Roman', 220, True))
    while n < length:
        description=list_nameUrl[n]['title']#歌单介绍
        songhref= list_nameUrl[n]['href']
        num=list_num[n].text#歌曲播放量
        #picture=list_pic[n]['src']#图片链接地址
        author=list_author[n]['title']#歌单作者
        row=[description, songhref, num, author]
        #print('歌单图片：'+list_pic[n]['src']+'\n\n')
        #print('歌单名称：'+list_nameUrl[n]['title']+'\n\n歌单地址：'+list_nameUrl[n]['href']+'\n\n')
        #print('歌单播放量：'+list_num[n].text+'\n\n')
        #print('歌单作者：'+list_author[n]['title']+'\n\n作者主页：'+list_author[n]['href']+'\n\n\n')
        n += 1
        for i in range(len(row)):
            data_sheet.write(n, i, row[i], set_style('Times New Roman', 220, True))
    workbook.save('C:/Users/Administrator/Desktop/xlwtDemo.xls')
url = 'http://music.163.com/discover/playlist'
url = gethtml(url, headers={
    'User-Agent': 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)',
    'Host': 'music.163.com'
})
parsehtmlMusicList(url)

    
