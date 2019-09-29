import random
import math
import learn1
import sys

temp = dict()  # 空参时用dict()，也可用{}
temp["name"] = "张三"  # 直接赋值
temp["age"] = "李四"
temp.update({"1": "a", "2": {"3": "c"}})  # 也可用于赋值
print(temp)

for t in temp:
    value = temp[t]
    print("key = %s , value = %s" % (t, value))

copy = temp.copy()
copy["123"] = str(123)

print("copy is %s" % copy)


class Person:

    def __init__(self) -> None:
        super().__init__()

    # 静态方法
    @staticmethod
    def test_age():
        return random.randrange(0, 100)

    # 类方法
    @classmethod
    def test_name(cls, name=""):
        randrange = random.randrange(0, 100)
        test = "111" + randrange
        return test


class Child(Person):

    def test_name(self, name=""):
        return super().test_name(name)


# 类型查看 type()认为子类属于父类
var = type("temp", (Person,), temp)
var1 = type(Person)
c = Child
p = Person

print(var.mro())
print(Person.test_age())
a = ["qq", "1111", "111111", {"1": {"1": "2"}}, (), [], ]
# 统计列表中某一对象的个数
print("None has : %s" % a.count(None))
a.sort(key=lambda ele: len(ele))
a.sort(key=lambda ele: len(ele))
print(a)
print(len(a))
# 统计了字符串中非abc的字符集合,集合元素不重复，列表可重复
# a = [x for x in 'abracadabra' if x not in 'abc']  # ['r', 'd', 'r']
a = {x for x in 'abracadabra' if x not in 'abc'}  # {'d', 'r'}
#
s1 = set()
for x in "abracadabra":
    if x not in "abc":
        s1.add(x)
# s1 = {'d', 'r'}
s1.add("22")
s1.update("33")
s1.remove("d")
print(s1)
print(a)

# Fibonacci series: 斐波纳契数列
# 两个元素的总和确定了下一个数
# a=0 b=1
a, b = 0, 1
print(a, b)
while b < 100:
    print(b, end=',')
    a, b = b, a + b
print("\n")
a = [10, 11, 111, 111, 111111, 111, 23]

print("result: %s" % learn1.list_print(a))
print("list by range ： %s " % (list(range(a.__len__() - 1, -40, -2))))
print("set: %s" % (set(range(a.__len__()))))

for f in a:
    pass
    # print(f)

for f in range(a.__len__()):
    pass
    # print(a[f])
# list会轮询 result： 23，111111，111，10，111
for f in range(a.__len__() - 1, -3, -2):
    pass
    # print(a[f])

i = iter(a)
for x in i:
    print(x)


class MyNumbers:

    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        if self.a < 20:
            self.a += 1
            return self.a
        else:
            raise StopIteration


myClass = MyNumbers()
myIter = iter(myClass)
while True:
    try:
        nextN = myIter.__next__()
        print(nextN)
    except StopIteration:
        # sys.exit()
        break
        pass
    # if nextN >= 100 * 1024 * 1024:
    #    break

test_list = [10, 20, 30, 33, 66, 99]
print(test_list)
# 此处传入1个可变对象list，当调用删除小于50的数后，list本身就发生了变化
learn1.list_del(test_list)
print("delete: " + test_list.__str__())


def s(v):
    return 2 * v


a = 100
tempS = s(a)
# a不会随函数运算发生变化
print("a = ", a)
print("s = ", tempS)


# 同名函数就近原则
def s(v: int):
    return ", " + str(v)


print(s(12))


def s(age=0, name=""):
    return str.format("姓名：%s, 年龄：%d" % (name, age))


# 如果指定了默认参数，则不传也不会报错
print(s(122))
# 指定名字传参则忽略顺序
print(s(name="张三", age=12))


# 指定了输入参数类型
def aa(data: list):
    count = 0
    for d in data:
        if d % 10 == 0:
            count += 1
    return count


a = [1, 1, 11, 10, 100, 1000, 1001]
print("aa = ", aa(a))


def change(*args):
    # 打印参数：为元组([1, 1, 11, 10, 100, 1000, 1001],)
    print(args)
    if len(args) == 0:
        return "None params!"
    else:
        return str(args)


#  打印返回值，如果没有返回值则为None
# print("change: ", change(a))
print("change: ", change(None))


# def change(v, v1, *args, v2):
#     pass


# def change(*args, v2, **kwargs):
#     pass


def change1(v2, **kwargs):
    print(v2, kwargs)
    pass
    return 100


change1(12, a=1, b=2, c=123, d=1222, name="张三")
# 偏离了匿名函数
v_ = lambda v1, v2: v1 * v2

print("r = ", v_(12, 23))


# 匿名函数直接做参数传入
def test(key=None, v=1):
    pass
    return key(v)


print("test is ", test(lambda v1: v1 * 10, 12))

number = 100


def fun(n):
    global number
    number = n
    return number


print("number: ", number)

print("fun: ", fun(300))

print("number: ", number)


def outer():
    n = 10
    print("n = ", n)

    def inner():
        nonlocal n  # nonlocal关键字声明
        n = 111
        print("n = ", n)
        return n

    return inner


print("outer: ", outer())
o = outer()
print(outer()())
