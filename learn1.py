# python基础
import random

# name = '张三'
# age = 20
# word = "I'm your friend"
# ''' 分段注释 '''
# print("name: %s,age: %d,word: %s" % (name, age, word))

# 生成指定范围的随机整数
# rd = random.randrange(0, 100)
# rd1 = random.random()
# print(rd1)
# if rd <= age:
#     print("little: %d" % rd)
# else:
#     print("big: %d" % rd)
# 集合 及其填充
lists = []
for c in range(10):
    lists.append(random.randrange(0, 100))


# 打印list的函数
def list_print(data_list):
    if data_list is None:
        return ""
    s = "{0}, "
    st = ''
    for j in data_list:
        item = data_list.__getitem__(data_list.__len__() - 1)
        if j == item:
            s = "{0}"
        s_format = s.format(j.__str__())
        st += s_format
    return "[%s]" % st


class Temp(object):
    # 类似于构造方法，可以初始化成员变量
    def __init__(self, name='', age=0):
        self.name = name
        self.age = age

    # 类似于toString()方法
    def __str__(self) -> str:
        return self.name


ss = []

for k in range(3):
    ss.append(Temp("张三%d" % k, k + 10))
print("result: %s" % list_print(ss))


# print("test: %s" % ss.__str__())


# 集合遍历
# for i in lists:
#     if i <= 50:
#         print(i)
#         lists.pop(lists.index(i))
#
# print(lists.__str__())
# print("len: %s" % lists.__str__())

# 用for循环倒序遍历
def list_del2(data_list):
    print("del before: %s" % data_list.__str__())
    for i in range(len(data_list) - 1, -1, -1):
        if data_list[i] < 50:
            data_list.pop(i)
    print("for del result: %s" % data_list)


# 遍历删除列表里的值
def list_del(data_list):
    if data_list is None:
        return
    print("del before: %s" % data_list.__str__())
    n = 0
    while n < data_list.__len__():
        if data_list.__getitem__(n) < 50:
            data_list.pop(n)
            n -= 1
        n += 1
    print("del result: %s" % data_list.__str__())


list_del2(lists)
