balance = 0
while True:
    choice = input("1) Deposit 2) Balance 3) Withdraw 0) Quit :")
    if choice == "1":
        amount = int(input("Enter the amount to deposit : "))
        balance += amount
        print(f"{amount} is deposited to your account")

    elif choice == "2":
        print(f"Availale balance is {balance:.2f}")
    elif choice == "3":
        withdraW = int(input("Enter the amount to withdraw : "))
        if withdraW <= balance:
            balance -= withdraW
            print(f"Remaining balance is {balance:.2f}")
        else:
            print("Not enough money")
    elif choice == "0":
        print("Goodbye")
        break

    else:
        print("Invalid Choice")