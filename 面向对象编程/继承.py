class Animal:
    def eat(self):
        print("吃")

    def drink(self):
        print("喝")

    def run(self):
        print("跑")

    def sleep(self):
        print("睡")


class Dog(Animal):
    def eat(self):
        super().eat()
        print("eat")

    def run(self):
        # python2.0版本中使用父类方法的写法
        Animal.run(self)
        print("run")

    def bark(self):
        print("狗叫")


dog = Dog()
dog.eat()
dog.run()
