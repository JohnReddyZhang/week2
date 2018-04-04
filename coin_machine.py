class CoinMachine:
    """
    return the amount in: [quarters, dimes, nickels, pennies]
    """
    def __init__(self, coin_slot):
        """
        param: coin_slot : List(Int)
        """
        self.quarters, self.dimes, self.nickels, self.pennies = coin_slot

    def calculation_dispense(self, number):
        # if number < 5:
        #     return [0,0,0,number]
        # elif number < 10:
        #     return [0,0, number // 5, number % 5]
        # else:
        quarters = number // 25
        dimes = number %25 // 10
        nickels = number % 25 % 10 // 5
        pennies = number %25 % 10 % 5
        return [quarters, dimes, nickels, pennies]

    def dispense(self, number):
        
