#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from posix import remove


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


def sorted_file_content(filetxt):
    """将文件内容按行排序"""
    out = open(r'out.list', 'r')
    out = sorted(out)
    for item in out:
        filetxt.writelines(item)
    filetxt.close()
    remove(r'out.list')


Remove_Repetition(open(r'/Users/bx/Downloads/Uncategorized/custom/原始文件/myblack_domain_set.txt', 'r'),
                  open(r'/Users/bx/Downloads/Uncategorized/custom/原始文件/myblack_domain_set1.txt', 'a'))
# mywhite = open(r'/Users/bx/Downloads/未命名文件夹/domain2.txt', 'w')
# sorted_file_content(mywhite)
