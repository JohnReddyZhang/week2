import account

checking = account.Account()
savings = account.Account()

checking.deposit(100)
checking.transfer(savings, 50)
# assert false == checking.transfer(savings, 150) # return false...

assert checking.balance() == 50
checking.deposit(10)
assert checking.balance() == 60

# print(checking.balance())


# How can we test this code?
