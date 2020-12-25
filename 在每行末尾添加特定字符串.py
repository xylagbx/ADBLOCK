#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from posix import remove


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


add_after_line(r'myblack.txt', ',direct\n')
