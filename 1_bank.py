import account

checking = account.Account()
savings = account.Account()

checking.deposit(100)
checking.transfer(savings, 50)


# How can we test this code?
