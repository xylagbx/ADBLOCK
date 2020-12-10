import re

def Extract_Line(file1, file2, words):
    """将 file1 中包含 words 的行提取到 file2 中"""
    try:
        for line in file1:
            g = re.search(words, line)
            if g:
                file2.writelines(line)
    finally:
        file1.close()
        file2.close()

org = open(r'原始文件/org.txt', 'r')
direct = open(r'原始文件/Direct.txt', 'w')
proxy = open(r'原始文件/Proxy.txt', 'w')

Extract_Line(org, direct, '')