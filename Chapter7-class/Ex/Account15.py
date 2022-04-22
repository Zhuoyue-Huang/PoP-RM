"""Implement in-place += and -= operators."""
from numbers import Number


class Account(object):
    def __init__(self, name, account_number, initial_amount):
        self.name = name
        self.no = account_number
        self.balance = initial_amount

    def __str__(self):
        s = f"{self.name}, {self.no}, balance: {self.balance}"
        return s

    def __repr__(self):
        return f"Account({self.name}, {self.no}, {self.balance})"

    def __iadd__(self, other):
        if isinstance(other, Number):
            self.balance += other
            return self

    def __isub__(self, other):
        if isinstance(other, Number):
            self.balance -= other
            return self
