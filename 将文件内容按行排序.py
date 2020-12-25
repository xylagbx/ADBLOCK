#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from posix import remove


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


# a = open(r'原始文件/clash.txt', 'r')
# out = open(r'out.list', 'w')
# out.write(a.read())
# a.close()
# a = open(r'原始文件/clash.txt', 'w')
# sorted_file_content(a)


# a = r'原始文件/clash.txt'
sorted_file_content(r'原始文件/clash.txt')
