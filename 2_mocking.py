import unittest
from unittest.mock import Mock

class Person:

    def greet(self):
        name = input("What is your name? ")
        print("Hi,", name)

    def calculate(*args):
        sum = 0
        for n in args:
            sum += n
        return sum

g = Person()
g.greet()
g.sum(1,2,3,4)

# How can we test this?
