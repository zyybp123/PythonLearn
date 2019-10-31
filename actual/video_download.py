import os
import sys

from bs4 import BeautifulSoup
import requests
import urllib.request

''' 简单视频下载'''


class Download:
    # 主机
    server = 'http://play.chinalink.tv'
    #video_path = 'download/video'
    video_path = 'D:\\video\\game_five\\download\\video'
    downloadUrlList = []

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
        #print(url_list)

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


if __name__ == '__main__':
    download = Download()
    download.download_media()
