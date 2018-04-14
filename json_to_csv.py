import json
import csv
def json_to_dict():
    # json文件读取
    json_file = open('tencent1.json','r')
    # print(json_file)
    # csv文件写入
    csv_file = open('csv.csv','w')
    # csv 的读写器 对象
    csv_writer = csv.writer(csv_file)
    # 转换json_file的类型 json_file是一个对象 转换成为一个list  通过load转换成为列表
    data_list = json.load(json_file)
    # print(data_list)
    # 取出表头  sheets是列表
    sheets = data_list[0].keys()
    # print(type(sheets))
    # print(sheets)
    # 取出内容  data_dict.values()是所有值的内容以元祖形式存储，只有一个列表元素
    content_list = []
    for data_dict in data_list:
        # print(data_dict.values())
        content_list.append(data_dict.values())

    # 写入表头 写入内容是列表的形式
    csv_writer.writerow(sheets)
    # 写入内容  需要使用列表的形式写入
    csv_writer.writerows(content_list)
    #关闭csv
    csv_file.close()
    # 关闭json 文件
    json_file.close()
if __name__ == '__main__':
    json_to_dict()