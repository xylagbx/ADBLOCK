import re


def del_line(file, words):
    """删除具有特定内容的行"""
    with file as f:
        p = re.compile(words)
        lines = [line for line in f.readlines() if p.search(line) is None]
        f.seek(0)
        f.truncate(0)
        f.writelines(lines)


myblack = open(r'原始文件/myblack.txt',  "r+", encoding="utf-8")
del_line(myblack, '#')
