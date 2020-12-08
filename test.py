#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# import requests
# from posix import remove
import re
# import chardet
# import codecs
# import urllib.request
# import sys
# import string


RuleSet = open(r'DOMAIN-BLOCK.txt', 'r')
test = open(
    r'test.txt', 'w')
test.write(RuleSet.read())
RuleSet.close()
test.close()


test = open(
    r'test.txt', 'r+')
with test as f:
    p = re.compile("DOMAIN-SUFFIX,|DOMAIN-KEYWORD,|DOMAIN,")
    lines = [line for line in f.readlines() if p.search(line) is None]
    f.seek(0)
    f.truncate(0)
    f.writelines(lines)
test.close()

# with test as f:
#     p = re.compile("DOMAIN-SUFFIX,|DOMAIN-KEYWORD,|DOMAIN,")
#     lines = [line for line in f.readlines() if p.search(line) is None]
#     f.seek(0)
#     f.truncate(0)
#     f.writelines(lines)


# file_object = open('test.txt', 'rU', encoding='UTF-8')
# f = open('/Users/bx/Library/Mobile Documents/com~apple~CloudDocs/备忘/custom/out.txt',
#          'w', encoding='UTF-8')
# try:
#     for line in test:
#         g = re.search("DOMAIN-SUFFIX,|DOMAIN-KEYWORD,|DOMAIN,", line)
#         if g:
#             # print(g.group())
#             f.writelines(line)
# finally:
#     test.close()

# RuleSet = open(
#     '/Users/bx/Library/Mobile Documents/com~apple~CloudDocs/备忘/custom/RuleSet.list', 'w')
# test = open(
#     '/Users/bx/Library/Mobile Documents/com~apple~CloudDocs/备忘/custom/test.txt', 'r')
# RuleSet.write(test.read())
# RuleSet.close()
# test.close()
