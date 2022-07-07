#3-4 嘉宾名单
lists = ['johnson', 'helen', 'liliana']
print("Hello, "+lists[0].title()+", welcome to dinner!")
print("Hello, "+lists[1].title()+", welcome to dinner!")
print("Hello, "+lists[2].title()+", welcome to dinner!")

#3-5 修改嘉宾名单
lists = ['johnson', 'helen', 'liliana']
not_come = lists.pop(0)
lists.append('Kevin')
print("\nHello, "+lists[0].title()+", welcome to dinner!")
print("Hello, "+lists[1].title()+", welcome to dinner!")
print("Hello, "+lists[2].title()+", welcome to dinner!")
print("For some reasons, "+not_come.title()+" cannot come to this dinner.")

#3-6 添加嘉宾
lists = ['helen', 'liliana', 'kevin']
lists.insert(0, 'gloria')
lists.insert(3, 'teo')
lists.append('darren')
print("\nHello, "+lists[0].title()+", welcome to dinner!")
print("Hello, "+lists[1].title()+", welcome to dinner!")
print("Hello, "+lists[2].title()+", welcome to dinner!")
print("Hello, "+lists[3].title()+", welcome to dinner!")
print("Hello, "+lists[4].title()+", welcome to dinner!")
print("Hello, "+lists[5].title()+", welcome to dinner!")
print("As we have found a larger table, other three guests will come and join the dinner!")

#3-7 缩减名单
lists = ['helen', 'liliana', 'kevin']
lists.insert(0, 'gloria')
lists.insert(3, 'teo')
lists.append('darren')
print("\nI feel so sorry, "+lists.pop()+", I cannot invite you to tonight's dinner as the new dinning table couldn't arrive in time.")
print("I feel so sorry, "+lists.pop()+", I cannot invite you to tonight's dinner as the new dinning table couldn't arrive in time.")
print("I feel so sorry, "+lists.pop()+", I cannot invite you to tonight's dinner as the new dinning table couldn't arrive in time.")
print("I feel so sorry, "+lists.pop()+", I cannot invite you to tonight's dinner as the new dinning table couldn't arrive in time.")
print("My beloved guest, "+lists[0]+", I am happy to tell you that you can still join the dinner!")
print("My beloved guest, "+lists[1]+", I am happy to tell you that you can still join the dinner!")
del lists[0]
del lists[0]
print(lists)