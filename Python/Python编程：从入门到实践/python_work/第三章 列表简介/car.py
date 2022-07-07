# 组织列表

#sort()永久性修改列表元素排列顺序，按字母顺序
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()
print(cars)

	#按字母顺序相反的顺序
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort(reverse=True)
print(cars)

#sorted()对列表进行临时排序
cars = ['bmw', 'audi', 'toyota', 'subaru']
print("\nHere is the original list: ")
print(cars)
print("\nHere is the sorted list: ")
print(sorted(cars))
print(sorted(cars, reverse=True))
print("\nHere is the original list again: ")
print(cars)

#反转列表元素排列顺序 reverse() 直接反转而非基于字母顺序
cars = ['bmw', 'audi', 'toyota', 'subaru']
print("\n")
print(cars)
cars.reverse()
print(cars)
cars.reverse()
print(cars)

#确定/打印表的长度
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(len(cars))