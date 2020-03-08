turns = int(input())
list = []
while turns != 0:
    x = input()
    k = x.split(" ")
    if(k[0].lower() == 'insert'):
        list.insert(int(k[1]), int(k[2]))
    elif(k[0].lower() == 'print'):
        print(list)
    elif(k[0].lower() == 'remove'):
        list.remove(int(k[1]))
    elif(k[0].lower() == 'append'):
        list.append(int(k[1]))
    elif(k[0].lower() == 'sort'):
        list.sort()
    elif(k[0].lower() == 'pop'):
        list.pop()
    elif(k[0].lower() == 'reverse'):
        list.reverse()
    turns -= 1
    k.clear()
