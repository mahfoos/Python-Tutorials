count=0
score=0
total=0
try:
    score=int(input("Enter the score: "))
    while score!=-9:
            total+=score
            count+=1
            score=int(input("Enter the score: "))
    if count==0:
        print("zero division error")
    else:
        average=total/count
        print("average is: ",average)


except ValueError:
    print("need integer")

    
