x = int(input())
result = []
# take array input in a single line
result = list(map(int, input().split()))
for i in range(0, x-1):
    for j in range(0, x-i-1):
        if(result[j] > result[j+1]):
            temp = result[j]
            result[j] = result[j+1]
            result[j+1] = temp

for i in range(0, x-1):
    if(result[i] < result[i+1]):
        k = result[i]

print(k)
