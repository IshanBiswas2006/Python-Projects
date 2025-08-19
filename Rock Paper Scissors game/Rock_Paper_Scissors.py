import random

n=input("Enter your choice(R,P,S): ").upper()

youDict={"R":1,"P":-1,"S":0}
revDict={1:"Rock",-1:"Paper",0:"Scissors"}
you=youDict[n]
Computer=random.choice([1,-1,0])

print(f"Your choice: {revDict[you]}\nComputer choice: {revDict[Computer]}")

if(Computer==you):
    print("Draw")

else:
    if (Computer == 1 and you == -1):
        print("You Win\nComputer Lose")

    elif (Computer == -1 and you == 1):
        print("You Lose\nComputer Win")

    elif (Computer == 1 and you == 0):
        print("You Lose\nComputer Win")

    elif (Computer == -1 and you == 0):
        print("You Lose\nComputer Win")

    elif (Computer == 0 and you == -1):
        print("You Lose\nComputer Win")

    elif (Computer == 0 and you == 1):
        print("You Win\nComputer Lose")

    else:
        print("Something wrong")