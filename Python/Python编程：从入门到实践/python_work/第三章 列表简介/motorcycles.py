#修改列表元素
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
motorcycles[0] = 'ducati'
print(motorcycles)

#添加元素
motorcycles = []
motorcycles.append('honda')
print(motorcycles)

#插入元素
motorcycles.insert(0, 'ducati')
print(motorcycles)

#删除元素
#使用del语句，不再使用它的值
del motorcycles[0]
print(motorcycles)

#使用pop() 删除/弹出末尾并接着使用它的值
motorcycles = ['honda', 'yamaha', 'suzuki']
poped_motorcycle = motorcycles.pop()
print(motorcycles)
print(poped_motorcycle)
print("The last motorcycle I owned was a "+poped_motorcycle.title()+".")

#弹出指定位置的元素
motorcycles = ['honda', 'yamaha', 'suzuki']
first_owned = motorcycles.pop(0)
print("The first motorcycle I owned was a "+first_owned.title()+".")

#根据值删除remove()
motorcycles = ['honda', 'yamaha', 'suzuki']
motorcycles.remove('suzuki')
print(motorcycles)

#使用remove()，并接着使用它的值
motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
too_expensive = 'ducati'
motorcycles.remove('ducati')
print(motorcycles)
print("\nA "+too_expensive.title()+" is too expensive for me.")