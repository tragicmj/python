x = input()
x = list(x)
if(x[0].islower):
    x[0] = x[0].upper()
for i in range(1, len(x)):
    if(x[i].isupper):
        x[i] = x[i].lower()

x = ''.join(map(str, x))

print(x)
