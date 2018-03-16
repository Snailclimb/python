# -*- coding: utf-8 -*-
"""
Created on Tue Mar 13 18:55:04 2018

@author: Administrator
"""

from wxpy import Bot,Tuling,embed
bot = Bot(cache_path=True)
my_group = bot.groups().search('群聊名称')[0]  # 记得把名字改成想用机器人的群
tuling = Tuling(api_key='72bce33cb2b248a199d07175225a5264')  # 一定要添加，不然实现不了
@bot.register(my_group, except_self=False)  # 使用图灵机器人自动在指定群聊天
def reply_my_friend(msg):
    print(tuling.do_reply(msg))
embed()