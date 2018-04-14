import requests
# from bs4 import BeautifulSoup
import urllib.parse
class Tencent_Spider(object):
    def __init__(self):
        self.base_url = 'https://hr.tencent.com/position.php?'
        self.headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko"}

    # 发送请求 获取数据
    def send_request(self,url,params={}):
        try:
            data = requests.get(self.base_url,params=params,headers=self.headers).content
            return data
        except Exception as e:
            print(e)


    # 解析数据
    def analysis_data(self):
        pass

    # 保存文件
    def write_file(self,data):
        with open('tencent.html','w') as f:
            f.write(data)

    # 调度
    def start_work(self):
        # 拼接参数
        params = {
            'lid':2175,
            'tid':87,
            'keywords':'python',
            'start':0,
        }
        # params_str = urllib.parse(params)
        # new_url =self.base_url + params_str
        # 发送请求
        data = self.send_request(self.base_url,params=params)
        data = data.decode('utf-8')
        # 解析数据

        # 保存文件
        self.write_file(data)

if __name__ == '__main__':
    tool = Tencent_Spider()
    tool.start_work()