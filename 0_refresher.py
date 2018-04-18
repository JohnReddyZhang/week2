# print("Hello")

# Functions, arguments, splat operator

def greet(name):
    print(f"Howdy, {name}")

def calculate(*numbers):
    sum = 0
    for n in numbers:
        sum += n
    return sum

# greet("Jeff")
# print(calculate(1,2,3))
# Assertions

# assert 1 == 2
# Classes, self, super()
class Person:
    def __init__(self, name):
        self.name = name


# assert 1 == 2

# Classes, self, super()

class Person:

    def __init__(self, name):
        self.name = name

    def introduce(self):
        print(f"Hi, my name is {self.name}")

class Employee(Person):

    def __init__(self, name):
        super().__init__(name)
        self.company = "UChicago"

    def introduce(self):
        super().introduce()
        print(f"I work at {self.company}.")

p1 = Employee("Alice")
p1.company = "Microsoft"
p1.introduce()
