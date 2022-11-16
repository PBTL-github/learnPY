class People:
    num = 0

    def __init__(self, name: str, age):
        self.name = name
        self.age = age

    @classmethod
    def setNum(cls, num: int):
        cls.num += num
        print(cls.countNum2(10, 20))

    @classmethod
    def testaaa(cls):
        cls.aaa()

    @staticmethod
    def countNum2(num: int, num2: int):
        return num + num2

    def aaa(self):
        self.setNum(10)
        print(self.countNum2(10, 30))


people = People("xiaoming", 18)
people.aaa()
print(people.num)
print("-" * 50)
people.testaaa()
print(people.num)

"""
静态方法和类方法的区别：
静态方法： 不能调用类中的类成员， 和对象成员方法
类方法： 能调用类成员和静态方法， 不能调用对象成员和对象方法

相同点：
不能调用对象成员方法
"""
