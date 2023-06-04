from typing import Literal


Currency = Literal["USD", "EUR", "JPY", "GBP", "CHF", "CAD", "AUD"]

class Money:
    def __init__(self, amount: float, currency: Currency):
        self.amount = amount
        self.currency = currency
    
    def __add__(self, other: "Money") -> "Money":
        if self.currency != other.currency:
            raise ValueError("Cannot add two Money objects with different currencies")
        return Money(self.amount + other.amount, self.currency)
    
    def __sub__(self, other: "Money") -> "Money":
        if self.currency != other.currency:
            raise ValueError("Cannot subtract two Money objects with different currencies")
        return Money(self.amount - other.amount, self.currency)
    
    def __mul__(self, other: float) -> "Money":
        return Money(self.amount * other, self.currency)
    
    def convert(self, to_currency: Currency, rate: float) -> "Money":
        return Money(self.amount * rate, to_currency)