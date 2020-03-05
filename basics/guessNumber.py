chances = 3
while chances != 0:
    chances -= 1
    x = int(input("Guess Number: "))
    if(x == 9):
        print("You Won!")
        break
else:
    print("Sorry You Failed")
