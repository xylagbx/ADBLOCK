#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests
from posix import remove
import re
# import string

# 函数


def Download_Cloud(urls):
    """从云端下载并保存在本地"""
    for web_url, local_url in urls:
        myfile = requests.get(web_url)
        open(local_url, 'wb').write(myfile.content)


def Merge_Files(tag, urls):
    """循环合并文件"""
    for web_url, local_url in urls:
        x = open(local_url,  "r")
        tag.write(x.read())
        x.close()
    tag.close()


def del_line(file, words):
    """删除具有特定内容的行"""
    with file as f:
        p = re.compile(words)
        lines = [line for line in f.readlines() if p.search(line) is None]
        f.seek(0)
        f.truncate(0)
        f.writelines(lines)


# def Replace_Words(File_r, File_w, org, tag):
#     """
#     将 File 文件中的字符或字符串 org 替换为 tag
#     """
#     alllines = File_r.readlines()
#     File_r.close()
#     for eachline in alllines:
#         a = eachline.replace(org, tag)
#         File_w.writelines(a)
#     File_w.close()


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


def Remove_Repetition(file1, file2):
    """将 file1 去除重复的行，并写入 file2 中，file1 保持原样"""
    with file1 as f, file2 as ff:
        data = [item.strip() for item in f.readlines()
                ]  # 针对最后一行没有换行符，与其他它行重复的情况
        new_data = list(set(data))
        # 针对去除文件中有多行空行的情况
        ff.writelines([item + '\n' for item in new_data if item])
    file1.close()
    file2.close()


# 云端地址 本地地址
# Rule-set
urls = [('https://anti-ad.net/surge.txt', r'原始文件/Rule_set/anti-ad.txt'),
        ('https://raw.githubusercontent.com/ACL4SSR/ACL4SSR/master/Clash/BanAD.list',
         r'原始文件/Rule_set/BanAD.txt'),
        ('https://raw.githubusercontent.com/ACL4SSR/ACL4SSR/master/Clash/BanProgramAD.list',
         r'原始文件/Rule_set/BanProgramAD.txt'),
        ('https://raw.githubusercontent.com/ACL4SSR/ACL4SSR/master/Clash/BanEasyList.list',
         r'原始文件/Rule_set/BanEasyList.txt'),
        ('https://raw.githubusercontent.com/ACL4SSR/ACL4SSR/master/Clash/BanEasyPrivacy.list',
         r'原始文件/Rule_set/BanEasyPrivacy.txt'),
        ('https://raw.githubusercontent.com/lhie1/Rules/master/Surge/Surge%203/Provider/Reject.list', r'原始文件/Rule_set/Reject.txt')]

# || 开头的规则
Adblock = [('https://raw.githubusercontent.com/durablenapkin/scamblocklist/master/adguard.txt',
            r'原始文件/AdGuard/Scam Blocklist by DurableNapkin.txt')]

# domain 开头的规则
Domain = [('https://raw.githubusercontent.com/Spam404/lists/master/main-blacklist.txt', r'原始文件/AdGuard/Spam404.txt'),
          ('https://raw.githubusercontent.com/mitchellkrogza/The-Big-List-of-Hacked-Malware-Web-Sites/master/hacked-domains.list', r'原始文件/AdGuard/The Big List of Hacked Malware Web Sites.txt')]

# 0.0.0.0 开头的规则
Host = [('https://raw.githubusercontent.com/hoshsadiq/adblock-nocoin-list/master/hosts.txt', r'原始文件/AdGuard/NoCoin Filter List.txt'),
        ('https://paulgb.github.io/BarbBlock/blacklists/hosts-file.txt', r'原始文件/AdGuard/BarbBlock.txt')]

# 本地已有文件
myblack = open(r'原始文件/myblack.txt',  "r")
# mywhite = open(r'原始文件/mywhite.txt',  "r")
AdBlockList = open(r'AdBlockList.txt', 'w')
adblock = open(r'adblock.txt', 'w')
domain = open(r'domain.txt', 'w')
host = open(r'host.txt', 'w')

#
myblack = myblack.read()
# mywhite = mywhite.read()


# 从云端下载并保存在本地
# Download_Cloud(urls)
# Download_Cloud(Adblock)
# Download_Cloud(Domain)
# Download_Cloud(Host)


# 合并文件
AdBlockList.write(myblack)
Merge_Files(AdBlockList, urls)
Merge_Files(adblock, Adblock)
Merge_Files(domain, Domain)
Merge_Files(host, Host)


# 创建 BLOCK-URL 规则集
Extract_Line(open(r'AdBlockList.txt', 'r'), open(
    r'BLOCK-URL.txt', 'w'), "URL-REGEX,")
Remove_Repetition(open(r'BLOCK-URL.txt', 'r'), open(r'out2.txt', 'a'))
URLBLOCK = open(r'BLOCK-URL.txt', 'w')
out2 = open(r'out2.txt', 'r')
URLBLOCK.write(out2.read())
URLBLOCK.close()
out2.close()

# 删除 URL-REGEX 规则所在行，因为部分规则含有 '^' ，如果不删除，会出现 'URL-REGEX,\n'
del_line(open(r'AdBlockList.txt', 'r+'), "URL-REGEX,")

# 对 adblock 规则进行修改
# 将 '\n!' 替换为 '\n#' ，将 '^' 替换为 '\n' ，替换开头的 '||' 为 'DOMAIN-SUFFIX,'
File_r = open(r'adblock.txt', 'r')
alllines = File_r.readlines()
File_r.close()
File_w = open(r'adblock.txt', 'w')
for eachline in alllines:
    a = eachline.replace('\n!', '\n#')
    File_w.writelines(a)
File_w.close()

File_r = open(r'adblock.txt', 'r')
alllines = File_r.readlines()
File_r.close()
File_w = open(r'adblock.txt', 'w')
for eachline in alllines:
    a = eachline.replace('^', '\n')
    File_w.writelines(a)
File_w.close()

File_r = open(r'adblock.txt', 'r')
alllines = File_r.readlines()
File_r.close()
File_w = open(r'adblock.txt', 'w')
for eachline in alllines:
    a = eachline.replace('||', 'DOMAIN-SUFFIX,')
    File_w.writelines(a)
File_w.close()


# 对 domain 规则进行修改，在每行开头添加'DOMAIN-SUFFIX,'
domain = open(r'domain.txt', 'r')
alllines = domain.readlines()
domain.close()
domain = open(r'domain.txt', 'w')
for eachline in alllines:
    a = 'DOMAIN-SUFFIX,' + eachline
    domain.writelines(a)
domain.close()

# 对 host 规则进行修改，替换开头的 '0.0.0.0 ' 为 'DOMAIN-SUFFIX,'
File_r = open(r'host.txt', 'r')
alllines = File_r.readlines()
File_r.close()
File_w = open(r'host.txt', 'w')
for eachline in alllines:
    a = eachline.replace('0.0.0.0 ', 'DOMAIN-SUFFIX,')
    File_w.writelines(a)
File_w.close()

# 将所有文件合并
AdBlockList = open(r'AdBlockList.txt', 'r+')
adblock = open(r'adblock.txt', 'r')
domain = open(r'domain.txt', 'r')
host = open(r'host.txt', 'r')
AdBlockList.write(adblock.read())
AdBlockList.write(domain.read())
AdBlockList.write(host.read())
AdBlockList.close()
adblock.close()
domain.close()
host.close()

# # 删除末尾的 '^'
# AdBlockList = open(r'AdBlockList.txt', 'r')
# alllines = AdBlockList.readlines()
# AdBlockList.close()
# AdBlockList = open(r'AdBlockList.txt', 'w')
# for eachline in alllines:
#     # a = re.sub('^\n', '\n', eachline)
#     a = eachline.replace('^', '\n')
#     # a = a.replace('$important', '')
#     # a = a.strip('imo.com')
#     # a = a.replace(',DIRECT\n', '\n')
#     # a = eachline.strip('^')
#     AdBlockList.writelines(a)
# AdBlockList.close()

# 删除本地原有的文件
# remove(r'AdBlock.txt')

# 新建一个 RuleSet.list 文件，如果已经存在，就覆盖掉它
RuleSet = open(r'RuleSet.list', 'w')
RuleSet.close()

# 去重
Remove_Repetition(open(r'AdBlockList.txt', 'r'), open(r'RuleSet.list', 'a'))


# 创建 DOMAIN-SET 规则集
Extract_Line(open(r'RuleSet.list', 'r'), open(
    r'BLOCK-DOMAIN.txt', 'w'), "DOMAIN-SUFFIX,|DOMAIN,")

# 将 out.txt 的内容复制给 BLOCK-DOMAIN-SET.list
BLOCKDomainSet = open(r'BLOCK-DOMAIN-SET.list', 'w')
out = open(r'BLOCK-DOMAIN.txt', 'r')
BLOCKDomainSet.write(out.read())
BLOCKDomainSet.close()
out.close()

File_r = open(r'BLOCK-DOMAIN-SET.list', 'r')
alllines = File_r.readlines()
File_r.close()
File_w = open(r'BLOCK-DOMAIN-SET.list', 'w')
for eachline in alllines:
    a = eachline.replace('DOMAIN-SUFFIX,', '.')
    File_w.writelines(a)
File_w.close()

File_r = open(r'host.txt', 'r')
alllines = File_r.readlines()
File_r.close()
File_w = open(r'host.txt', 'w')
for eachline in alllines:
    a = eachline.replace('DOMAIN,', '.')
    File_w.writelines(a)
File_w.close()

# 将 DOMAIN-SET 规则集中
# Extract_Line(open(r'BLOCK-DOMAIN-SET.list', 'r'), open(r'out.txt', 'w'), "\.")


# IP-CIDR 规则集
Extract_Line(open(r'RuleSet.list', 'r'), open(
    r'BLOCK-IP-CIDR.txt', 'w'), "IP-CIDR,")

File_r = open(r'BLOCK-IP-CIDR.txt', 'r')
alllines = File_r.readlines()
File_r.close()
File_w = open(r'BLOCK-IP-CIDR.txt', 'w')
for eachline in alllines:
    a = eachline.replace('# 广告列表 adblock rules', '')
    File_w.writelines(a)
File_w.close()

# keyword 规则集
Extract_Line(open(r'RuleSet.list', 'r'), open(
    r'BLOCK-KEYWORD.txt', 'w'), "DOMAIN-KEYWORD,")


# RuleSet = open(
#     r'RuleSet.list', 'w')
# out1 = open(
#     r'out1.txt', 'r')
# RuleSet.write(out1.read())
# RuleSet.close()
# out1.close()


remove(r'AdBlockList.txt')
remove(r'adblock.txt')
remove(r'domain.txt')
remove(r'host.txt')
# remove(r'RuleSet.txt')
# remove(r'out.txt')
remove(r'out2.txt')
