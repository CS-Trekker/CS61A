import sqlite3

db = sqlite3.connect("n.db")
# 建立一个 Python 和 SQLite 数据库文件的“连接”

db.execute("create table nums as select 2 as num union select 3;")
db.execute("create table dogs (name unique, age default 1);")


db.execute("insert into nums values (?), (?), (?);", range(4, 7))
db.execute("insert into dogs (name, age) values ('a', 2), ('b', 4);")

db.commit()  
# SQLite 在默认情况下会立刻把表结构（schema）写入数据库文件，即便没有 commit()
# INSERT / UPDATE / DELETE 这类数据修改，如果没有 commit()，数据就还停留在“事务缓存”里（内存里），别的连接（比如 VSCode 插件）看不到

# print(db.execute("select * from nums;"))
# <sqlite3.Cursor object at 0x000001352A0B6880>

print(db.execute("select * from nums;").fetchall())
# [(2,), (3,), (4,), (5,), (6,)]
# 元组

db.close()
# 释放 Python 程序和 SQLite 数据库之间建立的连接资源