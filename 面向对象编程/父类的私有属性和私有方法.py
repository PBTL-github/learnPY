class A:
    def __init__(self):
        self.num_1 = 100
        self.__num_2 = 200

    # 创建私有方法
    def __test(self):
        print(f"私有属性和共有属性的值： {self.num_1}, {self.__num_2}")


# 创建新类继承A
class B(A):
    def demo(self):
        super().__test()


b = B()
print(b.num_1)
# 不允许子类直接去调用父类的私有方法
b.demo()

"""
只能在父类中定义公有方法去调用私有方法才能让子类能够访问
"""
