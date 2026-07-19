"""
定义Hashmap
dict_name = {key1: value1, key2: value2...}

key如果重复，输出时后面的值会覆盖前面的值
内存中就像linked list般运行由1指向2，最终指向最后一个值

key不能使用List, sets, dict作为data type，因为它们其中的数据类型可变，而key需要不可变类型

value修改
dict_name[key] = new_value

key-value pair添加
dict_name[new_key] = value

删除键值对可以用pop也可以用del
variable = dict_name.pop(key) (只能pop value)
del dict_name[key]

五种查询方法

根据key获取value
variable = dict_name[key] (value)
dict_name.get(key)

获取所有key / value / key-value pair
dict_name.keys()
dict_name.values()
dict_name.items()
这些会封装至独特的字典数据容器中，可用于遍历for 循环
for i in dict_nam.keys
i就会遍历每一个keys
item会封装至元组后再封装至独特的字典数据容器，遍历时会遍历出元组数据类型
"""
