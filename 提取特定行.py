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


org = open(
    r'/Users/bx/Downloads/Uncategorized/未命名文件夹/大圣.txt', 'r')
tag = open(
    r'/Users/bx/Downloads/Uncategorized/未命名文件夹/大圣1.txt', 'w')
# Extract_Line(org, tag, '"FilterID":1}')


Extract_Line(org, tag, '127.0.0.1')
