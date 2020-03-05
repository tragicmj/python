x = input()
count_four = 0
count_seven = 0
error = 0
k = int(0)
for i in range(0, len(x)):
    if(x[i] == '4'):
        count_four += 1
    elif(x[i] == '7'):
        count_seven += 1
    else:
        error = -1
        break
if(error == -1):
    for i in range(0, len(x)):
        if(x[i] == '4' or x[i] == '7'):
            k = k + int(x[i])
        elif(int(x[i]) < 5):
            k = k + 4
        elif(int(x[i]) >= 5):
            k = k + 7
        k = k * 10
    k = int(k/10)
    print(k)

elif(count_seven == count_seven):
    print(x)
