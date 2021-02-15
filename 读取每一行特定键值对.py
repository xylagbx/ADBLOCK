import json

org = open(r'/Users/bx/Downloads/Uncategorized/未命名文件夹/querylog1.json', 'r')
alllines = org.readlines()
tag = open(r'/Users/bx/Downloads/Uncategorized/未命名文件夹/addomain.json', 'w')
for eachline in alllines:
    eachline = json.loads(eachline)
    tag.writelines(eachline["QH"] + '\n')
