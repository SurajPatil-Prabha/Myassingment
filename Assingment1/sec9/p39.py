balance = 1000

while True:
    print("1.Check")
    print("2.Deposit")
    print("3.Withdraw")
    print("4.Exit")

    choice = input()

    if choice == "1":
        print(balance)

    elif choice == "2":
        balance += int(input("Amount: "))

    elif choice == "3":
        balance -= int(input("Amount: "))

    elif choice == "4":
        break