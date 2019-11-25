import os
import sys
from selenium import webdriver
from bs4 import BeautifulSoup
import requests
import urllib.request
import json
import time

''' 简单视频下载'''


class Download:
    # 主机
    server = 'http://play.chinalink.tv'
    # video_path = 'download/video'
    video_path = 'D:\\video\\game_five\\download\\video'
    downloadUrlList = []
    downloadResList = []
    book_set = {}

    downloadDic = dict()

    # 解析下载清单
    def parse_list_file(self, server: str, url_list: []):
        f = open("download/download_list/120756.txt", "rb")
        # 为了读取一个文件的内容，调用 f.read(size), 这将读取一定数目的数据, 然后作为字符串或字节对象返回。
        # size 是一个可选的数字类型的参数。 当 size 被忽略了或者为负, 那么该文件的所有内容都将被读取并且返回。
        read = f.read()
        content = str(read, "utf-8")
        all_lines = content.split("\n")
        for line in all_lines:
            # print(line)
            if line.startswith(".."):
                temp = line.replace("../../..", server)
                url_list.append(temp)
        print(url_list.__len__())
        # print(url_list)

    def parse_list_file2(self, download_res_list: []):
        f = open("download/download_list/大赛视频.txt", "rb")
        # 为了读取一个文件的内容，调用 f.read(size), 这将读取一定数目的数据, 然后作为字符串或字节对象返回。
        # size 是一个可选的数字类型的参数。 当 size 被忽略了或者为负, 那么该文件的所有内容都将被读取并且返回。
        read = f.read()
        content = str(read, "utf-8")
        all_lines = content.replace("\r", "").split("\n")
        count = 0
        dictTemp = dict()
        for line in all_lines:
            # print(line)
            if count % 2 == 0:
                dictTemp = dict()
            if line.startswith("http"):
                # temp = line.replace("../../..", server)
                dictTemp["url"] = line
            else:
                dictTemp["name"] = line
            count = count + 1
            # print(temp)
            download_res_list.append(dictTemp)
        print(download_res_list)

    def start_download(self):
        self.parse_list_file(self.server, self.downloadUrlList)
        count = 0
        for url in self.downloadUrlList:
            count = count + 1
            file = "result: %s" % count
            # print("downloading with " + file)
            local_path = os.path.join('D:\\video\\game_five\\download\\video', file)
            # os.path.join将多个路径组合后返回
            urllib.request.urlretrieve(url, local_path)

    def download_media(self):
        # 解析文件
        self.parse_list_file(self.server, self.downloadUrlList)
        # 建立下载路径
        if not os.path.exists(self.video_path):
            os.makedirs(self.video_path)

        count = 0
        for url in self.downloadUrlList:
            res = requests.get(url)
            count = count + 1
            video_name = "{0}".format(count)
            if video_name.__len__() < 3:
                if video_name.__len__() < 2:
                    video_name = "00{0}".format(video_name)
                else:
                    video_name = "0{0}".format(video_name)
            file_path = "{0}/{1}.ts".format(self.video_path, video_name)
            with open(file_path, 'ab')as f:
                f.write(res.content)
                f.close()
        print("result: %s" % count)

    def download_video(self):
        self.parse_list_file2(self.downloadResList)
        # 建立下载路径
        if not os.path.exists(self.video_path):
            os.makedirs(self.video_path)

        count = 0
        for resDict in self.downloadResList:
            video_name = resDict["name"]
            video_url = resDict["url"]
            res = requests.get(video_url)
            file_path = "{0}/{1}.mp4".format(self.video_path, video_name)
            with open(file_path, 'ab')as f:
                f.write(res.content)
                f.close()
        print("result: %s" % count)

    def get_first_list(self, class_name, name):
        f = open("download/download_list/temp.html", "rb")
        # 为了读取一个文件的内容，调用 f.read(size), 这将读取一定数目的数据, 然后作为字符串或字节对象返回。
        # size 是一个可选的数字类型的参数。 当 size 被忽略了或者为负, 那么该文件的所有内容都将被读取并且返回。
        read = f.read()
        html = str(read, "utf-8")
        # 设置HTML解析
        bs = BeautifulSoup(html, "html.parser")
        # 获取对应的内容
        list_main = bs.find_all(name, class_=class_name)
        print(list_main.__len__())
        return list_main

    # 抽取的公共的解析某div下a标签的方法
    def common_parser_child_a(self, name: str, class_name: str, data_set):
        if name.startswith('a'):
            return
        list_main = self.get_first_list(class_name, name)
        for lm in list_main:
            a_bf = BeautifulSoup(str(lm), "html.parser")
            a = a_bf.find_all('a')
            # print(a)
            for each in a:
                # 遍历其中的a标签  self.server +
                href_ = each.get('href')
                # print(each)
                each_sub = BeautifulSoup(str(each), "html.parser")
                h2_ = each_sub.find('h2')
                # print(h2_)
                name = str(h2_.string)
                # 按条件过滤后存入列表
                if not name.startswith('None'):
                    if name.startswith("创客GO·精英汇 | 首届中国“互联网+”大学生创新创业大赛金奖项目——"):
                        real_name = name.replace("创客GO·精英汇 | 首届中国“互联网+”大学生创新创业大赛金奖项目——", "")
                        data_set[real_name] = href_
        # print(data_set)
        # 建立下载路径
        path = "download/download_list/"
        if not os.path.exists(path):
            os.makedirs(path)
        # 因为目标文件的编码是"utf-8"的，所以打开时要设置编码格式
        with open("{0}video_1.txt".format(path), "w", encoding='utf-8') as f:
            # 写入时过滤掉不需要的字符&nbsp;  (8个空格符)
            f.write(data_set.__str__())
            f.close()
        print(data_set.__len__())

    def test(self):
        self.common_parser_child_a(name='div', class_name='article_list',
                                   data_set=self.book_set)

    def get_all_video(self):
        self.test()
        count = 0
        for name in self.book_set:
            if count >= 1:
                break
            next_url = self.book_set[name]
            # print(next_url)
            # 请求html
            html = requests.get(next_url)
            # 解析html
            bs = BeautifulSoup(str(html.content, "utf-8"), "html.parser")
            # 获取对应的内容(span 下的iframe)
            iframe = bs.find("iframe", class_="video_iframe")
            src = iframe.get("data-src")
            print(src)
            # 请求iframe_html
            iframe_html = requests.get(src)

            # 建立下载路径
            path = "download/download_list/"
            if not os.path.exists(path):
                os.makedirs(path)
            # 因为目标文件的编码是"utf-8"的，所以打开时要设置编码格式
            with open("{0}source_3.html".format(path), "w", encoding='utf-8') as f:
                f.write(iframe_html.text)
                f.close()
            ih = BeautifulSoup(str(iframe_html.content, "utf-8"), "html.parser")

            count = count + 1
            print(iframe.__len__())

    def download_tencent(self):
        self.test()
        for name in self.book_set:
            next_url = self.book_set[name]
            self.open_browser(name, next_url)

    def open_browser(self, name: str, url: str):
        browser = webdriver.Chrome()
        # 打开浏览器
        browser.get(url)
        # 睡30s
        time.sleep(5)
        # 获取网站源码
        html = browser.page_source
        # 解析html
        bs = BeautifulSoup(html, "html.parser")
        # 获取对应的内容(span 下的iframe)
        iframe = bs.find("iframe")
        src = "http:" + iframe.get("src")
        print(src)
        # 打开新网页并等10s
        browser.get(src)
        time.sleep(5)
        # 没弹出新窗口，不用重新定义句柄
        # browser.current_window_handle()
        # 点击播放按钮
        play_btn = browser.find_element_by_class_name("txp_svg_play")
        print(play_btn)
        play_btn.click()
        time.sleep(61)
        # 获取video里的内容
        player = browser.page_source
        pb = BeautifulSoup(player, "html.parser")
        wrapper = pb.find("txpdiv", class_="txp_video_container")
        videos = wrapper.findAll("video")
        for video in videos:
            src = video.get("src")
            if not str(src).startswith('None'):
                self.book_set[name] = src
                print(self.book_set[name])
        time.sleep(1)
        browser.quit()
        # 下载
        # 建立下载路径
        download_path = "/download/video/"
        if not os.path.exists(download_path):
            os.makedirs(download_path)
        video_url = self.book_set[name]
        res = requests.get(video_url)
        file_path = "{0}{1}.mp4".format(download_path, name)
        with open(file_path, 'ab')as f:
            f.write(res.content)
            f.close()


if __name__ == '__main__':
    download = Download()
    # download.get_all_video()
    download.download_tencent()
