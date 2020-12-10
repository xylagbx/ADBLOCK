# # 删除末尾的 '^'
# adblock = open(
#     '/Users/bx/Library/Mobile Documents/com~apple~CloudDocs/备忘/custom/adblock.txt', 'r')
# alllines = adblock.readlines()
# adblock.close()
# adblock = open(
#     '/Users/bx/Library/Mobile Documents/com~apple~CloudDocs/备忘/custom/adblock.txt', 'w')
# for eachline in alllines:
#     a = eachline.replace('^', '')
#     # a = re.sub('^\n', '\n', eachline)
#     # a = eachline.strip('^')
#     adblock.writelines(a)
# adblock.close()

# # 替换开头的 '||' 为 'DOMAIN-SUFFIX,'
# adblock = open(
#     '/Users/bx/Library/Mobile Documents/com~apple~CloudDocs/备忘/custom/adblock.txt', 'r')
# alllines = adblock.readlines()
# adblock.close()
# adblock = open(
#     '/Users/bx/Library/Mobile Documents/com~apple~CloudDocs/备忘/custom/adblock.txt', 'w')
# for eachline in alllines:
#     # a = re.sub('||', 'DOMAIN-SUFFIX,', eachline)
#     a = eachline.replace('||', 'DOMAIN-SUFFIX,')
#     adblock.writelines(a)
# adblock.close()


# utf-8 改 ascii
# ruleset = open(
#     '/Users/bx/Library/Mobile Documents/com~apple~CloudDocs/备忘/custom/RuleSet.list', 'r')
# alllines = ruleset.readlines()
# ruleset.close()
# ruleset = open(
#     '/Users/bx/Library/Mobile Documents/com~apple~CloudDocs/备忘/custom/RuleSet.txt', 'w')
# for eachline in alllines:
#     # a = eachline.decode('utf-8')
#     # printable = set(string.eachline)
#     # a = filter(lambda x: x in eachline, s)
#     for char in eachline:
#         char = ord(char)
#         # a = a.decode('utf-8')
#     ruleset.writelines(eachline)
# ruleset.close()

# content = codecs.open(
#     '/Users/bx/Library/Mobile Documents/com~apple~CloudDocs/备忘/custom/RuleSet.list', 'r', 'utf-8').write(content)

# codecs.open("/Users/bx/Library/Mobile Documents/com~apple~CloudDocs/备忘/custom/RuleSet.txt",
#             'w', encoding='ascii').write(content)

# filename = '/Users/bx/Library/Mobile Documents/com~apple~CloudDocs/备忘/custom/RuleSet.txt'
# content = codecs.open(filename, 'r').read()
# # rule = content.write(content)
# # sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())
# codecs.open(filename, 'w', encoding='utf-8').write(content)


# 删除具有特定内容的行
# with open(r'RuleSet.list', "r+") as f:
#     # p = re.compile("#|/|_|\*|\^")
#     p = re.compile("\^")
#     lines = [line for line in f.readlines() if p.search(line) is None]
#     f.seek(0)
#     f.truncate(0)
#     f.writelines(lines)

# # 删除末尾的 '^'
# AdBlockList = open(r'AdBlockList.txt', 'r')
# alllines = AdBlockList.readlines()
# AdBlockList.close()
# AdBlockList = open(r'AdBlockList.txt', 'w')
# for eachline in alllines:
#     # a = re.sub('^\n', '\n', eachline)
#     a = eachline.replace('^', '\n')
#     # a = a.replace('$important', '')
#     # a = a.strip('imo.com')
#     # a = a.replace(',DIRECT\n', '\n')
#     # a = eachline.strip('^')
#     AdBlockList.writelines(a)
# AdBlockList.close()

# 删除本地原有的文件
# remove(r'AdBlock.txt')


# # 将 DOMAIN-SET.list 与 DOMAINreject.txt 合并去重
# total = open(r'BLOCK/total.list', 'w')
# BLOCKDomainSet=open(r'BLOCK/DOMAIN-SET.list', 'r')
# dset = open(r'原始文件/Rule_set/DOMAINreject.txt', 'r')
# total.write(dset.read())
# total.write(BLOCKDomainSet.read())
# BLOCKDomainSet.close()
# dset.close()
# total.close()
# Remove_Repetition(open(r'BLOCK/total.list', 'r'), open(r'out.txt', 'w'))
# out=open(r'out.txt', 'r')
# BLOCKDomainSet=open(r'BLOCK/DOMAIN-SET.list', 'w')
# BLOCKDomainSet.write(out.read())
# BLOCKDomainSet.close()
# out.close()


# # 将 DOMAIN.txt 与 DOMAINreject.txt 合并去重
# domain = open(r'BLOCK/DOMAIN.txt', 'r')
# total = open(r'BLOCK/total.list', 'w')
# dset = open(r'原始文件/Rule_set/DOMAINreject.txt', 'r')
# total.write(dset.read())
# total.write(domain.read())
# domain.close()
# dset.close()
# total.close()

# File_r = open(r'BLOCK/total.list', 'r')
# alllines = File_r.readlines()
# File_r.close()
# File_w = open(r'BLOCK/total.list', 'w')
# for eachline in alllines:
#     a = eachline.replace('\n.', '\nDOMAIN-SUFFIX,')
#     File_w.writelines(a)
# File_w.close()

# Remove_Repetition(open(r'BLOCK/total.list', 'r'), open(r'out.txt', 'w'))
# out = open(r'out.txt', 'r')
# domain = open(r'BLOCK/DOMAIN.txt', 'w')
# domain.write(out.read())
# domain.close()
# out.close()


# Merge_Files(AdBlockList, urls)
# # enfk.wefoi()
# Merge_Files(adblock, Adblock)
# Merge_Files(domain, Domain)
# Merge_Files(host, Host)
# # Merge_Files(dset, Dset)
# myblack.close()




## 函数
import re
def Download_Cloud(urls):
    """从云端下载并保存在本地"""
    for web_url, local_url in urls:
        myfile = requests.get(web_url)
        open(local_url, 'wb').write(myfile.content)


def Merge_Files(tag, urls):
    """循环合并文件"""
    for web_url, local_url in urls:
        x = open(local_url,  "r")
        tag.write(x.read())
        x.close()
    tag.close()


def Merge_File(tag, org):
    """将文件 org 合并到文件 tag 中"""
    tag.write(org.read())
    org.close()
    tag.close()


# def Replace_Words(File_r, File_w, tag, org):
#     """
#     将 File 文件中的某些字符或字符串 org 替换为 tag
#     """
    # alllines = File_r.readlines()
    # File_r.close()
    # for eachline in alllines:
    #     a = eachline.replace(org, tag)
    #     File_w.writelines(a)
    # File_w.close()


def Extract_Line(file1, file2, words):
    """将 file1 中包含 words 的行提取到 file2 中"""
    try:
        for line in file1:
            g = re.search(words, line)
            if g:
                # print(g.group())
                file2.writelines(line)
    finally:
        file1.close()
        file2.close()


def Remove_Repetition(file1, file2):
    """将 file1 去除重复的行，并写入 file2 中，file1 保持原样"""
    with file1 as f, file2 as ff:
        data = [item.strip() for item in f.readlines()]  # 针对最后一行没有换行符，与其他它行重复的情况
        new_data = list(set(data))
        # 针对去除文件中有多行空行的情况
        ff.writelines([item + '\n' for item in new_data if item])
    file1.close()
    file2.close()


def del_line(file, words):
    """删除具有特定内容的行"""
    with file as f:
        p = re.compile(words)
        lines = [line for line in f.readlines() if p.search(line) is None]
        f.seek(0)
        f.truncate(0)
        f.writelines(lines)
