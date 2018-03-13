# -*- coding: utf-8 -*-
"""
Created on Tue Mar 13 19:09:05 2018

@author: Administrator
"""

from wxpy import Bot,Tuling,embed,ensure_one
bot = Bot()
my_friend = ensure_one(bot.search('郑凯'))  #想和机器人聊天的好友的备注
tuling = Tuling(api_key='72bce33cb2b248a199d07175225a5264')
@bot.register(my_friend)  # 使用图灵机器人自动与指定好友聊天
def reply_my_friend(msg):
    tuling.do_reply(msg)
embed()