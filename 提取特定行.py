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
    r'/Users/bx/Downloads/Uncategorized/custom/原始文件/未命名文件夹/direct/user_agent的副本.txt', 'r')
tag = open(
    r'/Users/bx/Downloads/Uncategorized/custom/原始文件/未命名文件夹/direct/user_agent.txt', 'w')
# ipv6 = open(r'PROXY/ipv6.txt', 'w')

Extract_Line(org, tag, ',DIRECT')
# org = open(r'PROXY/IP-CIDR.txt', 'r')
# Extract_Line(org, ipv6, 'IP-CIDR6,')

org = open(
    r'/Users/bx/Downloads/Uncategorized/custom/原始文件/未命名文件夹/direct/user_agent的副本.txt', 'r')
tag = open(
    r'/Users/bx/Downloads/Uncategorized/custom/原始文件/未命名文件夹/proxy/user_agent.txt', 'w')
Extract_Line(org, tag, ',PROXY')

org = open(
    r'/Users/bx/Downloads/Uncategorized/custom/原始文件/未命名文件夹/direct/user_agent的副本.txt', 'r')
tag = open(
    r'/Users/bx/Downloads/Uncategorized/custom/原始文件/未命名文件夹/reject/user_agent.txt', 'w')
Extract_Line(org, tag, ',REJECT')
