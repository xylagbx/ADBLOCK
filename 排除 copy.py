import re


def del_line(file, words):
    """删除具有特定内容的行"""
    with file as f:
        p = re.compile(words)
        lines = [line for line in f.readlines() if p.search(line) is None]
        f.seek(0)
        f.truncate(0)
        f.writelines(lines)


# RuleSet = open(
#     r'/Users/bx/Downloads/Uncategorized/custom/原始文件/mywhite的副本.txt', 'r')
# alllines = RuleSet.readlines()
# RuleSet.close()
# for eachline in alllines:
eachline = open(
    r'/Users/bx/Downloads/Uncategorized/custom/原始文件/未命名文件夹/surge2.txt', 'r').read()
del_line(open(
    r'/Users/bx/Downloads/Uncategorized/custom/原始文件/未命名文件夹/dns-filter.txt', 'r+'), eachline)
# del_line(open(r'/Users/bx/Downloads/未命名文件夹/rule/URL.txt', 'r+'), eachline)


# eachline = open(r'/Users/bx/Downloads/未命名文件夹/rule/IP-CIDR.txt', 'r').read()
# del_line(open(r'/Users/bx/Downloads/未命名文件夹/domain/annoyances-filter.txt', 'r+'), eachline)
# del_line(open(r'/Users/bx/Downloads/未命名文件夹/domain/base-filter.txt', 'r+'), eachline)
# del_line(open(r'/Users/bx/Downloads/未命名文件夹/domain/chinese-filter.txt', 'r+'), eachline)
# del_line(open(r'/Users/bx/Downloads/未命名文件夹/domain/myblack.txt', 'r+'), eachline)
# del_line(open(r'/Users/bx/Downloads/未命名文件夹/domain/neohosts-full.txt', 'r+'), eachline)
# del_line(open(r'/Users/bx/Downloads/未命名文件夹/domain/social-media-filter.txt', 'r+'), eachline)
# del_line(open(r'/Users/bx/Downloads/未命名文件夹/domain/tracking-protection-filter.txt', 'r+'), eachline)
# del_line(open(r'/Users/bx/Downloads/未命名文件夹/rule/BanAD.list', 'r+'), eachline)
# del_line(open(r'/Users/bx/Downloads/未命名文件夹/rule/BanEasyListChina.list', 'r+'), eachline)
# del_line(open(r'/Users/bx/Downloads/未命名文件夹/rule/BanEasyPrivacy.list', 'r+'), eachline)
# del_line(open(r'/Users/bx/Downloads/未命名文件夹/rule/BanEasyList.list', 'r+'), eachline)
# del_line(open(r'/Users/bx/Downloads/未命名文件夹/rule/Reject.list', 'r+'), eachline)
# del_line(open(r'/Users/bx/Downloads/未命名文件夹/rule/BanProgramAD.list', 'r+'), eachline)
# del_line(open(r'/Users/bx/Downloads/未命名文件夹/rule/IP-CIDR.txt', 'r+'), eachline)
# del_line(open(r'/Users/bx/Downloads/未命名文件夹/rule/KEYWORD.txt', 'r+'), eachline)
# del_line(open(r'/Users/bx/Downloads/未命名文件夹/rule/myblack (1).txt', 'r+'), eachline)
# del_line(open(r'/Users/bx/Downloads/未命名文件夹/rule/reject.txt', 'r+'), eachline)
# del_line(open(r'/Users/bx/Downloads/未命名文件夹/rule/URL.txt', 'r+'), eachline)
