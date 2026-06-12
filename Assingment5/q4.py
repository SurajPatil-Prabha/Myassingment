class BankAccount:
    def __init__(self):
        self.balance = 0

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        self.balance -= amount

a = BankAccount()
a.deposit(1000)
a.withdraw(200)
print(a.balance)