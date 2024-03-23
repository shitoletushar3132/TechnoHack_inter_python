''' ATM simulator
Create a program that simulates the all atm
functionalities and operations (Check balance,
Deposit, Withdraw) '''

def check_balance(balance):
    print()
    print("Currnet Balance : ",balance)
    return balance

def deposit(balance):
    de = int (input("enter a amount that you want to deposit : " ))
    balance = balance + de
    print()
    print("deposit successfully---")
    check_balance(balance)
    return balance

def Withdraw(balance):
    de = int (input("enter a amount that you want to withdraw : " ))
    cu = check_balance(balance)
    if(de<= cu):
        balance = balance - de
        print()
        print("withdraw successfully---")
    elif(de>cu):
        print()
        print("Not sufficient balance  ")
    check_balance(balance)
    return balance

def user():

    balance = 100
    
    while(True):
        print('_'*30)
        print("1. Check Balance ")
        print("2. Deposit the amount")
        print("3. Withdraw the amount")
        print("4. Exit ")
        print('_'*30)
        print()

        ch = input("Enter a option(1/2/3/4): ")
        print('_'*30)

        while ch not in ['1','2','3','4']:
            print('_'*30)
            print("1. Check Balance ")
            print("2. Deposit the amount")
            print("3. Withdraw the amount")
            print("4. Exit ")
            print('_'*30)
            print()
            ch = input("Enter a option(1/2/3/4) : ")
            print('_'*30)
        match(ch):
            case '1':
                check_balance(balance)
            case '2':
                balance=deposit(balance)
            case '3':
                balance=Withdraw(balance)
            case '4':
                print()
                print("thanks for using the system")
                break
        
user()
