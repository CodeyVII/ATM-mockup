import sys
import datetime
now = datetime.datetime.now()
print ("Current date and time : ")
print (now.strftime("%Y-%m-%d %H:%M:%S"))

name = input("Welcome, What is your name? \n")
allowedUsers = ['Seyi','Mike','Love','Larry']
allowedPassword = ['passwordSeyi','passwordMike','passwordLove','passwordLarry']
balance = 20000

if(name in allowedUsers):
    password = input("Your password? \n")
    userId = allowedUsers.index(name)

    if(password == allowedPassword[userId]):
    
        print('Welcome %s' % name)
        print('These are the available options')
        print('1. Withdrawal')
        print('2. Cash Deposit')
        print('3. Complaint')
        
    isSelectedOptionValid = False
    while isSelectedOptionValid == False:

        selectedOption = int(input("Select transaction: "))


        if (selectedOption == 1):
            Withdraw = int(input("How much would you like to withdraw: "))
            if (Withdraw < balance):
                print("take your cash",Withdraw )  
            else:
                print("Invalid Cash")
                isSelectedOptionValid == True


        elif (selectedOption == 2): 
            Deposit = int(input("How much would you like to deposit?: "))
            currentBalance = (balance + Deposit)
            if (Deposit > 0):
                print("Current Balance ",currentBalance)
            else:
                print("No deposit made")
                isSelectedOptionValid == True


        elif (selectedOption == 3):
            Complaint = input("What issue will you like to report?: ")
            print('Thank you for contacting us')
            isSelectedOptionValid == True
            
            

        else:
            print('Invalid Option selected, Please try again')


    else:
        print('Password incorrect, Please try again')

else:
    print('Name not found, please try again')


    
    
            
