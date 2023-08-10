print("Main menu")
print("1- Account Balance\n2-Withdraw cash\n3-Deposit cash\n4-Transfer funds\n5-Change pin\n6-Exit")
user_pin = 5665
b = 2500
while True:
    r = int(input("Please enter your pin:"))
    if r != user_pin:
        continue
    else:
        break
while True:
    a = int(input("Please select the operation you want to perform:"))

    if a == 1:
        print(b)
    elif a == 2:
        c = int(input("Please enter the amount of money you want to withdraw:"))
        if c > b:
            print("Insufficient balance")
            continue
        b -= c
        f = input("If your want to print the receipt press '8' or don't want to print receipt press '9'")
        print("Your transaction is being processed.....")
        print("Please take your money")
    elif a == 3:
        d = int(input("Please enter the amount of money you want to deposit: "))
        g = input("If your want to print the receipt press '8' or don't want to print receipt press '9'")
        print("Your transaction is being processed.....")

        b += d
    elif a == 4:
        m = input("Please write the recipient's account number: ")
        k = int(input("Please write transfer amount you want: "))
        w = input("If your want to print the receipt press '8' or don't want to print receipt press '9'")
        if k > b:
            print("Insufficient balance")
            continue
        print("your transaction is being processed.....")
    elif a == 5:
        s = input("Please enter your pin:")
        if s == user_pin:
            p = input("please enter new pin:")
            ab = input("Again enter new pin:")
            if p == ab:
                user_pin = p
        if s != user_pin:
            print("Pins don't match.")
            continue
    elif a == 6:
        se = input("Please press 'l' to exit")
        if se == "l":
            break

