numbers = [2, 2, 4, 6, 3, 4, 6, 1]
uniques = []
count = 0
for i in range(0, len(numbers)):
    if numbers[i] not in uniques:
        uniques.append(numbers[i])
uniques.sort()
print(uniques)
