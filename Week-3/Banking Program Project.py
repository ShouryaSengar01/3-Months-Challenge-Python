def show_balance():
    print("***********************")
    print(f"Your balance is ${balance:.2f}")
    print("***********************")

def deposit():
    print("***********************")
    amount = float(input("Enter an amount to be deposited: "))
    print("***********************")

    if amount < 0:
        print("***********************")
        print("That amount can't be deposited")
        print("***********************")
        return 0
    else:
        print("Your amount has been deposited successfully")
        return amount

def withdraw():
    print("***********************")
    amount = float(input("Enter an amount to be withdrawn: "))
    print("***********************")

    if amount > balance:
        print("***********************")
        print("Insufficient Funds")
        print("***********************")
        return 0
    elif amount < 0:
        print("***********************")
        print("Enter a Valid Amount")
        print("***********************")
        return 0
    else:
        return amount

def main():
    global balance
    balance = 0
    is_running = True

    while is_running:
        print("***********************")
        print("    Banking Program    ")
        print("***********************")
        print("1. Show Balance")
        print("2.Deposit")
        print("3.Withdraw")
        print("4.Exit")
        print("***********************")

        choice = input("Enter Your Choice(1-4): ")

        if choice == "1":
            show_balance()
        if choice == "2":
            balance += deposit()
        if choice == "3":
            balance -= withdraw()
        if choice == "4":
            is_running = False
        else:
            print("***********************")
            print("That isn't a Valid Choice")
            print("***********************")
    print("***********************")
    print("Thank You, Have a Nice Day")
    print("***********************")

if __name__ == '__main__':
    main()



# P.S. I know it's been a very incosistent week, uploading files a day or 2 later on github but I just wanna make this clear that I was working on these but wasn't uploading(i really don't know why and yes it does sound like
# an excuse). But From now on i'll be uploading my files daily and i left some topics this week which i will cover in the upcoming week.
