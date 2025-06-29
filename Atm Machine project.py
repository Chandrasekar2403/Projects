print("                       Welcome to Chandru Bank!!!                ")
pin=4133
chances=3
balance=10000
while chances!=0:
    user_pin=int(input('Enter  your pin:  '))
    if user_pin != pin:
        chances=chances-1
        print('WRONG Pin number')
        print('You have ',chances,'of chances of left')
        
    else:
        user_choice = input("B : Balance, D :Deposit, W : Withdraw ")
        if user_choice == "B":
            print("Your balance is Rs.",balance)

        if user_choice == "D":
            deposit=int(input('Enter the amount that you want to deposit: '))
            balance=deposit + balance
            print("You have deposited Rs: ",deposit)
            print("Yor current balance is Rs: ",balance)

        if user_choice == "W":
            withdraw=int(input('Enter the amount that you want to withdraw: '))
            if withdraw <= balance:
                  balance = balance -  withdraw
                  print("You have withdrawn amount Rs: ",withdraw)
                  print("Your balance is Rs: ",balance)
            else:
                print('Insufficient Balance')
            

    user_exit = input("Would you like to exit: YES/NO")
    if user_exit == "YES":
        print("THANK YOU")
        break

    else:
        continue

                      
