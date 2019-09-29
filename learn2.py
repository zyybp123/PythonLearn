import os


class Test:
    def __init__(self) -> None:
        super().__init__()

    def test1(self, a):
        return a


i = 100
print(Test.test1(Test(), i))


# print("a or b: %s" % (a or b))  # 或运算 2 短路运算
# print("a and b: %s" % (a and b))  # 与运算 10
# print("not a: %s" % (not a))  # 非运算 False
#
# s1 = None
# s2 = 'b'
# print("s1 or s2: %s" % (s1 or s2))  # 或运算 b 短路运算
# print("s1 and s2: %s" % (s1 and s2))  # 与运算 None
# print("not s1: %s" % (not s1))  # 非运算 True


# not has a lower priority than non-Boolean operators,
# so not a == b is interpreted as not (a == b), and a == not b is a syntax error.

class Person:
    # 与Java的构造函数类似
    def __init__(self, name='', age=0):
        self.name = name
        self.age = age

    # 与Java的equals函数类似
    def __eq__(self, o: object) -> bool:
        # isinstance 和 type 的区别在于：
        #
        # type()不会认为子类是一种父类类型。
        # isinstance()会认为子类是一种父类类型。
        return isinstance(o, Person) and self.name.__eq__(o.name) and self.age == o.age

    # 与Java的toString方法类似
    def __str__(self) -> str:
        return "姓名：" + self.name


# print("a<b: %s" % (a < b))
# print("a>b: %s" % (a > b))
# print("a>=b: %s" % (a >= b))
# print("a<=b: %s" % (a <= b))
# print("a==b: %s" % (a == b))
# print("a is b: %s" % (a is b))
# print("a is not b: %s" % (a is not b))

p = Person("张三", 10)
p1 = Person("张三", 10)
t = Test

print("p is p1: %s" % (p is p1))  # 比较的是地址
print("p is not p1: %s" % (p is not p1))
# p equal p1: NotImplemented，比较前要重写eq 方法，与Java类似
print("p equal p1: %s" % Person.__eq__(p, p1))

a = 3.1415926
b = 10
print("a + b = %s " % (a + b))
print("a - b = %s " % (a - b))
print("a * b = %s " % (a * b))
print("a / b = %s " % (a / b))
print("a // b = %s " % (a // b))
print("a %% b = %s " % (a % b))
print("-a = %s " % (-a))
print("+a = %s " % (+a))
print("abs(a - b) = %s " % (abs(a - b)))  # 7 绝对值
print("int(a / b) = %s " % (int(a / b)))  # 0 和 // 类似
print("float(a / b) = %s " % (float(a / b)))
c: complex = complex(a)
print("complex(a) = %s " % c)  # 复数(3+0j)带有实部(re),虚部(im)虚部默认为0
print("c.conjugate() = %s " % c.conjugate())  # 共轭复数
print(divmod(a, b))  # 函数把除数和余数运算结果结合起来，返回一个包含商和余数的元组(a // b, a % b)。
print("pow(a, b) = %s " % pow(a, b))  # a的b次幂
print("a ** y = %s " % a ** b)  # a的b次幂
# 输入函数，2.x表现为raw_input
# input("按下 enter 键退出，其他任意键显示...\n")

del a, b  # 删除某一对象的引用
# 删除后要重新定义
a = 1
b = 2
print("a,b %s,%s " % (a, b))

test = 'who are you?'
# [start,end] 正数代表从左向右(0开始)，负数代表从右向左(-1开始)
print(test[-6:-3])  # e y

list1 = [a, b, c]
# 数据存储和类型无关
list2 = [0, 1, 2, 3, 4, "12", p]
print("len = %s, size = %s , list2 is %s" % (list2.__len__(), list2.__sizeof__(), list2))
# 与Python字符串不一样的是，列表中的元素是可以改变的：
list2[3] = "11111"
print(list2)
print(list2[1:5])  # [1, 2, '11111', 4] 不包尾
# Python 列表截取可以接收第三个参数，参数作用是截取的步长，包头尾
# 以下实例在索引 1 到索引 6 的位置并设置为步长为 2（间隔一个位置）来截取字符串：
print(list2[1:6:2])  # [1, '11111', '12']

tuple1 = (1, '123', p, 34, 46, 67)
tuple2 = ()
tuple2 = (1, 2, 1, 1)
tuple3 = (1,)

var = tuple1[-3]
print(tuple2)
# 集合
student = {'Tom', 'Jim', 'Mary', 'Tom', 'Jack', 'Rose'}
print(student)  # 输出集合，重复的元素被自动去掉
# 成员测试
if 'Rose' in student:
    print('Rose 在集合中')
else:
    print('Rose 不在集合中')
# set可以进行集合运算
a = set('abracadabra1222')  # 会遍历每个字符，然后去重得到一个字符集合
b = set('alacazam')
print(a)
print(a - b)  # a 和 b 的差集
print(a | b)  # a 和 b 的并集
print(a & b)  # a 和 b 的交集
print(a ^ b)  # a 和 b 中不同时存在的元素

#
di = {}
di['one'] = "1 - 菜鸟教程"
di[2] = "2 - 菜鸟工具"
tiny = {'name': 'runoob', 'code': 1, 'site': 'www.runoob.com'}
print(di['one'])  # 输出键为 'one' 的值
print(di[2])  # 输出键为 2 的值
print(tiny)  # 输出完整的字典
print(tiny.keys())  # 输出所有键
print(tiny.values())  # 输出所有值
