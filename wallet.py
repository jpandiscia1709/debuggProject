import coins


class Wallet:
    def __init__(self):
        money = []
        self.money = money
        self.fill_wallet = fill_wallet(self)


def fill_wallet(self):
    """Method will fill wallet's money list with certain amount of each type of coin when called."""
    for index in range(8):
        self.money.append(coins.Quarter())
    for index in range(10):
        self.money.append(coins.Dime())
    for index in range(20):
        self.money.append(coins.Nickel())
    for index in range(50):
        self.money.append(coins.Penny())
