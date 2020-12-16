import requests
from config_api import *


# 返回概览数据 dict
def get_overview_data():
    response = requests.get(CHINA_DAY_LIST_API)
    original_json_data = response.json()

    # 取最后一个元素(也就是今天的数据)
    # dict 数据说明：
    # confirm 累计确诊
    # importedCase 境外输入
    # date 日期
    # noInfect 无症状感染者
    # suspect 疑似病例
    # dead 累计死亡
    # heal 累计治愈
    # nowConfirm 现有确诊
    # nowSevere 现有重症
    # deadRate 死亡率
    # healRate 治愈率

    # print("今日数据概览：")
    # print(original_json_data['data']['chinaDayList'][-1])

    return original_json_data['data']['chinaDayList'][-1]


# 返回今日对比前一日数据 dict
def get_china_day_add_list():
    response = requests.get(CHINA_DAY_LIST_API)
    original_json_data = response.json()

    # "healRate": "治愈率",
    # "date": "日期",
    # "confirm": 累计确诊,
    # "suspect": 疑似病例,
    # "heal": 治愈,
    # "importedCase": 境外输入,
    # "infect": 无症状感染者,
    # "dead": 死亡数,
    # "deadRate": "死亡率"

    # print("今日对比前一日数据：")
    # print(original_json_data['data']['chinaDayAddList'][-1])

    return original_json_data['data']['chinaDayAddList'][-1]

# 返回国内城市疫情  dict
def get_china_city_statis():
    response = requests.get(CHINA_DAY_LIST_API)
    original_json_data = response.json()

    # "cityStatis": { 国内城市疫情
    #   "confirm": 339, 累计确诊
    #   "zeroNowConfirm": 330, 零病例城市
    #   "notZeroNowConfirm": 9 有病例城市
    # },

    # print("国内城市疫情数据：")
    # print(original_json_data['data']['cityStatis'][-1])

    return original_json_data['data']['cityStatis']




# if __name__ == '__main__':
#     # print(get_overview_data())
#     print(get_china_day_add_list())
#     print(get_china_city_statis())
