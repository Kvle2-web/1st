while True:
    print("======= STUDENT HUB =======")


    print("      ")
    print(f"1. GPA checker")
    print("2. Calculator")
    print("3. Student information")
    print("4. Age checker")
    print("5. Study hour calculator")
    print("6. Exit")

    choice = input("Kindly choose 1, 2, 3, 4, 5, or 6:")

    if choice == "1":
        print("You chose GPA_checker")
    
        GPA_checker = float(input("Enter your gpa: "))

        if GPA_checker >= 90:
              print(" ")
              print("PASSED - EXCELLENT")  
        elif GPA_checker >= 80:
              print(" ")
              print("PASSED - VERY GOOD")       
        elif GPA_checker >= 75:
              print(" ")
              print("PASSED - GOOD")
        else:
              print(" ")
              print("FAILED - SORRY BRO :(")
    
    elif choice == "2":
        print("You chose Calculator ")
    
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        operation = input("Choose operation +, -, *, /: ")

        if operation == "+":
            print(num1 + num2)
        elif operation == "-":
            print(num1 - num2)
        elif operation == "*":
            print(num1 * num2)
        elif operation == "/":
            print(num1 / num2)
        else:
            print("You trippin dawg")
        
    elif choice == "3":
        print("You chose Student profile")
 
        First_name  = input("Enter first name: ")
        Middle_name = input("Enter middle name: ")
        Last_name = input("Enter Last name: ")
        age = int(input("Enter age: "))
        Course = input("Enter course: ")
        Year = str(input("What year: "))
        
        print(" ")
        print("====== YOUR I.D ======")
        print("====================")    
        print(f"Name: {First_name} {Middle_name} {Last_name}")
        print(f"Age: {age}")
        print(f"Course: {Course}")
        print(f"Year: {Year}")
        
    elif choice == "4":
        print("You chose Age checker")
        
        Age_checker = int(input("Enter your age: "))
        
        if Age_checker >= 18:
            print("You're in Unc")
        else:
            print("Nahh you to young little bro")
    
    elif choice == "5":
        print("You chose Study hour calculator")
        
        Hour = float(input("Enter hours studied per day: "))
        Day = int(input("How many days: "))
        Total = Hour * Day
        
        print("  ")
        print(f"Your total study time is {Total} Hours! ")
        
    elif choice == "6":
        print("Why you backing up? you scared little boy? ")
        break
                 
                  
    
       
    
    
    



