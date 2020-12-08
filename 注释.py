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


def Replace_Words(File_r, File_w, tag, org):
    """
    将 File 文件中的某些字符或字符串 org 替换为 tag
    """
    alllines = File_r.readlines()
    File_r.close()
    for eachline in alllines:
        a = eachline.replace(org, tag)
        File_w.writelines(a)
    File_w.close()


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
