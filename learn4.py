import math
import pickle
import sys

import learn1
import base_lib.actual1

list1 = [2, 4, 6, 8, 10]
list2 = [2 * i for i in list1 if i is not 4]
print("1: ", list1)  # 1:  [2, 4, 6, 8, 10]
print("2: ", list2)  # 2:  [4, 8, 12, 16, 20]
print([i * j for i in list1 for j in list2])

list3 = [str(round(355 / 113, i)) for i in range(1, 60)]
print(list3)

m = [[-1, -2, 1], [10, 20, 30], [2, 4, 5, 7]]
# [[-1, 10, 2], [-2, 20, 4], [1, 30, 5]]
print([[row[i] for row in m] for i in range(3)])

d = {"name": "张三", "age": "12"}
d_ = [str("姓名：%s, 年龄：%s" % (key, age)) for key in d for age in d[key]]
print(d_)

# 关于字典的遍历
for i in d.items():
    # 同时取到键和值
    print("item: ", i[0], i[1])

# 列表遍历，同时取到索引和值
for i, v in enumerate(['tic', 'tac', 'toe']):
    print("index: %s, value: %s" % (i, v))

# 同时遍历两个列表
questions = ['name', 'quest', 'favorite color']
answers = ['lancelot', 'the holy grail', 'blue']
for q, a in zip(questions, answers):
    print('What is your {0}?  It is {1}.'.format(q, a))

# 反向遍历
for i in reversed(range(10)):
    print(i)

# 排序遍历
for i in sorted(iter(list1), key=lambda j: j / 2, reverse=True):
    print("i = ", i)
    pass
print(list1)

# 等同于clear，del语句有切割列表，元组，集合，字典的作用
del d["age"]
print(d)
del d_[:]
print(d_)

print(learn1)
print(sys.path)

print(dir(learn1))

print("test = ", base_lib.actual1.test(12, 3))

print(repr(list1))


# for x in range(1, 11):
#     print(repr(x).rjust(2), repr(x * x).rjust(3), end=' ')
#     # 注意前一行 'end' 的使用
#     print(repr(x * x * x).rjust(4))

# for x in range(1, 25):
#     # 0，1，2为占位符，2d 3d 5d 代表整数的位数
#     print('{0:2d} {1:3d} {2:5d}'.format(x, x * x, x * x * x))


# def triangles():
#     list4 = [1]
#     while True:
#         yield list4
#         list4 = [sum(i) for i in zip([0] + list4, list4 + [0])]
#         print(list4)

# 打印金字塔型的杨辉三角
def triangles(n):
    pass
    c = 0
    ret = []
    pre = []  # 存前序列表
    while True:
        c += 1
        ret.append(1)
        for i in range(1, len(ret) - 1):
            ret[i] = pre[i - 1] + pre[i]
        # 不能用pre = ret(此方法不创建新对象，只是让pre指向ret所指向的那片存储空间)
        pre = list(ret)
        s = ""
        for i in ret:
            # 遍历每一行，输出占5位的字符串
            s = s + ("{0:%dd}" % (n - 3)).format(i)
        # 输出时以100为宽居中
        print(s.center(n * 10))
        if c >= n:
            break


# triangles(13)

print("name: {}, age: {}".format("张三", 12))
print("name: {0}, age: {1:f}".format("张三", 12))  # name: 张三, age: 12.000000
# 如果在 format() 中使用了关键字参数, 那么它们的值会指向使用该名字的参数
# 位置及关键字参数可以任意的结合
print("n: {name}, a: {age}".format(name="John", age=13))  # n: John, a: 13
# '!a' (使用 ascii()),
# '!s' (使用 str())
# '!r' (使用 repr()) 可以用于在格式化某个值之前对其进行转化
print("pi: {!a}".format(math.pi))  # pi: 3.141592653589793
# 可选项 ':' 和格式标识符可以跟着字段名
print("pi: {0:.3f}".format(math.pi))  # pi: 3.142
# 在 ':' 后传入一个整数, 可以保证该域至少有这么多的宽度
print("pi: {0:3f}".format(math.pi))  # pi: 3.141593
print("test: {0:10d}".format(1000) + ", 123")  # test:       1000, 123
# 如果你有一个很长的格式化字符串, 而你不想将它们分开, 那么在格式化时通过变量名而非位置会是很好的事情。
# 最简单的就是传入一个字典, 然后使用方括号 '[]' 来访问键值 :
table = {'Google': 1, 'Run': 2}
print('Run: {0[Run]:d}; Google: {0[Google]:d}'.format(table))
# 用**
print('Run: {Run:d}; Google: {Google:d}'.format(**table))
# % 操作符也可以实现字符串格式化。
# 它将左边的参数作为类似 sprintf() 式的格式化字符串, 而将右边的代入, 然后返回格式化后的字符串
# 常量 PI 的值近似为：     3.142。, mm
print('常量 PI 的值近似为：%10.3f。' % math.pi + ", mm")
# 文件操作
# r,只读，rb,以二进制打开文件，指针在文件开头，r+,打开一个文件用于读写，rb+,
# w,只写，wb,w+,wb+ 从开头开始编辑，即原有内容会被删除。如果该文件不存在，创建新文件。
# a,打开一个文件用于追加。如果该文件已存在,新的内容将会被写入到已有内容之后。
# 如果该文件不存在,创建新文件进行写入。ab,a+,ab+,带+的代表读写
f = open("res/temp.txt", "wb+")
b = bytes("你好，how are you ?\n abc,ef", "utf-8")
f.write(b)
print(str(b, "utf-8"))
f.close()

# f = open("res/temp.txt", "w")
# f.write(str(bytes("你好，how are you ?", "utf-8")))
# f.close()

f = open("res/temp.txt", "rb")
# 为了读取一个文件的内容，调用 f.read(size), 这将读取一定数目的数据, 然后作为字符串或字节对象返回。
# size 是一个可选的数字类型的参数。 当 size 被忽略了或者为负, 那么该文件的所有内容都将被读取并且返回。
read = f.read()
print(str(read, "utf-8"))
print(f.tell())  # 返回文件对象当前所处的位置, 它是从文件开头开始算起的字节数。

data = {"name": "张三"}
data.update({"age": 12})
data["interesting"] = {"sport": {"ball": "basketball", "other": "dance"}, "look": "book"}

print(data)
# 序列化存储，类似于Java的对象流
f = open("tmp/test1.txt", "wb")
pickle.dump(data, f)
f.close()

f = open("tmp/test1.txt", "rb")
data1 = pickle.load(f)
print("data1: ", data1)

try:
    # i = 100 / 0
    f = open("123.txt", "r")
# except (ArithmeticError, NameError):
#     print("can not zero")
# 最后一个except子句可以忽略异常的名称，它将被当作通配符使用。
# 你可以使用这种方法打印一个错误信息，然后再次把异常抛出
except:
    print("Unexpected error:", sys.exc_info()[0])
    raise
# try except 语句还有一个可选的else子句，如果使用这个子句，
# 那么必须放在所有的except子句之后。这个子句将在try子句没有发生任何异常的时候执行。
else:
    pass
# 如果一个异常在 try 子句里（或者在 except 和 else 子句里）被抛出，
# 而又没有任何的 except 把它截住，那么这个异常会在 finally 子句执行后再次被抛出
finally:
    print("there is finally")


# 使用 else 子句比把所有的语句都放在 try 子句里面要好，这样可以避免一些意想不到的、
# 而except又没有捕获的异常。异常处理并不仅仅处理那些直接发生在try子句中的异常
# 而且还能处理子句中调用的函数（甚至间接调用的函数）里抛出的异常

# 当创建一个模块有可能抛出多种不同的异常时，
# 一种通常的做法是为这个包建立一个基础异常类，然后基于这个基础类为不同的错误情况创建不同的子类:
class MyException(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)

