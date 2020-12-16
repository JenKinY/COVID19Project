import requests

response = requests.get('https://news.qq.com/zt2020/page/feiyan.htm')
print(response.text)