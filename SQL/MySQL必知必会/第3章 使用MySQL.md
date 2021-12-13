[TOC]



# 3.1 连接

MySQL在内部保存自己的用户列表，并且把每个用户与各种权限关联起来。

为了连接到MySQL，需要以下信息：
❑ 主机名（计算机名）——如果连接到本地MySQL服务器，为localhost；
❑ 端口（如果使用默认端口3306之外的端口）；
❑ 一个合法的用户名；
❑ 用户口令（如果需要）。

# 3.2 选择数据库

在能执行任意数据库操作前，需要选择一个数据库。为此，可使用**USE关键字**。

关键字(key word) ：作为MySQL语言组成部分的一个保留字。决不要用关键字命名一个表或列。

`USE crashcourse;`  USE语句并不返回任何结果。依赖于使用的客户机，显示某种形式的通知。例如，这里显示出的**Database changed**消息是mysql命令行实用程序在数据库选择成功后显示的。

记住，**必须先使用USE打开数据库，才能读取其中的数据。**

# 3.3 了解数据库和表

数据库、表、列、用户、权限等的信息被存储在数据库和表中（MySQL使用MySQL来存储这些信息）。不过，内部的表一般不直接访问。可用MySQL的**SHOW命令**来显示这些信息（MySQL从内部表中提取这些信息）。

`SHOW DATABASES;`  返回可用数据库的一个列表。包含在这个列表中的可能是MySQL内部使用的数据库。

`SHOW TABLES;`  返回当前选择的数据库内可用表的列表。

`SHOW COLUMNS FROM 表名;`  显示表列

每个字段返回一行，行中包含字段名Field、数据类型Type、是否允许NULL、键信息Key、默认值Default以及其他信息Extra（如字段cust_id的auto_increment）。

***字段*(field)**，一个成员，它表示与对象或类关联的变量。 在数据库中，大多数时，表的“列”称为“*字段*” ，每个*字段*包含某一专题的信息。



**自动增量：** 在每个行添加到表中时，MySQL可以自动地为每个行分配下一个可用编号，不用在添加一行时手动分配唯一值。如果需要它，则必须在用CREATE语句创建表时把它作为表定义的组成部分。（第21章）



**DESCRIBE语句：** MySQL支持用DESCRIBE作为SHOW COLUMNS FROM的一种快捷方式。换句话说，`DESCRIBE customers；`是`SHOW COLUMNS FROM customers；`的一种快捷方式。



所支持的其他SHOW语句还有：
❑ SHOW STATUS，用于显示广泛的服务器状态信息；
❑ SHOW CREATE DATABASE和SHOW CREATE TABLE，分别用来显示创建特定数据库或表的MySQL语句；
❑ SHOW GRANTS，用来显示授予用户（所有用户或特定用户）的安全权限；
❑ SHOW ERRORS和SHOW WARNINGS，用来显示服务器错误或警告消息。



SHOW请在mysql命令行实用程序中，执行命令`HELP SHOW；`显示允许的SHOW语句。

