import types


class Student:
    # 如果不允许开发者动态添加属性
    # __slots__ = ("name", "age")

    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age


stu = Student("小明", 18)

stu.sex = "男"


def getname(self):
    print(self.name)


# 动态添加对象方法 , types.MethodType 第一个参数是方法, 第二个参数是要给方法传的第一个参数
stu.getname = types.MethodType(getname, stu)
print(stu.name, stu.age, stu.sex)
stu.getname()


"""
如何动态添加和删除属性和方法，参考 https://blog.csdn.net/feit2417/article/details/81508092
"""