from flask import Flask, render_template
from util import overview_data, grade_city_data, asymptomatic_province_data
import requests

app = Flask(__name__)


@app.route('/get')
def get_json_data():
    return 'get_json_data'


@app.route('/')
def show():
    china_overview_data = overview_data.get_overview_data()
    china_add_overview_data = overview_data.get_china_day_add_list()
    grade_city_data_list = grade_city_data.get_china_grade_city_data()

    # 全国城市疫情个数
    china_city_statis = overview_data.get_china_city_statis()

    # 现有无症状感染者
    now_asy_data = asymptomatic_province_data.get_asymptomatic_province()
    # 新增无症状感染者
    add_asy_data = asymptomatic_province_data.get_asymptomatic_add_province()

    return render_template('showData.html', china_overview_data=china_overview_data,
                           china_add_overview_data=china_add_overview_data, china_city_statis=china_city_statis,
                           grade_city_data_list=grade_city_data_list,
                           now_asy_data=now_asy_data, add_asy_data=add_asy_data)


if __name__ == '__main__':
    app.run()
