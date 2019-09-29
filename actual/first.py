import requests
import pandas as pd
from bs4 import BeautifulSoup


def get_request(url):
    response = requests.get(url)
    print("encoding = ", response.encoding)
    #  response.encoding = "gbk"
    c = response.content
    #  转码替换
    html = str(c, "gbk")
    #  print(str(html))
    #  html解析
    bs = BeautifulSoup(html, "html.parser")
    texts = bs.find_all('div', class_='showtxt')

    print(texts[0])
    # 解析结果里的文本
    str_content = str(texts[0].text)
    print(str_content)
    # 因为目标文件的编码是"utf-8"的，所以打开时要设置编码格式
    f = open("first.txt", "w", encoding='utf-8')
    # 写入时过滤掉不需要的字符&nbsp;  (8个空格符)
    f.writelines(str_content.replace('\xa0' * 8, '\n\n'))
    f.close()

    # print(texts[0].text.replace('\xa0'*8,'\n\n'))
    # print(texts)


class FirstTest:
    url = "https://www.biqukan.com/24_24125/8458043.html"
    url1 = "http://docs.python-requests.org/zh_CN/latest/user/quickstart.html"


if __name__ == '__main__':
    ft = FirstTest()
    get_request(ft.url)
