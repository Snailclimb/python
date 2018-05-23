# -*- coding: utf-8 -*-
__author__ = "liuzhijun"

import requests









def crawl():
    # url中的参数需要根据自己的情况做调整
    url = "https://mp.weixin.qq.com/mp/profile_ext?action=home&__biz=MzU4NDQ4MzU5OA==&scene=124&"

    headers = """
Host: mp.weixin.qq.com
Connection: keep-alive
User-Agent: Mozilla/5.0 (Linux; Android 7.0; FRD-AL10 Build/HUAWEIFRD-AL10; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.132 MQQBrowser/6.2 TBS/44068 Mobile Safari/537.36 MicroMessenger/6.6.6.1300(0x26060636) NetType/WIFI Language/zh_CN
x-wechat-key: e4d0b85bfed5799347d003048a6b2808543504e012e45917fa9963daf81d43fb5bb1033e428d2363c71bf081895cb4e5e31cb1d4c7cfe3cfbc1a1818bcb44e8796bd595ba7dbbcb009578a5e8298e07e
x-wechat-uin: MzIwMjA1OTM3
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,image/wxpic,image/sharpp,image/apng,*/*;q=0.8
Accept-Encoding: gzip, deflate
Accept-Language: zh-CN,zh-CN;q=0.8,en-US;q=0.6
Cookie: sd_userid=24811523971059409; sd_cookie_crttime=1523971059409; pgv_pvid=5490707453; pgv_info=ssid=s5182460012; rewardsn=; wxtokenkey=777; wxuin=320205937; devicetype=android-24; version=26060636; lang=zh_CN; pass_ticket=0iXHmW5c7/qdielT0m3lOeuxrLCMdn31Wc+lwcDdeScap7bw8BjSC1U7tLHbRLIN; wap_sid2=CPHo15gBElxlZmFuaVRkbTlERFlJblFGRXFBeVlKSmNMbWRJRXdfNTJEdU1sSjlNTmdTd0gyemg3WXRMVjFoTTVGSHZfNGVTRDlYdnE5d2JwZ1ppMU95dFBhVGowcnNEQUFBfjD0vqvXBTgNQJVO
Q-UA2: QV=3&PL=ADR&PR=WX&PP=com.tencent.mm&PPVN=6.6.6&TBSVC=43607&CO=BK&COVC=044068&PB=GE&VE=GA&DE=PHONE&CHID=0&LCID=9422&MO= FRD-AL10 &RL=1080*1794&OS=7.0&API=24
Q-GUID: 53abc69bd03d1e8b8bb80ef3117888cb
Q-Auth: 31045b957cf33acf31e40be2f3e71c5217597676a9729f1b
    """
    headers = headers_to_dict(headers)
    response = requests.get(url, headers=headers, verify=False)
    print(response.text)
    if '<title>验证</title>' in response.text:
        raise Exception("获取微信公众号文章失败，可能是因为你的请求参数有误，请重新获取")
    data = extract_data(response.text)
    for item in data:
        print(item)


def extract_data(html_content):
    """
    从html页面中提取历史文章数据
    :param html_content 页面源代码
    :return: 历史文章列表
    """
    import re
    import html
    import json

    rex = "msgList = '({.*?})'"
    pattern = re.compile(pattern=rex, flags=re.S)
    match = pattern.search(html_content)
    if match:
        data = match.group(1)
        data = html.unescape(data)
        data = json.loads(data)
        articles = data.get("list")
        for item in articles:
            print(item)
        return articles


def headers_to_dict(headers):
    """
    将字符串
    '''
    Host: mp.weixin.qq.com
    Connection: keep-alive
    Cache-Control: max-age=
    '''
    转换成字典类型
    :param headers: str
    :return: dict
    """
    headers = headers.split("\n")
    d_headers = dict()
    for h in headers:
        h = h.strip()
        if h:
            k, v = h.split(":", 1)
            d_headers[k] = v.strip()
    return d_headers


if __name__ == '__main__':
    crawl()