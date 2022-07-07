* 本章中，你将学习如何接受用户输入，让程序能够对其进行处理。在程序需要一个名字时，你需要提示用户输入该名字；程序需要一个名单时，你需要提示用户输入一系列名字。为此，你需要使用**函数input( )**。      
* 你还将学习如何让程序不断地运行，让用户能够根据需要输入信息，并在程序中使用这些信息。为此，你需要使用**while循环**让程序不断地运行，直到指定的条件不满足为止。   
* 通过**获取用户输入**并学会**控制程序的运行时间**，可编写出**交互式程序**。

# 7.1 函数input( )的工作原理

**函数input( )**让程序暂停运行，等待用户输入一些文本。获取用户输入后，Python将其存储在一个变量中，以方便你使用。


```python
message = input("Tell me something, and I will repeat it back to you: ")
print(message)
```

    Tell me something, and I will repeat it back to you: Hello everyone!
    Hello everyone!


函数input( )接受一个参数：即要向用户显示的提示或说明，让用户知道该如何做。在这个示例中，Python运行第1行代码时，用户将看到提示Tell me something, and I will repeat it back to you:。程序等待用户输入，并在用户按回车键后继续运行。输入存储在变量message中，接下来的print(message)将输入呈现给用户。

## 7.1.1 编写清晰的程序

每当你使用函数input( )时，都应指定清晰而易于明白的**提示**，准确地指出你希望用户提供什么样的信息——指出用户该输入任何信息的提示都行，如下所示：


```python
name = input("Please enter your name: ")
print("Hello, "+name+"!")
```

    Please enter your name: Eric
    Hello, Eric!


通过在提示末尾（这里是冒号后面）包含一个空格，可将提示与用户输入分开，让用户清楚地知道其输入始于何处。

有时候，提示可能超过一行，例如，你可能需要指出获取特定输入的原因。在这种情况下，可将**提示存储在一个变量中**，再将该变量传递给函数input( )。这样，即便提示超过一行，input( )语句也非常清晰。


```python
prompt = "If you tell us who you are, we can personalize the messages you see."
prompt+= "\nWhat is your first name? "
name = input(prompt)
print("\nHello, "+name+"!")
```

    If you tell us who you are, we can personalize the messages you see.
    What is your first name? Eric
    
    Hello, Eric!


这个示例演示了一种创建多行字符串的方式。第1行将消息的前半部分存储在变量prompt中；在第2行中，运算符+=在存储在prompt中的字符串末尾附加一个字符串。最终的提示横跨两行，并在问号后面包含一个空格，这也是出于清晰考虑。

## 7.1.2 使用int( )来获取数值输入

使用函数input( )时，Python将用户输入解读为字符串。


```python
age = input("How old are you? ")
age
```

    How old are you? 21





    '21'



用户输入的是数字21，但我们请求Python提供变量age的值时，它返回的是'21'——用户输入的数值的字符串表示。


```python
age = input("How old are you? ")
age >= 18
```

    How old are you? 21



    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    <ipython-input-6-677716768126> in <module>
          1 age = input("How old are you? ")
    ----> 2 age >= 18
    

    TypeError: '>=' not supported between instances of 'str' and 'int'


你试图将输入用于数值比较时，Python会引发错误，因为它无法将字符串和整数进行比较：不能将存储在age中的字符串'21'与数值18进行比较。

为解决这个问题，可使用**函数int( )**，它让Python将输入视为数值。*函数int( )将数字的字符串表示转换为数值表示*，如下所示：


```python
age = input("How old are you? ")
age = int(age)
age >= 18
```

    How old are you? 21





    True



在这个示例中，我们在提示时输入21后，Python将这个数字解读为字符串，但随后int( )将这个字符串转换成了数值表示。这样Python就能运行条件测试了：将变量age（它现在包含数值21）同18进行比较，看它是否大于或等于18。测试结果为True。


```python
height = input("How tall are you, in inches? ")
height = int(height)
if height >= 36:
    print("\nYou're tall enough to ride!")
else:
    print("\nYou'll be able to ride when you're a little older.")
```

    How tall are you, in inches? 71
    
    You're tall enough to ride!


将数值输入用于计算和比较前，务必将其转换为数值表示。

## 7.1.3 求模运算符

处理数值信息时，**求模运算符（%）**是一个很有用的工具，它**将两个数相除并返回余数**：


```python
7%3
```




    1



如果一个数可被另一个数整除，余数就为0，因此求模运算符将返回0。你可利用这一点来判断一个数是奇数还是偶数：


```python
number = input("Enter a number, and I'll tell you if it's even or odd: ")
number = int(number)
if number % 2 == 0:
    print("\nThe number "+str(number)+" is even.")
else:
    print("\nThe number "+str(number)+" is odd.")
```

    Enter a number, and I'll tell you if it's even or odd: 42
    
    The number 42 is even.


## 7.1.4 在Python 2.7中获取输入

如果你使用的是Python 2.7，应使用**函数raw_input( )**来提示用户输入。这个函数与Python 3中的input( )一样，也将输入解读为字符串。

## 动手试一试

### 7-1 汽车租赁：   
编写一个程序，询问用户要租赁什么样的汽车，并打印一条消息，如“Let me see if I can find you a Subaru”。


```python
prompt = "What kind of car do you want to borrow? "
car = input(prompt)
print("Let me see if I can find you a "+car.title()+".")
```

    What kind of car do you want to borrow? subaru
    Let me see if I can find you a Subaru.


### 7-2 餐馆订位：   
编写一个程序，询问用户有多少人用餐。如果超过8人，就打印一条消息，指出没有空桌；否则指出有空桌。


```python
prompt = "How many people will join this meal?"
prompt += "\nNumber: "
num = input(prompt)
num = int(num)
if num > 8:
    print("I am so sorry, there is no table available.")
else:
    print("There is a table available, please follow me!")
```

    How many people will join this meal?
    Number: 10
    I am so sorry, there is no table available.


### 7-3 10的整数倍：   
让用户输入一个数字，并指出这个数字是否是10的整数倍。


```python
number = input("Please enter a number, I'll tell you whether it is a multiples of ten: ")
number = int(number)
if number % 10 == 0:
    print("It certainly is a multiple of 10!")
else:
    print("This is not a multiple of 10, please try to think of another one please.")
```

    Please enter a number, I'll tell you whether it is a multiples of ten: 89
    This is not a multiple of 10, please try to think of another one please.


# 7.2 while循环简介

**for循环**用于针对**集合中的每个元素**的一个代码块，而**while循环不断地运行，直到指定的条件不满足为止**。

## 7.2.1 使用while循环


```python
current_number = 1
while current_number <= 5:
    print(current_number)
    current_number+= 1
```

    1
    2
    3
    4
    5


## 7.2.2 让用户选择何时退出


```python
prompt = "\nTell me something, and I will repeat it back to you:"
prompt+= "\nEnter 'quit' to end the program. "
message = ""
while message != 'quit':
    message = input(prompt)
    print(message)
```

    
    Tell me something, and I will repeat it back to you:
    Enter 'quit' to end the program. Hello everyone!
    Hello everyone!
    
    Tell me something, and I will repeat it back to you:
    Enter 'quit' to end the program. Hello again.
    Hello again.
    
    Tell me something, and I will repeat it back to you:
    Enter 'quit' to end the program. quit
    quit


我们定义了一条提示消息，告诉用户他有两个选择：要么输入一条消息，要么输入退出值（这里为'quit'）。接下来，我们创建了一个变量——message，用于存储用户输入的值。我们将变量message的初始值设置为空字符串""，让Python首次执行while代码行时有可供检查的东西。Python首次执行while语句时，需要将message的值与'quit'进行比较，但此时用户还没有输入。如果没有可供比较的东西，Python将无法继续运行程序。为解决这个问题，我们必须给变量message指定一个初始值。虽然这个初始值只是一个空字符串，但符合要求，让Python能够执行while循环所需的比较。**只要message的值不是'quit'，这个循环就会不断运行**。

首次遇到这个循环时，message是一个空字符串，因此Python进入这个循环。执行到代码行`message = input(prompt)`时，Python显示提示消息，并等待用户输入。不管用户输入是什么，都将存储到变量message中并打印出来；接下来，Python重新检查while语句中的条件。只要用户输入的不是单词'quit'，Python就会再次显示提示消息并等待用户输入。等到用户终于输入'quit'后，Python停止执行while循环，而整个程序也到此结束。

这个程序很好，唯一美中不足的是，它将单词'quit'也作为一条消息打印了出来。为修复这种问题，只需使用一个简单的if测试：


```python
prompt = "\nTell me something, and I will repeat it back to you:"
prompt+= "\nEnter 'quit' to end the program."
message = ""
while message != 'quit':
    message = input(prompt)
    if message != 'quit':
        print(message)
```

    
    Tell me something, and I will repeat it back to you:
    Enter 'quit' to end the program.Hello everyone!
    Hello everyone!
    
    Tell me something, and I will repeat it back to you:
    Enter 'quit' to end the program.Hello again.
    Hello again.
    
    Tell me something, and I will repeat it back to you:
    Enter 'quit' to end the program.quit


现在，程序在显示消息前将做简单的检查，仅在消息不是退出值时才打印它。

## 7.2.3 使用标志

在前一个示例中，我们让程序在满足指定条件时就执行特定的任务。在更复杂的程序中，很多不同的事件都会导致程序停止运行；在这种情况下，该怎么办呢？    
例如，在游戏中，多种事件都可能导致游戏结束，如玩家一艘飞船都没有了或要保护的城市都被摧毁了。导致程序结束的事件有很多时，如果在一条while语句中检查所有这些条件，将既复杂又困难。    

在要求很多条件都满足才继续运行的程序中，可**定义一个变量，用于判断整个程序是否处于活动状态**。这个变量被称为**标志**，充当了程序的交通信号灯。你可让**程序在标志为True时继续运行，并在任何事件导致标志的值为False时让程序停止运行**。这样，在while语句中就只需检查一个条件——标志的当前值是否为True，并将所有测试（是否发生了应将标志设置为False的事件）都放在其他地方，从而让程序变得更为整洁。


```python
prompt = "\nTell me something, and I will repeat it back to you:"
prompt+= "\nEnter 'quit' to end the program. "
active = True
while active:
    message = input(prompt)
    if message == 'quit':
        active = False
    else:
        print(message)
```

    
    Tell me something, and I will repeat it back to you:
    Enter 'quit' to end the program. Hello.
    Hello.
    
    Tell me something, and I will repeat it back to you:
    Enter 'quit' to end the program. quit


* 我们将变量active设置成了True，让程序最初处于活动状态。这样做简化了while语句，因为不需要在其中做任何比较——相关的逻辑由程序的其他部分处理。只要变量active为True，循环就将继续运行。   
* 在while循环中，我们在用户输入后使用一条if语句来检查变量message的值。如果用户输入的是'quit'，我们就将变量active设置为False，这将导致while循环不再继续执行。如果用户输入的不是'quit'，我们就将输入作为一条消息打印出来。   
* 这个程序的输出与前一个示例相同。在前一个示例中，我们**将条件测试直接放在了while语句中**，而在这个程序中，我们使用了一个标志来指出程序是否处于活动状态，这样如果要添加测试（如elif语句）以检查是否发生了其他导致active变为False的事件，将很容易。在复杂的程序中，如很多事件都会导致程序停止运行的游戏中，标志很有用：在其中的任何一个事件导致活动标志变成False时，主游戏循环将退出，此时可显示一条游戏结束消息，并让用户选择是否要重新玩。

## 7.2.4 使用break退出循环

要**立即退出while循环，不再运行循环中余下的代码**，也不管条件测试的结果如何，**可使用break语句**。break语句用于控制程序流程，可使用它来控制哪些代码行将执行，哪些代码行不执行，从而让程序按你的要求执行你要执行的代码。


```python
prompt = "\nPlease enter the name of a city you have visited:"
prompt+= "\n(Enter 'quit' when you are finished.)"
while True:
    city = input(prompt)
    if city == 'quit':
        break
    else:
        print("I'd love to go to "+city.title()+"!")
```

    
    Please enter the name of a city you have visited:
    (Enter 'quit' when you are finished.)San Francisco
    I'd love to go to San Francisco!
    
    Please enter the name of a city you have visited:
    (Enter 'quit' when you are finished.)quit


***注意***：   
在任何Python循环中都可使用break语句。例如，可使用break语句来退出遍历列表或字典的for循环。

## 7.2.5 在循环中使用continue

要**返回到循环开头**，并根据条件测试结果决定是否继续执行循环，可使用continue语句，它不像break语句那样不再执行余下的代码并退出整个循环。


```python
current_number = 0
while current_number < 10:
    current_number+= 1
    if current_number % 2 == 0:
        continue
    print(current_number)
```

    1
    3
    5
    7
    9


我们首先将current_number设置成了0，由于它小于10，Python进入while循环。进入循环后，我们以步长1的方式往上数，因此current_number为1。接下来，if语句检查current_number与2的求模运算结果。如果结果为0（意味着current_number可被2整除），就执行continue语句，让Python忽略余下的代码，并返回到循环的开头。**如果当前的数字不能被2整除，就执行循环中余下的代码，Python将这个数字打印出来**。

## 7.2.6 避免无限循环

每个while循环都必须有停止运行的途径，这样才不会没完没了地执行下去。


```python
x = 1
while x <= 5:
    print(x)
    x+= 1
```

    1
    2
    3
    4
    5


但如果你像下面这样不小心遗漏了代码行x+= 1，这个循环将没完没了地运行：    
```
# 这个循环将没完没了地运行
x = 1
while x <= 5:
print(x)
```

在这里，x的初始值为1，但根本不会变，因此条件测试x <= 5始终为True，导致while循环没完没了地打印1。

每个程序员都会偶尔因不小心而编写出无限循环，在循环的退出条件比较微妙时尤其如此。如果程序陷入无限循环，可按**Ctrl+C**，也可关闭显示程序输出的终端窗口。

要避免编写无限循环，务必对每个while循环进行测试，确保它按预期那样结束。如果你希望程序在用户输入特定值时结束，可运行程序并输入这样的值；如果在这种情况下程序没有结束，请检查程序处理这个值的方式，确认程序至少有一个这样的地方能让循环条件为False或让break语句得以执行。

## 动手试一试

### 7-4 比萨配料：    
编写一个循环，提示用户输入一系列的比萨配料，并在用户输入'quit'时结束循环。每当用户输入一种配料后，都打印一条消息，说我们会在比萨中添加这种配料。


```python
prompt = "\nPlease enter the topping you want to add: "
prompt+= "\n(Enter 'quit' when you are finished.)"
active = True
while active:
    topping = input(prompt)
    if topping == "quit":
        break
    print("We will add "+topping.title()+" to your pizza!")
```

    
    Please enter the topping you want to add: 
    (Enter 'quit' when you are finished.)mushroom
    We will add Mushroom to your pizza!
    
    Please enter the topping you want to add: 
    (Enter 'quit' when you are finished.)pepperoni
    We will add Pepperoni to your pizza!
    
    Please enter the topping you want to add: 
    (Enter 'quit' when you are finished.)quit


### 7-5 电影票：   
有家电影院根据观众的年龄收取不同的票价：不到3岁的观众免费；3～12岁的观众为10美元；超过12岁的观众为15美元。请编写一个循环，在其中询问用户的年龄，并指出其票价。


```python
prompt = "\nCan you tell me how old are you?"
prompt+= "\n(Enter 'quit' if you are finished.): "
while True:
    age = input(prompt)
    if age == 'quit':
        break
    else:
        age = int(age)
        if age < 3:
            print("Your movie ticket is free!")
        elif age <= 12:
            print("You need to pay $10 for this ticket.")
        else:
            print("You need to pay $15 for this ticket.")
```

    
    Can you tell me how old are you?
    (Enter 'quit' if you are finished.): 2
    Your movie ticket is free!
    
    Can you tell me how old are you?
    (Enter 'quit' if you are finished.): 6
    You need to pay $10 for this ticket.
    
    Can you tell me how old are you?
    (Enter 'quit' if you are finished.): 21
    You need to pay $15 for this ticket.
    
    Can you tell me how old are you?
    (Enter 'quit' if you are finished.): quit


### 7-6 三个出口：    
以另一种方式完成练习7-4或练习7-5，在程序中采取如下所有做法。   
* 在while循环中使用条件测试来结束循环。   
* 使用变量active来控制循环结束的时机。   
* 使用break语句在用户输入'quit'时退出循环。


```python
prompt = "\nCan you tell me how old are you?"
prompt+= "\n(Enter 'quit' if you are finished.): "
active = True
while active:
    age = input(prompt)
    if age == 'quit':
        active = False
        print("Thank you for using.")
        break
    if age.isdigit():
        age = int(age)
        if age < 3:
            print("Your movie ticket is free!")
        elif age <= 12:
            print("You need to pay $10 for this ticket.")
        elif age >12:
            print("You need to pay $15 for this ticket.")
    else:
            print("You are not entering numbers, check your input and try again.")
            
#使用isdigit()检测字符串是否只由数字组成。
```

    
    Can you tell me how old are you?
    (Enter 'quit' if you are finished.): xx
    You are not entering numbers, check your input and try again.
    
    Can you tell me how old are you?
    (Enter 'quit' if you are finished.): 2
    Your movie ticket is free!
    
    Can you tell me how old are you?
    (Enter 'quit' if you are finished.): 21
    You need to pay $15 for this ticket.
    
    Can you tell me how old are you?
    (Enter 'quit' if you are finished.): quit
    Thank you for using.


### 7-7 无限循环：   
编写一个没完没了的循环，并运行它（要结束该循环，可按Ctrl+C，也可关闭显示输出的窗口）。

```
while True:
    print("I love Python")
```

# 7.3 使用while循环来处理列表和字典

到目前为止，我们每次都只处理了一项用户信息：获取用户的输入，再将输入打印出来或作出应答；循环再次运行时，我们获悉另一个输入值并作出响应。然而，要记录大量的用户和信息，需要在while循环中使用列表和字典。

for循环是一种遍历列表的有效方式，但在**for循环中不应修改列表**，否则将导致Python难以跟踪其中的元素。要**在遍历列表的同时对其进行修改，可使用while循环**。通过将while循环**同列表和字典结合起来使用**，可收集、存储并组织大量输入，供以后查看和显示。

## 7.3.1 在列表之间移动元素

假设有一个列表，其中包含新注册但还未验证的网站用户；验证这些用户后，如何将他们移到另一个已验证用户列表中呢？一种办法是使用一个while循环，在验证用户的同时将其从未验证用户列表中提取出来，再将其加入到另一个已验证用户列表中。代码可能类似于下面这样：


```python
# 首先，创建一个待验证用户列表
# 和一个用于存储已验证用户的空列表
unconfirmed_users = ['alice', 'brian', 'candace']
confirmed_users = []
# 验证每个用户，直到没有未验证用户为止
# 将每个经过验证的列表都移到已验证用户列表中
while unconfirmed_users:
    current_user = unconfirmed_users.pop()
    print("Verifying user: "+current_user.title())
    confirmed_users.append(current_user)
# 显示所有已验证的用户
print("\nThe following users have been confirmed:")
for confirmed_user in confirmed_users:
    print(confirmed_user.title())
```

    Verifying user: Candace
    Verifying user: Brian
    Verifying user: Alice
    
    The following users have been confirmed:
    Candace
    Brian
    Alice


我们首先创建了一个未验证用户列表，其中包含用户Alice、Brian和Candace，还创建了一个空列表，用于存储已验证的用户。代码的第7行，while循环将不断地运行，直到列表unconfirmed_users变成空的。在这个循环中，**函数pop( )以每次一个的方式从列表unconfirmed_users末尾删除未验证的用户**。由于Candace位于列表unconfirmed_users末尾，因此其名字将首先被删除、存储到变量current_user中并加入到列表confirmed_users中。接下来是Brian，然后是Alice。

为模拟用户验证过程，我们打印一条验证消息并将用户加入到已验证用户列表中。未验证用户列表越来越短，而已验证用户列表越来越长。**未验证用户列表为空后结束循环**，再打印已验证用户列表。

## 7.3.2 删除包含特定值的所有列表元素

在第3章中，我们使用**函数remove( )**来删除列表中的特定值，这之所以可行，是因为要删除的值在列表中只出现了一次。如果要删除列表中所有包含特定值的元素，该怎么办呢？


```python
pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
print(pets)
while 'cat' in pets:
    pets.remove('cat')
print(pets)
```

    ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
    ['dog', 'dog', 'goldfish', 'rabbit']


我们首先创建了一个列表，其中包含多个值为'cat'的元素。打印这个列表后，Python进入while循环，因为它发现'cat'在列表中至少出现了一次。进入这个循环后，Python**删除第一个'cat'并返回到while代码行**，然后发现'cat'还包含在列表中，因此**再次进入循环**。它不断删除'cat'，直到这个值不再包含在列表中，然后退出循环并再次打印列表。

## 7.3.3 使用用户输入来填充字典

可使用while循环提示用户输入任意数量的信息。下面来创建一个调查程序，其中的循环每次执行时都提示输入被调查者的名字和回答。我们将收集的数据存储在一个字典中，以便将回答同被调查者关联起来：


```python
responses = {}
# 设置一个标志，指出调查是否继续
polling_active = True
while polling_active:
    # 提示输入被调查者的名字和回答
    name = input("\nWhat is your name? ")
    response = input("Which mountain would you like to climb someday? ")
    # 将答案存储在字典中
    responses[name] = response
    # 看看是否还有人要参与调查
    repeat = input("Would you like to let another person respond? (yes/ no) ")
    if repeat == 'no':
        polling_active = False
# 调查结束，显示结构
print("\n--- Poll Results ---")
for name, response in responses.items():
    print(name+" would like to climb "+response+".")
```

    
    What is your name? Eric
    Which mountain would you like to climb someday? Denali
    Would you like to let another person respond? (yes/ no) yes
    
    What is your name? Lynn
    Which mountain would you like to climb someday? Devil's Thumb
    Would you like to let another person respond? (yes/ no) no
    
    --- Poll Results ---
    Eric would like to climb Denali.
    Lynn would like to climb Devil's Thumb.


这个程序首先定义了一个空字典（responses），并设置了一个标志（polling_active），用于指出调查是否继续。只要polling_active为True，Python就运行while循环中的代码。

在这个循环中，提示用户输入其用户名及其喜欢爬哪座山。将这些信息存储在字典responses中，然后询问用户调查是否继续。如果用户输入yes，程序将再次进入while循环；如果用户输入no，标志polling_active将被设置为False，而while循环将就此结束。最后一个代码块显示调查结果。

***注意***:   
`responses[name] = response`的responses是开头定义的空字典，[name]是字典的键(keys)，右边response是对应这个键的值。通过while循环的input来创建新的键值对。也就是说，把用户输入的response存为这个用户name（name相当于key）的value。

## 动手试一试

### 7-8 熟食店：    
创建一个名为sandwich_orders的列表，在其中包含各种三明治的名字；再创建一个名为finished_sandwiches的空列表。遍历列表sandwich_orders，对于其中的每种三明治，都打印一条消息，如I made your tuna sandwich，并将其移到列表finished_sandwiches。所有三明治都制作好后，打印一条消息，将这些三明治列出来。


```python
sandwich_orders = ['open sandwich', 'submarine sandwich', 'pinwheel sandwich', 'club sandwich']
finished_sandwiches = []
while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    print("I made your "+current_sandwich+".")
    finished_sandwiches.append(current_sandwich)
print("\nThe following sandwiches are completed:")
for finished_sandwich in finished_sandwiches:
    print(finished_sandwich.title())
```

    I made your club sandwich.
    I made your pinwheel sandwich.
    I made your submarine sandwich.
    I made your open sandwich.
    
    The following sandwiches are completed:
    Club Sandwich
    Pinwheel Sandwich
    Submarine Sandwich
    Open Sandwich


### 7-9 五香烟熏牛肉（pastrami）卖完了：   
使用为完成练习7-8而创建的列表sandwich_orders，并确保'pastrami'在其中至少出现了三次。在程序开头附近添加这样的代码：打印一条消息，指出熟食店的五香烟熏牛肉卖完了；再使用一个while循环将列表sandwich_orders中的'pastrami'都删除。确认最终的列表finished_sandwiches中不包含'pastrami'。


```python
sandwich_orders = ['pastrami', 'pastrami', 'submarine sandwich', 'pinwheel sandwich', 'club sandwich', 'pastrami']
finished_sandwiches = []
print("Pastrami has sold out at our restaurant, sorry~")
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')
while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    finished_sandwiches.append(current_sandwich)
print("\nThe following sandwiches are completed:")
for finished_sandwich in finished_sandwiches:
    print(finished_sandwich.title())
```

    Pastrami has sold out at our restaurant, sorry~
    
    The following sandwiches are completed:
    Club Sandwich
    Pinwheel Sandwich
    Submarine Sandwich


### 7-10 梦想的度假胜地：    
编写一个程序，调查用户梦想的度假胜地。使用类似于“If you could visit one place in the world, where would you go?”的提示，并编写一个打印调查结果的代码块。


```python
responses = {}
polling_active = True
while polling_active:
    name = input("\nWhat is your name? ")
    response = input("If you could visit one place in the world, where would you go? ")
    responses[name] = response
    repeat = input("Would you like to let another person respond? (yes/ no) ")
    if repeat == 'no':
        polling_active = False
print("\n--- Poll Results ---")
for name, response in responses.items():
    print(name.title()+" would like to visit "+response+".")
```

    
    What is your name? kevin
    If you could visit one place in the world, where would you go? sydney
    Would you like to let another person respond? (yes/ no) yes
    
    What is your name? liliana
    If you could visit one place in the world, where would you go? london
    Would you like to let another person respond? (yes/ no) no
    
    --- Poll Results ---
    Kevin would like to visit sydney.
    Liliana would like to visit london.


# 7.4 小结

本章中，你学习了：   
1. 如何在程序中使用input( )来让用户提供信息；   
2. 如何处理文本和数字输入，以及如何使用while循环让程序按用户的要求不断地运行；   
3. 多种控制while循环流程的方式：设置活动标志、使用break语句以及使用continue语句；   
4. 如何使用while循环在列表之间移动元素，以及如何从列表中删除所有包含特定值的元素；   
5. 如何结合使用while循环和字典。
