# checking leap year using function
def is_leap(year):
    if year % 4 == 0:
        if year % 400 == 0:
            return True
        elif year % 100 == 0:
            return False

        return True
    else:
        return False

    # Write your logic here


year = int(input())
print(is_leap(year))
