# Account class

class Account:

    def __init__(self):
        self.money = 0

    def deposit(self, amount):
        self.money += amount

    def transfer(self, other_account, amount):
        self.money -= amount

    def balance(self):
        return self.money
