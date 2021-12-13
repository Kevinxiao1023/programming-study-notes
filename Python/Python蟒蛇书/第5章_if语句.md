# 第5章 if语句

Python中，if语句让你能够检查程序的当前状态，并据此采取相应的措施。

* 本章将学习条件测试，以检查感兴趣的任何条件。   
* 学习简单的if语句，以及创建一系列复杂的if语句来确定当前到底处于什么情形。   
* 把学到的知识应用于列表，以编写for循环，**以一种方式处理列表中的大多数元素，并以另一种不同的方式处理包含特定值的元素**。

## 5.1 一个简单示例


```python
cars = ['audi', 'bmw', 'subaru', 'toyota']
for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())
```

    Audi
    BMW
    Subaru
    Toyota


这个示例中的循环首先检查当前的汽车名是否是'bmw'。如果是，就以全大写的方式打印它；否则就以首字母大写的方式打印

## 5.2 条件测试

* 每条if语句的*核心*都是一个**值为True或False的表达式**，这种表达式被称为<u>条件测试</u>。   
* Python根据条件测试的值为True还是False来决定是否执行if语句中的代码。   
* 如果条件测试的值为True，Python就执行紧跟在if语句后面的代码；如果为False，Python就忽略这些代码。

### 5.2.1 检查是否相等

大多数条件测试都将一个变量的当前值同特定值进行比较。最简单的条件测试检查变量的值是否与特定值相等：


```python
car = 'bmw'
car == 'bmw'
```




    True



使用两个等号（==）检查car的值是否为'bmw'。这个**相等运算符**在它两边的值相等时返回True，否则返回False。在这个示例中，两边的值相等，因此Python返回True。


```python
car = 'audi'
car == 'bmw'
```




    False



1. 一个等号是陈述；可解读为“将变量car的值设置为'audi'”。   
2. 两个等号是发问；可解读为“变量car的值是'bmw'吗？”。   
大多数编程语言使用等号的方式都与这里演示的相同。

### 5.2.2 检查是否相等时不考虑大小写


```python
car = 'Audi'
car == 'audi'
```




    False



如果大小写很重要，检查大小写的行为有其优点。但如果大小写无关紧要，而只想检查变量的值，可**将变量的值转换为小写**，再进行比较：


```python
car = 'Audi'
car.lower() == 'audi'
```




    True



无论值'Audi'的大小写如何，上述测试都将返回True，因为该测试不区分大小写。**函数lower( )**不会修改存储在变量car中的值，因此进行这样的比较时不会影响原来的变量：


```python
car = 'Audi'
car.lower() == 'audi'
```




    True




```python
car = 'Audi'
car.lower() == 'audi'
car
```




    'Audi'



1. 首字母大写的字符串'Audi'存储在变量car中；   
2. 我们获取变量car的值并将其转换为小写，再将结果与字符串'audi'进行比较。这两个字符串相同，因此Python返回True。   
3. 根据最后的输出可知，这个**条件测试**并没有影响存储在变量car中的值。

网站采用类似的方式让用户输入的数据符合特定的格式。例如，网站可能使用类似的测试来**确保用户名是独一无二的**，而并非只是与另一个用户名的大小写不同。用户提交新的用户名时，将把它转换为小写，并与所有既有用户名的小写版本进行比较。执行这种检查时，如果已经有用户名'john'（不管大小写如何），则用户提交用户名'John'时将遭到拒绝。

### 5.2.3 检查是否不相等

要判断两个值是否不等，可结合使用惊叹号和等号（!=），其中的惊叹号表示不，在很多编程语言中都如此。


```python
requested_topping = 'mushrooms'
if requested_topping != 'anchovies':
    print("Hold the anchovies!")
```

    Hold the anchovies!


第一行的代码行将requested_topping的值与'anchovies'进行比较，   
1. 如果它们不相等，Python将返回True，进而执行紧跟在if语句后面的代码；   
2. 如果这两个值相等，Python将返回False，因此不执行紧跟在if语句后面的代码。

你编写的大多数条件表达式都检查两个值是否相等，但**有时候检查两个值是否不等的效率更高**。

### 5.2.4 比较数字


```python
age = 18
age == 18
```




    True




```python
answer = 17
if answer != 42:
    print("That is not the correct answer. Please try again!")
```

    That is not the correct answer. Please try again!


answer（17）不是42，if语句处的条件得到满足，因此缩进的代码块得以执行。

条件语句中可包含各种数学比较，如小于、小于等于、大于、大于等于：


```python
age = 19
age < 21
# <=
# >
# >=
```




    True



### 5.2.5 检查多个条件

你可能想同时检查多个条件，例如，有时候你需要在两个条件都为True时才执行相应的操作，而有时候你只要求一个条件为True时就执行相应的操作。在这些情况下，**关键字and和or**可助你一臂之力。

### 1．使用and检查多个条件

要检查是否两个条件都为True，可使用关键字and将两个条件测试合而为一；   
- 如果每个测试都通过了，整个表达式就为True；   
- 如果至少有一个测试没有通过，整个表达式就为False。


```python
age_0 = 22
age_1 = 18
age_0 >= 21 and age_1 >= 21
```




    False




```python
age_0 = 22
age_1 = 22
age_0 >= 21 and age_1 >= 21
```




    True



为改善可读性，可**将每个测试都分别放在一对括号内**，但并非必须这样做。如果你使用括号，测试将类似于下面这样：


```python
age_0 = 22
age_1 = 22
(age_0 >= 21) and (age_1 >= 21)
```




    True



### 2．使用or检查多个条件

关键字or也能够让你检查多个条件，但只要至少有一个条件满足，就能通过整个测试。仅当两个测试都没有通过时，使用or的表达式才为False。


```python
age_0 = 22
age_1 = 18
age_0 >= 21 or age_1 >= 21
```




    True




```python
age_0 = 18
age_1 = 18
age_0 >= 21 or age_1 >= 21
```




    False



### 5.2.6 检查特定值是否包含在列表中

有时候，执行操作前必须检查列表是否包含特定的值。例如，   
1. 结束用户的注册过程前，可能需要检查他提供的用户名是否已包含在用户名列表中。   
2. 在地图程序中，可能需要检查用户提交的位置是否包含在已知位置列表中。   

要判断特定的值是否已包含在列表中，可使用**关键字in**。


```python
requested_toppings = ['mushrooms', 'onions', 'pineapple']
'mushrooms' in requested_toppings
```




    True




```python
requested_toppings = ['mushrooms', 'onions', 'pineapple']
'pepperoni' in requested_toppings
```




    False



### 5.2.7 检查特定值是否不包含在列表中

确定特定的值未包含在列表中很重要；在这种情况下，可使用**关键字not in**。


```python
banned_users = ['andrews', 'carolina', 'david']
user = 'marie'
if user not in banned_users:
    print(user.title()+", you can post a response if you wish.")
```

    Marie, you can post a response if you wish.


### 5.2.8 布尔表达式

布尔表达式，它不过是条件测试的别名。与条件表达式一样，布尔表达式的结果要么为True，要么为False。

布尔值通常用于记录条件，如游戏是否正在运行，或用户是否可以编辑网站的特定内容:   
game_active = True   
can_edit = False

### 动手试一试

#### 5-1 条件测试：编写一系列条件测试；将每个测试以及你对其结果的预测和实际结果都打印出来。   
* 详细研究实际结果，直到你明白了它为何为True或False。   
* 创建至少10个测试，且其中结果分别为True和False的测试都至少有5个。


```python
car = 'audi'
if car == 'subaru':
    print("Is car == 'subaru'? I predict True.")
    print(car == 'subaru')
if car == 'audi':
    print("\nIs car == 'audi'? I predict False.")
    print(car == 'subaru')
```

    
    Is car == 'audi'? I predict False.
    False


#### 5-2 更多的条件测试：你并非只能创建10个测试。如果你想尝试做更多的比较，可再编写一些测试，并将它们加入到conditional_tests.py中。对于下面列出的各种测试，至少编写一个结果为True和False的测试。   
* 检查两个字符串相等和不等。   
* 使用函数lower()的测试。   
* 检查两个数字相等、不等、大于、小于、大于等于和小于等于。   
* 使用关键字and和or的测试。   
* 测试特定的值是否包含在列表中。   
* 测试特定的值是否未包含在列表中。


```python
str1 = 'gavin'
str2 = 'Gavin'
# 区分大小写，所以str1与str2不相等
if str2.lower() == 'gavin':
    print(str1 == str2)
```

    False


## 5.3 if语句

### 5.3.1 简单的if语句

最简单的if语句只有一个测试和一个操作：   
if conditional_test:   
    do something   

在第1行中，可包含任何条件测试，而在紧跟在测试后面的缩进代码块中，可执行任何操作。如果条件测试的结果为True，Python就会执行紧跟在if语句后面的代码；否则Python将忽略这些代码。


```python
age = 19
if age >= 18:
    print("You are old enough to vote!")
```

    You are old enough to vote!


Python检查变量age的值是否大于或等于18；答案是肯定的，因此Python执行缩进的print语句。

在if语句中，**缩进的作用与for循环中相同**。如果测试通过了，将执行if语句后面所有缩进的代码行，否则将忽略它们。


```python
age = 19
if age >= 18:
    print("You are old enough to vote!")
    print("Have you registered to vote yet?")
```

    You are old enough to vote!
    Have you registered to vote yet?


### 5.3.2 if-else语句

经常需要在条件测试通过了时执行一个操作，并在没有通过时执行另一个操作；在这种情况下，可使用Python提供的if-else语句。if-else语句块类似于简单的if语句，但其中的else语句让你能够指定条件测试未通过时要执行的操作。


```python
age = 17
if age >= 18:
    print("You are old enough to vote!")
    print("Have you registered to vote yet?")
else:
    print("Sorry, you are too young to vote.")
    print("Please register to vote as soon as you turn 18!")
```

    Sorry, you are too young to vote.
    Please register to vote as soon as you turn 18!


if-else结构非常适合用于要让Python执行两种操作之一的情形。在这种简单的if-else结构中，总是会执行两个操作中的一个。

### 5.3.3 if-elif-else结构

经常**需要检查超过两个的情形**，为此可使用Python提供的if-elif-else结构。Python只执行if-elif-else结构中的一个代码块，它依次检查每个条件测试，直到遇到通过了的条件测试。测试通过后，Python将执行紧跟在它后面的代码，并跳过余下的测试。


```python
age = 12
if age < 4:
    print("Your admission cost is $0.")
elif age < 18:
    print("Your admission cost is $5.")
else:
    print("Your admission cost is $10.")
```

    Your admission cost is $5.


为让代码更简洁，可不在if-elif-else代码块中打印门票价格，而只在其中设置门票价格，并在它后面添加一条简单的print语句：


```python
age = 12
if age < 4:
    price = 0
elif age < 18:
    price = 5
else:
    price = 10
print("Your admission cost is $"+str(price)+".")
```

    Your admission cost is $5.


除效率更高外，这些修订后的代码还更容易修改：要调整输出消息的内容，只需修改一条而不是三条print语句。

### 5.3.4 使用多个elif代码块


```python
age = 12
if age < 4:
    price = 0
elif age < 18:
    price = 5
elif age < 65:
    price = 10
else:
    price = 5
print("Your admission cost is $"+str(price)+".")
```

    Your admission cost is $5.


### 5.3.5 省略else代码块

Python并不要求if-elif结构后面必须有else代码块。在有些情况下，else代码块很有用；而在其他一些情况下，使用一条elif语句来处理特定的情形更清晰：


```python
age = 12
if age < 4:
    price = 0
elif age < 18:
    price = 5
elif age < 65:
    price = 10
elif age >= 65:
    price = 5
print("Your admission cost is $"+str(price)+".")
```

    Your admission cost is $5.


elif代码块在顾客的年龄超过65（含）时，将价格设置为5美元，这比使用else代码块更清晰些。经过这样的修改后，每个代码块都仅在通过了相应的测试时才会执行。

else是一条包罗万象的语句，只要不满足任何if或elif中的条件测试，其中的代码就会执行，这可能会引入无效甚至恶意的数据。如果知道最终要测试的条件，应考虑使用一个elif代码块来代替else代码块。这样，你就可以肯定，仅当满足相应的条件时，你的代码才会执行。

### 5.3.6 测试多个条件

* if-elif-else结构功能强大，但仅适合用于只有一个条件满足的情况。   
* 有时候必须检查你关心的所有条件。在这种情况下，应使用一系列不包含elif和else代码块的简单if语句。在可能有多个条件为True，且你需要在每个条件为True时都采取相应措施时，适合使用这种方法。


```python
requested_toppings = ['mushrooms', 'extra cheese']
if 'mushrooms' in requested_toppings:
    print("Adding mushrooms.")
if 'pepperoni' in requested_toppings:
    print("Adding pepperoni.")
if 'extra cheese' in requested_toppings:
    print("Adding extra cheese.")
print("\nFinished making your pizza!")
```

    Adding mushrooms.
    Adding extra cheese.
    
    Finished making your pizza!


每当这个程序运行时，都会进行这三个独立的测试。


```python
requested_toppings = ['mushrooms', 'extra cheese']
if 'mushrooms' in requested_toppings:
    print("Adding mushrooms.")
elif 'pepperoni' in requested_toppings:
    print("Adding pepperoni.")
elif 'extra cheese' in requested_toppings:
    print("Adding extra cheese.")
print("\nFinished making your pizza!")
```

    Adding mushrooms.
    
    Finished making your pizza!


第一个测试检查列表中是否包含'mushrooms'，它通过了，因此将在比萨中添加蘑菇。然而，Python将跳过if-elif-else结构中余下的测试，不再检查列表中是否包含'extra cheese'和'pepperoni'。其结果是，将添加顾客点的第一种配料，但不会添加其他的配料。

总之，如果你只想执行一个代码块，就使用if-elif-else结构；如果要运行多个代码块，就使用一系列独立的if语句。

### 动手试一试

### 5-3 外星人颜色#1：假设在游戏中刚射杀了一个外星人，请创建一个名为alien_color的变量，并将其设置为'green'、'yellow'或'red'。   
* 编写一条if语句，检查外星人是否是绿色的；如果是，就打印一条消息，指出玩家获得了5个点。   
* 编写这个程序的两个版本，在一个版本中上述测试通过了，而在另一个版本中未通过（未通过测试时没有输出）。


```python
alien_color = 'green'
if alien_color == 'green':
    print("You get five points!")
```

    You get five points!



```python
alien_color = 'red'
if alien_color != 'green':
    print("You get ten points!")
```

    You get ten points!


### 5-4 外星人颜色#2：像练习5-3那样设置外星人的颜色，并编写一个if-else结构。   
* 如果外星人是绿色的，就打印一条消息，指出玩家因射杀该外星人获得了5个点。   
* 如果外星人不是绿色的，就打印一条消息，指出玩家获得了10个点。    
* 编写这个程序的两个版本，在一个版本中执行if代码块，而在另一个版本中执行else代码块。


```python
alien_color = 'green'
if alien_color == 'green':
    print("You get five points!")
if alien_color != 'green':
    print("You get ten points!")
```

    You get five points!



```python
alien_color = 'red'
if alien_color == 'green':
    print("You get five points!")
else:
    print("You get ten points!")
```

    You get ten points!


### 5-5 外星人颜色#3：将练习5-4中的if-else结构改为if-elif-else结构。   
* 如果外星人是绿色的，就打印一条消息，指出玩家获得了5个点。   
* 如果外星人是黄色的，就打印一条消息，指出玩家获得了10个点。   
* 如果外星人是红色的，就打印一条消息，指出玩家获得了15个点。   
* 编写这个程序的三个版本，它们分别在外星人为绿色、黄色和红色时打印一条消息。


```python
alien_color = 'green'
if alien_color == 'green':
    score = 5
elif alien_color == 'red':
    score = 15
elif alien_cokor == 'yellow':
    score = 10
print("You get "+str(score)+" points!")
```

    You get 5 points!



```python
alien_color = 'red'
if alien_color == 'green':
    score = 5
elif alien_color == 'red':
    score = 15
else:
    score = 10
print("You get "+str(score)+" points!")
```

    You get 15 points!



```python
alien_color = 'yellow'
if alien_color == 'green':
    score = 5
if alien_color == 'red':
    score = 15
if alien_color == 'yellow':
    score = 10
print("You get "+str(score)+" points!")
```

    You get 10 points!


### 5-6 人生的不同阶段：设置变量age的值，再编写一个if-elif-else结构，根据age的值判断处于人生的哪个阶段。   
* 如果一个人的年龄小于2岁，就打印一条消息，指出他是婴儿。   
* 如果一个人的年龄为2（含）～4岁，就打印一条消息，指出他正蹒跚学步。   
* 如果一个人的年龄为4（含）～13岁，就打印一条消息，指出他是儿童。   
* 如果一个人的年龄为13（含）～20岁，就打印一条消息，指出他是青少年。   
* 如果一个人的年龄为20（含）～65岁，就打印一条消息，指出他是成年人。   
* 如果一个人的年龄超过65（含）岁，就打印一条消息，指出他是老年人。


```python
age = 21
if age < 2:
    id = 'a baby'
elif age < 4:
    id = 'a toddler'
elif age < 13:
    id = 'a child'
elif age < 20:
    id = 'a teenager'
elif age < 65:
    id = 'an adult'
else:
    id = 'the elderly'
print("He is "+id+".")
```

    He is an adult.


### 5-7 喜欢的水果：创建一个列表，其中包含你喜欢的水果，再编写一系列独立的if语句，检查列表中是否包含特定的水果。   
* 将该列表命名为favorite_fruits，并在其中包含三种水果。   
* 编写5条if语句，每条都检查某种水果是否包含在列表中，如果包含在列表中，就打印一条消息，如“You really like bananas!”。


```python
favorite_fruits = ['bananas', 'apples', 'grapes']
if 'bananas' in favorite_fruits:
    print("You really like bananas!")
if 'apples' in favorite_fruits:
    print("You really like apples!")
if 'grapes' in favorite_fruits:
    print("You really like grapes!")
if 'kiwi fruits' in favorite_fruits:
    print("You really like kiwi fruits!")
if 'pineapples' in favorite_fruits:
    print("You really like pineapples!")
```

    You really like bananas!
    You really like apples!
    You really like grapes!


## 5.4 使用if语句处理列表

通过结合使用if语句和列表，可完成一些有趣的任务：对列表中特定的值做特殊处理；高效地管理不断变化的情形，如餐馆是否还有特定的食材；证明代码在各种情形下都将按预期那样运行。

### 5.4.1 检查特殊元素


```python
requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']
for requested_topping in requested_toppings:
    print("Adding "+requested_topping+".")
print("\nFinished making your pizza!")
```

    Adding mushrooms.
    Adding green peppers.
    Adding extra cheese.
    
    Finished making your pizza!


如果比萨店的青椒用完了，该如何处理呢？为妥善地处理这种情况，可在for循环中包含一条if语句:


```python
requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']
for requested_topping in requested_toppings:
    if requested_topping == 'green peppers':
        print("Sorry, we are out of green peppers right now.")
    else:
        print("Adding "+requested_topping+".")
print("\nFinished making your pizza!")
```

    Adding mushrooms.
    Sorry, we are out of green peppers right now.
    Adding extra cheese.
    
    Finished making your pizza!


### 5.4.2 确定列表不是空的

我们马上就要让用户来提供存储在列表中的信息，因此不能再假设循环运行时列表不是空的。有鉴于此，在运行for循环前确定列表是否为空很重要。


```python
requested_toppings = []
if requested_toppings:  ##重点
    for requested_topping in requested_toppings:
        print("Adding "+requested_topping+".")
    print("\nFinished making your pizza!")
else:
    print("Are you sure you want a plain pizza?")
```

    Are you sure you want a plain pizza?


首先创建了一个空列表，其中不包含任何配料。我们进行了简单检查，而不是直接执行for循环。   
**在if语句中将列表名用在条件表达式中时，Python将在列表至少包含一个元素时返回True，并在列表为空时返回False。**   
如果requested_toppings不为空，就运行与前一个示例相同的for循环；否则，就打印一条消息，询问顾客是否确实要点不加任何配料的普通比萨

### 5.4.3 使用多个列表


```python
available_toppings = ['mushrooms', 'olives', 'green peppers', 'pepperoni', 'pineapple', 'extra cheese']
requested_toppings = ['mushrooms', 'french fries', 'extra cheese']
for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print("Adding "+requested_topping+".")
    else:
        print("Sorry, we don't have "+requested_topping+".")
print("\nFinished making your pizza!")
```

    Adding mushrooms.
    Sorry, we don't have french fries.
    Adding extra cheese.
    
    Finished making your pizza!


定义了一个列表，其中包含比萨店供应的配料。请注意，如果比萨店供应的配料是固定的，也可使用一个元组来存储它们。我们又创建了一个列表，其中包含顾客点的配料，请注意那个不同寻常的配料——'french fries'。我们遍历顾客点的配料列表。在这个循环中，对于顾客点的每种配料，我们都检查它是否包含在供应的配料列表中；如果答案是肯定的，就将其加入到比萨中，否则将运行else代码块：打印一条消息，告诉顾客不供应这种配料。

### 动手试一试

### 5-8 以特殊方式跟管理员打招呼：创建一个至少包含5个用户名的列表，且其中一个用户名为'admin'。想象你要编写代码，在每位用户登录网站后都打印一条问候消息。遍历用户名列表，并向每位用户打印一条问候消息。   
* 如果用户名为'admin'，就打印一条特殊的问候消息，如“Hello admin, would you like to see a status report?”。   
* 否则，打印一条普通的问候消息，如“Hello Eric, thank you for logging in again”。


```python
names = ['admin', 'Johnson', 'Kevin', 'Liliana', 'Helen']
for name in names:
    if name == 'admin':
        print("Hello admin, would you like to see a status report?")
    else:
        print("Hello "+name+", thank you for logging in again!")
```

    Hello admin, would you like to see a status report?
    Hello Johnson, thank you for logging in again!
    Hello Kevin, thank you for logging in again!
    Hello Liliana, thank you for logging in again!
    Hello Helen, thank you for logging in again!


### 5-9 处理没有用户的情形：在为完成练习5-8编写的程序中，添加一条if语句，检查用户名列表是否为空。   
* 如果为空，就打印消息“We need to find some users!”。   
* 删除列表中的所有用户名，确定将打印正确的消息。


```python
names = []
if names:
    for name in names:
        if name == 'admin':
            print("Hello admin, would you like to see a status report?")
        else:
            print("Hello "+name+", thank you for logging in again!")
else:
    print("We need to find some users!")
```

    We need to find some users!


### 5-10 检查用户名：按下面的说明编写一个程序，模拟网站确保每位用户的用户名都独一无二的方式。   
* 创建一个至少包含5个用户名的列表，并将其命名为current_users。   
* 再创建一个包含5个用户名的列表，将其命名为new_users，并确保其中有一两个用户名也包含在列表current_users中。   
* 遍历列表new_users，对于其中的每个用户名，都检查它是否已被使用。如果是这样，就打印一条消息，指出需要输入别的用户名；否则，打印一条消息，指出这个用户名未被使用。   
* 确保比较时不区分大小写；换句话说，如果用户名'John'已被使用，应拒绝用户名'JOHN'。


```python
current_users = ['Eric', 'Johnson', 'Kevin', 'Liliana', 'Helen']
new_users = ['KEVIN', 'Liliana', 'Rick', 'May', 'Leo']
for user in new_users:
    if user.lower() in [current_user.lower() for current_user in current_users]:
        print("Need to enter other names.")
    else:
        print("This user name is available!")
```

    Need to enter other names.
    Need to enter other names.
    This user name is available!
    This user name is available!
    This user name is available!


### 5-11 序数：序数表示位置，如1st和2nd。大多数序数都以th结尾，只有1、2和3例外。   
* 在一个列表中存储数字1～9。   
* 遍历这个列表。   
* 在循环中使用一个if-elif-else结构，以打印每个数字对应的序数。输出内容应为1st、2nd、3rd、4th、5th、6th、7th、8th和9th，但每个序数都独占一行。


```python
numbers = list(range(1,10))
for number in numbers:
    if number == 1:
        print(str(number)+"st")
    elif number == 2:
        print(str(number)+"nd")
    elif number == 3:
        print(str(number)+"rd")
    else:
        print(str(number)+"th")
```

    1st
    2nd
    3rd
    4th
    5th
    6th
    7th
    8th
    9th


## 5.5 设置if语句的格式

在条件测试的格式设置方面，PEP 8提供的唯一建议是，在诸如==、>=和<=等比较运算符**两边各添加一个空格**，例如，if age < 4:要比if age<4:好。

## 5.6 小结

1. 学习了如何编写结果要么为True要么为False的条件测试。   
2. 学习了如何编写简单的if语句、if-else语句和if-elif-else结构。在程序中，你使用了这些结构来测试特定的条件，以确定这些条件是否满足。   
3. 学习了如何在利用高效的for循环的同时，以不同于其他元素的方式对特定的列表元素进行处理。   
4. 再次学习了Python就代码格式方面提出的建议，这可确保即便你编写的程序越来越复杂，其代码依然易于阅读和理解。
