class Account(object):
    def __init__(self, name, account_number, initial_amount):
        self._name = name
        self._no = account_number
        self._balance = initial_amount
        self.transactions = 0

    def deposit(self, amount):
        self._balance += amount
        self.transactions += 1

    def withdraw(self, amount):
        self._balance -= amount
        self.transactions += 1

    def dump(self):
        s = f"{self._name}, {self._no}, balance: {self._balance}, \
            transactions: {self.transactions}"
        print(s)
