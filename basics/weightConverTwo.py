x = int(input())
y = input("(L)bs or (K)g: ")
if(y.lower() == 'l'):
    x = x*0.45
    print(f"You are {x} kilos")
else:
    x = x/0.45
    print(f"You are {x} lbs")
