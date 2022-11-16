class Student:
    def __init__(self, name: str, age: int):
        self.__name = name
        self.__age = age
        self.num = 0

    def getname(self):
        return self.__name


xiaoming = Student("小明", 18);
print(xiaoming.getname())
print(xiaoming.num)
print(xiaoming.__name)
# 所谓的私有属性在python中并非完全无法访问
print(xiaoming._Student__name)
