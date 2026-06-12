class ATM:
    def __init__(self, balance):
        self.__balance = balance

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        self.__balance -= amount

    def show_balance(self):
        print(self.__balance)

a = ATM(5000)
a.deposit(1000)
a.withdraw(500)
a.show_balance()