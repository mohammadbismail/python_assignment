class BankAccount:
    def __init__(self, int_rate=.02, myBalance=0):
        self.int_rate = int_rate
        self.balance = myBalance

    def deposit(self, myAmount):
        self.balance += myAmount
        return self

    def withdraw(self, myAmount):
        if self.balance <= myAmount:
            print("Insuffient balance")
        else:
            self.balance -= myAmount
        return self

    def display_account_info(self):
        print(self.balance)
        return self

    def yield_intrest(self):
        self.balance += self.int_rate * self.balance
        return self


class User:
    def __init__(self, myName, myEmail):
        self.name = myName
        self.email = myEmail
        self.balance = BankAccount()

    def make_deposit(self, myAmount):
        self.balance.deposit(myAmount)
        return self

    def make_withdraw(self, myAmount):
        self.balance.withdraw(myAmount)
        return self

    def display_balance(self):
        self.balance.display_account_info()
        return self


ahmad = User("Ahmad", "ahmad@gmail.com")

ahmad.make_deposit(100).display_balance()
