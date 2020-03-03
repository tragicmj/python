#!/bin/python3
num = input('Enter the integer: ')

if (int(num) % 2) != 0:
    print('Weird')
elif int(num) >= 2 and int(num) <= 5:
    print("Not Weird")
elif int(num) >= 6 and int(num) <= 20:
    print("Weird")
elif int(num) > 20:
    print("Not Weird")
