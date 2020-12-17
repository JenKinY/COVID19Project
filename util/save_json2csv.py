import os
import time

import requests
from config_api import CHINA_DAY_LIST_API, GRADE_CITY_DETAIL, ASYMPTOMATICP_ROVINCE

# 处理 JSON 数据，保存到 .cvs 文件

# 国内概览数据原始 JSON
cdl_original_json = requests.get(CHINA_DAY_LIST_API).json()


# 根据 API 返回原始 JSON 数据
def save_china_day_list():
    target_json = cdl_original_json['data']
    # target_json = cdl_original_json['data']['chinaDayList'][-1]

    # with open("FFFFFFFFFFFF.csv", 'w', newline='')as c:
    #     file_name = ['first_name', 'last_name']
    #     writer = csv.DictWriter(c, fieldnames=file_name)
    #     # 写入列标题，即DictWriter构造方法的fieldnames参数
    #     writer.writeheader()
    #     # 写入值
    #     # writer.writerow({"first_name": "55", "last_name": "666"})
    #     # writer.writerow({"first_name": "77", "last_name": "88"})
    #     for item in target_json:
    #         writer.writerow(item)
    # with open('mycsvfile.csv', 'wb') as f:
    #     keys = ["治愈率", "疑似", "死亡数", "nowConfirm", "现在重症", "境外输入", "死亡率", "累计确证", "治愈人数", "日期", "无症状"]
    #     w = csv.writer(f)
    # w.writerow(keys)
    # w.writerow(target_json.values())
    # print(type(target_json.values())
    # print(target_json.values())

    return target_json

    # 写入数据


def write_data():
    target_json = cdl_original_json['data']
    data = target_json
    if data == -1:
        print('no data')
        return
    # 获取日期
    month = str(time.localtime()[1])
    day = str(time.localtime()[2])
    # 打开文件
    curPath = 'static/wait_download_file/'
    if not os.path.exists(curPath):
        os.mkdir(curPath)
    # print(curPath + month + '-' + day + '.COVID19-CHINA国内概览数据.csv')
    print(curPath+'china_overview_data.csv')
    fp = open(curPath+ 'china_overview_data.csv', 'w+')
    chinaDayList = data['chinaDayList']
    print(chinaDayList[-1])
    fp.write(
        str('ID') + ',' + str('日期') + ',' + str('累计确诊') + ',' + str('当日确证人数') + ',' + str('当日重症') + ',' + str(
            '境外输入') + ',' + str(
            '无症状感染者') + ',' + str('疑似病例') + ',' + str('治愈人数') + ',' + str('死亡人数') + ',' + str('治愈率') + ',' + str('死亡率'))
    fp.write('\n')
    # 写入数据
    for num in range(0, len(chinaDayList)):
        day_info = chinaDayList[num]
        date = day_info['date']  # 日期
        confirm = day_info['confirm']  # 累计确诊
        nowConfirm = day_info['nowConfirm']  # 当日确证人数
        nowSevere = day_info['nowSevere']  # 当日重症
        importedCase = day_info['importedCase']  # 境外输入
        noInfect = day_info['noInfect']  # 无症状感染者
        suspect = day_info['suspect']  # 疑似病例
        heal = day_info['heal']  # 治愈人数
        dead = day_info['dead']  # 死亡人数
        healRate = day_info['healRate']  # 治愈率
        deadRate = day_info['deadRate']  # 死亡率
        fp.write(
            (str(num + 1) + ',' + str(date) + ',' + str(confirm) + ',' + str(nowConfirm) + ',' + str(
                nowSevere) + ',' + str(
                importedCase)
             + ',' + str(noInfect) + ',' + str(suspect) + ',' + str(heal) + ',' + str(dead) + ',' + str(
                        healRate) + ',' + str(deadRate)).encode(
                'utf-8').decode('utf-8'))
        fp.write('\n')
    fp.close()

def save_file_server():
    write_data()
    print("保存到服务器成功^_^")

#
# if __name__ == '__main__':
#     print(save_china_day_list())
#     write_data(data=save_china_day_list())
