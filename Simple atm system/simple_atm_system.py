# Simple ATM program in Python

balance = 1000.0  # initial balance


def show_menu():
    print("ATM Menu:")
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Exit")


def check_balance():
    print(f"Current Balance: {balance:.2f}")


def deposit_money():
    global balance
    amount = float(input("Enter amount to deposit: "))
    if amount > 0:
        balance += amount
        print(f"{amount:.2f} deposited successfully!")
    else:
        print("Invalid amount!")


def withdraw_money():
    global balance
    amount = float(input("Enter amount to withdraw: "))
    if amount > 0 and amount <= balance:
        balance -= amount
        print(f"{amount:.2f} withdrawn successfully!")
    elif amount > balance:
        print("Insufficient balance")
    else:
        print("Invalid amount")


def main():
    while True:
        show_menu()
        try:
            choice = int(input("Enter your choice (1-4): "))
        except ValueError:
            print("Invalid input! Please enter a number.")
            continue

        if choice == 1:
            check_balance()
        elif choice == 2:
            deposit_money()
        elif choice == 3:
            withdraw_money()
        elif choice == 4:
            print("Thank you for using the ATM. Bye!")
            break
        else:
            print("Invalid option! Try again.")


if __name__ == "__main__":
    main()
