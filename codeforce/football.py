x = input()
k = len(x)
count = 0
for i in range(0, k):
    if(x[i] == "1"):
        count += 1
    elif(x[i] == "0"):
        count = 0
    if(count == 7):
        break

if(count == 7):
    print("YES")
else:
    print("NO")
