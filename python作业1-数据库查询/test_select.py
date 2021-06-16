from select_function import *

# 数据库配置及查询表名
my_config = {"host": "localhost", "port": 3306, "user": "root", "pw": "gongwf", "db": "python", "charset": "utf8",
             "table": ["user", "money"]}
# 需要查询的列名
my_field = ("id", "name")
my_condition = 'user.id=1 and money.name = 1'

conn, connected, sql = select(*my_field, condition_str=my_condition, **my_config)
# SELECT id,name FROM user,money WHERE user.id=1 and money.name = 1
print(sql)
# True
print(connected)
