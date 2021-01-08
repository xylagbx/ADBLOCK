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


org = open(r'原始文件/Rule_set/dns-f.txt', 'r')
ipv4 = open(r'原始文件/Rule_set/dns-g.txt', 'w')
# ipv6 = open(r'PROXY/ipv6.txt', 'w')

Extract_Line(org, ipv4, 'DOMAIN,|DOMAIN-SUFFIX,')
# org = open(r'PROXY/IP-CIDR.txt', 'r')
# Extract_Line(org, ipv6, 'IP-CIDR6,')
