import random

hidden_no=random.randint(1,20)
print(hidden_no)

try:
    user_input=int(input("Enter a number between 1-20 : "))
    while user_input!=hidden_no:
        if (user_input<hidden_no):
            print ("too low")
        else:
            print("too high")
        user_input=int(input("Enter a number between 1-20 : "))
    else:
        print ("guess matched,hidden no is :",hidden_no)
    
except ValueError:
    print("need integer")
