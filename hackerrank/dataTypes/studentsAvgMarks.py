x = int(input())
mydict = {}
for i in range(0, x):
    info = input().split(" ")
    score = list(map(float, info[1:]))
    mydict[info[0]] = sum(score) / float(len(score))


print("%.2f" % round(mydict[input()], 2))
