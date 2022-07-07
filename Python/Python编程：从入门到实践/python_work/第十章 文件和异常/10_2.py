filename = 'learning_python.txt'
with open (filename) as file_object:
    for line in file_object:
        newline = line.replace('Python', 'C')
        print(newline.rstrip())
