class BankAccount:
    def __init__(self, int_rate, myBalance=0):
        self.int_rate = int_rate
        self.balance = myBalance

    def deposit(self, myAmount):
        self.balance += myAmount
        return self

    def withdraw(self, myAmount):
        self.balance -= myAmount
        return self

    def display_account_info(self):
        print(self.balance)
        return self

    def yield_intrest(self):
        self.balance -= self.int_rate * self.balance
        return self


mohammad = BankAccount(0.05, 1000)
ahmad = BankAccount(0.02)

mohammad.deposit(1000).deposit(2000).deposit(3000).withdraw(
    100
).yield_intrest().display_account_info()

ahmad.deposit(100).deposit(200).withdraw(10).withdraw(20).withdraw(10).withdraw(
    30
).yield_intrest().display_account_info()
