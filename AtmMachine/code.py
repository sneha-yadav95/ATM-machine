import time

print(" Please Insert Your Card : ")
time.sleep(4)

password = 12345

pin = int(input("Enter Your ATM Pin :"))

balance = 5000

if pin==password:
    while True:
    
        print("=========================================================================================")
        print("=========================================================================================")
        print("=========================================================================================")
        
        print("""
            1 == balance
            2 == withdraw balance
            3 == deposit balance
            4 == exit
            """)
        print("=========================================================================================")
        
        try:
            option = int(input("Please enter your choise : "))
            
        except:
            print("Please enter a valid option")
            
        match option:
            
            case 1:
                print("=================================================================================")
                
                print(f" Your current balance is {balance}")
                
            case 2:
                withdraw_amount = int(input("Please enter withdraw amount"))
                balance = balance-withdraw_amount
                
                print("=================================================================================")
                
                print(f"{withdraw_amount} is debited from your account")
                
                print("=================================================================================")
                print("=================================================================================")
                
                
                print(f" Your current balance is {balance}")
                
            case 3:
                deposit_amount = int(input("Please enter deposit amount :"))
                balance = balance + deposit_amount
                
                print("=================================================================================")
                print("=================================================================================")
                
                
                print(f"{deposit_amount} is credited to your account ")
                
                print("=================================================================================")
                print("=================================================================================")
                
                print(f"Your updated balance is {balance}")
                
            case 4:
                break
                           
else:
    print("Wrong pin please try again")            
        