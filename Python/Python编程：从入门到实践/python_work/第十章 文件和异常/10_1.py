filename = 'learning_python.txt'
with open (filename) as file_object:
    # 读取整个文件
    contents = file_object.read()
    print(contents)

with open(filename) as file_object:
    # 遍历文件对象
    for line in file_object:
        print(line.rstrip())

with open(filename) as file_object:
    # 将各行存储在一个列表中，在with代码块外打印它们
    lines = file_object.readlines()
for line in lines:
    print(line.rstrip())
