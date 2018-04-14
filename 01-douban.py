import requests
from bs4 import BeautifulSoup
from lxml import etree
import urllib.parse

def douban_data():
    # url 和 headers
    url = 'https://movie.douban.com/cinema/nowplaying/shanghai/'
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko"}
    # 发送请求 获取数据
    response = requests.get(url,headers=headers)
    data = response.content.decode('utf-8')
    # 对数据进行解析
    # 方法一 转换数据类型
    soup = BeautifulSoup(data,'lxml')
    # 获取标签 数据  select返回的是一个list find_all也是一个list,find是一个数据
    # result = soup.select('#26861685 .stitle a')[0].get_text().strip()
    # result = soup.select('#26861685 .stitle a')[0]
    # print(type(result))
    # 方法二 转换标签数据 为lxml类型  //*[@id="nowplaying"]/div[2]/ul/li/ul/li[2]/a/text()
    html_data = etree.HTML(data)

    # 获取解析出来的url data_new 是list
    data_new = html_data.xpath('//*[@id="nowplaying"]/div[2]/ul/li/ul/li[2]/a/text()')
    # 获取页面所有电影的名字
    result = ''.join(data_new)
    print(result)
if __name__ == '__main__':
    douban_data()