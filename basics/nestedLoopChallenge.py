numbers = [5, 2, 5, 2, 2]
for i in range(0, len(numbers)):
    output = ''
    for j in range(0, numbers[i]):
        output += 'x'
    print(output)
