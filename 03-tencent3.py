import json

import requests
from bs4 import BeautifulSoup
import urllib.parse
class Tencent_Spider(object):
    def __init__(self):
        self.base_url = 'https://hr.tencent.com/position.php?'
        self.headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko"}
        # 添加数据时使用
        self.dict_list = []
        # page
        self.page = 0
    # 发送请求 获取数据
    def send_request(self,url,params={}):
        try:
            data = requests.get(self.base_url,params=params,headers=self.headers).content
            # print(data)
            return data
        except Exception as e:
            print(e)


    # 解析数据
    def analysis_data(self,data):
        # 转换类型
        soup = BeautifulSoup(data,'lxml')

        # 取出数据 取出每一行的tr  data是list
        tr_list = soup.select('.even,.odd')
        # 遍历列表 获取每一个tr 再取出每一行的内容
        for tr in tr_list:
            item_dict = {}
            # 职位
            item_dict['work_name'] = tr.select('td a')[0].get_text()
            # 职位类别
            item_dict['work_object'] = tr.select('td')[1].get_text()
            # 人数
            item_dict['work_num'] = tr.select('td')[2].get_text()
            # 地点
            item_dict['work_place'] = tr.select('td')[3].get_text()
            # 发布时间
            item_dict['clain_time'] = tr.select('td')[4].get_text()
            self.dict_list.append(item_dict)
            # print(self.dict_list)
        # 根据最大页数来获取数据
        big_page = soup.select('.pagenav a')[-2].get_text()
        return big_page
    # 保存文件
    def write_file(self):
        # 把字典转换成字符串  list--> dic
        # 将列表写入文件
        json.dump(self.dict_list,open('tencent1.json','w'))
        # data_str = json.dumps(self.dict_list)
        # with open('tencent.html','w') as f:
        #     f.write(data)

    # 调度
    def start_work(self):

        # 拼接参数
        params = {
            'lid':'0',
            'tid':'0',
            'keywords':'python',
            'start':self.page,
        }
        # 发送请求
        data = self.send_request(self.base_url,params=params)
        # print(type(data))
        data = data.decode('utf-8')
        # 解析数据  获取最大页数
        big_page = self.analysis_data(data)
        big_page = int(big_page)
        for page in range(10,(big_page-1)*10,10):
            # 拼接参数
            params = {
                'lid': '0',
                'tid': '0',
                'keywords': 'python',
                'start': page,
            }
            print(page)
            # 发送请求
            data = self.send_request(self.base_url,params=params)
            self.analysis_data(data)
        # 保存文件
        self.write_file()

if __name__ == '__main__':
    tool = Tencent_Spider()
    tool.start_work()