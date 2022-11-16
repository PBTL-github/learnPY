class Student:
    """学生类"""

    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def __repr__(self):
        return f"{self.name}: {self.age}"


xiaoming = Student("小明", 18)
stud = {xiaoming}
print(stud)
print(xiaoming)
