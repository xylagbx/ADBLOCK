import re
def del_line(file, words):
    """删除具有特定内容的行"""
    with file as f:
        p = re.compile(words)
        lines = [line for line in f.readlines() if p.search(line) is None]
        f.seek(0)
        f.truncate(0)
        f.writelines(lines)


"""从proxy中排除apple"""
Apple = open(r'原始文件/Apple.txt', 'r')
alllines = Apple.readlines()
Apple.close()
for eachline in alllines:
    del_line(open(r'PRuleSet.list', 'r+'), eachline)

"""从direct中排除reject"""
RuleSet = open(r'RuleSet.list', 'r')
alllines = RuleSet.readlines()
RuleSet.close()
for eachline in alllines:
    del_line(open(r'DRuleSet.list', 'r+'), eachline)

"""从proxy中排除reject，direct"""
RuleSet = open(r'RuleSet.list', 'r')
alllines = RuleSet.readlines()
RuleSet.close()
for eachline in alllines:
    del_line(open(r'PRuleSet.list', 'r+'), eachline)
DRuleSet = open(r'DRuleSet.list', 'r')
alllines = DRuleSet.readlines()
DRuleSet.close()
for eachline in alllines:
    del_line(open(r'PRuleSet.list', 'r+'), eachline)
