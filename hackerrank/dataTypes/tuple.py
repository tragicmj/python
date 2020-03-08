x = int(input())
y = input()
t = tuple(map(int, y.split(' ')))
print(hash(t))
