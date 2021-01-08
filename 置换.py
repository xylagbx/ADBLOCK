# import requests
from posix import remove
import re

File_r = open(r'原始文件/Domain_set/myblack.txt', 'r')
alllines = File_r.readlines()
File_r.close()
File_w = open(r'原始文件/Domain_set/myblack.txt', 'w')
for eachline in alllines:
    a = eachline.replace('DOMAIN-SUFFIX,', '.')
    File_w.writelines(a)
File_w.close()


File_r = open(r'原始文件/Domain_set/myblack.txt', 'r')
alllines = File_r.readlines()
File_r.close()
File_w = open(r'原始文件/Domain_set/myblack.txt', 'w')
for eachline in alllines:
    a = eachline.replace('DOMAIN,', '.')
    File_w.writelines(a)
File_w.close()
