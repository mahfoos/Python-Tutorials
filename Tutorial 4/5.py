print(
    '''Enter 1 for current account
       Enter 2 for savings account
       Enter 3 for overdraft
       Enter 4 to quit'''
    )

while True:
    try:
        option = int(input("Select option: "))
        if option==1:
            print("Current account")
        elif option ==2:
            print("Savings account")
        elif option ==3:
            print("over account")
        elif option ==4:
            print("exit")
            break
        else:
            print("unrecognized menu number")
        
    except ValueError:
        print("menu option is not defined.")

