# -*- coding: utf-8 -*-

import requests
from posix import remove
import re
# import chardet
import codecs
# import urllib.request
# import sys
import string

# 云端地址 本地地址
# Rule-set
urls = [('https://anti-ad.net/surge.txt',
         '/Users/bx/Library/Mobile Documents/com~apple~CloudDocs/备忘/custom/原始文件/Rule_set/anti-ad.txt'),
        ('https://raw.githubusercontent.com/ACL4SSR/ACL4SSR/master/Clash/BanAD.list',
         '/Users/bx/Library/Mobile Documents/com~apple~CloudDocs/备忘/custom/原始文件/Rule_set/BanAD.txt'),
        ('https://raw.githubusercontent.com/ACL4SSR/ACL4SSR/master/Clash/BanProgramAD.list',
         '/Users/bx/Library/Mobile Documents/com~apple~CloudDocs/备忘/custom/原始文件/Rule_set/BanProgramAD.txt'),
        ('https://raw.githubusercontent.com/ACL4SSR/ACL4SSR/master/Clash/BanEasyList.list',
         '/Users/bx/Library/Mobile Documents/com~apple~CloudDocs/备忘/custom/原始文件/Rule_set/BanEasyList.txt'),
        ('https://raw.githubusercontent.com/ACL4SSR/ACL4SSR/master/Clash/BanEasyPrivacy.list',
         '/Users/bx/Library/Mobile Documents/com~apple~CloudDocs/备忘/custom/原始文件/Rule_set/BanEasyPrivacy.txt'),
        ('https://raw.githubusercontent.com/lhie1/Rules/master/Surge/Surge%203/Provider/Reject.list',
         '/Users/bx/Library/Mobile Documents/com~apple~CloudDocs/备忘/custom/原始文件/Rule_set/Reject.txt')]

# ||
Adblock = [('https://raw.githubusercontent.com/durablenapkin/scamblocklist/master/adguard.txt',
            '/Users/bx/Library/Mobile Documents/com~apple~CloudDocs/备忘/custom/原始文件/AdGuard/Scam Blocklist by DurableNapkin.txt')]

# domain
Domain = [('https://raw.githubusercontent.com/Spam404/lists/master/main-blacklist.txt',
           '/Users/bx/Library/Mobile Documents/com~apple~CloudDocs/备忘/custom/原始文件/AdGuard/Spam404.txt'),
          ('https://raw.githubusercontent.com/mitchellkrogza/The-Big-List-of-Hacked-Malware-Web-Sites/master/hacked-domains.list',
           '/Users/bx/Library/Mobile Documents/com~apple~CloudDocs/备忘/custom/原始文件/AdGuard/The Big List of Hacked Malware Web Sites.txt')]

# 0.0.0.0
Host = [('https://raw.githubusercontent.com/hoshsadiq/adblock-nocoin-list/master/hosts.txt',
         '/Users/bx/Library/Mobile Documents/com~apple~CloudDocs/备忘/custom/原始文件/AdGuard/NoCoin Filter List.txt'),
        ('https://paulgb.github.io/BarbBlock/blacklists/hosts-file.txt',
         '/Users/bx/Library/Mobile Documents/com~apple~CloudDocs/备忘/custom/原始文件/AdGuard/BarbBlock.txt')]

# 本地已有文件
my_black = open(
    '/Users/bx/Library/Mobile Documents/com~apple~CloudDocs/备忘/custom/原始文件/my_black.txt',  "r")
# my_white = open('/Users/bx/Library/Mobile Documents/com~apple~CloudDocs/备忘/custom/原始文件/my_white.txt',  "r")
AdBlockList = open(
    '/Users/bx/Library/Mobile Documents/com~apple~CloudDocs/备忘/custom/AdBlockList.txt', 'w')
adblock = open(
    '/Users/bx/Library/Mobile Documents/com~apple~CloudDocs/备忘/custom/adblock.txt', 'w')
domain = open(
    '/Users/bx/Library/Mobile Documents/com~apple~CloudDocs/备忘/custom/domain.txt', 'w')
host = open(
    '/Users/bx/Library/Mobile Documents/com~apple~CloudDocs/备忘/custom/host.txt', 'w')

#
my_black = my_black.read()
# my_white = my_white.read()


# 从云端下载并保存在本地
for web_url, local_url in urls:
    myfile = requests.get(web_url)
    open(local_url, 'wb').write(myfile.content)
for web_url, local_url in Adblock:
    myfile = requests.get(web_url)
    open(local_url, 'wb').write(myfile.content)
for web_url, local_url in Domain:
    myfile = requests.get(web_url)
    open(local_url, 'wb').write(myfile.content)
for web_url, local_url in Host:
    myfile = requests.get(web_url)
    open(local_url, 'wb').write(myfile.content)


# 合并文件
AdBlockList.write(my_black)
for web_url, local_url in urls:
    x = open(local_url,  "r")
    AdBlockList.write(x.read())
    x.close()
for web_url, local_url in Adblock:
    x = open(local_url,  "r")
    adblock.write(x.read())
    x.close()
for web_url, local_url in Domain:
    x = open(local_url,  "r")
    domain.write(x.read())
    x.close()
for web_url, local_url in Host:
    x = open(local_url,  "r")
    host.write(x.read())
    x.close()
AdBlockList.close()
adblock.close()
domain.close()
host.close()


# 对 adblock 规则进行修改
# 将 ! 替换为 #
adblock = open(
    '/Users/bx/Library/Mobile Documents/com~apple~CloudDocs/备忘/custom/adblock.txt', 'r')
alllines = adblock.readlines()
adblock.close()
adblock = open(
    '/Users/bx/Library/Mobile Documents/com~apple~CloudDocs/备忘/custom/adblock.txt', 'w')
for eachline in alllines:
    # a = re.sub('!', '#', eachline)
    a = eachline.replace('!', '#')
    adblock.writelines(a)
adblock.close()

# 删除末尾的 '^'
adblock = open(
    '/Users/bx/Library/Mobile Documents/com~apple~CloudDocs/备忘/custom/adblock.txt', 'r')
alllines = adblock.readlines()
adblock.close()
adblock = open(
    '/Users/bx/Library/Mobile Documents/com~apple~CloudDocs/备忘/custom/adblock.txt', 'w')
for eachline in alllines:
    a = eachline.replace('^', '')
    # a = re.sub('^\n', '\n', eachline)
    # a = eachline.strip('^')
    adblock.writelines(a)
adblock.close()

# 替换开头的 '||' 为 'DOMAIN-SUFFIX,'
adblock = open(
    '/Users/bx/Library/Mobile Documents/com~apple~CloudDocs/备忘/custom/adblock.txt', 'r')
alllines = adblock.readlines()
adblock.close()
adblock = open(
    '/Users/bx/Library/Mobile Documents/com~apple~CloudDocs/备忘/custom/adblock.txt', 'w')
for eachline in alllines:
    # a = re.sub('||', 'DOMAIN-SUFFIX,', eachline)
    a = eachline.replace('||', 'DOMAIN-SUFFIX,')
    adblock.writelines(a)
adblock.close()

# 对 domain 规则进行修改
# 将 ! 替换为 #
domain = open(
    '/Users/bx/Library/Mobile Documents/com~apple~CloudDocs/备忘/custom/domain.txt', 'r')
alllines = domain.readlines()
domain.close()
domain = open(
    '/Users/bx/Library/Mobile Documents/com~apple~CloudDocs/备忘/custom/domain.txt', 'w')
for eachline in alllines:
    a = 'DOMAIN-SUFFIX,' + eachline
    domain.writelines(a)
domain.close()

# 对 host 规则进行修改
# 替换开头的 '0.0.0.0 ' 为 'DOMAIN-SUFFIX,'
host = open(
    '/Users/bx/Library/Mobile Documents/com~apple~CloudDocs/备忘/custom/host.txt', 'r')
alllines = host.readlines()
host.close()
host = open(
    '/Users/bx/Library/Mobile Documents/com~apple~CloudDocs/备忘/custom/host.txt', 'w')
for eachline in alllines:
    # a = re.sub('0.0.0.0 ', 'DOMAIN-SUFFIX,', eachline)
    a = eachline.replace('0.0.0.0 ', 'DOMAIN-SUFFIX,')
    host.writelines(a)
host.close()


# 合并文件
AdBlockList = open(
    '/Users/bx/Library/Mobile Documents/com~apple~CloudDocs/备忘/custom/AdBlockList.txt', 'r+')
adblock = open(
    '/Users/bx/Library/Mobile Documents/com~apple~CloudDocs/备忘/custom/adblock.txt', 'r')
domain = open(
    '/Users/bx/Library/Mobile Documents/com~apple~CloudDocs/备忘/custom/domain.txt', 'r')
host = open(
    '/Users/bx/Library/Mobile Documents/com~apple~CloudDocs/备忘/custom/host.txt', 'r')
AdBlockList.write(adblock.read())
AdBlockList.write(domain.read())
AdBlockList.write(host.read())
AdBlockList.close()
adblock.close()
domain.close()
host.close()


# 删除末尾的 '^'
AdBlockList = open(
    '/Users/bx/Library/Mobile Documents/com~apple~CloudDocs/备忘/custom/AdBlockList.txt', 'r')
alllines = AdBlockList.readlines()
AdBlockList.close()
AdBlockList = open(
    '/Users/bx/Library/Mobile Documents/com~apple~CloudDocs/备忘/custom/AdBlockList.txt', 'w')
for eachline in alllines:
    # a = re.sub('^\n', '\n', eachline)
    a = eachline.replace('^', '')
    a = a.replace('$important', '')
    # a = eachline.strip('^')
    AdBlockList.writelines(a)
AdBlockList.close()

# 删除本地原有的文件
# remove('/Users/bx/Library/Mobile Documents/com~apple~CloudDocs/备忘/custom/AdBlock.txt')

# 新建一个 Rule_set.txt 文件，如果已经存在，就覆盖掉它
RuleSet = open(
    '/Users/bx/Library/Mobile Documents/com~apple~CloudDocs/备忘/custom/RuleSet.list', 'wb')
RuleSet.close()

# 去重
AdBlockList = open(
    '/Users/bx/Library/Mobile Documents/com~apple~CloudDocs/备忘/custom/AdBlockList.txt', 'r')
RuleSet = open(
    '/Users/bx/Library/Mobile Documents/com~apple~CloudDocs/备忘/custom/RuleSet.list', 'a')
with AdBlockList as f, RuleSet as ff:
    data = [item.strip() for item in f.readlines()
            ]  # 针对最后一行没有换行符，与其他它行重复的情况
    new_data = list(set(data))
    # 针对去除文件中有多行空行的情况
    ff.writelines([item + '\n' for item in new_data if item])
AdBlockList.close()
RuleSet.close()


with open('/Users/bx/Library/Mobile Documents/com~apple~CloudDocs/备忘/custom/RuleSet.list', "r+") as f:
    p = re.compile("#|URL-REGEX,|/")
    lines = [line for line in f.readlines() if p.search(line) is None]
    f.seek(0)
    f.truncate(0)
    f.writelines(lines)


ruleset = open(
    '/Users/bx/Library/Mobile Documents/com~apple~CloudDocs/备忘/custom/RuleSet.list', 'r')
alllines = ruleset.readlines()
ruleset.close()
ruleset = open(
    '/Users/bx/Library/Mobile Documents/com~apple~CloudDocs/备忘/custom/RuleSet.txt', 'w')
for eachline in alllines:
    # a = eachline.decode('utf-8')
    # printable = set(string.eachline)
    # a = filter(lambda x: x in eachline, s)
    for char in eachline:
        char = ord(char)
        # a = a.decode('utf-8')
    ruleset.writelines(eachline)
ruleset.close()


# content = codecs.open(
#     '/Users/bx/Library/Mobile Documents/com~apple~CloudDocs/备忘/custom/RuleSet.list', 'r', 'utf-8').write(content)

# codecs.open("/Users/bx/Library/Mobile Documents/com~apple~CloudDocs/备忘/custom/RuleSet.txt",
#             'w', encoding='ascii').write(content)

filename = '/Users/bx/Library/Mobile Documents/com~apple~CloudDocs/备忘/custom/RuleSet.txt'
content = codecs.open(filename, 'r').read()
# rule = content.write(content)
# sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())
codecs.open(filename, 'w', encoding='utf-8').write(content)


remove('/Users/bx/Library/Mobile Documents/com~apple~CloudDocs/备忘/custom/AdBlockList.txt')
remove('/Users/bx/Library/Mobile Documents/com~apple~CloudDocs/备忘/custom/adblock.txt')
remove('/Users/bx/Library/Mobile Documents/com~apple~CloudDocs/备忘/custom/domain.txt')
remove('/Users/bx/Library/Mobile Documents/com~apple~CloudDocs/备忘/custom/host.txt')
