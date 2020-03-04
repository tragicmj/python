x = int(input())
students = []
for i in range(0, x):
    name = input()
    marks = float(input())
    students.append([name, marks])


for i in range(0, x-1):
    for j in range(0, x-i-1):
        if(students[j][1] > students[j+1][1]):
            temp = students[j]
            students[j] = students[j+1]
            students[j+1] = temp

for i in range(0, x):
    if(students[i][1] != students[i+1][1]):
        second_low = students[i+1][1]
        break

students.sort()
for i in range(0, x):
    if(students[i][1] == second_low):
        print(students[i][0])
