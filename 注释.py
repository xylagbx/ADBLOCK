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
