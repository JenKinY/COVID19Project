import requests
from config_api import *


# 近期31省区市本土病例等级排序 5个 list
def get_china_grade_city_data():
    response = requests.get(GRADE_CITY_DETAIL)
    original_json_data = response.json()

    # "nowConfirm": 现有确诊,
    # "confirm": 累计确诊,
    # "dead": 死亡人数,
    # "heal": 治愈人数,
    # "date": "日期",
    # "sdate": "12/14",
    # "province": "省份",
    # "city": "城市",
    # "confirmAdd": 新增确诊,
    # "grade": "风险等级"

    # print("近期31省区市本土病例及风险等级排序：")
    # print(original_json_data['data']['statisGradeCityDetail'])

    return original_json_data['data']['statisGradeCityDetail']


if __name__ == '__main__':
    print(get_china_grade_city_data())
