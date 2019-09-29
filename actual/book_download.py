import os
import sys

from bs4 import BeautifulSoup
import requests

''' 简单小说下载'''


class Download:
    # 笔趣看首页
    server = 'https://www.biqukan.com'
    # 小说字典{名字:链接}
    book_set = {}
    # 章节字典{名字:链接}
    chapter_set = {}
    # 书籍的目录
    book_path = 'download/book'

    # 获取书籍列表
    def get_book_list(self):
        self.common_parser_child_a(self.server, 'div', 'p10', data_set=self.book_set)

    # 获取章节列表
    def get_chapter_list(self, url):
        self.common_parser_child_a(url, 'div', 'listmain', data_set=self.chapter_set)

    # 按章节写入文件
    def write_in(self, url, book_name, chapter_name):
        if book_name is None or chapter_name is None:
            print("download stop!")
            return
        # 建立下载路径
        path = self.book_path + "/" + book_name
        if not os.path.exists(path):
            os.makedirs(path)
        texts = self.request_all_parser(name='div', class_name='showtxt', url=url)
        print(len(texts))
        for text in texts:
            # 因为目标文件的编码是"utf-8"的，所以打开时要设置编码格式
            with open("{0}/{1}.txt".format(path, chapter_name), "w", encoding='utf-8') as f:
                # 写入时过滤掉不需要的字符&nbsp;  (8个空格符)
                f.write(text.text.replace('\xa0' * 8, '\n\n'))
                f.close()

    # 抽取的公共的解析某div下a标签的方法
    def common_parser_child_a(self, url, name: str, class_name: str, data_set):
        if (url is None) or (name.startswith('a')):
            return
        list_main = self.request_all_parser(class_name, name, url)
        for lm in list_main:
            a_bf = BeautifulSoup(str(lm), "html.parser")
            a = a_bf.find_all('a')
            for each in a:
                # 遍历其中的a标签
                href_ = self.server + each.get('href')
                name = str(each.string)
                # 按条件过滤后存入列表
                if not name.startswith('None'):
                    data_set[name] = href_
        print(data_set)

    ''' 请求html内容 
        class_name: 要解析的标签的class名字,
        name: 要解析的标签名
        url:请求的路径
        :return 返回解析后内容
    '''

    def request_all_parser(self, class_name, name, url):
        # 请求html
        html = requests.get(url)
        # 设置HTML解析
        bs = BeautifulSoup(str(html.content, "gbk"), "html.parser")
        # 获取对应的内容
        list_main = bs.find_all(name, class_=class_name)
        return list_main

    # 演示，问题：未处理一些异常
    def demo(self):
        self.get_book_list()
        # 展示当前小说名字
        for name in self.book_set:
            print(name, end=',')
        download_name = input('\n输入想要下载的小说名称：')
        # 获取章节目录
        print("----获取章节目录----")
        self.get_chapter_list(download.book_set[download_name])
        print("------开始下载----")
        # 遍历下载所有
        c = 0
        for name in download.chapter_set:
            url = download.chapter_set[name]
            self.write_in(url, download_name, name)
            c += 1

        print("-----下载结束-----")


if __name__ == '__main__':
    download = Download()
    download.demo()
