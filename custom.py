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
        x = open(local_url, 'wb')
        x.write(myfile.content)
        x.close()


def Merge_Files(tag, urls):
    """循环合并文件"""
    for web_url, local_url in urls:
        x = open(local_url,  "r")
        tag.write(x.read())
        x.close()
    tag.close()


def Merge_File(tag, org):
    """将文件 org 合并到文件 tag 中"""
    tag.write(org.read())
    org.close()
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


def sorted_file_content(a):
    """将文件内容按行排序"""
    b = open(a, 'r')
    out = open(r'out.list', 'w')
    out.write(b.read())
    b.close()
    out.close()
    b = open(a, 'w')
    out = open(r'out.list', 'r')
    out = sorted(out)
    for item in out:
        b.writelines(item)
    b.close()
    remove(r'out.list')


def sorted_file_content_reverse(a):
    """将文件内容按行排序-倒序"""
    b = open(a, 'r')
    out = open(r'out.list', 'w')
    out.write(b.read())
    b.close()
    out.close()
    b = open(a, 'w')
    out = open(r'out.list', 'r')
    out = sorted(out, reverse=True)
    for item in out:
        b.writelines(item)
    b.close()
    remove(r'out.list')


def add_after_line(a, b):
    """在每行末尾添加特定的字符串"""
    RuleSet = open(a, 'r')
    alllines = RuleSet.readlines()
    RuleSet.close()
    RuleSet = open(a, 'w')
    for eachline in alllines:
        a = eachline.strip() + b
        RuleSet.writelines(a)
    RuleSet.close()


# reject
# 云端地址 本地地址

# Domain-set
domainset = [
    ('https://raw.githubusercontent.com/geekdada/surge-list/master/domain-set/adaway.txt',
     r'原始文件/Domain_set/adaway.txt'),
    ('https://raw.githubusercontent.com/geekdada/surge-list/master/domain-set/annoyances-filter.txt',
     r'原始文件/Domain_set/annoyances-filter.txt'),
    ('https://raw.githubusercontent.com/geekdada/surge-list/master/domain-set/base-filter.txt',
     r'原始文件/Domain_set/base-filter.txt'),
    ('https://raw.githubusercontent.com/geekdada/surge-list/master/domain-set/chinese-filter.txt',
     r'原始文件/Domain_set/chinese-filter.txt'),
    ('https://raw.githubusercontent.com/geekdada/surge-list/master/domain-set/dns-filter.txt',
     r'原始文件/Domain_set/dns-filter.txt'),
    ('https://raw.githubusercontent.com/geekdada/surge-list/master/domain-set/neohosts-full.txt',
     r'原始文件/Domain_set/neohosts-full.txt'),
    ('https://raw.githubusercontent.com/geekdada/surge-list/master/domain-set/neohosts.txt',
     r'原始文件/Domain_set/neohosts.txt'),
    ('https://raw.githubusercontent.com/geekdada/surge-list/master/domain-set/social-media-filter.txt',
     r'原始文件/Domain_set/social-media-filter.txt'),
    ('https://raw.githubusercontent.com/geekdada/surge-list/master/domain-set/tracking-protection-filter.txt',
     r'原始文件/Domain_set/tracking-protection-filter.txt')]

# Rule-set
urls = [('https://raw.githubusercontent.com/privacy-protection-tools/anti-AD/master/anti-ad-surge.txt',
         r'原始文件/Rule_set/anti-ad.txt'),
        ('https://raw.githubusercontent.com/ACL4SSR/ACL4SSR/master/Clash/BanAD.list',
         r'原始文件/Rule_set/BanAD.txt'),
        ('https://raw.githubusercontent.com/ACL4SSR/ACL4SSR/master/Clash/BanProgramAD.list',
         r'原始文件/Rule_set/BanProgramAD.txt'),
        ('https://raw.githubusercontent.com/ACL4SSR/ACL4SSR/master/Clash/BanEasyList.list',
         r'原始文件/Rule_set/BanEasyList.txt'),
        ('https://raw.githubusercontent.com/ACL4SSR/ACL4SSR/master/Clash/BanEasyPrivacy.list',
         r'原始文件/Rule_set/BanEasyPrivacy.txt'),
        ('https://raw.githubusercontent.com/lhie1/Rules/master/Surge/Surge%203/Provider/Reject.list',
         r'原始文件/Rule_set/Reject.txt'),
        ('https://raw.githubusercontent.com/ACL4SSR/ACL4SSR/master/Clash/BanEasyListChina.list',
         r'原始文件/Rule_set/BanEasyListChina.txt'),
        ('https://raw.githubusercontent.com/Loyalsoldier/surge-rules/release/ruleset/reject.txt',
         r'原始文件/Rule_set/adreject.txt')]

# || 开头的规则
Adblock = [('https://raw.githubusercontent.com/durablenapkin/scamblocklist/master/adguard.txt',
            r'原始文件/AdGuard/Scam Blocklist by DurableNapkin.txt'),
           ('https://adguardteam.github.io/AdGuardSDNSFilter/Filters/filter.txt',
            r'原始文件/AdGuard/filter.txt'),
           ('https://pgl.yoyo.org/adservers/serverlist.php?hostformat=adblockplus&showintro=1&mimetype=plaintext',
            r'原始文件/AdGuard/Peter.txt'),
           ('https://raw.githubusercontent.com/DandelionSprout/adfilt/master/GameConsoleAdblockList.txt',
            r'原始文件/AdGuard/GameConsoleAdblockList.txt')]

# domain 开头的规则
Domain = [('https://raw.githubusercontent.com/Spam404/lists/master/main-blacklist.txt',
           r'原始文件/AdGuard/Spam404.txt'),
          ('https://raw.githubusercontent.com/mitchellkrogza/The-Big-List-of-Hacked-Malware-Web-Sites/master/hacked-domains.list',
           r'原始文件/AdGuard/The Big List of Hacked Malware Web Sites.txt')]

# 0.0.0.0 开头的规则
Host = [('https://raw.githubusercontent.com/hoshsadiq/adblock-nocoin-list/master/hosts.txt',
         r'原始文件/AdGuard/NoCoin Filter List.txt'),
        ('https://paulgb.github.io/BarbBlock/blacklists/hosts-file.txt',
         r'原始文件/AdGuard/BarbBlock.txt'),
        ('https://someonewhocares.org/hosts/zero/hosts',
         r'原始文件/AdGuard/someonewhocares.txt')]


# direct
Direct = [('https://raw.githubusercontent.com/Loyalsoldier/surge-rules/release/ruleset/direct.txt',
           r'原始文件/Direct/direct.txt'),
          ('https://raw.githubusercontent.com/Loyalsoldier/surge-rules/release/ruleset/cncidr.txt',
           r'原始文件/Direct/cncidr.txt'),
          ('https://raw.githubusercontent.com/ACL4SSR/ACL4SSR/master/Clash/LocalAreaNetwork.list',
           r'原始文件/Direct/LocalAreaNetwork.txt'),
          ('https://raw.githubusercontent.com/ACL4SSR/ACL4SSR/master/Clash/GoogleCN.list',
           r'原始文件/Direct/GoogleCN.txt'),
          ('https://raw.githubusercontent.com/ACL4SSR/ACL4SSR/master/Clash/ChinaDomain.list',
           r'原始文件/Direct/ChinaDomain.txt'),
          ('https://raw.githubusercontent.com/ACL4SSR/ACL4SSR/master/Clash/ChinaCompanyIp.list',
           r'原始文件/Direct/ChinaCompanyIp.txt'),
          ('https://raw.githubusercontent.com/lhie1/Rules/master/Surge/Surge%203/Provider/Special.list',
           r'原始文件/Direct/Special.txt'),
          ('https://raw.githubusercontent.com/lhie1/Rules/master/Surge/Surge%203/Provider/Media/Bilibili.list',
           r'原始文件/Direct/Bilibili.txt'),
          ('https://raw.githubusercontent.com/lhie1/Rules/master/Surge/Surge%203/Provider/Media/iQiyi.list',
           r'原始文件/Direct/iQiyi.txt'),
          ('https://raw.githubusercontent.com/lhie1/Rules/master/Surge/Surge%203/Provider/Media/Letv.list',
           r'原始文件/Direct/Letv.txt'),
          ('https://raw.githubusercontent.com/lhie1/Rules/master/Surge/Surge%203/Provider/Media/Netease%20Music.list',
           r'原始文件/Direct/Netease_Music.txt'),
          ('https://raw.githubusercontent.com/lhie1/Rules/master/Surge/Surge%203/Provider/Media/Tencent%20Video.list',
           r'原始文件/Direct/Tencent_Video.txt'),
          ('https://raw.githubusercontent.com/lhie1/Rules/master/Surge/Surge%203/Provider/Media/Youku.list',
           r'原始文件/Direct/Youku.txt'),
          ('https://raw.githubusercontent.com/lhie1/Rules/master/Surge/Surge%203/Provider/Domestic.list',
           r'原始文件/Direct/Domestic.txt'),
          ('https://raw.githubusercontent.com/lhie1/Rules/master/Surge/Surge%203/Provider/Domestic%20IPs.list',
           r'原始文件/Direct/Domestic_IPs.txt'),
          ('https://raw.githubusercontent.com/ACL4SSR/ACL4SSR/master/Clash/ChinaIp.list',
           r'原始文件/Direct/ChinaIp.txt'),
          ('https://raw.githubusercontent.com/ACL4SSR/ACL4SSR/master/Clash/ChinaMedia.list', r'原始文件/Direct/ChinaMedia.txt')]


# proxy
Proxy = [
    ('https://raw.githubusercontent.com/Loyalsoldier/surge-rules/release/ruleset/proxy.txt',
     r'原始文件/Proxy/proxyA.txt'),
    ('https://raw.githubusercontent.com/Loyalsoldier/surge-rules/release/ruleset/google.txt',
     r'原始文件/Proxy/google.txt'),
    ('https://raw.githubusercontent.com/Loyalsoldier/surge-rules/release/ruleset/gfw.txt',
     r'原始文件/Proxy/gfw.txt'),
    ('https://raw.githubusercontent.com/Loyalsoldier/surge-rules/release/ruleset/greatfire.txt',
     r'原始文件/Proxy/greatfire.txt'),
    ('https://raw.githubusercontent.com/Loyalsoldier/surge-rules/release/ruleset/telegramcidr.txt',
     r'原始文件/Proxy/telegramcidr.txt'),
    ('https://raw.githubusercontent.com/ACL4SSR/ACL4SSR/master/Clash/Microsoft.list',
     r'原始文件/Proxy/MicrosoftA.txt'),
    ('https://raw.githubusercontent.com/ACL4SSR/ACL4SSR/master/Clash/Telegram.list',
     r'原始文件/Proxy/TelegramA.txt'),
    ('https://raw.githubusercontent.com/ACL4SSR/ACL4SSR/master/Clash/ProxyMedia.list',
     r'原始文件/Proxy/ProxyMedia.txt'),
    ('https://raw.githubusercontent.com/ACL4SSR/ACL4SSR/master/Clash/ProxyLite.list',
     r'原始文件/Proxy/ProxyLite.txt'),
    ('https://raw.githubusercontent.com/lhie1/Rules/master/Surge/Surge%203/Provider/Telegram.list',
     r'原始文件/Proxy/Telegraml.txt'),
    ('https://raw.githubusercontent.com/lhie1/Rules/master/Surge/Surge%203/Provider/Microsoft.list',
     r'原始文件/Proxy/Microsoftl.txt'),
    ('https://raw.githubusercontent.com/lhie1/Rules/master/Surge/Surge%203/Provider/Proxy.list',
     r'原始文件/Proxy/Proxyl.txt'),
    ('https://raw.githubusercontent.com/lhie1/Rules/master/Surge/Surge%203/Provider/Steam.list',
     r'原始文件/Proxy/Steam.txt'),
    ('https://raw.githubusercontent.com/lhie1/Rules/master/Surge/Surge%203/Provider/Speedtest.list',
     r'原始文件/Proxy/Speedtest.txt'),
    ('https://raw.githubusercontent.com/lhie1/Rules/master/Surge/Surge%203/Provider/PayPal.list',
     r'原始文件/Proxy/PayPal.txt'),
    ('https://raw.githubusercontent.com/ACL4SSR/ACL4SSR/master/Clash/OneDrive.list',
     r'原始文件/Proxy/OneDrive.txt'),
    ('https://raw.githubusercontent.com/ACL4SSR/ACL4SSR/master/Clash/Netflix.list',
     r'原始文件/Proxy/Netflix.txt'),
    ('https://raw.githubusercontent.com/ACL4SSR/ACL4SSR/master/Clash/ProxyGFWlist.list', r'原始文件/Proxy/ProxyGFWlist.txt')]


# 本地已有文件
myblack = open(r'原始文件/myblack.txt',  "r")
myclash = open(r'原始文件/clash.txt',  "r")
myDirect = open(r'原始文件/Direct.txt',  "r")
myProxy = open(r'原始文件/Proxy.txt',  "r")
# mywhite = open(r'原始文件/mywhite.txt',  "r")
AdBlockList = open(r'AdBlockList.txt', 'w')
DirectList = open(r'DirectList.txt', 'w')
ProxyList = open(r'ProxyList.txt', 'w')
adblock = open(r'adblock.txt', 'w')
domain = open(r'domain.txt', 'w')
host = open(r'host.txt', 'w')


# 从云端下载并保存在本地
Download_Cloud(urls)
Download_Cloud(Adblock)
Download_Cloud(Domain)
Download_Cloud(domainset)
Download_Cloud(Host)
Download_Cloud(Direct)
Download_Cloud(Proxy)


# 合并文件
AdBlockList.write(myblack.read())
AdBlockList.close()
myblack.close()
Merge_Files(open(r'AdBlockList.txt', 'a'), urls)
Merge_Files(open(r'adblock.txt', 'a'), Adblock)
Merge_Files(open(r'domain.txt', 'a'), Domain)
Merge_Files(open(r'domainset.txt', 'a'), domainset)
Merge_Files(open(r'host.txt', 'a'), Host)
DirectList.write(myDirect.read())
DirectList.close()
myDirect.close()
Merge_Files(open(r'DirectList.txt', 'a'), Direct)
ProxyList.write(myProxy.read())
ProxyList.close()
myProxy.close()
Merge_Files(open(r'ProxyList.txt', 'a'), Proxy)

# 将 'IP-CIDR,180.76.76.76/32DOMAIN-SUFFIX,0-100.com' 替换为 'IP-CIDR,180.76.76.76/32\nDOMAIN-SUFFIX,0-100.com'
# 将 'IP-CIDR,2001:67c:4e8::/48DOMAIN-SUFFIX,000000000000000000000000000000000000000000000000000000000000001.com' 替换为 'IP-CIDR,2001:67c:4e8::/48\nDOMAIN-SUFFIX,000000000000000000000000000000000000000000000000000000000000001.com'
File_r = open(r'ProxyList.txt', 'r')
alllines = File_r.readlines()
File_r.close()
File_w = open(r'ProxyList.txt', 'w')
for eachline in alllines:
    a = eachline.replace('IP-CIDR,180.76.76.76/32DOMAIN-SUFFIX,0-100.com',
                         'IP-CIDR,180.76.76.76/32\nDOMAIN-SUFFIX,0-100.com')
    a = a.replace('IP-CIDR,2001:67c:4e8::/48DOMAIN-SUFFIX,000000000000000000000000000000000000000000000000000000000000001.com',
                  'IP-CIDR,2001:67c:4e8::/48\nDOMAIN-SUFFIX,000000000000000000000000000000000000000000000000000000000000001.com')
    File_w.writelines(a)
File_w.close()


# domainset = open(r'domainset.txt', 'r+')
# domainset.write('\n')
# domainset.write(' ')
# domainset.close()
# sorted_file_content(r'domainset.txt')


del_line(open(r'domainset.txt', 'r+'), ' nalytics.163.com')


# 将 domainset 中开头的 '.' 替换为 'DOMAIN-SUFFIX,'
File_r = open(r'domainset.txt', 'r')
alllines = File_r.readlines()
File_r.close()
File_w = open(r'domainset.txt', 'w')
for eachline in alllines:
    a = eachline.replace('.', 'DOMAIN-SUFFIX,', 1)
    File_w.writelines(a)
File_w.close()


# 将所有到 '#' 替换为 '\n#\n'
# 将所有到 ',no-resolve' 替换为 '\n,no-resolve\n'
File_r = open(r'adblock.txt', 'r')
alllines = File_r.readlines()
File_r.close()
File_w = open(r'adblock.txt', 'w')
for eachline in alllines:
    a = eachline.replace('#', '\n#\n')
    a = a.replace(',no-resolve', '\n,no-resolve\n')
    File_w.writelines(a)
File_w.close()
File_r = open(r'domain.txt', 'r')
alllines = File_r.readlines()
File_r.close()
File_w = open(r'domain.txt', 'w')
for eachline in alllines:
    a = eachline.replace('#', '\n#\n')
    a = a.replace(',no-resolve', '\n,no-resolve\n')
    File_w.writelines(a)
File_w.close()
File_r = open(r'host.txt', 'r')
alllines = File_r.readlines()
File_r.close()
File_w = open(r'host.txt', 'w')
for eachline in alllines:
    a = eachline.replace('#', '\n#\n')
    a = a.replace(',no-resolve', '\n,no-resolve\n')
    File_w.writelines(a)
File_w.close()
File_r = open(r'原始文件/myblack.txt', 'r')
alllines = File_r.readlines()
File_r.close()
File_w = open(r'原始文件/myblack.txt', 'w')
for eachline in alllines:
    a = eachline.replace('#', '\n#\n')
    a = a.replace(',no-resolve', '\n,no-resolve\n')
    File_w.writelines(a)
File_w.close()
File_r = open(r'原始文件/clash.txt', 'r')
alllines = File_r.readlines()
File_r.close()
File_w = open(r'原始文件/clash.txt', 'w')
for eachline in alllines:
    a = eachline.replace('#', '\n#\n')
    a = a.replace(',no-resolve', '\n,no-resolve\n')
    File_w.writelines(a)
File_w.close()
File_r = open(r'原始文件/Direct.txt', 'r')
alllines = File_r.readlines()
File_r.close()
File_w = open(r'原始文件/Direct.txt', 'w')
for eachline in alllines:
    a = eachline.replace('#', '\n#\n')
    a = a.replace(',no-resolve', '\n,no-resolve\n')
    File_w.writelines(a)
File_w.close()
File_r = open(r'原始文件/Proxy.txt', 'r')
alllines = File_r.readlines()
File_r.close()
File_w = open(r'原始文件/Proxy.txt', 'w')
for eachline in alllines:
    a = eachline.replace('#', '\n#\n')
    a = a.replace(',no-resolve', '\n,no-resolve\n')
    File_w.writelines(a)
File_w.close()
File_r = open(r'AdBlockList.txt', 'r')
alllines = File_r.readlines()
File_r.close()
File_w = open(r'AdBlockList.txt', 'w')
for eachline in alllines:
    a = eachline.replace('#', '\n#\n')
    a = a.replace(',no-resolve', '\n,no-resolve\n')
    File_w.writelines(a)
File_w.close()
File_r = open(r'DirectList.txt', 'r')
alllines = File_r.readlines()
File_r.close()
File_w = open(r'DirectList.txt', 'w')
for eachline in alllines:
    a = eachline.replace('#', '\n#\n')
    a = a.replace(',no-resolve', '\n,no-resolve\n')
    File_w.writelines(a)
File_w.close()
File_r = open(r'ProxyList.txt', 'r')
alllines = File_r.readlines()
File_r.close()
File_w = open(r'ProxyList.txt', 'w')
for eachline in alllines:
    a = eachline.replace('#', '\n#\n')
    a = a.replace(',no-resolve', '\n,no-resolve\n')
    File_w.writelines(a)
File_w.close()


# 创建 BLOCK-URL 规则集
Extract_Line(open(r'AdBlockList.txt', 'r'), open(
    r'BLOCK/URL.txt', 'w'), "URL-REGEX,")
Remove_Repetition(open(r'BLOCK/URL.txt', 'r'), open(r'out2.txt', 'a'))
URLBLOCK = open(r'BLOCK/URL.txt', 'w')
out2 = open(r'out2.txt', 'r')
URLBLOCK.write(out2.read())
URLBLOCK.close()
out2.close()

Extract_Line(open(r'DirectList.txt', 'r'), open(
    r'DIRECT/URL.txt', 'w'), "URL-REGEX,")
Remove_Repetition(open(r'DIRECT/URL.txt', 'r'), open(r'out1.txt', 'a'))
URLDIRECT = open(r'DIRECT/URL.txt', 'w')
out1 = open(r'out1.txt', 'r')
URLDIRECT.write(out1.read())
URLDIRECT.close()
out1.close()

Extract_Line(open(r'ProxyList.txt', 'r'), open(
    r'PROXY/URL.txt', 'w'), "URL-REGEX,")
Remove_Repetition(open(r'PROXY/URL.txt', 'r'), open(r'out3.txt', 'a'))
URLPROXY = open(r'PROXY/URL.txt', 'w')
out3 = open(r'out3.txt', 'r')
URLPROXY.write(out3.read())
URLPROXY.close()
out3.close()

# 删除 URL-REGEX 规则所在行，因为部分规则含有 '^' ，如果不删除，会出现 'URL-REGEX,\n'
del_line(open(r'AdBlockList.txt', 'r+'), "URL-REGEX,")
del_line(open(r'DirectList.txt', 'r+'), "URL-REGEX,")
del_line(open(r'ProxyList.txt', 'r+'), "URL-REGEX,")

# 对 adblock 规则进行修改
# 将 '!' 替换为 '\n#' ，将 '^' 替换为 '\n' ，替换开头的 '||' 为 'DOMAIN-SUFFIX,'
File_r = open(r'adblock.txt', 'r')
alllines = File_r.readlines()
File_r.close()
File_w = open(r'adblock.txt', 'w')
for eachline in alllines:
    a = eachline.replace('!', '\n#')
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
    a = eachline.replace('$', '\n')
    File_w.writelines(a)
File_w.close()

File_r = open(r'adblock.txt', 'r')
alllines = File_r.readlines()
File_r.close()
File_w = open(r'adblock.txt', 'w')
for eachline in alllines:
    a = eachline.replace('||', '\nDOMAIN-SUFFIX,')
    File_w.writelines(a)
File_w.close()


# 对 domain 规则进行修改，在每行开头添加'DOMAIN,'
domain = open(r'domain.txt', 'r')
alllines = domain.readlines()
domain.close()
domain = open(r'domain.txt', 'w')
for eachline in alllines:
    a = 'DOMAIN,' + eachline
    domain.writelines(a)
domain.close()

# 对 host 规则进行修改，替换开头的 '0.0.0.0 ' 为 'DOMAIN,'
File_r = open(r'host.txt', 'r')
alllines = File_r.readlines()
File_r.close()
File_w = open(r'host.txt', 'w')
for eachline in alllines:
    a = eachline.replace('0.0.0.0 ', 'DOMAIN,')
    File_w.writelines(a)
File_w.close()

# 将所有文件合并
Merge_File(open(r'AdBlockList.txt', 'a'), open(r'adblock.txt', 'r'))
Merge_File(open(r'AdBlockList.txt', 'a'), open(r'domain.txt', 'r'))
Merge_File(open(r'AdBlockList.txt', 'a'), open(r'host.txt', 'r'))
Merge_File(open(r'AdBlockList.txt', 'a'), open(r'domainset.txt', 'r'))


# 新建一个 RuleSet.list 文件，如果已经存在，就覆盖掉它
RuleSet = open(r'RuleSet.list', 'w')
RuleSet.close()
DRuleSet = open(r'DRuleSet.list', 'w')
DRuleSet.close()
PRuleSet = open(r'PRuleSet.list', 'w')
PRuleSet.close()

# 去重
Remove_Repetition(open(r'AdBlockList.txt', 'r'), open(r'RuleSet.list', 'a'))
Remove_Repetition(open(r'DirectList.txt', 'r'), open(r'DRuleSet.list', 'a'))
Remove_Repetition(open(r'ProxyList.txt', 'r'), open(r'PRuleSet.list', 'a'))


"""从proxy中排除apple"""
Apple = open(r'原始文件/Apple.txt', 'r')
alllines = Apple.readlines()
Apple.close()
for eachline in alllines:
    del_line(open(r'PRuleSet.list', 'r+'), eachline)

# PRuleSet = open(r'PRuleSet.list', 'r')
# alllines = PRuleSet.readlines()
# PRuleSet.close()
# alllines = alllines + 'DOMAIN-SUFFIX, smartmailcloud.com\n'
PRuleSet = open(r'PRuleSet.list', 'r+')
PRuleSet.write('DOMAIN-SUFFIX, smartmailcloud.com\n')
PRuleSet.close()


"""从direct中排除apple"""
Apple = open(r'原始文件/Apple.txt', 'r')
alllines = Apple.readlines()
Apple.close()
for eachline in alllines:
    del_line(open(r'DRuleSet.list', 'r+'), eachline)

del_line(open(r'DRuleSet.list', 'r+'), "DOMAIN-SUFFIX,cn\n")
del_line(open(r'DRuleSet.list', 'r+'), "smartmailcloud.com")


"""从block中排除mywhite"""
mywhite = open(r'原始文件/mywhite.txt',  "r")
alllines = mywhite.readlines()
mywhite.close()
for eachline in alllines:
    del_line(open(r'RuleSet.list', 'r+'), eachline)


# del_line(open(r'custom.conf', 'r+'), '[Adblock Plus 3.4]')

# """从direct中排除reject"""
# RuleSet = open(r'RuleSet.list', 'r')
# alllines = RuleSet.readlines()
# RuleSet.close()
# for eachline in alllines:
#     del_line(open(r'DRuleSet.list', 'r+'), eachline)

# """从proxy中排除reject，direct"""
# RuleSet = open(r'RuleSet.list', 'r')
# alllines = RuleSet.readlines()
# RuleSet.close()
# for eachline in alllines:
#     del_line(open(r'PRuleSet.list', 'r+'), eachline)
# DRuleSet = open(r'DRuleSet.list', 'r')
# alllines = DRuleSet.readlines()
# DRuleSet.close()
# for eachline in alllines:
#     del_line(open(r'PRuleSet.list', 'r+'), eachline)


# 将部分以 'IP-CIDR,' 开头的 ipv6 地址规则改为 'IP-CIDR6,' 开头
File_r = open(r'PRuleSet.list', 'r')
alllines = File_r.readlines()
File_r.close()
File_w = open(r'PRuleSet.list', 'w')
for eachline in alllines:
    g = re.search(':', eachline)
    if g:
        a = eachline.replace('IP-CIDR,', 'IP-CIDR6,')
        File_w.writelines(a)
    else:
        File_w.writelines(eachline)
File_w.close()

# Extract_Line(open(r'PROXY/IP-CIDR.txt', 'r'), open(r'PROXY/IP-CIDR6.txt', 'w'), ':')
# File_r = open(r'PROXY/IP-CIDR6.txt', 'r')
# alllines = File_r.readlines()
# File_r.close()
# File_w = open(r'PROXY/IP-CIDR6.txt', 'w')
# for eachline in alllines:
#     a = eachline.replace('IP-CIDR,', 'IP-CIDR6,')
#     File_w.writelines(a)
# File_w.close()


# All = open(r'customq.conf', 'w')
# RuleSet = open(r'RuleSet.txt', 'r')
# DRuleSet = open(r'DRuleSet.txt', 'r')
# PRuleSet = open(r'PRuleSet.txt', 'r')
# url = open(r'BLOCK/URL.list', 'r')
# titleq = open(r'原始文件/titleq.txt', 'r')
# tail = open(r'原始文件/tail.txt', 'r')
# All.write(titleq.read())
# All.write(PRuleSet.read())
# All.write(DRuleSet.read())
# All.write(RuleSet.read())
# All.write(url.read())
# All.write(tail.read())
# All.close()
# RuleSet.close()
# DRuleSet.close()
# PRuleSet.close()
# url.close()
# titleq.close()
# tail.close()


# ,no-resolveDOMAIN-SUFFIX,0.nextyourcontent.com,REJECT
del_line(open(r'RuleSet.list', 'r+'),
         ',no-resolveDOMAIN-SUFFIX,0.nextyourcontent.com')

del_line(open(r'RuleSet.list', 'r+'),
         'There is a version of this file that uses 127.0.0.1 instead of DOMAIN,')
del_line(open(r'RuleSet.list', 'r+'),
         'that reads "DOMAIN,machine.domain.tld". This will have the effect of')


# 添加 Apple 规则
Merge_File(open(r'DRuleSet.list', 'a'),
           open(r'原始文件/Apple_Direct.txt', 'r'))
Merge_File(open(r'PRuleSet.list', 'a'), open(r'原始文件/Apple_Proxy.txt', 'r'))
Merge_File(open(r'DRuleSet.list', 'a'),
           open(r'原始文件/Apple_Direct_USER-AGENT.txt', 'r'))
Merge_File(open(r'PRuleSet.list', 'a'), open(
    r'原始文件/Apple_Proxy_USER-AGENT.txt', 'r'))

a = open(r'a.list', 'w')
a.close()
b = open(r'b.list', 'w')
b.close()
Remove_Repetition(open(r'DRuleSet.list', 'r'), open(r'a.list', 'a'))
Remove_Repetition(open(r'PRuleSet.list', 'r'), open(r'b.list', 'a'))
a = open(r'a.list', 'r')
a1 = open(r'DRuleSet.list', 'w')
a1.write(a.read())
a.close()
a1.close
b = open(r'b.list', 'r')
b1 = open(r'PRuleSet.list', 'w')
b1.write(b.read())
b.close()
b1.close
remove(r'a.list')
remove(r'b.list')


# 创建 DOMAIN-SET 规则集
Extract_Line(open(r'RuleSet.list', 'r'), open(
    r'BLOCK/DOMAIN.txt', 'w'), "DOMAIN-SUFFIX,|DOMAIN,")
Extract_Line(open(r'DRuleSet.list', 'r'), open(
    r'DIRECT/DOMAIN.txt', 'w'), "DOMAIN-SUFFIX,|DOMAIN,")
Extract_Line(open(r'PRuleSet.list', 'r'), open(
    r'PROXY/DOMAIN.txt', 'w'), "DOMAIN-SUFFIX,|DOMAIN,")


# 将 DOMAIN.txt 的内容复制给 BLOCK/DOMAIN-SET.txt
BLOCKDomainSet = open(r'BLOCK/DOMAIN-SET.txt', 'w')
out = open(r'BLOCK/DOMAIN.txt', 'r')
BLOCKDomainSet.write(out.read())
BLOCKDomainSet.close()
out.close()
DIRECTDomainSet = open(r'DIRECT/DOMAIN-SET.txt', 'w')
out = open(r'DIRECT/DOMAIN.txt', 'r')
DIRECTDomainSet.write(out.read())
DIRECTDomainSet.close()
out.close()
PROXYDomainSet = open(r'PROXY/DOMAIN-SET.txt', 'w')
out = open(r'PROXY/DOMAIN.txt', 'r')
PROXYDomainSet.write(out.read())
PROXYDomainSet.close()
out.close()

File_r = open(r'BLOCK/DOMAIN-SET.txt', 'r')
alllines = File_r.readlines()
File_r.close()
File_w = open(r'BLOCK/DOMAIN-SET.txt', 'w')
for eachline in alllines:
    a = eachline.replace('DOMAIN-SUFFIX,', '.')
    File_w.writelines(a)
File_w.close()
File_r = open(r'DIRECT/DOMAIN-SET.txt', 'r')
alllines = File_r.readlines()
File_r.close()
File_w = open(r'DIRECT/DOMAIN-SET.txt', 'w')
for eachline in alllines:
    a = eachline.replace('DOMAIN-SUFFIX,', '.')
    File_w.writelines(a)
File_w.close()
File_r = open(r'PROXY/DOMAIN-SET.txt', 'r')
alllines = File_r.readlines()
File_r.close()
File_w = open(r'PROXY/DOMAIN-SET.txt', 'w')
for eachline in alllines:
    a = eachline.replace('DOMAIN-SUFFIX,', '.')
    File_w.writelines(a)
File_w.close()

File_r = open(r'BLOCK/DOMAIN-SET.txt', 'r')
alllines = File_r.readlines()
File_r.close()
File_w = open(r'BLOCK/DOMAIN-SET.txt', 'w')
for eachline in alllines:
    a = eachline.replace('DOMAIN,', '.')
    File_w.writelines(a)
File_w.close()
File_r = open(r'DIRECT/DOMAIN-SET.txt', 'r')
alllines = File_r.readlines()
File_r.close()
File_w = open(r'DIRECT/DOMAIN-SET.txt', 'w')
for eachline in alllines:
    a = eachline.replace('DOMAIN,', '.')
    File_w.writelines(a)
File_w.close()
File_r = open(r'PROXY/DOMAIN-SET.txt', 'r')
alllines = File_r.readlines()
File_r.close()
File_w = open(r'PROXY/DOMAIN-SET.txt', 'w')
for eachline in alllines:
    a = eachline.replace('DOMAIN,', '.')
    File_w.writelines(a)
File_w.close()


# IP-CIDR 规则集
Extract_Line(open(r'RuleSet.list', 'r'), open(
    r'BLOCK/IP-CIDR.txt', 'w'), "IP-CIDR,|IP-CIDR6,")
Extract_Line(open(r'DRuleSet.list', 'r'), open(
    r'DIRECT/IP-CIDR.txt', 'w'), "IP-CIDR,|IP-CIDR6,")
Extract_Line(open(r'PRuleSet.list', 'r'), open(
    r'PROXY/IP-CIDR.txt', 'w'), "IP-CIDR,|IP-CIDR6,")

File_r = open(r'BLOCK/IP-CIDR.txt', 'r')
alllines = File_r.readlines()
File_r.close()
File_w = open(r'BLOCK/IP-CIDR.txt', 'w')
for eachline in alllines:
    a = eachline.replace('# 广告列表 adblock rules', '')
    File_w.writelines(a)
File_w.close()


# keyword 规则集
Extract_Line(open(r'RuleSet.list', 'r'), open(
    r'BLOCK/KEYWORD.txt', 'w'), "DOMAIN-KEYWORD,")
Extract_Line(open(r'DRuleSet.list', 'r'), open(
    r'DIRECT/KEYWORD.txt', 'w'), "DOMAIN-KEYWORD,")
Extract_Line(open(r'PRuleSet.list', 'r'), open(
    r'PROXY/KEYWORD.txt', 'w'), "DOMAIN-KEYWORD,")

# USER-AGENT 规则集
Extract_Line(open(r'DRuleSet.list', 'r'), open(
    r'DIRECT/USER-AGENT.txt', 'w'), "USER-AGENT,")
Extract_Line(open(r'PRuleSet.list', 'r'), open(
    r'PROXY/USER-AGENT.txt', 'w'), "USER-AGENT,")


sorted_file_content(r'BLOCK/DOMAIN-SET.txt')
sorted_file_content(r'BLOCK/DOMAIN.txt')
sorted_file_content(r'BLOCK/IP-CIDR.txt')
sorted_file_content(r'BLOCK/KEYWORD.txt')
sorted_file_content(r'BLOCK/URL.txt')

sorted_file_content(r'DIRECT/DOMAIN-SET.txt')
sorted_file_content(r'DIRECT/DOMAIN.txt')
sorted_file_content(r'DIRECT/IP-CIDR.txt')
sorted_file_content(r'DIRECT/KEYWORD.txt')
sorted_file_content(r'DIRECT/URL.txt')
sorted_file_content(r'DIRECT/USER-AGENT.txt')

sorted_file_content(r'PROXY/DOMAIN-SET.txt')
sorted_file_content(r'PROXY/DOMAIN.txt')
sorted_file_content(r'PROXY/IP-CIDR.txt')
sorted_file_content(r'PROXY/KEYWORD.txt')
sorted_file_content(r'PROXY/URL.txt')
sorted_file_content(r'PROXY/USER-AGENT.txt')


# 合并生成 Shadowrocket 配置文件
Extract_Line(open(r'RuleSet.list', 'r'), open(
    r'RuleSet_DOMAIN-SUFFIX.txt', 'w'), "DOMAIN-SUFFIX,")
Extract_Line(open(r'RuleSet.list', 'r'), open(
    r'RuleSet_DOMAIN.txt', 'w'), "DOMAIN,")
Extract_Line(open(r'RuleSet.list', 'r'), open(
    r'RuleSet_IP.txt', 'w'), "IP-CIDR,|IP-CIDR6,")
Extract_Line(open(r'RuleSet.list', 'r'), open(
    r'RuleSet_DOMAIN-KEYWORD.txt', 'w'), "DOMAIN-KEYWORD,")


Extract_Line(open(r'DRuleSet.list', 'r'), open(
    r'DRuleSet_DOMAIN-SUFFIX.txt', 'w'), "DOMAIN-SUFFIX,")
Extract_Line(open(r'DRuleSet.list', 'r'), open(
    r'DRuleSet_DOMAIN.txt', 'w'), "DOMAIN,")
Extract_Line(open(r'DRuleSet.list', 'r'), open(
    r'DRuleSet_IP.txt', 'w'), "IP-CIDR,|IP-CIDR6,")
Extract_Line(open(r'DRuleSet.list', 'r'), open(
    r'DRuleSet_DOMAIN-KEYWORD.txt', 'w'), "DOMAIN-KEYWORD,")
Extract_Line(open(r'DRuleSet.list', 'r'), open(
    r'DRuleSet_USER-AGENT.txt', 'w'), "USER-AGENT,")


Extract_Line(open(r'PRuleSet.list', 'r'), open(
    r'PRuleSet_DOMAIN-SUFFIX.txt', 'w'), "DOMAIN-SUFFIX,")
Extract_Line(open(r'PRuleSet.list', 'r'), open(
    r'PRuleSet_DOMAIN.txt', 'w'), "DOMAIN,")
Extract_Line(open(r'PRuleSet.list', 'r'), open(
    r'PRuleSet_IP.txt', 'w'), "IP-CIDR,|IP-CIDR6,")
Extract_Line(open(r'PRuleSet.list', 'r'), open(
    r'PRuleSet_DOMAIN-KEYWORD.txt', 'w'), "DOMAIN-KEYWORD,")
Extract_Line(open(r'PRuleSet.list', 'r'), open(
    r'PRuleSet_USER-AGENT.txt', 'w'), "USER-AGENT,")


add_after_line(r'RuleSet_DOMAIN-SUFFIX.txt', ',REJECT\n')
add_after_line(r'RuleSet_DOMAIN.txt', ',REJECT\n')
add_after_line(r'RuleSet_IP.txt', ',REJECT\n')
add_after_line(r'RuleSet_DOMAIN-KEYWORD.txt', ',REJECT\n')
sorted_file_content(r'RuleSet_DOMAIN-SUFFIX.txt')
sorted_file_content(r'RuleSet_DOMAIN.txt')
sorted_file_content(r'RuleSet_IP.txt')
sorted_file_content(r'RuleSet_DOMAIN-KEYWORD.txt')

add_after_line(r'DRuleSet_DOMAIN-SUFFIX.txt', ',DIRECT\n')
add_after_line(r'DRuleSet_DOMAIN.txt', ',DIRECT\n')
add_after_line(r'DRuleSet_IP.txt', ',DIRECT\n')
add_after_line(r'DRuleSet_DOMAIN-KEYWORD.txt', ',DIRECT\n')
add_after_line(r'DRuleSet_USER-AGENT.txt', ',DIRECT\n')
sorted_file_content(r'DRuleSet_DOMAIN-SUFFIX.txt')
sorted_file_content(r'DRuleSet_DOMAIN.txt')
sorted_file_content(r'DRuleSet_IP.txt')
sorted_file_content(r'DRuleSet_DOMAIN-KEYWORD.txt')
sorted_file_content(r'DRuleSet_USER-AGENT.txt')

add_after_line(r'PRuleSet_DOMAIN-SUFFIX.txt', ',PROXY\n')
add_after_line(r'PRuleSet_DOMAIN.txt', ',PROXY\n')
add_after_line(r'PRuleSet_IP.txt', ',PROXY\n')
add_after_line(r'PRuleSet_DOMAIN-KEYWORD.txt', ',PROXY\n')
add_after_line(r'PRuleSet_USER-AGENT.txt', ',PROXY\n')
sorted_file_content(r'PRuleSet_DOMAIN-SUFFIX.txt')
sorted_file_content(r'PRuleSet_DOMAIN.txt')
sorted_file_content(r'PRuleSet_IP.txt')
sorted_file_content(r'PRuleSet_DOMAIN-KEYWORD.txt')
sorted_file_content(r'PRuleSet_USER-AGENT.txt')


a = open(r'BLOCK/URL.list', 'w')
RuleSet = open(r'BLOCK/URL.txt', 'r')
a.write(RuleSet.read())
RuleSet.close()
a.close()
RuleSet = open(r'BLOCK/URL.list', 'r')
alllines = RuleSet.readlines()
RuleSet.close()
RuleSet = open(r'BLOCK/URL.list', 'w')
for eachline in alllines:
    a = eachline.strip() + ',REJECT\n'
    RuleSet.writelines(a)
RuleSet.close()


a1 = open(r'RuleSet_DOMAIN-SUFFIX.txt', 'r')
a2 = open(r'RuleSet_DOMAIN.txt', 'r')
a3 = open(r'RuleSet_IP.txt', 'r')
a4 = open(r'RuleSet_DOMAIN-KEYWORD.txt', 'r')


b1 = open(r'DRuleSet_DOMAIN-SUFFIX.txt', 'r')
b2 = open(r'DRuleSet_DOMAIN.txt', 'r')
b3 = open(r'DRuleSet_IP.txt', 'r')
b4 = open(r'DIRECT/USER-AGENT.txt', 'r')


c1 = open(r'PRuleSet_DOMAIN-SUFFIX.txt', 'r')
c2 = open(r'PRuleSet_DOMAIN.txt', 'r')
c3 = open(r'PRuleSet_IP.txt', 'r')
c4 = open(r'PROXY/USER-AGENT.txt', 'r')


All = open(r'custom.conf', 'w')
# RuleSet = open(r'RuleSet.txt', 'r')
# DRuleSet = open(r'DRuleSet.txt', 'r')
# PRuleSet = open(r'PRuleSet.txt', 'r')
url = open(r'BLOCK/URL.list', 'r')
title = open(r'原始文件/title.txt', 'r')
tail = open(r'原始文件/tail.txt', 'r')
All.write(title.read())
All.write(a1.read())
All.write(a2.read())
All.write(a3.read())
All.write(a4.read())
All.write(b1.read())
All.write(b2.read())
All.write(b3.read())
All.write(b4.read())
All.write(c1.read())
All.write(c2.read())
All.write(c3.read())
All.write(c4.read())
# All.write(DRuleSet.read())
# All.write(PRuleSet.read())
# All.write(RuleSet.read())
All.write(url.read())
All.write(tail.read())
All.close()
a1.close()
a2.close()
a3.close()
a4.close()
b1.close()
b2.close()
b3.close()
b4.close()
c1.close()
c2.close()
c3.close()
c4.close()
url.close()
title.close()
tail.close()

# del_line(open(r'custom.conf', 'r+'), 'DOMAIN-KEYWORD,')


remove(r'AdBlockList.txt')
remove(r'DirectList.txt')
remove(r'ProxyList.txt')
remove(r'adblock.txt')
remove(r'domain.txt')
remove(r'domainset.txt')
remove(r'host.txt')
remove(r'RuleSet.list')
remove(r'DRuleSet.list')
remove(r'PRuleSet.list')

# remove(r'RuleSet.txt')
# remove(r'DRuleSet.txt')
# remove(r'PRuleSet.txt')
remove(r'BLOCK/URL.list')

remove(r'out1.txt')
remove(r'out2.txt')
remove(r'out3.txt')

remove(r'RuleSet_DOMAIN-SUFFIX.txt')
remove(r'RuleSet_DOMAIN.txt')
remove(r'RuleSet_IP.txt')
remove(r'RuleSet_DOMAIN-KEYWORD.txt')
remove(r'DRuleSet_DOMAIN-SUFFIX.txt')
remove(r'DRuleSet_DOMAIN.txt')
remove(r'DRuleSet_IP.txt')
remove(r'DRuleSet_DOMAIN-KEYWORD.txt')
remove(r'DRuleSet_USER-AGENT.txt')
remove(r'PRuleSet_DOMAIN-SUFFIX.txt')
remove(r'PRuleSet_DOMAIN.txt')
remove(r'PRuleSet_IP.txt')
remove(r'PRuleSet_DOMAIN-KEYWORD.txt')
remove(r'PRuleSet_USER-AGENT.txt')

# remove(r'BLOCK/total.list')
# remove(r'out.txt')
