import requests
from config_api import *


# 现有无症状感染者省份数据 18 lsit
def get_asymptomatic_province():
    response = requests.get(ASYMPTOMATICP_ROVINCE)
    original_json_data = response.json()

    # "province": "省份",
    # "increase": 新增数量,
    # "confirm": 已有无症状感染者数量

    # print("现有无症状感染者省份数据：")
    # print(original_json_data['data']['asymptomaticProvince']['confirm'])

    return original_json_data['data']['asymptomaticProvince']['confirm']

# 新增无症状感染者省份数据 18 lsit
def get_asymptomatic_add_province():
    response = requests.get(ASYMPTOMATICP_ROVINCE)
    original_json_data = response.json()

    # "province": "省份",
    # "increase": 新增数量,
    # "confirm": 已有无症状感染者数量

    # print("现有无症状感染者省份数据：")
    # print(original_json_data['data']['asymptomaticProvince']['increase'])

    return original_json_data['data']['asymptomaticProvince']['increase']


if __name__ == '__main__':
    print(get_asymptomatic_province())
    print(get_asymptomatic_add_province())
