x = input()
if(x[0].isalpha()):
    k = x[0].capitalize()
    print(k)
    x.replace(x[0], k)

for i in range(0, len(x)):
    if(x[i] == " " and x[i+1].isalpha() == True):

        x.replace(x[i+1], x[i+1].capitalize())
        print(x[i+1])
print(x)
