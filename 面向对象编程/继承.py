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
        print("eat")

    def bark(self):
        print("狗叫")


dog = Dog()
dog.eat()
