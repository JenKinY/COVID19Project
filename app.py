from flask import Flask, render_template, make_response, send_file
from util import overview_data, grade_city_data, asymptomatic_province_data,save_json2csv
import time

app = Flask(__name__)


@app.route('/download_content')
def download_content():
    # 发送 content 内容 下载
    content = "long text"
    response = make_response(content)
    response.headers["Content-Disposition"] = "p_w_upload; filename=myfilename.txt"
    return response

@app.route('/download_file')
def download_file():

    # 保存数据到服务器
    save_json2csv.save_file_server()

    nowdate = time.strftime("%Y-%m-%d_%H:%M:%S", time.localtime())
    # 下载服务器内容
    response = make_response(send_file("./static/wait_download_file/china_overview_data.csv"))
    response.headers["Content-Disposition"] = "p_w_upload; filename="+nowdate+"COVID19-CHINA-OVERVIEW-DATA.csv;"
    return response


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
