
pet_name = " "
pet_gender = " "
pet_hunger = 10
Apple = 5
JELLO = 10
function = 4
while True:
    print("THIS IS YOUR PET!")
    print("     ")
    print("---------------------")
    print("|                   |")
    print("|   •°    v   •°    |")
    print("|___________________|")
    print("   ")
    print("1. Create Pet ")
    print("2. Feed Pet ")
    print("3. View Pet ")
    print("4. Exit ")
    print(" ")
    choice = input("Wachu wanna do? choose 1, 2, 3 ;) ")
        
    if choice =="1":
        print("You chose to create pet!")
                
        pet_name =  input("Enter pet name: ")
        pet_gender = input("Enter pet gender: ")
        print("vvvvvvvv")
        print(f"Your pet name is {pet_name}, {pet_gender}! ")
        print("∆∆∆∆∆∆")
               
    elif choice == "2":
        print("---- LET'S FEED YOUR PET ----")
        print(" ")
        print("---------------------") 
        print("|                    |")                             
        print("|   •°    v   •°    |")
        print("|___________________|")
        print("   ")
        
        print(f"Current pet hunger: {pet_hunger}")
        hunger = input("Feed Pet type Apple +5, JELLO +10: ")
        if hunger == "Apple":
            pet_hunger = pet_hunger + Apple
            print(f"Current Pet Hunger: {pet_hunger}")
            print(" ")
            
        elif hunger == "JELLO":
            pet_hunger = pet_hunger + JELLO
            print(f"Current Pet Hunger: {pet_hunger}")
            print(" ")
        
        else:
            pet_hunger = pet_hunger - function
            print(f"Current Pet Hunger: {pet_hunger}")
  
                       
 
                
    elif choice == "3":
        print("------ VIEWING PET ------")
        print(" ")
        print("---------------------")
        print("|                   |")
        print("|   •°    v   •°    |")
        print("|___________________|")
        print("   ")
        print("vvvvvvvvvvvvvvvvvvvv")
        print(f"Pet name: {pet_name}")
        print(f"Pet gender: {pet_gender}")
        print(f"Current Pet Hunger: {pet_hunger}")
        print("∆∆∆∆∆∆∆∆∆∆∆∆∆∆")
        Message = input("Enter 1 to exit: ")
        
        if Message == "1":
            print("Going to the Menu")

          
    elif choice == "4":
        print("YOU CHOSE EXIT")
        break
                    
                
                
                
                
            
            
            
       
            
    
