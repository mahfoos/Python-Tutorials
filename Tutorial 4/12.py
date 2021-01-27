import random

random_number=random.randint(1,20)
print(random_number)

for i in range(1,6):
    guess=int(input("Guess the number in between 1-20: "))
    if guess==random_number:
        print("guess matched with system, you got it on attempt",i)
        break
    else:
        if guess<random_number:
            print("guess is too low")
        else:
            print("guess is too high")
        print("you have only ",5-i,"attempts to guess number\n") 
        

