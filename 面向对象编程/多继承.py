class A:
    def test(self):
        print("test")


class B:
    def demo(self):
        print("demo")

    def test(self):
        print("BTest")


class C(A, B):
    pass


c = C()
c.test()