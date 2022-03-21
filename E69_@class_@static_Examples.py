class FixedFloat:
    def __init__(self, amount):
        self.amount = amount

    def __repr__(self):
        return f'<FixedFloat {self.amount:.2f}>' # ":.2f" ~ prints the amount to 2 decimal places

    @classmethod
    def from_sum(cls, value1, value2):
        return cls(value1 + value2)

new_number = FixedFloat.from_sum(19.575, 0.789)
print(new_number)


class Euro(FixedFloat):
    def __init__(self, amount):
        super().__init__(amount)
        self.symbol = '€'

    def __repr__(self):
        return f'<Euro {self.symbol}{self.amount:.2f}>'

money = Euro.from_sum(16.758, 9.999)        # This will return a FixedFloat object if we used a @staticmethod
print(money)

# Use a class method whenever something DOES NOT use self.
# Try not to use staticmethods they are not very useful
        # only when you know the class will NOT be inherited from






