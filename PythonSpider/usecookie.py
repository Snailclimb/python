#coding:utf-8  
import sys  
import io  
import urllib.request  
import http.cookiejar  
  
################## 第二种登陆方式 ##################  
################## 模拟登录后再携带得到的cookie访问 ##################  
  
# #改变标准输出的默认编码  
#sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf8')  
  
  
# # 登陆信息  
# # 登录后才能访问的网站  
url = 'http://221.233.24.23/eams/login.action'  
login_url = "http://221.233.24.23/eams/login.action"  
login_username = "201503402"  
login_password = "201503402"  
  
#登录时需要POST的数据  
login_data = {  
   "username" : login_username,  
     "password" : login_password  
 }  
post_data = urllib.parse.urlencode(login_data).encode('utf-8')  
  
# #设置请求头  
headers = {'User-agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36'}  
# #构造登录请求  
req = urllib.request.Request(login_url, headers = headers, data = post_data)  
  
  
# #构造cookie  
cookie = http.cookiejar.CookieJar()  
  
# #由cookie构造opener  
opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cookie))  
  
  
# #发送登录请求，此后这个opener就携带了cookie，以证明自己登录过  
resp = opener.open(req)  
  
# #构造访问请求  
req = urllib.request.Request(url, headers = headers)  
  
resp = opener.open(req)  
  
print(resp.read().decode('utf-8'))  