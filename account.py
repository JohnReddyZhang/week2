#Account

class Account:
    def __init__(self):
        self.money = 0

    def deposit(self, amount):
        self.money += amount

    def transfer(self, target, amount):
        self.money -= amount
        target.money += amount

# SIMPLEST THING YOU COULD DO:
class Account:
    # def __init__(self):
    #     self.money = 0

    def deposit(self, amount):
        # self.money += amount
        pass

    def transfer(self, target, amount):
        # self.money -= amount
        # target.money += amount
        pass
