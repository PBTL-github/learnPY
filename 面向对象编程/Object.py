class Student:
    # 以下为类成员
    num = 0

    # 以下为对象只能添加的动态成员
    # __slots__ = ("name", "age")

    def __init__(self, name: str = None, age: int = None):
        self.name = name
        self.age = age


xiaoming = Student("小明", 18)
# xiaoming.name = "xiaoming"
print(xiaoming.name)

print(xiaoming.num)
print(Student.num)
