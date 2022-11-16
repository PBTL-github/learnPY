class Student:
    def __init__(self, name: str, age: int):
        self.__name = name
        self.__age = age

    # 获取私有属性name
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


xiaoming = Student("小明", 18)

print(xiaoming.name)
xiaoming.name = "asdfas"
print(xiaoming.name)
