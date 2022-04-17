class AccountP(object):
    def __init__(self, name, account_number, initial_amount):
        self._name = name
        self._no = account_number
        self.transactions = 0
        self._transactions = []

    def deposit(self, amount):
        import datetime
        current_time = datetime.datetime.now()
        self.transactions += 1
        self._transactions.append({'amount': amount, 'time': current_time})

    def withdraw(self, amount):
        import datetime
        current_time = datetime.datetime.now()
        self.transactions += 1
        self._transactions.append({'amount': -amount, 'time': current_time})

    def get_balance(self):
        return sum([dic['amount'] for dic in self._transactions])

    def dump(self):
        name = self._name
        no = self._no
        bal = self.get_balance()
        trans = self.transactions
        s = f"{name}, {no}, balance: {bal}, transactions: {trans}"
        print(s)
