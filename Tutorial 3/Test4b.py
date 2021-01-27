num_1=int(input("Enter the First Number"))
operator=input("Enter the operator")
num_2=int(input("Enter the Seccond Number"))
try:
    if operator=="+":
        print(num_1+num_2)
    elif operator=="-":
        print(num_1-num_2)
    elif operator=="*":
        print(num_1*num_2)
    elif operator=="/":
         print(num_1/num_2)

except ZeroDivisionError:
    print("Cant Divide Zero")
         
       

