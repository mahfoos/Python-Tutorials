import random

hidden_no=random.randint(1,20)
print(hidden_no)

try:
    user_input=int(input("Enter a number between 1-20 : "))
    while user_input!=hidden_no:
        if (0<=user_input<=20):
            print ("incorrect guess")
        else:
            print("not in range")
        user_input=int(input("Enter a number between 1-20 : "))
    #else:
    print ("guess matched,hidden no is :",hidden_no)
    
except ValueError:
    print("need integer")
