#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests
import re


def Download_Cloud(urls):
    """从云端下载并保存在本地"""
    for web_url, local_url in urls:
        myfile = requests.get(web_url)
        x = open(local_url, 'wb')
        x.write(myfile.content)
        x.close()


def Extract_Line(file1, file2, words):
    """将 file1 中包含 words 的行提取到 file2 中"""
    try:
        for line in file1:
            g = re.search(words, line)
            if g:
                # print(g.group())
                file2.writelines(line)
    finally:
        file1.close()
        file2.close()


# External 策略组
External = [
    ('https://api.dler.io/sub?target=surge&ver=4&url=https%3A%2F%2Fjj-rss-01.best%2Flink%2FaKgikRhRwi8v2kOv%3Fclash%3D2&insert=true&append_type=true&emoji=true&list=false&udp=true&tfo=false&scv=false&fdn=true&sort=true&surge.doh=true', r'../External.txt')]

Download_Cloud(External)

# 制作 External 策略组
Extract_Line(open(r'../External.txt', 'r'),
             open(r'../egroup.txt', 'w'), 'vmess|trojan')

e = open(r'../egroup.txt', 'r')
a = e.read()
e.close()

a = 'iPad = http, 192.168.1.7, 1082\niPhone = http, 192.168.1.3, 1082\nssr = http, 127.0.0.1, 7890\n' + a
e = open(r'../egroup.txt', 'w')
e.write(a)
e.close()
