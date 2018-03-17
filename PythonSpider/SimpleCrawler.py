import json
import requests 
class SimpleCrawler: 
    init_url = "https://zhuanlan.zhihu.com/api/columns/pythoneer/followers"
    offset = 0 
    def crawl(self, params = None): #必须指定UA， 否则知乎服务器会判定请求不合法 
        headers = {
                   "Host": "zhuanlan.zhihu.com",
                   "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                   "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36",
       }
        response = requests.get(self.init_url, headers = headers, params = params) 
        print(response.url) 
        data = response.json()# 7000 表示所有关注量# 分页加载更多， 递归调用
        while self.offset < 7000: 
              self.parse(data) 
              self.offset += 20 
              params = {
                      "limit": 20,
                       "offset": self.offset
                      }
              self.crawl(params) 
    def parse(self, data): 
    #以json格式存储到文件 
        with open("followers.json", "a", encoding = "utf-8") as f: 
             for item in data:
                 f.write(json.dumps(item)) 
                 f.write('\n') 
if __name__ == '__main__': 
    SimpleCrawler().crawl();