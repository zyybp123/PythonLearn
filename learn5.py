class Base:
    id = 0
    name = ""
    __age = 10  # 私有成员变量

    # def __init__(self) -> None:
    #     super().__init__()

    def __init__(self, name, id):
        self.name = name
        self.id = id
        super().__init__()

    def name_set(self, name):
        self.name = name


# b = Base()
# b.name = "张三"
# print("name, ", b.name)
# b.name_set("李四")
# print("name, ", b.name)

b = Base("张三", 1)
# print(b.__age)
print("name = {}, id = {}".format(b.name, b.id))


class Vector:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __str__(self):
        return 'Vector (%d, %d)' % (self.a, self.b)

    # 定义了add方法，所以对象可以直接加
    def __add__(self, other):
        return Vector(self.a + other.a, self.b + other.b)

    def __mul__(self, other):
        return Vector(self.a * other.a, self.b * other.b)


v1 = Vector(2, 10)
v2 = Vector(5, -2)
print(v1 + v2)
print(v1 * v2)
