def Remove_Repetition(file1, file2):
    """将 file1 去除重复的行，并写入 file2 中，file1 保持原样"""
    with file1 as f, file2 as ff:
        data = [item.strip() for item in f.readlines()
                ]  # 针对最后一行没有换行符，与其他它行重复的情况
        new_data = list(set(data))
        # 针对去除文件中有多行空行的情况
        ff.writelines([item + '\n' for item in new_data if item])
    file1.close()
    file2.close()


Remove_Repetition(open(r'原始文件/Apple.txt', 'r'), open(r'out.list', 'a'))
Apple = open(r'原始文件/Apple.txt', 'w')
out = open(r'out.list', 'r')
Apple.write(out.read())
Apple.close()
out.close()