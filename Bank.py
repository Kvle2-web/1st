Bank = float( )
while True:
    print("=====================")
    print("========BANK========")
    print(" ")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Check Balance")
    print("4. Exit")
    function = input("Deposit or Withdraw? Choose 1, 2, 3, or 4: ")
    
    if function == "1":
        print("Let's Deposit")
        Deposit = float(input("Enter Deposit amount: "))
        Bank = Bank + Deposit
    
        print(Bank)
        
       
    elif function == "2":
        print("Let's Withdraw") 
        Withdraw = float(input("Enter Withdrawal amount: "))
                                                  
        if Withdraw > Bank:
            print("Sorry not enough Balance")
        else:
            Bank = Bank - Withdraw
            print(Bank)
                   
    elif function == "3":
        print("Let's check your current Balance")
        print(" ")
        print(f"Your Current Balance is: ₱{Bank}")
    
    else:
        print("Let's Exit")
        break
    