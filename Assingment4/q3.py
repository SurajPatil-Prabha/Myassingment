class BankAccount:
    bank_name = "State Bank of India"

    def __init__(self, account_number, holder_name, balance):
        self.account_number = account_number
        self.holder_name = holder_name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print("Deposited:", amount)

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print("Withdrawn:", amount)
        else:
            print("Insufficient Balance")

    def check_balance(self):
        print("Current Balance:", self.balance)

    @classmethod
    def change_bank_name(cls, new_name):
        cls.bank_name = new_name


acc1 = BankAccount(1001, "Suraj", 10000)
acc2 = BankAccount(1002, "Rahul", 15000)

acc1.deposit(2000)
acc1.withdraw(1000)
acc1.check_balance()

print("\nBank Name:", BankAccount.bank_name)

BankAccount.change_bank_name("HDFC Bank")

print("Updated Bank Name:", BankAccount.bank_name)