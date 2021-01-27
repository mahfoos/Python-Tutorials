cost_of_meal = int(input("Cost of the Meal:"))
dinner_satis = input("Press '1' to Totally satisfied \nPress '2' to Satisfied \nPress '3' to Dissatisfied\n")
if dinner_satis =='1':
    tip=cost_of_meal*(20/100)
    print("You got",tip,"tips")

elif dinner_satis =='2':
    tip=cost_of_meal*(15/100)
    print("You got",tip,"tips")

elif dinner_satis =='3':
    tip=cost_of_meal*(10/100)
    print("You got",tip,"tips")

else:
    print("Please rating")
