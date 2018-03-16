# -*- coding: utf-8 -*-
"""
朋友圈朋友签名的词云生成以及
签名情感分析
"""
import re,jieba,itchat
import jieba.analyse
import numpy as np
from PIL import Image
from snownlp import SnowNLP
from wordcloud import WordCloud
import matplotlib.pyplot as plt
itchat.auto_login(hotReload=True)
friends = itchat.get_friends(update=True)
def analyseSignature(friends):
    signatures = ''
    emotions = []
    for friend in friends:
        signature = friend['Signature']
        if(signature != None):
            signature = signature.strip().replace('span', '').replace('class', '').replace('emoji', '')
            signature = re.sub(r'1f(\d.+)','',signature)
            if(len(signature)>0):
                nlp = SnowNLP(signature)
                emotions.append(nlp.sentiments)
                signatures += ' '.join(jieba.analyse.extract_tags(signature,5))
    with open('signatures.txt','wt',encoding='utf-8') as file:
         file.write(signatures)

    # 朋友圈朋友签名的词云相关属性设置
    back_coloring = np.array(Image.open('alice_color.png'))
    wordcloud = WordCloud(
        font_path='simfang.ttf',
        background_color="white",
        max_words=1200,
        mask=back_coloring, 
        max_font_size=75,
        random_state=45,
        width=1250, 
        height=1000, 
        margin=15
    )
    
    #生成朋友圈朋友签名的词云
    wordcloud.generate(signatures)
    plt.imshow(wordcloud)
    plt.axis("off")
    plt.show()
    wordcloud.to_file('signatures.jpg')#保存到本地文件

    # Signature Emotional Judgment
    count_good = len(list(filter(lambda x:x>0.66,emotions)))#正面积极
    count_normal = len(list(filter(lambda x:x>=0.33 and x<=0.66,emotions)))#中性
    count_bad = len(list(filter(lambda x:x<0.33,emotions)))#负面消极
    labels = [u'负面消极',u'中性',u'正面积极']
    values = (count_bad,count_normal,count_good)
    plt.rcParams['font.sans-serif'] = ['simHei'] 
    plt.rcParams['axes.unicode_minus'] = False
    plt.xlabel(u'情感判断')#x轴
    plt.ylabel(u'频数')#y轴
    plt.xticks(range(3),labels)
    plt.legend(loc='upper right',)
    plt.bar(range(3), values, color = 'rgb')
    plt.title(u'%s的微信好友签名信息情感分析' % friends[0]['NickName'])
    plt.show()
analyseSignature(friends)