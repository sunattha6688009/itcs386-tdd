class Quantity:

# A1    
    # def __init__(self, amount):
    #     self.amount = amount

    # def times(self, multiplier):
    #     self.amount = 600

# A2
    def __init__(self, amount):
        self.amount = amount

    def times(self, multiplier):
        return Quantity(self.amount * multiplier)